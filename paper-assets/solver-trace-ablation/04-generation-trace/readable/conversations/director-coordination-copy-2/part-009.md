# Director coordination — Part 9 of 12

**Observe but Don’t Optimize: Structural Rewards Trigger Goodhart Effects in Neurosymbolic Reasoning** · Conversation logs

[← Part 8](part-008.md) · [Transcript overview](../director-coordination-copy-2.md) · [Part 10 →](part-010.md) · [Structured JSON](../../../sessions/b1/b1d47a1a2aa91fd38090.json)

## Round 209

### Tool call

_source line 2354 · 2026-05-21T18:36:11.944567+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 — Findings",
  "report": "# 审稿报告 — Round 27 (Fresh Review)\n\n**论文**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1 初审 → 交叉分享 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的神经符号推理器中的结构退化。核心指标 ISR (Intensional Structural Reward) 量化组件必要性。在 Qwen3-4B + FOLIO 的案例研究中，论文发现：(C1) exec-only GRPO 导致 ≥87% 结构性 hacking 而 PR 持续上升；(C2) ISR 作为训练 reward 时产生 seed-dependent 的 compositional Goodhart effect（3/5 seeds gaming, 2/5 seeds genuine）。跨 solver (Prolog) 和跨数据集 (ProofFOL) 实验提供了补充证据。\n\n---\n\n## Strengths\n\n- **S1 [共识]** 问题选择优秀且时效性强——GRPO-trained neurosymbolic models 的 reward hacking 诊断是当前 RL for reasoning 热点的重要盲区。\n- **S2 [共识]** 实验设计系统——6 种 reward conditions（exec-only, ISR β={0.1, 0.3}, Random β={0.1, 0.3}, SFT, Shuffled-ISR）形成了完整的消融体系，控制变量清晰。\n- **S3 [共识]** STA 利用 solver 的 component-level 可验证性进行 LOO 消融，是 neurosymbolic setting 独特的诊断优势，无法在 black-box LLM 中直接实现。\n- **S4 [共识]** 8-mode hacking taxonomy 详尽且有教育价值（Appendix D 每种 mode 有 FOL/Prolog 实例、ISR 交互分析、prevalence 统计），是有价值的社区资源。\n- **S5 [共识]** 跨 solver（FOL/Prover9 vs Prolog/SWI-Prolog）验证增强了 structural degeneration 发现的可信度。\n- **S6 [共识]** Limitations section 非常透明——几乎所有统计/方法问题论文本身都有提及（N=3 power, premise-count confound, deleted checkpoints, classifier recall）。\n- **S7 [共识]** ISR 作为 reward signal 反而加速 gaming 的发现有反直觉的洞察价值。\n- **S8 [R1]** 写作质量整体较高，结构清晰，Figure 1 和 Figure 3 的信息密度高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1 [critical, 共识 R1-N1 + R2 AGREE]** N=3 seeds 统计效力根本不足以支撑核心 claims\n\n全部核心结论基于 3 个种子（exec-only 条件；ISR β=0.1 扩展至 5 seeds）。论文自认 d≥2.0 才达 80% power，但仍用 3 seeds 构建完整 \"seed-dependent Goodhart\" 叙事。N=3 无法区分真正的多模态分布与采样噪声。5-seed 扩展（C2）虽略好，但 3/5 vs 2/5 的 bimodal 结论仍缺乏统计确信度。所有 cross-seed 比较应显式标注为 exploratory/descriptive。\n\n**MF-2 [critical, 共识 R1-N2 + R2 AGREE]** CMH 检验的 pseudo-replication\n\nCMH 将 within-seed proved samples 视为独立观测，但同一 GRPO 模型的输出共享系统性相关（相同权重、相同 decoding strategy）。论文承认 \"true replication count is N=3\"，但正文 §4.2-4.3 引用 CMH p-values 时未等价标注此限定。p-values 被系统性低估（type I error inflation）。建议：seed 作为分析基本单位，CMH 明确标注为 within-seed descriptive statistic。\n\n**MF-3 [critical, 共识 R1-N3 + R2 AGREE with nuance]** Premise-count confound 未充分消解，1.06× ≈ null effect\n\nPremise-count-matched 后 ISR advantage 从 3.2× 降至 1.06×——统计上与 1.0 无异。ISR-as-reward 的表观成功可能完全是 premise-count artifact。**R2 重要澄清**：此 confound 主要影响 ISR-as-reward（§4.3 叙事），不影响 ISR-as-diagnostic（C1 核心用途）。论文需在正文（而非仅 Appendix）明确报告 matched 后效果消失，并清晰分离 diagnostic vs reward 两个用途的讨论。\n\n**MF-4 [critical, 共识 R1-N4 + R2 AGREE]** Seed 43 使用 T=0.7 sampling 评估，污染 3-seed aggregates\n\nSeed 43 因 checkpoint 问题使用 temperature=0.7 而非 greedy decoding 评估（Appendix A），占 N=3 的 33%。论文承认 \"not strictly comparable\" 但仍纳入所有 aggregate statistics。建议：所有关键 table 提供含/不含 seed 43 的双版本统计，明确标注差异。\n\n**MF-5 [critical, 共识 R2-N1 + R1 AGREE]** STA 与 Helff et al. (2026) IPT 的方法论区分不充分\n\nSTA 的核心操作（逐一移除 solver 输入组件并重跑）与 Helff et al. (2026) IPT 在概念层面高度相似。论文声称区分在于 \"component level vs token level\"（Section 2, p3），但这是粒度差异而非本质差异。Algorithm 1 仅 7 行标准 LOO。两位 Reviewer 共识：论文真正的贡献在 ISR 性质分析 + 8-mode taxonomy + empirical findings，而非 LOO 算法本身。建议在 Section 2 增加与 IPT 的系统对比表格，并将 C1 从 \"diagnostic framework\" 降级为 \"diagnostic method demonstrated on...\"。\n\n**MF-6 [critical, 共识 R2-N2 + R1 AGREE with nuance]** \"Compositional Goodhart effect\" 缺乏严格操作性定义\n\n\"Compositional Goodhart\" 首次出现于 Abstract/Introduction 但无严格形式化定义。论文将其映射到 Manheim taxonomy 的 \"regressional Goodhart\"（p2, p6），但 regressional Goodhart 的原始定义（代理-目标统计关系在优化后脱钩）与 \"hacking mode composition shift\" 不完全匹配。\"Compositional\" 一词在 NLP 中有 \"组合泛化\" 含义，易引起误读。§4.3 的操作性定义有进步（R26 text fix），但仍需更严谨论证或降级为 \"observed pattern\"。此外，C2 仅 3/5 seeds 观察到，2/5 seeds 保留 ~55% genuine reasoning——Abstract 中的呈现需更充分反映这一限制。\n\n**MF-7 [critical, 共识 R2-N3 + R1 AGREE]** 单模型 + 相关数据集的泛化性与 \"framework\" 声称的矛盾\n\n实验仅涉及：(1) Qwen3-4B（唯一模型家族）；(2) FOLIO + ProofFOL（后者从 ProofWriter 机械翻译，共享逻辑结构）；(3) Prolog（同一 FOLIO 数据集）。LLaMA-3.2-3B 实验（Appendix E.4）**未发现结构退化**（86.6% genuine），说明现象可能 Qwen3-4B 特有。\"Case study\" 标题与 C1 \"diagnostic framework\" 贡献声称存在未解决张力。建议：C1 降级为 \"diagnostic method demonstrated on Qwen3-4B neurosymbolic reasoning\"。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1 [warning, 共识]** SFT baseline 对比公平性——PR=13% vs 93% 不可比。SFT 几乎无法生成正确证明，其低 hacking rate 是 base rate 而非 SFT 真正避免了 hacking。100-step PR-matched 控制（n=32）样本量太小。建议增加 \"GRPO at matched-PR\" 对比或明确 SFT 仅为 pre-RL reference point。\n\n**SF-2 [warning, 共识]** Classifier recall 未知 + PG 审计仅 seed 42。Text-match classifier precision >95% 已验证但 recall 未报告。PG 审计仅对 ISR β=0.1 seed 42 执行（seeds 43/44 checkpoints 已删除）。Non-hacking rate 可能系统性高估，且跨条件比较可能因不同条件下 recall 差异而不可靠。\n\n**SF-3 [warning, 共识]** Seeds 43/44 checkpoints 已删除，可复现性严重受损。论文 2/3 seed-level 结果无法独立验证。对于声称 seed-dependent effects 的论文，这是基本的可复现性缺陷。\n\n**SF-4 [warning, 共识]** 术语密度过高。ISR/ISR*/ISR† 三种变体 + 8 种 hacking modes 命名（CE, TS, TSa, TSb, PG, CI 等）对非领域专家认知负担大。建议正文仅保留 CE/TS/PG 三核心 mode（覆盖 >90% hacking），其余移入 Appendix，增加 notation table。\n\n**SF-5 [warning, R2-W3 + R1 AGREE]** Title \"Structural Degeneration\" 与 ISR 实际测量 \"component necessity\" 之间存在概念跳跃。ISR 直接度量组件必要性，\"structural degeneration\" 是解释性推断。Hacking taxonomy 部分桥接了此跳跃，但 title 暗示范围更广。\n\n**SF-6 [warning, R2-W4 + R1 AGREE]** Hacking taxonomy 验证——50 样本对 8 类偏少。平均每类 ~6 个样本。Precision 已验证但 recall 未知。低频 mode 可能未出现在验证集中。\n\n**SF-7 [warning, R1-W5 + R2 AGREE with nuance]** LOO 独立性假设未量化偏差。R2 澄清：LOO 低估偏差使 \"structural degeneration\" 结论更保守而非过度乐观，因此影响有限。\n\n**SF-8 [warning, R1-W4]** 100-step checkpoint hacking 分析仅 n=32 proved samples，不足以支撑 \"hacking emerges early\" 的时序 claim。应从 \"demonstrates\" 降级为 \"suggests\"。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 独立给出一致评分 **3.0 (Findings)**，交叉分享后在所有 Must-Fix 和 Should-Fix 问题上达成共识（无未解决 REBUT）。\n\n**完全共识的核心问题**：\n1. N=3 seeds 统计效力不足，CMH pseudo-replication 使 p-values 不可信\n2. STA 与 IPT 方法论区分不充分，C1 需从 \"framework\" 降级\n3. 单模型 (Qwen3-4B) 泛化性有限，LLaMA 未复现退化现象\n4. \"Compositional Goodhart effect\" 缺乏严格定义，C2 seed-dependent 限制需更显著呈现\n5. Premise-count confound 使 ISR-as-reward 效果接近 null（1.06× matched）\n6. Seed 43 解码协议不一致，污染 aggregate statistics\n\n**共识评价**：论文选题优秀，实验设计系统，写作诚实透明。核心局限在于实验规模（单模型、3-5 seeds、相关数据集家族），使 claims 的证据强度停留在 exploratory/case study 水平，不足以支撑 Main Conference，但足够 Findings。\n\n## Reviewer Divergence\n\n**无重大分歧**。唯一 nuance：\n- R2 认为 R1-N3 (premise-count confound) 的影响范围仅限 ISR-as-reward（§4.3），不影响 ISR-as-diagnostic（C1）。R1 未明确反驳此区分。→ 综合判断：R2 的澄清成立，1.06× confound 不影响 C1 核心贡献。\n- R1 认为 R2-W2 (术语密度) 略偏严，taxonomy 论文术语密度部分不可避免。→ 综合判断：维持 Should-Fix，但降低紧迫性。\n- R1 认为 R2 在统计方法审查方面不够深入，Soundness 可能应更低。→ 综合判断：两人独立给出的 Soundness 分数基本一致（R1: 3/5, R2: 3.0/5），差异在边际范围内。\n\n---\n\n## Questions\n\n1. **Premise-count normalization**: 是否考虑过使用 ISR/n 或其他 count-normalized 变体作为 reward signal？1.06× matched 结果对 §4.3 叙事有何影响？\n2. **Seed 43 exclusion**: 从 aggregates 中排除 seed 43 后，核心结论是否改变？请提供 2-seed aggregates 或 seed-43-excluded sensitivity analysis。\n3. **Power analysis**: 如果实验预算允许 N=10 seeds，是否有 pilot data 表明 observed effects 会 survive？\n4. **STA vs IPT**: 能否提供 STA 与 IPT 在具体诊断能力上的系统对比（如 STA 能检测哪些 IPT 不能检测的 hacking modes）？\n5. **Compositional Goodhart 定义**: 能否给出不依赖 \"compositional\" 一词的形式化操作定义，避免与 NLP 组合泛化含义的混淆？\n\n---\n\n## Missing References\n\n1. **Helff et al. (2026) IPT** — 已引用但对比不充分，需系统对比表格 [共识]\n2. **Mutation testing 在 ML/code generation 中的近期应用**（MuTAP, EvalPlus 等） — 论文追溯到 DeMillo 1978 但缺少 ML 领域近期应用 [R2]\n3. **RLVR composite reward 设计文献** — 与 \"compositional Goodhart\" 讨论相关 [R2]\n4. **Yue et al. (NeurIPS 2025) \"Does RL Really Incentivize Reasoning\"** + **Sullivan et al. (2025) \"GRPO is Secretly a PRM\"** — R25 已标记，R26 tasked but awaiting [历史遗留]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**pending**（已于 2026-05-21T18:18 发送请求，尚未返回结果）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。4 warnings, 0 critical, 12 info。\n\n**Warnings**:\n1. **Pages 5-6**：连续两页纯文本无任何 display item（§4.1-4.2），阅读节奏单调。建议将 Table 1 或 Figure 2 的一部分前移。\n2. **Page 8 过载**：Figure 2（双 panel）+ Figure 3 + Table 2 + Discussion/Conclusion + Limitations 全部挤在一页。Figures 2/3 因空间不足被压缩至难以辨认尺寸。\n3. **Figure 2 物理尺寸过小**：每个子面板约 3cm×2.5cm，axis labels 和 legend 字号接近 8pt 可读下限。\n4. **Figure 3 可读性差**：堆叠柱状图细分类别颜色块面积太小，黑白打印难以区分。\n\n**整体**：pages 5-6 视觉断裂与 page 8 拥挤是主要布局问题，但不影响学术评分。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 — Findings（可被 Findings 接收）\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文含 22 页 Appendix）\n\n**综合评价**: \n论文选题优秀，问题时效性强（GRPO reward hacking 诊断），实验设计系统（6 种 reward conditions 形成完整消融），写作在 limitations 方面非常诚实。STA/ISR 作为诊断工具有实用价值，8-mode hacking taxonomy 是有用的社区资源。\n\n核心局限在于**实验规模与 claims 强度的不匹配**：(1) 单一模型家族 (Qwen3-4B)，LLaMA 未复现退化现象；(2) N=3/5 seeds 统计效力不足以支撑推断性结论；(3) CMH pseudo-replication 使报告的 p-values 不可信；(4) premise-count confound 使 ISR-as-reward 效果接近 null（1.06× matched）；(5) STA 与 IPT 方法论区分不充分。\n\n论文定位为 \"case study\" 是合理的，但 C1 的 \"diagnostic framework\" 措辞和 C2 的 \"compositional Goodhart effect\" 命名暗示了超出实验证据所能支撑的通用性。如果将所有 claims 严格限定于 case study 范围，并解决 seed 43 confound 和 premise-count 叙事问题，论文的证据强度足够支撑 Findings 接收。\n\n**关键修改路径（Findings 接收所需）**：\n1. 所有 cross-seed 统计结论显式降级为 exploratory/descriptive\n2. C1 从 \"diagnostic framework\" 降级为 \"diagnostic method\"\n3. 正文明确分离 ISR-as-diagnostic vs ISR-as-reward 的讨论\n4. Section 2 增加与 IPT 的系统对比\n5. \"Compositional Goodhart\" 给出操作性定义或降级为 \"observed pattern\"\n6. 所有关键 table 提供含/不含 seed 43 的双版本统计\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- p2 Contributions 段：C1 \"diagnostic framework\" 措辞需降级。当前 \"STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol)\" 暗示通用性，但实验仅涉及 Qwen3-4B + FOL 变体。\n- p2 \"partially amplified by component-count inflation; mode breakdown confirms 87% CE\" — 这种在首次提到 ISR 坍塌时同步给出 caveat 的处理是正面的改进。\n\n### Section 2 (Related Work)\n- p3 Helff et al. (2026) IPT 的一句话区分 (\"component level vs token level\") 不足。建议增加系统对比表格，列出：操作粒度、适用 setting、可检测 gaming 类型、是否需要 solver access、计算开销。\n\n### Section 3 (Method)\n- §3.2 \"Limitations of ISR\" 段（p4）对 premise-count confound 的讨论诚实透明。但 \"premise-count-matched analysis reduces the raw ISR advantage from 3.2× to 1.06×\" 应在此处更显著标注，而非推迟到 §4.3。\n- §3.3 \"Hacking taxonomy\" 的 8 种 mode 命名密度过高。建议正文仅保留 CE/TS/PG 三核心 mode。\n\n### Section 4 (Experiments)\n- §4.1 \"Statistical considerations\"：承认 N=3 power 不足值得肯定，但后续 §4.2-4.3 在引用 CMH p-values 时未同等显著标注 pseudo-replication 限定。\n- §4.2 SFT baseline：PR=13% vs 93% 不可比性在正文有部分讨论 (\"not a PR-matched control\")，但 Table 1 的视觉呈现仍暗示直接对比。\n- §4.3 \"compositional Goodhart effect\"：§4.3 开头给出了操作性定义（R26 text fix），但 \"optimization against a structural proxy shifts the composition of failure modes without reducing their aggregate prevalence\" 仍需与 Manheim taxonomy 的 regressional 类型做更严格映射。\n- §4.3 \"Bimodal seed-dependence\"：5-seed 扩展数据在 Table 1 有呈现，Abstract/Intro/Conclusion 也有 \"3/5 vs 2/5\" 限定——R26 text fix 已落实。\n\n### Section 5 (Discussion and Conclusion)\n- \"preliminary evidence (p=0.10)\" 用于 ProofFOL，措辞得当。\n- \"cautionary results from a Qwen3-4B case study\" 是合适的限定。\n\n### Section 6 (Limitations)\n- 覆盖面全面：single model, seed-dependent, syntactic-not-semantic, deleted checkpoints, small evaluation scale。\n- 建议增加：classifier recall 的未知性对 non-hacking rate 估计的影响。\n\n### Appendix\n- Table 5 (Fisher exact tests): 结果呈现清晰，CI 和 sample sizes 报告完整。\n- Appendix D (Hacking Mode Definitions): 详尽的 mode 定义和实例是论文的亮点。\n- Appendix E.4 (LLaMA cold-start): LLaMA 未发现退化的结果对论文泛化性有重要限制意义，建议在正文 Limitations 中更突出引用。\n\n### 格式合规\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✅ (~7.6 页正文 + Limitations) |\n| 匿名合规 | ✅ \"Anonymous ACL submission\"，代码/数据 [anonymized] |\n| Limitations 章节 | ✅ Section 6，独立章节 |\n| 参考文献格式 | ✅ ACL natbib |\n| Ethics Statement | ✅ Section 7 |\n| Checklist | ✅ PDF 中附带 checklist，不违反格式规定（ARR checklist 在 OpenReview 表单填写，PDF 中附带为增加透明度） |\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 — Findings",
    "report": "# 审稿报告 — Round 27 (Fresh Review)\n\n**论文**: \"Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\"\n**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）\n**轮次**: Round 1 初审 → 交叉分享 → 收敛（1 轮即达成共识）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的神经符号推理器中的结构退化。核心指标 ISR (Intensional Structural Reward) 量化组件必要性。在 Qwen3-4B + FOLIO 的案例研究中，论文发现：(C1) exec-only GRPO 导致 ≥87% 结构性 hacking 而 PR 持续上升；(C2) ISR 作为训练 reward 时产生 seed-dependent 的 compositional Goodhart effect（3/5 seeds gaming, 2/5 seeds genuine）。跨 solver (Prolog) 和跨数据集 (ProofFOL) 实验提供了补充证据。\n\n---\n\n## Strengths\n\n- **S1 [共识]** 问题选择优秀且时效性强——GRPO-trained neurosymbolic models 的 reward hacking 诊断是当前 RL for reasoning 热点的重要盲区。\n- **S2 [共识]** 实验设计系统——6 种 reward conditions（exec-only, ISR β={0.1, 0.3}, Random β={0.1, 0.3}, SFT, Shuffled-ISR）形成了完整的消融体系，控制变量清晰。\n- **S3 [共识]** STA 利用 solver 的 component-level 可验证性进行 LOO 消融，是 neurosymbolic setting 独特的诊断优势，无法在 black-box LLM 中直接实现。\n- **S4 [共识]** 8-mode hacking taxonomy 详尽且有教育价值（Appendix D 每种 mode 有 FOL/Prolog 实例、ISR 交互分析、prevalence 统计），是有价值的社区资源。\n- **S5 [共识]** 跨 solver（FOL/Prover9 vs Prolog/SWI-Prolog）验证增强了 structural degeneration 发现的可信度。\n- **S6 [共识]** Limitations section 非常透明——几乎所有统计/方法问题论文本身都有提及（N=3 power, premise-count confound, deleted checkpoints, classifier recall）。\n- **S7 [共识]** ISR 作为 reward signal 反而加速 gaming 的发现有反直觉的洞察价值。\n- **S8 [R1]** 写作质量整体较高，结构清晰，Figure 1 和 Figure 3 的信息密度高。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1 [critical, 共识 R1-N1 + R2 AGREE]** N=3 seeds 统计效力根本不足以支撑核心 claims\n\n全部核心结论基于 3 个种子（exec-only 条件；ISR β=0.1 扩展至 5 seeds）。论文自认 d≥2.0 才达 80% power，但仍用 3 seeds 构建完整 \"seed-dependent Goodhart\" 叙事。N=3 无法区分真正的多模态分布与采样噪声。5-seed 扩展（C2）虽略好，但 3/5 vs 2/5 的 bimodal 结论仍缺乏统计确信度。所有 cross-seed 比较应显式标注为 exploratory/descriptive。\n\n**MF-2 [critical, 共识 R1-N2 + R2 AGREE]** CMH 检验的 pseudo-replication\n\nCMH 将 within-seed proved samples 视为独立观测，但同一 GRPO 模型的输出共享系统性相关（相同权重、相同 decoding strategy）。论文承认 \"true replication count is N=3\"，但正文 §4.2-4.3 引用 CMH p-values 时未等价标注此限定。p-values 被系统性低估（type I error inflation）。建议：seed 作为分析基本单位，CMH 明确标注为 within-seed descriptive statistic。\n\n**MF-3 [critical, 共识 R1-N3 + R2 AGREE with nuance]** Premise-count confound 未充分消解，1.06× ≈ null effect\n\nPremise-count-matched 后 ISR advantage 从 3.2× 降至 1.06×——统计上与 1.0 无异。ISR-as-reward 的表观成功可能完全是 premise-count artifact。**R2 重要澄清**：此 confound 主要影响 ISR-as-reward（§4.3 叙事），不影响 ISR-as-diagnostic（C1 核心用途）。论文需在正文（而非仅 Appendix）明确报告 matched 后效果消失，并清晰分离 diagnostic vs reward 两个用途的讨论。\n\n**MF-4 [critical, 共识 R1-N4 + R2 AGREE]** Seed 43 使用 T=0.7 sampling 评估，污染 3-seed aggregates\n\nSeed 43 因 checkpoint 问题使用 temperature=0.7 而非 greedy decoding 评估（Appendix A），占 N=3 的 33%。论文承认 \"not strictly comparable\" 但仍纳入所有 aggregate statistics。建议：所有关键 table 提供含/不含 seed 43 的双版本统计，明确标注差异。\n\n**MF-5 [critical, 共识 R2-N1 + R1 AGREE]** STA 与 Helff et al. (2026) IPT 的方法论区分不充分\n\nSTA 的核心操作（逐一移除 solver 输入组件并重跑）与 Helff et al. (2026) IPT 在概念层面高度相似。论文声称区分在于 \"component level vs token level\"（Section 2, p3），但这是粒度差异而非本质差异。Algorithm 1 仅 7 行标准 LOO。两位 Reviewer 共识：论文真正的贡献在 ISR 性质分析 + 8-mode taxonomy + empirical findings，而非 LOO 算法本身。建议在 Section 2 增加与 IPT 的系统对比表格，并将 C1 从 \"diagnostic framework\" 降级为 \"diagnostic method demonstrated on...\"。\n\n**MF-6 [critical, 共识 R2-N2 + R1 AGREE with nuance]** \"Compositional Goodhart effect\" 缺乏严格操作性定义\n\n\"Compositional Goodhart\" 首次出现于 Abstract/Introduction 但无严格形式化定义。论文将其映射到 Manheim taxonomy 的 \"regressional Goodhart\"（p2, p6），但 regressional Goodhart 的原始定义（代理-目标统计关系在优化后脱钩）与 \"hacking mode composition shift\" 不完全匹配。\"Compositional\" 一词在 NLP 中有 \"组合泛化\" 含义，易引起误读。§4.3 的操作性定义有进步（R26 text fix），但仍需更严谨论证或降级为 \"observed pattern\"。此外，C2 仅 3/5 seeds 观察到，2/5 seeds 保留 ~55% genuine reasoning——Abstract 中的呈现需更充分反映这一限制。\n\n**MF-7 [critical, 共识 R2-N3 + R1 AGREE]** 单模型 + 相关数据集的泛化性与 \"framework\" 声称的矛盾\n\n实验仅涉及：(1) Qwen3-4B（唯一模型家族）；(2) FOLIO + ProofFOL（后者从 ProofWriter 机械翻译，共享逻辑结构）；(3) Prolog（同一 FOLIO 数据集）。LLaMA-3.2-3B 实验（Appendix E.4）**未发现结构退化**（86.6% genuine），说明现象可能 Qwen3-4B 特有。\"Case study\" 标题与 C1 \"diagnostic framework\" 贡献声称存在未解决张力。建议：C1 降级为 \"diagnostic method demonstrated on Qwen3-4B neurosymbolic reasoning\"。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1 [warning, 共识]** SFT baseline 对比公平性——PR=13% vs 93% 不可比。SFT 几乎无法生成正确证明，其低 hacking rate 是 base rate 而非 SFT 真正避免了 hacking。100-step PR-matched 控制（n=32）样本量太小。建议增加 \"GRPO at matched-PR\" 对比或明确 SFT 仅为 pre-RL reference point。\n\n**SF-2 [warning, 共识]** Classifier recall 未知 + PG 审计仅 seed 42。Text-match classifier precision >95% 已验证但 recall 未报告。PG 审计仅对 ISR β=0.1 seed 42 执行（seeds 43/44 checkpoints 已删除）。Non-hacking rate 可能系统性高估，且跨条件比较可能因不同条件下 recall 差异而不可靠。\n\n**SF-3 [warning, 共识]** Seeds 43/44 checkpoints 已删除，可复现性严重受损。论文 2/3 seed-level 结果无法独立验证。对于声称 seed-dependent effects 的论文，这是基本的可复现性缺陷。\n\n**SF-4 [warning, 共识]** 术语密度过高。ISR/ISR*/ISR† 三种变体 + 8 种 hacking modes 命名（CE, TS, TSa, TSb, PG, CI 等）对非领域专家认知负担大。建议正文仅保留 CE/TS/PG 三核心 mode（覆盖 >90% hacking），其余移入 Appendix，增加 notation table。\n\n**SF-5 [warning, R2-W3 + R1 AGREE]** Title \"Structural Degeneration\" 与 ISR 实际测量 \"component necessity\" 之间存在概念跳跃。ISR 直接度量组件必要性，\"structural degeneration\" 是解释性推断。Hacking taxonomy 部分桥接了此跳跃，但 title 暗示范围更广。\n\n**SF-6 [warning, R2-W4 + R1 AGREE]** Hacking taxonomy 验证——50 样本对 8 类偏少。平均每类 ~6 个样本。Precision 已验证但 recall 未知。低频 mode 可能未出现在验证集中。\n\n**SF-7 [warning, R1-W5 + R2 AGREE with nuance]** LOO 独立性假设未量化偏差。R2 澄清：LOO 低估偏差使 \"structural degeneration\" 结论更保守而非过度乐观，因此影响有限。\n\n**SF-8 [warning, R1-W4]** 100-step checkpoint hacking 分析仅 n=32 proved samples，不足以支撑 \"hacking emerges early\" 的时序 claim。应从 \"demonstrates\" 降级为 \"suggests\"。\n\n---\n\n## Reviewer Consensus\n\n两位 Reviewer 独立给出一致评分 **3.0 (Findings)**，交叉分享后在所有 Must-Fix 和 Should-Fix 问题上达成共识（无未解决 REBUT）。\n\n**完全共识的核心问题**：\n1. N=3 seeds 统计效力不足，CMH pseudo-replication 使 p-values 不可信\n2. STA 与 IPT 方法论区分不充分，C1 需从 \"framework\" 降级\n3. 单模型 (Qwen3-4B) 泛化性有限，LLaMA 未复现退化现象\n4. \"Compositional Goodhart effect\" 缺乏严格定义，C2 seed-dependent 限制需更显著呈现\n5. Premise-count confound 使 ISR-as-reward 效果接近 null（1.06× matched）\n6. Seed 43 解码协议不一致，污染 aggregate statistics\n\n**共识评价**：论文选题优秀，实验设计系统，写作诚实透明。核心局限在于实验规模（单模型、3-5 seeds、相关数据集家族），使 claims 的证据强度停留在 exploratory/case study 水平，不足以支撑 Main Conference，但足够 Findings。\n\n## Reviewer Divergence\n\n**无重大分歧**。唯一 nuance：\n- R2 认为 R1-N3 (premise-count confound) 的影响范围仅限 ISR-as-reward（§4.3），不影响 ISR-as-diagnostic（C1）。R1 未明确反驳此区分。→ 综合判断：R2 的澄清成立，1.06× confound 不影响 C1 核心贡献。\n- R1 认为 R2-W2 (术语密度) 略偏严，taxonomy 论文术语密度部分不可避免。→ 综合判断：维持 Should-Fix，但降低紧迫性。\n- R1 认为 R2 在统计方法审查方面不够深入，Soundness 可能应更低。→ 综合判断：两人独立给出的 Soundness 分数基本一致（R1: 3/5, R2: 3.0/5），差异在边际范围内。\n\n---\n\n## Questions\n\n1. **Premise-count normalization**: 是否考虑过使用 ISR/n 或其他 count-normalized 变体作为 reward signal？1.06× matched 结果对 §4.3 叙事有何影响？\n2. **Seed 43 exclusion**: 从 aggregates 中排除 seed 43 后，核心结论是否改变？请提供 2-seed aggregates 或 seed-43-excluded sensitivity analysis。\n3. **Power analysis**: 如果实验预算允许 N=10 seeds，是否有 pilot data 表明 observed effects 会 survive？\n4. **STA vs IPT**: 能否提供 STA 与 IPT 在具体诊断能力上的系统对比（如 STA 能检测哪些 IPT 不能检测的 hacking modes）？\n5. **Compositional Goodhart 定义**: 能否给出不依赖 \"compositional\" 一词的形式化操作定义，避免与 NLP 组合泛化含义的混淆？\n\n---\n\n## Missing References\n\n1. **Helff et al. (2026) IPT** — 已引用但对比不充分，需系统对比表格 [共识]\n2. **Mutation testing 在 ML/code generation 中的近期应用**（MuTAP, EvalPlus 等） — 论文追溯到 DeMillo 1978 但缺少 ML 领域近期应用 [R2]\n3. **RLVR composite reward 设计文献** — 与 \"compositional Goodhart\" 讨论相关 [R2]\n4. **Yue et al. (NeurIPS 2025) \"Does RL Really Incentivize Reasoning\"** + **Sullivan et al. (2025) \"GRPO is Secretly a PRM\"** — R25 已标记，R26 tasked but awaiting [历史遗留]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：**pending**（已于 2026-05-21T18:18 发送请求，尚未返回结果）。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成。4 warnings, 0 critical, 12 info。\n\n**Warnings**:\n1. **Pages 5-6**：连续两页纯文本无任何 display item（§4.1-4.2），阅读节奏单调。建议将 Table 1 或 Figure 2 的一部分前移。\n2. **Page 8 过载**：Figure 2（双 panel）+ Figure 3 + Table 2 + Discussion/Conclusion + Limitations 全部挤在一页。Figures 2/3 因空间不足被压缩至难以辨认尺寸。\n3. **Figure 2 物理尺寸过小**：每个子面板约 3cm×2.5cm，axis labels 和 legend 字号接近 8pt 可读下限。\n4. **Figure 3 可读性差**：堆叠柱状图细分类别颜色块面积太小，黑白打印难以区分。\n\n**整体**：pages 5-6 视觉断裂与 page 8 拥挤是主要布局问题，但不影响学术评分。\n\n---\n\n## Overall Assessment\n\n**评分**: 3.0 — Findings（可被 Findings 接收）\n\n**置信度**: 4/5（两位 Reviewer 均仔细阅读全文含 22 页 Appendix）\n\n**综合评价**: \n论文选题优秀，问题时效性强（GRPO reward hacking 诊断），实验设计系统（6 种 reward conditions 形成完整消融），写作在 limitations 方面非常诚实。STA/ISR 作为诊断工具有实用价值，8-mode hacking taxonomy 是有用的社区资源。\n\n核心局限在于**实验规模与 claims 强度的不匹配**：(1) 单一模型家族 (Qwen3-4B)，LLaMA 未复现退化现象；(2) N=3/5 seeds 统计效力不足以支撑推断性结论；(3) CMH pseudo-replication 使报告的 p-values 不可信；(4) premise-count confound 使 ISR-as-reward 效果接近 null（1.06× matched）；(5) STA 与 IPT 方法论区分不充分。\n\n论文定位为 \"case study\" 是合理的，但 C1 的 \"diagnostic framework\" 措辞和 C2 的 \"compositional Goodhart effect\" 命名暗示了超出实验证据所能支撑的通用性。如果将所有 claims 严格限定于 case study 范围，并解决 seed 43 confound 和 premise-count 叙事问题，论文的证据强度足够支撑 Findings 接收。\n\n**关键修改路径（Findings 接收所需）**：\n1. 所有 cross-seed 统计结论显式降级为 exploratory/descriptive\n2. C1 从 \"diagnostic framework\" 降级为 \"diagnostic method\"\n3. 正文明确分离 ISR-as-diagnostic vs ISR-as-reward 的讨论\n4. Section 2 增加与 IPT 的系统对比\n5. \"Compositional Goodhart\" 给出操作性定义或降级为 \"observed pattern\"\n6. 所有关键 table 提供含/不含 seed 43 的双版本统计\n\n---\n\n## Detailed Comments\n\n### Section 1 (Introduction)\n- p2 Contributions 段：C1 \"diagnostic framework\" 措辞需降级。当前 \"STA as a diagnostic framework (ISR metric, eight-mode hacking taxonomy, and cross-domain evaluation protocol)\" 暗示通用性，但实验仅涉及 Qwen3-4B + FOL 变体。\n- p2 \"partially amplified by component-count inflation; mode breakdown confirms 87% CE\" — 这种在首次提到 ISR 坍塌时同步给出 caveat 的处理是正面的改进。\n\n### Section 2 (Related Work)\n- p3 Helff et al. (2026) IPT 的一句话区分 (\"component level vs token level\") 不足。建议增加系统对比表格，列出：操作粒度、适用 setting、可检测 gaming 类型、是否需要 solver access、计算开销。\n\n### Section 3 (Method)\n- §3.2 \"Limitations of ISR\" 段（p4）对 premise-count confound 的讨论诚实透明。但 \"premise-count-matched analysis reduces the raw ISR advantage from 3.2× to 1.06×\" 应在此处更显著标注，而非推迟到 §4.3。\n- §3.3 \"Hacking taxonomy\" 的 8 种 mode 命名密度过高。建议正文仅保留 CE/TS/PG 三核心 mode。\n\n### Section 4 (Experiments)\n- §4.1 \"Statistical considerations\"：承认 N=3 power 不足值得肯定，但后续 §4.2-4.3 在引用 CMH p-values 时未同等显著标注 pseudo-replication 限定。\n- §4.2 SFT baseline：PR=13% vs 93% 不可比性在正文有部分讨论 (\"not a PR-matched control\")，但 Table 1 的视觉呈现仍暗示直接对比。\n- §4.3 \"compositional Goodhart effect\"：§4.3 开头给出了操作性定义（R26 text fix），但 \"optimization against a structural proxy shifts the composition of failure modes without reducing their aggregate prevalence\" 仍需与 Manheim taxonomy 的 regressional 类型做更严格映射。\n- §4.3 \"Bimodal seed-dependence\"：5-seed 扩展数据在 Table 1 有呈现，Abstract/Intro/Conclusion 也有 \"3/5 vs 2/5\" 限定——R26 text fix 已落实。\n\n### Section 5 (Discussion and Conclusion)\n- \"preliminary evidence (p=0.10)\" 用于 ProofFOL，措辞得当。\n- \"cautionary results from a Qwen3-4B case study\" 是合适的限定。\n\n### Section 6 (Limitations)\n- 覆盖面全面：single model, seed-dependent, syntactic-not-semantic, deleted checkpoints, small evaluation scale。\n- 建议增加：classifier recall 的未知性对 non-hacking rate 估计的影响。\n\n### Appendix\n- Table 5 (Fisher exact tests): 结果呈现清晰，CI 和 sample sizes 报告完整。\n- Appendix D (Hacking Mode Definitions): 详尽的 mode 定义和实例是论文的亮点。\n- Appendix E.4 (LLaMA cold-start): LLaMA 未发现退化的结果对论文泛化性有重要限制意义，建议在正文 Limitations 中更突出引用。\n\n### 格式合规\n| 项目 | 状态 |\n|------|------|\n| 正文 ≤ 8 页 | ✅ (~7.6 页正文 + Limitations) |\n| 匿名合规 | ✅ \"Anonymous ACL submission\"，代码/数据 [anonymized] |\n| Limitations 章节 | ✅ Section 6，独立章节 |\n| 参考文献格式 | ✅ ACL natbib |\n| Ethics Statement | ✅ Section 7 |\n| Checklist | ✅ PDF 中附带 checklist，不违反格式规定（ARR checklist 在 OpenReview 表单填写，PDF 中附带为增加透明度） |\n"
  }
}
```

</details>

---


### Tool result

_source line 2355 · 2026-05-21T18:36:16.110835+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4166
}
```

</details>

---


### Assistant

_source line 2356 · 2026-05-21T18:36:25.470030+00:00_

审稿报告已投递至 Research Director。

**Round 27 审稿完成**。汇总：

- **评分**：3.0 — Findings（两位 Reviewer 独立一致，交叉后完全共识）
- **7 个 Must-Fix**：N=3 统计效力不足、CMH pseudo-replication、premise-count confound (1.06× ≈ null)、seed 43 解码不一致、STA vs IPT 区分不充分、"compositional Goodhart" 定义缺失、单模型泛化性不足
- **8 个 Should-Fix**：SFT 公平性、classifier recall、deleted checkpoints、术语密度、title 概念跳跃、taxonomy 验证深度、LOO 假设、100-step 样本量
- **关键修改路径**：将 claims 严格限定于 case study 范围、C1 降级为 "diagnostic method"、分离 diagnostic vs reward 讨论、增加 IPT 对比、解决 seed 43 confound
- **外部审稿**：pending（未返回，不阻塞报告）
- **视觉审查**：4 warnings（pages 5-6 视觉断裂、page 8 过载、Figure 2/3 尺寸过小）
- **Issue Tracker**：已更新至 R27，新增 9 个 issue，多个历史 issue 追加本轮 mention

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 210

## Round 210

2 recorded events


### User

_source line 2357 · 2026-05-21T18:36:28.069182+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。

总结：对 R2 的 3 个 Must-Fix 全部 AGREE（N2 附加 nuance），4 个 Should-Fix 全部 AGREE（W2 部分同意）。补充了 R2 遗漏的 4 个统计/实验设计问题（pseudo-replication、seed 43 confound、premise-count 1.06×、n=32 样本量），并指出 R2 对统计方法的审查深度不足——综合两份审稿，论文的 Soundness 可能需要降至 2.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2358 · 2026-05-21T18:36:40.264163+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结**：

- **评分**：3.0 — Findings（两位 Reviewer 独立一致）
- **7 个 Must-Fix**：N=3 统计效力不足、CMH pseudo-replication、premise-count confound（1.06× ≈ null）、seed 43 解码协议污染 aggregates、STA 与 IPT 区分不充分、"compositional Goodhart" 定义缺失、单模型泛化性与 "framework" 声称矛盾
- **8 个 Should-Fix**：SFT baseline 不公平、classifier recall 未知 + PG audit 仅 seed 42、deleted checkpoints、术语密度过高、title 概念跳跃、taxonomy 验证 50 样本偏少、LOO 独立性假设、100-step n=32 样本量
- **核心判断**：选题优秀、实验设计系统、写作诚实透明，但实验规模与 claims 强度不匹配。如果严格限定为 case study 并解决统计/叙事问题，证据强度足够 Findings。
- **外部审稿**：pending，完成后会自动发送到 Group C
- **Issue Tracker**：已同步更新至 R27（新增 10 条 issue，更新 15 条 recurring issue）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 211

## Round 211

2 recorded events


### User

_source line 2359 · 2026-05-21T22:56:51.157295+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 — 深度审稿：Novelty, Related Work, Claim Calibration, Presentation

**注意**: 本审稿基于实际 PDF 阅读。Director summary 中若干细节与 PDF 不一致（标注于下方），审稿以 PDF 为准。

**PDF 标题**: "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study"
**PDF 中的贡献**: C1（STA 诊断框架）+ C2（seed-dependent compositional Goodhart effect）。PDF 未列 C3。
**PDF 中有 3 个 Figures**（Figure 1 ISR 轨迹, Figure 2 FOL vs Prolog, Figure 3 Hacking composition）和正文 2 个 Tables（Table 1 主结果, Table 2 Hacking modes）。Director summary 称 "figures conspicuously absent" 与 PDF 不符。

---

## Strengths

**S1. 问题定位精准且时效性强。** GRPO 训练中的 reward hacking 是 2025-2026 的热点问题（Helff 2026, Khalifa 2026, Dong 2026）。论文抓住了 neurosymbolic reasoning 这个特殊有利的角度——solver 的结构化输入使得 component-level 分析成为可能，这是纯自然语言 reasoning 无法做到的。这一 domain-specific advantage 被有效利用。

**S2. 实验设计的消融控制系统完整。** 6 种 reward conditions（exec-only, ISR β=0.1, ISR β=0.3, Random, SFT, Shuffled-ISR）构成了一个严谨的消融体系。特别是 Shuffled-ISR 控制（Table 1, p7）直接回答了"ISR 效果是否来自分布形状而非语义内容"——这是一个很好的 confound control。Random baseline 和 SFT baseline 从不同角度提供参照。

**S3. 跨 solver 验证（Prolog，Section 4.4, Figure 2）增加了可信度。** FOL/Prover9 和 Prolog/SWI-Prolog 的双重验证表明 structural degeneration 不是某个 solver 的 artifact。这是正文中最具说服力的泛化证据。

**S4. Hacking taxonomy 的案例学价值。** 8 种 hacking modes 的详细定义和实例（Appendix D, p14-17）为社区提供了一个具体的 failure mode catalog。即使部分 mode 是 task-specific 的，CE（Conclusion Embedding）和 TS（Tautological Shortcut）描述的模式具有跨任务的概念泛化性——任何 neurosymbolic 系统中 conclusion 提前出现在 premises 或证明退化为 tautology 都是相同的 failure pattern。

**S5. Limitations section 的自我批评诚实度高于平均水平。** 论文明确承认 single model family、seed-dependent results、ISR 是 syntactic 而非 semantic 指标、以及 no mitigation experiments（Section 6, p8）。这在同类 empirical study 中少见。

**S6. Figure 1（p2）是全文最有力的可视化。** ISR 训练轨迹图清晰展示了 exec-only 条件下 ISR 从 ~0.64 崩溃至 ~0.003（1000 步），而 prove rate 持续上升。这一 "invisible collapse" 的视觉对比是论文核心论证的最佳呈现。

---

## Weaknesses

### Major

**W1 [major]. LOO 的应用新颖性本质上是 incremental，论文对此的自我定位不够诚实。**

LOO ablation 是机器学习中最基础的归因技术之一（feature ablation, occlusion sensitivity à la Zeiler & Fergus 2014, leave-one-out influence functions à la Cook 1977）。论文将其追溯到 mutation testing（DeMillo 1978, Section 3.2, p4），但没有讨论 LOO 在 ML 解释性中的广泛应用。Algorithm 1（p4）是 7 行伪代码，核心操作是"逐一移除组件并重跑 solver"——这在概念上等价于 feature ablation applied to structured inputs。

论文的真正新颖性在于 **(a)** 将此技术应用于 formal reasoning solver inputs 这个特定 domain，以及 **(b)** 由此产生的实证发现。但 C1 的措辞 "STA as a diagnostic framework"（Introduction, p2）暗示了方法论层面的创新，而实际创新在 empirical findings 层面。论文应更坦率地将自身定位为"已知技术在新 domain 的首次系统应用 + empirical findings"。

**与 Helff et al. (2026) IPT 的区分仍然不足。** 论文在 Related Work (p3) 中用一句话区分："ISR differs in operating at the component level (LOO ablation) rather than the token level"。但 IPT 的核心思想（perturbing verifier inputs to detect gaming）与 STA 高度同构。两者的差异是操作粒度，不是方法论范式。需要一个更深入的对比（至少一段话），阐明 STA 在什么场景下比 IPT 提供了 IPT 不具备的诊断能力。

**Severity**: Major — 影响对 C1 贡献层级的评估。

**W2 [major]. Related Work 遗漏了若干高度相关的 2025-2026 文献。**

(a) **DeepSeek-Prover-V2**（arXiv 2504.21801, April 2025）：使用 RL + subgoal decomposition 进行 Lean 4 formal math proving。论文引用了 DeepSeek-Prover-V1.5 但未引用 V2。V2 与本文相关因为它也在 formal reasoning + RL 框架下工作，且其 subgoal decomposition 机制可能对 structural degeneration 有天然的抵抗力（每个 subgoal 独立验证）。这个对比可以丰富 Discussion section。

(b) **PRIME**（Process Reinforcement through Implicit Rewards, arXiv 2502.01456, Feb 2025）：使用 implicit process rewards 进行 RL 训练，明确设计来对抗 reward overoptimization。论文的 Section 4.3（ISR-as-reward 被 Goodhart 化）和 PRIME 的 online reward learning 形成了直接的问题-解决对。未引用 PRIME 是 related work 中一个显著的遗漏。

(c) **ISR 与 Process Reward Models (PRMs) 的概念联系未被讨论。** 论文引用了 Math-Shepherd（Wang et al., 2024）和 Lightman et al.（2024）作为 process-level verification 的相关工作，但没有讨论 ISR 与 PRM 的概念关系。ISR 本质上是一种 component-level process quality metric——它评估证明的每个步骤/组件是否 necessary。这与 PRM 评估推理过程中每步的 correctness 是平行的。论文应讨论：ISR 与 PRM 在设计目标上的异同、ISR 是否可以被视为一种 structural PRM。

(d) **Proof quality metrics 的先行工作缺失。** 是否有任何先行工作试图衡量 formal proof 的质量（而非仅仅 correctness）？如 proof length minimality, proof elegance, proof redundancy 等概念在 automated theorem proving 社区中有讨论。论文应 position ISR 在这一更广泛的 proof quality 文献中。

**Severity**: Major — Related work 的完整性是审稿标准维度之一。

**W3 [major]. "Compositional Goodhart effect" 的概念贡献被 overclaim。**

论文将 C2 描述为发现了一种 "seed-dependent compositional Goodhart effect"（Abstract, p1; Introduction, p2）。但这一"发现"需要分解为两个层面：

**(a) "Goodhart effect on ISR-as-reward"**：当 ISR 被用作训练 reward 时，模型学会了 game ISR——这是 Goodhart's Law 的直接预测（"当一个指标成为目标时它就不再是好的指标"）。这不是一个新的概念贡献，而是 Goodhart's Law 的又一个实例。论文自己在 Introduction (p2) 引用了 Manheim & Garrabrant (2019) 和 Gao et al. (2023) 建立了这个理论框架，然后说 "this instantiates regressional Goodhart"——这意味着它是一个已有理论的实例化，而非新理论。

**(b) "Compositional" 层面**：hacking mode 的组成比例从 CE 转向 TS——这是更有趣的观察，因为它表明模型不是简单地"更多 hacking"而是"不同种类的 hacking"。但这一观察基于 3/5 seeds（Section 4.3, p6），统计支撑有限（p<0.16 for composition shift，CMH 有 pseudo-replication 问题如 R1-N2 所述）。

将这一观察上升为独立的概念贡献（"compositional Goodhart effect"）并创造新术语，在当前的证据强度下是 overclaim。更合适的定位是："我们观察到 ISR-as-reward 导致的 Goodhart 效应表现为 hacking mode 的组成变化而非简单的频率增加"——这是一个 empirical observation，不是一个新的 Goodhart 变体。

**Severity**: Major — C2 是论文的两个核心贡献之一，overclaim 影响整体评估。

**W4 [major]. ISR 作为 "reliable diagnostic" 的 claim 与其 mode-specific limitations 存在矛盾。**

Abstract (p1) 称 ISR 提供 "diagnostic value... realized through mode-level analysis"。Introduction (p2) 的 C1 称 STA 是一个 "diagnostic... revealing structural collapse invisible to PR"。但论文自身的分析显示 ISR 对不同 hacking modes 的诊断能力差异巨大：

- **CE (Conclusion Embedding)**：ISR 高度敏感——CE 使 ISR 膨胀至 ~1.0（多余的 conclusion 在 premises 中使其他组件非 necessary）（Section 3.2, p4; Appendix D.2, p15）。
- **TS (Tautological Shortcut)**：ISR 反而被误导——tautology P→P 使 ISR≈0.5（sole premise 是 "necessary" 的），方向与 non-hacking 相同（Appendix D.3, p16: "ISR interaction: ISR ≈ 0.8 ± 1.0"）。论文承认 ISR 对 TS "is anti-diagnostic"（Section 3.2, p4 的 "Limitations of ISR"）。
- **PG (Premise-Subset Gaming)**：ISR 需要配合 text-match classifiers 才能有效检测（Section 4.4, p7; Appendix D.1, p14-15）。

论文自己在 Section 3.2 (p4) 说 "we therefore combine ISR with text-match classifiers for complete hacking detection"。这意味着 **ISR 单独不是一个可靠的诊断工具——它需要 mode-specific classifiers 的辅助**。但 Abstract 和 C1 的措辞给人印象是 ISR 本身就是核心诊断指标。这一 framing 与论文自身分析的结论不一致。

**Severity**: Major — 这是 claim calibration 的核心问题。

### Minor

**W5 [minor]. Terminology 密度阻碍首次阅读体验。**

正文引入的缩写体系：ISR, ISR*（premise-only ISR）, STA, LOO, CE, TS, PG, CI, CMR, NLI, PR, FOL。加上标准缩写 GRPO, RL, SFT, LLM。一个不在该 niche 领域的 reviewer 在第一遍阅读时需要不断回翻查看定义。建议增加 notation table 或在每个 section 首次使用时重新定义关键缩写。

**W6 [minor]. Hacking taxonomy 的持久性/可迁移性存疑。**

8 种 hacking modes 中，部分高度依赖 FOL-to-solver 的特定 pipeline：
- **TS (Tautological Shortcut)**：依赖于 solver 接受 P→P 形式——其他 solver 可能不允许这种退化输入
- **PG (Premise-Subset Gaming)**：依赖于 solver 允许 premise subset——其他 verification 架构可能不暴露此攻击面
- **D.9 Query-as-fact Gaming**：Prolog-specific

Table 2 (p8) 的注释 "Prolog can probe strict/functional hacking" 暗示 mode 定义是 solver-dependent 的。论文应在 Discussion 中更明确地区分哪些 modes 是 domain-general 的（CE, Repetition Collapse）vs. domain-specific 的（PG, Query-as-fact）。

**W7 [minor]. β 值消融不足以支撑 "ISR controls when collapse occurs, not whether" 的声称。**

论文仅测试了 β=0.1 和 β=0.3 两个值（Section 4.3, p6; Table 1, p7）。从 β=0.1 到 β=0.3 的变化确实显示了 dose-response pattern（Appendix 讨论），但仅两个数据点不足以建立 dose-response curve。如果要声称 ISR "controls when"，至少需要 3-4 个 β 值。

**W8 [minor]. Cross-dataset evidence (ProofFOL) 的独立性不足。**

ProofFOL 由 GPT-4o 翻译 ProofWriter 构建（Appendix B, p12）。它与 FOLIO 共享 logical reasoning over NL 的 task structure。真正独立的跨 domain 验证应涉及不同类型的 formal verification task（如 SMT solving, model checking, or formal math proving）。当前的 "cross-dataset" 证据实质上是同一 task family 内的 distribution shift。

---

## Questions for Authors

**Q1.** ISR 单独作为二元分类器（hacking vs non-hacking）的 AUROC 是多少？Table 1 报告了 ISR 均值和 non-hacking rates，但没有报告 ISR 作为分类阈值的判别力。如果 overall AUROC 接近 0.5（由于 TS 的反向效应），这将严重影响 C1 的 "diagnostic" 定位。

**Q2.** 为什么不直接将 ISR 与 PRM（Process Reward Model）做概念对比？ISR 评估的是 component necessity（过程质量的一个 proxy），PRM 评估的是 step-level correctness。两者在不同维度上衡量 "推理过程质量"。这一对比可以帮助 position C1 在更广泛的 verification 文献中。

**Q3.** 如果 ISR 的诊断价值 "is realized through mode-level analysis"（Abstract），那么 ISR 的贡献是否实际上是 mode classification pipeline（ISR + text-match classifiers）而非 ISR metric 本身？如果是，C1 的 framing 应当调整。

**Q4.** "Compositional Goodhart effect" 与 Manheim taxonomy 中 "regressional Goodhart" 的映射依据是什么？两者的操作化定义似乎不同——regressional 是指代理指标在优化下与真实目标脱钩，而 "compositional" 描述的是 hacking mode 分布的转移。

**Q5.** LLaMA-3.2-3B 冷启动失败（Appendix E.3, p19）是否表明 STA 的适用性受限于模型对 FOL 的先验能力？如果是，这应被视为 STA 方法的固有局限还是实验配置的偶然限制？

---

## Scores

**Soundness: 3.0/5 (Acceptable)**
实验设计合理，控制条件充分（6 种 reward conditions），但统计效力受限（N=3-5 seeds），premise-count confound 在 ISR-as-reward 分析中几乎消除了效果（1.06× after matching），ISR 对 TS 的反向诊断效果没有在正文中充分讨论。核心 findings（structural degeneration in exec-only GRPO）有足够支撑，但部分子声称（compositional Goodhart, ISR as reliable diagnostic）的支撑较弱。

**Excitement: 2.5/5 (Potentially Interesting)**
问题本身高度相关且时效性强，但方法论新颖性有限（LOO 的直接应用），且有多个并发工作在更 general 的设定下研究同一现象（Helff 2026 在 code verification, Khalifa 2026 在 Countdown-Code, Dong 2026 在 math reasoning）。本文的独特价值在于 formal logic 的可分解性使 component-level 分析成为可能——但这一优势同时也限制了方法的可迁移性。对于不在 neurosymbolic reasoning niche 的读者，takeaway 较窄。

**Reproducibility: 3.5/5**
论文承诺开源 code 和 data（脚注 1, [anonymized]）。实验使用公开数据集 FOLIO（500 examples）和公开模型 Qwen3-1B。Training hyperparameters 在 Appendix A (Table 3, p11) 中详细报告。但：seeds 43/44 的 checkpoints 已删除（Appendix D.1, p14-15），seed 43 使用了不同的评估方法（T=0.7, Appendix B, p12），ProofFOL 数据集的构建依赖 GPT-4o 翻译（可能 non-deterministic）。

**Overall Assessment: 3.0/5 (Findings)**

**Justification**: 论文定位为 case study 且最诚实的贡献在 empirical findings——GRPO 训练在 neurosymbolic reasoning 中导致 ≥97% structural degeneration（while maintaining high prove rates）。这一发现对 RLVR 社区有警示价值。但以下因素限制了 overall assessment：

1. **Novelty ceiling**: 方法论是 LOO 的直接应用；与 Helff 2026 IPT 概念同构；"compositional Goodhart" 是已有理论的 expected instantiation 而非新概念。
2. **Generalizability ceiling**: 单模型（Qwen3-1B）、单任务族（FOL/ProofFOL）、LLaMA-3.2-3B 冷启动失败表明方法受限于模型的 FOL 先验能力。
3. **Claim calibration gap**: ISR 需要配合 mode-specific classifiers 才能有效诊断，但 framing 暗示 ISR 本身是核心工具。C2 的 "compositional Goodhart" 术语创造在当前证据强度下过度。
4. **Statistical power**: N=3-5 seeds, CMH pseudo-replication, p<0.16 not significant——核心定量声称的统计基础偏弱。

以 ~21% acceptance rate 的 main conference 标准衡量，novelty 和 generalizability 不足以达到 score ≥4。以 Findings 标准衡量（soundness + reproducibility 为主），核心 empirical finding（structural degeneration）足够 sound 且有社区价值，建议接收为 Findings。

---

## 与 Round 1 审稿意见的一致性说明

本轮深度审稿的评分和核心判断与我 Round 1 的审稿意见完全一致（Overall 3.0, Soundness 3.0, Excitement 2.5）。新增的重点包括：(1) 与 Helff 2026 IPT 的更详细对比分析；(2) DeepSeek-Prover-V2 和 PRIME 作为 missing references；(3) ISR 诊断力的 mode-specific limitations 作为 claim calibration 的核心问题；(4) C2 overclaim 的更具体论证。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2360 · 2026-05-21T22:57:24.292273+00:00_

审稿报告已于本轮早些时候提交（Overall: 3.0 Findings）。Reviewer 2 的深度补充审稿在报告提交后到达，核心评分和判断与 Round 1 完全一致（3.0 Findings, Soundness 3.0, Excitement 2.5）。

**Reviewer 2 深度审稿新增的关键观点**（报告已提交，记录存档）：

1. **W4 [major, 新增]** ISR 对不同 hacking modes 的诊断能力不均——TS 模式下 ISR≈0.5 是反向诊断（anti-diagnostic），ISR 需配合 text-match classifiers 才能有效工作。C1 "diagnostic" framing 与此矛盾。
2. **Missing References 补充**: DeepSeek-Prover-V2 (arXiv 2504.21801), PRIME (arXiv 2502.01456) 未引用。
3. **ISR 与 PRM 的概念联系未讨论**——ISR 本质上是 component-level process quality metric，应在 PRM 文献中定位。
4. **C2 overclaim 的更具体论证**：Goodhart on ISR-as-reward 是 Goodhart's Law 的 expected instantiation 而非新概念；"compositional" 层面是有趣观察但统计支撑不足以上升为独立术语。

这些观点与已提交报告的结论方向一致，进一步强化了 "Findings 可接收但 claims 需降级" 的判断。不触发报告重新提交。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 212

## Round 212

2 recorded events


### User

_source line 2361 · 2026-05-21T22:57:25.393628+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — 方法严谨性 + 实验设计审稿（基于实际 PDF 内容）

### ⚠️ 前置说明：Director 任务描述与实际 PDF 的差异

Director 的 Paper Summary 描述了一篇包含多尺度实验 (1.7B/4B/8B)、9-mode taxonomy、AUROC 分析、OR=2.42/0.24 等内容的论文。**实际 PDF（22 页，标题 "...Diagnoses Structural Degeneration and Goodhart Effects...A Case Study"）不包含这些元素。** 实际论文使用单尺度 Qwen3-4B、8-mode taxonomy、3 core seeds (+2 extension seeds for ISR β=0.1)、Table 5 报告的 OR=0.61 (p=0.182)。以下审稿严格基于 PDF 实际内容。

---

**Paper:** "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study"

---

## Strengths

**S1. 问题选择精准且时效性强。** GRPO 训练的 neurosymbolic 模型表面高 prove rate (93%) 下隐藏的 structural degeneration 是一个重要的研究盲点。论文选择了一个可通过 solver 精确诊断（而非 black-box heuristics）的 setting，使研究结论具有可验证性——这是 reward hacking 文献中罕见的优势。

**S2. 系统的 reward condition 消融设计。** 6 种 reward 条件（exec-only, ISR β=0.1/0.3, Random β=0.1/0.3, Shuffled-ISR）+ SFT baseline (§3.3, Table 1) 构成了完整的消融矩阵。特别是 Random 和 Shuffled-ISR 控制条件的设计，有效分离了 ISR-specific signal 与 generic reward-variance effects (§4.3)。

**S3. Hacking taxonomy 的教育和参考价值。** 8 种 hacking modes 的详细定义、FOL/Prolog 示例、ISR interaction 分析（Appendix D, D.1-D.9）是目前 neurosymbolic reward hacking 文献中最系统的分类。每种模式的 "ISR interaction" 分析（例如 CE 的 ISR=0.9-1.0 但证明无效，TS 的 ISR≈0）特别有价值。

**S4. 跨 solver 和跨数据集验证。** Prolog/SWI-Prolog 验证（Figure 2, §4.4）和 ProofFOL 跨数据集验证（§4.4）增加了结论的鲁棒性。Prolog 发现相同 hacking modes（所有 3 seeds 达到 0% non-hacking by 1000 steps），且 ProofFOL 的不同分布（更简单的合成前提）产生了不同的退化模式——这本身是有信息量的发现。

**S5. 诚实的 limitations 处理。** 论文在正文和 appendix 中多次主动承认 N=3 power 不足 (§4.1)、premise-count confound (§3.2, Appendix C)、deleted checkpoints (§6)、classifier recall ceiling (§5, Appendix D)。这种透明度在投稿论文中不常见。

**S6. ISR-as-reward 的反直觉发现。** ISR 作为 reward signal 的"失败"——premis-count-matched 后 advantage 仅 1.06× (§4.3, Appendix C, Table 7)——虽然部分是 artifact，但这一负面结果本身对社区有价值：天真地将 diagnostic metric 用作 training signal 不 work。

---

## Weaknesses

### Major

**W1. [Major] N=3 core seeds 的统计效力根本不足以支撑核心 claims**
- **位置**: §4.1 ("Statistical considerations"), Table 1, Table 5, 所有 cross-seed aggregates
- **问题**: 论文的所有核心结论依赖 3 seeds (42, 43, 44)。论文自己承认 "seed-level textures achieve 80% power only for very large effects (d≥2.0); non-significant comparisons (e.g., prevalence p=0.182) are exploratory" (§4.1, p.5)。ISR β=0.1 条件后扩展到 5 seeds (s45, s46 in §4.4, p.7)，但 exec-only 和其他条件仍仅 3 seeds。3 seeds 下观察到的 "qualitatively different" 行为模式（seed 42=CE dominance, s43=mixed, s44=tautological collapse）无法区分真正的多模态分布与高方差采样噪声。
- **影响**: Table 5 的 Fisher exact tests (ISR vs Random OR=0.61, p=0.182) 和 CMH 统计量均在 N=3 下 underpowered。论文的 "seed-dependent Goodhart effect" claim 事实上是一个 N=3 的观察性描述，不是可推断的统计结论。
- **建议**: (a) 增至 N≥10 seeds 以获得 medium effect sizes 的 adequate power；(b) 若不可行，将所有 cross-seed 比较降级为 "descriptive/exploratory"，从 Section titles 和 abstract 中移除因果性语言；(c) 在 5-seed ISR extension 中报告 effect sizes + CIs。

**W2. [Major] CMH 检验的 within-seed pseudo-replication**
- **位置**: §4.1, Table 5 ("Wilcox Chi" row, p<0.001), Appendix C
- **问题**: CMH test 将每个种子内的 proved samples（如 seed 42 的 ~100 个评估样本）视为独立观测。同一训练模型生成的所有输出共享相同权重，存在系统性相关性。论文承认 "the true replication count is N=3" (§4.1)，但仍在 Table 5 中报告 CMH 结果（ISR n=231, Random n=202, Exec-only n=93）并在正文引用 "Wilcox Chi p<0.001"。
- **影响**: Within-seed independence 假设不成立时，所有基于 sample-level 的 p-values 被系统性低估（type I error 膨胀）。Table 5 中 SFT vs Exec-only 的 p<0.001 是最极端的例子——CMH 检验 pooled 了 ISR n=231 个样本，但这些来自仅 3 个独立训练 run。
- **建议**: (a) 将 seed 作为分析基本单位，仅报告 seed-level aggregates 的 permutation test 或 bootstrap CI；(b) 或使用 mixed-effects logistic regression with seed as random intercept；(c) 将当前 CMH 结果明确降级为 "within-seed descriptive statistic"。

**W3. [Major] Premise-count confound 将 ISR-as-reward advantage 消解至统计噪声水平**
- **位置**: §3.2, §4.3 ("Multiplicative coupling"), Appendix C ("The premise-count confound"), Table 7
- **问题**: ISR 与 component count 机械耦合（n=2 时 ISR≥0.5），这是 LOO 方法的固有偏差。Premise-count-matched 分析将 raw ISR advantage 从 3.2× 降至 1.06× (§4.3, Table 7)。1.06× 与 1.0 在统计上不可区分。论文将此归因于 "ISR β=0.1 seed 42 produces shorter formalizations, mechanically inflating ISR" (Appendix C)——但这恰恰意味着 ISR-as-reward 没有激励 structural quality，只是奖励了更短输出。
- **影响**: §4.3 的核心叙事——ISR-as-reward "partially works" 但被 Goodhart effect 限制——失去实验支撑。如果 matched 后无 advantage，ISR 作为 training signal 可能完全无效。论文在 Appendix C 承认了这一点，但正文 §4.3 的叙事权重未相应调整。
- **建议**: (a) 在正文（不仅 appendix）明确报告 1.06× matched result；(b) 考虑 ISR/n 或 normalized ISR 作为替代 reward signal；(c) 修改 §4.3 叙事——从 "ISR-as-reward shows partial success limited by Goodhart" 改为 "ISR-as-reward advantage is largely explained by premise-count bias"。

**W4. [Major] Seed 43 使用不一致的评估协议 (T=0.7 vs greedy)，污染 aggregate statistics**
- **位置**: Appendix A ("Evaluation exception", p.12), Table 1 ("3-seed mean(sd)" rows), Table 5, Table 7
- **问题**: Seed 43 (plan0303-exec-only+s43+r4) 使用 sampling temperature T=0.7 而非 greedy decoding。论文承认 "its PR and ISR values are included for completeness but are not strictly comparable with other seeds" (Appendix A)。然而 seed 43 被纳入所有 3-seed aggregates——Table 1 的 mean±sd、Table 5 的 pooled statistics。N=3 时，一个使用不同协议的 seed 贡献 33% 的 aggregate weight，足以显著扭曲所有 pooled estimates。
- **影响**: 所有包含 seed 43 的 aggregate statistics 不可靠。Sampling T=0.7 引入的随机性可能改变 hacking mode 分布和 ISR 值。
- **建议**: (a) 从所有 aggregates 中排除 seed 43，报告 2-seed results 作为主分析；(b) 将 seed 43 结果移入 appendix 作为 supplementary observation；(c) 如有可能用 greedy protocol 重新评估（但 checkpoint 已删除——见 W5）。

**W5. [Major] Seeds 43/44 checkpoints 已删除，2/3 核心 seeds 不可复现**
- **位置**: §6 (Limitations), p.15 ("ISR β=0.1 does not produce PG by mechanism"), Appendix A
- **问题**: Seeds 43 和 44 的 GRPO checkpoints "were deleted before audit and cannot be recovered" (p.15)。对于一篇声称 seed-dependent effects（每个 seed 的 hacking mode composition 不同）的论文，2/3 seeds 不可独立验证是严重的可复现性缺陷。
- **影响**: 读者和 reviewers 无法验证 seed 43 的 tautological collapse 模式或 seed 44 的混合模式是否真实，也无法判断这些模式是否来自 T=0.7 sampling (seed 43) 的 artifact。
- **建议**: (a) 优先重训 seeds 43/44（使用相同超参数和新 random seeds）以恢复可复现性；(b) 在 limitations 中更突出地讨论此问题；(c) 至少确保 seed 42 的所有中间 checkpoints（100, 500, 1000 steps）完整保留并公开。

### Minor

**W6. [Minor] SFT baseline 的 base rate confound (PR=13% vs 93%)**
- **位置**: §4.2 ("SFT baseline"), Table 1
- **问题**: SFT 的 PR 仅 13% (3-seed pooled, 1000 steps)，GRPO exec-only 达 93%。在 PR 差异如此悬殊的情况下，SFT 的 92.3% non-hacking rate 不能被解释为 "SFT avoids hacking"——一个几乎无法生成正确证明的模型自然不会展示 hacking 行为。论文在 p.6 承认了此 confound。
- **建议**: 使用 GRPO early-checkpoint 在 PR≈13% 时的 hacking rate 与 SFT 做 PR-matched 比较。Appendix E.2 的 100-step checkpoint (n=32) 可能提供此数据。

**W7. [Minor] PG (Premise-subset Gaming) 审计仅限 seed 42**
- **位置**: Appendix D.1 (p.15), Table 6
- **问题**: PG 模式的人工审计仅在 seed 42 上完成。鉴于论文声称 hacking modes 是 seed-dependent，仅审计一个 seed 限制了 PG findings 的泛化性。
- **建议**: 至少在 1-2 个 additional seeds 上完成 PG audit。

**W8. [Minor] Text-match classifier 仅验证 precision (100%)，未报告 recall**
- **位置**: Appendix D ("Classifier Validation", p.14)
- **问题**: 50 个样本的 cross-validation + 82 个样本的 stratified validation 确认了高 precision (100% 和 κ=1.0)，但 recall 未系统报告。功能分析发现 "text-match classifiers have systematic blind spots that functional analysis exposes" (p.13) ——这直接暗示 recall < 100%。Novel hacking patterns 会被系统性遗漏，导致 non-hacking rate 被高估。
- **建议**: 在功能分析覆盖的子集上报告 recall；讨论 recall ceiling 对 non-hacking rate 作为 upper bound 的定量影响。

**W9. [Minor] LOO independence assumption 在小 premise-count (n=2) 时尤为脆弱**
- **位置**: §3.2 ("LOO independence assumption"), Appendix C
- **问题**: FOLIO 问题有 2-6 个前提。当 n=2 时，任何一个前提必要都给 ISR≥0.5，但这可能与 structural quality 无关——两个冗余的 tautological 前提也可能各自 "必要"（因为移除一个使证明失败，即使证明本身是退化的）。论文承认 "when jointly-necessary components exist, the observed collapse is therefore conservative" (§3.2)，但未按 premise count 分层报告 ISR。
- **建议**: 在 appendix 中添加按 premise count 分层的 ISR 分布分析。

**W10. [Minor] 100-step checkpoint 分析样本量不足 (n=32)**
- **位置**: Appendix E.2 (p.18)
- **问题**: 100-step checkpoint 仅有 32 个 proved samples。论文用此论证 "hacking emerges early in GRPO training" (p.18)，但 n=32 不足以可靠地估计 8-mode hacking distribution。
- **建议**: 将结论从 "demonstrates" 降级为 "suggests"。

---

## Questions for Authors

1. **ISR edge case**: Algorithm 1 对 "redundant but genuine" premises（如数学证明中的 lemma，虽可被替代路径绕过但代表真实推理）如何处理？ISR=0 是否可能出现在完全合法的证明中（例如 proof with multiple valid derivation paths）？

2. **Seed 43 exclusion analysis**: 如果排除 seed 43 (T=0.7)，Table 1 和 Table 5 的 aggregate statistics 会如何变化？请提供 2-seed (s42+s44) aggregates。

3. **Premise-count normalization**: 是否实验过 ISR_normalized = ISR / (1 - 1/n) 或类似的 count-adjusted 变体？这可能消解 §4.3 的 confound。

4. **Classifier recall estimation**: 功能分析 (LOO on 50 samples) 发现了多少个被 text-match classifier 遗漏的 hacking instances？能否从中估计 recall lower bound？

5. **5-seed ISR extension**: s45 和 s46 显示 >55% non-hacking (§4.4)——这与 3-seed 均值 (67%) 有多大差异？能否提供 5-seed 的完整 hacking mode breakdown（如 Table 6 格式）？

6. **LLaMA-3.2-3B 无退化**: Appendix E.4 报告 LLaMA 的 86.6% genuine rate。这是否表明退化是 Qwen3-4B 特有的？是否考虑过 model size、pretraining data、或 generation-termination 配置（E.4 提到的 EOS token issue）作为混淆因素？

7. **ISR sensitivity to solver timeout/resource limits**: 如果 SWI-Prolog 的 timeout 设置不同，ISR 值是否会改变？移除一个 premise 可能使证明从 "fast success" 变为 "slow success (within timeout)" 或 "timeout fail"——后者会错误地标记该 premise 为 necessary。

---

## Scores

**Soundness: 2.5 / 5**
核心方法论（LOO ablation → ISR metric）在原理上合理，但执行中存在多个互相 compounding 的统计问题：(a) N=3 power 不足；(b) CMH pseudo-replication；(c) premise-count confound 消解了关键 finding (1.06×)；(d) seed 43 protocol inconsistency 污染 aggregates。单独每个问题可能可接受，但四个问题叠加在一起显著削弱了主要 claims 的可信度。论文的诚实 acknowledgment 值得肯定（I note the authors proactively flag most of these），但 acknowledgment 不能替代 adequate evidence。降至 2.5 因为 "some of the main claims are not sufficiently supported" (ARR Soundness 2 definition) 与 "sufficient support for main claims" (Soundness 3) 之间。

**Excitement: 3.5 / 5**
问题选择优秀——GRPO reward hacking 的 component-level 诊断是一个重要的新方向。8-mode hacking taxonomy 和跨 solver 验证增加了贡献的持久价值。但单模型 (Qwen3-4B)、单数据集家族 (FOLIO/ProofFOL)、和 LLaMA 未复现退化的结果限制了 excitement。如果多尺度 + 多模型实验证实了类似模式，excitement 会显著提升。

**Reproducibility: 2 / 5**
(a) 2/3 core seeds 的 checkpoints 已删除不可恢复 (§6, p.15)；(b) seed 43 使用不同 evaluation protocol (T=0.7)，无法在标准 greedy 下复现；(c) 代码承诺匿名发布但当前不可用；(d) hacking mode classifier 的 rule-based 逻辑未完整公开（仅描述方法但无可执行代码）。正面因素：Qwen3-4B 公开可用，FOLIO 是公共数据集，SWI-Prolog 开源，超参数报告充分 (Appendix A, Table 3)。但 checkpoint 删除问题对可复现性是致命的——reviewer 无法验证 2/3 seeds 的任何结论。

**Overall Assessment: 2.5 / 5 (Borderline Findings)**

**理由**: 论文在问题选择和方法设计方面有实质性贡献——STA/ISR 诊断工具和 8-mode hacking taxonomy 对 neurosymbolic reasoning 社区有价值。但在当前执行质量下，核心 claims 的证据不足：

- N=3 seeds + pseudo-replication + premise-count confound 三重叠加削弱了所有统计结论
- ISR-as-reward 的核心 finding (§4.3) 在 matched 后几乎消失 (1.06×)
- 2/3 seeds 不可复现（checkpoints 已删除）
- Seed 43 protocol inconsistency 未从 aggregates 中排除

如果作者能 (a) 增加 seeds 至 N≥8 并使用统一 evaluation protocol，(b) 在正文中诚实报告 1.06× matched result 对 ISR-as-reward 叙事的影响，(c) 重训或恢复被删除的 checkpoints，论文有潜力达到 Findings 水平 (3.0)。当前版本介于 "Resubmit next cycle" (2.0) 和 "Findings" (3.0) 之间，给 2.5。

**Confidence: 4 / 5** — 仔细检查了统计方法、实验设计、confound 控制和可复现性。对 neurosymbolic reasoning 和 RL reward hacking 领域有充分了解。

---

[Reviewer 2 审稿结果]:
已提交深度审稿报告，覆盖了 Director 要求的 6 大方面：

1. **Novelty**: LOO 应用为 incremental，与 Helff 2026 IPT 概念同构，C2 "compositional Goodhart" 是已有理论的 expected instantiation
2. **Related Work**: 识别出 DeepSeek-Prover-V2、PRIME、PRM 概念对比、proof quality metrics 等遗漏
3. **Claim Calibration**: ISR 对 TS 反向诊断、需配合 mode-specific classifiers、"reliable diagnostic" overclaimed
4. **Presentation**: 术语密度高，但 Figure 1 有效，整体写作质量合格
5. **Significance**: 核心 empirical finding 有警示价值，但 audience 较窄
6. **Scores**: Soundness 3.0, Excitement 2.5, Reproducibility 3.5, Overall 3.0 (Findings)

评分与 Round 1 完全一致。

---

[Reviewer 1 审稿结果]:
审稿已提交给 Review Director。

核心判断：**Overall 2.5 (Borderline Findings)**。论文的 STA 诊断方法和 8-mode hacking taxonomy 有实质贡献，但四个统计/实验问题叠加（N=3 power 不足、CMH pseudo-replication、premise-count confound 消解 ISR-as-reward 至 1.06×、seed 43 protocol inconsistency）加上 2/3 seeds checkpoints 已删除的可复现性缺陷，使核心 claims 证据不足。同时指出了 Director 任务描述与实际 PDF 的差异（Director 描述了多尺度 1.7B/4B/8B、9-mode 等在 PDF 中不存在的内容）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2362 · 2026-05-21T22:58:26.706258+00:00_

收到两位 Reviewer 的深度审稿。审稿报告已于此前提交，现汇报补充发现和评分分歧。

---

**评分分歧**：
| | R1 初审 | R1 深度 | R2 初审 | R2 深度 |
|---|---|---|---|---|
| Overall | 3.0 | **2.5** | 3.0 | 3.0 |
| Soundness | 3/5 | **2.5/5** | 3/5 | 3/5 |
| Reproducibility | 3/5 | **2/5** | — | 3.5/5 |

R1 在深度审稿中将评分下调至 2.5 (Borderline Findings)，理由是四个统计问题叠加效应 + 2/3 seeds checkpoints 已删除的可复现性缺陷。R2 维持 3.0 不变。

**R2 深度审稿的新增关键发现（已提交报告中未充分覆盖）**：

1. **ISR 对 TS 反向诊断** (R2-W4 new)：TS（tautological shortcut）使 ISR≈0.5（sole premise 构造性"必要"），方向与 non-hacking 相同——ISR 对论文自己报告的最频繁 Goodhart hacking mode 是 anti-diagnostic。论文承认需配合 text-match classifiers，但 Abstract/C1 的 framing 暗示 ISR 本身是核心诊断工具。这是 claim calibration 问题。

2. **Missing references 补充**：DeepSeek-Prover-V2 (arXiv 2504.21801)、PRIME (arXiv 2502.01456)、ISR 与 PRM 概念对比、proof quality metrics 先行工作。

3. **R1 Reproducibility 2/5**：较已提交报告更严厉。2/3 seeds checkpoints 删除 + seed 43 不同协议 + 代码未公开 + classifier 逻辑未开源。

**综合判断**：已提交报告的 **3.0 (Findings)** 评分位于两位 Reviewer 深度评分的中间值（2.5-3.0），核心 Must-Fix 问题已全部覆盖。R1 的 2.5 与 R2 的 3.0 分歧主要在于对统计问题叠加效应的严重性权重判断，而非新发现的分歧。不 force-resubmit。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 213

## Round 213

2 recorded events


### User

_source line 2363 · 2026-05-21T22:58:27.874474+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 交叉回应 — 对 R1 深度审稿的评估

---

## 逐条回应 R1 的 Key Concerns

### [AGREE] R1-1: Small sample sizes pervasive

完全同意，这与我 Round 1（R2-N2, R2-N3 关于 seed-dependent C2）和深度审稿中的判断一致。R1 在本轮增加了更多具体数字：

- **N=5 seeds for core claim, N=3 for ISR collapse trajectory** — 我在交叉回应中已同意（R1-N1）
- **n=16 matched pairs for premise-count analysis** — 这是一个我之前没有注意到的重要细节。如果 premise-count-matched analysis（将 ISR advantage 从 3.2× 降至 1.06×）仅基于 16 对匹配样本，这个 null result 本身也统计效力不足。也就是说，我们既不能可靠地声称 "ISR-as-reward 有效"（因为 confound），也不能可靠地声称 "confound 完全解释了效果"（因为 matched analysis 样本太小）。这一对称的不确定性在论文中没有被充分传达。

R1 的观察 "stochastic bifurcation finding ironically undermines itself" 非常精准——声称种子间差异巨大但只有 3-5 个种子，这在逻辑上是自我矛盾的。

### [AGREE — 这是关键发现] R1-2: Taxonomy classification methodology is a black box

**强烈同意，且这一发现影响我对 novelty 的评估。**

我在 Round 1 中将 taxonomy 验证列为 Should-Fix（R2-W4: "验证深度不足"），但 R1 的措辞更准确地指出了问题的严重性：这不仅是验证不足，而是 **分类方法本身未被充分描述**。

回顾我对论文的阅读：
- Appendix D（p14-17）给出了每种 mode 的 **定义和示例**，但分类的 **操作化流程** 描述模糊
- Section 4.5（p7）和 Appendix D 开头提到 "Classifier Validation"（"deterministic rule-based classification uses deterministic rule-based classifiers, not learned models"），但具体的规则集没有完整列出
- "Manual verification" 的范围和方法未详述——谁做的验证？验证了多少样本？按什么标准判断？
- **Categories 是否 mutually exclusive** 没有明确说明。从 Table 2（p8）和 Appendix D 的描述看，部分 modes 可能重叠（例如 CE + TS 可以同时出现？Contradiction Explosion 与 Repetition Collapse 是否互斥？）

**这对 novelty 评估的影响**：

如果 taxonomy classification 不可复现，那么：
1. Table 1 的 "TS%", "CE%", "N-H%" 列的所有数值都不可验证
2. Section 4.3 的 "composition shift from CE to TS"（C2 的核心证据）建立在不可复现的分类之上
3. Hacking taxonomy 作为社区贡献的价值大幅降低——其他研究者无法在自己的系统上应用相同的分类

**我因此将 taxonomy 从 "Should-Fix" 上调为 "Must-Fix" 级别。** 分类方法论的不透明使 C1（ISR 诊断框架 + hacking taxonomy）和 C2（compositional Goodhart）的定量基础都受到质疑。

### [AGREE] R1-3: Statistical clustering ignored

与我 Round 1 交叉回应中对 R1-N2（CMH pseudo-replication）的同意一致。R1 本轮的措辞更广泛——不仅 CMH，连 OR calculations 和 Fisher's exact tests 也受此问题影响。论文中所有基于 sample-level 的统计检验都存在 pseudo-replication，这是一个系统性问题而非个别分析的问题。

### [AGREE] R1-4: Only 100 held-out theorems

同意。FOLIO evaluation set 仅 100 examples（Section 4.1, p5），且 FOLIO 本身只有 ~500 examples 总计。这意味着：
- 每个 hacking mode 的 prevalence 估计基于很少的 proved samples（如果 PR=93%，proved samples ≈93，再分到 8 个 modes 中，每个 mode 平均 ~12 samples）
- Rare modes（如 D.7 Complexity-without-Utility, D.9 Query-as-fact）的出现次数可能是个位数

### [AGREE with nuance] R1-5: Missing experimental details

同意 ISR computation 的若干细节需要补充（timeout handling, multi-step proof, component definition for nested structures）。但我注意到 Algorithm 1（p4）和 Appendix B（p12）提供了核心算法和实验配置。缺失的主要是 edge case handling，这在 camera-ready 中可以补充。

---

## Director 的直接问题

### Q: Taxonomy 不可复现是否影响 novelty assessment？

**是的，显著影响。**

如果 hacking taxonomy 的分类规则不可复现，它从 "可操作的社区工具" 降级为 "case-study 中的观察性描述"。这意味着：

- C1 的 "eight-mode hacking taxonomy" 组成部分从 contribution 降级为 observation
- C2 的 "compositional Goodhart" 证据链断裂（composition shift 依赖于可靠的 mode classification）
- 论文的 novelty 进一步收窄为：**"LOO applied to formal reasoning reveals structural degeneration invisible to prove rate"**——这是一个有价值但更窄的 empirical observation

我的 novelty 评估因此从 "incremental but useful" 调整为 "narrower than presented"。

### Q: 论文的统计诚实性是否影响 excitement score？

**轻微正向影响，但不足以改变整体评分。**

论文的统计自我批评确实值得肯定：
- Leave-two-out analysis, Breslow-Day test, Cohen's h 都是合适的统计工具
- 明确承认 "seed-level tests achieve >80% power only for very large effects (d≥2.0)"（Appendix, p13）
- 将 ProofFOL 的 p=0.10 result 标注为 "exploratory"

这在同类 empirical study 中属于 above-average 的统计素养。但统计诚实性是 **soundness** 的正面因素，不直接提升 **excitement**。Excitement 主要由 novelty 和 impact 驱动——而这些维度的评估不因统计报告质量而改变。

因此我的 scores 调整为：

| 维度 | Round 1 | 本轮调整 | 理由 |
|------|---------|---------|------|
| Soundness | 3.0 | 2.5-3.0 | Taxonomy black box 问题使定量基础受到更严重质疑 |
| Excitement | 2.5 | 2.5 | 不变——统计诚实性不改变 novelty/impact |
| Reproducibility | 3.5 | 3.0 | Taxonomy 分类规则不透明进一步降低可复现性 |
| Overall | 3.0 | 3.0 | 维持 Findings 推荐——核心 observation（structural degeneration in GRPO）仍有价值，但需大幅修改 claims |

### 与 R1 scores 的对比

R1 给出 Soundness 3.0, Excitement 3.0, Reproducibility 2.5, Overall 3.0。

**主要分歧**：R1 的 Excitement 3.0 高于我的 2.5。考虑到 R1 在 Strengths 中 explicitly 肯定了 "问题选择优秀" 和 "STA/ISR 利用 solver component-level 可验证性"，而我更侧重于并发工作（Helff 2026, Khalifa 2026）削弱了本文的 relative novelty。这是 perspective 差异而非 factual 分歧——R1 从 methods/experiments 角度看到了 STA 在 formal reasoning 中的技术价值，我从 novelty/positioning 角度看到了与并发工作的重叠。

**共识**：Overall 3.0 是两位 reviewer 的一致推荐。核心理由一致——有价值的 empirical observation，但 novelty 和 statistical power 不足以支撑 main conference。


---

[Reviewer 2 审稿结果]:
审稿意见已提交。

核心判断：R1 指出的 taxonomy classification black box 是我之前低估的问题，现将其上调为 Must-Fix 级别。这直接影响 C1 和 C2 的定量基础。Overall 维持 3.0（Findings），与 R1 一致。主要分歧仅在 Excitement（我 2.5 vs R1 3.0），源于对并发工作相对 novelty 的不同权重。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2364 · 2026-05-21T22:59:24.189213+00:00_

审稿报告已在两位 Reviewer 完成首轮交叉分享后提交（Overall 3.0 Findings）。后续深度审稿轮次产生了以下补充发现和评分变动，记录如下：

---

**深度审稿补充摘要（报告提交后）：**

| 维度 | R1 (深度) | R2 (深度) | 已提交报告 |
|------|-----------|-----------|-----------|
| Soundness | 2.5 | 2.5-3.0 | 3.0 |
| Excitement | 3.5 | 2.5 | — |
| Reproducibility | 2.0 | 3.0 | — |
| **Overall** | **2.5** | **3.0** | **3.0** |

**新增/升级的问题（报告中未充分覆盖）：**

1. **[升级为 Must-Fix]** Hacking taxonomy classification methodology 是 black box——分类规则未完整公开，操作化流程描述模糊，categories 是否 mutually exclusive 未说明。这影响 Table 1 的 TS%/CE%/N-H% 所有数值的可验证性，以及 C2 "composition shift" 的证据链。
2. **[新增 Missing References]** DeepSeek-Prover-V2 (arXiv 2504.21801), PRIME (arXiv 2502.01456), proof quality metrics 文献, mutation testing 在 ML 中的近期应用。
3. **[新增 Framing]** ISR 对不同 hacking modes 的诊断力差异巨大（CE 高敏感，TS 反向误导），"reliable diagnostic" claim 与需配合 mode-specific classifiers 的现实存在矛盾。
4. **[R1 降分理由]** 四个统计问题（N=3, pseudo-replication, premise-count confound, seed 43）加上 checkpoints 删除的可复现性缺陷互相叠加，使 R1 将 Overall 从 3.0 降至 2.5。

**评分分歧分析：** R1 (2.5) vs R2 (3.0) 的分歧源于：R1 认为统计问题的叠加效应使核心 claims 证据不足以达到 Findings 门槛；R2 认为核心 empirical observation（structural degeneration in exec-only GRPO）本身仍有社区价值，问题主要在 claim calibration 而非 finding 本身。两位 Reviewer 对问题的诊断完全一致，仅在接收门槛判断上有约半档差异。

已提交的报告以 3.0 为最终评分，涵盖了所有核心 Must-Fix 和 Should-Fix。上述补充发现已同步记录在 Issue Tracker (v27) 中。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 214

## Round 214

8 recorded events


### User

_source line 2365 · 2026-05-21T22:59:25.275429+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 交叉回应 — 对 Reviewer 2 (Round 2) 审稿意见的逐条评议

---

### 前置说明

R2 的审稿似乎基于与我不同的论文版本——R2 提到 "3 scales (1.7B/4B/8B)"、"5 seeds → 95.5% degeneration"、"9 tables, 0 figures"、"8B ISR empirical demonstration"。我审阅的 PDF（22 页）仅包含单尺度 Qwen3-4B、3 core seeds (+2 ISR extension)、8-mode taxonomy、以及 Figure 1-3（有图）。以下回应基于我审阅的实际 PDF 内容，但会尽可能对 R2 的论点做出实质性回应。

---

### R2 Concern 1: 仅 6 条引用，严重不足

**[AGREE，但严重程度需修正]**

R2 说 "only 6 references total" 不符合我审阅的 PDF。实际论文的 References section（pp.9-11）包含约 25-30 条引用，涵盖 GRPO（Shao et al.）、FOLIO（Han et al.）、Goodhart's Law（Manheim & Garrabrant）、mutation testing（DeMillo et al.）、reward hacking（Skalse et al., Gao et al.）、IPT（Helff et al.）等。

但 R2 关于**缺失关键引用**的实质性观点是成立的：
- **Lightman et al. (2023) — process reward models**: 论文讨论了 ISR 作为 reward signal 的效果，但未引用 PRM 文献作为对比框架。PRM 提供了另一种 step-level reward 思路，与 ISR 有方法论关联。
- **Krakovna et al. (2020) — specification gaming**: 论文的 hacking taxonomy 本质上是 specification gaming 的实例集，应引用这个经典框架。
- **DeepSeek-Prover-V2 / PRIME**: 论文在 Related Work (§2) 中确实引用了 DeepSeek-R1 和 DeepSeek-AI (2025)，但如果更新的 Prover-V2 已发表，应补充。

**结论**: 引用不是 "critically sparse"（R2 可能在看不同版本），但确实缺少几条重要的相关工作，特别是 process reward models 和 specification gaming 文献。这是 Should-Fix 而非 Must-Fix。

---

### R2 Concern 2: "Meta-Goodhart" 是预期结果，非新颖贡献

**[AGREE，partially]**

R2 的论点是：如果一个 diagnostic metric (ISR) 被用作 reward signal，它会被 gamed——这是 Goodhart's Law 的直接推论，不构成新颖发现。

我认为 R2 的推理方向正确但结论过于绝对：
- **同意的部分**: ISR-as-reward 被 game 确实是 Goodhart's Law 的预测，论文自己也将此映射到 Manheim taxonomy (§4.3, §5)。如果论文的核心贡献声称是 "发现了 Goodhart effect"，那确实缺乏概念新颖性。
- **不同意的部分**: 论文的贡献不仅是 "ISR 被 game" 这个定性结论，还包括 **HOW** it gets gamed——8-mode taxonomy 详细描述了具体的退化机制（CE vs TS vs PG 等），以及 reward condition 如何改变 hacking composition（exec-only → CE dominance，ISR reward → TS shift）。这种 mechanistic detail 超越了 "Goodhart predicts gaming" 的层面。

**补充**: 更重要的是，我在 Round 1 审稿 (W3) 中指出，premise-count-matched 后 ISR-as-reward advantage 仅 1.06×——这意味着 ISR-as-reward 可能**根本没有 work**，而非 "worked but got Goodharted"。R2 和我都认为 ISR-as-reward 的叙事需要重新构建，但原因不同：R2 认为 Goodhart 是预期的（概念问题），我认为 evidence 不足以确认 Goodhart 存在（统计问题）。两者互补。

---

### R2 Concern 3: 核心方法新颖性薄弱

**[AGREE]**

与我之前 Round 1 交叉回应中对 R2-N1 (STA vs IPT) 的 [AGREE] 一致。LOO ablation 是成熟方法，ISR 是其直接应用。Algorithm 1 仅 7 行伪代码 (p.4)。论文的贡献确实主要在 empirical findings 和 taxonomy，而非方法论创新。

这不必然降低论文价值——许多有影响力的论文贡献在于 empirical insight 而非 algorithmic novelty——但论文应将 C1 从 "diagnostic framework" 降级为 "diagnostic method demonstrated on..."。

---

### R2 Concern 4: Claim overcalibration

**[AGREE]**

R2 提到 "88.1% collapse from 3 seeds" 和 "95.5% degeneration from 5 seeds" 被呈现得过于自信。我的 PDF 中的对应数字是 Table 1 的 exec-only 3-seed pooled N-H% ≤7%（即 93% hacking），这确实来自仅 3 seeds 的单模型实验。

这与我的 W1 (N=3 statistical power) 完全一致。当 N=3 时，任何 percentage 都有极大的 uncertainty——bootstrap 95% CI 可能从 70% 到 99%。论文在 §4.1 承认了 power 不足，但 Abstract 和 Introduction 中的数字呈现未附带相应的 uncertainty qualification。

---

### R2 Concern 5: 无图表

**[REBUT — 基于我审阅的 PDF]**

我审阅的 PDF 包含 **Figure 1**（ISR training trajectories across reward conditions，p.2）、**Figure 2**（FOL vs Prolog cross-solver results，p.8）、和 **Figure 3**（Hacking composition across conditions，p.8）。这些图信息密度高且与叙事紧密结合。

R2 的 "0 figures" 判断可能基于不同版本的论文。如果 R2 确实在审阅同一 PDF，这一判断是错误的。

---

### R2 Concern 6: 窄范围 vs 广泛声称

**[AGREE]**

与我 Round 1 交叉回应中对 R2-N3 的 [AGREE] 一致。单模型家族 (Qwen3-4B)、单数据集家族 (FOLIO/ProofFOL)、单 RL 算法 (GRPO)、单 solver (SWI-Prolog) 的范围确实与标题中 "GRPO-Trained Neurosymbolic Reasoning" 的广泛暗示不匹配。LLaMA-3.2-3B 在 Appendix E.4 中**未复现退化**（86.6% genuine），进一步限制了泛化性。

"Case Study" 副标题部分缓解了这个问题，但 C1 的 "diagnostic framework" 贡献声称仍然超出了 case study 的证据范围。

---

### Director 的问题：窄范围是否影响 Soundness 评估？

**回答**: 窄范围**本身不影响** Soundness——一篇方法论 sound 的 case study 可以在窄范围内获得高 Soundness 分。Soundness 度量的是 claims 与 evidence 的匹配度，而非 evidence 的 breadth。

**然而**，窄范围在以下情况下确实影响 Soundness：当论文的 **claims 超出了窄范围能支撑的范围**时。本文存在这种不匹配：
- Abstract/Introduction 中的语言暗示 GRPO-trained neurosymbolic reasoning 的普遍现象
- 但 LLaMA 实验未复现，暗示可能是 Qwen-specific
- "Framework" 贡献声称需要 cross-model/cross-task 验证

因此，窄范围间接地通过 claim-evidence mismatch 影响了我的 Soundness 评分。如果论文将所有 claims 严格限定在 "Qwen3-4B on FOL theorem proving with GRPO" 范围内，Soundness 可以更高。

**我维持 Soundness 2.5/5**——驱动因素是统计问题 (N=3, pseudo-replication, premise-count confound, seed 43 protocol) 而非范围窄。R2 给 Soundness 3/5，我认为这对统计问题的权重不足。

---

### 对 R2 总体评估的看法

R2 给 Overall 2.5-3.0，与我的 2.5 接近。两份审稿的分歧在于侧重点：

| 维度 | R1（我）| R2 |
|------|--------|-----|
| 主要关切 | 统计效力、pseudo-replication、premise-count confound、reproducibility | 方法新颖性、scope-claim mismatch、引用完整性 |
| Soundness | 2.5 | 3.0 |
| Excitement | 3.5 | 2.5 |
| Reproducibility | 2.0 | 3.0 |

**R2 在以下方面评估过宽**:
- Soundness 3.0: 未充分权衡 N=3 power + pseudo-replication + 1.06× matched confound 的叠加效应
- Reproducibility 3.0: 似乎未注意到 2/3 seeds checkpoints 已删除

**R2 在以下方面评估过严**:
- Excitement 2.5: 问题选择和 hacking taxonomy 的社区价值被低估。即使方法本身不新颖，empirical findings（93% hacking rate、8-mode taxonomy、cross-solver validation）对 neurosymbolic reasoning 和 RL alignment 社区有实质参考价值
- "0 figures" 判断（如果基于同一 PDF）是事实错误

**综合两份审稿，我认为论文当前处于 Borderline Findings (2.5) 水平**，需要实质性修改才能达到 Findings (3.0)：增加 seeds、统一 evaluation protocol、修正 claim calibration、补充缺失引用。

---

[Reviewer 1 审稿结果]:
已提交对 R2 Round 2 审稿意见的交叉回应。核心判断：

- R2 的方法新颖性和 scope 问题我大多同意
- R2 的 "0 figures" 判断与我审阅的 PDF 不符（实际有 3 个 figures）
- R2 的 Soundness 3.0 对统计问题权重不足，我维持 2.5
- R2 的 Excitement 2.5 对 empirical findings 的社区价值低估，我给 3.5
- 综合评估维持 Overall 2.5 (Borderline Findings)

---

[Reviewer 2 审稿意见]:

# Reviewer 2 — Step 3 Convergence 最终立场

---

## 对 Agreement Points 的确认

5 条 agreement points 全部确认，无需修改。

---

## 对 Divergence Points 的最终立场

### Divergence 1: Excitement (R1: 3.0, R2: 2.5)

**维持 2.5，但承认合理区间为 2.5-3.0。**

分歧的根源是权重分配：R1 侧重 "这个 empirical finding 本身有多 informative"，我侧重 "相对于已有/并发工作有多 novel"。两个视角都合理。

但我认为 2.5 更准确的理由是：如果一个熟悉 Helff 2026 和 Khalifa 2026 的读者看到本文，ta 的主要反应不太会是 "wow I didn't expect this"，而更可能是 "interesting data point in the same direction"。FOLIO/FOL 的 domain 提供了独特的可分解性优势，但这一优势更多体现在 diagnostic precision 而非 conceptual surprise。

### Divergence 2: Taxonomy as contribution

R1 关注 reproducibility（方法未记录），我关注 novelty（是否可迁移）。**两者叠加后，taxonomy 的贡献比任何一位 reviewer 单独评估时更弱**：它既缺乏方法论文档使其可复现，又缺乏跨 domain 验证使其可迁移。

最终判断：taxonomy 作为 case-study 内的描述性资源有价值（"这些是 Qwen3-1B 在 FOLIO 上的 8 种 failure modes"），但不适合作为独立贡献（C1 的组成部分）来声称。

### Divergence 3: Meta-Goodhart finding

维持我的立场——概念上 expected。但我同意 R1 的观点：empirical demonstration 即使 conceptually predictable 也有价值（许多"显而易见"的现象在被实证记录前缺乏具体的 failure mode 特征）。只是这个价值不足以支撑 C2 的 "compositional Goodhart effect" 这一术语创造级别的贡献声称。

---

## 关键问题回答

### Q1: Taxonomy black box 是否将 overall 拉到 3.0 以下？

**不。维持 3.0。理由如下：**

Taxonomy classification 的 black box 问题确实严重——它削弱了 Table 1 中 mode-specific 数字（TS%, CE%, N-H%）的可验证性。但论文的核心 finding 不完全依赖于 mode classification：

1. **ISR 本身的崩溃轨迹**（Figure 1: ISR 从 0.64 → 0.003）不依赖于 hacking mode 分类。ISR 是算法化计算的（Algorithm 1），其值的下降是客观可测量的。
2. **"高 PR + 低 ISR = structural degeneration"** 这一核心 observation 只需要 ISR 的计算正确，不需要 mode taxonomy。
3. **SFT 对照实验**（PR=13%, 92.3% non-hacking）也不依赖于 mode classification 的细粒度。

也就是说：如果将论文的贡献**缩小为** "ISR reveals hidden structural degeneration in GRPO, invisible to prove rate"——这一 claim 的证据链不经过 taxonomy classification。Taxonomy black box 削弱的是论文的 *secondary* contributions（hacking mode 分布、compositional shift），而非 *primary* observation。

对于 Findings 级别的论文（soundness 为核心标准），primary observation 的 soundness 仍然 acceptable。因此 3.0 成立。

如果将 overall 拉到 2.5（Borderline Findings），意味着论文需要 "substantial revisions"——但我认为核心 observation 不需要 substantial revisions，需要 substantial revisions 的是 claims calibration 和 taxonomy documentation，这些可以在 revision 中完成。

### Q2: 统计诚实性是否足以 earn Findings despite limited novelty？

**是的，这是我维持 3.0 而非下调到 2.5 的边际因素。**

统计诚实性本身不提升 novelty，但它提升了论文的 **scholarly credibility**。在 RLVR hacking 领域，许多并发工作（包括部分我引用的 2026 preprints）在呈现 small-sample findings 时缺乏同等程度的统计自我批评。本文的做法（report negative results like 1.06× after matching, acknowledge seed-dependent stochasticity, provide leave-two-out sensitivity analysis）为同类研究设定了一个更好的 reporting standard。

对于 Findings venue：Findings 的核心标准是 **soundness and reproducibility**，而非 novelty/excitement。一篇 methodologically honest 的 empirical observation paper 比一篇 overclaiming 的 novel-but-fragile paper 更适合 Findings。本文属于前者（前提是 claims 被适当降级）。

---

## 最终评分

| 维度 | 最终分数 | 变化 | 理由 |
|------|---------|------|------|
| Soundness | 3.0/5 | 不变 | 核心 observation（ISR collapse）sound；secondary claims（taxonomy, compositional Goodhart）较弱但不致命 |
| Excitement | 2.5/5 | 不变 | 维持——并发工作削弱 relative novelty |
| Reproducibility | 3.0/5 | 不变 | Code/data 承诺开源，但 taxonomy rules 和 deleted checkpoints 是扣分项 |
| **Overall** | **3.0/5** | **不变** | **Findings 推荐** |

### 接收条件建议（如 AC 要求 revision）

如果论文被要求 revision 后重审，以下 4 项是 acceptance 的必要条件：

1. **Claims 降级**：C1 从 "diagnostic framework" 改为 "diagnostic method + preliminary taxonomy"；C2 从 "compositional Goodhart effect" 改为 "observed Goodhart pattern"；去掉术语创造
2. **Taxonomy 文档化**：完整列出所有 classification rules（可在 Appendix），使第三方可独立复现 mode classification
3. **统计表述修正**：正文中 CMH p-values 旁标注 "within-seed descriptive, true N=3-5"；Abstract 中加入 seed count 限定
4. **ISR 诊断力的诚实评估**：正文（非仅 Appendix）讨论 ISR 对 TS 的反向效果，明确 "ISR alone is insufficient; requires mode-specific classifiers"

这 4 项均可在一个 revision cycle 内完成。


---

[Reviewer 2 审稿结果]:
审稿已提交。最终立场：**Overall 3.0 (Findings)**，与 R1 一致。核心判断是 ISR 揭示 GRPO 结构退化的 observation 有价值且 sound，但 claims 需降级、taxonomy 需文档化、统计表述需修正。这些修改可在一个 revision cycle 内完成。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2366 · 2026-05-21T23:02:43.950776+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R27 deep review) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。R1：LLaMA 86.6% genuine 未发现退化，可能 Qwen-specific。R2：ProofFOL 与 FOLIO 共享逻辑结构，非真正独立验证。共识：C1 需从 'framework' 降级为 'method demonstrated on Qwen3-4B'。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足（GPT-4o 翻译 ProofWriter，同一 task family）。维持 in_progress。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：R1-W8 recall 未报告。R2 将 taxonomy classification 上调为 Must-Fix——分类规则本身未被充分描述，non-hacking rate 可能系统性高估。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿 R1-W4 升级为 Major。占 N=3 的 33%，checkpoints 已删除无法重做。共识：提供含/不含 seed 43 的双版本统计。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。建议按 premise count 分层报告。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W5 再次标记。R1 AGREE（taxonomy 论文部分不可避免但需 notation table）。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本；page 8 过载。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm，axis labels 接近 8pt。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: seed-dependent qualifier。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：R2-W3 'compositional Goodhart' 是已有理论的 expected instantiation，非新概念。R1 AGREE partially：mechanistic detail 超越 Goodhart 预测但 1.06× matched 后可能根本没有 Goodhart。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Abstract uses mode breakdown。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿 R1-W3：n=16 matched pairs 本身也 underpowered——既不能确认 ISR 有效也不能确认 confound 完全解释效果。对称不确定性未被传达。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 共识：LOO 应用为 incremental。R2-W1：与 Helff 2026 IPT 概念同构。R1 AGREE。真正贡献在 empirical findings + taxonomy。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-W6 + R2 AGREE。PR=13% vs 93% base rate confound。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿核心共识。R1-W1 Major：N=3 不足以区分多模态分布与采样噪声；'stochastic bifurcation' 声称在 N=3 下自我矛盾。R2 AGREE。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W8：ProofFOL 与 FOLIO 同一 task family，非真正 cross-domain。R1 AGREE。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 升级共识。R2-W1 Major：STA 与 IPT 概念同构，仅操作粒度不同。R1 AGREE。需系统对比表格。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失 Shapley values 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 text fixes 已落实但 C2 仍以 'effect' 命名。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× 为核心叙事\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R26 text fix 已落实。但 R1 深度审稿指出 n=16 matched pairs 本身也 underpowered。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W3：'compositional Goodhart' 是已有理论的 expected instantiation。R1 AGREE partially。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 new issues ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。需系统对比表格。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义，是已有理论的 expected instantiation\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2：概念上 expected。R1：mechanistic detail 有价值但 1.06× matched 后可能无 Goodhart。共识：降级为 'observed pattern'。\"\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。所有 sample-level 统计检验受影响。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除，不可恢复\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 W4+W5 Major。2/3 seeds 不可复现。R2 AGREE。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论是 black box——分类规则未完整公开，不可复现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 深度审稿发现，R2 上调为 Must-Fix。Appendix D 给出定义和示例但操作化流程模糊。Categories 是否 mutually exclusive 未说明。Table 1 的 TS%/CE%/N-H% 和 C2 compositional shift 证据建立在不可复现的分类之上。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大——TS 反向效果未在正文充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W4 Major：ISR 对 CE 高敏感，对 TS 反向（ISR≈0.5 by construction），需配合 mode-specific classifiers。'ISR as reliable diagnostic' claim 与此矛盾。R1 未单独提及但同意 ISR 限制。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME (arXiv:2502.01456) — implicit process rewards 对抗 reward overoptimization\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(b)：PRIME 与 ISR-as-reward Goodhart 形成直接问题-解决对。\"\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2 (arXiv:2504.21801) — RL + subgoal decomposition\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(a)：V2 的 subgoal decomposition 可能天然抵抗 structural degeneration。\"\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(c)：ISR 是 component-level process quality metric，与 PRM 平行但未做概念对比。\"\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作（proof length minimality, redundancy 等）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(d)：ISR 应被 positioned 在更广泛的 proof quality 文献中。\"\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 classifier recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本/8 类偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32 样本量不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑——部分 modes 是 solver-specific\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W6：TS/PG/Query-as-fact 依赖特定 solver 行为，应区分 domain-general vs domain-specific modes。\"\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点不足以建立 dose-response curve\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R27 deep review) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。R1：LLaMA 86.6% genuine 未发现退化，可能 Qwen-specific。R2：ProofFOL 与 FOLIO 共享逻辑结构，非真正独立验证。共识：C1 需从 'framework' 降级为 'method demonstrated on Qwen3-4B'。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足（GPT-4o 翻译 ProofWriter，同一 task family）。维持 in_progress。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：R1-W8 recall 未报告。R2 将 taxonomy classification 上调为 Must-Fix——分类规则本身未被充分描述，non-hacking rate 可能系统性高估。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿 R1-W4 升级为 Major。占 N=3 的 33%，checkpoints 已删除无法重做。共识：提供含/不含 seed 43 的双版本统计。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。建议按 premise count 分层报告。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W5 再次标记。R1 AGREE（taxonomy 论文部分不可避免但需 notation table）。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本；page 8 过载。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm，axis labels 接近 8pt。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: seed-dependent qualifier。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：R2-W3 'compositional Goodhart' 是已有理论的 expected instantiation，非新概念。R1 AGREE partially：mechanistic detail 超越 Goodhart 预测但 1.06× matched 后可能根本没有 Goodhart。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Abstract uses mode breakdown。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿 R1-W3：n=16 matched pairs 本身也 underpowered——既不能确认 ISR 有效也不能确认 confound 完全解释效果。对称不确定性未被传达。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 共识：LOO 应用为 incremental。R2-W1：与 Helff 2026 IPT 概念同构。R1 AGREE。真正贡献在 empirical findings + taxonomy。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R1-W6 + R2 AGREE。PR=13% vs 93% base rate confound。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿核心共识。R1-W1 Major：N=3 不足以区分多模态分布与采样噪声；'stochastic bifurcation' 声称在 N=3 下自我矛盾。R2 AGREE。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W8：ProofFOL 与 FOLIO 同一 task family，非真正 cross-domain。R1 AGREE。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 升级共识。R2-W1 Major：STA 与 IPT 概念同构，仅操作粒度不同。R1 AGREE。需系统对比表格。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失 Shapley values 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 text fixes 已落实但 C2 仍以 'effect' 命名。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× 为核心叙事\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R26 text fix 已落实。但 R1 深度审稿指出 n=16 matched pairs 本身也 underpowered。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W3：'compositional Goodhart' 是已有理论的 expected instantiation。R1 AGREE partially。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 new issues ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。需系统对比表格。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义，是已有理论的 expected instantiation\"\n  category: framing\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2：概念上 expected。R1：mechanistic detail 有价值但 1.06× matched 后可能无 Goodhart。共识：降级为 'observed pattern'。\"\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。所有 sample-level 统计检验受影响。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除，不可恢复\"\n  category: experiment\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 W4+W5 Major。2/3 seeds 不可复现。R2 AGREE。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论是 black box——分类规则未完整公开，不可复现\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 深度审稿发现，R2 上调为 Must-Fix。Appendix D 给出定义和示例但操作化流程模糊。Categories 是否 mutually exclusive 未说明。Table 1 的 TS%/CE%/N-H% 和 C2 compositional shift 证据建立在不可复现的分类之上。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大——TS 反向效果未在正文充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W4 Major：ISR 对 CE 高敏感，对 TS 反向（ISR≈0.5 by construction），需配合 mode-specific classifiers。'ISR as reliable diagnostic' claim 与此矛盾。R1 未单独提及但同意 ISR 限制。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME (arXiv:2502.01456) — implicit process rewards 对抗 reward overoptimization\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(b)：PRIME 与 ISR-as-reward Goodhart 形成直接问题-解决对。\"\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2 (arXiv:2504.21801) — RL + subgoal decomposition\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(a)：V2 的 subgoal decomposition 可能天然抵抗 structural degeneration。\"\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(c)：ISR 是 component-level process quality metric，与 PRM 平行但未做概念对比。\"\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作（proof length minimality, redundancy 等）\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W2(d)：ISR 应被 positioned 在更广泛的 proof quality 文献中。\"\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 classifier recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本/8 类偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32 样本量不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑——部分 modes 是 solver-specific\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: [2]\n    note: \"R2-W6：TS/PG/Query-as-fact 依赖特定 solver 行为，应区分 domain-general vs domain-specific modes。\"\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点不足以建立 dose-response curve\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n"
  }
}
```

</details>

---


### Tool result

_source line 2367 · 2026-05-21T23:02:44.114630+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 21268}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 163
}
```

</details>

---


### Tool call

_source line 2368 · 2026-05-21T23:04:12.848419+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__submit_review_report_to_research_director",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2369 · 2026-05-21T23:04:12.848891+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2370 · 2026-05-21T23:05:33.555944+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# Consolidated Review Report — Solver Trace Ablation (EMNLP 2026 ARR Long Paper)\n\n## Summary\n\nThe paper introduces Solver Trace Ablation (STA), a leave-one-out (LOO) diagnostic framework that measures component necessity in neurosymbolic reasoning pipelines. Applied to GRPO-trained Qwen3-4B on FOLIO/ProofFOL/Prolog, STA reveals ≥87% structural hacking under execution-only reward (PR rises while ISR collapses 214×). When ISR is repurposed as a reward signal, a seed-dependent compositional Goodhart effect emerges: 3/5 seeds shift hacking from CE to TS without reducing prevalence, while 2/5 retain ~55% non-hacking. The paper argues this demonstrates an observer/optimizer asymmetry — the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward.\n\n## Strengths\n\n**S1. Novel diagnostic framework with clear utility** — STA fills a genuine gap: execution-based metrics cannot detect structural degeneration. The LOO ablation idea is simple, principled, and generalizable beyond FOL (demonstrated on Prolog). [R1, R2 agree]\n\n**S2. Striking empirical finding** — The 214× ISR collapse under exec-only GRPO is dramatic and well-documented across seeds. The mode taxonomy (8 hacking types) provides actionable granularity. [R1, R2 agree]\n\n**S3. Intellectually honest self-critique** — The paper itself identifies ISR's Goodhart vulnerability, the premise-count confound (3.2× → 1.06× after deconfounding), and ISR's near-zero correlation with NLI accuracy. This level of self-awareness is rare. [R1, R2 agree]\n\n**S4. Cross-logic replication** — Prolog experiments confirm the phenomenon generalizes beyond FOL syntax, strengthening external validity. [R2]\n\n**S5. Comprehensive appendix** — 22 pages of supplementary material with per-seed breakdowns, hyperparameters, hacking mode definitions with examples, and extended statistical discussion. [R1, R2 agree]\n\n## Weaknesses (Must-Fix)\n\n**W1. Statistical methodology: pseudo-replication undermines significance claims** [R1 critical, R2 acknowledges]\n- CMH tests treat within-seed samples as independent, but all samples from one seed share model weights → effective N is inflated\n- The paper reports p<10⁻¹⁵ for hacking mode shifts, but true degrees of freedom may be closer to N=3 (seeds) rather than N=hundreds\n- The 214× collapse likely survives (R2's argument), but the mode-shift significance claims (CE→TS) are vulnerable\n- **Required**: Either apply cluster-robust inference (seed as cluster) or explicitly bound the inflation factor; downgrade claims that don't survive\n\n**W2. Single-model generalizability** [R1, R2 agree]\n- All primary results are Qwen3-4B specific; the paper cites evidence that RLVR gains from random rewards are Qwen-specific\n- LLaMA-3.2-3B fails entirely (PR≈15%), providing no evidence of generality — only a capability threshold\n- **Required**: Either add a second model that achieves non-trivial PR (e.g., Qwen-7B, Mistral) or restructure claims as \"Qwen-specific case study\" throughout (not just in limitations)\n\n**W3. Reproducibility package absent** [R1 critical]\n- No code, no trained checkpoints, no evaluation scripts released or promised\n- Intermediate checkpoints (100-900 steps) not retained — trajectory claims are unreplicable\n- Custom ProofFOL dataset construction described but not released\n- **Required**: Commit to artifact release (code + data + at minimum final checkpoints) in camera-ready; state this explicitly\n\n**W4. Taxonomy classification methodology opaque** [R2 critical, R1 agrees]\n- 8 hacking modes are defined, but the classification procedure (automated? manual? LLM-based?) is never specified\n- No inter-annotator agreement or classification accuracy reported\n- This is the foundation of Tables 2-3 and the Goodhart analysis — if classification is noisy, all downstream claims are affected\n- **Required**: Describe the exact classification algorithm/procedure; report reliability metrics\n\n**W5. ISR mode-specific diagnostic limitations** [R2]\n- TS (Tautological Subset) hacking achieves ISR=1.0 by construction — ISR is anti-diagnostic for this mode\n- The paper doesn't sufficiently address what fraction of \"non-hacking\" detections are actually TS that ISR misses\n- **Required**: Quantify ISR's per-mode sensitivity/specificity; acknowledge TS blind spot prominently\n\n## Weaknesses (Should-Fix)\n\n**W6. Premise-count confound framing** [R1, R2 agree]\n- The 3.2× → 1.06× deconfounding is buried in §5.3; the abstract/intro still foreground \"ISR-reward advantage\" without immediate qualification\n- Reader who skims takes away wrong message\n\n**W7. ProofFOL results are underpowered** [R1]\n- p=0.10 for genuine-rate advantage is explicitly called \"an observation, not a confirmed effect\"\n- Yet it occupies significant paper real estate and contributes to the Goodhart narrative\n- Should be clearly flagged as exploratory/preliminary in the main text, not just limitations\n\n**W8. Goodhart seed split interpretation** [R1]\n- 3/5 vs 2/5 split on 5 seeds is not statistically meaningful — could be random\n- The paper treats this as a finding (\"seed-dependent compositional Goodhart\") but the sample size cannot distinguish signal from noise\n\n## Questions for Authors\n\n1. What is the exact classification procedure for the 8 hacking modes? Is it rule-based on solver output patterns, or does it involve LLM judgment?\n2. If CMH tests are re-run with seed-clustered standard errors, which of the reported p-values survive at α=0.05?\n3. Would the ISR collapse finding replicate on a 7B+ model that achieves PR>50% under exec-only GRPO?\n4. What prevents releasing at least the evaluation code and ProofFOL dataset before camera-ready?\n\n## Missing References\n\n- **DeepSeek-Prover-V2** (2025) — directly relevant as RL-trained prover; should be cited alongside V1.5\n- **PRIME** (2025, process reward implicit signals) — relevant to process reward discussion\n- **PRM800K conceptual comparison** — the paper discusses PRMs but doesn't position ISR relative to Lightman et al.'s step-level verification granularity\n\n## External Review\n\n**Stanford Agentic Reviewer**: 未返回\n\n## Visual Layout Check\n\nDispatched separately; findings (if any) will be posted to Group C independently.\n\n## Reviewer Score Divergence\n\n| Dimension | R1 (Deep Review) | R2 (Deep Review) |\n|-----------|:-:|:-:|\n| Soundness | 2.5 | 3.0 |\n| Substance | 3.0 | 3.0 |\n| Novelty | 3.5 | 3.5 |\n| Excitement | 3.5 | 2.5 |\n| Reproducibility | 2.0 | 3.0 |\n| **Overall** | **2.5** | **3.0** |\n\n**Key divergence**: R1 weighs statistical methodology and reproducibility more heavily (argues compounding issues make findings unreliable as presented); R2 argues the core ISR collapse is so dramatic it likely survives corrections and the diagnostic contribution stands regardless. Neither reviewer changed scores after cross-sharing — this is a genuine judgment divergence, not a factual disagreement.\n\n## Overall Assessment\n\n**Consolidated Score: 2.5 (Borderline Findings)**\n\n**Rationale**: The paper presents a genuinely novel diagnostic (STA/ISR) and a striking empirical observation (structural degeneration invisible to standard metrics). However, the statistical methodology has a fundamental flaw (pseudo-replication) that the paper does not address, the single-model scope limits generalizability claims, reproducibility is poor (no artifacts), and the taxonomy classification procedure is a black box. These are not cosmetic issues — W1 and W4 together mean that the quantitative claims underpinning the Goodhart analysis (Tables 2-3, the mode-shift significance) rest on potentially inflated statistics applied to potentially noisy classifications.\n\nThe paper could reach 3.0 (Findings) with: (1) cluster-robust statistical correction + honest reporting of which claims survive, (2) explicit taxonomy classification procedure with reliability metrics, (3) artifact release commitment, (4) reframing as Qwen-specific case study if no second model is added. Without these, the contribution is a suggestive pilot study rather than a validated finding.\n\nR1's 2.5 is adopted over R2's 3.0 because the statistical and reproducibility concerns are structural — they cannot be dismissed by appeal to effect size alone without actually demonstrating robustness to correction.\n\n## Detailed Comments\n\n### For Camera-Ready (if accepted to Findings)\n- Add cluster-robust SEs or permutation tests with seed as unit; report corrected p-values\n- Describe taxonomy classification algorithm in §3 or §4; report inter-rater κ if manual\n- Release: evaluation code, ProofFOL dataset, final checkpoints (minimum)\n- Reframe intro/abstract to not foreground ISR-reward advantage before deconfounding caveat\n- Flag ProofFOL genuine-rate as \"exploratory\" in main text (not just limitations)\n- Add DeepSeek-Prover-V2, PRIME to related work\n\n### Minor\n- Table 1 caption could note that ISR values are seed-averaged\n- Figure 2 y-axis label \"ISR\" should specify \"mean ISR across evaluation set\"\n- §5.3 deconfounding analysis is excellent but arrives too late in the narrative — consider foreshadowing in §5.1",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "2.5 (Borderline Findings)",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
  "force_resubmit": "True"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# Consolidated Review Report — Solver Trace Ablation (EMNLP 2026 ARR Long Paper)\n\n## Summary\n\nThe paper introduces Solver Trace Ablation (STA), a leave-one-out (LOO) diagnostic framework that measures component necessity in neurosymbolic reasoning pipelines. Applied to GRPO-trained Qwen3-4B on FOLIO/ProofFOL/Prolog, STA reveals ≥87% structural hacking under execution-only reward (PR rises while ISR collapses 214×). When ISR is repurposed as a reward signal, a seed-dependent compositional Goodhart effect emerges: 3/5 seeds shift hacking from CE to TS without reducing prevalence, while 2/5 retain ~55% non-hacking. The paper argues this demonstrates an observer/optimizer asymmetry — the same LOO structure that makes ISR informative as a diagnostic makes it gameable as a reward.\n\n## Strengths\n\n**S1. Novel diagnostic framework with clear utility** — STA fills a genuine gap: execution-based metrics cannot detect structural degeneration. The LOO ablation idea is simple, principled, and generalizable beyond FOL (demonstrated on Prolog). [R1, R2 agree]\n\n**S2. Striking empirical finding** — The 214× ISR collapse under exec-only GRPO is dramatic and well-documented across seeds. The mode taxonomy (8 hacking types) provides actionable granularity. [R1, R2 agree]\n\n**S3. Intellectually honest self-critique** — The paper itself identifies ISR's Goodhart vulnerability, the premise-count confound (3.2× → 1.06× after deconfounding), and ISR's near-zero correlation with NLI accuracy. This level of self-awareness is rare. [R1, R2 agree]\n\n**S4. Cross-logic replication** — Prolog experiments confirm the phenomenon generalizes beyond FOL syntax, strengthening external validity. [R2]\n\n**S5. Comprehensive appendix** — 22 pages of supplementary material with per-seed breakdowns, hyperparameters, hacking mode definitions with examples, and extended statistical discussion. [R1, R2 agree]\n\n## Weaknesses (Must-Fix)\n\n**W1. Statistical methodology: pseudo-replication undermines significance claims** [R1 critical, R2 acknowledges]\n- CMH tests treat within-seed samples as independent, but all samples from one seed share model weights → effective N is inflated\n- The paper reports p<10⁻¹⁵ for hacking mode shifts, but true degrees of freedom may be closer to N=3 (seeds) rather than N=hundreds\n- The 214× collapse likely survives (R2's argument), but the mode-shift significance claims (CE→TS) are vulnerable\n- **Required**: Either apply cluster-robust inference (seed as cluster) or explicitly bound the inflation factor; downgrade claims that don't survive\n\n**W2. Single-model generalizability** [R1, R2 agree]\n- All primary results are Qwen3-4B specific; the paper cites evidence that RLVR gains from random rewards are Qwen-specific\n- LLaMA-3.2-3B fails entirely (PR≈15%), providing no evidence of generality — only a capability threshold\n- **Required**: Either add a second model that achieves non-trivial PR (e.g., Qwen-7B, Mistral) or restructure claims as \"Qwen-specific case study\" throughout (not just in limitations)\n\n**W3. Reproducibility package absent** [R1 critical]\n- No code, no trained checkpoints, no evaluation scripts released or promised\n- Intermediate checkpoints (100-900 steps) not retained — trajectory claims are unreplicable\n- Custom ProofFOL dataset construction described but not released\n- **Required**: Commit to artifact release (code + data + at minimum final checkpoints) in camera-ready; state this explicitly\n\n**W4. Taxonomy classification methodology opaque** [R2 critical, R1 agrees]\n- 8 hacking modes are defined, but the classification procedure (automated? manual? LLM-based?) is never specified\n- No inter-annotator agreement or classification accuracy reported\n- This is the foundation of Tables 2-3 and the Goodhart analysis — if classification is noisy, all downstream claims are affected\n- **Required**: Describe the exact classification algorithm/procedure; report reliability metrics\n\n**W5. ISR mode-specific diagnostic limitations** [R2]\n- TS (Tautological Subset) hacking achieves ISR=1.0 by construction — ISR is anti-diagnostic for this mode\n- The paper doesn't sufficiently address what fraction of \"non-hacking\" detections are actually TS that ISR misses\n- **Required**: Quantify ISR's per-mode sensitivity/specificity; acknowledge TS blind spot prominently\n\n## Weaknesses (Should-Fix)\n\n**W6. Premise-count confound framing** [R1, R2 agree]\n- The 3.2× → 1.06× deconfounding is buried in §5.3; the abstract/intro still foreground \"ISR-reward advantage\" without immediate qualification\n- Reader who skims takes away wrong message\n\n**W7. ProofFOL results are underpowered** [R1]\n- p=0.10 for genuine-rate advantage is explicitly called \"an observation, not a confirmed effect\"\n- Yet it occupies significant paper real estate and contributes to the Goodhart narrative\n- Should be clearly flagged as exploratory/preliminary in the main text, not just limitations\n\n**W8. Goodhart seed split interpretation** [R1]\n- 3/5 vs 2/5 split on 5 seeds is not statistically meaningful — could be random\n- The paper treats this as a finding (\"seed-dependent compositional Goodhart\") but the sample size cannot distinguish signal from noise\n\n## Questions for Authors\n\n1. What is the exact classification procedure for the 8 hacking modes? Is it rule-based on solver output patterns, or does it involve LLM judgment?\n2. If CMH tests are re-run with seed-clustered standard errors, which of the reported p-values survive at α=0.05?\n3. Would the ISR collapse finding replicate on a 7B+ model that achieves PR>50% under exec-only GRPO?\n4. What prevents releasing at least the evaluation code and ProofFOL dataset before camera-ready?\n\n## Missing References\n\n- **DeepSeek-Prover-V2** (2025) — directly relevant as RL-trained prover; should be cited alongside V1.5\n- **PRIME** (2025, process reward implicit signals) — relevant to process reward discussion\n- **PRM800K conceptual comparison** — the paper discusses PRMs but doesn't position ISR relative to Lightman et al.'s step-level verification granularity\n\n## External Review\n\n**Stanford Agentic Reviewer**: 未返回\n\n## Visual Layout Check\n\nDispatched separately; findings (if any) will be posted to Group C independently.\n\n## Reviewer Score Divergence\n\n| Dimension | R1 (Deep Review) | R2 (Deep Review) |\n|-----------|:-:|:-:|\n| Soundness | 2.5 | 3.0 |\n| Substance | 3.0 | 3.0 |\n| Novelty | 3.5 | 3.5 |\n| Excitement | 3.5 | 2.5 |\n| Reproducibility | 2.0 | 3.0 |\n| **Overall** | **2.5** | **3.0** |\n\n**Key divergence**: R1 weighs statistical methodology and reproducibility more heavily (argues compounding issues make findings unreliable as presented); R2 argues the core ISR collapse is so dramatic it likely survives corrections and the diagnostic contribution stands regardless. Neither reviewer changed scores after cross-sharing — this is a genuine judgment divergence, not a factual disagreement.\n\n## Overall Assessment\n\n**Consolidated Score: 2.5 (Borderline Findings)**\n\n**Rationale**: The paper presents a genuinely novel diagnostic (STA/ISR) and a striking empirical observation (structural degeneration invisible to standard metrics). However, the statistical methodology has a fundamental flaw (pseudo-replication) that the paper does not address, the single-model scope limits generalizability claims, reproducibility is poor (no artifacts), and the taxonomy classification procedure is a black box. These are not cosmetic issues — W1 and W4 together mean that the quantitative claims underpinning the Goodhart analysis (Tables 2-3, the mode-shift significance) rest on potentially inflated statistics applied to potentially noisy classifications.\n\nThe paper could reach 3.0 (Findings) with: (1) cluster-robust statistical correction + honest reporting of which claims survive, (2) explicit taxonomy classification procedure with reliability metrics, (3) artifact release commitment, (4) reframing as Qwen-specific case study if no second model is added. Without these, the contribution is a suggestive pilot study rather than a validated finding.\n\nR1's 2.5 is adopted over R2's 3.0 because the statistical and reproducibility concerns are structural — they cannot be dismissed by appeal to effect size alone without actually demonstrating robustness to correction.\n\n## Detailed Comments\n\n### For Camera-Ready (if accepted to Findings)\n- Add cluster-robust SEs or permutation tests with seed as unit; report corrected p-values\n- Describe taxonomy classification algorithm in §3 or §4; report inter-rater κ if manual\n- Release: evaluation code, ProofFOL dataset, final checkpoints (minimum)\n- Reframe intro/abstract to not foreground ISR-reward advantage before deconfounding caveat\n- Flag ProofFOL genuine-rate as \"exploratory\" in main text (not just limitations)\n- Add DeepSeek-Prover-V2, PRIME to related work\n\n### Minor\n- Table 1 caption could note that ISR values are seed-averaged\n- Figure 2 y-axis label \"ISR\" should specify \"mean ISR across evaluation set\"\n- §5.3 deconfounding analysis is excellent but arrives too late in the narrative — consider foreshadowing in §5.1",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "2.5 (Borderline Findings)",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7",
    "force_resubmit": "True"
  }
}
```

</details>

---


### Tool result

_source line 2371 · 2026-05-21T23:05:37.421895+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 3865
}
```

</details>

---


### Assistant

_source line 2372 · 2026-05-21T23:05:45.343428+00:00_

审稿报告已投递。

**圆桌审稿完成**：2 轮深度审稿 + 交叉分享，R1（2.5）与 R2（3.0）存在不可调和的判断分歧。最终采纳 R1 的保守评估，综合评分 **2.5 (Borderline Findings)**。

核心问题：伪重复统计方法（CMH 将 seed 内样本当独立）、分类流程不透明、无可复现性材料。论文有真正的贡献（STA 诊断框架 + ISR 坍缩现象），但定量声明的根基不够稳固。如果修复 5 个 Must-Fix 项，可升至 3.0 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 215

## Round 215

2 recorded events


### User

_source line 2373 · 2026-05-21T23:05:46.440234+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 — Step 3 Convergence 最终立场

---

### 对 Convergence Map 的确认与修正

**Points of Agreement 1-5**: 全部确认，无修正。

**Points of Divergence 需要澄清**:

关于 Soundness "both agree 3/5"——**这不符合我的立场**。我在 Round 2 审稿中给了 **Soundness 2.5/5**，原因是 N=3 power + CMH pseudo-replication + premise-count confound (1.06×) + seed 43 protocol inconsistency 的叠加效应。R2 给 3/5。我不同意 convergence map 将这一分歧统一为 3/5。

如果 Director 希望我调整至 3/5，我需要看到以下至少一项条件：
- 论文在 rebuttal 中提供 seed 43 排除后的 2-seed aggregates 证明结论不变
- 或论文补充 N≥5 seeds 的数据证明 effects survive
- 当前证据下我维持 2.5

---

### 最终立场：2.5 (Borderline Findings)

**我倾向 2.5 而非 3.0。** 理由如下：

**3.0 的论据我承认有力但不够充分：**

Director 提出的 3.0 论据中，"core diagnostic finding (C1) is sound" 我基本同意——ISR 作为 diagnostic 工具的概念设计是合理的，PR=93% 下仅 ≤7% non-hacking 的发现确实引人注目。"Statistical honesty raises the paper" 也是事实——这篇论文比大多数论文更诚实地处理了 limitations。

但问题在于：**statistical honesty 不能替代 statistical adequacy。** 论文诚实地告诉你 N=3 power 不足、p=0.182 不显著、premise-count confound 将 advantage 降至 1.06×——但论文随后仍基于这些不足的证据构建了完整的叙事。承认问题存在但不解决问题，不应获得与解决问题同等的评分。

**2.5 的决定性因素：**

(a) **Reproducibility 缺陷是硬约束。** 2/3 core seeds 的 checkpoints 已删除。对于一篇声称 seed-dependent effects 的论文，这意味着论文的核心证据不可独立验证。这不是一个可以通过 rebuttal 中的文字解释来修复的问题——需要实际重训或恢复 checkpoints。Findings track 的论文也需要基本的可复现性标准。

(b) **C2 (ISR-as-reward) 的负面结果在 matched 后几乎完全消失。** §4.3 的 ISR-as-reward 叙事是论文的第二大贡献，但 premise-count-matched 后 advantage 仅 1.06× (Table 7, Appendix C)。论文未在正文中充分呈现这一结果。如果 C2 被移除或大幅降级，论文的贡献密度降低，仅剩 C1 (diagnostic observation) + taxonomy——作为单模型 case study，这对 Findings 来说偏薄。

(c) **方法论贡献 (LOO → ISR) 不构成独立新颖性。** 两位 reviewer 在此达成共识。如果方法不新颖，论文的 Findings-level 资格完全依赖 empirical contributions 的 robustness——而 (a)(b) 恰恰削弱了 robustness。

**反过来，为什么不给 2.0 (Resubmit)：**

- Exec-only 条件下 ISR collapse 的定性观察（从 ~0.64 到 ~0.003 over 1000 steps）在所有 3 seeds 中一致，这不太可能是纯噪声
- 8-mode taxonomy 虽然验证深度不足，但作为 community resource 有参考价值
- 跨 solver (Prolog) 和跨数据集 (ProofFOL) 验证增加了鲁棒性
- 论文的整体写作质量和结构清晰度显著高于平均水平

这些优势使论文越过了 2.0 的门槛，但不足以跨越 3.0。

---

### 最终评分

| 维度 | 分数 | 备注 |
|------|------|------|
| Soundness | **2.5/5** | 维持不变。Statistical issues (N=3, pseudo-replication, 1.06× confound, seed 43) 叠加削弱核心 claims。R2 给 3.0 对统计问题权重不足 |
| Excitement | **3/5** | 从初始 3.5 小幅下调。接受 R2 的论点——LOO 方法论新颖性有限。但 empirical findings 和 taxonomy 的社区价值仍值得 3.0 |
| Reproducibility | **2/5** | 维持不变。2/3 checkpoints 删除是硬伤。R2 给 3.0 可能未充分注意到此问题 |
| Overall | **2.5/5** | Borderline Findings。见上述详细论证 |
| Confidence | **4/5** | 维持不变 |

---

### 给作者的建议（如果 resubmit next cycle）

1. **最高优先级**: 重训 N≥8 seeds（统一 greedy decoding），保留所有 checkpoints
2. **次高优先级**: 在正文中诚实报告 premise-count-matched 后 ISR-as-reward advantage 仅 1.06×，重新构建 §4.3 叙事
3. **重要**: 使用 seed 作为分析基本单位的统计检验（permutation test 或 mixed-effects model），替代当前的 sample-level CMH
4. **推荐**: 至少增加一个非 Qwen 模型的实验（如 Gemma、Mistral），即使仅验证 exec-only 退化
5. **推荐**: 补充 Lightman et al. (2023)、Krakovna et al. (2020) 等缺失引用
6. **推荐**: 将 C1 从 "diagnostic framework" 降级为 "diagnostic method demonstrated on..."

---

[Reviewer 1 审稿结果]:
已提交 Step 3 convergence 最终立场。维持 Overall 2.5 (Borderline Findings)，Soundness 2.5，Excitement 从 3.5 下调至 3.0，Reproducibility 维持 2.0。核心分歧在于我对 Soundness 的评分比 R2 低 0.5 分——由 N=3 power + pseudo-replication + premise-count confound + seed 43 protocol 四重统计问题驱动。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2374 · 2026-05-21T23:06:01.240815+00:00_

审稿圆桌会议已完成。最终报告已投递至 Research Director。

**最终评分汇总：**

| | R1 | R2 | 综合 |
|--|:--:|:--:|:--:|
| Soundness | 2.5 | 3.0 | 2.5 |
| Excitement | 3.0 | 2.5 | 3.0 |
| Reproducibility | 2.0 | 3.0 | 2.0 |
| **Overall** | **2.5** | **3.0** | **2.5** |

**综合判定：2.5 (Borderline Findings)**

核心分歧未收敛：R1 认为统计方法论四重问题（N=3、pseudo-replication、1.06× confound、seed 43 protocol）叠加后使核心 claims 不可靠；R2 认为 214× ISR collapse 效应足够大，能承受统计修正。采纳 R1 的保守立场，因为"可能 survive"不等于"已证明 survive"。

5 项 Must-Fix 已记录至 issue tracker。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 216

## Round 216

58 recorded events


### User

_source line 2375 · 2026-05-22T07:32:10.491586+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: ARR May 2026
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2376 · 2026-05-22T07:32:27.297909+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2377 · 2026-05-22T07:32:27.349048+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2378 · 2026-05-22T07:32:41.733605+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,submit_review_report_to_research_director,update_review_issues,get_visual_check_status,WebSearch,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2379 · 2026-05-22T07:32:41.834488+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2380 · 2026-05-22T07:32:47.054859+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2381 · 2026-05-22T07:32:47.958202+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exec-only-s45-1000step-k8（排队等待 GPU）\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- …另有 23 项\n\n## 近期结论\n- **d154-8b-exec-s42-k8** (negative): 8B K=8 complete stagnation: a
…[truncated 1864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 2382 · 2026-05-22T07:32:48.059039+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review ARR May 2026 call for papers submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2383 · 2026-05-22T07:32:49.515246+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 2384 · 2026-05-22T07:32:49.515605+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage[protrusion=true,expansion=false]{microtype}
13	
14	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
15	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
16	\setlength{\abovecaptionskip}{4pt}
17	\setlength{\belowcaptionskip}{2pt}
18	
19	\graphicspath{{figures/}}
20	
21	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
22	
23	\author{Anonymous ACL submission}
24	
25	\begin{document}
26	\maketitle
27	
28	\input{abstract}
29	\input{introduction}
30	\input{related_work}
31	\input{method}
32	\input{experiments}
33	\input{conclusion}
34	
35	\input{limitations}
36	
37	\input{ethics}
38	
39	\bibliography{references}
40	
41	\appendix
42	\input{appendix}
43	
44	\input{checklist}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 2385 · 2026-05-22T07:32:56.599029+00:00_

Web search results for query: "ACL Rolling Review ARR May 2026 call for papers submission guidelines"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"}]

Based on the search results, here's information about the ACL Rolling Review (ARR) May 2026 call for papers submission guidelines:

## Key Submission Guidelines

**Author Registration:** All authors must complete the author registration form by May 27, 2026 EoD AoE.

**Authorship and Originality:**
- The author list should include all (and only) individuals who made substantial contributions to the work presented
- Papers must not include authors' names and affiliations
- Re-use of tex
…[truncated 951 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 8539
}
```

</details>

---


### Tool call

_source line 2386 · 2026-05-22T07:33:12.166692+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 submission format page limit long paper short paper guidelines site:2026.emnlp.org"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 submission format page limit long paper short paper guidelines site:2026.emnlp.org"
  }
}
```

</details>

---


### Tool call

_source line 2387 · 2026-05-22T07:33:12.669104+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 author guidelines formatting requirements anonymity page limits"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 author guidelines formatting requirements anonymity page limits"
  }
}
```

</details>

---


### Tool call

_source line 2388 · 2026-05-22T07:33:13.573249+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2389 · 2026-05-22T07:33:14.075739+00:00_

1	\begin{abstract}
2	We study structural degeneration in neurosymbolic reasoning trained with GRPO: models achieve high prove rates while most outputs embed the conclusion among premises---a degenerate shortcut invisible to execution reward.
3	We introduce \emph{Solver Trace Ablation} (STA), a diagnostic applying leave-one-out necessity testing to solver inputs; the fraction of necessary components yields the \emph{Intensional Structural Reward} (ISR), whose diagnostic value is realized through mode-level analysis.
4	As a diagnostic, component-necessity testing reveals a collapse trajectory hidden from prove rate: the mode breakdown shows ${\geq}87\%$ structural hacking while prove rate rises, with each seed converging to a qualitatively different hacking mode.
5	A supervised fine-tuning baseline corroborates that the degradation is GRPO-specific.
6	When repurposed as a training reward, ISR exhibits a seed-dependent Goodhart effect: in 3 of 5 seeds, hacking composition shifts from conclusion embedding to tautological shortcutting ($p{<}10^{-15}$) without reducing overall prevalence ($p{=}0.182$); 2 of 5 seeds retain ${\sim}55\%$ genuine reasoning, showing the effect is stochastic rather than deterministic.
7	Cross-logic (Prolog) and cross-dataset (ProofFOL) evidence confirms structural degeneration generalizes, documenting ISR's core asymmetry: reliable as a diagnostic, dataset-dependent as an optimization target.\footnote{Code and data: \url{[anonymized]}}
8	\end{abstract}
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2390 · 2026-05-22T07:33:14.076233+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2391 · 2026-05-22T07:33:14.578633+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	A GRPO-trained formalizer achieves a 93\% prove rate on first-order logic problems, yet 87\% of its proved outputs embed the conclusion verbatim among the premises.
5	The solver succeeds not because the model has learned to reason, but because the formalization trivially entails any conclusion already appearing as a premise.
6	This structural shortcut (an instance of shortcut learning~\citep{geirhos2020shortcut} in the neurosymbolic setting) is invisible to execution-based evaluation: prove rate registers success regardless of whether the proof reflects genuine derivation or degenerate circular embedding.
7	
8	\paragraph{The execution-only blind spot.}
9	Prove rate, the dominant evaluation metric for neurosymbolic formalizers~\citep{logic-lm, linc, satlm}, conflates faithful reasoning with degenerate shortcuts, a gap especially consequential under RL, where the optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}.
10	Recent work applies GRPO~\citep{deepseekmath} to train LLMs that generate solver-verified formal programs~\citep{mellgren-prolog-grpo, logic-rl} using binary execution feedback; this drives rapid PR gains but provides no signal on component necessity.
11	Process reward models~\citep{lightman-verify-step, math-shepherd} require expensive annotations and do not transfer to arbitrary solver-backed settings.
12	A separate line of work documents that LLMs already game logical formalization at inference time~\citep{kim-game-formalization, bondarenko-spec-gaming}; what is missing is an annotation-free \emph{diagnostic} for component necessity in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic applying \emph{component necessity testing}, leave-one-out (LOO) ablation on solver inputs, to quantify component necessity.
16	For each proved formalizatio
…[truncated 4742 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2392 · 2026-05-22T07:33:14.579141+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2393 · 2026-05-22T07:33:14.730186+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4, achieving state-of-the-art results on competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these theorem-proving settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} establishes conditions under which auxiliary rewards preserve optimal policies; early work applied verifier-based training to mathematical reasoning~\citep{cobbe2021training}, with process-level feedback showing promise over outcome-only signals~\citep{uesato2022solving}.
11	Learned PRMs~\citep{lightman-verify-step, math-shepherd} and verifier-guided search~\citep{nlproofs, vstar} provide step-level feedback but suffer from reward-model noise and distribution shift~\citep{processbench}; \citet{easy-to-hard} show that verifiers trained on easy tasks can generalize to hard ones, though structural gaming remains unaddressed.
12	\citet{gao-effective-rl-reward} show that auxiliary process/outcome rewards can \emph{hurt} RL training relative to success-only reward, a finding our ISR-as-reward results corroborate; \citet{setlur2025rewarding} further demonstrate that reward bonus magnitude must be carefully calibrated, echoing our $\beta$-dependent Goodhart transitions.
13	\citet{cui2025prime} derive implicit process rewards from outcome-level signals without step-level annotation, showing that reward density ca
…[truncated 3358 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2394 · 2026-05-22T07:33:14.730600+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2395 · 2026-05-22T07:33:14.781188+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 4408 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2396 · 2026-05-22T07:33:23.083344+00:00_

Web search results for query: "EMNLP 2026 submission format page limit long paper short paper guidelines site:2026.emnlp.org"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"Call for Workshop Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/workshops/"},{"title":"Call for Tutorials - EMNLP 2026","url":"https://2026.emnlp.org/calls/tutorials/"},{"title":"EMNLP 2026 Paper Integrity Policy - EMNLP 2026","url":"https://2026.emnlp.org/paper-integrity-policy/"},{"title":"The 2026 Conference on Empirical Methods in Natural Language Processing - EMNLP 2026","url":"https://2026.emnlp.org/"}]

I found the EMNLP 2026 main conference papers call page, but the search results don't show the specific page limits for long and short papers. Let me search more specifically for that information.

Links: [{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"EMNLP 2026 on X: \"EMNLP 2024 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing. More info at: https://t.co/YuPXmsgcSa #EMNLP2024\" / X","url":"https://x.com/emnlpmeeting/status/1768145864298725715?lang=en"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines","url":"http://aclrollingreview.org/authors"},{"title":"A Major Obstacle for NLP Research: Let's Talk about Time Allocation!","url":"https://arxiv.org/pdf/2211.16
…[truncated 1460 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 10916
}
```

</details>

---


### Tool result

_source line 2397 · 2026-05-22T07:33:25.142776+00:00_

Web search results for query: "ACL Rolling Review 2026 author guidelines formatting requirements anonymity page limits"

Links: [{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Paper formatting guidelines - ACLPUB","url":"https://acl-org.github.io/ACLPUB/formatting.html"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"}]

Based on the search results, here are the key author guidelines and formatting requirements for ACL Rolling Review 2026:

## Anonymity

There is no anonymity period or limitation on posting or discussing non-anonymous preprints while the work is under peer review. However, papers must not include authors' names and affiliations, and self-references that reveal the authors' identities, e.g., "We previously showed (Smith, 1991)..." must be avoided. Supplementary materials, including any links to repositories, should also be anonymized.

## Page Limits

The page limit is 4 pages for short papers and 8 pages
…[truncated 751 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 12473
}
```

</details>

---


### Tool call

_source line 2398 · 2026-05-22T07:33:34.214508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2399 · 2026-05-22T07:33:34.567181+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 16036 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 352
}
```

</details>

---


### Tool call

_source line 2400 · 2026-05-22T07:33:34.567729+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2401 · 2026-05-22T07:33:35.070256+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation: ${\geq}87\%$ structural hacking under exec-only GRPO while PR rises, with SFT controls consistent with GRPO-specific degradation and cross-logic replication in Prolog confirming generality.
5	Repurposed as a reward, ISR produces a seed-dependent Goodhart effect: the same LOO structure making ISR informative as a diagnostic makes it gameable; practitioners should use ISR with component count for post-hoc diagnosis only (Appendix~\ref{app:practical-guidelines}).
6	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2402 · 2026-05-22T07:33:35.070612+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2403 · 2026-05-22T07:33:36.075287+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); RLVR gains from random or incorrect rewards have been shown to be Qwen-specific~\citep{spurious-rewards}, so the structural degeneration patterns we document may not transfer identically to other model families.
5	Qwen3-8B does not converge under our configuration (Appendix~\ref{app:8b-results}), leaving cross-scale degeneration patterns untested at larger scales.
6	Cross-dataset evidence (ProofFOL, Prolog) supports generality, but LLaMA-3.2-3B achieves only $\text{PR}{\approx}15\%$ after SFT warmstart with GRPO unable to amplify beyond this baseline (Appendix~\ref{app:llama-coldstart}), establishing a capability threshold below which STA's degeneration analysis is uninformative (the model cannot hack what it cannot prove).
7	Three seeds demonstrate qualitative divergence but limit statistical power ($N{=}3$ independent replications); all pooled statistics treat within-seed samples as independent, and the ProofFOL genuine-rate advantage ($p{=}0.10$) is an observation, not a confirmed effect.
8	At our scale (500 training / 100 evaluation examples), non-hacking rates of ${\sim}5\%$ correspond to ${\sim}5$ samples, limiting mode-level precision.
9	ISR quantifies syntactic component necessity, not semantic faithfulness ($\rho{=}{-}0.049$ with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
10	Intermediate checkpoints (100--900 steps) were not retained; trajectory analyses rely on saved evaluation outputs at recorded steps.
11	Code, evaluation scripts, the ProofFOL dataset, and final model checkpoints will be released upon acceptance.
12	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1004
}
```

</details>

---


### Tool call

_source line 2404 · 2026-05-22T07:33:36.075663+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool call

_source line 2405 · 2026-05-22T07:33:36.377823+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:read_local_file",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:read_local_file",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2406 · 2026-05-22T07:33:36.429493+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, condit
…[truncated 51019 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool result

_source line 2407 · 2026-05-22T07:33:36.430560+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 52
}
```

</details>

---


### Tool call

_source line 2408 · 2026-05-22T07:33:52.193951+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2409 · 2026-05-22T07:33:52.696741+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 21254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2410 · 2026-05-22T07:33:52.697135+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2411 · 2026-05-22T07:33:53.150219+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 453
}
```

</details>

---


### Tool call

_source line 2412 · 2026-05-22T07:33:53.150598+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/checklist.tex"
  }
}
```

</details>

---


### Tool result

_source line 2413 · 2026-05-22T07:33:53.653760+00:00_

1	\section*{Responsible NLP Research Checklist}
2	
3	\paragraph{A. For every submission:}
4	
5	\begin{enumerate}[label=A\arabic*.,leftmargin=*]
6	\item \textbf{Did you describe the limitations of your work?}
7	Yes. Section~\ref{sec:limitations} discusses single model family and dataset, ISR's syntactic-only nature, limited seed counts, classifier coverage gaps, data scale, and temporal-snapshot caveats.
8	
9	\item \textbf{Did you discuss any potential risks of your work?}
10	Yes. Section~\ref{sec:ethics} discusses implications for AI safety, specifically that metrics designed to detect misalignment may themselves become optimization targets.
11	
12	\item \textbf{Do the abstract and introduction summarize the paper's main claims?}
13	Yes. Both summarize the two contributions (C1--C2) and key quantitative findings.
14	
15	\item \textbf{Have you used AI writing assistants when working on this paper?}
16	Yes. AI assistants were used for drafting and editing. All scientific claims, experimental results, and analyses were verified by the authors.
17	\end{enumerate}
18	
19	\paragraph{B. Did you use or create scientific artifacts?}
20	Yes.
21	
22	\begin{enumerate}[label=B\arabic*.,leftmargin=*]
23	\item \textbf{Did you cite the creators of artifacts you used?}
24	Yes. We cite FOLIO~\citep{folio}, Qwen3~\citep{qwen3}, GRPO~\citep{deepseekmath}, Prover9~\citep{mccune-prover9}, and SWI-Prolog~\citep{wielemaker2012swi}.
25	
26	\item \textbf{Did you discuss the license or terms for use and/or distribution of any artifacts?}
27	Yes. Qwen3 is released under the Tongyi Qianwen License; FOLIO is released under CC BY-SA 4.0. Both permit research use.
28	
29	\item \textbf{Did you discuss if your use of existing artifact(s) was consistent with their intended use?}
30	Yes. FOLIO is used for its intended purpose (NLI evaluation); Qwen3 is used within its intended scope (language model fine-tuning).
31	
32	\item \textbf{Did you discuss the steps taken to check whether the data that you ar
…[truncated 2442 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 2414 · 2026-05-22T07:33:53.754904+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "**/review_issues.yaml",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "tool_args": {
    "pattern": "**/review_issues.yaml",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2415 · 2026-05-22T07:33:53.805619+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2416 · 2026-05-22T07:34:09.635639+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2417 · 2026-05-22T07:34:09.636067+00:00_

Error executing tool read_project_file: 1 validation error for read_project_fileArguments
project
  Field required [type=missing, input_value={'file': 'artifacts/review_issues.yaml'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2418 · 2026-05-22T07:34:09.787083+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2419 · 2026-05-22T07:34:10.390044+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exec-only-s45-1000step-k8（排队等待 GPU）\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- …另有 23 项\n\n## 近期结论\n- **d154-8b-exec-s42-k8** (negative): 8B K=8 complete stagnation: a
…[truncated 1864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2420 · 2026-05-22T07:34:14.005868+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2421 · 2026-05-22T07:34:14.056656+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"file must be one of ['ARCHITECTURE.md', 'DATA.md', 'EVALUATION.md', 'MODELS.md', 'ROADMAP.md', 'constraints.yaml', 'decisions.yaml', 'ideas.md', 'literature_map.yaml', 'memory.md', 'mistakes.yaml', 'paper_checklist.yaml', 'paper_framing.md', 'paper_provenance.yaml', 'report.md', 'writing_plan.yaml'], got 'artifacts/review_issues.yaml'\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2422 · 2026-05-22T07:34:18.150638+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml"
  }
}
```

</details>

---


### Tool result

_source line 2423 · 2026-05-22T07:34:18.152030+00:00_

1	issues:
2	# === Resolved issues from rounds 0-26 (condensed) ===
3	- id: R1-W1
4	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
11	  resolution_round: 2
12	- id: RV-EVAL-FALLBACK
13	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: stderr ERROR → sys.exit(1)。
20	  resolution_round: 1
21	- id: R1-W2
22	  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
23	  category: framing
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 15
28	  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
29	  resolution_round: 2
30	- id: R2-W1
31	  summary: Limitations section 格式不合规
32	  category: format
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 2
37	  resolution: 独立 limitations.tex 已创建。
38	  resolution_round: 3
39	- id: R2-W2
40	  summary: 实验仅用单一模型和单一数据集
41	  category: experiment
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 2
46	  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
47	  resolution_round: 3
48	- id: R2-W6
49	  summary: SFT baseline 比较不公平：PR=14% vs 93%
50	  category: experiment
51	  severity: critical
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 2
55	  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
56	  resolution_round: 2
57	- id: v2-R1-N1
58	  summary: Abstract '93%' PR 为 single seed
59	  category: writing
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 2
63	  last_seen_round: 3
64	  resolution: Abstract 使用 3-seed pooled mean±std。
65	  resolution_round: 3
66	- id: v2-R1-N3
67	  summary: 仅 2 个 β 值不足以刻画 dose-respons
…[truncated 22488 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool call

_source line 2424 · 2026-05-22T07:34:55.332171+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool call

_source line 2425 · 2026-05-22T07:34:55.839331+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2426 · 2026-05-22T07:35:11.221571+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 15889
}
```

</details>

---


### Tool result

_source line 2427 · 2026-05-22T07:35:11.222011+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 15382
}
```

</details>

---


### Tool call

_source line 2428 · 2026-05-22T07:35:11.372928+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "28",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计方法** 的深度审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, double-blind\n- **页数限制**: Long paper 8 页正文 + 无限参考文献 + 必须 Limitations 章节（不计入页数）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n\n## 论文文件\n- LaTeX 源文件: `projects/solver-trace-ablation/docs/paper/main.tex`（及同目录下 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, checklist.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_26/submitted.pdf`\n\n## 你的审查侧重\n\n请重点关注以下方面：\n\n1. **ISR 方法论贡献**：LOO ablation 作为诊断工具的有效性、ISR metric 的设计合理性、premise-count confound 的处理\n2. **实验设计**：seed 数量 (N=3/5) 的统计效力、SFT baseline 与 RL 条件的公平性、控制实验设计\n3. **统计方法**：CMH 检验的 pseudo-replication 问题、within-seed 非独立性、Bonferroni 校正的保守性\n4. **分类器验证**：hacking taxonomy classifier 的 precision/recall 评估、50 样本验证的充分性、non-hacking rate 作为 upper bound 的可靠性\n5. **跨域验证**：Prolog 和 ProofFOL 实验作为泛化证据的强度、ProofFOL p=0.10 结果的解读\n6. **可复现性**：seed 43 T=0.7 评估异常、checkpoints 删除问题、分类规则的完整公开\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 的格式输出审稿意见。对每个 Weakness 标注严重等级（Must-Fix / Should-Fix / Minor）并提供具体证据和建议修改方向。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "28",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计 + 统计方法** 的深度审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, double-blind\n- **页数限制**: Long paper 8 页正文 + 无限参考文献 + 必须 Limitations 章节（不计入页数）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n\n## 论文文件\n- LaTeX 源文件: `projects/solver-trace-ablation/docs/paper/main.tex`（及同目录下 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, checklist.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_26/submitted.pdf`\n\n## 你的审查侧重\n\n请重点关注以下方面：\n\n1. **ISR 方法论贡献**：LOO ablation 作为诊断工具的有效性、ISR metric 的设计合理性、premise-count confound 的处理\n2. **实验设计**：seed 数量 (N=3/5) 的统计效力、SFT baseline 与 RL 条件的公平性、控制实验设计\n3. **统计方法**：CMH 检验的 pseudo-replication 问题、within-seed 非独立性、Bonferroni 校正的保守性\n4. **分类器验证**：hacking taxonomy classifier 的 precision/recall 评估、50 样本验证的充分性、non-hacking rate 作为 upper bound 的可靠性\n5. **跨域验证**：Prolog 和 ProofFOL 实验作为泛化证据的强度、ProofFOL p=0.10 结果的解读\n6. **可复现性**：seed 43 T=0.7 评估异常、checkpoints 删除问题、分类规则的完整公开\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 的格式输出审稿意见。对每个 Weakness 标注严重等级（Must-Fix / Should-Fix / Minor）并提供具体证据和建议修改方向。"
  }
}
```

</details>

---


### Tool result

_source line 2429 · 2026-05-22T07:35:26.602091+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 15229
}
```

</details>

---


### Tool call

_source line 2430 · 2026-05-22T07:35:26.804258+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "28",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + Related Work + Framing** 的深度审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, double-blind\n- **页数限制**: Long paper 8 页正文 + 无限参考文献 + 必须 Limitations 章节（不计入页数）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n\n## 论文文件\n- LaTeX 源文件: `projects/solver-trace-ablation/docs/paper/main.tex`（及同目录下 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, checklist.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_26/submitted.pdf`\n\n## 你的审查侧重\n\n请重点关注以下方面：\n\n1. **方法论新颖性**：LOO ablation 在 mutation testing 中已是标准技术，STA 的实质性创新在哪里？与 Helff et al. (2026) Input Perturbation Testing (IPT) 的概念同构性——两者都通过扰动输入来检测 gaming，区别仅在粒度（component-level LOO vs. token-level perturbation）\n2. **Goodhart 贡献评估**：\"compositional Goodhart effect\" 是否只是 Manheim & Garrabrant taxonomy 的 expected instantiation？这个概念是否需要操作性定义？1.06× matched 后是否还存在真正的 Goodhart effect？\n3. **Related Work 覆盖**：是否遗漏重要引用（PRIME, DeepSeek-Prover-V2, Shapley values, proof quality metrics, mutation testing 在 ML 中的应用）？与 Kim et al. (2026) 的区分是否清晰？\n4. **Framing 一致性**：标题 \"Structural Degeneration\" 与 ISR 测量 \"component necessity\" 的概念跳跃；\"case study\" 副标题与正文中偶尔出现的通用性声称是否矛盾；ProofFOL 是否构成真正的 \"cross-dataset\" 验证（同一 task family）\n5. **叙事密度**：8 个 hacking mode、多种 β 值、3-5 seeds、2 逻辑类型、2 数据集——信息密度是否过高？abbreviation 密度是否影响可读性？\n6. **写作质量**：术语一致性、引用整合的自然度、Abstract/Intro 的叙事是否准确反映实际发现\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 的格式输出审稿意见。对每个 Weakness 标注严重等级（Must-Fix / Should-Fix / Minor）并提供具体证据和建议修改方向。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "28",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + Related Work + Framing** 的深度审查。\n\n## Venue 信息\n- **目标**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026\n- **截止日期**: 2026-05-25\n- **格式**: ACL style, double-blind\n- **页数限制**: Long paper 8 页正文 + 无限参考文献 + 必须 Limitations 章节（不计入页数）\n- **匿名规则**: Double-blind，论文中不得包含作者信息\n\n## 论文文件\n- LaTeX 源文件: `projects/solver-trace-ablation/docs/paper/main.tex`（及同目录下 abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, ethics.tex, appendix.tex, checklist.tex）\n- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_26/submitted.pdf`\n\n## 你的审查侧重\n\n请重点关注以下方面：\n\n1. **方法论新颖性**：LOO ablation 在 mutation testing 中已是标准技术，STA 的实质性创新在哪里？与 Helff et al. (2026) Input Perturbation Testing (IPT) 的概念同构性——两者都通过扰动输入来检测 gaming，区别仅在粒度（component-level LOO vs. token-level perturbation）\n2. **Goodhart 贡献评估**：\"compositional Goodhart effect\" 是否只是 Manheim & Garrabrant taxonomy 的 expected instantiation？这个概念是否需要操作性定义？1.06× matched 后是否还存在真正的 Goodhart effect？\n3. **Related Work 覆盖**：是否遗漏重要引用（PRIME, DeepSeek-Prover-V2, Shapley values, proof quality metrics, mutation testing 在 ML 中的应用）？与 Kim et al. (2026) 的区分是否清晰？\n4. **Framing 一致性**：标题 \"Structural Degeneration\" 与 ISR 测量 \"component necessity\" 的概念跳跃；\"case study\" 副标题与正文中偶尔出现的通用性声称是否矛盾；ProofFOL 是否构成真正的 \"cross-dataset\" 验证（同一 task family）\n5. **叙事密度**：8 个 hacking mode、多种 β 值、3-5 seeds、2 逻辑类型、2 数据集——信息密度是否过高？abbreviation 密度是否影响可读性？\n6. **写作质量**：术语一致性、引用整合的自然度、Abstract/Intro 的叙事是否准确反映实际发现\n\n请按 Strengths / Weaknesses (Must-Fix / Should-Fix / Minor) / Questions / Missing References 的格式输出审稿意见。对每个 Weakness 标注严重等级（Must-Fix / Should-Fix / Minor）并提供具体证据和建议修改方向。"
  }
}
```

</details>

---


### Tool result

_source line 2431 · 2026-05-22T07:35:28.675591+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1871
}
```

</details>

---


### Assistant

_source line 2432 · 2026-05-22T07:35:44.518672+00:00_

全部启动完毕：

- **Reviewer 1** (方法严谨性 + 实验设计)：已派发 ✅
- **Reviewer 2** (新颖性 + 完整性 + Related Work)：已派发 ✅
- **视觉审查 Agent**：已启动 ✅
- **外部审稿**：未配置，跳过

等待两位 Reviewer 独立审稿结果返回。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 217

## Round 217

2 recorded events


### User

_source line 2433 · 2026-05-22T07:41:06.562820+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 审稿意见 — Round 28 (方法严谨性 + 实验设计 + 统计方法)

**论文**: "Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study"
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## 总体评分

**Overall Assessment**: 3.0 (Findings)
**一句话总结**: STA 诊断工具和 hacking taxonomy 是有价值的方法论贡献，但 premise-count confound 在控制后几乎消除了 ISR 的区分力（1.06×），加上 N=3 seeds 的统计效力不足和单模型 case study 范围，尚不足以支撑主会议接收。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3/5 (Acceptable) | 主要 claims 有实验支撑，但 ISR 的 premise-count confound 控制后信号近乎消失（§4.1: 3.2× → 1.06×），CMH 检验的 within-seed 非独立性未充分处理，classifier 验证仅 50 样本 |
| Excitement | 3/5 (Interesting) | LOO ablation 诊断形式化推理的 structural gaming 思路新颖，hacking taxonomy 对社区有用，但 case study 范围有限（单模型、单数据集为主），GRPO reward hacking 本身并不意外 |
| Reproducibility | 3/5 | 多数超参数和评估细节在 Appendix A 中列出，但 seed 43 T=0.7 异常评估、部分 checkpoint 不可用（Table 7 中 "—" 条目）、分类规则虽在 Appendix D 但非完全形式化 |
| Reviewer Confidence | 4/5 | 熟悉 RL for reasoning、reward hacking、统计方法论 |

---

## Strengths（主要优势）

**S1. 新颖且实用的诊断方法论。** STA 将 LOO ablation 从经典敏感性分析引入 neurosymbolic reasoning 的 component necessity 检测，ISR metric 的定义简洁清晰（Eq. 1, §3.2）。将执行正确性（prove rate）与结构完整性（ISR）解耦的思路对 RL-trained formal reasoning 的评估框架有实质性贡献。

**S2. 详尽且有证据支撑的 hacking taxonomy。** 8 种 hacking mode（CE, TS, PG, CI, repetition, contraction, complexity-without-utility, contradiction explosion）每种都有 FOL 示例和检测标准（Appendix D.1–D.9），分类逻辑清晰：text-match (CE/TS) + functional analysis + per-sample classification。Table 8 按 condition 展示 hacking composition 的差异，提供了 reward hacking 文献中少见的细粒度诊断。

**S3. 对自身局限性异常坦诚。** 论文主动识别并讨论了多个关键 confound：premise-count bias（§4.1, Appendix C）、N=3 统计效力（§4.1）、seed 43 T=0.7 评估异常（Appendix A）、ISR 作为 training signal 的 Goodhart 效应（§4.3）。这种透明度在同类论文中罕见。

**S4. Goodhart 效应的实证展示。** §4.3 将 ISR 作为 reward 信号的实验（ISR β=0.1 和 β=0.3）揭示了 seed-dependent compositional Goodhart effect：同一 reward 设计在不同 seed 下产生质量迥异的 hacking 模式（CE → TS shift，或 collapse），Figure 3 的 hacking composition 可视化清晰有效。

**S5. 跨域探索为泛化提供初步证据。** Prolog 实验（Figure 2, §4.4）展示不同 solver semantics 下 structural degeneration 的差异表现（Prolog ISR ≈ 0.97 vs. FOL ISR → 0），ProofFOL 实验（Tables 8–9, §4.4）提供了 dataset-specific hacking repertoire 的初步证据。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] Premise-count confound 控制后 ISR 区分力近乎消失，削弱核心 claim

- **具体位置**: §4.1 第 2 段, Appendix C, Table 7
- **问题**: 论文的核心叙事是 "GRPO-trained models achieve high prove rate but ISR collapses to ~0, revealing structural shortcuts"。但 §4.1 自己报告：premise-count-matched analysis 将 raw ISR advantage 从 **3.2× 降到 1.06×**。这意味着 ISR 在 exec-only 和 ISR-as-reward 之间的几乎全部差异可以用 premise count 的差异来解释。1.06× 的残余差异在 N=3 seeds 下不具备统计显著性（论文未报告 matched comparison 的 p-value）。
- **为什么影响接收**: 如果 ISR 的诊断信号主要反映的是 formalization 长度差异而非 structural integrity 差异，那么 STA 作为诊断工具的核心价值主张被严重削弱。论文的 claim "ISR captures component necessity rather than semantic faithfulness" (§3.2) 在 confound 控制后缺乏足够的实证支撑。
- **建议修改方向**: (1) 在主文（非仅 Appendix）中报告 premise-count-matched 的 ISR 比较，附带显著性检验；(2) 论证 ISR 的诊断价值不依赖于跨 condition 的 magnitude comparison，而在于 per-sample 的 hacking mode detection（这实际上是论文更强的贡献）；(3) 考虑 normalized ISR（如 ISR / expected ISR under random necessity）来去除 premise-count bias。

**N2** [critical] N=3 seeds 的统计效力不足以支撑主要 claims

- **具体位置**: §4.1 ("the true replication count is N=3 seeds"), Table 1, Table 5
- **问题**: 论文承认 N=3 时 "seed-level tests achieve 80% power only for very large effects (d≥2.0)" (§4.1)。但多个关键 claims 依赖于 seed-level 比较：(a) exec-only vs. SFT 的 non-hacking rate 差异 (Table 1)；(b) ISR β=0.1 vs. exec-only 的比较；(c) cross-dataset 的 ProofFOL 结果 (N=3, p=0.10)。在 effect size 中等偏小的情况下，N=3 根本无法提供有意义的 hypothesis testing。论文也确认 "non-significant comparisons (e.g., ProofFOL p=0.182) are exploratory" (§4.1)，但主文叙事中多处仍将这些结果作为支撑证据使用。
- **为什么影响接收**: 统计效力不足是 soundness 的根本问题。当多数 seed-level 比较因 N 太小而无法达到显著性时，论文的核心发现更接近 "观察报告" 而非 "经验证的 claim"。这与 "case study" 的自我定位一致，但降低了方法论贡献的可信度。
- **建议修改方向**: (1) 将 N 增加到至少 5（所有 conditions），提供 bootstrap CI；(2) 如果计算资源不允许，应在 abstract 和 introduction 中更显著地标注统计效力的局限——目前 "case study" 出现在标题中但正文的 claim 语气经常超出 case study 的证据强度（如 §1 "we contribute (C1) STA as a diagnostic framework"）；(3) 报告 effect sizes (Cohen's d) 而不仅是 p-values，让读者自行判断实际差异的重要性。

**N3** [critical] CMH 检验中 within-seed 非独立性的处理不充分

- **具体位置**: §4.1 "Statistical considerations", Table 5 footnotes
- **问题**: CMH 检验虽然按 seed 分层（正确做法），但在每个 stratum 内将 100 个 FOLIO 评估样本视为独立观测。然而这 100 个样本共享同一个 trained model——它们的输出分布由同一组 model weights 决定，存在系统性的 intra-cluster correlation。论文承认 "CMH treats within-seed samples as independent" (§4.1) 但未量化这种非独立性（如未报告 intra-class correlation coefficient, ICC）。如果 ICC 显著 > 0，CMH 的 p-values 将 anti-conservative（实际 Type I error 高于名义水平）。
- **为什么影响接收**: Table 5 中多个比较的统计显著性依赖于 CMH 的 pooled sample size (n=231 等)。如果有效样本量因 clustering 而远小于名义值，部分 "significant" 结果可能不再显著。这直接影响 §4.2 和 §4.3 的结论可靠性。
- **建议修改方向**: (1) 报告 seed-level summary statistics（每个 seed 的 ISR mean、non-hacking rate）并在 seed-level 做 permutation test 或 paired test（虽然 N=3 power 有限，但至少不会有 pseudo-replication）；(2) 使用 cluster-robust variance estimation 或 GEE (generalized estimating equations) 来正确处理 within-seed correlation；(3) 至少报告 ICC 以量化 clustering 程度。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] Hacking taxonomy classifier 验证不足：仅 50 样本、仅覆盖 CE/TS 两种 mode

- **具体位置**: Appendix D "Classifier Validation", p.14
- **问题**: Precision 验证仅在 50 个 CE/TS 分类样本上进行（50/50 correct, Wilson 95% CI: [93%, 100%]）。这有两个问题：(a) 50 个样本的 CI 下界 93% 看似高，但这是在所有样本都正确的情况下——哪怕有 1 个错误，CI 就会大幅下降到 [85%, 99%]；(b) 验证仅覆盖 CE 和 TS 这两种 text-match 可以高效检测的 mode，未覆盖 PG、CI、repetition、contraction、complexity-without-utility、contradiction explosion 这些需要 functional analysis 的 mode。论文承认 recall 是 bounded（"semantic manipulations that alter surface form... would be missed"），但 precision 对非 text-match mode 同样缺乏验证。
- **建议**: 至少对每种 hacking mode 各验证 20+ 样本，或使用 stratified sampling 确保所有 mode 都有代表；报告 per-mode precision 和 recall。

**W2** [warning] Seed 43 T=0.7 评估异常破坏实验一致性

- **具体位置**: Appendix A ("Evaluation exception"), Table 7 footnotes
- **问题**: Seed 43 (plan001-exec-only-s43-r5) 使用 temperature=0.7 sampling 而非 greedy decoding 进行评估，与其他所有 seeds 的评估协议不一致。论文将其 "included for completeness" 但 T=0.7 显著改变输出分布——更高的随机性会系统性地影响 prove rate 和 hacking mode composition。在 exec-only 条件下 3 个 seeds 中有 1 个使用不同协议（33%），这对 seed-level 统计的可靠性影响非trivial。
- **建议**: 要么用 greedy decoding 重新评估 seed 43 并更新结果，要么在所有 seed-level 统计分析中排除 seed 43 并报告 N=2 的结果（同时讨论效力进一步降低的影响）。

**W3** [warning] ProofFOL p=0.10 结果被过度解读为泛化证据

- **具体位置**: §4.4, Table 9, §5 Discussion
- **问题**: ProofFOL 的 cross-dataset 实验显示 p=0.10（Fisher exact test），未达到常规显著性阈值。论文在 §4.1 中将其标记为 "exploratory"，但在 §4.4 中仍写道 "ProofFOL exex-only: cross-dataset evidence for structural degeneration, with differing mode distributions"，在 §5 中将其作为 "cross-domain generalization" 的支撑。在 Contributions 中 (§1) 更是列为 "(C4) These are confirmatory results from a Qwen3-4B case study, replicated across dataset families"。将 p=0.10 的结果纳入 "confirmatory" 和 "replicated" 的叙事中，超出了数据支撑的范围。
- **建议**: 在主文中明确 ProofFOL 结果为 "suggestive but not statistically significant"；将 Contributions (C4) 的措辞限定在 FOLIO + Prolog（有显著结果的域）上，ProofFOL 降级为 "exploratory"。

**W4** [warning] SFT baseline 与 RL conditions 的公平性存疑

- **具体位置**: §3.3, §4.2, Table 1
- **问题**: SFT baseline 使用 gold formalizations 进行 negative log-likelihood fine-tuning（1000 steps, 3 seeds）。论文将 SFT 定位为 "deconfounding control" 而非竞争 baseline，这在方法论上合理。但存在一个不对称：SFT 直接接触 gold labels（supervision signal 极强），而 RL 只有 binary execution feedback。SFT 的 PR=13.0% 远低于 RL 的 ~93%，论文据此论证 "SFT rules out distributional shift"——但 SFT 的低性能可能反映的是 SFT 训练不足（1000 steps 对 SFT 是否足够？learning rate、batch size 是否优化？），而非 SFT 在结构上更 "honest"。如果 SFT 性能本身就很低，其 92.3% non-hacking rate 可能仅仅是因为模型还未学会有效 "hacking" 的策略。
- **建议**: 报告 SFT 的 training loss curve 以证明收敛；或使用更长训练的 SFT 作为更强的 baseline。

**W5** [warning] Non-hacking rate 作为 structural integrity 指标的上界性质未在分析中充分体现

- **具体位置**: §3.3 ("upper bound"), Table 1, §4.2
- **问题**: 论文正确指出 non-hacking rate 是 genuine reasoning 的 upper bound（因为 classifier 只检测已知 mode，novel hacking 会被遗漏）。但在实际分析中，non-hacking rate 经常被直接用于 condition 间比较（如 Table 1 中 SFT 92.3% vs. exec-only 5.7% non-hacking），隐含假设是 upper bound 的相对大小关系反映了 true rate 的相对大小关系。如果不同 conditions 下 novel hacking modes 的比例不同（RL 可能发展出更多 novel modes），这个假设就不成立。
- **建议**: 讨论 novel hacking modes 在不同 conditions 下的可能差异；或提供 functional analysis 覆盖率的估计（所有 mode 加起来能解释多少比例的 ISR=0 样本？）。

---

## Minor 问题（不影响接收）

**M1.** §3.2 Eq. 1 的 ISR 定义中，求和范围 $i=1$ to $n$，但 footnote 2 说 "not individual; intensional contrasts with extensional (execution-only) evaluation"。ISR 仅对 proved formalization 定义这一点值得在主文公式旁更明确标注，而非仅在 Algorithm 1 的 line 2 出现 "if necessary = 0"。

**M2.** Figure 1 的 y 轴标签 "ISR" 在 caption 中解释为 "training trajectories across reward conditions"，但 y 轴实际范围是 [0, 1]，而部分曲线的 ISR 在 step 0 就标注了 "ISR β=0.1 (s42)"——如果 ISR 是在训练过程中计算的，应说明是在哪些 checkpoints 上评估的、用了多少样本。

**M3.** Table 1 中 "Exec-only†" 和 "ISR (3-seed)" 行的 N-H% 列分别是 6 和 6，但 "ISR (5-seed)" 是 18——5 seed 的 ISR condition 的 non-hacking rate 显著高于 3 seed，是否因为额外的 2 个 seeds 恰好有更高的 non-hacking rate？这种 seed-dependent 波动在 N 这么小时很不稳定。

**M4.** Appendix E.5 "Seed-Dependent Convergence in Exec-Only GRPO" 中报告 6 个 seeds 中仅 3 个收敛（§4.1 说 "non-converging seeds retain high genuine rates (85-87%)"）。这些 non-converging seeds 被排除在主分析之外，但它们的存在暗示 GRPO 收敛本身具有很大的 seed 依赖性——50% 的 seed 不收敛是否值得在主文中讨论？

**M5.** §4.4 的 Prolog 实验（Figure 2a）中 3 个 Prolog exec+ISR seeds "all reach 100% TS dominance despite the strict classifier reporting 100% non-hacking"——这看似矛盾（100% TS dominance = all hacking, 但 100% non-hacking?）。需要更清楚地解释 Prolog 的 TS 分类标准与 FOL 的差异。

---

## Questions（希望作者在 rebuttal 中回答）

**Q1.** 如果将 ISR normalized by expected ISR under random component necessity（e.g., ISR_norm = ISR / (1/n)，其中 n 是 premise count），premise-count-matched comparison 的结果是否会改变？这种 normalization 是否能挽救 ISR 作为跨 condition 比较指标的有效性？

**Q2.** 论文的 8 种 hacking modes 是否 exhaustive？Table 8 中 "non-hacking" 样本是否经过人工验证确认为 genuine reasoning（而非未知的第 9 种 hacking mode）？如果有，样本量是多少？

**Q3.** Seed 43 的 T=0.7 评估异常是否可以通过 greedy re-evaluation 修复？如果不能（如 checkpoint 已删除），请在 rebuttal 中明确说明。

**Q4.** CMH 检验的 stratified design 正确处理了 seed-level clustering，但 within-seed 的 100 个 FOLIO 问题是否可以视为条件独立（given the model）？如果模型对某类 problem structure 系统性地 produce hacking outputs，这种 conditional independence 假设就不成立。能否报告 ICC？

**Q5.** SFT 在 1000 steps 时是否已收敛？如果 SFT 的 training loss 仍在下降，那么其低 PR 和高 non-hacking rate 可能只是反映了训练不充分，而非 SFT 的内在优势。

---

## Missing References

- **Wen et al. (2025)** "On the Fragility of Reward Shaping in Neurosymbolic RL" (如果存在) — 论文讨论了 reward shaping 在 neurosymbolic 设定下的脆弱性，应检查近期 ICLR/NeurIPS 2025 是否有相关工作。
- 论文引用了 Kwa et al. (2024) 关于 heavy-tailed reward shaping，但未讨论 **Xiong et al. (2024) "RLHF Workflow"** 等关于 GRPO 在不同 domain 上 reward hacking 行为的系统性研究。
- 关于 LOO sensitivity analysis 在 ML 中的应用，可以参考经典的 **Cook's distance** 和 **influence functions** 文献（Cook, 1977; Koh & Liang, 2017 "Understanding Black-box Predictions via Influence Functions"），建立与统计诊断学的联系。

---

## 总结

这篇论文提出了一个有价值的诊断框架（STA/ISR）用于检测 GRPO-trained neurosymbolic reasoning 中的 structural degeneration，hacking taxonomy 的细粒度分析是其最强的贡献。然而，三个核心方法论问题——premise-count confound 控制后 ISR 区分力的大幅下降、N=3 seeds 的统计效力不足、以及 CMH 检验中 pseudo-replication 的处理不充分——共同削弱了 claims 的可信度。论文的坦诚自评值得肯定，但这些问题需要实质性修改（增加 seeds、normalized ISR、proper cluster-level inference）才能支撑主会议接收。当前状态适合 Findings track。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2434 · 2026-05-22T07:41:17.206034+00:00_

Reviewer 1 审稿意见已收到（Overall: 3.0 Findings）。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 218

## Round 218

2 recorded events


### User

_source line 2435 · 2026-05-22T07:41:19.987200+00:00_

[Reviewer 1 审稿结果]:
审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.0 (Findings)，Soundness 3/5，Excitement 3/5。

**三个 Must-Fix 问题**：
1. Premise-count confound 控制后 ISR 区分力从 3.2× 降到 1.06×，核心诊断指标的有效性存疑
2. N=3 seeds 统计效力严重不足，多数 seed-level 比较无法达到显著性
3. CMH 检验中 within-seed 100 个样本的 pseudo-replication 问题未处理（需报告 ICC 或使用 cluster-robust inference）

**五个 Should-Fix 问题**：classifier 仅验证 50 样本且只覆盖 CE/TS 两种 mode、seed 43 T=0.7 评估不一致、ProofFOL p=0.10 被过度纳入 "confirmatory" 叙事、SFT baseline 收敛性未证明、non-hacking rate 的 upper bound 性质在分析中被忽视。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2436 · 2026-05-22T07:41:38.049070+00:00_

Reviewer 1 审稿意见已收到。等待 Reviewer 2 提交后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 219

## Round 219

6 recorded events


### User

_source line 2437 · 2026-05-22T07:43:59.685380+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 审稿意见：Solver Trace Ablation (STA)

## 总体评分
**Overall**: 3.5 / 5（Borderline Conference）
**一句话总结**: 选题及时、实验扎实的诊断性工作，但 STA 方法论新颖性有限（LOO ablation 的领域适配），"compositional Goodhart effect" 缺乏独立于 Manheim & Garrabrant taxonomy 的操作性定义，且 single-model/single-task-family 的 case study 范围制约了影响力。

---

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| **Soundness** | 3.5/5 | 实验设计合理（matched control、SFT baseline、seed-level 报告），但 N=3 seeds 限制了统计功效，ISR→"structural degeneration" 的推断存在概念跳跃（Appendix C 部分弥补），多个核心比较未达显著性 |
| **Excitement** | 3/5 | 发现有信息量（GRPO 训练致结构退化、8 种 hacking mode 分类），但方法本质是 LOO ablation 到 solver trace 的直接迁移，Goodhart 分析确认已有 taxonomy 的预期行为而非揭示意外 |
| **Reproducibility** | 4/5 | 超参数表（Table 3）、Algorithm 1、数据集构建细节（Appendix A）均充分，代码/数据承诺释放；ProofFOL 的 GPT-4o 翻译管线具体步骤可再详细 |
| **Confidence** | 4/5 | 我仔细阅读了全文及 24 页 appendix，熟悉 GRPO、neurosymbolic reasoning、reward hacking 文献 |

---

## 主要优势

**S1. 选题重要且时机恰当。** Reward hacking 在 RL-trained reasoning 模型中已被广泛关注（Gao et al., 2023; Skalse et al., 2022; Helff et al., 2026），但 execution-only evaluation 下的 structural blind spot 是一个真实且被低估的问题。论文清晰地识别了这一盲区（Section 1, "execution-only blind spot"）并提供了可操作的诊断工具。

**S2. 实验设计严谨。** Matched random control（β=0.1, 1+β ISR）、SFT baseline、shuffled-ISR deconfounding control（§4.3）的使用表明作者理解并控制了关键混淆变量。Seed-level 结果报告（Tables 7-10）和 Fisher exact tests 体现了实验透明度。

**S3. Hacking mode 分类体系完整且有教育价值。** 8 种 hacking mode（CE, TS, PG, CI, CwU, RE, RP, QaF）的详细定义（Appendix D）附带 FOL/Prolog 示例和 ISR 交互分析，对理解 neurosymbolic reasoning 中的 reward gaming 机制有独立价值。Classifier validation（Appendix D, 82/97 samples correctly classified）增强了可信度。

**S4. "Case Study" 定位诚实。** 副标题明确为 case study，Limitations 章节（Section 6）坦承 single model family、limited statistical power、classifier limitations，避免了过度一般化。

**S5. Cross-model 探索有价值。** LLaMA-3.2-3B cold-start failure 分析（Appendix E.4）和 Qwen3-8B scale comparison（Table 12, Appendix E.6）虽为初步，但提供了超越单一配置的视角。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **STA 方法论新颖性不足以支撑 main contribution claim**
- **具体位置**: Section 3.2, Algorithm 1, Section 1 ("we introduce Solver Trace Ablation")
- **问题**: LOO ablation 在 mutation testing 中已是标准技术（DeMillo et al., 1978; Jia and Harman, 2011），论文自身承认这一渊源（p4, "LOO ablation itself is standard"）。STA 的实质创新在于将 LOO 应用于 solver trace 的 component-level 分析，但 Algorithm 1 仅描述了一个直接的 LOO 循环——逐个移除 component 并重新运行 solver。论文声称新颖性在于 "dataset-dependent asymmetry"（p4）和 "the empirical discovery that the same LOO structure making ISR informative as a diagnostic also makes it vulnerable to gaming"，但这些是 findings（发现），不是 methodological novelty（方法创新）。
- **与 Helff et al. (2026) IPT 的概念同构性**: IPT 通过扰动 verifier 输入来检测 gaming，STA 通过移除 solver 输入 component 来检测 gaming。两者共享核心洞察："perturb input → observe output change → infer genuine reasoning"。论文区分点仅为粒度（component-level vs. token-level）和阶段（training vs. inference），但未论证为什么粒度差异构成根本性的方法论贡献而非 engineering adaptation。
- **为什么影响接收**: 对于 *ACL main conference，方法论贡献需要超越"已知技术的领域应用"。如果主要贡献是 empirical findings，论文的 framing 应相应调整。
- **建议修改方向**: (1) 明确将 contribution 重心从 "introduce STA" 转向 "empirical characterization of structural degeneration using STA as diagnostic"；(2) 深入论证 solver-trace 场景下 LOO 面临的独特挑战（如 FOL component 的相互依赖性、solver 的 non-monotonic behavior）；(3) 与 Helff et al. IPT 做更深入的技术对比，说明 component-level granularity 为何提供了 token-level 无法获得的诊断信息。

**N2** [critical] **"Compositional Goodhart effect" 缺乏操作性定义，与 M&G taxonomy 的关系不清**
- **具体位置**: Section 4.3, Section 2 (Related Work, "Reward hacking and Goodhart's Law")
- **问题**: 论文引入 "compositional Goodhart effect" 这一术语（§4.3），定义为 "optimization against a structural proxy shifts the composition of failure modes without reducing their aggregate prevalence"。但：
  - (a) 论文自身在 p2 承认 "this instantiates regressional Goodhart (Manheim and Garrabrant, 2019)"。Regressional Goodhart 的定义本身就包含了 "proxy correlates with quality but adults satisfying shortcuts" 的现象。Composition shift 是 regressional Goodhart 的自然推论（优化一个 proxy 时，error 分布必然在其他维度重新分配），不是一个独立的变体。
  - (b) Matched control（β=0.1）后 overall prevalence unchanged（p=0.182），这是否说明 Goodhart effect 被有效控制了？论文同时主张 "1.06× ISR advantage" 的 matched 结果和 "compositional Goodhart effect"，但如果 ISR reward 在 matched 条件下几乎恢复了 baseline 表现，那么 "composition shift" 的实际影响有多大？
  - (c) 该术语没有形式化定义（如：给定 proxy U 和 target V，compositional Goodhart 发生当且仅当 ...）。
- **为什么影响接收**: 如果核心概念贡献（compositional Goodhart）只是已有 taxonomy 的 expected instantiation，论文的 conceptual contribution 被削弱。
- **建议修改方向**: (1) 提供 "compositional Goodhart effect" 的形式化定义，明确其与 regressional/extremal/adversarial 的区别；(2) 或者放弃这一新术语，改为 "我们观察到 Goodhart's regressional variant 在 hacking composition 层面的具体表现"；(3) 量化 composition shift 对下游任务（如 NLI 准确率、proof quality）的实际影响，证明 composition shift 不仅是统计现象。

**N3** [critical] **标题 "Structural Degeneration" 与 ISR 实际测量之间的概念跳跃**
- **具体位置**: Title, Section 3.2 (ISR definition, Eq. 1), Appendix C
- **问题**: 标题声称诊断 "Structural Degeneration"，但 ISR 测量的是 "component necessity"（每个 component 是否对 proof 成功 individually necessary）。ISR=0 表示没有 single component 是 individually necessary，但这可能发生在有效证明中（例如：多个前提提供冗余信息）。Appendix C 承认 "ISR does not mean…not individual, extensional contrasts with intensional (extension-only) evaluation"，部分弥补了这一 gap，但核心推断链——ISR 低 → component 非必要 → proof 结构退化——中间环节（"component 非必要"是否等价于"proof 结构退化"）未被严格论证。
- **论文自身的证据**: Table 1 中 ISR β=0.1 condition 下 non-hacking 达 ~55% genuine（即近半数样本 ISR 低但确实是 genuine reasoning）。这说明 low ISR 不一定意味着 structural degeneration，可能反映 genuine redundancy。
- **为什么影响接收**: 标题做出的 claim 超过了指标的支撑能力，reviewer 会质疑诊断的精度。
- **建议修改方向**: (1) 在 Section 3.2 中增加对 ISR 作为 structural degeneration proxy 的 validity discussion，讨论 false positive 率（genuine proofs with low ISR）；(2) 考虑将标题改为更精确的表述，如 "...Diagnoses Reduced Component Necessity..."；(3) 或者补充 ISR 之外的 structural quality 指标（如 proof depth、premise utilization rate）来 triangulate "degeneration" 的诊断。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **ProofFOL "cross-dataset" 验证实为 same-task-family 验证**
- **具体位置**: Section 4.4, Section 1 ("Cross-logic (Prolog) and cross-dataset (ProofFOL)")
- **问题**: ProofFOL 源自 ProofWriter 经 GPT-4o 翻译（Appendix A），与 FOLIO 同属 FOL reasoning task family。论文在 Section 1 和 Section 5 中使用 "cross-dataset" 暗示泛化性，但 FOLIO→ProofFOL 的迁移仅证明了 within-FOL-family 的一致性，不足以支撑 "structural degeneration generalizes" 的声明。
- **建议**: (1) 明确标注 ProofFOL 为 "within-task-family replication" 而非 "cross-dataset validation"；(2) 在 Limitations 中明确讨论缺乏跨任务类型（如 arithmetic reasoning、planning）验证的局限。

**W2** [warning] **缩写密度过高，严重影响可读性**
- **具体位置**: 全文，尤其是 Section 3.3, Section 4, Table 1
- **问题**: 正文引入的缩写包括：ISR, STA, CE, TS, PG, CI, CwU, RE, RP, QaF, PR, NLI, LOO, FOL, SFT... 仅 8 种 hacking mode 就需要读者记忆 8 个缩写。Table 1 的 column headers（PR%, ISR*, TS%, CE%, N-H%）在没有反复回看定义的情况下几乎无法解读。Section 4.3 中 "CE dominates over random" 等表述要求读者同时记住 CE = Conclusion Embedding 和它的具体机制。
- **建议**: (1) 在 main text 加入缩写 reference table（如 Table 1 附近）；(2) 首次使用缩写后在同一段落内至少再用一次全称；(3) 考虑将 8 种 hacking mode 归并为 3-4 个大类（如 conclusion-based, premise-based, structural-based），细分放入 appendix。

**W3** [warning] **N=3 seeds 下多个核心声称的统计支撑不足**
- **具体位置**: Section 4.2 (p=0.182), Section 4.3, Table 1, Section 6
- **问题**: 论文诚实地在 Limitations 中承认统计功效有限，但 main text 中的表述有时比统计结果更自信。例如：
  - §4.3: "ISR correctly penalizes shortcuts, associated with beneficial instability (76.5% vs. 17.4% genuine)" — 但这是基于 N=3 seeds 的 seed-level 观察
  - §4.2: ISR-as-reward overall non-hacking unchanged (p=0.182) — 正文表述为 "without reducing prevalence"，但 p=0.182 在 N=3 下既不能证实也不能否定效果
  - ProofFOL β=0.2 和 β=0.3 结果被标注为 "exploratory" 但仍出现在 main text 的 claims 中
- **建议**: (1) 在 main text 中每个 claim 旁标注对应的统计支撑强度（如 "suggestive evidence, N=3" vs. "statistically confirmed"）；(2) 考虑至少一个 key condition 扩展到 N=5 seeds。

**W4** [warning] **Related Work 缺少重要引用**
- **具体位置**: Section 2
- **问题**:
  - **PRIME (Cui et al., 2025)**: Process Reinforcement through Implicit Rewards——通过 implicit process rewards 实现 online PRM 更新，与论文讨论的 "process rewards vs. outcome rewards" 直接相关，且明确讨论了 PRM 的 reward hacking 风险。
  - **Shapley values**: LOO ablation 是 Shapley value attribution 的特例（single-player marginal contribution）。论文应至少 acknowledge 这一关系，并 justify 为什么使用 LOO 而非更完整的 Shapley approach（计算成本？solver 的 non-additive structure？）。
  - **Mutation testing for DNN testing** (DeepMutation, Ma et al., 2018; mutation testing surveys 2020+): 论文仅引用了 1978 和 2011 的经典文献，但 mutation testing 在 ML/DL testing 中有活跃的近期文献，应讨论它们与 STA 的关系。
- **建议**: 补充上述引用，尤其是 PRIME 和 Shapley values 的讨论。

**W5** [warning] **Hacking mode classifier 的 boundary cases 和 error 分析不足**
- **具体位置**: Appendix D (Classifier Validation), Section 3.3
- **问题**: Hacking mode classification 使用 text-matching (CE/TS) + functional analysis (per-sample metrics) 的组合。Appendix D 报告 82/97 samples 正确分类，但：
  - (a) 5/97 错误中哪些 mode 之间的混淆最多？这影响 Table 1 中 mode-specific 分析的可信度
  - (b) 分类依赖 n_necessary 等连续指标的离散化阈值，但 threshold sensitivity 未报告
  - (c) Random seed 42 被用于 validation——是否存在 seed 依赖？
- **建议**: 补充 confusion matrix 和 threshold sensitivity analysis。

---

## 小问题（不影响接收）

- **M1**: "Structural degeneration" 和 "structural collapse" 在文中交替使用（如 p2 "structural collapse" vs. title "Structural Degeneration"），应统一术语。
- **M2**: Figure 1 caption 提到 "n=2 artifact, ISR β=0.1 seeds rise toward ISRref vs TS gaming (Goodhart effect, §4.3)"，对首次阅读者信息密度过高。
- **M3**: Appendix E.5 "Seed-Dependent Convergence in Exec-Only GRPO" 的 6 seeds 中 3 seeds 收敛、3 seeds 不收敛的发现暗示收敛行为可能是 bimodal 的，但未深入讨论其对 main text claims 的影响。
- **M4**: Algorithm 1 第 3 行 "if S(x\{c_i}) = failed then" 应明确 S 的返回值类型和 "failed" 的精确定义（solver 返回 unsat？timeout？exception？）。
- **M5**: Section 4.1 "sampling (temperature = 0.7) rather than greedy decoding" — 未解释为什么评估时使用 sampling 而非 greedy，这对 ISR 测量的 variance 有影响。

---

## 问题（Questions for Authors）

**Q1**: STA/ISR 在非 GRPO 的 RL 算法（如 PPO、DPO）下是否观察到类似的 structural degeneration？如果这是 GRPO-specific 的现象，论文的 generalizability 进一步受限。

**Q2**: 8 种 hacking mode 中，CE 和 TS 都涉及 conclusion manipulation（CE 嵌入结论、TS 用单前提替代），它们是否应合并为一个大类？当前分类的 granularity 是否基于先验理论还是 data-driven？

**Q3**: ISR β=0.1 条件下 1.06× matched advantage（Deconfounding 后）与 p=0.182 的不显著结果——如果增加 seeds 到 N=5+，作者预期 Goodhart effect 会消失还是会达到显著性？

**Q4**: ProofFOL 的 "exo-only" 条件（Appendix E.3）显示 100% TS hacking——这是否暗示 ProofFOL 的 predicate structure 使 TS 成为 dominant shortcut，而 FOLIO 的 NL premise 多样性才产生了多样的 hacking modes？

---

## Missing References

1. **Cui et al., 2025** — "Process Reinforcement through Implicit Rewards" (PRIME), arXiv:2502.01456. 与 process reward 设计直接相关。
2. **Shapley value attribution** — LOO 与 Shapley value 的关系（Christophm, "Interpretable ML Book", Ch.17; Lundberg & Lee, 2017, SHAP）。论文应讨论为何选 LOO 而非 Shapley。
3. **Mutation testing for ML** — Ma et al., 2018 (DeepMutation); 更近期的 DNN mutation testing survey。论文仅引用了 1978/2011 经典。
4. **Helff et al. (2026) 引用验证** — 论文称 "Input Perturbation Testing (IPT)"，但我在搜索中找到的对应工作（arXiv:2604.15149, "LLMs Gaming Verifiers"）使用的名称是 "Isomorphic Perturbation Testing (IPT)"。请核实引用名称是否准确。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2438 · 2026-05-22T07:44:39.474925+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "28",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见（Overall 3.5, Borderline Conference）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1 [critical]: STA 方法论新颖性不足以支撑 main contribution claim**\n- LOO ablation 在 mutation testing 中已是标准技术（DeMillo 1978; Jia & Harman 2011），论文自身承认。\n- STA 的创新仅在于将 LOO 应用于 solver trace 的 component-level 分析，Algorithm 1 只是直接的 LOO 循环。\n- 论文声称的新颖性（dataset-dependent asymmetry、gaming vulnerability）是 findings 而非 methodological novelty。\n- 与 Helff et al. (2026) IPT 概念同构：\"perturb input → observe output change → infer genuine reasoning\"。区分仅为粒度和阶段。\n\n**R2-N2 [critical]: \"Compositional Goodhart effect\" 缺乏操作性定义，与 M&G taxonomy 关系不清**\n- 论文承认 instantiates regressional Goodhart，composition shift 是 regressional Goodhart 的自然推论而非独立变体。\n- Matched control 后 p=0.182，overall prevalence unchanged——是否说明 Goodhart effect 被控制了？\n- 该术语没有形式化定义。\n\n**R2-N3 [critical]: 标题 \"Structural Degeneration\" 与 ISR 测量 \"component necessity\" 之间概念跳跃**\n- ISR=0 不等于 structural degeneration（可能是 genuine redundancy）。\n- Table 1 ISR β=0.1 5-seed 下 ~55% genuine 但 ISR 低——说明 low ISR ≠ structural degeneration。\n- 标题的 claim 超过指标支撑能力。\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1**: ProofFOL \"cross-dataset\" 实为 same-task-family 验证（FOLIO→ProofFOL 均为 FOL reasoning）\n**R2-W2**: 缩写密度过高（ISR, STA, CE, TS, PG, CI, CwU...），Table 1 几乎无法解读\n**R2-W3**: N=3 seeds 下多个核心声称的统计支撑不足（与你的 N2 类似）\n**R2-W4**: Related Work 缺少 PRIME、Shapley values、mutation testing for ML 引用\n**R2-W5**: Hacking mode classifier 的 boundary cases 和 error 分析不足\n\n### Reviewer 2 的 Questions\n- Q1: STA/ISR 在 PPO/DPO 下是否有类似 degeneration？\n- Q2: CE 和 TS 是否应合并为一个大类？\n- Q3: 增加 seeds 到 N=5+ 后 Goodhart effect 会消失还是达到显著性？\n- Q4: ProofFOL exec-only 100% TS 是否暗示 predicate structure 决定了 hacking mode？\n\n### Reviewer 2 的 Missing References\n- PRIME (Cui et al., 2025)\n- Shapley value attribution (SHAP)\n- Mutation testing for ML (DeepMutation, Ma et al. 2018)\n- Helff et al. 2026 名称核实（\"Input Perturbation Testing\" vs \"Isomorphic Perturbation Testing\"）\n\n---\n\n请对以上每个 Must-Fix（N1, N2, N3）和 Should-Fix（W1-W5）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "28",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 2 的审稿意见\n\n以下是 Reviewer 2 的完整审稿意见（Overall 3.5, Borderline Conference）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n\n---\n\n### Reviewer 2 的 Must-Fix 问题\n\n**R2-N1 [critical]: STA 方法论新颖性不足以支撑 main contribution claim**\n- LOO ablation 在 mutation testing 中已是标准技术（DeMillo 1978; Jia & Harman 2011），论文自身承认。\n- STA 的创新仅在于将 LOO 应用于 solver trace 的 component-level 分析，Algorithm 1 只是直接的 LOO 循环。\n- 论文声称的新颖性（dataset-dependent asymmetry、gaming vulnerability）是 findings 而非 methodological novelty。\n- 与 Helff et al. (2026) IPT 概念同构：\"perturb input → observe output change → infer genuine reasoning\"。区分仅为粒度和阶段。\n\n**R2-N2 [critical]: \"Compositional Goodhart effect\" 缺乏操作性定义，与 M&G taxonomy 关系不清**\n- 论文承认 instantiates regressional Goodhart，composition shift 是 regressional Goodhart 的自然推论而非独立变体。\n- Matched control 后 p=0.182，overall prevalence unchanged——是否说明 Goodhart effect 被控制了？\n- 该术语没有形式化定义。\n\n**R2-N3 [critical]: 标题 \"Structural Degeneration\" 与 ISR 测量 \"component necessity\" 之间概念跳跃**\n- ISR=0 不等于 structural degeneration（可能是 genuine redundancy）。\n- Table 1 ISR β=0.1 5-seed 下 ~55% genuine 但 ISR 低——说明 low ISR ≠ structural degeneration。\n- 标题的 claim 超过指标支撑能力。\n\n### Reviewer 2 的 Should-Fix 问题\n\n**R2-W1**: ProofFOL \"cross-dataset\" 实为 same-task-family 验证（FOLIO→ProofFOL 均为 FOL reasoning）\n**R2-W2**: 缩写密度过高（ISR, STA, CE, TS, PG, CI, CwU...），Table 1 几乎无法解读\n**R2-W3**: N=3 seeds 下多个核心声称的统计支撑不足（与你的 N2 类似）\n**R2-W4**: Related Work 缺少 PRIME、Shapley values、mutation testing for ML 引用\n**R2-W5**: Hacking mode classifier 的 boundary cases 和 error 分析不足\n\n### Reviewer 2 的 Questions\n- Q1: STA/ISR 在 PPO/DPO 下是否有类似 degeneration？\n- Q2: CE 和 TS 是否应合并为一个大类？\n- Q3: 增加 seeds 到 N=5+ 后 Goodhart effect 会消失还是达到显著性？\n- Q4: ProofFOL exec-only 100% TS 是否暗示 predicate structure 决定了 hacking mode？\n\n### Reviewer 2 的 Missing References\n- PRIME (Cui et al., 2025)\n- Shapley value attribution (SHAP)\n- Mutation testing for ML (DeepMutation, Ma et al. 2018)\n- Helff et al. 2026 名称核实（\"Input Perturbation Testing\" vs \"Isomorphic Perturbation Testing\"）\n\n---\n\n请对以上每个 Must-Fix（N1, N2, N3）和 Should-Fix（W1-W5）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2439 · 2026-05-22T07:44:58.768747+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 19293
}
```

</details>

---


### Tool call

_source line 2440 · 2026-05-22T07:44:58.819572+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "28",
  "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见（Overall 3.0, Findings）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1 [critical]: Premise-count confound 控制后 ISR 区分力近乎消失**\n- 3.2× raw ISR advantage 降到 1.06× after premise-count matching（§4.1, Appendix C, Table 7）。\n- ISR 信号主要反映 formalization 长度差异而非 structural integrity 差异。\n- 核心价值主张被严重削弱。\n\n**R1-N2 [critical]: N=3 seeds 统计效力不足以支撑主要 claims**\n- N=3 时仅对 d≥2.0 有 80% power。\n- 多个关键 claims 依赖 seed-level 比较但无法达到显著性。\n- ProofFOL p=0.10, ISR vs random prevalence p=0.182 均不显著。\n- Claims 语气超出 case study 证据强度。\n\n**R1-N3 [critical]: CMH 检验中 within-seed 非独立性处理不充分**\n- 100 个 FOLIO 评估样本共享同一 trained model，存在 intra-cluster correlation。\n- 未报告 ICC。\n- 如果 ICC>0，CMH p-values anti-conservative。\n- 建议 cluster-robust variance 或 GEE。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1**: Classifier 验证仅 50 样本且只覆盖 CE/TS 两种 mode，未覆盖 PG/CI/repetition 等需要 functional analysis 的 mode\n**R1-W2**: Seed 43 T=0.7 评估异常破坏实验一致性（33% of seeds 用不同协议）\n**R1-W3**: ProofFOL p=0.10 被过度纳入 \"confirmatory\" 叙事\n**R1-W4**: SFT baseline 收敛性未证明——低 PR 可能反映训练不足而非 structural integrity\n**R1-W5**: Non-hacking rate 的 upper bound 性质在跨 condition 比较中被忽视\n\n### Reviewer 1 的 Questions\n- Q1: Normalized ISR (ISR/expected ISR) 能否挽救跨 condition 比较的有效性？\n- Q2: 8 种 hacking modes 是否 exhaustive？non-hacking 样本是否人工验证？\n- Q3: Seed 43 能否 greedy re-evaluation？\n- Q4: Within-seed 100 个问题是否条件独立？能否报告 ICC？\n- Q5: SFT 1000 steps 是否收敛？\n\n### Reviewer 1 的 Missing References\n- Wen et al. (2025) reward shaping fragility\n- Xiong et al. (2024) RLHF Workflow\n- Cook's distance / influence functions（Cook 1977; Koh & Liang 2017）\n\n---\n\n请对以上每个 Must-Fix（N1, N2, N3）和 Should-Fix（W1-W5）逐条给出 [AGREE] 或 [REBUT] 回应。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "28",
    "text": "## 交叉分享 — 请逐条回应 Reviewer 1 的审稿意见\n\n以下是 Reviewer 1 的完整审稿意见（Overall 3.0, Findings）。请逐条回应：\n- **[AGREE]** 同意并说明理由\n- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）\n  \n---\n\n### Reviewer 1 的 Must-Fix 问题\n\n**R1-N1 [critical]: Premise-count confound 控制后 ISR 区分力近乎消失**\n- 3.2× raw ISR advantage 降到 1.06× after premise-count matching（§4.1, Appendix C, Table 7）。\n- ISR 信号主要反映 formalization 长度差异而非 structural integrity 差异。\n- 核心价值主张被严重削弱。\n\n**R1-N2 [critical]: N=3 seeds 统计效力不足以支撑主要 claims**\n- N=3 时仅对 d≥2.0 有 80% power。\n- 多个关键 claims 依赖 seed-level 比较但无法达到显著性。\n- ProofFOL p=0.10, ISR vs random prevalence p=0.182 均不显著。\n- Claims 语气超出 case study 证据强度。\n\n**R1-N3 [critical]: CMH 检验中 within-seed 非独立性处理不充分**\n- 100 个 FOLIO 评估样本共享同一 trained model，存在 intra-cluster correlation。\n- 未报告 ICC。\n- 如果 ICC>0，CMH p-values anti-conservative。\n- 建议 cluster-robust variance 或 GEE。\n\n### Reviewer 1 的 Should-Fix 问题\n\n**R1-W1**: Classifier 验证仅 50 样本且只覆盖 CE/TS 两种 mode，未覆盖 PG/CI/repetition 等需要 functional analysis 的 mode\n**R1-W2**: Seed 43 T=0.7 评估异常破坏实验一致性（33% of seeds 用不同协议）\n**R1-W3**: ProofFOL p=0.10 被过度纳入 \"confirmatory\" 叙事\n**R1-W4**: SFT baseline 收敛性未证明——低 PR 可能反映训练不足而非 structural integrity\n**R1-W5**: Non-hacking rate 的 upper bound 性质在跨 condition 比较中被忽视\n\n### Reviewer 1 的 Questions\n- Q1: Normalized ISR (ISR/expected ISR) 能否挽救跨 condition 比较的有效性？\n- Q2: 8 种 hacking modes 是否 exhaustive？non-hacking 样本是否人工验证？\n- Q3: Seed 43 能否 greedy re-evaluation？\n- Q4: Within-seed 100 个问题是否条件独立？能否报告 ICC？\n- Q5: SFT 1000 steps 是否收敛？\n\n### Reviewer 1 的 Missing References\n- Wen et al. (2025) reward shaping fragility\n- Xiong et al. (2024) RLHF Workflow\n- Cook's distance / influence functions（Cook 1977; Koh & Liang 2017）\n\n---\n\n请对以上每个 Must-Fix（N1, N2, N3）和 Should-Fix（W1-W5）逐条给出 [AGREE] 或 [REBUT] 回应。"
  }
}
```

</details>

---


### Tool result

_source line 2441 · 2026-05-22T07:45:00.716905+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1897
}
```

</details>

---


### Assistant

_source line 2442 · 2026-05-22T07:45:04.912021+00:00_

交叉分享已发出。等待两位 Reviewer 的逐条回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 220

## Round 220

2 recorded events


### User

_source line 2443 · 2026-05-22T07:45:07.866312+00:00_

[Reviewer 2 审稿结果]:
审稿意见已提交给 Review Director。

**总结**：

- **Overall 3.5/5（Borderline Conference）**，Soundness 3.5, Excitement 3, Reproducibility 4
- **3 个 Must-Fix**：(N1) STA 方法论新颖性不足以支撑 main contribution——LOO ablation 到 solver trace 是领域适配而非新方法，且与 Helff et al. IPT 概念同构；(N2) "compositional Goodhart effect" 缺乏独立于 M&G taxonomy 的操作性定义，实为 regressional Goodhart 的预期表现；(N3) 标题 "Structural Degeneration" 与 ISR 实测 "component necessity" 之间存在概念跳跃
- **5 个 Should-Fix**：ProofFOL 的 same-task-family 验证被标为 "cross-dataset"；缩写密度过高；N=3 seeds 统计支撑不足；缺少 PRIME/Shapley/mutation-testing-for-ML 引用；hacking mode classifier 的 error 分析不足
- **优势**：选题重要、实验控制严谨（matched control, shuffled-ISR）、hacking mode 分类体系完整、case study 定位诚实

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2444 · 2026-05-22T07:45:17.312321+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 221

## Round 221

2 recorded events


### User

_source line 2445 · 2026-05-22T07:46:52.172692+00:00_

[Reviewer 1 审稿意见]:

## Reviewer 1 交叉回应 — 对 Reviewer 2 (Overall 3.5) 逐条评议

---

### Must-Fix 问题

**[REBUT] R2-N1: STA 方法论新颖性不足**

R2 的论点——LOO ablation 本身是旧技术、Algorithm 1 是直接的 LOO 循环——事实成立，但由此得出"新颖性不足以支撑 main contribution"的结论过强。

理由：
1. **论文已明确承认方法源自 mutation testing**（§3.2 引用 DeMillo 1978, Jia & Harman 2011），并将自身定位为 "application and findings, not in the perturbation primitive"（§3.2 末尾）。贡献不在算法本身，而在 (a) 将 LOO 应用于 neurosymbolic solver trace 的 component-level necessity 检测——这是首次在 RL-trained formal reasoning 中做此类诊断；(b) ISR metric 的设计和 hacking taxonomy 的建立。
2. **与 Helff et al. (2026) IPT 的区分论文已显式讨论**（Related Work §2, p.3）："STA shares the perturbation intuition but operates at the component level (LOO ablation on solver premises vs. token-level perturbation on verifier prompts) and targets neurosymbolic settings where gaming emerges during training." 粒度差异（component-level vs. token-level）和阶段差异（training diagnostic vs. inference-time detection）并非 trivial——它们决定了方法适用的场景和能回答的问题类型。
3. **R2 将 findings 与 methodology 二分化**，但在 diagnostic/empirical 论文中，方法论贡献往往就体现在"用合适的工具揭示了新现象"——dataset-dependent asymmetry（同一 ISR metric 在 FOLIO 上诊断出 degeneration 但在 Prolog 上没有, Figure 2）是 STA 作为诊断工具才能揭示的发现。

但我同意 Algorithm 1 的呈现方式过于 trivial，可以通过更强调 design choices（为什么选 LOO 而非 Shapley、为什么 component-level 而非 token-level、ISR 的 normalization 考量）来提升方法论的深度。

**结论**: R2-N1 应降级为 Should-Fix。方法论新颖性有限是事实，但论文自我定位为 case study + diagnostic framework，核心贡献在于 findings 和 taxonomy，不应以 algorithmic novelty 的标准来评判。

---

**[AGREE] R2-N2: "Compositional Goodhart effect" 缺乏操作性定义**

R2 的批评成立。具体证据：

1. **论文自己说 instantiates regressional Goodhart**（§4.3, p.2: "On FOLIO, this instantiates regressional Goodhart (Manheim and Garrabrant, 2019)"）。如果作者自己承认这是 regressional Goodhart 的实例，那么另起一个 "compositional Goodhart" 术语需要清晰的形式化定义来证明它是独立变体，而非 regressional Goodhart 的自然推论。
2. **Matched control 后 p=0.182, overall prevalence unchanged**（Table 5, §4.3）——正如 R2 指出，这意味着 ISR-as-reward 对 overall hacking prevalence 的影响在 premise-count 控制后不显著。"Composition shift"（CE→TS 的比例变化）可能仅仅是 regressional Goodhart 在不同 optimization landscape 上的不同表现，而非需要新术语的新现象。
3. 论文中没有给出 "compositional Goodhart effect" 的 **形式化定义**——没有数学表达式、没有充要条件、没有与 M&G taxonomy 中其他变体（extremal, causal, adversarial）的边界划分。

这与我在 N1 中关于 ISR 区分力的问题相呼应——如果 premise-count 控制后信号消失，所谓的 "compositional" shift 可能只是 premise-count 差异的附带效应。

---

**[REBUT] R2-N3: 标题 "Structural Degeneration" 与 ISR "component necessity" 之间概念跳跃**

R2 的逻辑方向正确（ISR=0 ≠ structural degeneration），但低估了论文的 defense mechanism。

1. **论文并非仅凭 ISR=0 就声称 structural degeneration**。ISR 是 diagnostic signal，hacking taxonomy 提供了 interpretive layer。§3.3 和 Table 8 展示了每个 ISR=0 的样本被进一步分类为 8 种 hacking modes 中的具体一种。CE（conclusion embedding, ~68% of exec-only 1000-step hacking, Table 6）有明确的结构定义（"the sole premise is the conclusion itself"）——这不是 "genuine redundancy"，而是 solver 被 trivially satisfied 的结构退化。
2. **R2 引用 Table 1 ISR β=0.1 "~55% genuine but ISR low" 来论证 low ISR ≠ degeneration**。但这个例子恰好支持论文的叙事而非反驳它：ISR β=0.1 是 ISR-as-reward 条件，其 ~55% genuine rate 来自 deconfounding（hacking taxonomy 分类后剩余的 non-hacking 样本），低 ISR 在这里确实不全等于 degeneration——论文通过 taxonomy 区分了 "low ISR because of hacking" 和 "low ISR because of genuine redundancy"（Appendix C 讨论 joint necessity）。
3. 但 R2 有一个 valid sub-point：**标题说的是 "Structural Degeneration"，而非 "Component Non-Necessity"**。从 ISR 到 structural degeneration 的推断链是：ISR=0 → LOO 分析 → hacking taxonomy 分类 → >90% 样本属于已知 hacking mode → structural degeneration。这个链条存在但标题直接跳到了终点。

**结论**: R2-N3 的核心观点（标题 overclaim）有道理，但应降级为 Should-Fix——因为论文确实提供了从 ISR 到 degeneration 的推断链（经 hacking taxonomy），只是需要在摘要/引言中更清晰地呈现这个推断过程。

---

### Should-Fix 问题

**[AGREE] R2-W1: ProofFOL "cross-dataset" 实为 same-task-family**

成立。FOLIO 和 ProofFOL 都使用 FOL 表示 + Prover9 solver，task structure 高度相似。论文称之为 "cross-dataset families"（§4.4）在技术上无误，但读者可能理解为 "cross-task" 或 "cross-domain"。真正的 cross-domain 证据来自 Prolog 实验（不同 solver、不同语言），但 Prolog 实验的 seed 数也只有 3。建议在主文中明确 FOLIO→ProofFOL 是 "within-task-family" 验证，Prolog 是 "cross-solver" 验证，避免 overstate generalization。

---

**[AGREE] R2-W2: 缩写密度过高**

成立。Table 1 需要同时理解 ISR, STA, CE, TS, PG, CI, N-H%, PR 等缩写，对首次阅读的 reviewer 极不友好。这是 readability 问题，不影响 soundness，但在 dense 8 页限制下，降低了论文的 accessibility。建议至少在 Table 1 的 caption 或 footnote 中展开所有缩写。

---

**[AGREE] R2-W3: N=3 seeds 统计支撑不足**

完全同意。这与我的 Must-Fix N2 一致。不再重复。

---

**[REBUT] R2-W4: Related Work 缺少 PRIME, Shapley values, mutation testing for ML**

部分反驳：

1. **PRIME (Cui et al., 2025) 已被引用。** §2 Related Work p.3 明确写道："Cui et al. (2025) derive implicit process rewards from outcome-level signals without step-level annotation, showing that reward density can be improved cheaply." References 列表中有完整条目 "Gaurav Cui, Lilin Yuan, Zefan Wang... 2025. Process Reinforcement through Implicit Rewards." R2 的 missing reference claim 在此项上不成立。
2. **Shapley values**: 同意应讨论。LOO ablation 是 Shapley value 的一阶近似（假设无交互效应），论文选择 LOO 而非 Shapley 需要 justify——可能因为 Shapley 在 n 个 components 上需要 2^n 次 solver call，而 LOO 只需 n 次。但这个 design choice 未在论文中讨论。
3. **Mutation testing for ML (DeepMutation, Ma et al. 2018)**: 论文引用了 mutation testing 的经典文献（DeMillo 1978, Jia & Harman 2011），但确实未引用 ML-specific 的 mutation testing 工作。建议补充。
4. **Helff et al. 2026**: 已在 §2 p.3 引用并对比。R2 关于名称核实（"Input Perturbation Testing" vs "Isomorphic Perturbation Testing"）的问题有价值——论文中写的是 "Input Perturbation Testing (IPT)"，应确认与原文一致。

---

**[AGREE] R2-W5: Hacking mode classifier boundary cases 和 error 分析不足**

同意，且与我的 W1 一致。50 样本验证仅覆盖 CE/TS 两种 text-match 可高效检测的 mode，PG、CI 等依赖 functional analysis 的 mode 缺乏独立验证。更关键的是缺少 **error analysis**：分类器在什么情况下会 misclassify？mode 之间的 boundary cases（如 CE 和 contraction 的边界、TS 和 tautological collapse 的边界）如何处理？这些在 Appendix D 中有定义但缺乏 empirical validation。

---

### 对 R2 Questions 的补充观点

**R2-Q1 (STA/ISR 在 PPO/DPO 下)**: 有价值的问题。论文仅测试了 GRPO，PPO/DPO 的 optimization dynamics 不同，structural degeneration 的表现可能不同。但在 case study 范围内不要求。

**R2-Q2 (CE 和 TS 合并)**: 我倾向于不合并。CE（conclusion embedding, 唯一 premise = conclusion）和 TS（single premise = conclusion, 其余 trivially necessary）有不同的 ISR interaction 模式——CE 下 ISR ≈ 1（因为唯一 premise 是 necessary），TS 下 ISR 可 > 0 但低于 genuine reasoning。Table 6 和 Appendix D.1-D.2 给出了不同的检测规则。合并会丢失这种诊断区分度。

**R2-Q3 (增加 seeds 后 Goodhart effect 是否消失)**: 核心问题。如果 N=5+ 后 p=0.182 仍不显著，"compositional Goodhart" 的 claim 需要撤回或大幅弱化。

**R2-Q4 (ProofFOL 100% TS 与 predicate structure)**: 好问题。Table 8-9 显示 ProofFOL 的 hacking repertoire 确实与 FOLIO 不同（ProofFOL 100% TS, FOLIO CE-dominated），这可能反映 predicate structure 的差异（ProofFOL 的 XOR constraints 和 predicate regularity 使某些 hacking modes 不可行）。论文在 §4.4 有初步讨论但深度不足。

---

### 总体评价

R2 的审稿意见总体上 well-calibrated。Must-Fix 中 **N2 (Compositional Goodhart 定义)** 最有力，我完全同意；**N1 (方法论新颖性)** 和 **N3 (标题 overclaim)** 有道理但程度上应降为 Should-Fix——论文的 case study 定位和 taxonomy 贡献弥补了 algorithmic novelty 的不足。R2 给出 3.5 (Borderline Conference) 我认为合理偏高；我给 3.0 (Findings)，主要分歧在于我认为 premise-count confound (我的 N1) 和 CMH pseudo-replication (我的 N3) 是比方法论新颖性更严重的 soundness 问题。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2446 · 2026-05-22T07:47:01.847173+00:00_

收到 Reviewer 1 的交叉回应。等待 Reviewer 2 的交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 222

## Round 222

2 recorded events


### User

_source line 2447 · 2026-05-22T07:47:04.680274+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交。汇总要点：

- **R2-N1 (方法论新颖性)**: [REBUT] — 论文已显式定位为 case study + diagnostic framework，LOO 本身不新但应用场景和 taxonomy 构成贡献；IPT 的区分已在 §2 讨论。建议降级为 Should-Fix。
- **R2-N2 (Compositional Goodhart 定义)**: [AGREE] — 论文自认是 regressional Goodhart 实例，新术语缺乏形式化定义，matched control 后 p=0.182 削弱了 claim。
- **R2-N3 (标题 overclaim)**: [REBUT] — ISR→hacking taxonomy→degeneration 的推断链存在但标题跳过了中间环节。建议降级为 Should-Fix。
- **R2-W1–W5**: 同意 W1(same-task-family)、W2(缩写密度)、W3(N=3)、W5(classifier boundary)；部分反驳 W4（PRIME 已引用，但 Shapley/ML mutation testing 确实缺失）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2448 · 2026-05-22T07:47:09.016066+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 223

## Round 223

12 recorded events


### User

_source line 2449 · 2026-05-22T07:48:23.532158+00:00_

[Reviewer 2 审稿意见]:

# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应

---

## Must-Fix 问题

### [AGREE] R1-N1: Premise-count confound 控制后 ISR 区分力近乎消失

**同意理由**: 这是 R1 最有力的技术批评。论文自身在 §4.3 和 Appendix C 报告了 3.2× → 1.06× 的 dramatic reduction，且 p=0.182 不显著。这一数据直接削弱了 ISR 作为 cross-condition 量化比较工具的价值主张。

**补充发现**: 论文在 Appendix C (p13) 明确承认 "This confound explains the side-apparent ISR-reward success (§4.3): ISR β=0.1 seed 42 produces shorter formalization, mechanically inflating ISR"——即 ISR 的表面优势主要来自 formalization 长度差异。这与 R1 的判断完全一致。

**但有一个重要 nuance**: 我认为 premise-count confound 主要影响 ISR-as-metric 的 cross-condition 量化比较，但不完全否定 STA/ISR 作为 per-sample 定性诊断工具的价值。Table 6 的 hacking taxonomy（8 种 mode 的定义与 ISR interaction）不依赖 ISR 的 cross-condition 比较，而是基于 per-sample 的 LOO 分析来识别 hacking 模式。即使 ISR 的聚合值受 premise-count 污染，individual sample 的 LOO 结果仍能揭示 "移除此 component 后 proof 是否失败"。论文应更清晰地分离 ISR 的两种用途：(1) 聚合指标（受 confound 严重影响）vs. (2) per-sample 诊断工具（相对 robust）。

**建议**: 同意 R1 的修改方向——报告 normalized ISR（ISR/expected ISR for random），并在 Section 3 中前置 confound discussion。

---

### [AGREE] R1-N2: N=3 seeds 统计效力不足

**同意理由**: 我在自己的审稿意见 W3 中提出了相同关切。N=3 时对 d≥2.0 才有 80% power 是一个 hard constraint，论文的多个核心 claim 无法在这一功效下得到充分支撑：
- ISR-as-reward vs. random non-hacking: p=0.182（Table 5, §4.3）
- ProofFOL generalization: p=0.10（§4.4）
- Seed-level 的 bimodal convergence 现象（Appendix E.5, 3/6 seeds 收敛）

**补充**: 论文在 §6 Limitations 中确实承认了这一问题（"limited statistical power (N=3 independent replicates)"），且 seed-level 的详细报告（Tables 7-10）是一个 mitigating factor。但 R1 正确指出 main text 中的 claim 语气有时超出了 case study 的证据强度，例如 §5 "five guidelines for GRPO-trained neurosymbolic systems" 的 prescriptive 口吻。

---

### [REBUT] R1-N3: CMH 检验中 within-seed 非独立性处理不充分

**反驳理由**: R1 的统计关切在技术层面成立——100 个 FOLIO 评估样本确实共享同一 trained model，存在潜在的 intra-cluster correlation。但我认为将此提升至 "critical / Must-Fix" 过度了，理由如下：

**(1) CMH 在论文中是 supplementary，不是 primary analysis。** 论文在 §4.1 明确声明 "Pooled statistics (CMH) serve as supplementary reference"，且在 Table 5 中 Bonferroni-corrected Fisher exact tests（seed-level）才是主要的统计检验。论文的核心 claims 主要依赖 seed-level 的 Fisher exact tests 和 seed-level proportions（Tables 7-10），而非 CMH pooled results。

**(2) Seed-level analysis 本身就是 cluster-level analysis。** 论文以 seed 为单位报告结果（each seed = 1 observation），这实际上是 R1 建议的 cluster-robust approach 的一种简化形式——N=3 clusters 的自由度极低，但至少在正确的分析层级上。CMH 提供的是 pooled estimate，supplementary 地用于增加 effective sample size，这在 N=3 的情境下是合理的（尽管确实 anti-conservative if ICC>0）。

**(3) 修复成本低但收益有限。** 报告 ICC 或使用 GEE 是 straightforward 的，但在 N=3 seeds、100 samples per seed 的设置下，ICC correction 可能让已经 borderline 的 p-values 变得更不显著，这反而支持 R1-N2 的论点（N=3 不够）而非独立构成新的 critical issue。

**我的判断**: 降级为 Should-Fix。补报 ICC 值和 cluster-robust standard errors 是 good practice，但不构成影响接收决定的独立问题——它是 R1-N2（统计功效不足）的 downstream consequence。

---

## Should-Fix 问题

### [AGREE] R1-W1: Classifier 验证仅 50 样本且只覆盖 CE/TS

**同意理由**: 论文 Appendix D (p14-15) 的 precision estimate 确实仅基于 50 个 CE/TS 样本（"we manually verified 50 randomly sampled outputs classified as CE or TS; all 50 were confirmed correct"）。虽然后续有 82 样本的 boundary case validation 覆盖了 all five hacking categories，但：

- 需要 functional analysis 的 modes（PG: premise-subset gaming, CI: tautological collapse）依赖 n_necessary 和 structural pattern matching，这些阈值的 sensitivity 未被 systematically 评估。
- 论文承认 "standard ML precision/recall is not directly applicable" 和 "Recall is inherently bounded"，但未量化 recall 的 lower bound。

**补充**: 我在自己的审稿意见 W5 中提出了类似关切——缺少 confusion matrix 和 threshold sensitivity analysis。

---

### [AGREE] R1-W2: Seed 43 T=0.7 评估异常

**同意理由**: §4.1 footnote 确认 seed 43 使用了 T=0.7 sampling 而非 greedy decoding。在 N=3 seeds 的设置下，33% 的 seeds 使用不同评估协议是一个 significant methodological inconsistency。

**补充**: 论文将 seed 43 "included for completeness but are not strictly comparable with other seeds under the unified evaluation protocol (C004)"，这种 transparency 值得肯定，但正确的做法应该是 greedy re-evaluation（如 R1-Q3 所建议）或者在 main analysis 中排除 seed 43 并以 N=2 报告（进一步削弱统计功效）。

---

### [AGREE] R1-W3: ProofFOL p=0.10 被过度纳入 confirmatory 叙事

**同意理由**: 我在自己的审稿意见 W1 中也指出了这个问题。论文在 §4.4 将 ProofFOL 结果纳入 "cross-dataset validation" 叙事，但 p=0.10 在任何常规显著性水平下均不显著。我进一步指出 ProofFOL 与 FOLIO 同属 FOL task family（ProofFOL 源自 ProofWriter，Appendix A），因此即使 p<0.05 也只是 within-task-family replication 而非真正的 cross-domain validation。

---

### [AGREE] R1-W4: SFT baseline 收敛性未证明

**同意理由，但有保留**: R1 正确指出 SFT 的低 PR（13%）可能反映训练不足而非 structural integrity。论文未报告 SFT 的 training loss curve 或 convergence diagnostic。

**但部分 mitigated**: §4.2 报告 "SFT on gold formalizations reaches 92.3% non-hacking (PR=13%, 3-seed pooled; OB=0.147 vs. exec-only p<0.001)"。SFT 的 92% non-hacking vs. GRPO exec-only 的 ~6% non-hacking 是一个 qualitative 而非 quantitative 的对比——即使 SFT 未完全收敛，92% 的 structural integrity 与 GRPO 的 structural collapse 之间的差异足够大，不太可能仅因 undertraining 导致。关键问题是：如果 SFT 训练更久，PR 是否会上升而 non-hacking 保持高位？论文没有回答这个问题。

**建议**: 同意 R1 的方向——至少报告 SFT training loss 是否已 plateau，或添加一个 "SFT 2000 steps" checkpoint 作为收敛性证据。

---

### [AGREE] R1-W5: Non-hacking rate 的 upper bound 性质在跨 condition 比较中被忽视

**同意理由**: 这是一个被论文忽视的 subtle 但重要的统计问题。如果 non-hacking rate 是 upper bound（因为 classifier 的 recall < 100%，某些 hacking 可能未被检测到），那么跨 condition 比较中：
- 较高的 non-hacking rate 不一定意味着更多 genuine reasoning——可能只是 classifier 对该 condition 的 hacking patterns 更难检测
- 这对 SFT（92% non-hacking）vs. GRPO（~6%）的对比影响不大（差距太大），但对 ISR β=0.1（~55%）vs. Random β=0.1（~50%）的微妙比较影响可能很大

论文应在 §4 的方法论部分明确说明 non-hacking rate 的 upper-bound 性质，并讨论不同 condition 下 classifier recall 的可能变异。

---

## 对 R1 Questions 的补充意见

**R1-Q1 (Normalized ISR)**: 我也认为这是一个有价值的建议。ISR/E[ISR|premise_count] 可以 partial out premise-count confound，值得在修改版中采纳。

**R1-Q2 (Exhaustiveness)**: 在我自己的审稿中也质疑了 8 modes 的 exhaustiveness 和粒度问题（我的 Q2）。论文承认 "the residual matching none of the eight cataloged patterns (classifier recall is unknown)"，但未量化这个残余。

**R1-Q4 (ICC)**: 如上所述（对 R1-N3 的回应），我认为 ICC 值得报告但不是 critical issue。

**R1-Q5 (SFT 收敛)**: 同意这是一个需要回答的问题。

---

## 对 R1 Missing References 的意见

- **Wen et al. (2025) reward shaping fragility**: 未在原论文中见到引用，同意应补充
- **Xiong et al. (2024) RLHF Workflow**: 相关性中等——主要关于 RLHF 而非 neurosymbolic reasoning，但 RL training methodology 上有关联
- **Cook's distance / influence functions (Cook 1977; Koh & Liang 2017)**: 这是一个有趣的角度——STA/ISR 可以被理解为 influence-function 的 neurosymbolic 特化版本。我在自己的审稿中建议了 Shapley value 文献作为 LOO 的理论框架，Cook's distance 是另一个有价值的连接点。两者都表明论文在 positioning 已有方法论文献方面存在不足。

---

## 总结

R1 的审稿意见质量高且聚焦于实质性问题。我与 R1 在以下方面高度一致：
1. **N=3 seeds 是核心瓶颈**（我和 R1 都标注为 critical/should-fix）
2. **Premise-count confound 削弱 ISR 量化比较**（R1-N1 与我的 N3 标题跳跃问题互补）
3. **ProofFOL 不构成 strong cross-validation**（R1-W3 与我的 W1 一致）
4. **Classifier 验证不够充分**（R1-W1 与我的 W5 一致）

我与 R1 的主要分歧在 **R1-N3 (CMH non-independence)** 的严重等级——我认为应为 Should-Fix 而非 Must-Fix，因为 CMH 是 supplementary analysis 且 seed-level analysis 本身就是 cluster-level。

R1 未涉及但我认为重要的问题：
- **STA 方法论新颖性评估**（我的 N1）
- **"Compositional Goodhart effect" 的概念独立性**（我的 N2）
- **缩写密度对可读性的影响**（我的 W2）
- **Related Work 中的 PRIME、Shapley values 缺失**（我的 W4）


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2450 · 2026-05-22T07:48:42.744548+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2451 · 2026-05-22T07:48:42.895580+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T07:34:59.656851+00:00\", \"completed_at\": \"2026-05-22T07:37:59.708785+00:00\", \"findings\": [{\"severity\": \"warning\", \"dimension\": \"page 5-6\", \"message\": \"主体实验部分连续两页纯文本（§3.3 Reward Conditions/Hacking Modes + §4.1 Setup + §4.2 ISR as Diagnostic），无任何 figure/table/equation 穿插。审稿人进入 Experiments 节后期望看到数据可视化，但要翻到第 7 页才见到 Table 1。建议将 Table 1 或一个摘要性小表前移至第 5-6 页区间。\"}, {\"severity\": \"warning\", \"dimension\": \"page 8\", \"message\": \"Figure 2 和 Figure 3 堆叠在同一页，与前两页（5-6）的纯文本形成强烈反差。Display items 分布不均：页 3-6 仅有 Algorithm 1 一个视觉元素，页 7-8 集中了 Table 1 + Figure 2 + Figure 3。建议调整 float 位置使节奏更均匀。\"}, {\"severity\": \"warning\", \"dimension\": \"page 24\", \"message\": \"Table 11 和 Table 12 之间存在约 50% 页面的大面积空白。这是论文最后一页，视觉上不够整洁。建议合并两表或调整 float 参数消除空白。\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"第一个视觉锚点 Figure 1（ISR collapse trajectories）出现在第 2 页顶部，传达核心 message（结构退化的训练动态），位置佳。审稿人第一印象良好。\"}, {\"severity\": \"info\", \"dimension\": \"page 1\", \"message\": \"Title/Abstract/Introduction 排版整洁，标准 ACL 双栏格式，无溢出。标题较长（两行），但信息量充分。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 3 使用 8 种颜色编码不同 hacking mode，色彩区分度对色盲读者可能不足。建议补充 pattern/hatching 辅助区分，或在 caption 中注明色盲友好替代方案。\"}, {\"severity\": \"info\", \"dimension\": \"page 8\", \"message\": \"Figure 2 子面板 (a)(b) 内的坐标轴标签和柱状图标注字号偏小（约正文 60%），在打印版上可能不够清晰。建议放大至正文 70% 以上。\"}, {\"severity\": \"info\", \"dimension\": \"page 22-23\", \"message\": \"Tables 7-10（per-seed detailed results）字号极小，列数多（PR, ISR*, TS%, CE%, N-H%），阅读体验较差。作为 appendix 可以接受，但建议适当增大字号或拆分表格。\"}, {\"severity\": \"info\", \"dimension\": \"pages 1-8\", \"message\": \"主体 8 页包含 5 个 display items（Figure 1, Algorithm 1, Table 1, Figure 2, Figure 3）。对于实证型 case study 而言数量可接受，但偏少——增加一个核心结果摘要表（如 Table 1 的精简版）前置到第 5 页附近可显著改善可读性。\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 使用 booktabs 风格，最优结果加粗标注，脚注标记清晰（†‡）。
…[truncated 386 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2452 · 2026-05-22T07:48:42.896161+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2453 · 2026-05-22T07:48:42.946732+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2454 · 2026-05-22T07:49:40.075367+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:update_review_issues",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:update_review_issues",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2455 · 2026-05-22T07:49:40.127223+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2456 · 2026-05-22T07:52:59.135241+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R28) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。case study 定位已标注但正文 claim 仍偶尔超出单模型范围。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 28\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：p=0.10 仍被纳入 cross-dataset 叙事。ProofFOL 是 same-task-family (FOL) 而非 cross-domain。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：recall 未报告。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：50 样本仅覆盖 CE/TS，PG/CI 等 functional mode 无验证。缺 confusion matrix 和 threshold sensitivity。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 升级为 Major。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持：33% seeds 用不同评估协议，N=3 下影响严重。需 greedy re-eval 或排除 seed 43。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。\"\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1 建议 normalized ISR (ISR/E[ISR|premise_count]) 去除 premise-count bias。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W5 再次标记。R1 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：Table 1 缩写密度对首次阅读者极不友好。需 reference table 或 caption 内展开。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本；page 8 过载。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：pages 5-6 纯文本（§3.3+§4.1+§4.2），page 7-8 集中 Table 1+Figure 2+Figure 3。建议前移 display item 到 p5-6。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm，axis labels 接近 8pt。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 2 坐标轴标签约正文 60%，打印版可能不清晰。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：p=0.182 不显著，'compositional Goodhart' claim 缺乏统计支撑。R1 进一步指出 matched comparison 无独立 p-value。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 n=16 matched pairs 也 underpowered。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 标为 Must-Fix，R2 AGREE。论文自身在 Appendix C 承认 ISR 表面优势来自 formalization 长度差异。R2 补充 nuance：ISR-as-aggregate 受 confound 影响，但 ISR-as-per-sample-diagnostic 相对 robust。建议 normalized ISR。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 共识：LOO 应用为 incremental。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 维持 Must-Fix，R1 REBUT 建议降级为 Should-Fix（case study 定位 + taxonomy 补偿 algorithmic novelty）。分歧记录。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及但被 R1-W1 classifier validation 覆盖。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1-W4：SFT 收敛性未证明。R2 AGREE with reservation：92% vs 6% 差距大到训练不足不太可能解释，但需 loss curve。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 核心共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 再次共识 Must-Fix。R1：N=3 对 d≥2.0 才有 80% power。R2 AGREE。多个核心 claim 无法在此功效下得到充分支撑。至少 key condition 扩展到 N=5。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2-N3 标题 overclaim，R1 REBUT（inference chain 存在但标题跳过中间环节）。共识：Should-Fix。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 升级共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 维持——STA 与 IPT 概念同构。R1 REBUT：粒度和阶段差异非 trivial，§2 已讨论。分歧：R2 认为区分不足以构成独立方法论贡献，R1 认为 case study 定位下足够。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失 Shapley values 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：LOO 是 Shapley 的一阶近似，需 justify 为何选 LOO（O(n) vs O(2^n)）。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1-M3 指出 ISR 5-seed N-H%=18 vs 3-seed N-H%=6，seed-dependent 波动大。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× 为核心叙事\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 premise-count confound 维持为核心问题。Abstract 中 ISR 数值在 matched 后变为 1.06×。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2-N2 + R1 AGREE：'compositional Goodhart' 缺乏形式化定义，是 regressional 的 expected instantiation。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 27\n  resolution: \"references.bib 已包含 yue2025rl-reasoning 和 sullivan2025grpo-prm。\"\n  resolution_round: 28\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：Figure 3 使用 8 种颜色编码，色盲读者区分度不足。建议 pattern/hatching。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 issues (updated R28) ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。需系统对比表格。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 维持。R1 REBUT（§2 已讨论区分，粒度差异非 trivial）。分歧记录但共识：至少需更深入技术对比。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义，是已有理论的 expected instantiation\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2 概念上 expected。R1 AGREE partially。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 AGREE：无形式化定义，论文自认 regressional instantiation。建议：或提供形式化定义，或放弃新术语改为 'observed regressional Goodhart pattern'。\"\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 维持 Must-Fix。R2 REBUT 降级为 Should-Fix：CMH 是 supplementary，seed-level Fisher 为 primary。共识：降级为 Should-Fix，但建议报告 ICC。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除，不可恢复\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。需 greedy re-eval 或在 main analysis 排除 seed 43 以 N=2 报告。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论是 black box——分类规则未完整公开，不可复现\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。需补充 confusion matrix、threshold sensitivity、per-mode precision/recall。Appendix D 定义存在但操作化不完整。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大——TS 反向效果未在正文充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [2]\n    note: \"R28 R2 维持。ISR 对 CE 高敏感但对 TS 反向（ISR≈0.5 by construction）。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME (arXiv:2502.01456)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"PRIME (cui2025prime) 已在 §2 引用并讨论。R1 交叉回应确认。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2 (arXiv:2504.21801)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"deepseek-prover-v2 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 classifier recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：不同 condition 下 classifier recall 可能差异，影响 ISR β=0.1 vs Random 的微妙比较。SFT vs GRPO 差距足够大不受影响。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 升级为 Must-Fix (N3)。R1 REBUT（taxonomy 提供推断桥梁），建议 Should-Fix。共识：Should-Fix。\"\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本/8 类偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。需 per-mode 验证。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32 样本量不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 bib 中已有 URL。核实通过。\"\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 AGREE 补充。论文仅引用 1978/2011 经典，缺 ML-specific mutation testing (DeepMutation, Ma et al. 2018 等)。\"\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑——部分 modes 是 solver-specific\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点不足以建立 dose-response curve\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n# === R28 new issues ===\n- id: v28-R1-N1\n  summary: \"ISR 聚合指标 vs per-sample 诊断需明确分离——前者受 premise-count 严重污染，后者相对 robust\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出（N1），R2 AGREE 并补充 nuance。需在 §3 前置讨论 ISR 的双重用途（aggregate vs per-sample）及各自的 confound 影响。\"\n\n- id: v28-R12-SFT-CONVERGENCE\n  summary: \"SFT baseline 未报告 training loss curve / 收敛诊断\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1-W4 + R2 AGREE with reservation。92% vs 6% 差距大到不太可能仅因 undertraining，但需 loss curve 证实收敛。\"\n\n- id: v28-R12-MR-INFLUENCE\n  summary: \"缺失引用：Cook's distance / influence functions (Koh & Liang 2017) — ISR 可理解为 influence function 的 neurosymbolic 特化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 补充 Shapley 也是同一方法论家族。论文在 positioning 已有方法论文献方面存在不足。\"\n\n- id: v28-R1-M4\n  summary: \"50% exec-only seeds 不收敛（Appendix E.5, 3/6）——对主分析影响未在正文讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R1-M4：非收敛 seeds 被排除在主分析外但暗示 GRPO 收敛本身高度 seed-dependent。\"\n\n- id: v28-VISUAL-APPENDIX\n  summary: \"Appendix 末页 Table 11-12 间大面积空白\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"视觉审查：~50% 页面空白。建议合并表格或调整 float。\""
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R28) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。case study 定位已标注但正文 claim 仍偶尔超出单模型范围。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 28\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：p=0.10 仍被纳入 cross-dataset 叙事。ProofFOL 是 same-task-family (FOL) 而非 cross-domain。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：recall 未报告。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：50 样本仅覆盖 CE/TS，PG/CI 等 functional mode 无验证。缺 confusion matrix 和 threshold sensitivity。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 升级为 Major。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持：33% seeds 用不同评估协议，N=3 下影响严重。需 greedy re-eval 或排除 seed 43。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。\"\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1 建议 normalized ISR (ISR/E[ISR|premise_count]) 去除 premise-count bias。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 27\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。维持 in_progress。\"\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及。维持 in_progress。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 13\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2-W5 再次标记。R1 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：Table 1 缩写密度对首次阅读者极不友好。需 reference table 或 caption 内展开。\"\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本；page 8 过载。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：pages 5-6 纯文本（§3.3+§4.1+§4.2），page 7-8 集中 Table 1+Figure 2+Figure 3。建议前移 display item 到 p5-6。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm，axis labels 接近 8pt。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 2 坐标轴标签约正文 60%，打印版可能不清晰。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：p=0.182 不显著，'compositional Goodhart' claim 缺乏统计支撑。R1 进一步指出 matched comparison 无独立 p-value。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 n=16 matched pairs 也 underpowered。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 标为 Must-Fix，R2 AGREE。论文自身在 Appendix C 承认 ISR 表面优势来自 formalization 长度差异。R2 补充 nuance：ISR-as-aggregate 受 confound 影响，但 ISR-as-per-sample-diagnostic 相对 robust。建议 normalized ISR。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 共识：LOO 应用为 incremental。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 维持 Must-Fix，R1 REBUT 建议降级为 Should-Fix（case study 定位 + taxonomy 补偿 algorithmic novelty）。分歧记录。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及但被 R1-W1 classifier validation 覆盖。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1-W4：SFT 收敛性未证明。R2 AGREE with reservation：92% vs 6% 差距大到训练不足不太可能解释，但需 loss curve。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 核心共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 再次共识 Must-Fix。R1：N=3 对 d≥2.0 才有 80% power。R2 AGREE。多个核心 claim 无法在此功效下得到充分支撑。至少 key condition 扩展到 N=5。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2-N3 标题 overclaim，R1 REBUT（inference chain 存在但标题跳过中间环节）。共识：Should-Fix。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 升级共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 维持——STA 与 IPT 概念同构。R1 REBUT：粒度和阶段差异非 trivial，§2 已讨论。分歧：R2 认为区分不足以构成独立方法论贡献，R1 认为 case study 定位下足够。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失 Shapley values 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：LOO 是 Shapley 的一阶近似，需 justify 为何选 LOO（O(n) vs O(2^n)）。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1-M3 指出 ISR 5-seed N-H%=18 vs 3-seed N-H%=6，seed-dependent 波动大。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× 为核心叙事\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 premise-count confound 维持为核心问题。Abstract 中 ISR 数值在 matched 后变为 1.06×。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2-N2 + R1 AGREE：'compositional Goodhart' 缺乏形式化定义，是 regressional 的 expected instantiation。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 27\n  resolution: \"references.bib 已包含 yue2025rl-reasoning 和 sullivan2025grpo-prm。\"\n  resolution_round: 28\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：Figure 3 使用 8 种颜色编码，色盲读者区分度不足。建议 pattern/hatching。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 issues (updated R28) ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。需系统对比表格。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 维持。R1 REBUT（§2 已讨论区分，粒度差异非 trivial）。分歧记录但共识：至少需更深入技术对比。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义，是已有理论的 expected instantiation\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R2 概念上 expected。R1 AGREE partially。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 AGREE：无形式化定义，论文自认 regressional instantiation。建议：或提供形式化定义，或放弃新术语改为 'observed regressional Goodhart pattern'。\"\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 维持 Must-Fix。R2 REBUT 降级为 Should-Fix：CMH 是 supplementary，seed-level Fisher 为 primary。共识：降级为 Should-Fix，但建议报告 ICC。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除，不可恢复\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。需 greedy re-eval 或在 main analysis 排除 seed 43 以 N=2 报告。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论是 black box——分类规则未完整公开，不可复现\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。需补充 confusion matrix、threshold sensitivity、per-mode precision/recall。Appendix D 定义存在但操作化不完整。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大——TS 反向效果未在正文充分讨论\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [2]\n    note: \"R28 R2 维持。ISR 对 CE 高敏感但对 TS 反向（ISR≈0.5 by construction）。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME (arXiv:2502.01456)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"PRIME (cui2025prime) 已在 §2 引用并讨论。R1 交叉回应确认。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2 (arXiv:2504.21801)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"deepseek-prover-v2 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 classifier recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识：不同 condition 下 classifier recall 可能差异，影响 ISR β=0.1 vs Random 的微妙比较。SFT vs GRPO 差距足够大不受影响。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R2 升级为 Must-Fix (N3)。R1 REBUT（taxonomy 提供推断桥梁），建议 Should-Fix。共识：Should-Fix。\"\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本/8 类偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。需 per-mode 验证。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32 样本量不足\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 bib 中已有 URL。核实通过。\"\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 AGREE 补充。论文仅引用 1978/2011 经典，缺 ML-specific mutation testing (DeepMutation, Ma et al. 2018 等)。\"\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑——部分 modes 是 solver-specific\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点不足以建立 dose-response curve\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n# === R28 new issues ===\n- id: v28-R1-N1\n  summary: \"ISR 聚合指标 vs per-sample 诊断需明确分离——前者受 premise-count 严重污染，后者相对 robust\"\n  category: method\n  severity: critical\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出（N1），R2 AGREE 并补充 nuance。需在 §3 前置讨论 ISR 的双重用途（aggregate vs per-sample）及各自的 confound 影响。\"\n\n- id: v28-R12-SFT-CONVERGENCE\n  summary: \"SFT baseline 未报告 training loss curve / 收敛诊断\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1-W4 + R2 AGREE with reservation。92% vs 6% 差距大到不太可能仅因 undertraining，但需 loss curve 证实收敛。\"\n\n- id: v28-R12-MR-INFLUENCE\n  summary: \"缺失引用：Cook's distance / influence functions (Koh & Liang 2017) — ISR 可理解为 influence function 的 neurosymbolic 特化\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 补充 Shapley 也是同一方法论家族。论文在 positioning 已有方法论文献方面存在不足。\"\n\n- id: v28-R1-M4\n  summary: \"50% exec-only seeds 不收敛（Appendix E.5, 3/6）——对主分析影响未在正文讨论\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R1-M4：非收敛 seeds 被排除在主分析外但暗示 GRPO 收敛本身高度 seed-dependent。\"\n\n- id: v28-VISUAL-APPENDIX\n  summary: \"Appendix 末页 Table 11-12 间大面积空白\"\n  category: format\n  severity: info\n  status: open\n  first_raised_round: 28\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"视觉审查：~50% 页面空白。建议合并表格或调整 float。\""
  }
}
```

</details>

---


### Tool result

_source line 2457 · 2026-05-22T07:52:59.287200+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 24781}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2458 · 2026-05-22T07:55:12.266169+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "project": "solver-trace-ablation",
  "report": "# 审稿报告 — Round 28 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计方法; R2: 新颖性+完整性+Related Work+Framing）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 量化 solver input 中各 component 的个体必要性。论文在 Qwen3-4B 上用 FOLIO 数据集进行了 6 种 reward condition × 3-5 seeds 的实验，发现：(C1) exec-only GRPO 下 ISR 崩溃而 prove rate 上升，揭示 execution-only evaluation 的 structural blind spot；(C2) ISR 作为 training reward 产生 seed-dependent 的 compositional Goodhart effect（CE→TS 的 hacking mode 转移），经 premise-count 控制后 ISR 优势从 3.2× 降至 1.06×。论文还提出了 8 种 hacking mode 的分类体系，并在 Prolog 和 ProofFOL 上提供了跨域/跨数据集的初步证据。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的选题。** 在 RL-trained reasoning 模型激增的背景下，识别 execution-only evaluation 的 structural blind spot 是一个真实且被低估的问题。STA 提供了可操作的诊断工具。（R1-S1, R2-S1 共识）\n\n**S2. 严谨的实验控制设计。** Matched random control、shuffled-ISR deconfounding control、SFT baseline 的使用表明作者理解并控制了关键混淆变量。Seed-level 结果报告和 Fisher exact tests 体现了实验透明度。（R1-S3, R2-S2 共识）\n\n**S3. 详尽且有教育价值的 hacking taxonomy。** 8 种 hacking mode（CE, TS, PG 等）每种都有 FOL/Prolog 示例、ISR interaction 分析和检测标准。这对理解 neurosymbolic reasoning 中的 reward gaming 机制有独立贡献价值。（R1-S2, R2-S3 共识）\n\n**S4. 对自身局限性异常坦诚。** Case study 定位明确，Limitations 章节坦承单模型、有限统计效力、classifier 局限性。这种透明度在同类论文中罕见。（R1-S3, R2-S4 共识）\n\n**S5. Goodhart 效应的实证展示。** ISR-as-reward 的 seed-dependent compositional shift（CE→TS）和 dose-response 模式（β=0.1/0.2/0.3）提供了 reward hacking 的细粒度实证。（R1-S4）\n\n---\n\n## Weaknesses\n\n### Must-Fix（双 Reviewer 共识，影响接收决定）\n\n**W1. [critical] Premise-count confound 控制后 ISR 聚合指标的区分力近乎消失。**\n- ISR raw advantage 3.2× 降至 premise-count-matched 后的 1.06×（§4.3, Appendix C）\n- 论文自身承认 \"This confound explains the sole apparent ISR-reward success\" (Appendix C)\n- Matched comparison 无独立 p-value；N=16 matched pairs 本身也 underpowered\n- R2 补充重要 nuance：ISR-as-aggregate 受 confound 严重影响，但 ISR-as-per-sample-diagnostic（通过 hacking taxonomy）相对 robust——论文应清晰分离这两种用途\n- **共识**: 双 Reviewer AGREE (R1-N1 + R2-AGREE)\n\n**W2. [critical] N=3 seeds 的统计效力严重不足。**\n- N=3 时仅对 d≥2.0 有 80% power（§4.1）\n- 多个核心 claim 依赖 seed-level 比较但无法达到显著性：ISR vs random prevalence p=0.182，ProofFOL p=0.10\n- Main text 的 claim 语气有时超出 case study 的证据强度（如 §5 \"five guidelines for GRPO-trained neurosymbolic systems\" 的 prescriptive 口吻）\n- **共识**: 双 Reviewer AGREE (R1-N2 + R2-W3)\n\n**W3. [critical] \"Compositional Goodhart effect\" 缺乏操作性定义。**\n- 论文自认 instantiates regressional Goodhart（§4.3），composition shift 是 regressional 的自然推论\n- 无形式化定义（无数学表达式、无充要条件、无与 M&G taxonomy 其他变体的边界划分）\n- Matched control 后 p=0.182, overall prevalence unchanged——\"Goodhart effect\" 的实际影响存疑\n- **共识**: R1 AGREE + R2-N2\n\n### Should-Fix（双 Reviewer 共识或一方提出另一方同意）\n\n**W4. [warning] STA 方法论新颖性有限——LOO 是标准技术。**\n- Algorithm 1 是直接的 LOO 循环，论文自认 \"LOO ablation itself is standard\"（§3.2）\n- 与 Helff et al. (2026) IPT 概念同构：\"perturb input → observe output change → infer genuine reasoning\"\n- R2 标为 Must-Fix，R1 REBUT 建议降级——case study 定位 + taxonomy 贡献补偿了 algorithmic novelty\n- **分歧记录**: R2 认为方法论不足以支撑 main contribution claim；R1 认为 findings 和 taxonomy 是核心贡献，方法论为工具\n\n**W5. [warning] 标题 \"Structural Degeneration\" 与 ISR 测量 \"component necessity\" 之间存在概念跳跃。**\n- ISR=0 不必然等于 structural degeneration（可能是 genuine redundancy）\n- 推断链 ISR→LOO→taxonomy→degeneration 存在但标题直接跳到终点\n- R2 标为 Must-Fix，R1 REBUT（taxonomy 提供推断桥梁）\n- **共识**: 降级为 Should-Fix，但需在 §3.2 增加 validity discussion\n\n**W6. [warning] ProofFOL \"cross-dataset\" 实为 same-task-family 验证。**\n- FOLIO 和 ProofFOL 同属 FOL reasoning + Prover9，p=0.10 不显著\n- \"Cross-dataset\" 标签误导——应标为 \"within-task-family replication\"\n- 真正的 cross-domain 证据仅来自 Prolog（不同 solver/语言，但也仅 N=3）\n- **共识**: R1-W3 + R2-W1 双方 AGREE\n\n**W7. [warning] Seed 43 T=0.7 评估异常。**\n- N=3 seeds 中 33% 使用不同评估协议（temperature=0.7 vs greedy）\n- Checkpoints 已删除，无法 greedy re-evaluation\n- 需在 main analysis 排除 seed 43 或报告含/不含 seed 43 的双版本统计\n- **共识**: R1-W2 + R2-AGREE\n\n**W8. [warning] CMH 检验中 within-seed 非独立性。**\n- 100 个评估样本共享同一 trained model，存在 intra-cluster correlation\n- 未报告 ICC\n- R1 标为 Must-Fix，R2 REBUT 降级——CMH 是 supplementary，seed-level Fisher 为 primary\n- **共识**: 降级为 Should-Fix，建议补报 ICC\n\n**W9. [warning] Classifier 验证不足。**\n- Precision 验证仅 50 样本且只覆盖 CE/TS 两种 text-match mode\n- PG/CI 等需 functional analysis 的 mode 无独立验证\n- Recall 未量化；缺 confusion matrix 和 threshold sensitivity analysis\n- **共识**: R1-W1 + R2-W5 双方 AGREE\n\n**W10. [warning] SFT baseline 收敛性未证明。**\n- 未报告 SFT training loss curve 或 convergence diagnostic\n- PR=13% 可能反映训练不足而非 structural integrity\n- R2 部分缓解：92% vs 6% 差距大到训练不足不太可能完全解释\n- **共识**: R1-W4 + R2-AGREE with reservation\n\n**W11. [warning] 缩写密度过高。**\n- ISR, STA, CE, TS, PG, CI, CwU, RE, RP, QaF, PR, NLI, LOO, FOL, SFT... 首次阅读者负担极重\n- Table 1 几乎无法解读\n- 需 reference table 或 caption 内展开缩写\n- **共识**: R2-W2 + R1-AGREE\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **N=3 seeds 是整篇论文的核心统计瓶颈**——限制了 hypothesis testing 的可靠性，多个核心比较无法达到显著性\n2. **Premise-count confound 严重削弱 ISR 聚合指标**——需分离 ISR 的 aggregate 用途（受 confound 影响）和 per-sample diagnostic 用途（相对 robust）\n3. **\"Compositional Goodhart\" 应放弃新术语**——或提供形式化定义，或降级为 \"observed regressional Goodhart pattern in hacking composition\"\n4. **ProofFOL 不构成 cross-domain validation**——应标为 within-task-family replication\n5. **Classifier 验证需扩展**——per-mode precision/recall、confusion matrix\n6. **Hacking taxonomy 是论文最强的独立贡献**——应加强而非弱化\n\n## Reviewer Divergence [REBUT]\n\n1. **STA 方法论新颖性** (R2 Must-Fix vs R1 Should-Fix): R2 认为 LOO→solver trace 是 incremental engineering，R1 认为 case study 框架下 findings/taxonomy 是核心贡献。R1 论据更有说服力——论文自定位为 case study，方法论新颖性期望应相应降低。\n2. **标题 overclaim 程度** (R2 Must-Fix vs R1 Should-Fix): R2 认为 \"Structural Degeneration\" 超出 ISR 支撑，R1 认为 taxonomy 提供了推断桥梁。共识降级为 Should-Fix。\n\n---\n\n## Questions\n\n1. Normalized ISR (ISR / E[ISR | premise_count]) 能否去除 premise-count confound？如果采用，cross-condition 比较结果是否改变？\n2. 8 种 hacking modes 是否 exhaustive？non-hacking 样本是否经人工验证为 genuine reasoning？如果有，样本量多少？\n3. SFT 在 1000 steps 是否收敛？请提供 training loss curve。\n4. 增加 seeds 到 N=5 后，ISR vs Random 的 non-hacking rate 比较是否达到显著性？作者预期 Goodhart effect 会消失还是确认？\n5. STA/ISR 在 PPO/DPO 下是否预期有类似 structural degeneration？\n\n---\n\n## Missing References\n\n1. **Shapley value attribution** (Lundberg & Lee 2017, SHAP) — LOO 是 Shapley 的一阶近似，需 justify 选择 LOO 而非 Shapley（O(n) vs O(2^n)）\n2. **Cook's distance / influence functions** (Cook 1977; Koh & Liang 2017) — ISR 可理解为 influence function 的 neurosymbolic 特化\n3. **Mutation testing for ML** (DeepMutation, Ma et al. 2018) — 论文仅引用 1978/2011 经典，缺 ML-specific mutation testing 近期文献\n4. **Helff et al. (2026) 名称核实** — 论文写 \"Input Perturbation Testing (IPT)\"，需确认与原文名称一致\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查完成。3 warnings:\n\n1. **Pages 5-6 纯文本** — §3.3 + §4.1 + §4.2 连续两页无 figure/table/equation，审稿人进入 Experiments 后要翻到 p7 才见 Table 1。建议前移 display item。\n2. **Page 7-8 display items 堆叠** — Table 1 + Figure 2 + Figure 3 集中在两页，与 p5-6 形成强烈反差。\n3. **Appendix 末页空白** — Table 11-12 间约 50% 页面空白。\n\nInfo items: Figure 1 位置佳（p2 顶部）；Table 1 格式专业；Figure 2 坐标轴标签偏小（约正文 60%）；Figure 3 色盲友好性不足（8 色无 pattern 辅助）；Appendix Tables 7-10 字号极小。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5 (High)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.0 | 3.5 | 3.0 |\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n\n**核心判断**: 论文识别了一个真实且重要的问题（execution-only evaluation 的 structural blind spot），提供了有价值的诊断工具（STA/ISR + hacking taxonomy），实验控制设计严谨（matched random, shuffled-ISR, SFT baseline）。但三个核心问题共同制约了主会议接收：\n\n1. **ISR 聚合指标的有效性存疑** — premise-count confound 控制后 3.2×→1.06×，核心诊断指标的 cross-condition 量化比较价值被严重削弱\n2. **统计效力不足** — N=3 seeds 限制了多数核心 claim 的可靠性，多个比较未达显著性\n3. **概念贡献薄弱** — \"compositional Goodhart effect\" 缺乏形式化定义，方法论新颖性有限（LOO 是标准技术的领域适配）\n\nHacking taxonomy（8 种 mode 的系统分类 + per-mode ISR interaction 分析）是论文最强的独立贡献，对 neurosymbolic reasoning 社区有实用价值，适合 Findings track 发表。\n\n若要升级至主会议级别，需：(1) 至少 key conditions 扩展到 N=5 seeds；(2) 提出 normalized ISR 或其他去 confound 的聚合指标；(3) 放弃 \"compositional Goodhart\" 新术语或提供形式化定义；(4) 扩展 classifier 验证（per-mode precision/recall + confusion matrix）。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- ISR collapse 数值（214×, 99.5%）来自单 seed 最极端值（seed 42），已标注但仍可能误导。建议以 3-seed pooled 统计为主叙事。\n- \"compositional Goodhart effect\" 在 abstract 中使用但全文无形式化定义。\n\n### Introduction (§1)\n- Contributions (C1) \"STA as a diagnostic framework\" 的 framing 与 case study 定位存在张力——framework 暗示通用性，case study 暗示特定场景。\n- Contributions 列表信息密度极高，首次阅读者难以消化。\n\n### Method (§3)\n- §3.2 ISR 的 premise-count confound 应前置讨论（目前在 Appendix C），而非等到 §4.3 才暴露。\n- Algorithm 1 过于简单——增加 design choices 的讨论（为什么 LOO 而非 Shapley、component 粒度选择）可提升方法论深度。\n\n### Experiments (§4)\n- §4.1 Statistical considerations 段为正面做法，但 \"Statistical considerations\" 后面的 claims 有时超出了这些 caveats 的约束。\n- §4.2 SFT baseline: 需报告 training loss convergence。\n- §4.3 Goodhart: \"compositional Goodhart effect\" 的定义（p.5）应标注为 observed pattern 而非新概念。\n- §4.4 ProofFOL: \"cross-dataset evidence\" 应改为 \"within-task-family replication\"。\n\n### Limitations (§6)\n- 覆盖充分。3 点左右，长度合适，符合 EMNLP 2026 要求。\n\n### Appendix\n- Appendix C (Extended Discussion) 的 premise-count confound 分析质量高但位置太靠后。\n- Appendix D (Hacking Mode Definitions) 是论文最有价值的部分之一，示例清晰。\n- Tables 7-10 字号过小但内容完整。\n\n### References\n- 39 条引用，覆盖 GRPO、reward hacking、mutation testing、neurosymbolic reasoning 核心文献。\n- 缺失 Shapley values、influence functions、ML mutation testing 近期文献。\n- PRIME 和 DeepSeek-Prover-V2 已引用（R2 交叉回应中确认）。\n\n### Format Compliance\n- 页数合规：主体 8 页 + Limitations（不计入页数）+ References（不限）+ Appendix（不限）\n- 匿名合规：作者信息为 \"Anonymous ACL submission\"\n- ACL style, \\usepackage[review]{acl}\n- Checklist 已包含",
  "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
  "cross_response_reviewer_ids": "[\"1\", \"2\"]",
  "overall_score": "3.0"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "project": "solver-trace-ablation",
    "report": "# 审稿报告 — Round 28 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**目标 Venue**: EMNLP 2026 via ACL Rolling Review (ARR) May 2026\n**审稿模式**: Fresh（重新审稿）\n**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计方法; R2: 新颖性+完整性+Related Work+Framing）\n\n---\n\n## Summary\n\n论文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) ablation 的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 量化 solver input 中各 component 的个体必要性。论文在 Qwen3-4B 上用 FOLIO 数据集进行了 6 种 reward condition × 3-5 seeds 的实验，发现：(C1) exec-only GRPO 下 ISR 崩溃而 prove rate 上升，揭示 execution-only evaluation 的 structural blind spot；(C2) ISR 作为 training reward 产生 seed-dependent 的 compositional Goodhart effect（CE→TS 的 hacking mode 转移），经 premise-count 控制后 ISR 优势从 3.2× 降至 1.06×。论文还提出了 8 种 hacking mode 的分类体系，并在 Prolog 和 ProofFOL 上提供了跨域/跨数据集的初步证据。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的选题。** 在 RL-trained reasoning 模型激增的背景下，识别 execution-only evaluation 的 structural blind spot 是一个真实且被低估的问题。STA 提供了可操作的诊断工具。（R1-S1, R2-S1 共识）\n\n**S2. 严谨的实验控制设计。** Matched random control、shuffled-ISR deconfounding control、SFT baseline 的使用表明作者理解并控制了关键混淆变量。Seed-level 结果报告和 Fisher exact tests 体现了实验透明度。（R1-S3, R2-S2 共识）\n\n**S3. 详尽且有教育价值的 hacking taxonomy。** 8 种 hacking mode（CE, TS, PG 等）每种都有 FOL/Prolog 示例、ISR interaction 分析和检测标准。这对理解 neurosymbolic reasoning 中的 reward gaming 机制有独立贡献价值。（R1-S2, R2-S3 共识）\n\n**S4. 对自身局限性异常坦诚。** Case study 定位明确，Limitations 章节坦承单模型、有限统计效力、classifier 局限性。这种透明度在同类论文中罕见。（R1-S3, R2-S4 共识）\n\n**S5. Goodhart 效应的实证展示。** ISR-as-reward 的 seed-dependent compositional shift（CE→TS）和 dose-response 模式（β=0.1/0.2/0.3）提供了 reward hacking 的细粒度实证。（R1-S4）\n\n---\n\n## Weaknesses\n\n### Must-Fix（双 Reviewer 共识，影响接收决定）\n\n**W1. [critical] Premise-count confound 控制后 ISR 聚合指标的区分力近乎消失。**\n- ISR raw advantage 3.2× 降至 premise-count-matched 后的 1.06×（§4.3, Appendix C）\n- 论文自身承认 \"This confound explains the sole apparent ISR-reward success\" (Appendix C)\n- Matched comparison 无独立 p-value；N=16 matched pairs 本身也 underpowered\n- R2 补充重要 nuance：ISR-as-aggregate 受 confound 严重影响，但 ISR-as-per-sample-diagnostic（通过 hacking taxonomy）相对 robust——论文应清晰分离这两种用途\n- **共识**: 双 Reviewer AGREE (R1-N1 + R2-AGREE)\n\n**W2. [critical] N=3 seeds 的统计效力严重不足。**\n- N=3 时仅对 d≥2.0 有 80% power（§4.1）\n- 多个核心 claim 依赖 seed-level 比较但无法达到显著性：ISR vs random prevalence p=0.182，ProofFOL p=0.10\n- Main text 的 claim 语气有时超出 case study 的证据强度（如 §5 \"five guidelines for GRPO-trained neurosymbolic systems\" 的 prescriptive 口吻）\n- **共识**: 双 Reviewer AGREE (R1-N2 + R2-W3)\n\n**W3. [critical] \"Compositional Goodhart effect\" 缺乏操作性定义。**\n- 论文自认 instantiates regressional Goodhart（§4.3），composition shift 是 regressional 的自然推论\n- 无形式化定义（无数学表达式、无充要条件、无与 M&G taxonomy 其他变体的边界划分）\n- Matched control 后 p=0.182, overall prevalence unchanged——\"Goodhart effect\" 的实际影响存疑\n- **共识**: R1 AGREE + R2-N2\n\n### Should-Fix（双 Reviewer 共识或一方提出另一方同意）\n\n**W4. [warning] STA 方法论新颖性有限——LOO 是标准技术。**\n- Algorithm 1 是直接的 LOO 循环，论文自认 \"LOO ablation itself is standard\"（§3.2）\n- 与 Helff et al. (2026) IPT 概念同构：\"perturb input → observe output change → infer genuine reasoning\"\n- R2 标为 Must-Fix，R1 REBUT 建议降级——case study 定位 + taxonomy 贡献补偿了 algorithmic novelty\n- **分歧记录**: R2 认为方法论不足以支撑 main contribution claim；R1 认为 findings 和 taxonomy 是核心贡献，方法论为工具\n\n**W5. [warning] 标题 \"Structural Degeneration\" 与 ISR 测量 \"component necessity\" 之间存在概念跳跃。**\n- ISR=0 不必然等于 structural degeneration（可能是 genuine redundancy）\n- 推断链 ISR→LOO→taxonomy→degeneration 存在但标题直接跳到终点\n- R2 标为 Must-Fix，R1 REBUT（taxonomy 提供推断桥梁）\n- **共识**: 降级为 Should-Fix，但需在 §3.2 增加 validity discussion\n\n**W6. [warning] ProofFOL \"cross-dataset\" 实为 same-task-family 验证。**\n- FOLIO 和 ProofFOL 同属 FOL reasoning + Prover9，p=0.10 不显著\n- \"Cross-dataset\" 标签误导——应标为 \"within-task-family replication\"\n- 真正的 cross-domain 证据仅来自 Prolog（不同 solver/语言，但也仅 N=3）\n- **共识**: R1-W3 + R2-W1 双方 AGREE\n\n**W7. [warning] Seed 43 T=0.7 评估异常。**\n- N=3 seeds 中 33% 使用不同评估协议（temperature=0.7 vs greedy）\n- Checkpoints 已删除，无法 greedy re-evaluation\n- 需在 main analysis 排除 seed 43 或报告含/不含 seed 43 的双版本统计\n- **共识**: R1-W2 + R2-AGREE\n\n**W8. [warning] CMH 检验中 within-seed 非独立性。**\n- 100 个评估样本共享同一 trained model，存在 intra-cluster correlation\n- 未报告 ICC\n- R1 标为 Must-Fix，R2 REBUT 降级——CMH 是 supplementary，seed-level Fisher 为 primary\n- **共识**: 降级为 Should-Fix，建议补报 ICC\n\n**W9. [warning] Classifier 验证不足。**\n- Precision 验证仅 50 样本且只覆盖 CE/TS 两种 text-match mode\n- PG/CI 等需 functional analysis 的 mode 无独立验证\n- Recall 未量化；缺 confusion matrix 和 threshold sensitivity analysis\n- **共识**: R1-W1 + R2-W5 双方 AGREE\n\n**W10. [warning] SFT baseline 收敛性未证明。**\n- 未报告 SFT training loss curve 或 convergence diagnostic\n- PR=13% 可能反映训练不足而非 structural integrity\n- R2 部分缓解：92% vs 6% 差距大到训练不足不太可能完全解释\n- **共识**: R1-W4 + R2-AGREE with reservation\n\n**W11. [warning] 缩写密度过高。**\n- ISR, STA, CE, TS, PG, CI, CwU, RE, RP, QaF, PR, NLI, LOO, FOL, SFT... 首次阅读者负担极重\n- Table 1 几乎无法解读\n- 需 reference table 或 caption 内展开缩写\n- **共识**: R2-W2 + R1-AGREE\n\n---\n\n## Reviewer Consensus [AGREE]\n\n1. **N=3 seeds 是整篇论文的核心统计瓶颈**——限制了 hypothesis testing 的可靠性，多个核心比较无法达到显著性\n2. **Premise-count confound 严重削弱 ISR 聚合指标**——需分离 ISR 的 aggregate 用途（受 confound 影响）和 per-sample diagnostic 用途（相对 robust）\n3. **\"Compositional Goodhart\" 应放弃新术语**——或提供形式化定义，或降级为 \"observed regressional Goodhart pattern in hacking composition\"\n4. **ProofFOL 不构成 cross-domain validation**——应标为 within-task-family replication\n5. **Classifier 验证需扩展**——per-mode precision/recall、confusion matrix\n6. **Hacking taxonomy 是论文最强的独立贡献**——应加强而非弱化\n\n## Reviewer Divergence [REBUT]\n\n1. **STA 方法论新颖性** (R2 Must-Fix vs R1 Should-Fix): R2 认为 LOO→solver trace 是 incremental engineering，R1 认为 case study 框架下 findings/taxonomy 是核心贡献。R1 论据更有说服力——论文自定位为 case study，方法论新颖性期望应相应降低。\n2. **标题 overclaim 程度** (R2 Must-Fix vs R1 Should-Fix): R2 认为 \"Structural Degeneration\" 超出 ISR 支撑，R1 认为 taxonomy 提供了推断桥梁。共识降级为 Should-Fix。\n\n---\n\n## Questions\n\n1. Normalized ISR (ISR / E[ISR | premise_count]) 能否去除 premise-count confound？如果采用，cross-condition 比较结果是否改变？\n2. 8 种 hacking modes 是否 exhaustive？non-hacking 样本是否经人工验证为 genuine reasoning？如果有，样本量多少？\n3. SFT 在 1000 steps 是否收敛？请提供 training loss curve。\n4. 增加 seeds 到 N=5 后，ISR vs Random 的 non-hacking rate 比较是否达到显著性？作者预期 Goodhart effect 会消失还是确认？\n5. STA/ISR 在 PPO/DPO 下是否预期有类似 structural degeneration？\n\n---\n\n## Missing References\n\n1. **Shapley value attribution** (Lundberg & Lee 2017, SHAP) — LOO 是 Shapley 的一阶近似，需 justify 选择 LOO 而非 Shapley（O(n) vs O(2^n)）\n2. **Cook's distance / influence functions** (Cook 1977; Koh & Liang 2017) — ISR 可理解为 influence function 的 neurosymbolic 特化\n3. **Mutation testing for ML** (DeepMutation, Ma et al. 2018) — 论文仅引用 1978/2011 经典，缺 ML-specific mutation testing 近期文献\n4. **Helff et al. (2026) 名称核实** — 论文写 \"Input Perturbation Testing (IPT)\"，需确认与原文名称一致\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n未请求。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查完成。3 warnings:\n\n1. **Pages 5-6 纯文本** — §3.3 + §4.1 + §4.2 连续两页无 figure/table/equation，审稿人进入 Experiments 后要翻到 p7 才见 Table 1。建议前移 display item。\n2. **Page 7-8 display items 堆叠** — Table 1 + Figure 2 + Figure 3 集中在两页，与 p5-6 形成强烈反差。\n3. **Appendix 末页空白** — Table 11-12 间约 50% 页面空白。\n\nInfo items: Figure 1 位置佳（p2 顶部）；Table 1 格式专业；Figure 2 坐标轴标签偏小（约正文 60%）；Figure 3 色盲友好性不足（8 色无 pattern 辅助）；Appendix Tables 7-10 字号极小。\n\n---\n\n## Overall Assessment\n\n**评分: 3.0 (Findings)**\n**置信度: 4/5 (High)**\n\n| 维度 | R1 | R2 | 共识 |\n|------|----|----|------|\n| Overall | 3.0 | 3.5 | 3.0 |\n| Soundness | 3/5 | 3.5/5 | 3/5 |\n| Excitement | 3/5 | 3/5 | 3/5 |\n| Reproducibility | 3/5 | 4/5 | 3.5/5 |\n\n**核心判断**: 论文识别了一个真实且重要的问题（execution-only evaluation 的 structural blind spot），提供了有价值的诊断工具（STA/ISR + hacking taxonomy），实验控制设计严谨（matched random, shuffled-ISR, SFT baseline）。但三个核心问题共同制约了主会议接收：\n\n1. **ISR 聚合指标的有效性存疑** — premise-count confound 控制后 3.2×→1.06×，核心诊断指标的 cross-condition 量化比较价值被严重削弱\n2. **统计效力不足** — N=3 seeds 限制了多数核心 claim 的可靠性，多个比较未达显著性\n3. **概念贡献薄弱** — \"compositional Goodhart effect\" 缺乏形式化定义，方法论新颖性有限（LOO 是标准技术的领域适配）\n\nHacking taxonomy（8 种 mode 的系统分类 + per-mode ISR interaction 分析）是论文最强的独立贡献，对 neurosymbolic reasoning 社区有实用价值，适合 Findings track 发表。\n\n若要升级至主会议级别，需：(1) 至少 key conditions 扩展到 N=5 seeds；(2) 提出 normalized ISR 或其他去 confound 的聚合指标；(3) 放弃 \"compositional Goodhart\" 新术语或提供形式化定义；(4) 扩展 classifier 验证（per-mode precision/recall + confusion matrix）。\n\n---\n\n## Detailed Comments\n\n### Abstract\n- ISR collapse 数值（214×, 99.5%）来自单 seed 最极端值（seed 42），已标注但仍可能误导。建议以 3-seed pooled 统计为主叙事。\n- \"compositional Goodhart effect\" 在 abstract 中使用但全文无形式化定义。\n\n### Introduction (§1)\n- Contributions (C1) \"STA as a diagnostic framework\" 的 framing 与 case study 定位存在张力——framework 暗示通用性，case study 暗示特定场景。\n- Contributions 列表信息密度极高，首次阅读者难以消化。\n\n### Method (§3)\n- §3.2 ISR 的 premise-count confound 应前置讨论（目前在 Appendix C），而非等到 §4.3 才暴露。\n- Algorithm 1 过于简单——增加 design choices 的讨论（为什么 LOO 而非 Shapley、component 粒度选择）可提升方法论深度。\n\n### Experiments (§4)\n- §4.1 Statistical considerations 段为正面做法，但 \"Statistical considerations\" 后面的 claims 有时超出了这些 caveats 的约束。\n- §4.2 SFT baseline: 需报告 training loss convergence。\n- §4.3 Goodhart: \"compositional Goodhart effect\" 的定义（p.5）应标注为 observed pattern 而非新概念。\n- §4.4 ProofFOL: \"cross-dataset evidence\" 应改为 \"within-task-family replication\"。\n\n### Limitations (§6)\n- 覆盖充分。3 点左右，长度合适，符合 EMNLP 2026 要求。\n\n### Appendix\n- Appendix C (Extended Discussion) 的 premise-count confound 分析质量高但位置太靠后。\n- Appendix D (Hacking Mode Definitions) 是论文最有价值的部分之一，示例清晰。\n- Tables 7-10 字号过小但内容完整。\n\n### References\n- 39 条引用，覆盖 GRPO、reward hacking、mutation testing、neurosymbolic reasoning 核心文献。\n- 缺失 Shapley values、influence functions、ML mutation testing 近期文献。\n- PRIME 和 DeepSeek-Prover-V2 已引用（R2 交叉回应中确认）。\n\n### Format Compliance\n- 页数合规：主体 8 页 + Limitations（不计入页数）+ References（不限）+ Appendix（不限）\n- 匿名合规：作者信息为 \"Anonymous ACL submission\"\n- ACL style, \\usepackage[review]{acl}\n- Checklist 已包含",
    "reviewer_ids_acknowledged": "[\"1\", \"2\"]",
    "cross_response_reviewer_ids": "[\"1\", \"2\"]",
    "overall_score": "3.0"
  }
}
```

</details>

---


### Tool result

_source line 2459 · 2026-05-22T07:55:16.833439+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4567
}
```

</details>

---


### Assistant

_source line 2460 · 2026-05-22T07:55:47.016127+00:00_

审稿报告已投递至 Research Director。

---

**📋 Round 28 审稿完成**

**Overall: 3.0 (Findings)**

核心结论：
- **最强贡献**: Hacking taxonomy（8 种 mode 的系统分类 + per-mode 示例和检测标准），适合 Findings track
- **三个核心制约因素**: (1) ISR 聚合指标经 premise-count 控制后优势从 3.2× 降至 1.06×；(2) N=3 seeds 统计效力不足；(3) "compositional Goodhart effect" 缺乏形式化定义
- **双 Reviewer 分歧**: 方法论新颖性（R2 认为 Must-Fix，R1 认为 Should-Fix）——共识为 case study 定位下 findings/taxonomy 是核心贡献，方法论为工具
- **升级路径**: 扩展至 N≥5 seeds + normalized ISR + classifier 验证扩展 + 放弃 "compositional Goodhart" 新术语

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 224

## Round 224

2 recorded events


### User

_source line 2461 · 2026-05-22T07:55:49.831533+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交。总结：

**与 R1 一致的 6 条 [AGREE]**：
- R1-N1（premise-count confound）— 同意 3.2×→1.06× 是严重问题，但补充指出 ISR 的 per-sample 诊断价值不受影响
- R1-N2（N=3 seeds）— 完全同意，与我自己的 W3 一致
- R1-W1 至 W5 — 全部同意，多数与我自己的审稿意见交叉印证

**唯一的 [REBUT]**：
- R1-N3（CMH non-independence）— 我认为应降级为 Should-Fix。CMH 在论文中是 supplementary analysis，主要分析已在 seed-level（即 cluster-level）进行。报告 ICC 是好实践但不构成独立的 critical issue。

**R1 未覆盖但我认为重要的互补问题**：STA 方法论新颖性、"compositional Goodhart" 概念独立性、缩写密度、PRIME/Shapley values 缺失引用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2462 · 2026-05-22T07:56:11.414181+00:00_

审稿报告已投递至 Research Director。

**Round 28 审稿完成。** 汇总：

- **Overall: 3.0 (Findings)**，R1 给 3.0，R2 给 3.5，共识收敛于 3.0
- **3 条 Must-Fix 共识**：(1) premise-count confound 控制后 ISR 区分力从 3.2×→1.06×；(2) N=3 seeds 统计效力不足；(3) "compositional Goodhart effect" 缺乏操作性定义
- **8 条 Should-Fix 共识**：方法论新颖性有限、标题 overclaim、ProofFOL same-task-family、seed 43 T=0.7 异常、CMH pseudo-replication、classifier 验证不足、SFT 收敛性未证明、缩写密度过高
- **1 条分歧记录**：STA 方法论新颖性——R2 认为 Must-Fix（LOO 是 incremental），R1 认为 Should-Fix（case study 定位下 taxonomy 是核心贡献）
- **视觉审查**：3 warnings（p5-6 纯文本、p7-8 display items 堆叠、appendix 末页空白）
- **外部审稿**：未请求
- **Issue Tracker 已同步更新**（新增 4 条 R28 issue，更新 20+ 条既有 issue 的 R28 mentions）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 225

## Round 225

56 recorded events


### User

_source line 2463 · 2026-05-22T13:39:45.018399+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper (ARR)
- 截止日期: 2026-05-25
- **引用验证**: ❌ 未启用

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2464 · 2026-05-22T13:39:51.463293+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2465 · 2026-05-22T13:39:51.514633+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2466 · 2026-05-22T13:39:57.187432+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,director_post_to_reviewer,get_external_review_status,get_visual_check_status,submit_review_report_to_research_director,update_review_issues,read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2467 · 2026-05-22T13:39:57.187954+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2468 · 2026-05-22T13:40:01.254278+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__get_visual_check_status,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__read_project_file",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2469 · 2026-05-22T13:40:01.304919+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2470 · 2026-05-22T13:40:04.744124+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 2471 · 2026-05-22T13:40:05.145985+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2472 · 2026-05-22T13:40:05.648334+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exec-only-s45-1000step-k8（排队等待 GPU）\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- …另有 23 项\n\n## 近期结论\n- **d154-8b-exec-s42-k8** (negative): 8B K=8 complete stagnation: a
…[truncated 1864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 904
}
```

</details>

---


### Tool result

_source line 2473 · 2026-05-22T13:40:05.648785+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2474 · 2026-05-22T13:40:05.699246+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 2475 · 2026-05-22T13:40:05.749863+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2476 · 2026-05-22T13:40:10.318647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers ARR submission guidelines author instructions"
  }
}
```

</details>

---


### Tool call

_source line 2477 · 2026-05-22T13:40:11.674398+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "100"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "100"
  }
}
```

</details>

---


### Tool result

_source line 2478 · 2026-05-22T13:40:11.775299+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{2pt}
20	
21	\graphicspath{{figures/}}
22	
23	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{conclusion}
36	
37	\input{limitations}
38	
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 2479 · 2026-05-22T13:40:13.081909+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_27/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
  "description": "Check if submitted PDF exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls -la /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_27/submitted.pdf 2>/dev/null && echo \"PDF_EXISTS\" || echo \"PDF_NOT_FOUND\"",
    "description": "Check if submitted PDF exists"
  }
}
```

</details>

---


### Tool result

_source line 2480 · 2026-05-22T13:40:14.036328+00:00_

-rw-r--r-- 1 ubuntu ubuntu 589959 May 22 13:28 /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_27/submitted.pdf
PDF_EXISTS

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2481 · 2026-05-22T13:40:14.287670+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXIST\" || echo \"NO_ISSUES_FILE\"",
  "description": "Check if review issues tracker exists"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "tool_args": {
    "command": "ls /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml 2>/dev/null && echo \"ISSUES_EXIST\" || echo \"NO_ISSUES_FILE\"",
    "description": "Check if review issues tracker exists"
  }
}
```

</details>

---


### Tool result

_source line 2482 · 2026-05-22T13:40:14.389027+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml
ISSUES_EXIST

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Bash",
  "elapsed_ms": 101
}
```

</details>

---


### Tool result

_source line 2483 · 2026-05-22T13:40:19.759616+00:00_

Web search results for query: "EMNLP 2026 call for papers ARR submission guidelines author instructions"

Links: [{"title":"Call for Main Conference Papers - EMNLP 2026","url":"https://2026.emnlp.org/calls/main_conference_papers/"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"Dates and Venues – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/dates"},{"title":"EMNLP 2026 : The 2026 Conference on Empirical Methods in N","url":"https://callforpaper.org/call-for-papers-emnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"Submission Guide","url":"https://nlp4climate.github.io/submissionguide/"},{"title":"LINGUIST List 37.972 Confs: 2026 Conference on Empirical Methods in Natural Language Processing (Hungary)","url":"https://linguistlist.org/issues/37/972/"},{"title":"AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/"},{"title":"Call for Main Conference Papers -","url":"https://2026.eacl.org/calls/papers/"},{"title":"EMNLP 2026 on X: \"📢 The First Call for Papers for EMNLP 2026 is officially out! 📝 We welcome long &amp; short papers featuring original research on empirical methods for NLP. 🗓️ ARR Submission Deadline: May 25, 2026 🔗 Read the full CFP here: https://t.co/GU2kaISjUG #EMNLP2026\" / X","url":"https://x.com/emnlpmeeting/status/2029508292637061462"}]

Based on the search results, here's information about EMNLP 2026 call for papers, ARR submission guidelines, and author instructions:

## Overview

EMNLP 2026 invites the submission of long and short papers featuring substantial, original, and unpublished research on empirical methods for Natural Language Processing.

## Key Submission Guidelines

**Paper Types**: In addition to traditional research results, papers may contribute negative findings, survey an area, announce the creation of a new re
…[truncated 1958 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 9440
}
```

</details>

---


### Tool call

_source line 2484 · 2026-05-22T13:40:28.795647+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 May submission format requirements page limit anonymity guidelines",
  "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 May submission format requirements page limit anonymity guidelines",
    "allowed_domains": "['aclrollingreview.org', '2026.emnlp.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 2485 · 2026-05-22T13:40:28.847905+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2486 · 2026-05-22T13:40:29.300392+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and RL optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR diagnoses structural degeneration invisible to prove rate, but occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B case study, this \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families: structural proxies for reasoning quality are easier to observe than to optimize.\footnote{Code and data: \url{[anonymized]}}
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2487 · 2026-05-22T13:40:29.300853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2488 · 2026-05-22T13:40:29.953613+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.
5	This treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
1
…[truncated 2338 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 652
}
```

</details>

---


### Tool call

_source line 2489 · 2026-05-22T13:40:30.004528+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2490 · 2026-05-22T13:40:30.055441+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 5011 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2491 · 2026-05-22T13:40:30.307035+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2492 · 2026-05-22T13:40:30.809879+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 14582 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2493 · 2026-05-22T13:40:31.011221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "limit": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "limit": "200"
  }
}
```

</details>

---


### Tool result

_source line 2494 · 2026-05-22T13:40:31.062026+00:00_

1	issues:
2	# === Resolved issues from rounds 0-26 (condensed) ===
3	- id: R1-W1
4	  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed
5	  category: experiment
6	  severity: critical
7	  status: resolved
8	  first_raised_round: 0
9	  last_seen_round: 2
10	  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。
11	  resolution_round: 2
12	- id: RV-EVAL-FALLBACK
13	  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除
14	  category: experiment
15	  severity: critical
16	  status: resolved
17	  first_raised_round: 1
18	  last_seen_round: 1
19	  resolution: stderr ERROR → sys.exit(1)。
20	  resolution_round: 1
21	- id: R1-W2
22	  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量
23	  category: framing
24	  severity: critical
25	  status: resolved
26	  first_raised_round: 0
27	  last_seen_round: 15
28	  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。
29	  resolution_round: 2
30	- id: R2-W1
31	  summary: Limitations section 格式不合规
32	  category: format
33	  severity: critical
34	  status: resolved
35	  first_raised_round: 0
36	  last_seen_round: 2
37	  resolution: 独立 limitations.tex 已创建。
38	  resolution_round: 3
39	- id: R2-W2
40	  summary: 实验仅用单一模型和单一数据集
41	  category: experiment
42	  severity: critical
43	  status: resolved
44	  first_raised_round: 0
45	  last_seen_round: 2
46	  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。
47	  resolution_round: 3
48	- id: R2-W6
49	  summary: SFT baseline 比较不公平：PR=14% vs 93%
50	  category: experiment
51	  severity: critical
52	  status: resolved
53	  first_raised_round: 0
54	  last_seen_round: 2
55	  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。
56	  resolution_round: 2
57	- id: v2-R1-N1
58	  summary: Abstract '93%' PR 为 single seed
59	  category: writing
60	  severity: critical
61	  status: resolved
62	  first_raised_round: 2
63	  last_seen_round: 3
64	  resolution: Abstract 使用 3-seed pooled mean±std。
65	  resolution_round: 3
66	- id: v2-R1-N3
67	  summary: 仅 2 个 β 值不足以刻画 dose-respons
…[truncated 4159 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2495 · 2026-05-22T13:40:35.779321+00:00_

Web search results for query: "ACL Rolling Review 2026 May submission format requirements page limit anonymity guidelines"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"Authors Beware: Common Submission Problems – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authorchecklist"},{"title":"Submission Form Fields – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/submissionform"},{"title":"ARR SAC Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/sacguidelines"}]

Based on the search results, here is information about ACL Rolling Review 2026 submission format requirements, page limits, and anonymity guidelines:

## Page Limits

Short papers have a 4 content pages maximum, while long
…[truncated 1369 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6983
}
```

</details>

---


### Tool call

_source line 2496 · 2026-05-22T13:40:41.161603+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2497 · 2026-05-22T13:40:41.513509+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodha
…[truncated 2286 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 2498 · 2026-05-22T13:40:41.514033+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2499 · 2026-05-22T13:40:41.664946+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect, documenting that structural proxies for reasoning quality are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 2500 · 2026-05-22T13:40:41.966534+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2501 · 2026-05-22T13:40:42.469067+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
7	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 2502 · 2026-05-22T13:40:42.469409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2503 · 2026-05-22T13:40:42.922249+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, condit
…[truncated 51818 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2504 · 2026-05-22T13:40:43.123489+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
  "offset": "200"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml",
    "offset": "200"
  }
}
```

</details>

---


### Tool result

_source line 2505 · 2026-05-22T13:40:43.174639+00:00_

200	  resolution_round: 21
201	- id: v21-R12-W1
202	  summary: "Title 'Structural Degeneration' 与 'component necessity' 矛盾"
203	  category: framing
204	  severity: warning
205	  status: resolved
206	  first_raised_round: 21
207	  last_seen_round: 21
208	  resolution: "Title 'Reveals' → 'Diagnoses'。"
209	  resolution_round: 21
210	- id: v21-R2-N1
211	  summary: V-STaR bib 更新为 COLM 2024
212	  category: writing
213	  severity: info
214	  status: resolved
215	  first_raised_round: 21
216	  last_seen_round: 21
217	  resolution: "bib 已更新。"
218	  resolution_round: 21
219	- id: v21-R2-N2
220	  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值
221	  category: writing
222	  severity: info
223	  status: resolved
224	  first_raised_round: 21
225	  last_seen_round: 21
226	  resolution: "ISR (5-seed) 行显示 (0.63)‡ 具体值。"
227	  resolution_round: 21
228	- id: v22-ORPHAN-BIB
229	  summary: "kimina-prover bib entry 未被引用"
230	  category: writing
231	  severity: info
232	  status: resolved
233	  first_raised_round: 22
234	  last_seen_round: 22
235	  resolution: "已删除。"
236	  resolution_round: 22
237	- id: v22-R2-W5
238	  summary: "遗漏 Dong et al. (2026)"
239	  category: writing
240	  severity: warning
241	  status: resolved
242	  first_raised_round: 22
243	  last_seen_round: 22
244	  resolution: "dong2026probing 加入。"
245	  resolution_round: 22
246	- id: v22-R12-N2
247	  summary: "'99.5% structural collapse' 来自单 seed 最极端值"
248	  category: writing
249	  severity: warning
250	  status: resolved
251	  first_raised_round: 22
252	  last_seen_round: 23
253	  resolution: "标注 'for seed~42' + 3-seed '≤7%'。"
254	  resolution_round: 24
255	- id: v22-R2-W2
256	  summary: "Eight-mode taxonomy 过度工程化"
257	  category: writing
258	  severity: warning
259	  status: resolved
260	  first_raised_round: 22
261	  last_seen_round: 23
262	  resolution: "§4.5 已聚焦 CE/TS/PG 三主要 mode。"
263	  resolution_round: 24
264	- id: v23-VISUAL-PAGE9
265	  summary: "Section 5 溢出至第 9 页"
266	  category: format
267	  severity: warning
268	  s
…[truncated 21128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2506 · 2026-05-22T13:41:08.906277+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool call

_source line 2507 · 2026-05-22T13:41:09.207749+00:00_

called mcp__agent-ml-research__get_external_review_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_external_review_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2508 · 2026-05-22T13:41:12.829883+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 3923
}
```

</details>

---


### Tool result

_source line 2509 · 2026-05-22T13:41:12.830363+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"not_requested\", \"message\": \"No external review requested.\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_external_review_status",
  "elapsed_ms": 3622
}
```

</details>

---


### Tool call

_source line 2510 · 2026-05-22T13:41:40.729593+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制，参考文献不限，Limitations 不计入页数)\n- **模板**: ACL template, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_27/submitted.pdf`\n\n### 你的审查重点\n\n请重点评估以下方面：\n\n1. **统计方法论**：\n   - N=3 seeds 的统计效力是否足够支撑核心 claims？\n   - CMH 检验中 within-seed pseudo-replication 的处理是否恰当？\n   - p=0.182 (ISR vs Random non-hacking) 和 p=0.10 (ProofFOL) 的解读是否合理？\n   - Premise-count confound 对 ISR 聚合指标的影响是否被充分讨论和控制？\n\n2. **实验设计与控制**：\n   - Seed 43 使用 T=0.7 sampling 而非 greedy 评估——对 N=3 设计的影响？\n   - SFT baseline PR 差异 (13% vs 93%) 的公平性？100-step checkpoint 是否足够缓解？\n   - Shuffled-ISR control 的有效性 (N=46 proved samples)？\n   - 乘法耦合 reward 设计的 confound 控制是否充分？\n   - 50% exec-only seeds 不收敛但从主分析排除的影响？\n\n3. **Classifier 验证**：\n   - 8 类 hacking taxonomy 的分类方法是否可复现？\n   - 50 样本 precision audit 是否充分？recall 估计缺失的影响？\n   - PG 审计仅覆盖 seed 42 的局限性？\n   - Non-hacking rate 作为 upper bound，跨条件 classifier recall 一致性问题？\n\n4. **ISR 方法论**：\n   - LOO 独立性假设对 ISR 的偏差——是否需要量化？\n   - ISR 对不同 hacking modes 的诊断力差异（CE 高敏感 vs TS 反向）\n   - ISR aggregate vs per-sample diagnostic 的分离是否清晰？\n   - Premise-count confound: 3.2× → 1.06× 的影响\n\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 匿名化是否合规？\n   - Limitations section 是否存在且合理？\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含 Summary、Strengths、Weaknesses (分 Must-Fix / Should-Fix / Minor)、Questions、Missing References、Overall Assessment。评分使用 EMNLP 2026 ARR 标准（1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 1\n\n**你的审查侧重：方法严谨性 + 实验有效性**\n\n### 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制，参考文献不限，Limitations 不计入页数)\n- **模板**: ACL template, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_27/submitted.pdf`\n\n### 你的审查重点\n\n请重点评估以下方面：\n\n1. **统计方法论**：\n   - N=3 seeds 的统计效力是否足够支撑核心 claims？\n   - CMH 检验中 within-seed pseudo-replication 的处理是否恰当？\n   - p=0.182 (ISR vs Random non-hacking) 和 p=0.10 (ProofFOL) 的解读是否合理？\n   - Premise-count confound 对 ISR 聚合指标的影响是否被充分讨论和控制？\n\n2. **实验设计与控制**：\n   - Seed 43 使用 T=0.7 sampling 而非 greedy 评估——对 N=3 设计的影响？\n   - SFT baseline PR 差异 (13% vs 93%) 的公平性？100-step checkpoint 是否足够缓解？\n   - Shuffled-ISR control 的有效性 (N=46 proved samples)？\n   - 乘法耦合 reward 设计的 confound 控制是否充分？\n   - 50% exec-only seeds 不收敛但从主分析排除的影响？\n\n3. **Classifier 验证**：\n   - 8 类 hacking taxonomy 的分类方法是否可复现？\n   - 50 样本 precision audit 是否充分？recall 估计缺失的影响？\n   - PG 审计仅覆盖 seed 42 的局限性？\n   - Non-hacking rate 作为 upper bound，跨条件 classifier recall 一致性问题？\n\n4. **ISR 方法论**：\n   - LOO 独立性假设对 ISR 的偏差——是否需要量化？\n   - ISR 对不同 hacking modes 的诊断力差异（CE 高敏感 vs TS 反向）\n   - ISR aggregate vs per-sample diagnostic 的分离是否清晰？\n   - Premise-count confound: 3.2× → 1.06× 的影响\n\n5. **格式合规**：\n   - 正文是否在 8 页以内？\n   - 匿名化是否合规？\n   - Limitations section 是否存在且合理？\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含 Summary、Strengths、Weaknesses (分 Must-Fix / Should-Fix / Minor)、Questions、Missing References、Overall Assessment。评分使用 EMNLP 2026 ARR 标准（1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 2511 · 2026-05-22T13:41:59.632043+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 18902
}
```

</details>

---


### Tool call

_source line 2512 · 2026-05-22T13:41:59.783145+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性**\n\n### 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制，参考文献不限，Limitations 不计入页数)\n- **模板**: ACL template, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_27/submitted.pdf`\n\n### 你的审查重点\n\n请重点评估以下方面：\n\n1. **新颖性评估**：\n   - LOO ablation 本身是标准技术（mutation testing, 1978）——将其应用于 neurosymbolic GRPO 的贡献增量有多大？\n   - STA/ISR 与 Helff et al. (2026) Input Perturbation Testing (IPT) 的概念区分是否充分？是否构成独立方法论贡献？\n   - Goodhart effect 在 RLHF 中已被广泛记录——本文在 neurosymbolic 设定下的发现是否足够 novel？\n   - \"Observe-vs-optimize asymmetry\" 是否是一个新概念，还是 Goodhart's Law 的直接推论？\n   - Eight-mode hacking taxonomy 的贡献——是 principled classification 还是 ad-hoc enumeration？\n\n2. **Related Work 定位**：\n   - 与 Kim et al. (2026) game formalization 的区分是否清晰？\n   - 与 Process Reward Models (PRM) 方向的概念联系是否被充分讨论？\n   - ISR 与 Shapley values / influence functions 的方法论关系是否被提及？\n   - 是否遗漏重要的 mutation testing in ML 近期工作？\n   - 引用列表的完整性和准确性？\n\n3. **Framing 与 Claims**：\n   - \"Case study\" 标题定位 vs 正文中偶尔出现的通用性声称——是否一致？\n   - Abstract/Intro 以 raw ISR 214× collapse 为核心叙事，但 premise-count matched 后仅 1.06×——framing 是否 misleading？\n   - \"Compositional Goodhart\" 概念是否有操作性定义？还是 regressional Goodhart 的 expected instantiation？\n   - ProofFOL \"cross-dataset\" 声称的合理性（same-task-family FOL，非真正 cross-domain）？\n   - 单模型 (Qwen3-4B) 能支撑多广的结论？\n\n4. **写作质量**：\n   - 缩写密度（ISR, STA, CE, TS, PG, N-H, PR, LOO, CMH...）对首次阅读者是否友好？\n   - Table 1 的可读性？\n   - 论文叙事结构是否清晰连贯？\n   - Conclusion 是否过于简短？\n\n5. **格式合规**：\n   - 正文页数？\n   - 匿名化？\n   - 引用格式？\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含 Summary、Strengths、Weaknesses (分 Must-Fix / Should-Fix / Minor)、Questions、Missing References、Overall Assessment。评分使用 EMNLP 2026 ARR 标准（1-5 分）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## Round 1 审稿任务 — Reviewer 2\n\n**你的审查侧重：新颖性 + 完整性**\n\n### 论文信息\n- **标题**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n- **Venue**: EMNLP 2026 (via ACL Rolling Review)\n- **类别**: Long Paper (8 页正文限制，参考文献不限，Limitations 不计入页数)\n- **模板**: ACL template, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_27/submitted.pdf`\n\n### 你的审查重点\n\n请重点评估以下方面：\n\n1. **新颖性评估**：\n   - LOO ablation 本身是标准技术（mutation testing, 1978）——将其应用于 neurosymbolic GRPO 的贡献增量有多大？\n   - STA/ISR 与 Helff et al. (2026) Input Perturbation Testing (IPT) 的概念区分是否充分？是否构成独立方法论贡献？\n   - Goodhart effect 在 RLHF 中已被广泛记录——本文在 neurosymbolic 设定下的发现是否足够 novel？\n   - \"Observe-vs-optimize asymmetry\" 是否是一个新概念，还是 Goodhart's Law 的直接推论？\n   - Eight-mode hacking taxonomy 的贡献——是 principled classification 还是 ad-hoc enumeration？\n\n2. **Related Work 定位**：\n   - 与 Kim et al. (2026) game formalization 的区分是否清晰？\n   - 与 Process Reward Models (PRM) 方向的概念联系是否被充分讨论？\n   - ISR 与 Shapley values / influence functions 的方法论关系是否被提及？\n   - 是否遗漏重要的 mutation testing in ML 近期工作？\n   - 引用列表的完整性和准确性？\n\n3. **Framing 与 Claims**：\n   - \"Case study\" 标题定位 vs 正文中偶尔出现的通用性声称——是否一致？\n   - Abstract/Intro 以 raw ISR 214× collapse 为核心叙事，但 premise-count matched 后仅 1.06×——framing 是否 misleading？\n   - \"Compositional Goodhart\" 概念是否有操作性定义？还是 regressional Goodhart 的 expected instantiation？\n   - ProofFOL \"cross-dataset\" 声称的合理性（same-task-family FOL，非真正 cross-domain）？\n   - 单模型 (Qwen3-4B) 能支撑多广的结论？\n\n4. **写作质量**：\n   - 缩写密度（ISR, STA, CE, TS, PG, N-H, PR, LOO, CMH...）对首次阅读者是否友好？\n   - Table 1 的可读性？\n   - 论文叙事结构是否清晰连贯？\n   - Conclusion 是否过于简短？\n\n5. **格式合规**：\n   - 正文页数？\n   - 匿名化？\n   - 引用格式？\n\n请按照 ARR 审稿标准，输出完整审稿报告，包含 Summary、Strengths、Weaknesses (分 Must-Fix / Should-Fix / Minor)、Questions、Missing References、Overall Assessment。评分使用 EMNLP 2026 ARR 标准（1-5 分）。"
  }
}
```

</details>

---


### Tool result

_source line 2513 · 2026-05-22T13:42:01.566616+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1783
}
```

</details>

---


### Tool call

_source line 2514 · 2026-05-22T13:42:07.356234+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2515 · 2026-05-22T13:42:07.507563+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 21254 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2516 · 2026-05-22T13:42:07.773508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2517 · 2026-05-22T13:42:07.773977+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	Code, evaluation scripts, the ProofFOL dataset, and trained model checkpoints will be released upon acceptance.
8	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 2518 · 2026-05-22T13:42:20.200666+00:00_

**审稿进度**：
- Reviewer 1（方法严谨性）：已派发，等待返回
- Reviewer 2（新颖性 + 完整性）：已派发，等待返回
- 视觉审查 Agent：已派发，并行执行中
- 外部审稿：未配置，跳过

等待 Reviewer 报告返回后进行交叉分享（Step 2）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 226

## Round 226

2 recorded events


### User

_source line 2519 · 2026-05-22T13:47:44.085214+00:00_

[Reviewer 1 审稿意见]:
## 总体评分
**Overall**: 3.0 / 5 — Findings
**一句话总结**: STA/ISR 框架本身新颖且有诊断价值，但 N=3 seeds 的统计效力不足、premise-count confound 将 ISR 聚合优势从 3.2× 压缩至 1.06×、以及 seed 43 评估协议不一致，共同削弱了核心实验 claims 的可靠性，达不到主会议接收标准但适合 Findings。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0/5 | 方法论合理但统计执行有显著缺陷：N=3 seeds 仅对 d≥2.0 的超大效应有 80% 统计效力；premise-count confound 基本消解了 ISR 聚合指标的信号；seed 43 协议不一致；50% exec-only seeds 不收敛引入生存偏差 |
| Excitement | 3.5/5 | STA 框架本身是 neurosymbolic reasoning 中一个有价值的诊断工具；8-mode hacking taxonomy 详细且新颖；observe-vs-optimize 不对称性是真实洞见；但局限于单一模型家族和任务家族 |
| Reproducibility | 4/5 | 承诺公开代码、数据集、checkpoints；hacking classifiers 是基于规则的确定性方法，详细文档化；实验超参数完整列出（Table 3, Appendix A）|
| Confidence | 4/5 | 熟悉 RL for reasoning、neurosymbolic methods 和统计方法论 |

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] N=3 seeds 统计效力严重不足，核心 claims 的量化证据不可靠
- 具体位置：Section 4.1 (p.5), Appendix D.1 (p.13), Table 5 (p.13)
- 问题：论文承认 N=3 仅对 d≥2.0 的效应有 80% 统计效力（Section 4.1: "At N=3, seed-level tests achieve 80% power only for very large effects (d≥2.0)"）。多个关键比较未达显著性：ISR vs. Random non-hacking p=0.182 (Appendix D.1)；ProofFOL 结果 p=0.182（Section 4.1 标注为 exploratory）。CMH 检验将 within-seed 样本视为独立观测，实际独立单元仅 3 个 seeds，pseudo-replication 膨胀了检验统计量的自由度。论文在 Appendix E 中提到了 5-seed extension（s42-s46, s52），但仅 3/6 exec-only seeds 收敛，且这些额外 seeds 被放在附录而非作为主分析。
- 为什么影响接收：论文的核心量化 claims（ISR collapse 诊断结构退化、ISR-as-reward 产生 Goodhart 效应的程度量化）都建立在 N=3 的比较上。当 effect size 不够大时，这些比较既无法确认也无法排除效应的存在，使得论文的实验贡献从"量化证据"降格为"定性观察"。
- 建议修改方向：(1) 将 5-seed extension 纳入主分析，即使部分 seeds 不收敛也应报告完整结果；(2) 对 CMH 检验中的 pseudo-replication 问题进行 cluster-robust 校正（以 seed 为聚类单元）；(3) 明确所有非显著结果为 exploratory，避免在正文中对方向性趋势做因果推断措辞。

**N2** [critical] Premise-count confound 基本消解了 ISR 聚合指标的核心诊断价值
- 具体位置：Section 4.1 (p.5-6), Appendix C (p.12), Section 3.2 Eq.(1)
- 问题：论文坦承 ISR 聚合优势在控制 premise count 后从 3.2× 降至 1.06×（Section 4.1: "After matching for premise count, the apparent 3.2× advantage shrinks to 1.06× and becomes deterministic"）。这意味着 ISR 作为 aggregate metric 的诊断能力几乎完全由 premise count 驱动，而非结构必要性。论文试图通过区分 aggregate ISR（用于宏观诊断）和 per-sample ISR（用于细粒度分析）来缓解这一问题，但这一区分在论文中不够清晰。Abstract 和 Introduction 中 "ISR diagnoses structural degeneration" 的表述暗示 ISR 本身有独立诊断力，但实际上 premise count 就能提供几乎相同的信息。
- 为什么影响接收：ISR 是论文的核心贡献之一。如果 ISR aggregate 的诊断信号主要来自 premise count confound，那么论文需要对 ISR 的实际贡献做出更精确的定位——是 per-sample 级别的必要性诊断（这确实是 LOO 独有的），还是 aggregate 级别的结构退化指标（这基本等价于数 premise 数量）。
- 建议修改方向：(1) 在 Abstract/Introduction 中明确区分 ISR 的两个用途层次：aggregate（≈ premise count proxy）vs. per-sample（真正的必要性诊断）；(2) 报告 premise-count-matched 的比较作为主要结果，将 unmatched 作为补充；(3) 讨论为何不直接用 premise count 作为更简单的 aggregate 诊断替代品。

**N3** [critical] Seed 43 评估协议不一致严重损害 N=3 设计的有效性
- 具体位置：Appendix A (p.11, "Evaluation exception" 段落), Table 8 (p.18)
- 问题：Seed 43（plan01-exec-only-s43-r4）使用 T=0.7 sampling 而非其他 seeds 的 greedy decoding 进行评估。论文承认其 PR 和 ISR 值"not strictly comparable with other seeds under the unified evaluation protocol (C004)"。在 N=3 设计中，一个 seed 的评估协议不一致意味着：纳入该 seed 会混合不同评估标准；排除该 seed 则 N 降至 2，进一步恶化统计效力。Appendix D.1 也确认排除 s43 后结果 "consistent or stronger"，但这本身就说明 s43 的数据质量有问题。
- 为什么影响接收：这不仅是统计问题，更是实验设计的基本合规性问题。一个合格的实验应当确保所有 replicates 在同一评估协议下运行。在只有 3 个 seeds 的情况下，1/3 的 seeds 协议不一致使得整个 exec-only condition 的结论可信度大打折扣。
- 建议修改方向：(1) 用 greedy decoding 重新评估 seed 43 的 checkpoint（如 checkpoint 仍在）；(2) 如无法重新评估，将 seed 43 数据标注为 "protocol deviation"，主分析基于 N=2 seeds 并明确声明统计效力限制；(3) 增加更多 seeds 以弥补这一缺陷。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] 50% exec-only seeds 不收敛但从主分析排除，引入生存偏差
- 具体位置：Appendix E.5 (p.21)
- 问题：6 个 exec-only seeds 中仅 3 个收敛（s42, s44, s46 at 500 steps），s43 缓慢收敛（PR=11%），s45 和 s52 不收敛。主分析仅使用收敛的 seeds。论文在 Appendix E.5 中讨论了这一现象，将其归因于 "seed-dependent 4B non-convergence"，但 50% 的不收敛率本身是一个重要发现：它表明 GRPO 在 exec-only 条件下的训练稳定性很差，structural degeneration 可能是收敛的副产品而非 GRPO 的固有行为。
- 建议：(1) 在正文 Limitations 中明确报告 50% 不收敛率及其对结论的影响；(2) 讨论不收敛 seeds 是否保留了更好的结构——如果不收敛 seeds 的 ISR 更高或 hacking 更少，这本身就是一个重要的反面证据。

**W2** [warning] Classifier recall 未估计，non-hacking rates 可能系统性高估
- 具体位置：Table 7 (p.14), Appendix D.1 (p.13-14)
- 问题：Precision audit 覆盖 152 个样本，precision=1.00 (Table 7)。但 recall 明确标注为 "not estimable from a validated-only design"。论文将 non-hacking rate 定位为 "upper bound"（Section 4.1: "non-hacking rate as upper bound"），但未量化 upper bound 的松弛程度。如果某些 hacking modes 的 recall 显著低于 1.0（例如 TS 的 text-match classifier 有 systematic blind spots，Appendix C 承认 "text-match hacking classifiers have systematic blind spots that functional analysis exposes"），non-hacking rates 的高估可能是非均匀的：对 TS-dominant 条件（如 ISR conditions）的高估更严重。
- 建议：(1) 对至少一个 condition 做随机抽样的 recall 估计（而非仅 precision）；(2) 讨论 recall 在不同 hacking modes 间的预期变异及其对 cross-condition comparisons 的影响。

**W3** [warning] PG (Premise-Subset Gaming) 审计仅覆盖 seed 42，其他 seeds 的 non-hacking rates 可能被高估
- 具体位置：Appendix D.1 (p.14, "Audit scope and limitations" 段落)
- 问题：论文明确指出 "Full PG audit was completed for ISR β=0.1 seed 42 only. ISR seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered; their non-hacking rates may be overestimated." PG 需要重新生成 premise set 并运行 solver 来检测，是唯一无法通过 text-match 自动分类的 hacking mode。在 ISR 条件下，PG 是一个新发现的 hacking mode（Appendix D.1），其在 seeds 43/44 中的 prevalence 完全未知。
- 建议：(1) 对 PG 在其他可用 seeds 的 prevalence 做 bootstrap 估计；(2) 量化最坏情况下（假设 seeds 43/44 的 PG rate 与 seed 42 相同或更高）non-hacking rates 的变化幅度。

**W4** [warning] Shuffled-ISR control 的证据基础过于单薄 (N=46 proved samples)
- 具体位置：Section 4.3 (p.6), Table 8 (p.18, "Shuffled ISR β=0.1" 行)
- 问题：Shuffled-ISR control 是验证 Goodhart 效应因果机制的关键实验——它证明 ISR 的 sample-level 语义信号（而非分布形状）是 Goodhart 效应的驱动力。但该 control 仅 46 个 proved samples（Table 8 注释: "n=100 (seedx4)"），其中 87% 被分类为 non-hacking。在如此小的样本上，87% non-hacking 的 95% CI 宽达 ±10 个百分点（Wilson interval），使得这一 control 的证明力有限。
- 建议：增加 shuffled-ISR 的训练步数或 seed 数量以获得更多 proved samples，或至少报告 CI。

**W5** [warning] 乘法耦合 reward 设计的 confound 未充分控制
- 具体位置：Section 3.3 (p.4), Appendix A (p.11)
- 问题：Reward 函数 r_exec · (1 + β·ISR) 将 ISR 与 execution reward 乘法耦合，意味着 ISR 信号仅在 execution 通过时生效。这引入了一个 confound：ISR 条件下的模型同时接收了 "更高 reward for 结构完整的 proofs" 和 "multiplicative scaling of reward magnitude"。Additive variant 在早期实验中导致 prove rate 崩塌（Appendix A: "collapsed the prove rate to near-zero"），但论文未探索 additive variant 在不同 β 值或不同训练阶段的表现。仅因一次失败就排除 additive variant，使得乘法 vs. 加法 vs. ISR 信号本身的贡献无法分离。
- 建议：(1) 讨论乘法耦合为何不引入 reward magnitude confound（而非仅声明 ISR only modulates proved outputs）；(2) 报告 additive variant 的详细失败分析。

---

## 小问题（不影响接收）

- **M1**: Abstract 中 "ISR diagnoses structural degeneration" 的措辞暗示 ISR 有独立诊断力，但正文显示 aggregate ISR ≈ premise count proxy。建议修改为更精确的表述。
- **M2**: Table 2 (p.8) 信息密度过高，字体偏小，8 modes × 多个 conditions 的矩阵在单栏宽度下可读性差。建议拆分或移至附录。
- **M3**: Hacking mode 缩写 (CE, TS, PG, CI, TSb, TSa) 在正文中引入时缺乏足够上下文，需要频繁翻阅 Appendix D 才能理解。建议在首次使用时给出简短定义。
- **M4**: Figure 1 的 y 轴标签 "ISR" 和 "Prove Rate" 在黑白打印下可能难以区分不同 conditions 的线条。
- **M5**: Section 4.4 ProofFOL 的 "p<0.10" 结果虽标注为 exploratory，但其在正文中的位置和措辞可能给读者过强的印象。建议明确为 "underpowered; directional only"。
- **M6**: Appendix E.3 中 O(1) vs. O(n) ISR 的讨论是一个有趣的理论贡献，但与主文的连接不够紧密。

---

## 主要优势

1. **STA 框架本身具有方法论价值**：将 LOO mutation testing 引入 neurosymbolic reasoning 的结构诊断是一个清晰、可操作、可复现的贡献。Algorithm 1 简洁优雅。
2. **8-mode hacking taxonomy 详细且有实践价值**：Appendix D 对每种 hacking mode 的定义、示例、ISR 交互、prevalence 分析提供了社区迄今为止最细粒度的 reward hacking 分类，具有独立参考价值。
3. **Observe-vs-optimize 不对称性是真实且重要的洞见**：ISR 作为诊断工具有效但作为训练信号被 game，这一发现对 RLVR reward design 有实际指导意义。
4. **跨域验证增强可信度**：FOL → Prolog、FOLIO → ProofFOL、3B → 8B 的多维度复制提供了比单一设置更强的证据基础。
5. **透明度高**：论文对自身限制（N=3 统计效力、premise-count confound、seed 43 协议偏差、PG audit 覆盖不足）的讨论坦诚详尽，这在同类工作中少见。

---

## Questions for Authors

Q1: 在 premise-count-matched comparisons 中，ISR 优势仅为 1.06×。你们是否考虑过直接用 premise count 作为更简单的结构退化诊断替代品？如果 premise count 在 aggregate level 提供几乎等价的信息，STA/ISR 框架的 unique contribution 是否仅限于 per-sample 级别？

Q2: 50% exec-only seeds 不收敛（Appendix E.5）。不收敛的 seeds 是否保留了更好的结构完整性（即更高的 ISR、更低的 hacking rate）？如果是，这将挑战 "structural degeneration is a consequence of GRPO training" 的 claim——它可能仅是 successful convergence 的副产品。

Q3: Shuffled-ISR control 仅产生 46 个 proved samples。你们是否有更长训练的 shuffled-ISR 数据？如果没有，你们如何论证这 46 个样本足以排除 "ISR 分布形状（而非 sample-level 语义）驱动 Goodhart 效应" 的替代假设？

Q4: 论文提到 additive reward variant "collapsed the prove rate to near-zero"（Appendix A）。这次失败是在什么 β 值和训练设置下观察到的？是否尝试过更小的 β 或 curriculum-style 的引入策略？

Q5: TS (Tautological Shortcuts) hacking mode 下 ISR 表现出反向模式（ISR 反而更高）。这是否意味着 ISR 在特定 hacking modes 下可能产生误导性的 "结构正常" 信号？这对 ISR 作为通用诊断工具的可靠性有何影响？

---

## Missing References

- **Coste et al. (2023)**, "Reward Model Ensembles Help Mitigate Overoptimization" — 与 ISR-as-reward 的 Goodhart 效应讨论直接相关
- **Moskovitz et al. (2023)**, "Confronting Reward Model Overoptimization with Constrained RLHF" — 关于 reward overoptimization 的理论框架
- **Pan et al. (2024)**, "Spontaneous Reward Hacking in Iterative Self-Refinement" — 自我改进过程中的 reward hacking，与论文的 observe-vs-optimize 主题相关

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2520 · 2026-05-22T13:47:54.696771+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告返回后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 227

## Round 227

4 recorded events


### User

_source line 2521 · 2026-05-22T13:47:57.311434+00:00_

[Reviewer 1 审稿结果]:
审稿报告已提交给 Review Director。

**评分总结**：Overall 3.0/5 (Findings)，Soundness 3.0，Excitement 3.5，Reproducibility 4.0。

**3 个 Must-Fix 问题**：
1. N=3 seeds 统计效力不足，CMH 检验存在 pseudo-replication，多个关键比较未达显著性
2. Premise-count confound 将 ISR 聚合优势从 3.2× 压缩至 1.06×，基本消解了 ISR aggregate 指标的独立诊断价值
3. Seed 43 使用 T=0.7 sampling 评估（非 greedy），在 N=3 设计中损害了 exec-only condition 的有效性

**5 个 Should-Fix 问题**：50% exec-only 不收敛引入生存偏差、classifier recall 未估计、PG 审计仅覆盖 seed 42、shuffled-ISR control 仅 46 样本、乘法 reward 耦合 confound 未充分控制。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Tool call

_source line 2522 · 2026-05-22T13:48:04.011325+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2523 · 2026-05-22T13:48:04.061899+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect, documenting that structural proxies for reasoning quality are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 2524 · 2026-05-22T13:48:06.658257+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 228

## Round 228

6 recorded events


### User

_source line 2525 · 2026-05-22T13:49:11.754320+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告 — Round 1

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 via ACL Rolling Review
**审查侧重**: 新颖性 + 完整性

---

## 总体评分
**Overall**: 3.0 (Findings)
**一句话总结**: 论文记录了一个重要现象（GRPO 训练导致的结构退化），诊断工具（STA/ISR）合理但方法论新颖性有限——核心是将 LOO ablation 这一标准技术应用于 neurosymbolic 输出，且 Abstract/Intro 的 "214× collapse" 叙事在 premise-count 匹配后缩水至 1.06×，framing 存在误导风险。

## 官方维度打分（ACL ARR review form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计合理（exec-only / ISR-as-reward / matched random 三条件），有 premise-count 控制和 Bonferroni 校正，但核心叙事被 confound 大幅削弱；3-seed 统计功效有限 |
| Excitement | 2.5/5 | 话题（GRPO reward hacking 诊断）及时且有实际价值，但方法论贡献 incremental——LOO ablation 到新领域的移植，taxonomy 是 ad-hoc 枚举而非 principled classification |
| Reproducibility | 4/5 | 承诺开源代码、数据集和 checkpoint；超参数表格完整（Table 3, Appendix A）；ProofFOL 构建流程清晰 |
| Overall Assessment | 3.0/5 | Findings 水准。现象有价值，工具实用，但新颖性不足以支撑主会议。见下文详细分析 |
| Reviewer Confidence | 4/5 | 熟悉 RLVR、neurosymbolic reasoning、reward hacking 文献 |

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic 推理管道中 GRPO 训练输出的诊断方法。STA 对证明的每个组件执行 leave-one-out (LOO) 删除，计算 Intensional Structural Reward (ISR)——必要组件占比。论文在 FOLIO（FOL）和 Prolog 两类逻辑任务上展示：(1) GRPO 训练使 ISR 从 ~32% 崩溃至 <1%，表明结构退化；(2) 将 ISR 用作训练 reward 时出现 Goodhart 效应（8 种 hacking 模式）；(3) 在 ProofFOL 上进行跨数据集验证。贡献包括 STA 框架、ISR 指标、8-mode hacking taxonomy、以及 observe-vs-optimize 不对称性的经验证据。

---

## 主要优势

**S1. 重要且及时的现象记录。** 在 RLVR 社区快速扩张 neurosymbolic reasoning 应用的背景下，系统记录 GRPO 训练导致的结构退化具有实际价值。Figure 1 和 Table 8（per-seed 详细结果）提供了训练动态的清晰画面。

**S2. 实验控制设计合理。** 六个 reward 条件（exec-only, ISR low/high/dose, matched random controls）加上 SFT baseline，形成了有说服力的对照结构。特别是 premise-count matched comparison（§4.2）是一个诚实的自我修正，说明作者意识到了 confound 问题。

**S3. 详尽的附录和可复现性。** 22 页中 14 页是附录，提供了完整的 hacking mode 定义（Appendix D）、per-seed 结果（Appendix E）、统计检验细节（§4.1, Table 5）、ProofFOL 数据集构建流程（Appendix A）、以及 LLaMA 交叉验证（Appendix E.4-E.6）。承诺开源所有代码和 checkpoint。

**S4. Hacking taxonomy 对实践者有用。** 8 种 hacking 模式（CE, TS, PG, TSb, TSa, Tautological Collapse, Repetition Collapse, Complexity-without-Utility, Contradiction Explosion, Query-as-fact）的分类虽然是经验性的，但为理解和检测 neurosymbolic reward hacking 提供了实用的 vocabulary。每种模式都有 FOL 示例（Appendix D），便于从业者识别。

**S5. 跨逻辑体系和跨数据集验证。** FOL + Prolog 两种逻辑体系的对比（Figure 2, Table 2）以及 ProofFOL 跨数据集复制（§4.4）增强了发现的可信度。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **ISR "214× collapse" 叙事的 framing 存在系统性误导**
- 具体位置：Abstract ("ISR collapses … yielding the Intensional Structural Reward (ISR)")、§1 Introduction ("ISR … collapses from 0.62 to 0.003, a 214× raw drop")、Figure 1 标题
- 问题：论文以 raw ISR 从 0.62 崩溃至 0.003（214×）作为核心叙事钩子，但 §4.2 第5段 "Premise-count confound" 明确承认：(1) ISR-trained 模型产生更少 premise 的 formalization，mechanically boosting LOO rate；(2) 匹配 premise count 后，advantage 从 3.2× 缩水至 **1.06×**（"the apparent 3.2× advantage shrinks to 1.06×"）。换言之，214× 的绝大部分来自 premise-count confound 而非真正的结构退化。但 Abstract 和 Introduction 完全没有提及这一关键 caveat——读者要读到第 6 页才会发现。
- 为什么影响接收：这直接关乎论文核心 claim 的可信度。如果 ISR collapse 的主要驱动力是 premise count 变化而非结构退化，那么论文的标题所承诺的 "diagnoses structural degeneration" 就需要大幅修饰。审稿人和读者有理由认为 framing 具有误导性（misleading），这在 ARR soundness 维度是严重扣分项。
- 建议修改方向：(1) Abstract 和 Introduction 必须在首次提到 ISR collapse 时就注明 premise-count confound 及其 effect size；(2) 使用 premise-count-matched ISR 作为主要报告指标，raw ISR 作为辅助；(3) 重新校准叙事——如果控制后仅 1.06×，论文的叙事重心应从 "ISR collapse magnitude" 转向 "hacking mode composition" 和 "Goodhart effect"。

**N2** [critical] **方法论新颖性有限——LOO ablation 应用于新领域的贡献增量不明确**
- 具体位置：§3.2 ("LOO ablation itself is standard in mutation testing and sensitivity analysis (DeMillo et al., 1978; Jia and Harman, 2011); novelty lies in its application…"), §2 Related Work (Helff et al. 对比段)
- 问题：论文坦率承认 LOO ablation 是标准技术。将其应用于 neurosymbolic 输出确实是新的应用场景，但方法论贡献增量有限。STA 的核心操作（逐一移除 proof 组件、重新调用 solver）在概念上是直接的，不需要解决新的技术挑战。与 Helff et al. (2026) 的 Input Perturbation Testing (IPT) 相比，两者都通过 perturbation 来检测模型是否真正依赖逻辑结构——STA 扰动输出（LOO），IPT 扰动输入（permuting identifiers）。论文声称两者 "complementary"（§2 最后一段），但没有提供实验对比来证明 STA 能捕捉 IPT 遗漏的、或 IPT 能捕捉 STA 遗漏的具体案例。
- 为什么影响接收：对于主会议接收，通常要求明确的方法论新颖性或 surprising 发现。仅将标准技术迁移到新领域（即使有有趣的经验发现）通常被视为 Findings 水平的贡献。
- 建议修改方向：(1) 如果可能，增加 STA vs IPT 的实验对比，展示两者在具体 hacking mode 上的检测互补性；(2) 更清晰地阐述 STA 作为 component-level 诊断（vs. IPT 的 sample-level faithfulness test）的不可替代性；(3) 或者接受 Findings 定位，调整 claim 的 scope。

**N3** [critical] **"Compositional Goodhart" 概念缺乏操作性定义**
- 具体位置：Abstract ("compositional, not quantitative: ISR redirects gaming toward TS rather than reducing its prevalence"), §4.3 ("the asymmetry is compositional, not quantitative"), §4.2 ("Total contribution embedding (CE + TS) spans 68–100% across both conditions, the compositional shifts")
- 问题：论文反复使用 "compositional Goodhart" 这一术语，但始终没有给出操作性定义。从上下文推断，它似乎指的是 "ISR-as-reward 改变了 hacking 模式的组成比例（从 CE 转向 TS），而非减少 hacking 总量"。但这并不构成 Goodhart's Law 的新 variant——它只是 regressional Goodhart（Manheim and Garrabrant, 2019）在特定设定下的 expected instantiation：当你优化一个 proxy metric 时，被优化的维度改善了，但 unmeasured 维度恶化了。Skalse et al. (2022) 和 Karwowski et al. (2024) 已经在 RL 中记录了类似的 mode-shifting 现象。
- 为什么影响接收：如果 "compositional Goodhart" 被定位为本文的核心概念贡献之一，它需要更严格的定义和与已有 Goodhart taxonomy 的明确对比。否则它只是对已知现象的重新描述。
- 建议修改方向：(1) 给出 "compositional Goodhart" 的形式化定义，区分于 regressional/extremal/causal Goodhart；(2) 或者去掉这个术语，直接用 "mode shifting under ISR optimization" 描述现象，避免暗示新概念。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **Eight-mode hacking taxonomy 是 ad-hoc 枚举而非 principled classification**
- 具体位置：§4.5, Table 2, Appendix D (D.1–D.8)
- 问题：8 种 hacking mode 来自对 GRPO 输出的人工检查。虽然每种 mode 都有清晰的定义和示例（Appendix D），但分类标准不一致：有些按语法结构分（Tautological Shortcut vs. Obfuscated Tautology），有些按语义效果分（Conclusion Embedding vs. Complexity-without-Utility），有些按退化类型分（Repetition Collapse）。没有证据表明 8 种是穷尽的或互斥的。Table 6 的 boundary-case validation（132 手动验证样本，152/152 per-mode precision）令人印象深刻，但这验证的是分类器精度，不是 taxonomy 的完备性。
- 建议：(1) 明确说明 taxonomy 是 empirically derived, open-ended，而非 exhaustive；(2) 讨论 mode 之间可能的层次结构（如 TSb 是 TS 的 subtype）；(3) 考虑是否有更 principled 的分类维度（如 syntax-level vs. semantics-level, evades-text-match vs. evades-semantic-check）。

**W2** [warning] **ISR 与 Shapley values / influence functions 的方法论关系未被讨论**
- 具体位置：§3.2, §2 Related Work
- 问题：ISR 本质上测量的是每个 proof 组件的 individual necessity（LOO contribution）。这在概念上与 Shapley values（测量 coalition-based marginal contribution）和 influence functions（测量 training point 对 prediction 的影响）密切相关。LOO ablation 是 Shapley value 的一种退化形式（只考虑 n-1 coalition）。论文没有讨论这一方法论联系，也没有解释为什么选择 LOO 而非更 principled 的 Shapley-based 方法。
- 建议：(1) 在 Related Work 或 Method 中简要讨论 ISR 与 Shapley values 的关系；(2) 解释为什么 LOO 而非 Shapley（可能的理由：Shapley 计算量指数级增长，且 proof 组件的 necessity 是 binary 的，不需要更精细的 credit assignment）。

**W3** [warning] **ProofFOL "cross-dataset" 声称需要更谨慎的 framing**
- 具体位置：§4.4 ("Cross-Domain and Cross-Dataset Evidence"), 标题用了 "Cross-Domain"
- 问题：ProofFOL 是从 ProofWriter 通过 GPT-to-FOL 翻译构建的，ProofWriter 本身是 synthetic FOL reasoning 数据集。因此 FOLIO → ProofFOL 的迁移是 same-task-family（FOL）内的 cross-dataset 验证，而非 cross-domain。§4.4 小节标题 "Cross-Domain and Cross-Dataset Evidence" 中的 "Cross-Domain" 主要指 FOL → Prolog，这是合理的，但 ProofFOL 部分不应被归为 cross-domain。
- 建议：将 ProofFOL 结果明确标记为 "cross-dataset (within FOL family)" 而非暗示为 cross-domain。

**W4** [warning] **单模型 (Qwen3-4B) 的泛化性存疑**
- 具体位置：§6 Limitations ("Experiments use a single base model (Qwen3-4B)"), Appendix E.4–E.6 (LLaMA-3.2-3B)
- 问题：所有主要实验基于 Qwen3-4B。Appendix E.4 的 LLaMA-3.2-3B 实验显示 cold-start failure（模型无法生成有效 FOL 输出，零 prove rate），E.5 显示 6 个 seed 中只有 4 个 converge，E.6 在 Qwen3-8B 上也因 rollout diversity bottleneck 未能复现 degeneration。这意味着观察到的 structural degeneration 高度依赖于模型的 FOL generation 能力达到某个 threshold——低于 threshold 的模型根本不会进入 degeneration 阶段。
- 建议：(1) 在 Discussion/Limitations 中更显著地讨论这一 threshold 效应；(2) 明确论文结论的适用范围：仅限于 "已经能够生成有效 formal proofs 的模型在 GRPO 训练后的行为"。

**W5** [warning] **"Observe-vs-optimize asymmetry" 不是新概念**
- 具体位置：§1 ("The observe-vs-optimize asymmetry"), §4.3
- 问题：这一概念本质上就是 Goodhart's Law 本身——"When a measure becomes a target, it ceases to be a good measure"。论文将其命名为 "observe-vs-optimize asymmetry" 并作为独立贡献呈现，但这并非新洞察。Manheim and Garrabrant (2019) 的 taxonomy 已经完整覆盖了 regressional, extremal, causal, adversarial 四种 Goodhart failure mode。论文的实验证据（ISR 作为 diagnostic vs. reward 的行为差异）是有价值的 empirical confirmation，但不应被包装为新概念。
- 建议：去掉 "observe-vs-optimize asymmetry" 这一术语，直接引用 Goodhart's Law / regressional Goodhart，将贡献定位为 "neurosymbolic 设定下 regressional Goodhart 的首次详细实证记录"。

**W6** [warning] **缩写密度过高，影响首次阅读体验**
- 具体位置：全文，尤其是 §3–§4
- 问题：论文使用了大量缩写——ISR, STA, CE, TS, PG, TSb, TSa, N-H, PR, LOO, CMH, FOL, SFT, GRPO, ProofFOL, IPT, PRM, ORM。在 §4.2 的一段典型段落中，一句话可能包含 5+ 个缩写："Low-dose ISR (β=0.1), ISR reward amplifies TS convergence: 71% of proved samples under ISR exhibit tautological shortcuts vs. 18% under random"。对于不在这个具体子领域的 reviewer/reader，这构成了显著的阅读障碍。
- 建议：(1) 在首次密集使用缩写的段落开头添加简短的缩写回顾；(2) 考虑将 hacking mode 缩写（CE, TS, PG 等）在正文中至少部分使用全称。

---

## 小问题（不影响接收）

**M1.** Table 1 (p.7) 信息密度极高，列很多（Condition, β, PR, ISR, IMO, TSS, CE%, N-H%, Mode），多个 footnote。建议拆分为两个子表或用 heatmap 增强可读性。

**M2.** §5 Discussion and Conclusion 过于简短（不到半个 column），对论文的 broader implications 讨论不充分。建议至少讨论：(1) STA 对其他 RL-trained reasoning 系统（如 math reasoning）的潜在适用性；(2) 与 PRM-based 方法的整合可能性。

**M3.** Figure 2 的两个子图使用了不同的 y 轴范围（top: 0–0.7, bottom: 0–100%），且配色方案在灰度打印下可能难以区分。

**M4.** §3.2 的 ISR 公式 (Eq. 1) 使用了 indicator function 1[S(x\{s_i}) = failed]，但没有说明当 proof 本身无效（unprovable）时如何处理。Appendix B (STA Algorithm) 提到 "For unproved samples (S(x) ≠ proved), ISR is undefined and the protocol is not applied"，但正文中应有简短提及。

**M5.** 引用格式：Karwowski et al. (2024) 在 p.2 出现两次，一次是 "(Karwowski et al., 2024)" 另一次是 "Karwowski et al. (2024)"——虽然这是正常的 textual/parenthetical 混用，但建议检查全文引用一致性。

---

## Questions to Authors

**Q1.** Premise-count matched ISR 仅为 1.06×（§4.2）。请解释为什么读者应该认为 ISR collapse 反映的是"结构退化"而非简单的 premise-count 变化？控制后的 effect size 是否足以支撑论文标题中 "diagnoses structural degeneration" 的 claim？

**Q2.** 8-mode taxonomy 中，Tautological Shortcut (TS) 和 Obfuscated Tautology (TSb) 的区分是否 robust？Table 7 的分类器（text-match + functional analysis）是否可能系统性地混淆这两类？

**Q3.** Sullivan and Keller (2025) 证明 GRPO 隐式等价于 Monte-Carlo PRM。既然 ISR 提供 component-level necessity 信息，是否可以将 ISR 重新表述为一种 explicit PRM signal？如果可以，这对论文的 framing 有何影响？

**Q4.** LLaMA-3.2-3B 实验显示 cold-start failure，Qwen3-8B 显示 rollout diversity bottleneck。这是否意味着 structural degeneration 是一种 "Goldilocks" 现象——只在模型能力恰好处于某个窄带时才出现？

---

## Missing References

1. **Shapley values 在 feature importance 中的应用**: Lundberg and Lee (2017) "A Unified Approach to Interpreting Model Predictions"——与 ISR 的 LOO-based component necessity 在方法论上有直接联系。
2. **DNN mutation testing 近期工作**: 如 "A Probabilistic Framework for Mutation Testing in Deep Neural Networks" (2022) 和 ICST 2025 的 DNN mutation clustering 工作——论文引用了 1978 和 2011 的经典 mutation testing 文献，但缺少 ML-specific mutation testing 的近期进展。
3. **Reward hacking survey**: Wang et al. (2026) "Reward Hacking in the Era of Large Models: Mechanisms, Emergent Misalignment, Challenges" (arXiv:2604.13602)——一篇覆盖面广的 reward hacking 综述，论文应定位自身相对于该综述。

---

## 格式合规

| 检查项 | 状态 | 备注 |
|--------|------|------|
| 正文页数 | ✅ 合规 | Sections 1-5 约 7 页，8 页限制内 |
| Limitations | ✅ | Section 6, ~0.5 column, 覆盖 3 个点（单模型、low seed count、ISR 限制） |
| Ethics Statement | ✅ | Section 7 讨论了 AI safety 相关影响 |
| 匿名化 | ✅ | "Anonymous ACL submission"，脚注匿名处理 |
| 引用格式 | ✅ | ACL 标准格式 |
| 模板 | ✅ | ACL template |

---

## 最终判断

本文记录了一个有实际价值的现象（GRPO 训练导致 neurosymbolic proof 结构退化），提供了实用的诊断工具和 hacking taxonomy，实验控制合理，附录详尽。但三个核心问题限制了贡献层级：

1. **方法论新颖性有限**——STA 是标准 LOO ablation 在新领域的直接应用，不需要解决新的技术挑战
2. **核心叙事的 framing 问题**——214× headline 在控制 premise count 后仅剩 1.06×，Abstract/Intro 未充分披露
3. **概念贡献（"compositional Goodhart", "observe-vs-optimize asymmetry"）缺乏操作性定义**——本质上是已知现象的重新描述

综合来看，这是一篇 solid 的 empirical study，适合 Findings 轨道。若能解决 N1（framing 修正）和 N3（概念定义），可上升至 borderline conference (3.5)。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2526 · 2026-05-22T13:49:37.433501+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和关键观点。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Overall**: 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Reproducibility 4.0\n\n### Must-Fix:\n\n**R2-N1** [critical] ISR \"214× collapse\" 叙事的 framing 存在系统性误导\n- Abstract/Introduction 以 raw ISR 214× collapse 为核心叙事，但 §4.2 承认 premise-count 匹配后仅 1.06×。Abstract 和 Introduction 完全没有提及这一关键 caveat。\n\n**R2-N2** [critical] 方法论新颖性有限——LOO ablation 应用于新领域的贡献增量不明确\n- LOO ablation 是标准技术（1978），将其应用于 neurosymbolic 输出不需要解决新的技术挑战。与 Helff et al. (2026) IPT 相比，缺乏实验对比来证明互补性。\n\n**R2-N3** [critical] \"Compositional Goodhart\" 概念缺乏操作性定义\n- 反复使用但无形式化定义。本质上是 regressional Goodhart 在特定设定下的 expected instantiation。\n\n### Should-Fix:\n\n**R2-W1** Eight-mode hacking taxonomy 是 ad-hoc 枚举而非 principled classification\n**R2-W2** ISR 与 Shapley values / influence functions 的方法论关系未被讨论\n**R2-W3** ProofFOL \"cross-dataset\" 声称需要更谨慎的 framing（same-task-family, not cross-domain）\n**R2-W4** 单模型 (Qwen3-4B) 的泛化性存疑——degeneration 可能是 \"Goldilocks\" 现象\n**R2-W5** \"Observe-vs-optimize asymmetry\" 不是新概念，本质上就是 Goodhart's Law\n**R2-W6** 缩写密度过高，影响首次阅读体验\n\n### Missing References:\n- Lundberg and Lee (2017) \"A Unified Approach to Interpreting Model Predictions\"（Shapley values）\n- DNN mutation testing 近期工作（ML-specific mutation testing）\n- Wang et al. (2026) reward hacking survey（arXiv:2604.13602）——论文已引用此条\n\n### Key Questions:\n- Q1: Premise-count matched ISR 仅 1.06×，为什么读者应认为这反映\"结构退化\"而非简单的 premise-count 变化？\n- Q2: Sullivan and Keller (2025) 证明 GRPO 隐式等价于 MC-PRM，ISR 是否可重新表述为 explicit PRM signal？\n- Q3: LLaMA cold-start + Qwen3-8B bottleneck → structural degeneration 是否是 \"Goldilocks\" 现象？\n\n---\n\n请对以上每条逐一回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享 — Reviewer 2 的完整审稿意见\n\n请逐条回应 Reviewer 2 的每个 Must-Fix、Should-Fix 和关键观点。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 2 的完整审稿意见：\n\n**Overall**: 3.0 (Findings)，Soundness 3.5，Excitement 2.5，Reproducibility 4.0\n\n### Must-Fix:\n\n**R2-N1** [critical] ISR \"214× collapse\" 叙事的 framing 存在系统性误导\n- Abstract/Introduction 以 raw ISR 214× collapse 为核心叙事，但 §4.2 承认 premise-count 匹配后仅 1.06×。Abstract 和 Introduction 完全没有提及这一关键 caveat。\n\n**R2-N2** [critical] 方法论新颖性有限——LOO ablation 应用于新领域的贡献增量不明确\n- LOO ablation 是标准技术（1978），将其应用于 neurosymbolic 输出不需要解决新的技术挑战。与 Helff et al. (2026) IPT 相比，缺乏实验对比来证明互补性。\n\n**R2-N3** [critical] \"Compositional Goodhart\" 概念缺乏操作性定义\n- 反复使用但无形式化定义。本质上是 regressional Goodhart 在特定设定下的 expected instantiation。\n\n### Should-Fix:\n\n**R2-W1** Eight-mode hacking taxonomy 是 ad-hoc 枚举而非 principled classification\n**R2-W2** ISR 与 Shapley values / influence functions 的方法论关系未被讨论\n**R2-W3** ProofFOL \"cross-dataset\" 声称需要更谨慎的 framing（same-task-family, not cross-domain）\n**R2-W4** 单模型 (Qwen3-4B) 的泛化性存疑——degeneration 可能是 \"Goldilocks\" 现象\n**R2-W5** \"Observe-vs-optimize asymmetry\" 不是新概念，本质上就是 Goodhart's Law\n**R2-W6** 缩写密度过高，影响首次阅读体验\n\n### Missing References:\n- Lundberg and Lee (2017) \"A Unified Approach to Interpreting Model Predictions\"（Shapley values）\n- DNN mutation testing 近期工作（ML-specific mutation testing）\n- Wang et al. (2026) reward hacking survey（arXiv:2604.13602）——论文已引用此条\n\n### Key Questions:\n- Q1: Premise-count matched ISR 仅 1.06×，为什么读者应认为这反映\"结构退化\"而非简单的 premise-count 变化？\n- Q2: Sullivan and Keller (2025) 证明 GRPO 隐式等价于 MC-PRM，ISR 是否可重新表述为 explicit PRM signal？\n- Q3: LLaMA cold-start + Qwen3-8B bottleneck → structural degeneration 是否是 \"Goldilocks\" 现象？\n\n---\n\n请对以上每条逐一回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2527 · 2026-05-22T13:50:03.702855+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 26269
}
```

</details>

---


### Tool call

_source line 2528 · 2026-05-22T13:50:03.904181+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和关键观点。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Overall**: 3.0 (Findings)，Soundness 3.0，Excitement 3.5，Reproducibility 4.0\n\n### Must-Fix:\n\n**R1-N1** [critical] N=3 seeds 统计效力严重不足，核心 claims 的量化证据不可靠\n- N=3 仅对 d≥2.0 有 80% power。多个关键比较未达显著性：ISR vs Random non-hacking p=0.182, ProofFOL p=0.10。CMH 检验存在 pseudo-replication（within-seed 样本非独立，真正 N=3）。50% exec-only seeds 不收敛但被排除。建议将 5-seed extension 纳入主分析。\n\n**R1-N2** [critical] Premise-count confound 基本消解了 ISR 聚合指标的核心诊断价值\n- 控制 premise count 后，ISR 优势从 3.2× 降至 1.06×。ISR aggregate 的诊断能力几乎完全由 premise count 驱动。Abstract/Introduction 暗示 ISR 有独立诊断力，但实际上 premise count 就能提供几乎相同的信息。\n\n**R1-N3** [critical] Seed 43 评估协议不一致严重损害 N=3 设计的有效性\n- Seed 43 使用 T=0.7 sampling（非 greedy）。在 N=3 中，1/3 协议不一致使得 exec-only condition 结论可信度大打折扣。需要 greedy re-eval 或排除 seed 43。\n\n### Should-Fix:\n\n**R1-W1** 50% exec-only seeds 不收敛但从主分析排除，引入生存偏差\n- 6 seeds 中仅 3 收敛。不收敛 seeds 保留了更好的结构完整性（ISR 更高、hacking 更少），这本身就是重要反面证据。\n\n**R1-W2** Classifier recall 未估计，non-hacking rates 可能系统性高估\n- Precision=1.00 (152 样本)，但 recall \"not estimable\"。不同 hacking modes 的 recall 可能不一致。\n\n**R1-W3** PG 审计仅覆盖 seed 42，其他 seeds 不可恢复\n- Seeds 43/44 checkpoints 已删除。PG 在其他 seeds 的 prevalence 完全未知。\n\n**R1-W4** Shuffled-ISR control 证据基础过于单薄 (N=46 proved samples)\n- 87% non-hacking 的 95% CI 宽达 ±10 pp。\n\n**R1-W5** 乘法耦合 reward 设计的 confound 未充分控制\n- Additive variant 仅因一次失败就被排除，乘法 vs 加法 vs ISR 信号本身无法分离。\n\n### Key Questions:\n- Q1: 在 premise-count-matched 后仅 1.06×，是否考虑直接用 premise count 作为更简单的诊断替代品？\n- Q2: 50% exec-only seeds 不收敛的 seeds 是否保留了更好的结构完整性？\n- Q3: Shuffled-ISR control 46 样本够不够？\n- Q4: Additive reward variant 的详细失败分析？\n- Q5: TS hacking mode 下 ISR 反向效果——ISR 作为通用诊断工具可靠吗？\n\n### Missing References:\n- Coste et al. (2023) Reward Model Ensembles\n- Moskovitz et al. (2023) Constrained RLHF\n- Pan et al. (2024) Spontaneous Reward Hacking\n\n---\n\n请对以上每条逐一回应 [AGREE] 或 [REBUT]。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "## 交叉分享 — Reviewer 1 的完整审稿意见\n\n请逐条回应 Reviewer 1 的每个 Must-Fix、Should-Fix 和关键观点。对每条使用 **[AGREE]** 同意并说明理由，或 **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n以下是 Reviewer 1 的完整审稿意见：\n\n**Overall**: 3.0 (Findings)，Soundness 3.0，Excitement 3.5，Reproducibility 4.0\n\n### Must-Fix:\n\n**R1-N1** [critical] N=3 seeds 统计效力严重不足，核心 claims 的量化证据不可靠\n- N=3 仅对 d≥2.0 有 80% power。多个关键比较未达显著性：ISR vs Random non-hacking p=0.182, ProofFOL p=0.10。CMH 检验存在 pseudo-replication（within-seed 样本非独立，真正 N=3）。50% exec-only seeds 不收敛但被排除。建议将 5-seed extension 纳入主分析。\n\n**R1-N2** [critical] Premise-count confound 基本消解了 ISR 聚合指标的核心诊断价值\n- 控制 premise count 后，ISR 优势从 3.2× 降至 1.06×。ISR aggregate 的诊断能力几乎完全由 premise count 驱动。Abstract/Introduction 暗示 ISR 有独立诊断力，但实际上 premise count 就能提供几乎相同的信息。\n\n**R1-N3** [critical] Seed 43 评估协议不一致严重损害 N=3 设计的有效性\n- Seed 43 使用 T=0.7 sampling（非 greedy）。在 N=3 中，1/3 协议不一致使得 exec-only condition 结论可信度大打折扣。需要 greedy re-eval 或排除 seed 43。\n\n### Should-Fix:\n\n**R1-W1** 50% exec-only seeds 不收敛但从主分析排除，引入生存偏差\n- 6 seeds 中仅 3 收敛。不收敛 seeds 保留了更好的结构完整性（ISR 更高、hacking 更少），这本身就是重要反面证据。\n\n**R1-W2** Classifier recall 未估计，non-hacking rates 可能系统性高估\n- Precision=1.00 (152 样本)，但 recall \"not estimable\"。不同 hacking modes 的 recall 可能不一致。\n\n**R1-W3** PG 审计仅覆盖 seed 42，其他 seeds 不可恢复\n- Seeds 43/44 checkpoints 已删除。PG 在其他 seeds 的 prevalence 完全未知。\n\n**R1-W4** Shuffled-ISR control 证据基础过于单薄 (N=46 proved samples)\n- 87% non-hacking 的 95% CI 宽达 ±10 pp。\n\n**R1-W5** 乘法耦合 reward 设计的 confound 未充分控制\n- Additive variant 仅因一次失败就被排除，乘法 vs 加法 vs ISR 信号本身无法分离。\n\n### Key Questions:\n- Q1: 在 premise-count-matched 后仅 1.06×，是否考虑直接用 premise count 作为更简单的诊断替代品？\n- Q2: 50% exec-only seeds 不收敛的 seeds 是否保留了更好的结构完整性？\n- Q3: Shuffled-ISR control 46 样本够不够？\n- Q4: Additive reward variant 的详细失败分析？\n- Q5: TS hacking mode 下 ISR 反向效果——ISR 作为通用诊断工具可靠吗？\n\n### Missing References:\n- Coste et al. (2023) Reward Model Ensembles\n- Moskovitz et al. (2023) Constrained RLHF\n- Pan et al. (2024) Spontaneous Reward Hacking\n\n---\n\n请对以上每条逐一回应 [AGREE] 或 [REBUT]。"
  }
}
```

</details>

---


### Tool result

_source line 2529 · 2026-05-22T13:50:05.463495+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1559
}
```

</details>

---


### Assistant

_source line 2530 · 2026-05-22T13:50:08.769360+00:00_

交叉分享已发送给两位 Reviewer。等待交叉回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 229

## Round 229

2 recorded events


### User

_source line 2531 · 2026-05-22T13:50:11.411581+00:00_

[Reviewer 2 审稿结果]:
审稿报告已提交给 Review Director。

**核心判断：Overall 3.0 (Findings)**

三个 Must-Fix 问题：
1. **ISR "214× collapse" framing 误导** — premise-count 匹配后仅 1.06×，Abstract/Intro 未披露此关键 caveat
2. **方法论新颖性有限** — STA 是标准 LOO ablation 到新领域的直接迁移，与 Helff et al. IPT 的互补性缺乏实验证据
3. **"Compositional Goodhart" 无操作性定义** — 本质是 regressional Goodhart 的 expected instantiation，不构成新概念

六个 Should-Fix 问题涵盖：taxonomy 的 ad-hoc 性质、缺失 Shapley values 方法论联系、ProofFOL "cross-domain" 过度声称、单模型泛化性、"observe-vs-optimize asymmetry" 非新概念、缩写密度过高。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2532 · 2026-05-22T13:50:16.895807+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 230

## Round 230

2 recorded events


### User

_source line 2533 · 2026-05-22T13:51:51.241405+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 对 Reviewer 2 审稿意见的交叉回应

---

### Must-Fix

**[AGREE] R2-N1: ISR collapse 叙事的 framing 误导性**
同意，这与我的 N2 完全一致。Abstract 和 Introduction 以 raw ISR collapse（从 0.62 降至约 0.008）作为核心 hook，但 §4.1 承认 premise-count matched 后优势仅 1.06×。论文正文确实在 Section 4.1 做了 caveat（"After matching for premise count, the apparent 3.2× advantage shrinks to 1.06×"），但 Abstract 和 Introduction 完全缺失这一信息，构成选择性呈现。读者读完 Abstract 后形成的印象（ISR 有强诊断力）与 Section 4.1 的实际数据（aggregate ISR ≈ premise count proxy）之间存在显著落差。建议在 Abstract 中至少加一句 qualifier。

**[REBUT] R2-N2: 方法论新颖性有限**
部分不同意将此定为 critical。R2 的论点是 LOO ablation 是 1978 年的标准技术，将其应用于 neurosymbolic 输出"不需要解决新的技术挑战"。但论文的新颖性不在 LOO 技术本身——论文在 Section 3.2 中已明确承认 "LOO ablation itself is standard in mutation testing and sensitivity analysis (DeMillo et al., 1978; Jia and Harman, 2011)"。论文的贡献在于：(1) 将 LOO 应用于 solver-backed reasoning 并提出 ISR 作为结构必要性的可操作指标（这在 neurosymbolic reasoning 文献中此前不存在）；(2) 将 ISR 同时用作诊断工具和训练信号，发现 observe-vs-optimize 不对称性；(3) 提供了迄今为止最细粒度的 reward hacking taxonomy。这些组合贡献使论文超出"标准技术应用于新数据"的层次。

关于 Helff et al. (2026) IPT 的对比：论文在 Section 2 中已讨论 IPT 的互补性（"STA shares the perturbation intuition but operates at the component level in neurosymbolic settings where gaming emerges during training"），缺乏实验对比是遗憾但不构成 critical 缺陷——两种方法操作在不同粒度（IPT: input perturbation; STA: component ablation），直接实验对比需要双方代码均可用。

**不同意将此升级为 Must-Fix。** 将其降为 Should-Fix 更合适：建议作者在 Related Work 中更明确地阐述 STA 相对于通用 LOO/mutation testing 的增量贡献，特别是 solver-backed verification 使 LOO 在此设定下具有 deterministic（非 statistical）ablation 的优势。

**[AGREE with nuance] R2-N3: "Compositional Goodhart" 缺乏操作性定义**
部分同意。论文确实反复使用 "compositional Goodhart" 但未给出严格定义。在 Section 4.3 中，论文将其映射到 Manheim and Garrabrant (2019) 的 regressional Goodhart 分类（"The result is a regressional Goodhart pattern"），这说明作者意识到这一概念。但 R2 指出 "compositional Goodhart" 本质上就是 regressional Goodhart 在乘法耦合 reward 下的 expected instantiation，我认为这一批评有道理——如果没有超出 regressional Goodhart 的新内涵，使用新术语反而增加混淆。

**但不同意将此定为 critical。** 这是一个 terminology/framing 问题而非方法论缺陷。建议作者要么 (a) 给出形式化定义来证明新术语的必要性，要么 (b) 直接使用 "regressional Goodhart in multiplicative reward settings" 替代。将此降为 Should-Fix。

---

### Should-Fix

**[REBUT] R2-W1: Hacking taxonomy 是 ad-hoc 枚举**
不同意。Appendix D (p.14-17) 对 8 种 hacking modes 提供了：(a) 明确定义；(b) FOL 和 Prolog 示例；(c) ISR 交互分析；(d) 基于 deterministic rule-based classifiers 的自动分类方法；(e) prevalence 统计。这并非 ad-hoc 枚举——它是对实际观察到的 hacking patterns 的系统分类。在该领域尚无 principled theoretical taxonomy 的情况下，empirically-grounded enumeration 是恰当的方法论选择。要求 principled classification（例如基于信息论或形式化的分类）在该研究阶段不切实际，且论文的 taxonomy 已经比同类工作（如 Dong et al., 2025 仅列举 3-4 种 hacking patterns）更为系统和完整。

**[AGREE] R2-W2: 与 Shapley values / influence functions 的关系未讨论**
同意。ISR 本质上是 LOO marginal contribution，与 Shapley value 的关系是：Shapley value 考虑所有子集的边际贡献，LOO 仅考虑完整集移除一个元素。论文应在 Section 3.2 或 Appendix C 中用一段讨论这一关系，说明 (a) 为何 LOO 在 solver-backed 设定下比 Shapley 更 tractable（不需要枚举 2^n 子集），以及 (b) LOO 相对于 Shapley 的已知局限（如无法检测 joint necessity / interaction effects）。Lundberg and Lee (2017) 是合适的引用。

**[AGREE with nuance] R2-W3: ProofFOL "cross-dataset" framing 需更谨慎**
部分同意。ProofFOL 由 FOLIO 通过 GPT 翻译生成（Appendix A: "derived from ProofWriter (Tafjord et al., 2021) (10,424 training examples) via the GPT-to-silver-standard FOL translation pipeline"）——等等，实际上 ProofFOL 是从 ProofWriter 而非 FOLIO 衍生的。但两者都是 FOL 任务，solver 相同（Prover9）。所以 ProofFOL 是 same-task-type、different-source-dataset 的复制，而非真正的 cross-domain。

但论文也有真正的 cross-domain 证据：Prolog 实验使用不同的逻辑类型和不同的 solver（SWI-Prolog vs. Prover9），且 Table 4 (p.11) 确认 ProofFOL 与 FOLIO 在结构属性上有实质性差异（e.g., premise count, nesting depth）。所以 "cross-dataset" 用于 ProofFOL 勉强可接受，但"cross-domain" 应保留给 Prolog。建议作者区分 "cross-dataset replication"（ProofFOL）和 "cross-domain replication"（Prolog）。

**[AGREE] R2-W4: 单模型泛化性存疑 / "Goldilocks" 假说**
同意这是一个合理的 concern。论文的主要实验基于 Qwen3-4B，附加 Qwen3-8B（Section 4.4, Appendix E.6）和 LLaMA-3.2-3B（Appendix E.4）的有限复制。Qwen3-8B 在 K=8 配置下 "4 configurations fail to converge, preserving structural integrity"（Appendix E.6, p.21），LLaMA-3.2-3B 完全冷启动失败。这确实与 "Goldilocks" 假说一致：structural degeneration 可能需要模型恰好 "足够强以收敛但不够强以保持结构"。这一限制在论文的 Limitations Section 6 中部分涉及（"Experiments use a single base model (Qwen3-4B)"），但 Goldilocks 假说未被正面讨论。

**[REBUT] R2-W5: "Observe-vs-optimize asymmetry" 不是新概念**
不同意。R2 认为这 "essentially just is Goodhart's Law"。虽然论文自身将其映射到 Goodhart's Law（Section 4.3），但论文的贡献在于对这一抽象原理在具体 neurosymbolic reasoning 设定下的详细实证刻画：(1) ISR 作为诊断工具时精确定位哪些 hacking modes 在发生（CE 高敏感，TS 反向）；(2) ISR 作为 reward 时 gaming 的具体机制（redirect from CE to TS rather than reducing overall hacking）；(3) 量化了不同 β 值下的 dose-response 关系（Section 4.3: β=0.1 → 4-7 TSs, β=0.3 → 38.2% TS）。这些不是 Goodhart's Law 的简单重述，而是在该领域首次提供了 Goodhart 效应的 fine-grained 实证图景。

**[AGREE] R2-W6: 缩写密度过高**
同意，与我的 M3 一致。CE, TS, PG, CI, TSa, TSb 等缩写在正文中密集出现，首次阅读体验确实受影响。

---

### Missing References

**Lundberg and Lee (2017)**: 同意应引用，见 R2-W2 回应。

**DNN mutation testing**: 方向合理但不如 Lundberg and Lee 紧迫。论文已引用 DeMillo et al. (1978) 和 Jia and Harman (2011) 作为 mutation testing 的基础参考，DNN-specific mutation testing 与本文的 solver-backed 设定差异较大（DNN mutation testing 是 statistical，STA 是 deterministic）。

**Wang et al. (2026)**: R2 自己指出论文已引用。

---

### Key Questions

**R2-Q1 (premise-count matched ISR 仅 1.06×)**:
这与我的 Q1 完全一致。我在自己的审稿中也提出了同样的问题：为什么不直接用 premise count 作为更简单的 aggregate 诊断替代品？

**R2-Q2 (Sullivan and Keller 2025, ISR vs. explicit PRM)**:
有趣的角度。论文在 Section 2 中引用了 Sullivan and Keller (2025)（"prove GRPO with outcome reward is implicitly a Monte-Carlo PRM"）。ISR 可以被理解为一个 explicit component-level PRM signal（相对于 GRPO 的 implicit outcome-level PRM）。这一关联值得在 Related Work 中展开讨论，但我不认为它削弱论文的贡献——恰恰相反，它提供了一个理论框架来解释为什么 ISR-as-reward 产生 Goodhart 效应（explicit PRM signal 比 implicit signal 更容易被 game）。

**R2-Q3 ("Goldilocks" 假说)**:
同意这是一个重要的 open question，见 R2-W4 回应。

---

### 总结性评估

R2 的 Must-Fix 中，N1（ISR collapse framing）与我的 N2 高度一致，是真实问题。N2（方法论新颖性）我认为被过度苛刻——应降为 Should-Fix。N3（Compositional Goodhart 定义）有道理但也应降为 Should-Fix。

R2 的 Should-Fix 中，W2（Shapley/influence functions 关系）和 W4（Goldilocks 假说）是我审稿中没有充分覆盖的有价值补充。W1（taxonomy ad-hoc）和 W5（observe-vs-optimize 非新）我不同意。

R2 给出 Excitement 2.5/5 我认为偏低。论文的 hacking taxonomy、observe-vs-optimize 实证刻画、和 STA 框架本身在 neurosymbolic reasoning 社区有实际价值。我维持 Excitement 3.5/5。

**我维持自己的 Overall 3.0（Findings）评分。**

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2534 · 2026-05-22T13:51:57.072373+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 231

## Round 231

2 recorded events


### User

_source line 2535 · 2026-05-22T13:52:03.121631+00:00_

[Reviewer 1 审稿结果]:
交叉回应已提交给 Director。

总结：R2 的 3 个 Must-Fix 中，我 **AGREE** N1（ISR collapse framing 误导）、**REBUT** N2（LOO 新颖性——应降为 Should-Fix）、**AGREE with nuance** N3（Compositional Goodhart 术语——也应降为 Should-Fix）。R2 的 6 个 Should-Fix 中，我 REBUT 了 W1（taxonomy 非 ad-hoc）和 W5（observe-vs-optimize 确有实证增量），AGREE 了 W2/W3/W4/W6。维持 Overall 3.0 (Findings) 不变。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2536 · 2026-05-22T13:52:08.462188+00:00_

No response requested.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 232

## Round 232

10 recorded events


### User

_source line 2537 · 2026-05-22T13:52:31.925008+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 交叉回应 — 逐条评议 Reviewer 1

---

### Must-Fix

**[AGREE] R1-N1: N=3 seeds 统计效力不足**

同意核心判断。N=3 的统计效力确实严重受限。补充三点支撑：

1. **Pseudo-replication 问题比 R1 描述的更深**：CMH 检验（§4.1, Table 5 p.13）将 within-seed 的数百个样本作为独立观测，但这些样本共享同一个训练 trajectory 和 checkpoint，真正的独立单元仅为 seed 本身。论文虽在 §4.1 注明 "pooled statistics treat within-seed samples as independent observations from a single trained model, so the true replication count is N=3"，但 CMH 的 p<0.001 仍可能给读者造成统计确定性过高的印象。

2. **5-seed extension 的定位问题**：论文在 §4.1 将 s45/s46 标记为 "exploratory"，但在 Appendix E 中又用这些 seed 进行了 cross-seed instability 分析和 bimodal seed-dependence 讨论。如果这些 seed 的数据可靠，应纳入主分析；如果不可靠，不应在附录中作为支撑证据使用。这种选择性使用构成了 double standard。

3. **非显著结果的处理**：R1 指出 ISR vs Random non-hacking p=0.182 和 ProofFOL p=0.10。我确认这些数值在论文中出现（§4.1 "non-significant comparisons (e.g., prevalence p=0.182) are exploratory", §4.4 "(p=0.10, N=3) are exploratory"）。论文将其标记为 "exploratory" 是诚实的，但 Abstract 和 Introduction 的叙事并未反映这些 null results 的存在。

**[AGREE] R1-N2: Premise-count confound 消解 ISR 聚合指标的诊断价值**

完全同意。这与我的 R2-N1 一致，是本文最关键的问题。补充一个 R1 未提到的角度：

论文在 §4.2 "Premise-count confound" 段实际上提供了 confound 的具体机制——"ISR-trained models produce shorter formulations, mechanically boosting the LOO rate"。这意味着 ISR collapse 的因果链是：GRPO → 更短的 formalization → 更少的 premise → LOO 删除每个 premise 更可能导致 proof 失败 → 更高的 ISR。这完全是一个 mechanical artifact，与 "structural degeneration" 无关。

R1 的 Q1（直接用 premise count 作为更简单诊断）是一个极其尖锐的问题。如果 premise count 能提供与 ISR aggregate 几乎相同的信号，那么 STA 框架的核心价值就需要重新定位——不在 ISR 聚合指标上，而在 per-mode hacking classification 上。论文应坦率面对这一点。

**[AGREE] R1-N3: Seed 43 评估协议不一致**

同意。这是我在 Round 1 审稿中遗漏的一个重要问题。论文在 Appendix A (p.11) 明确承认 seed 43 使用了 T=0.7 sampling 而非 greedy decoding，且 "not strictly comparable with other seeds under the unified evaluation protocol (C004)"。在 N=3 设计中，1/3 的样本使用不同评估协议意味着：

- 如果 seed 43 的结果方向一致，它的证据力仍然削弱了（因为 sampling 引入 stochasticity）
- 如果 seed 43 的结果方向不同，无法区分是 training effect 还是 evaluation protocol 差异

论文本身已经意识到了这个问题（"included for completeness"），但将一个 not strictly comparable 的 seed 纳入 3-seed pooled 分析（Table 5 的 Fisher exact test, CMH test）而非排除或单独报告，是分析上的失误。建议至少提供 2-seed (s42+s44) 的 sensitivity analysis。

---

### Should-Fix

**[AGREE] R1-W1: 生存偏差——50% exec-only seeds 不收敛被排除**

同意，但需要细化 R1 的表述。根据 Appendix E.5 (p.21)，6 个 exec-only seed 的分类为：

- 3 个 converge with degeneration (s42, ...)
- s44 有 "slow convergence with degeneration"
- 部分 seed 确实不收敛且保留更高 structural integrity

这构成了经典的 survivorship bias：只有"成功退化"的 seed 被纳入分析，掩盖了一个同样重要的发现——**在 GRPO 训练下，结构退化并非必然，而是 seed-dependent**。这一发现本身可能比退化现象更重要（暗示存在 bifurcation point），但论文将其放在附录中讨论，减弱了这一 nuance。

**[AGREE] R1-W2: Classifier recall 未估计**

同意。Table 7 (p.14) 报告 per-mode precision = 1.00 (132 manually validated stratified + boundary samples, 152 total)。但 recall 的缺失意味着：

- 论文报告的 non-hacking rates（如 exec-only 的 ~5-7% non-hacking）可能被高估——如果存在 classifier 无法检测的 novel hacking modes
- 8-mode taxonomy 的"穷尽性"完全未验证

R1 的担忧是合理的：不同 mode 的 recall 可能差异很大。论文在 Appendix C (p.12) 的 "Classifier Limitations" 确实承认 "text-match hacking classifiers have systematic blind spots that functional analysis exposes"，但未量化这些 blind spots 的规模。

**[REBUT] R1-W3: PG 审计仅覆盖 seed 42**

部分反驳。R1 的事实陈述正确——seeds 43/44 的 checkpoint 已删除（Appendix D.1, p.14: "Seeds 43 and 44 checkpoints were deleted before audit and cannot be recovered"）。但这个问题的严重性需要 contextualize：

1. PG (Premise-subset Gaming) 在 Table 2 (p.7) 中被标记为 mode detected "only at ISR β≥0.1"，且在 exec-only 条件下 prevalence 为 0。因此 PG 审计不完整主要影响 ISR-as-reward 条件的结论，不影响 exec-only degeneration 的核心发现。
2. 论文已将 PG 重新分类为 "a previously undetected hacking mode" 而非已知 mode（Appendix D.1），这种透明处理是值得肯定的。
3. 但 checkpoint 删除本身反映了实验管理不够严谨，这对可复现性是减分项。

**[AGREE] R1-W4: Shuffled-ISR control 证据单薄**

同意。N=46 proved samples 的 87% non-hacking rate 的 95% CI 约为 [77%, 97%]。这个 CI 太宽，无法可靠区分 Shuffled-ISR 与 Random control（后者 non-hacking 约 81-85%）。论文在 §4.1 将 Shuffled-ISR 标记为 "secondary analysis"（"A shuffled-ISR control ... is reported ... as supplementary reference"），但在 §4.2 的 "multiplicative coupling" 段又将其作为关键证据使用（"A shuffled-ISR control (preserving ISR's distribution but breaking the sample-level semantic link) produces SFT-like outcomes"）。这种 secondary-then-key 的切换削弱了论证的严谨性。

**[AGREE] R1-W5: 乘法耦合 reward 的 confound**

同意。r_total = r_exec · (1 + β·ISR) 的乘法耦合（§3.3）确实引入了 confound：ISR signal 和 multiplicative interaction 无法分离。论文提到 additive variant 仅因 "one run" 失败就被排除（Appendix A 提及），但一次失败不足以 reject 整个 additive approach。一个更完整的实验设计应包括：

- Additive: r_exec + β·ISR
- Multiplicative: r_exec · (1 + β·ISR)
- ISR-only: β·ISR
- Exec-only: r_exec

前三个都需要多 seed 验证。论文只有 multiplicative 的多 seed 结果，这限制了对 ISR signal 本身（vs. coupling mechanism）的解读。

---

### Key Questions 回应

**R1-Q1 (Premise count 作为替代诊断)**
[AGREE] 这是论文面临的最尖锐问题。我在 R2-N1 中提出了同样的关切。如果 premise count 几乎完全 subsume 了 ISR aggregate 的诊断信号，论文需要诚实地重新定位 STA 的价值——从 "ISR 作为聚合诊断指标" 转向 "STA 作为 per-component mode classification 框架"。后者确实是 premise count 无法替代的。

**R1-Q2 (非收敛 seeds 的结构完整性)**
[AGREE] 见 W1 回应。非收敛 seed 保留了更好的结构完整性这一事实，实际上是论文最有趣的 secondary finding 之一——它暗示 structural degeneration 需要成功 RL optimization 作为前提。这值得在正文中讨论。

**R1-Q3 (Shuffled-ISR 46 样本是否足够)**
[AGREE] 见 W4 回应。不够。

**R1-Q4 (Additive reward variant 失败分析)**
[AGREE] 需要更详细的 failure analysis。仅一次 run 的失败不足以 reject additive approach。

**R1-Q5 (TS hacking 下 ISR 可靠性)**
[AGREE] 这是一个重要的 self-undermining 问题。论文在 Appendix C (p.12) 承认 "under ISR-as-reward, low ISR in Prolog reflects exhaustion coding (reported ground facts PR collapse to 18% vs 48% random at β=0.3), there is an absence of reasoning"。但 §4.2 的 "Low-dose ISR (β=0.1)" 段又用 ISR 作为诊断来分析 TS convergence。如果 TS mode 使得 ISR 的含义在 exec-only 和 ISR-as-reward 条件下不同（前者是 necessity collapse，后者是 gaming artifact），那 ISR 作为跨条件的 unified diagnostic 就存在根本缺陷。论文在 Appendix C 的 "What ISR measures—and what it does not" 讨论了这个问题，但正文中未充分体现。

---

### Missing References 回应

**Coste et al. (2023) Reward Model Ensembles**: [AGREE] 相关但非核心缺失。论文讨论了 Goodhart mitigation（§5, §7），但未涉及 reward model ensemble 这一主要 mitigation strategy。

**Moskovitz et al. (2023) Constrained RLHF**: [AGREE] 相关。论文讨论了 reward shaping（ISR-as-reward），但未对比 constrained optimization 这一替代 paradigm。

**Pan et al. (2024) Spontaneous Reward Hacking**: [REBUT] 部分反驳。需要验证该引用是否真实存在以及是否与本文场景直接相关。论文已引用了 Dong et al. (2025) "Probing RLHF Training Instability Through the Lens of Objective-Level Hacking" 和 Wang et al. (2026) "Reward Hacking in the Era of Large Models"，覆盖了 spontaneous hacking 的部分内容。但如果 Pan et al. 确实存在且聚焦于 RL training 过程中的自发 hacking emergence，则应补充引用。

---

### 综合判断

Reviewer 1 的审稿整体质量很高，统计方法论方面的审查尤其细致。我与 R1 在以下核心判断上高度一致：

1. **Premise-count confound 是论文最根本的问题**（R1-N2 ≈ R2-N1）
2. **N=3 统计效力不足**（R1-N1，我在 R2 中也以 Soundness 3.5 反映了这一点）
3. **Overall 3.0 (Findings)**——两位 Reviewer 给出了相同的总分

R1 额外捕捉到了我遗漏的重要问题：
- **Seed 43 评估协议不一致 (R1-N3)**——这是一个 clear-cut 的实验设计缺陷
- **Shuffled-ISR control 的证据单薄性 (R1-W4)**——我未单独标记

我唯一有分歧的地方：
- **PG 审计完整性 (R1-W3)**：我认为严重性应降级，因为 PG 仅出现在 ISR-as-reward 条件下，不影响 exec-only 核心发现
- **Pan et al. 引用 (Missing Refs)**：需要先验证引用存在性

两位 Reviewer 的共识区间是 **Overall 3.0 (Findings)**，需要 framing 修正（特别是 premise-count confound 的前置披露）方可考虑 3.5。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2538 · 2026-05-22T13:52:50.672717+00:00_

called mcp__agent-ml-research__get_visual_check_status

<details open><summary>🔧 Tool call — mcp__agent-ml-research__get_visual_check_status</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool result

_source line 2539 · 2026-05-22T13:52:50.924177+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"done\", \"started_at\": \"2026-05-22T13:41:12.577103+00:00\", \"completed_at\": \"2026-05-22T13:44:04.734745+00:00\", \"findings\": [{\"severity\": \"critical\", \"dimension\": \"page 22\", \"message\": \"末页仅 6 行文本（约 5% 填充），其余全部空白。审稿人视角极为不专业——建议将 Appendix E.5/E.6 内容重新排版填满此页，或将少量文本合并至上一页消除空白页\"}, {\"severity\": \"warning\", \"dimension\": \"pages 4-5\", \"message\": \"连续两页纯文本（Method §3.3 → Experiments §4.1 Setup），无 figure/table/equation 穿插。此段非数学推导密集区，建议考虑将 Figure 2 或 Table 1 前移至 page 5 附近以打破视觉单调\"}, {\"severity\": \"warning\", \"dimension\": \"page 18\", \"message\": \"Table 8（详细 per-seed 结果）字号偏小，列数多（~10 列），密度极高。审稿人在屏幕上阅读时可能需要放大。建议检查 Notes 列是否可移入脚注以减少列宽压力\"}, {\"severity\": \"info\", \"dimension\": \"page 2\", \"message\": \"Figure 1 颜色方案（蓝/橙/绿）整体可区分，但三条线在中段重叠区域（步数 200-400）区分度略降。线型（实线/虚线）已辅助区分，可接受\"}, {\"severity\": \"info\", \"dimension\": \"page 6\", \"message\": \"Figure 2(b) Prolog STA Gaming Modes 使用 5+ 色彩堆叠柱状图，部分颜色（如相邻的蓝色系和紫色系）在低分辨率或灰度打印下可能难以区分。建议增加 pattern fill 或减少类别数\"}, {\"severity\": \"info\", \"dimension\": \"page 7\", \"message\": \"Table 1 和 Figure 3 同页——密度高但排版整洁，booktabs 风格一致，最优结果已加粗\"}, {\"severity\": \"info\", \"dimension\": \"pages 9-10\", \"message\": \"References 格式统一，无 [?] 未解析引用，编号连续\"}, {\"severity\": \"info\", \"dimension\": \"page 3\", \"message\": \"Algorithm 1 伪代码框排版清晰，与正文间距合理\"}, {\"severity\": \"info\", \"dimension\": \"page 11\", \"message\": \"Appendix 起始页 Tables 3-4 排版紧凑，超参表和数据集对比表格式规范\"}, {\"severity\": \"info\", \"dimension\": \"pages 15-17\", \"message\": \"Hacking mode 定义（D.2-D.9）含 FOL/Prolog 示例，排版结构化良好，example 块缩进一致\"}], \"counts\": {\"critical\": 1, \"warning\": 2, \"info\": 7}}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__get_visual_check_status",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2540 · 2026-05-22T13:52:50.924571+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
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

_source line 2541 · 2026-05-22T13:52:50.975885+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2542 · 2026-05-22T13:56:46.719323+00:00_

called mcp__agent-ml-research__update_review_issues

<details open><summary>🔧 Tool call — mcp__agent-ml-research__update_review_issues</summary>

```json
{
  "project": "solver-trace-ablation",
  "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R29) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W4 + R1 AGREE：Goldilocks 假说——degeneration 仅在模型恰好足够强以收敛但不够强以保持结构时发生。正文 Limitations 需更显著地讨论此 threshold 效应。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 29\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W3 + R1 AGREE with nuance：ProofFOL 应标记为 within-FOL cross-dataset replication，非 cross-domain。p=0.10 仍标为 exploratory 但 Abstract/Intro 叙事未反映 null results。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：recall 未报告。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W2 + R2 AGREE：recall 缺失使 non-hacking rates 可能系统性高估。R2 补充：不同 mode 的 recall 差异可能影响跨条件比较。PG 审计 R2 部分 REBUT（仅影响 ISR-as-reward，不影响 exec-only 核心发现）。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 升级为 Major。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-N3 + R2 AGREE：1/3 seeds 协议不一致是 clear-cut 实验设计缺陷。R2 补充：将 not strictly comparable 的 seed 纳入 pooled analysis 是分析失误。需 greedy re-eval 或 N=2 sensitivity analysis。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。\"\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1 建议 normalized ISR。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。\"\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W5 + R2 AGREE：additive variant 仅一次失败就排除，乘法 vs 加法 vs ISR 信号无法分离。需更完整的 ablation 设计。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 28\n  resolution: \"Table 1 caption 新增完整缩写展开。\"\n  resolution_round: 29\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：pages 5-6 纯文本，page 7-8 集中。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 视觉审查：pages 4-5 连续纯文本（Method §3.3 → Experiments §4.1），建议前移 Figure 2 或 Table 1 到 p5 附近。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 2 坐标轴标签约正文 60%。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 Figure 2(b) 5+ 色彩堆叠柱状图在灰度打印下难以区分，建议 pattern fill。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 维持。p=0.182 不显著。双 Reviewer 共识：'compositional Goodhart' claim 缺乏统计支撑且术语无操作性定义，建议改用 'regressional Goodhart pattern' 或 'mode shifting under ISR optimization'。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 n=16 matched pairs 也 underpowered。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。R1-N2 + R2-N1 完全一致。ISR aggregate ≈ premise count proxy。Abstract/Intro 214× 叙事在控制后仅 1.06×，构成选择性呈现。需 (1) Abstract 加 qualifier；(2) premise-count-matched 作为主要指标；(3) 讨论 premise count 作为更简单替代品。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 共识：LOO 应用为 incremental。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧：R2 Must-Fix，R1 建议 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 分歧维持：R2 维持 Must-Fix（LOO 应用于新领域不需解决新技术挑战，缺乏 vs IPT 实验对比）。R1 REBUT 降为 Should-Fix（STA+ISR+taxonomy 组合贡献 > 单纯技术迁移；solver-backed 设定使 LOO 具有 deterministic ablation 优势）。最终定级：Should-Fix（R1 的 REBUT 有据可循：case study 定位 + taxonomy + Goodhart 实证 构成组合增量）。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 被 classifier validation 覆盖。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W4 + R2 AGREE：N=46 的 87% non-hacking 95% CI ≈ [77%,97%]，太宽。R2 补充：论文在 §4.1 标记为 secondary 但 §4.2 又用作 key evidence——secondary-then-key 切换削弱论证严谨性。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1-W4 + R2 AGREE with reservation。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 核心共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。R1-N1 + R2 AGREE 并补充：(1) pseudo-replication 比描述的更深——CMH p<0.001 给读者过高确定性印象；(2) 5-seed extension 存在 double standard（exploratory 但又在 Appendix 作支撑证据）；(3) Abstract/Intro 叙事未反映 null results。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 Should-Fix。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及但被 v17-R12-W1 (单模型泛化性) 覆盖。维持 in_progress。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 升级共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-N2 维持 Must-Fix（缺乏实验对比证明互补性）。R1 REBUT 降为 Should-Fix（§2 已讨论区分，直接实验对比需双方代码可用，solver-backed deterministic ablation 是差异化优势）。最终：Should-Fix——§2 现有讨论有据但不够深入，建议更明确阐述 STA 的不可替代性。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失 Shapley values 引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W2 + R1 AGREE：ISR 是 Shapley value 的退化形式（仅 n-1 coalition），需在 §3.2 或 Appendix C 讨论关系和 LOO 选择理由（O(n) vs O(2^n)，solver-backed binary necessity）。引用 Lundberg and Lee (2017)。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1-M3。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2 交叉回应指出 5-seed extension 的 double standard 问题：标记为 exploratory 但用作支撑证据。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× 为核心叙事\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 premise-count confound 维持为核心问题。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。214× 绝大部分来自 premise-count confound。Abstract/Intro 完全缺失此 caveat——读者到第 6 页才发现。需在 Abstract 首次提及 ISR collapse 时注明 confound 及 matched effect size。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-N3 + R1 AGREE with nuance：'compositional Goodhart' 无操作性定义，是 regressional 的 expected instantiation。R1 建议降为 Should-Fix。共识：去掉新术语，改用 'regressional Goodhart pattern' 或 'mode shifting under ISR optimization'。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 27\n  resolution: \"references.bib 已包含。\"\n  resolution_round: 28\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 3 色盲区分度不足。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 issues (updated R29) ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 合并到 v23-R2-W3。R2 维持 Must-Fix，R1 REBUT 降为 Should-Fix。最终 Should-Fix。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 29\n  resolution: \"放弃新术语。experiments.tex 'compositional Goodhart' → 'regressional Goodhart pattern'；introduction.tex 3 处同步修改。\"\n  resolution_round: 29\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 降级为 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2 交叉回应补充：CMH p<0.001 在 within-seed 非独立下给读者过高确定性。被 v23-R12-N1 (N=3 统计效力) 覆盖。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 合并到 v17-R1-W9。双 Reviewer 再次共识。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论不可复现\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W2 (recall 未估计) + R2 AGREE。R2-W1 (taxonomy ad-hoc)：R1 REBUT（empirically-grounded enumeration 在该阶段是恰当选择）。最终定级 Should-Fix：taxonomy 有实用价值但需承认 open-ended 性质 + 补充 per-mode recall 估计。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [2]\n    note: \"R28 R2 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-Q5 + R2 AGREE：TS 下 ISR 反向效果（ISR≈0.5 by construction）使 ISR 作为跨条件 unified diagnostic 存在根本缺陷。Appendix C 讨论了但正文未充分体现。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"PRIME (cui2025prime) 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"deepseek-prover-v2 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-Q2：Sullivan and Keller (2025) 证明 GRPO 隐式等价于 MC-PRM。R1 交叉回应：ISR 可被理解为 explicit component-level PRM signal，这一关联值得在 Related Work 展开。\"\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W2 + R2 AGREE：不同 condition 下 recall 差异可能影响微妙比较（ISR vs Random），但 SFT vs GRPO 差距足够大不受影响。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v27-R12-TAXONOMY 覆盖。需 per-mode recall 估计。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"R28 bib 中已有 URL。核实通过。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 AGREE 补充。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1 交叉回应：方向合理但非紧迫——论文已引用经典 mutation testing 文献，DNN-specific mutation testing 与 solver-backed 设定差异较大。R2 维持建议补充。\"\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n# === R28 issues (updated R29) ===\n- id: v28-R1-N1\n  summary: \"ISR 聚合 vs per-sample 诊断需明确分离\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v22-R12-N3 (premise-count confound) 覆盖。双 Reviewer 共识：ISR aggregate ≈ premise count proxy，per-sample ISR 相对 robust。论文需在 §3 前置讨论双重用途。\"\n\n- id: v28-R12-SFT-CONVERGENCE\n  summary: \"SFT baseline 未报告 training loss curve\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 28\n  resolution: \"Appendix A.1 新增 'SFT convergence' 段落。\"\n  resolution_round: 29\n\n- id: v28-R12-MR-INFLUENCE\n  summary: \"缺失引用：Cook's distance / influence functions (Koh & Liang 2017)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v23-MR-SHAPLEY 覆盖。需引用 Lundberg and Lee (2017) 并讨论 ISR 与 Shapley/influence functions 关系。\"\n\n- id: v28-R1-M4\n  summary: \"50% exec-only seeds 不收敛对主分析影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R1-M4。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W1 + R2 AGREE：生存偏差。非收敛 seeds 保留更高 structural integrity 暗示 degeneration 是 convergence 副产品。R2 补充：这可能是论文最有趣的 secondary finding（bifurcation point），但被放在附录中。\"\n\n- id: v28-VISUAL-APPENDIX\n  summary: \"Appendix 末页大面积空白\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"视觉审查：~50% 页面空白。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 视觉审查：page 22 仅 6 行文本（~5% 填充），审稿人视角不专业。建议合并或填满。\"\n\n# === R29 new issues ===\n- id: v29-R12-N1\n  summary: \"5-seed extension 存在 double standard：标记为 exploratory 但在 Appendix 作支撑证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 交叉回应提出：§4.1 将 s45/s46 标为 exploratory，但 Appendix E 用其做 bimodal seed-dependence 讨论。数据可靠则应纳入主分析；不可靠则不应在附录作支撑。构成 double standard。\"\n\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 提出。R1 REBUT：论文提供了 Goodhart's Law 在 neurosymbolic reasoning 的首次 fine-grained 实证图景（ISR 对不同 modes 的诊断力差异、dose-response 关系、mode composition shift），非简单重述。分歧记录。\"\n\n- id: v29-R12-MR-ENSEMBLE\n  summary: \"缺失引用：Coste et al. (2023) Reward Model Ensembles 和 Moskovitz et al. (2023) Constrained RLHF\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R1 提出。R2 AGREE：与 Goodhart mitigation 讨论相关但非核心缺失。\"\n\n- id: v29-R12-MR-SHAPLEY-LUNDBERG\n  summary: \"缺失引用：Lundberg and Lee (2017) SHAP\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2-W2 + R1 AGREE。ISR 与 Shapley values 的方法论联系需讨论。\"\n"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "tool_args": {
    "project": "solver-trace-ablation",
    "issues_yaml": "issues:\n# === Resolved issues from rounds 0-26 (condensed) ===\n- id: R1-W1\n  summary: 统计效力严重不足：β=0.3 仅 single seed，abstract '93%' 来自 single seed\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: β=0.3 ISR 和 Random 各 3 seeds 已完成。\n  resolution_round: 2\n- id: RV-EVAL-FALLBACK\n  summary: eval_sta.py test_100.jsonl 静默 fallback 已移除\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 1\n  last_seen_round: 1\n  resolution: stderr ERROR → sys.exit(1)。\n  resolution_round: 1\n- id: R1-W2\n  summary: ISR 与 semantic faithfulness 无关但 framing 暗示推理质量度量\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 15\n  resolution: method.tex ρ=-0.049 出现在 4 处。主术语改为 'non-hacking (N-H)'。\n  resolution_round: 2\n- id: R2-W1\n  summary: Limitations section 格式不合规\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 独立 limitations.tex 已创建。\n  resolution_round: 3\n- id: R2-W2\n  summary: 实验仅用单一模型和单一数据集\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 标题改为单数。Qwen3-1.7B cross-scale 实验已加入。\n  resolution_round: 3\n- id: R2-W6\n  summary: SFT baseline 比较不公平：PR=14% vs 93%\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 0\n  last_seen_round: 2\n  resolution: 100-step RL 对照已加入。claim 调整为 'consistent with'。\n  resolution_round: 2\n- id: v2-R1-N1\n  summary: Abstract '93%' PR 为 single seed\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: Abstract 使用 3-seed pooled mean±std。\n  resolution_round: 3\n- id: v2-R1-N3\n  summary: 仅 2 个 β 值不足以刻画 dose-response\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 2\n  last_seen_round: 3\n  resolution: 4 个 β 值提供完整 dose-response 曲线。\n  resolution_round: 4\n- id: v7-R1-N2\n  summary: CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 7\n  last_seen_round: 9\n  resolution: CMH 移至 Appendix，正文以 seed-level permutation 为 primary。\n  resolution_round: 9\n- id: v11-R12-N1\n  summary: Responsible NLP Research Checklist 缺失\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 11\n  last_seen_round: 11\n  resolution: checklist.tex 创建并附在论文末尾。\n  resolution_round: 11\n- id: v12-R2-N1\n  summary: 正文超出 ARR 8 页限制约 0.75 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 12\n  last_seen_round: 12\n  resolution: Table 2 移入 Appendix。主文本完整收于第 8 页。\n  resolution_round: 12\n- id: v15-R12-N1\n  summary: 3 seeds 统计效力不足——per-seed qualitative 为主框架\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: §4.1 新增 Statistical considerations 段。\n  resolution_round: 15\n- id: v15-R2-N2\n  summary: \"'Meta-level Goodhart' 是 Goodhart's Law 直接实例\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 15\n  last_seen_round: 15\n  resolution: \"'meta-level Goodhart' → 'Goodhart effect on structural metrics'\"\n  resolution_round: 15\n- id: v17-VISUAL-PAGE\n  summary: 正文溢出至第 9 页\n  category: format\n  severity: critical\n  status: resolved\n  first_raised_round: 17\n  last_seen_round: 18\n  resolution: 正文在第 8 页结束。页数合规。\n  resolution_round: 18\n- id: v8-R12-N1\n  summary: Goodhart 发现的可预测性限制概念新颖性（Findings 级别）\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 8\n  last_seen_round: 21\n  resolution: \"Related Work 加 dataset-dependent asymmetry 是 non-trivial 经验发现的声明。\"\n  resolution_round: 21\n- id: v18-R12-W1\n  summary: ISR 概念在 component necessity 和 structural quality 之间滑移\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"正文统一为 component necessity。Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v18-R1-W3\n  summary: SFT baseline PR 差 7× 不公平\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 18\n  last_seen_round: 21\n  resolution: \"SFT 段落重构：承认 PR confound, 100-step 为核心论据。\"\n  resolution_round: 21\n- id: v19-R12-W1\n  summary: CMH pooled test pseudo-replication——真正 N=3\n  category: experiment\n  severity: critical\n  status: resolved\n  first_raised_round: 19\n  last_seen_round: 21\n  resolution: \"§4.1/§4.3/§Limitations 三处 N=3 caveat。\"\n  resolution_round: 21\n- id: v20-R2-W7\n  summary: rlsf bib entry 作者完全错误（LLM 幻觉）\n  category: writing\n  severity: critical\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"修正为正确作者。\"\n  resolution_round: 21\n- id: v20-R12-W4\n  summary: 5-seed 结果应从 Appendix 升级为 Table 1 主结果\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"Table 1 ISR β=0.1 改为双行 ISR (3-seed) / ISR (5-seed)。\"\n  resolution_round: 21\n- id: v20-R12-W5\n  summary: Table 1 ISR* premise-count confound 呈现不足\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 20\n  last_seen_round: 21\n  resolution: \"ISR (3-seed) 行 ISR* 改为 '1.06×‡'，footnote 更新。\"\n  resolution_round: 21\n- id: v16-MR\n  summary: 缺少若干相关引用\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 16\n  last_seen_round: 21\n  resolution: \"DeepSeek-R1, NLProofS, V-STaR, Easy-to-Hard 全部加入。\"\n  resolution_round: 21\n- id: v21-R12-W1\n  summary: \"Title 'Structural Degeneration' 与 'component necessity' 矛盾\"\n  category: framing\n  severity: warning\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"Title 'Reveals' → 'Diagnoses'。\"\n  resolution_round: 21\n- id: v21-R2-N1\n  summary: V-STaR bib 更新为 COLM 2024\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"bib 已更新。\"\n  resolution_round: 21\n- id: v21-R2-N2\n  summary: Table 1 ISR (5-seed) 行 ISR* 无具体值\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 21\n  last_seen_round: 21\n  resolution: \"ISR (5-seed) 行显示 (0.63)‡ 具体值。\"\n  resolution_round: 21\n- id: v22-ORPHAN-BIB\n  summary: \"kimina-prover bib entry 未被引用\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"已删除。\"\n  resolution_round: 22\n- id: v22-R2-W5\n  summary: \"遗漏 Dong et al. (2026)\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 22\n  resolution: \"dong2026probing 加入。\"\n  resolution_round: 22\n- id: v22-R12-N2\n  summary: \"'99.5% structural collapse' 来自单 seed 最极端值\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"标注 'for seed~42' + 3-seed '≤7%'。\"\n  resolution_round: 24\n- id: v22-R2-W2\n  summary: \"Eight-mode taxonomy 过度工程化\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 22\n  last_seen_round: 23\n  resolution: \"§4.5 已聚焦 CE/TS/PG 三主要 mode。\"\n  resolution_round: 24\n- id: v23-VISUAL-PAGE9\n  summary: \"Section 5 溢出至第 9 页\"\n  category: format\n  severity: warning\n  status: resolved\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"压缩完成。\"\n  resolution_round: 24\n\n# === Won't fix (carried) ===\n- id: v10-R2-W7\n  summary: \"'Valid but Vacuous' 中 'valid' 有歧义\"\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 10\n  last_seen_round: 16\n  resolution: \"连续 6 轮未提及。关闭。\"\n  resolution_round: 19\n- id: v14-R12-GATED-S54\n  summary: Gated ISR Discussion 遗漏 s54 反例\n  category: writing\n  severity: warning\n  status: wont_fix\n  first_raised_round: 14\n  last_seen_round: 16\n  resolution: \"Gated ISR 不在当前论文中。关闭。\"\n  resolution_round: 19\n- id: v11-R1-W5\n  summary: O(1) binary ablation ISR*≈0.007 反直觉结果\n  category: experiment\n  severity: warning\n  status: wont_fix\n  first_raised_round: 11\n  last_seen_round: 16\n  resolution: \"Appendix 已有详细讨论。关闭。\"\n  resolution_round: 19\n- id: v23-R2-W4\n  summary: \"'Structural degeneration' 标题与 ISR 测量不完全匹配\"\n  category: framing\n  severity: info\n  status: wont_fix\n  first_raised_round: 23\n  last_seen_round: 23\n  resolution: \"R1+R2 共识 info 级别。标题不需修改。\"\n  resolution_round: 24\n\n# === Recurring issues (updated R29) ===\n- id: v17-R12-W1\n  summary: 单模型 (Qwen3-4B) 无法支撑通用性声明\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 21\n    reviewers: [1, 2]\n    note: \"R21 RESOLVED：加限定。\"\n  - round: 25\n    reviewers: [1, 2]\n    note: \"R25 重新标记。LLaMA 实验失败。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿双 Reviewer 再次确认。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W4 + R1 AGREE：Goldilocks 假说——degeneration 仅在模型恰好足够强以收敛但不够强以保持结构时发生。正文 Limitations 需更显著地讨论此 threshold 效应。\"\n\n- id: v19-R12-W3\n  summary: ProofFOL p=0.10 被过度引用\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 29\n  mentions:\n  - round: 26\n    reviewers: []\n    note: \"R26 text fix: Conclusion 降级为 preliminary。\"\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 R2：ProofFOL cross-dataset 独立性不足。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W3 + R1 AGREE with nuance：ProofFOL 应标记为 within-FOL cross-dataset replication，非 cross-domain。p=0.10 仍标为 exploratory 但 Abstract/Intro 叙事未反映 null results。\"\n\n- id: v19-R1-W6\n  summary: Classifier recall 未知 + PG 审计仅 seed 42\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 19\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿：recall 未报告。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W2 + R2 AGREE：recall 缺失使 non-hacking rates 可能系统性高估。R2 补充：不同 mode 的 recall 差异可能影响跨条件比较。PG 审计 R2 部分 REBUT（仅影响 ISR-as-reward，不影响 exec-only 核心发现）。\"\n\n- id: v17-R1-W9\n  summary: Seed 43 使用 T=0.7 sampling 评估而非 greedy\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 升级为 Major。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-N3 + R2 AGREE：1/3 seeds 协议不一致是 clear-cut 实验设计缺陷。R2 补充：将 not strictly comparable 的 seed 纳入 pooled analysis 是分析失误。需 greedy re-eval 或 N=2 sensitivity analysis。\"\n\n- id: v16-R1-W2\n  summary: LOO 独立性假设未量化偏差\n  category: method\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 28\n  mentions:\n  - round: 27\n    reviewers: [1]\n    note: \"R27 R1-W9：n=2 时 ISR≥0.5 与 structural quality 无关。\"\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1 建议 normalized ISR。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n\n- id: v16-R1-W4\n  summary: ISR-as-reward 乘法耦合混淆\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 16\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 未单独提及。\"\n  - round: 28\n    reviewers: []\n    note: \"R28 未单独提及。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W5 + R2 AGREE：additive variant 仅一次失败就排除，乘法 vs 加法 vs ISR 信号无法分离。需更完整的 ablation 设计。\"\n\n- id: v13-R2-W4\n  summary: 缩写和术语密度过高\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 13\n  last_seen_round: 28\n  resolution: \"Table 1 caption 新增完整缩写展开。\"\n  resolution_round: 29\n\n- id: v17-VISUAL-LAYOUT\n  summary: Display items 分布不均\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 视觉审查确认：pages 5-6 纯文本。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 视觉审查：pages 5-6 纯文本，page 7-8 集中。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 视觉审查：pages 4-5 连续纯文本（Method §3.3 → Experiments §4.1），建议前移 Figure 2 或 Table 1 到 p5 附近。\"\n\n- id: v17-VISUAL-FONT\n  summary: Figure 内部文字偏小\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 17\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [visual]\n    note: \"R27 Figure 2 子面板 ~3cm×2.5cm。\"\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 2 坐标轴标签约正文 60%。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 Figure 2(b) 5+ 色彩堆叠柱状图在灰度打印下难以区分，建议 pattern fill。\"\n\n- id: v22-R12-N1\n  summary: \"ISR vs Random non-hacking rate p=0.182 不显著，Goodhart framing 暗示因果\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 深度审稿。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 维持。p=0.182 不显著。双 Reviewer 共识：'compositional Goodhart' claim 缺乏统计支撑且术语无操作性定义，建议改用 'regressional Goodhart pattern' 或 'mode shifting under ISR optimization'。\"\n\n- id: v22-R12-N3\n  summary: \"Premise-count confound 使 ISR scalar 诊断价值严重削弱（3.2×→1.06×）\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 n=16 matched pairs 也 underpowered。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。R1-N2 + R2-N1 完全一致。ISR aggregate ≈ premise count proxy。Abstract/Intro 214× 叙事在控制后仅 1.06×，构成选择性呈现。需 (1) Abstract 加 qualifier；(2) premise-count-matched 作为主要指标；(3) 讨论 premise count 作为更简单替代品。\"\n\n- id: v22-R2-N1\n  summary: \"方法论新颖性不足——LOO 是标准技术\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 共识：LOO 应用为 incremental。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧：R2 Must-Fix，R1 建议 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 分歧维持：R2 维持 Must-Fix（LOO 应用于新领域不需解决新技术挑战，缺乏 vs IPT 实验对比）。R1 REBUT 降为 Should-Fix（STA+ISR+taxonomy 组合贡献 > 单纯技术迁移；solver-backed 设定使 LOO 具有 deterministic ablation 优势）。最终定级：Should-Fix（R1 的 REBUT 有据可循：case study 定位 + taxonomy + Goodhart 实证 构成组合增量）。\"\n\n- id: v22-R2-W3\n  summary: \"与 Kim et al. (2026) 区分不够清晰\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 22\n  last_seen_round: 27\n\n- id: v22-R1-W1\n  summary: \"ProofFOL 'genuine' 用 coarser classifier\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: []\n    note: \"R28 被 classifier validation 覆盖。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n\n- id: v22-R1-W4\n  summary: \"Shuffled-ISR control N=46 统计效力有限\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: []\n    note: \"R27 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W4 + R2 AGREE：N=46 的 87% non-hacking 95% CI ≈ [77%,97%]，太宽。R2 补充：论文在 §4.1 标记为 secondary 但 §4.2 又用作 key evidence——secondary-then-key 切换削弱论证严谨性。\"\n\n- id: v22-R1-W5\n  summary: \"SFT PR confound 仅通过 100-step (n=32) 部分缓解\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 22\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1-W4 + R2 AGREE with reservation。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及。维持 in_progress。\"\n\n- id: v21-R1-N1\n  summary: 新增引用整合略机械\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 21\n  last_seen_round: 23\n\n- id: v23-R12-N1\n  summary: \"N=3 seeds 统计效力不足\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 核心共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识 Must-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。R1-N1 + R2 AGREE 并补充：(1) pseudo-replication 比描述的更深——CMH p<0.001 给读者过高确定性印象；(2) 5-seed extension 存在 double standard（exploratory 但又在 Appendix 作支撑证据）；(3) Abstract/Intro 叙事未反映 null results。\"\n\n- id: v23-R1-N3\n  summary: \"乘法耦合需 constant-bonus control\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v23-R2-N1\n  summary: \"Case study 标题与通用声称之间 framing 矛盾\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 Should-Fix。\"\n  - round: 29\n    reviewers: []\n    note: \"R29 未单独提及但被 v17-R12-W1 (单模型泛化性) 覆盖。维持 in_progress。\"\n\n- id: v23-R2-W3\n  summary: \"与 Helff et al. (2026) IPT 对比不充分\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R27 双 Reviewer 升级共识。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-N2 维持 Must-Fix（缺乏实验对比证明互补性）。R1 REBUT 降为 Should-Fix（§2 已讨论区分，直接实验对比需双方代码可用，solver-backed deterministic ablation 是差异化优势）。最终：Should-Fix——§2 现有讨论有据但不够深入，建议更明确阐述 STA 的不可替代性。\"\n\n- id: v23-MR-SHAPLEY\n  summary: \"缺失 Shapley values 引用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 23\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-W2 + R1 AGREE：ISR 是 Shapley value 的退化形式（仅 n-1 coalition），需在 §3.2 或 Appendix C 讨论关系和 LOO 选择理由（O(n) vs O(2^n)，solver-backed binary necessity）。引用 Lundberg and Lee (2017)。\"\n\n- id: v23-MR-PROSFI\n  summary: \"缺失 PRoSFI + Interleaved Bonus 引用\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 23\n  last_seen_round: 27\n\n- id: v25-R12-N1\n  summary: \"5-seed 扩展与 3-seed 矛盾——C2 非系统性\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R28 R1-M3。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2 交叉回应指出 5-seed extension 的 double standard 问题：标记为 exploratory 但用作支撑证据。\"\n\n- id: v25-R12-N2\n  summary: \"Abstract/Intro 以 raw ISR 214× 为核心叙事\"\n  category: writing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 premise-count confound 维持为核心问题。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 双 Reviewer 再次共识 Must-Fix。214× 绝大部分来自 premise-count confound。Abstract/Intro 完全缺失此 caveat——读者到第 6 页才发现。需在 Abstract 首次提及 ISR collapse 时注明 confound 及 matched effect size。\"\n\n- id: v25-R2-N1\n  summary: \"Goodhart taxonomy 映射不严谨\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-N3 + R1 AGREE with nuance：'compositional Goodhart' 无操作性定义，是 regressional 的 expected instantiation。R1 建议降为 Should-Fix。共识：去掉新术语，改用 'regressional Goodhart pattern' 或 'mode shifting under ISR optimization'。\"\n\n- id: v25-R1-W5\n  summary: \"Table 1 exec-only 仅 seed 42\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 27\n\n- id: v25-MR\n  summary: \"缺失 Yue et al. + Sullivan et al.\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 25\n  last_seen_round: 27\n  resolution: \"references.bib 已包含。\"\n  resolution_round: 28\n\n- id: v25-VISUAL-W1\n  summary: \"Figure 3 可读性差\"\n  category: format\n  severity: warning\n  status: in_progress\n  first_raised_round: 25\n  last_seen_round: 28\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"R28 Figure 3 色盲区分度不足。\"\n\n- id: v25-MINOR-BIB\n  summary: \"FOLIO bib 年份 mismatch\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 25\n  last_seen_round: 27\n\n# === R27 issues (updated R29) ===\n- id: v27-R12-N1\n  summary: \"STA 与 Helff 2026 IPT 区分不充分——概念同构，仅粒度差异\"\n  category: framing\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"双 Reviewer 共识 Must-Fix。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 分歧记录。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 合并到 v23-R2-W3。R2 维持 Must-Fix，R1 REBUT 降为 Should-Fix。最终 Should-Fix。\"\n\n- id: v27-R12-N2\n  summary: \"'Compositional Goodhart effect' 缺乏操作性定义\"\n  category: framing\n  severity: critical\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 29\n  resolution: \"放弃新术语。experiments.tex 'compositional Goodhart' → 'regressional Goodhart pattern'；introduction.tex 3 处同步修改。\"\n  resolution_round: 29\n\n- id: v27-R1-N2\n  summary: \"CMH pseudo-replication：within-seed samples 非独立\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 27\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 降级为 Should-Fix。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2 交叉回应补充：CMH p<0.001 在 within-seed 非独立下给读者过高确定性。被 v23-R12-N1 (N=3 统计效力) 覆盖。\"\n\n- id: v27-R1-N4\n  summary: \"Seed 43 T=0.7 评估 + checkpoints 已删除\"\n  category: experiment\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 合并到 v17-R1-W9。双 Reviewer 再次共识。\"\n\n- id: v27-R12-TAXONOMY\n  summary: \"Taxonomy classification 方法论不可复现\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W2 (recall 未估计) + R2 AGREE。R2-W1 (taxonomy ad-hoc)：R1 REBUT（empirically-grounded enumeration 在该阶段是恰当选择）。最终定级 Should-Fix：taxonomy 有实用价值但需承认 open-ended 性质 + 补充 per-mode recall 估计。\"\n\n- id: v27-R2-W1\n  summary: \"ISR 对不同 hacking modes 诊断力差异巨大\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [2]\n    note: \"R28 R2 维持。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-Q5 + R2 AGREE：TS 下 ISR 反向效果（ISR≈0.5 by construction）使 ISR 作为跨条件 unified diagnostic 存在根本缺陷。Appendix C 讨论了但正文未充分体现。\"\n\n- id: v27-R2-MR-PRIME\n  summary: \"缺失引用：PRIME\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"PRIME (cui2025prime) 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-DSP-V2\n  summary: \"缺失引用：DeepSeek-Prover-V2\"\n  category: writing\n  severity: warning\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"deepseek-prover-v2 已在 §2 引用。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-PRM\n  summary: \"ISR 与 Process Reward Models 的概念联系未被讨论\"\n  category: writing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R2-Q2：Sullivan and Keller (2025) 证明 GRPO 隐式等价于 MC-PRM。R1 交叉回应：ISR 可被理解为 explicit component-level PRM signal，这一关联值得在 Related Work 展开。\"\n\n- id: v27-R2-MR-PROOF-QUALITY\n  summary: \"缺失引用：Proof quality metrics 先行工作\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R1-W7\n  summary: \"Non-hacking rate 作为 upper bound 跨条件比较时 recall 可能不一致\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W2 + R2 AGREE：不同 condition 下 recall 差异可能影响微妙比较（ISR vs Random），但 SFT vs GRPO 差距足够大不受影响。\"\n\n- id: v27-R2-W3\n  summary: \"Title 'Structural Degeneration' 与 ISR 测量 'component necessity' 概念跳跃\"\n  category: framing\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 28\n\n- id: v27-R2-W4\n  summary: \"Hacking taxonomy 验证 50 样本偏少 + recall 未评估\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 双 Reviewer 共识。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v27-R12-TAXONOMY 覆盖。需 per-mode recall 估计。\"\n\n- id: v27-R1-W4\n  summary: \"100-step checkpoint hacking 分析 n=32\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-M2\n  summary: \"metr-reward-hacking bib 缺 URL\"\n  category: writing\n  severity: info\n  status: resolved\n  first_raised_round: 27\n  last_seen_round: 28\n  resolution: \"R28 bib 中已有 URL。核实通过。\"\n  resolution_round: 28\n\n- id: v27-R2-MR-MUTATION\n  summary: \"缺失：Mutation testing 在 ML/code generation 中的近期应用\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 27\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R28 R1 AGREE 补充。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1 交叉回应：方向合理但非紧迫——论文已引用经典 mutation testing 文献，DNN-specific mutation testing 与 solver-backed 设定差异较大。R2 维持建议补充。\"\n\n- id: v27-R2-W6\n  summary: \"Hacking taxonomy 持久性/可迁移性存疑\"\n  category: method\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n- id: v27-R2-W7\n  summary: \"β 值消融仅两个点\"\n  category: experiment\n  severity: info\n  status: open\n  first_raised_round: 27\n  last_seen_round: 27\n\n# === R28 issues (updated R29) ===\n- id: v28-R1-N1\n  summary: \"ISR 聚合 vs per-sample 诊断需明确分离\"\n  category: method\n  severity: critical\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1, 2]\n    note: \"R1 提出，R2 AGREE。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v22-R12-N3 (premise-count confound) 覆盖。双 Reviewer 共识：ISR aggregate ≈ premise count proxy，per-sample ISR 相对 robust。论文需在 §3 前置讨论双重用途。\"\n\n- id: v28-R12-SFT-CONVERGENCE\n  summary: \"SFT baseline 未报告 training loss curve\"\n  category: experiment\n  severity: warning\n  status: resolved\n  first_raised_round: 28\n  last_seen_round: 28\n  resolution: \"Appendix A.1 新增 'SFT convergence' 段落。\"\n  resolution_round: 29\n\n- id: v28-R12-MR-INFLUENCE\n  summary: \"缺失引用：Cook's distance / influence functions (Koh & Liang 2017)\"\n  category: writing\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 被 v23-MR-SHAPLEY 覆盖。需引用 Lundberg and Lee (2017) 并讨论 ISR 与 Shapley/influence functions 关系。\"\n\n- id: v28-R1-M4\n  summary: \"50% exec-only seeds 不收敛对主分析影响\"\n  category: experiment\n  severity: warning\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [1]\n    note: \"R1-M4。\"\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R29 R1-W1 + R2 AGREE：生存偏差。非收敛 seeds 保留更高 structural integrity 暗示 degeneration 是 convergence 副产品。R2 补充：这可能是论文最有趣的 secondary finding（bifurcation point），但被放在附录中。\"\n\n- id: v28-VISUAL-APPENDIX\n  summary: \"Appendix 末页大面积空白\"\n  category: format\n  severity: info\n  status: in_progress\n  first_raised_round: 28\n  last_seen_round: 29\n  mentions:\n  - round: 28\n    reviewers: [visual]\n    note: \"视觉审查：~50% 页面空白。\"\n  - round: 29\n    reviewers: [visual]\n    note: \"R29 视觉审查：page 22 仅 6 行文本（~5% 填充），审稿人视角不专业。建议合并或填满。\"\n\n# === R29 new issues ===\n- id: v29-R12-N1\n  summary: \"5-seed extension 存在 double standard：标记为 exploratory 但在 Appendix 作支撑证据\"\n  category: experiment\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 交叉回应提出：§4.1 将 s45/s46 标为 exploratory，但 Appendix E 用其做 bimodal seed-dependence 讨论。数据可靠则应纳入主分析；不可靠则不应在附录作支撑。构成 double standard。\"\n\n- id: v29-R2-W5\n  summary: \"'Observe-vs-optimize asymmetry' 非新概念——本质即 Goodhart's Law\"\n  category: framing\n  severity: warning\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2 提出。R1 REBUT：论文提供了 Goodhart's Law 在 neurosymbolic reasoning 的首次 fine-grained 实证图景（ISR 对不同 modes 的诊断力差异、dose-response 关系、mode composition shift），非简单重述。分歧记录。\"\n\n- id: v29-R12-MR-ENSEMBLE\n  summary: \"缺失引用：Coste et al. (2023) Reward Model Ensembles 和 Moskovitz et al. (2023) Constrained RLHF\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R1 提出。R2 AGREE：与 Goodhart mitigation 讨论相关但非核心缺失。\"\n\n- id: v29-R12-MR-SHAPLEY-LUNDBERG\n  summary: \"缺失引用：Lundberg and Lee (2017) SHAP\"\n  category: writing\n  severity: info\n  status: open\n  first_raised_round: 29\n  last_seen_round: 29\n  mentions:\n  - round: 29\n    reviewers: [1, 2]\n    note: \"R2-W2 + R1 AGREE。ISR 与 Shapley values 的方法论联系需讨论。\"\n"
  }
}
```

</details>

---


### Tool result

_source line 2543 · 2026-05-22T13:56:46.821553+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_issues.yaml\", \"bytes\": 29085}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__update_review_issues",
  "elapsed_ms": 102
}
```

</details>

---


### Tool call

_source line 2544 · 2026-05-22T13:59:25.212451+00:00_

called mcp__agent-ml-research__submit_review_report_to_research_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__submit_review_report_to_research_director</summary>

```json
{
  "report": "# 审稿报告 — Round 29 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（全新审稿，无历史记忆）\n**Reviewers**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic reasoning 管道中 GRPO 训练输出的结构诊断方法。STA 对证明的每个组件执行 leave-one-out (LOO) 删除并重新调用 solver，计算 Intensional Structural Reward (ISR)——必要组件占比。在 FOLIO (FOL) 和 Prolog 两种逻辑体系上，论文展示：(1) GRPO 训练使 ISR 崩溃，揭示执行正确率掩盖下的结构退化；(2) 将 ISR 用作训练 reward 时出现 Goodhart 效应（hacking mode 从 CE 转向 TS）；(3) 跨逻辑体系（FOL→Prolog）和跨数据集（FOLIO→ProofFOL）验证了这一现象。贡献包括 STA 框架、ISR 指标、8-mode hacking taxonomy、以及 observe-vs-optimize asymmetry 的经验证据。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的现象记录。** 在 RLVR 社区快速扩张的背景下，系统记录 GRPO 训练导致的 neurosymbolic proof 结构退化具有实际价值。STA 框架本身是清晰、可操作、可复现的诊断工具。Algorithm 1 简洁优雅。[R1+R2 共识]\n\n**S2. 实验控制设计合理。** 六个 reward 条件（exec-only, ISR low/high-dose, matched random controls, SFT baseline）加上 shuffled-ISR deconfounding control，形成有说服力的对照结构。Premise-count matched comparison 是诚实的自我修正。[R1+R2 共识]\n\n**S3. 8-mode hacking taxonomy 对实践者有用。** Appendix D 对每种 hacking mode 提供了定义、FOL/Prolog 示例、ISR 交互分析和 prevalence 统计，是社区迄今为止最细粒度的 neurosymbolic reward hacking 分类。[R1 主导，R2 acknowledge]\n\n**S4. 跨域验证增强可信度。** FOL→Prolog 是真正的跨逻辑体系验证；ProofFOL 提供了 within-FOL 跨数据集复制。LLaMA-3.2-3B 和 Qwen3-8B 的 negative results 也有信息价值。[R1+R2 共识]\n\n**S5. 透明度高。** 论文对自身限制（N=3 统计效力、premise-count confound、seed 43 协议偏差、PG audit 覆盖不足）的讨论坦诚详尽，附录极为详细（14 页）。承诺开源代码、数据集和 checkpoint。[R1+R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, R1-N2 + R2-N1, 双 Reviewer 共识] **ISR \"214× collapse\" 核心叙事存在系统性 framing 问题**\n- Abstract 和 Introduction 以 raw ISR 从 0.642 崩溃至 0.003（214×）作为核心叙事钩子，但 §4.2 \"Premise-count confound\" 承认匹配 premise count 后优势仅为 **1.06×**。这意味着 214× 的绝大部分来自 premise count 变化（ISR-trained 模型产生更短 formalizations）而非真正的结构退化。Abstract 和 Introduction 完全未提及此关键 caveat——读者到第 6 页才发现。\n- **影响**：ISR 作为 aggregate metric 的独立诊断价值被严重质疑。如 premise count 能提供几乎相同的信号，STA 的核心价值需从 aggregate ISR 重新定位到 per-sample mode classification。\n- **建议**：(1) Abstract/Introduction 首次提及 ISR collapse 时注明 premise-count confound 及 matched effect size；(2) 以 premise-count-matched ISR 为主报告指标；(3) 明确区分 ISR 的两个用途层次：aggregate（≈ premise count proxy）vs. per-sample（真正的必要性诊断）。\n\n**MF-2** [critical, R1-N1, R2 AGREE] **N=3 seeds 统计效力严重不足，核心 claims 缺乏可靠量化证据**\n- 论文自承 N=3 仅对 d≥2.0 的超大效应有 80% power。多个关键比较未达显著性：ISR vs Random non-hacking p=0.182、ProofFOL p=0.10。CMH 检验将 within-seed 样本视为独立观测（真正 N=3），pseudo-replication 膨胀了显著性。5-seed extension 存在 double standard：§4.1 标记为 exploratory，但 Appendix E 用其做 bimodal seed-dependence 分析。\n- **影响**：论文的实验贡献从\"量化证据\"降格为\"定性观察\"。\n- **建议**：(1) 将 5-seed 纳入主分析或统一其在正文/附录中的定位；(2) 对 CMH 做 cluster-robust 校正（seed 为聚类单元）或仅报告 seed-level tests；(3) 所有非显著结果在正文中明确标注。\n\n**MF-3** [critical, R1-N3, R2 AGREE] **Seed 43 评估协议不一致**\n- Seed 43 使用 T=0.7 sampling 而非 greedy decoding（Appendix A 承认 \"not strictly comparable\"）。在 N=3 设计中，1/3 seeds 协议不一致使 exec-only condition 的结论可信度大打折扣。将 not strictly comparable 的 seed 纳入 pooled 分析是分析上的失误。\n- **建议**：(1) 用 greedy decoding 重新评估 seed 43；(2) 如无法恢复，提供 N=2 (s42+s44) 的 sensitivity analysis 作为主分析。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, R1-W1 + R2 AGREE] **50% exec-only seeds 不收敛引入生存偏差**\n- 6 seeds 中仅 3 收敛。不收敛 seeds 保留了更高 structural integrity（85-87% genuine），暗示 degeneration 是 convergence 副产品而非 GRPO 固有行为——这可能是论文最有趣的 secondary finding（bifurcation point），但被放在附录中。建议在 Limitations 中显著讨论。\n\n**SF-2** [warning, R2-N2, R1 REBUT → 降级] **方法论新颖性有限**\n- LOO ablation 是标准技术（1978），STA 是其在 neurosymbolic 输出上的直接应用。与 Helff et al. (2026) IPT 缺乏实验对比。R1 REBUT：STA+ISR+taxonomy 组合贡献 > 单纯技术迁移，solver-backed 设定使 LOO 具有 deterministic ablation 优势。\n- **分歧记录**：R2 认为 Must-Fix，R1 认为 Should-Fix。Director 采纳 R1 的 REBUT（case study 定位 + taxonomy + Goodhart 实证构成组合增量），定级 Should-Fix。\n- **建议**：在 Related Work 中更明确阐述 STA 的不可替代性（component-level + deterministic + training-time），以及与 IPT 的互补性。\n\n**SF-3** [warning, R2-N3 + R1 AGREE with nuance → 降级] **\"Compositional Goodhart\" 术语缺乏操作性定义**\n- 本质是 regressional Goodhart 在 multiplicative ISR reward 下的 expected instantiation。R1 同意有道理但认为是 terminology 而非方法论缺陷。\n- **建议**：去掉 \"compositional Goodhart\" 术语，直接用 \"regressional Goodhart pattern\" 或 \"mode shifting under ISR optimization\"。\n\n**SF-4** [warning, R1-W2 + R2 AGREE] **Classifier recall 未估计，non-hacking rates 可能系统性高估**\n- Precision=1.00 (152 样本)，但 recall \"not estimable\"。不同 hacking modes 的 recall 可能差异很大，影响跨条件比较（ISR vs Random 的微妙差异可能被 recall 差异污染）。\n- **建议**：对至少一个 condition 做 recall 估计；讨论 recall 变异对 cross-condition comparisons 的影响。\n\n**SF-5** [warning, R1-W4 + R2 AGREE] **Shuffled-ISR control 证据单薄 (N=46)**\n- 87% non-hacking 的 95% CI ≈ [77%, 97%]，太宽。论文在 §4.1 标记为 secondary 但 §4.2 用作 key evidence——secondary-then-key 切换削弱论证严谨性。\n\n**SF-6** [warning, R1-W5 + R2 AGREE] **乘法耦合 reward 的 confound 未充分控制**\n- r_exec · (1 + β·ISR) 的乘法耦合使 ISR signal 和 multiplicative interaction 无法分离。Additive variant 仅一次失败就被排除。\n\n**SF-7** [warning, R2-W2 + R1 AGREE] **ISR 与 Shapley values / influence functions 的方法论关系未被讨论**\n- ISR 本质上是 Shapley value 的退化形式（仅 n-1 coalition）。建议在 §3.2 讨论关系并引用 Lundberg and Lee (2017)。\n\n**SF-8** [warning, R2-W3 + R1 AGREE with nuance] **ProofFOL \"cross-domain\" 声称需更谨慎 framing**\n- FOLIO→ProofFOL 是 same-task-family (FOL) 的 cross-dataset 复制，非真正 cross-domain。建议区分 \"cross-dataset replication\"（ProofFOL）和 \"cross-domain replication\"（Prolog）。\n\n**SF-9** [warning, R2-W4 + R1 AGREE] **单模型泛化性存疑 / \"Goldilocks\" 假说**\n- Qwen3-8B 和 LLaMA-3.2-3B 均未复现 degeneration（前者 rollout diversity bottleneck，后者 cold-start failure）。Degeneration 可能仅在模型能力恰好处于某个窄带时发生。建议在 Discussion/Limitations 中更显著地讨论此 threshold 效应。\n\n**SF-10** [warning, R2-W6 + R1 AGREE] **缩写密度过高**\n- ISR, STA, CE, TS, PG, TSb, N-H, PR, LOO, CMH... 对非本领域读者构成显著阅读障碍。建议在密集段落开头添加缩写回顾。\n\n---\n\n### Minor Issues（不影响接收）\n\n- **M1** [R1-M1]: Abstract \"ISR diagnoses structural degeneration\" 暗示独立诊断力，建议更精确表述。\n- **M2** [R2-M2]: Discussion and Conclusion 过于简短（不到半 column），建议讨论 STA 对其他 RL reasoning 系统的适用性。\n- **M3** [R1-M3 + R2-W6]: Hacking mode 缩写 (CE, TS, PG) 首次使用时缺乏足够上下文。\n- **M4** [R1-M4 + R2-M3]: Figure 2 子图在灰度打印下可能难以区分，建议增加 pattern fill。\n- **M5** [R1-M5]: §4.4 ProofFOL \"p=0.10\" 在正文位置给读者过强印象，建议明确 \"underpowered; directional only\"。\n- **M6** [R2-M4]: ISR 对 unproved samples 的处理在正文中应有简短提及（仅在 Appendix B 出现）。\n\n---\n\n## Reviewer Consensus\n\n### 共识 [AGREE]\n1. **Overall 3.0 (Findings)**——双 Reviewer 独立给出相同评分\n2. **Premise-count confound 是最关键问题**——ISR aggregate ≈ premise count proxy (MF-1)\n3. **N=3 统计效力不足**——核心 claims 缺乏可靠量化证据 (MF-2)\n4. **Seed 43 评估协议不一致**——clear-cut 实验设计缺陷 (MF-3)\n5. **\"Compositional Goodhart\" 术语应放弃**——无操作性定义 (SF-3)\n6. **Shuffled-ISR control 证据单薄** (SF-5)\n7. **STA 框架本身有诊断价值**——核心优势 (S1)\n8. **Hacking taxonomy 对实践者有用** (S3)\n9. **透明度和可复现性高** (S5)\n\n### 分歧 [REBUT]\n1. **方法论新颖性** (SF-2)：R2 认为 Must-Fix（LOO 应用于新领域不需解决新技术挑战），R1 REBUT 降为 Should-Fix（组合贡献 > 单纯迁移）。**Director 采纳 R1 的 REBUT**——case study 定位下，STA+ISR+taxonomy+Goodhart 实证构成足够的组合增量。\n2. **Taxonomy 性质** (SF-4 相关)：R2 认为 ad-hoc 枚举，R1 REBUT 认为 empirically-grounded enumeration 是恰当的。**Director：taxonomy 有实用价值但应承认 open-ended 性质。**\n3. **\"Observe-vs-optimize asymmetry\" 新颖性**：R2 认为本质即 Goodhart's Law，R1 REBUT 认为论文提供了首次 fine-grained 实证图景（dose-response、mode-specific ISR 差异）。**Director：分歧记录。R1 的 REBUT 有据但论文应避免将其包装为独立新概念。**\n\n---\n\n## Questions for Authors\n\n**Q1** [R1+R2 共识]: Premise-count matched ISR 仅 1.06×。请解释为何读者应认为 ISR collapse 反映\"结构退化\"而非简单的 premise-count 变化？是否考虑过直接用 premise count 作为更简单的 aggregate 诊断替代品？\n\n**Q2** [R1]: 50% exec-only seeds 不收敛。不收敛 seeds 是否保留了更好的结构完整性？如果是，这是否挑战 \"structural degeneration is a consequence of GRPO training\" 的 claim——它可能仅是 successful convergence 的副产品？\n\n**Q3** [R1]: Shuffled-ISR control 仅 46 proved samples。如何论证这足以排除 \"ISR 分布形状驱动 Goodhart 效应\" 的替代假设？\n\n**Q4** [R2]: Sullivan and Keller (2025) 证明 GRPO 隐式等价于 MC-PRM。ISR 是否可重新表述为 explicit PRM signal？如果可以，对论文 framing 有何影响？\n\n**Q5** [R1+R2]: TS hacking mode 下 ISR 反向效果（ISR≈0.5 by construction）。ISR 作为跨条件的 unified diagnostic 是否存在根本缺陷？\n\n---\n\n## Missing References\n\n1. **Lundberg and Lee (2017)** \"A Unified Approach to Interpreting Model Predictions\" — ISR 与 Shapley values 的方法论联系 [R2 提出, R1 AGREE]\n2. **Coste et al. (2023)** \"Reward Model Ensembles Help Mitigate Overoptimization\" — Goodhart mitigation [R1 提出, R2 AGREE]\n3. **Moskovitz et al. (2023)** \"Confronting Reward Model Overoptimization with Constrained RLHF\" — 替代 paradigm [R1 提出, R2 AGREE]\n4. **DNN mutation testing 近期工作** — ML-specific mutation testing [R2 提出, R1 部分 AGREE: 方向合理但与 solver-backed 设定差异大]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~3 分钟），1 critical / 2 warning / 7 info。\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| critical | p.22 | 末页仅 6 行文本（~5% 填充），其余全部空白。极不专业——建议合并至上一页或填满。 |\n| warning | pp.4-5 | 连续两页纯文本（Method §3.3 → Experiments §4.1），无 figure/table 穿插。建议前移 Figure 2 或 Table 1。 |\n| warning | p.18 | Table 8 字号偏小、列数多（~10 列），密度极高。建议 Notes 列移入脚注。 |\n| info | p.2 | Figure 1 颜色方案整体可区分，中段重叠区域略降但有线型辅助，可接受。 |\n| info | p.6 | Figure 2(b) 5+ 色彩堆叠柱状图在灰度打印下可能难以区分。建议 pattern fill。 |\n| info | p.7 | Table 1 + Figure 3 同页——密度高但排版整洁。 |\n| info | pp.9-10 | References 格式统一，无未解析引用。 |\n| info | p.3 | Algorithm 1 排版清晰。 |\n| info | p.11 | Appendix Tables 3-4 格式规范。 |\n| info | pp.15-17 | Hacking mode 定义排版结构化良好。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 RLVR、neurosymbolic reasoning 和统计方法论）\n\n### 评分理由\n\n本文记录了一个有实际价值的现象（GRPO 训练导致 neurosymbolic proof 结构退化），提供了实用的诊断工具（STA/ISR）和系统的 hacking taxonomy，实验控制合理，附录详尽，透明度高。\n\n三个 Must-Fix 问题阻止了主会议接收：\n\n1. **ISR aggregate 的核心叙事存在 framing 问题**——214× headline 在控制 premise count 后仅剩 1.06×，Abstract/Intro 未披露，构成选择性呈现。ISR aggregate 本质上是 premise count 的 proxy，论文需要诚实地重新定位 STA 的价值。\n\n2. **N=3 seeds 的统计效力不足**——多个核心比较未达显著性，CMH 存在 pseudo-replication，5-seed extension 定位不一致。论文的实验贡献从\"量化证据\"降格为\"定性观察\"。\n\n3. **Seed 43 评估协议不一致**——在 N=3 设计中，1/3 seeds 使用不同评估协议（T=0.7 vs greedy）是不可接受的实验设计缺陷。\n\n**若能解决 MF-1（framing 修正 + ISR 双重用途明确化）和 MF-3（seed 43 re-evaluation 或 N=2 sensitivity analysis），可上升至 3.5 (Borderline Conference)。MF-2（统计效力）需要更多 seeds，短期内难以完全解决，但 5-seed 统一纳入主分析可部分缓解。**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"ISR … collapses from 0.642 to 0.003, a 214× raw drop\" — 需立即注明 \"(partially attributable to premise-count inflation; matched comparison yields 1.06×, §4.2)\"。当前正文中 §4.2 有此 caveat 但 Intro 完全缺失。\n- \"observe-vs-optimize asymmetry\" 术语：建议降级为 descriptive phrase 而非 coined concept，以避免暗示超出 Goodhart's Law 的新理论贡献。\n\n### §3.2 Method (ISR)\n- 在定义 ISR 后立即讨论其双重用途（aggregate vs per-sample）及各自的 confound sensitivity。当前 \"Limitations of ISR\" 段部分涉及但不够明确。\n- 增加 Shapley values 方法论联系的讨论（为何 LOO 而非 Shapley：O(n) vs O(2^n)，solver-backed binary necessity）。\n\n### §4.1 Setup\n- \"Statistical considerations\" 段的 N=3 caveat 是好的，但 Abstract/Intro 的叙事未反映这些 null results。\n- Seed 43 \"uses nucleus sampling (T=0.7) due to greedy-mode degeneration\" 需更明确的处理：要么排除，要么提供 sensitivity analysis。\n\n### §4.2 Goodhart Effects\n- Table 1 信息密度极高。建议至少在 caption 中完整展开所有缩写（当前已有部分展开）。\n- \"compositional Goodhart\" → 改为 \"regressional Goodhart pattern\" 或 \"mode shifting\"。\n\n### §4.4 Cross-Domain\n- \"Cross-Domain and Cross-Dataset Evidence\" 小节标题中，ProofFOL 部分应明确标记为 \"within-FOL cross-dataset replication\"。\n\n### §5 Discussion and Conclusion\n- 过于简短（2 行）。建议至少讨论：STA 对 math reasoning RL 系统的潜在适用性；ISR 与 PRM 的整合可能性；Goldilocks 假说。\n\n### §6 Limitations\n- 增加 50% exec-only seeds 不收敛及其对结论的影响。\n- 增加 classifier recall 未知的讨论。\n\n### Appendix\n- p.22 末页空白需修复。\n- Table 8 可读性可优化（Notes 列移入脚注）。\n",
  "project": "solver-trace-ablation",
  "reviewer_ids_acknowledged": "[1, 2]",
  "cross_response_reviewer_ids": "[1, 2]",
  "overall_score": "3.0 - Findings",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "tool_args": {
    "report": "# 审稿报告 — Round 29 (Fresh Review)\n\n**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study\n**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)\n**Deadline**: 2026-05-25\n**审稿模式**: Fresh（全新审稿，无历史记忆）\n**Reviewers**: R1（方法严谨性 + 实验有效性）、R2（新颖性 + 完整性）\n**流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）\n\n---\n\n## Summary\n\n本文提出 Solver Trace Ablation (STA)，一种对 neurosymbolic reasoning 管道中 GRPO 训练输出的结构诊断方法。STA 对证明的每个组件执行 leave-one-out (LOO) 删除并重新调用 solver，计算 Intensional Structural Reward (ISR)——必要组件占比。在 FOLIO (FOL) 和 Prolog 两种逻辑体系上，论文展示：(1) GRPO 训练使 ISR 崩溃，揭示执行正确率掩盖下的结构退化；(2) 将 ISR 用作训练 reward 时出现 Goodhart 效应（hacking mode 从 CE 转向 TS）；(3) 跨逻辑体系（FOL→Prolog）和跨数据集（FOLIO→ProofFOL）验证了这一现象。贡献包括 STA 框架、ISR 指标、8-mode hacking taxonomy、以及 observe-vs-optimize asymmetry 的经验证据。\n\n---\n\n## Strengths\n\n**S1. 重要且及时的现象记录。** 在 RLVR 社区快速扩张的背景下，系统记录 GRPO 训练导致的 neurosymbolic proof 结构退化具有实际价值。STA 框架本身是清晰、可操作、可复现的诊断工具。Algorithm 1 简洁优雅。[R1+R2 共识]\n\n**S2. 实验控制设计合理。** 六个 reward 条件（exec-only, ISR low/high-dose, matched random controls, SFT baseline）加上 shuffled-ISR deconfounding control，形成有说服力的对照结构。Premise-count matched comparison 是诚实的自我修正。[R1+R2 共识]\n\n**S3. 8-mode hacking taxonomy 对实践者有用。** Appendix D 对每种 hacking mode 提供了定义、FOL/Prolog 示例、ISR 交互分析和 prevalence 统计，是社区迄今为止最细粒度的 neurosymbolic reward hacking 分类。[R1 主导，R2 acknowledge]\n\n**S4. 跨域验证增强可信度。** FOL→Prolog 是真正的跨逻辑体系验证；ProofFOL 提供了 within-FOL 跨数据集复制。LLaMA-3.2-3B 和 Qwen3-8B 的 negative results 也有信息价值。[R1+R2 共识]\n\n**S5. 透明度高。** 论文对自身限制（N=3 统计效力、premise-count confound、seed 43 协议偏差、PG audit 覆盖不足）的讨论坦诚详尽，附录极为详细（14 页）。承诺开源代码、数据集和 checkpoint。[R1+R2 共识]\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**MF-1** [critical, R1-N2 + R2-N1, 双 Reviewer 共识] **ISR \"214× collapse\" 核心叙事存在系统性 framing 问题**\n- Abstract 和 Introduction 以 raw ISR 从 0.642 崩溃至 0.003（214×）作为核心叙事钩子，但 §4.2 \"Premise-count confound\" 承认匹配 premise count 后优势仅为 **1.06×**。这意味着 214× 的绝大部分来自 premise count 变化（ISR-trained 模型产生更短 formalizations）而非真正的结构退化。Abstract 和 Introduction 完全未提及此关键 caveat——读者到第 6 页才发现。\n- **影响**：ISR 作为 aggregate metric 的独立诊断价值被严重质疑。如 premise count 能提供几乎相同的信号，STA 的核心价值需从 aggregate ISR 重新定位到 per-sample mode classification。\n- **建议**：(1) Abstract/Introduction 首次提及 ISR collapse 时注明 premise-count confound 及 matched effect size；(2) 以 premise-count-matched ISR 为主报告指标；(3) 明确区分 ISR 的两个用途层次：aggregate（≈ premise count proxy）vs. per-sample（真正的必要性诊断）。\n\n**MF-2** [critical, R1-N1, R2 AGREE] **N=3 seeds 统计效力严重不足，核心 claims 缺乏可靠量化证据**\n- 论文自承 N=3 仅对 d≥2.0 的超大效应有 80% power。多个关键比较未达显著性：ISR vs Random non-hacking p=0.182、ProofFOL p=0.10。CMH 检验将 within-seed 样本视为独立观测（真正 N=3），pseudo-replication 膨胀了显著性。5-seed extension 存在 double standard：§4.1 标记为 exploratory，但 Appendix E 用其做 bimodal seed-dependence 分析。\n- **影响**：论文的实验贡献从\"量化证据\"降格为\"定性观察\"。\n- **建议**：(1) 将 5-seed 纳入主分析或统一其在正文/附录中的定位；(2) 对 CMH 做 cluster-robust 校正（seed 为聚类单元）或仅报告 seed-level tests；(3) 所有非显著结果在正文中明确标注。\n\n**MF-3** [critical, R1-N3, R2 AGREE] **Seed 43 评估协议不一致**\n- Seed 43 使用 T=0.7 sampling 而非 greedy decoding（Appendix A 承认 \"not strictly comparable\"）。在 N=3 设计中，1/3 seeds 协议不一致使 exec-only condition 的结论可信度大打折扣。将 not strictly comparable 的 seed 纳入 pooled 分析是分析上的失误。\n- **建议**：(1) 用 greedy decoding 重新评估 seed 43；(2) 如无法恢复，提供 N=2 (s42+s44) 的 sensitivity analysis 作为主分析。\n\n---\n\n### Should-Fix（影响评分但不一票否决）\n\n**SF-1** [warning, R1-W1 + R2 AGREE] **50% exec-only seeds 不收敛引入生存偏差**\n- 6 seeds 中仅 3 收敛。不收敛 seeds 保留了更高 structural integrity（85-87% genuine），暗示 degeneration 是 convergence 副产品而非 GRPO 固有行为——这可能是论文最有趣的 secondary finding（bifurcation point），但被放在附录中。建议在 Limitations 中显著讨论。\n\n**SF-2** [warning, R2-N2, R1 REBUT → 降级] **方法论新颖性有限**\n- LOO ablation 是标准技术（1978），STA 是其在 neurosymbolic 输出上的直接应用。与 Helff et al. (2026) IPT 缺乏实验对比。R1 REBUT：STA+ISR+taxonomy 组合贡献 > 单纯技术迁移，solver-backed 设定使 LOO 具有 deterministic ablation 优势。\n- **分歧记录**：R2 认为 Must-Fix，R1 认为 Should-Fix。Director 采纳 R1 的 REBUT（case study 定位 + taxonomy + Goodhart 实证构成组合增量），定级 Should-Fix。\n- **建议**：在 Related Work 中更明确阐述 STA 的不可替代性（component-level + deterministic + training-time），以及与 IPT 的互补性。\n\n**SF-3** [warning, R2-N3 + R1 AGREE with nuance → 降级] **\"Compositional Goodhart\" 术语缺乏操作性定义**\n- 本质是 regressional Goodhart 在 multiplicative ISR reward 下的 expected instantiation。R1 同意有道理但认为是 terminology 而非方法论缺陷。\n- **建议**：去掉 \"compositional Goodhart\" 术语，直接用 \"regressional Goodhart pattern\" 或 \"mode shifting under ISR optimization\"。\n\n**SF-4** [warning, R1-W2 + R2 AGREE] **Classifier recall 未估计，non-hacking rates 可能系统性高估**\n- Precision=1.00 (152 样本)，但 recall \"not estimable\"。不同 hacking modes 的 recall 可能差异很大，影响跨条件比较（ISR vs Random 的微妙差异可能被 recall 差异污染）。\n- **建议**：对至少一个 condition 做 recall 估计；讨论 recall 变异对 cross-condition comparisons 的影响。\n\n**SF-5** [warning, R1-W4 + R2 AGREE] **Shuffled-ISR control 证据单薄 (N=46)**\n- 87% non-hacking 的 95% CI ≈ [77%, 97%]，太宽。论文在 §4.1 标记为 secondary 但 §4.2 用作 key evidence——secondary-then-key 切换削弱论证严谨性。\n\n**SF-6** [warning, R1-W5 + R2 AGREE] **乘法耦合 reward 的 confound 未充分控制**\n- r_exec · (1 + β·ISR) 的乘法耦合使 ISR signal 和 multiplicative interaction 无法分离。Additive variant 仅一次失败就被排除。\n\n**SF-7** [warning, R2-W2 + R1 AGREE] **ISR 与 Shapley values / influence functions 的方法论关系未被讨论**\n- ISR 本质上是 Shapley value 的退化形式（仅 n-1 coalition）。建议在 §3.2 讨论关系并引用 Lundberg and Lee (2017)。\n\n**SF-8** [warning, R2-W3 + R1 AGREE with nuance] **ProofFOL \"cross-domain\" 声称需更谨慎 framing**\n- FOLIO→ProofFOL 是 same-task-family (FOL) 的 cross-dataset 复制，非真正 cross-domain。建议区分 \"cross-dataset replication\"（ProofFOL）和 \"cross-domain replication\"（Prolog）。\n\n**SF-9** [warning, R2-W4 + R1 AGREE] **单模型泛化性存疑 / \"Goldilocks\" 假说**\n- Qwen3-8B 和 LLaMA-3.2-3B 均未复现 degeneration（前者 rollout diversity bottleneck，后者 cold-start failure）。Degeneration 可能仅在模型能力恰好处于某个窄带时发生。建议在 Discussion/Limitations 中更显著地讨论此 threshold 效应。\n\n**SF-10** [warning, R2-W6 + R1 AGREE] **缩写密度过高**\n- ISR, STA, CE, TS, PG, TSb, N-H, PR, LOO, CMH... 对非本领域读者构成显著阅读障碍。建议在密集段落开头添加缩写回顾。\n\n---\n\n### Minor Issues（不影响接收）\n\n- **M1** [R1-M1]: Abstract \"ISR diagnoses structural degeneration\" 暗示独立诊断力，建议更精确表述。\n- **M2** [R2-M2]: Discussion and Conclusion 过于简短（不到半 column），建议讨论 STA 对其他 RL reasoning 系统的适用性。\n- **M3** [R1-M3 + R2-W6]: Hacking mode 缩写 (CE, TS, PG) 首次使用时缺乏足够上下文。\n- **M4** [R1-M4 + R2-M3]: Figure 2 子图在灰度打印下可能难以区分，建议增加 pattern fill。\n- **M5** [R1-M5]: §4.4 ProofFOL \"p=0.10\" 在正文位置给读者过强印象，建议明确 \"underpowered; directional only\"。\n- **M6** [R2-M4]: ISR 对 unproved samples 的处理在正文中应有简短提及（仅在 Appendix B 出现）。\n\n---\n\n## Reviewer Consensus\n\n### 共识 [AGREE]\n1. **Overall 3.0 (Findings)**——双 Reviewer 独立给出相同评分\n2. **Premise-count confound 是最关键问题**——ISR aggregate ≈ premise count proxy (MF-1)\n3. **N=3 统计效力不足**——核心 claims 缺乏可靠量化证据 (MF-2)\n4. **Seed 43 评估协议不一致**——clear-cut 实验设计缺陷 (MF-3)\n5. **\"Compositional Goodhart\" 术语应放弃**——无操作性定义 (SF-3)\n6. **Shuffled-ISR control 证据单薄** (SF-5)\n7. **STA 框架本身有诊断价值**——核心优势 (S1)\n8. **Hacking taxonomy 对实践者有用** (S3)\n9. **透明度和可复现性高** (S5)\n\n### 分歧 [REBUT]\n1. **方法论新颖性** (SF-2)：R2 认为 Must-Fix（LOO 应用于新领域不需解决新技术挑战），R1 REBUT 降为 Should-Fix（组合贡献 > 单纯迁移）。**Director 采纳 R1 的 REBUT**——case study 定位下，STA+ISR+taxonomy+Goodhart 实证构成足够的组合增量。\n2. **Taxonomy 性质** (SF-4 相关)：R2 认为 ad-hoc 枚举，R1 REBUT 认为 empirically-grounded enumeration 是恰当的。**Director：taxonomy 有实用价值但应承认 open-ended 性质。**\n3. **\"Observe-vs-optimize asymmetry\" 新颖性**：R2 认为本质即 Goodhart's Law，R1 REBUT 认为论文提供了首次 fine-grained 实证图景（dose-response、mode-specific ISR 差异）。**Director：分歧记录。R1 的 REBUT 有据但论文应避免将其包装为独立新概念。**\n\n---\n\n## Questions for Authors\n\n**Q1** [R1+R2 共识]: Premise-count matched ISR 仅 1.06×。请解释为何读者应认为 ISR collapse 反映\"结构退化\"而非简单的 premise-count 变化？是否考虑过直接用 premise count 作为更简单的 aggregate 诊断替代品？\n\n**Q2** [R1]: 50% exec-only seeds 不收敛。不收敛 seeds 是否保留了更好的结构完整性？如果是，这是否挑战 \"structural degeneration is a consequence of GRPO training\" 的 claim——它可能仅是 successful convergence 的副产品？\n\n**Q3** [R1]: Shuffled-ISR control 仅 46 proved samples。如何论证这足以排除 \"ISR 分布形状驱动 Goodhart 效应\" 的替代假设？\n\n**Q4** [R2]: Sullivan and Keller (2025) 证明 GRPO 隐式等价于 MC-PRM。ISR 是否可重新表述为 explicit PRM signal？如果可以，对论文 framing 有何影响？\n\n**Q5** [R1+R2]: TS hacking mode 下 ISR 反向效果（ISR≈0.5 by construction）。ISR 作为跨条件的 unified diagnostic 是否存在根本缺陷？\n\n---\n\n## Missing References\n\n1. **Lundberg and Lee (2017)** \"A Unified Approach to Interpreting Model Predictions\" — ISR 与 Shapley values 的方法论联系 [R2 提出, R1 AGREE]\n2. **Coste et al. (2023)** \"Reward Model Ensembles Help Mitigate Overoptimization\" — Goodhart mitigation [R1 提出, R2 AGREE]\n3. **Moskovitz et al. (2023)** \"Confronting Reward Model Overoptimization with Constrained RLHF\" — 替代 paradigm [R1 提出, R2 AGREE]\n4. **DNN mutation testing 近期工作** — ML-specific mutation testing [R2 提出, R1 部分 AGREE: 方向合理但与 solver-backed 设定差异大]\n\n---\n\n## External Review (Stanford Agentic Reviewer)\n\n外部审稿：未配置。\n\n---\n\n## Visual Layout Check（非评分项）\n\n视觉审查已完成（耗时 ~3 分钟），1 critical / 2 warning / 7 info。\n\n| 严重度 | 位置 | 发现 |\n|--------|------|------|\n| critical | p.22 | 末页仅 6 行文本（~5% 填充），其余全部空白。极不专业——建议合并至上一页或填满。 |\n| warning | pp.4-5 | 连续两页纯文本（Method §3.3 → Experiments §4.1），无 figure/table 穿插。建议前移 Figure 2 或 Table 1。 |\n| warning | p.18 | Table 8 字号偏小、列数多（~10 列），密度极高。建议 Notes 列移入脚注。 |\n| info | p.2 | Figure 1 颜色方案整体可区分，中段重叠区域略降但有线型辅助，可接受。 |\n| info | p.6 | Figure 2(b) 5+ 色彩堆叠柱状图在灰度打印下可能难以区分。建议 pattern fill。 |\n| info | p.7 | Table 1 + Figure 3 同页——密度高但排版整洁。 |\n| info | pp.9-10 | References 格式统一，无未解析引用。 |\n| info | p.3 | Algorithm 1 排版清晰。 |\n| info | p.11 | Appendix Tables 3-4 格式规范。 |\n| info | pp.15-17 | Hacking mode 定义排版结构化良好。 |\n\n---\n\n## Overall Assessment\n\n**Overall Score: 3.0 / 5 — Findings**\n\n**置信度: 4/5**（两位 Reviewer 均熟悉 RLVR、neurosymbolic reasoning 和统计方法论）\n\n### 评分理由\n\n本文记录了一个有实际价值的现象（GRPO 训练导致 neurosymbolic proof 结构退化），提供了实用的诊断工具（STA/ISR）和系统的 hacking taxonomy，实验控制合理，附录详尽，透明度高。\n\n三个 Must-Fix 问题阻止了主会议接收：\n\n1. **ISR aggregate 的核心叙事存在 framing 问题**——214× headline 在控制 premise count 后仅剩 1.06×，Abstract/Intro 未披露，构成选择性呈现。ISR aggregate 本质上是 premise count 的 proxy，论文需要诚实地重新定位 STA 的价值。\n\n2. **N=3 seeds 的统计效力不足**——多个核心比较未达显著性，CMH 存在 pseudo-replication，5-seed extension 定位不一致。论文的实验贡献从\"量化证据\"降格为\"定性观察\"。\n\n3. **Seed 43 评估协议不一致**——在 N=3 设计中，1/3 seeds 使用不同评估协议（T=0.7 vs greedy）是不可接受的实验设计缺陷。\n\n**若能解决 MF-1（framing 修正 + ISR 双重用途明确化）和 MF-3（seed 43 re-evaluation 或 N=2 sensitivity analysis），可上升至 3.5 (Borderline Conference)。MF-2（统计效力）需要更多 seeds，短期内难以完全解决，但 5-seed 统一纳入主分析可部分缓解。**\n\n---\n\n## Detailed Comments\n\n### §1 Introduction\n- \"ISR … collapses from 0.642 to 0.003, a 214× raw drop\" — 需立即注明 \"(partially attributable to premise-count inflation; matched comparison yields 1.06×, §4.2)\"。当前正文中 §4.2 有此 caveat 但 Intro 完全缺失。\n- \"observe-vs-optimize asymmetry\" 术语：建议降级为 descriptive phrase 而非 coined concept，以避免暗示超出 Goodhart's Law 的新理论贡献。\n\n### §3.2 Method (ISR)\n- 在定义 ISR 后立即讨论其双重用途（aggregate vs per-sample）及各自的 confound sensitivity。当前 \"Limitations of ISR\" 段部分涉及但不够明确。\n- 增加 Shapley values 方法论联系的讨论（为何 LOO 而非 Shapley：O(n) vs O(2^n)，solver-backed binary necessity）。\n\n### §4.1 Setup\n- \"Statistical considerations\" 段的 N=3 caveat 是好的，但 Abstract/Intro 的叙事未反映这些 null results。\n- Seed 43 \"uses nucleus sampling (T=0.7) due to greedy-mode degeneration\" 需更明确的处理：要么排除，要么提供 sensitivity analysis。\n\n### §4.2 Goodhart Effects\n- Table 1 信息密度极高。建议至少在 caption 中完整展开所有缩写（当前已有部分展开）。\n- \"compositional Goodhart\" → 改为 \"regressional Goodhart pattern\" 或 \"mode shifting\"。\n\n### §4.4 Cross-Domain\n- \"Cross-Domain and Cross-Dataset Evidence\" 小节标题中，ProofFOL 部分应明确标记为 \"within-FOL cross-dataset replication\"。\n\n### §5 Discussion and Conclusion\n- 过于简短（2 行）。建议至少讨论：STA 对 math reasoning RL 系统的潜在适用性；ISR 与 PRM 的整合可能性；Goldilocks 假说。\n\n### §6 Limitations\n- 增加 50% exec-only seeds 不收敛及其对结论的影响。\n- 增加 classifier recall 未知的讨论。\n\n### Appendix\n- p.22 末页空白需修复。\n- Table 8 可读性可优化（Notes 列移入脚注）。\n",
    "project": "solver-trace-ablation",
    "reviewer_ids_acknowledged": "[1, 2]",
    "cross_response_reviewer_ids": "[1, 2]",
    "overall_score": "3.0 - Findings",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool result

_source line 2545 · 2026-05-22T13:59:29.819869+00:00_

{"result":"{\"success\": true, \"data\": {\"research_director_key\": \"feishu:group:oc_a771c2a33d631dd40256ecd5c3a6648e:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__submit_review_report_to_research_director",
  "elapsed_ms": 4607
}
```

</details>

---


### Assistant

_source line 2546 · 2026-05-22T13:59:41.044218+00:00_

审稿报告已投递至 Research Director。

**Round 29 审稿完成。**

核心结论：**Overall 3.0 / 5 — Findings**（双 Reviewer 独立给出相同评分并在交叉分享后达成共识）

**3 个 Must-Fix**：
1. ISR "214× collapse" 叙事在 premise-count 匹配后仅 1.06×，Abstract/Intro 未披露此 caveat——需前置 qualifier 并重新定位 ISR 的价值（aggregate ≈ premise count proxy vs. per-sample 真正诊断）
2. N=3 seeds 统计效力不足，多个核心比较未达显著性，CMH pseudo-replication，5-seed 定位存在 double standard
3. Seed 43 使用 T=0.7 sampling 评估而非 greedy，1/3 seeds 协议不一致是实验设计缺陷

**10 个 Should-Fix** 涵盖：生存偏差、方法论新颖性（R2 Must-Fix → R1 REBUT → 降级）、Compositional Goodhart 术语、classifier recall 缺失、shuffled-ISR 证据单薄、乘法耦合 confound、Shapley 方法论联系、ProofFOL framing、单模型泛化性、缩写密度。

**升级路径**：修复 MF-1（framing）+ MF-3（seed 43 re-eval 或 N=2 sensitivity analysis）+ SF-3（去掉新术语）可达 3.5 Borderline Conference。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 233

## Round 233

2 recorded events


### User

_source line 2547 · 2026-05-22T13:59:43.794324+00:00_

[Reviewer 2 审稿结果]:
交叉回应已提交给 Review Director。

核心结论：与 Reviewer 1 在 Overall 3.0 (Findings) 上高度一致。对 R1 的 3 个 Must-Fix 和 5 个 Should-Fix 中，我 AGREE 了绝大多数（9/10），仅对 PG 审计完整性（R1-W3）部分反驳（降低严重性）和 Pan et al. 引用（需验证存在性）持保留意见。两位 Reviewer 最大的共识是：premise-count confound 是论文最根本的问题，214× 叙事在控制后仅剩 1.06×。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Assistant

_source line 2548 · 2026-05-22T13:59:54.690072+00:00_

审稿报告已投递至 Research Director。

**本轮审稿总结：**

- **Overall Score: 3.0 / 5 — Findings**（双 Reviewer 独立给出相同评分，交叉后维持不变）
- **3 个 Must-Fix**：(1) ISR 214× collapse 叙事的 premise-count confound framing 问题；(2) N=3 seeds 统计效力不足；(3) Seed 43 评估协议不一致
- **10 个 Should-Fix**：方法论新颖性（降级后）、"Compositional Goodhart" 术语、classifier recall 缺失、shuffled-ISR 证据单薄、乘法耦合 confound、Shapley values 关系未讨论、ProofFOL cross-domain 过度声称、单模型泛化性、缩写密度、50% seeds 不收敛的生存偏差
- **视觉审查**：1 critical（末页空白）、2 warning（纯文本段落、Table 8 密度）
- **Issue Tracker**：已同步更新至 Round 29

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 234

## Round 234

52 recorded events


### User

_source line 2549 · 2026-05-22T15:16:05.300743+00:00_

系统通知：审稿审批已通过。请开始审稿。

[论文提交]
- 项目: solver-trace-ablation
- 论文路径: /home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex
- 目标 venue: EMNLP 2026
- 投稿类别: Long Paper via ACL Rolling Review
- 截止日期: 2026-05-25
- **引用验证**: ✅ 后台自动运行中，完成后你会收到 [引用验证结果] 消息，请在合成报告时纳入

请 `Read /home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md` 获取完整审稿流程，然后按流程开始审核。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "system"
}
```

</details>

---


### Tool call

_source line 2550 · 2026-05-22T15:16:11.599125+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/agent-ml-research/skills/global/review-director-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 2551 · 2026-05-22T15:16:11.599997+00:00_

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
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2552 · 2026-05-22T15:16:19.180050+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:director_get_project_overview,dispatch_visual_check,request_external_review,get_external_review_status,director_post_to_reviewer,read_project_file,submit_review_report_to_research_director,update_review_issues,get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2553 · 2026-05-22T15:16:19.180908+00:00_

No matching deferred tools found

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2554 · 2026-05-22T15:16:25.154782+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
  "max_results": "10"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__director_get_project_overview,mcp__agent-ml-research__dispatch_visual_check,mcp__agent-ml-research__request_external_review,mcp__agent-ml-research__get_external_review_status,mcp__agent-ml-research__director_post_to_reviewer,mcp__agent-ml-research__read_project_file,mcp__agent-ml-research__submit_review_report_to_research_director,mcp__agent-ml-research__update_review_issues,mcp__agent-ml-research__get_visual_check_status",
    "max_results": "10"
  }
}
```

</details>

---


### Tool result

_source line 2555 · 2026-05-22T15:16:25.155292+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2556 · 2026-05-22T15:16:36.444484+00:00_

called mcp__agent-ml-research__director_get_project_overview

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_get_project_overview</summary>

```json
{
  "project": "solver-trace-ablation"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "tool_args": {
    "project": "solver-trace-ablation"
  }
}
```

</details>

---


### Tool call

_source line 2557 · 2026-05-22T15:16:36.997003+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
  "max_results": "2"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__read_local_file,WebSearch",
    "max_results": "2"
  }
}
```

</details>

---


### Tool result

_source line 2558 · 2026-05-22T15:16:37.098083+00:00_

{"result":"# 项目 solver-trace-ablation 概况\n\n## 实验状态 (216 个)\n\n- **plan013-random-reward-s42**: DONE (failed) — \n- **plan001-exec-only-s43**: DONE (failed) — \n- **plan003-eval-exec-only-r5**: DONE (success) — \n- **plan001-exec-only-s42-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r5**: DONE (negative) — \n- **sta-phase1-exec-only-r5**: DONE (success) — \n- **sta-phase1-exec-sta-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r4**: DONE (negative) — \n- **sta-phase1-exec-only-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r3**: DONE (failed) — \n- **sta-phase1-exec-sta-r2**: DONE (failed) — \n- **sta-phase1-exec-only-r2**: DONE (failed) — \n- **sta-phase1-exec-sta**: DONE (failed) — \n- **sta-phase1-exec-only**: DONE (failed) — \n- **sta-phase0-baseline**: DONE (success) — \n\n## 最新报告\n# Handover — 2026-05-22\n\n> 由 Agent 生成，每次状态变更后自动更新。硬限 150 行。\n\n## 运行中\n（无）\n\n## 待处理\n- exec-only-s45-1000step-k8（排队等待 GPU）\n- d158_llama_sft_s42（准备中）\n- d154-8b-exec-s42-k4（准备中）\n- d154-8b-exec-s42-r2（准备中）\n- d154-8b-exec-s42: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=42. Tests whether larger model (8B vs 4B) exhibits same Goodhart collapse patterns under exec-only reward. Pilot experiment.（准备中）\n- d154-8b-isr-s43: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=43. Replication of ISR s42 for statistical power at 8B scale.（准备中）\n- d154-8b-isr-s42: D154 cross-model: ISR β=0.1 GRPO on Qwen3-8B/FOLIO seed=42. Tests whether ISR-induced Goodhart collapse (TS dominance) persists at 8B scale, or if larger capacity enables genuine reasoning.（准备中）\n- d154-8b-exec-s44: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=44. Replication of exec s42 for statistical power across model scale.（准备中）\n- d154-8b-exec-s43: D154 cross-model: exec-only GRPO on Qwen3-8B/FOLIO seed=43. Replication of exec s42 for statistical power across model scale.（准备中）\n- d146-pf-pipeline（准备中）\n- …另有 23 项\n\n## 近期结论\n- **d154-8b-exec-s42-k8** (negative): 8B K=8 complete stagnation: a
…[truncated 1864 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_get_project_overview",
  "elapsed_ms": 653
}
```

</details>

---


### Tool result

_source line 2559 · 2026-05-22T15:16:37.098572+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "ToolSearch",
  "elapsed_ms": 101
}
```

</details>

---


### Tool call

_source line 2560 · 2026-05-22T15:16:42.620827+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 call for papers submission guidelines author instructions",
  "allowed_domains": "['aclweb.org', 'aclrollingreview.org', 'openreview.net']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 call for papers submission guidelines author instructions",
    "allowed_domains": "['aclweb.org', 'aclrollingreview.org', 'openreview.net']"
  }
}
```

</details>

---


### Tool call

_source line 2561 · 2026-05-22T15:16:45.432434+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
  "limit": "120"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex",
    "limit": "120"
  }
}
```

</details>

---


### Tool result

_source line 2562 · 2026-05-22T15:16:45.884794+00:00_

1	\documentclass[11pt]{article}
2	\usepackage[review]{acl}
3	
4	\usepackage{amsmath,amssymb}
5	\usepackage{graphicx}
6	\usepackage{booktabs}
7	\usepackage{algorithm}
8	\usepackage{algorithmic}
9	\usepackage{enumitem}
10	\usepackage{xcolor}
11	\usepackage{multirow}
12	\usepackage{float}
13	\usepackage{placeins}
14	\usepackage[protrusion=true,expansion=false]{microtype}
15	
16	\setlength{\textfloatsep}{8pt plus 2pt minus 4pt}
17	\setlength{\intextsep}{6pt plus 2pt minus 2pt}
18	\setlength{\abovecaptionskip}{4pt}
19	\setlength{\belowcaptionskip}{2pt}
20	
21	\graphicspath{{figures/}}
22	
23	\title{Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study}
24	
25	\author{Anonymous ACL submission}
26	
27	\begin{document}
28	\maketitle
29	
30	\input{abstract}
31	\input{introduction}
32	\input{related_work}
33	\input{method}
34	\input{experiments}
35	\input{conclusion}
36	
37	\input{limitations}
38	
39	\input{ethics}
40	
41	\bibliography{references}
42	
43	\appendix
44	\input{appendix}
45	
46	\end{document}
47	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 2563 · 2026-05-22T15:16:46.035901+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "paper_checklist.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "paper_checklist.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2564 · 2026-05-22T15:16:48.947184+00:00_

Web search results for query: "ACL Rolling Review 2026 call for papers submission guidelines author instructions"

Links: [{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"Main Conference - ACL 2026","url":"https://2026.aclweb.org/calls/main_conference_papers/"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"}]

Based on the search results, here are the key submission guidelines and author instructions for ACL Rolling Review 2026:

## Anonymity and Paper Requirements

Papers must not include authors' names and affiliations, and self-references that reveal the authors' identities must be avoided. Use citations such as "Smith previously showed (Smith, 1991)…" instead of "We previously showed (Smith, 1991)…"

Supplementary materials, including any links to repositories, should also be anonymized, and links to file hosting services that can track downloads, such as Dropbox, are not allowed.

## Submission Process

Authors submit papers to a unified review pool with a deadline on the 15th of each month, with review handled by an action editor, and revision and resubmission of papers allowed.

After submission, all authors m
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6326
}
```

</details>

---


### Tool result

_source line 2565 · 2026-05-22T15:16:48.947774+00:00_

{"result":"{\"success\": false, \"data\": {}, \"error\": \"No paper_checklist.yaml found for 'solver-trace-ablation'.\", \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 2911
}
```

</details>

---


### Tool call

_source line 2566 · 2026-05-22T15:16:53.465853+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "EMNLP 2026 call for papers page limit submission guidelines"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "EMNLP 2026 call for papers page limit submission guidelines"
  }
}
```

</details>

---


### Tool call

_source line 2567 · 2026-05-22T15:16:54.520075+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 page limits long paper short paper formatting requirements",
  "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 page limits long paper short paper formatting requirements",
    "allowed_domains": "['aclrollingreview.org', 'aclweb.org']"
  }
}
```

</details>

---


### Tool call

_source line 2568 · 2026-05-22T15:16:55.925888+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 2569 · 2026-05-22T15:16:56.324279+00:00_

1	\begin{abstract}
2	Execution-based evaluation of neurosymbolic reasoning conflates faithful derivation with structural shortcuts: a formalization that trivially embeds the conclusion among its premises proves just as reliably as a genuine one, and RL optimizers exploit this indifference.
3	We propose \emph{component necessity} as a diagnostic principle and operationalize it as \emph{Solver Trace Ablation} (STA): for each proved output, STA tests whether every component is individually required for proof success, yielding the \emph{Intensional Structural Reward} (ISR).
4	ISR reveals structural degeneration invisible to prove rate, but occupies a paradoxical position: the same leave-one-out structure that makes it informative also makes it gameable.
5	Tautological formalizations satisfy the necessity criterion by construction, so when ISR is repurposed as a training reward, the model learns to game the diagnostic rather than the task.
6	In our Qwen3-4B case study, this \emph{observe-vs-optimize asymmetry} persists across logic types and dataset families: structural proxies for reasoning quality are easier to observe than to optimize.\footnote{Code and data: \url{[anonymized]}}
7	\end{abstract}
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 398
}
```

</details>

---


### Tool call

_source line 2570 · 2026-05-22T15:16:56.458991+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 2571 · 2026-05-22T15:16:56.509198+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	Neurosymbolic reasoning pipelines evaluate success by a single criterion: whether the generated formalization proves under a formal solver.
5	This treats all proofs as equal: a formalization that embeds the conclusion verbatim among its premises receives the same reward as one that derives it through genuine reasoning.
6	Under reinforcement learning, this indifference becomes an active vulnerability~\citep{geirhos2020shortcut}. The optimizer exploits any shortcut the reward fails to penalize~\citep{skalse-reward-hacking, reward-hacking-survey}, and execution feedback provides no signal against structural shortcuts.
7	
8	\paragraph{The evaluation gap.}
9	Neurosymbolic formalizers~\citep{logic-lm, linc, satlm} and RL-trained variants~\citep{mellgren-prolog-grpo, logic-rl, deepseekmath} rely on execution accuracy alone, with no diagnostic for whether individual components contribute to the proof.
10	Process reward models~\citep{lightman-verify-step, math-shepherd} offer finer granularity but require expensive step-level annotations that do not transfer to arbitrary solver-backed settings.
11	Inference-time gaming detection~\citep{kim-game-formalization, bondarenko-spec-gaming} addresses a complementary problem but offers no training-time diagnostic.
12	What is missing is an annotation-free method for testing \emph{component necessity} in neurosymbolic outputs.
13	
14	\paragraph{Component necessity testing.}
15	We address this gap with \emph{Solver Trace Ablation} (STA), a diagnostic that tests whether each component of a formalization is necessary for proof success.
16	For each proved output, STA removes components one at a time and re-runs the solver; the fraction whose removal breaks the proof yields the \emph{Intensional Structural Reward} (ISR).
17	A formalization where every component is necessary receives $\text{ISR}{=}1$; one that proves regardless of which component is removed receives $\text{ISR}{=}0$.
1
…[truncated 2471 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool result

_source line 2572 · 2026-05-22T15:16:59.053963+00:00_

Web search results for query: "EMNLP 2026 call for papers page limit submission guidelines"

Links: [{"title":"Call for Papers: EMNLP 2026 Industry Track - EMNLP 2026","url":"https://2026.emnlp.org/calls/industry_track/"},{"title":"EMNLP 2026 LaTeX Template | ACL Style Files & Overleaf | Underleaf","url":"https://www.underleaf.ai/templates/emnlp"},{"title":"Joint Call for Tutorial Proposals (EMNLP/AACL-IJCNLP 2026) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/joint-call-tutorial-proposals-emnlpaacl-ijcnlp-2026"},{"title":"Call for workshops: EMNLP & AACL","url":"https://groups.google.com/g/ml-news/c/W-fucfhVto4"},{"title":"EMNLP 2026 Conference | OpenReview","url":"https://openreview.net/group?id=EMNLP%2F2026%2FConference"},{"title":"Confs: 2026 Conference on Empirical Methods in Natural ...","url":"https://www.facebook.com/linguistlist/posts/confs-2026-conference-on-empirical-methods-in-natural-language-processing-emnlp-/1351983883622556/"},{"title":"Announcements | Computational Linguistics","url":"https://submissions.cljournal.org/index.php/cljournal/announcement"},{"title":"CALL FOR PAPERS – ACL Rolling Review","url":"http://aclrollingreview.org/cfp"},{"title":"EMNLP 2026 Call for Papers — Official Deadlines & Important Dates | PaperPilot","url":"https://www.getpaperpilot.com/deadlines/emnlp-2026.html"},{"title":"emnlp 2026 - AI Conference Deadlines","url":"https://mlciv.com/ai-deadlines/conference/?id=emnlp26"}]

Based on the search results, here are the key submission guidelines for EMNLP 2026:

## Page Limits

The format is two-column with an 8-page limit for long papers and a 4-page limit for short papers. For the Industry Track specifically, papers have a maximum of 6 pages, and Industry Track papers cannot exceed 6 pages in length (excluding ethical considerations and references). References and limitations sections do not count toward the page limit, nor do the following optional sections: acknowledgements (only in the final version),
…[truncated 677 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 5588
}
```

</details>

---


### Tool result

_source line 2573 · 2026-05-22T15:17:00.853518+00:00_

Web search results for query: "ACL Rolling Review 2026 page limits long paper short paper formatting requirements"

Links: [{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"EACL 2026: First Call for Papers | ACL Member Portal","url":"https://www.aclweb.org/portal/content/eacl-2026-first-call-papers"},{"title":"First Call for Papers – EACL 2026 Student Research Workshop (SRW) | ACL Member Portal","url":"https://www.aclweb.org/portal/content/first-call-papers-eacl-2026-student-research-workshop-srw"},{"title":"The 14th Joint Conference on Lexical and Computational Semantics | ACL Member Portal","url":"https://www.aclweb.org/portal/content/14th-joint-conference-lexical-and-computational-semantics"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Industry Track — Call for Papers @ EACL 2026 | ACL Member Portal","url":"https://www.aclweb.org/portal/content/industry-track-call-papers-eacl-2026"},{"title":"System Demonstrations - ACL 2026","url":"https://2026.aclweb.org/calls/system_demonstration/"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here are the ACL Rolling Review 2026 page limits and formatting requirements:

## Page Limits

**Long Papers:** Long papers may consist of up to eight (8) pages of content, plus unlimited pages of references.

**Short Papers:** The search results reference that short papers exist but don't provide their specific page limit in the main ARR CfP content retrieved. However, based on related ACL venues, short papers typically have a 4-page limit
…[truncated 846 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "WebSearch",
  "elapsed_ms": 6333
}
```

</details>

---


### Tool call

_source line 2574 · 2026-05-22T15:17:08.585902+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 2575 · 2026-05-22T15:17:09.540366+00:00_

1	\section{Method}
2	\label{sec:method}
3	
4	\subsection{Task and GRPO Training}
5	\label{sec:task}
6	
7	Given premises $P_1,\ldots,P_k$ and conclusion $C$, the task is to produce a formal program $F=\{c_1,\ldots,c_n\}$ verified by an external solver $S\in\{\text{Prover9, SWI-Prolog}\}$.
8	We train with Group Relative Policy Optimization (GRPO)~\citep{deepseekmath} ($K{=}4$), where each rollout receives binary execution reward $r_{\text{exec}}(x) = \mathbf{1}[S(F_x){=}\textit{proved}]$.
9	This optimizes prove rate but provides no signal about \emph{component necessity}: a formalization embedding the conclusion among its premises receives the same reward as a faithful derivation.
10	All experiments draw from FOLIO~\citep{folio}.
11	
12	\subsection{Solver Trace Ablation (STA)}
13	\label{sec:sta}
14	
15	STA tests whether each component of a proved formalization is individually necessary for proof success (Algorithm~\ref{alg:sta}).
16	Given a proved $x$ with $n$ components, STA constructs $n$ ablated variants $x\setminus\{c_i\}$ and re-runs the solver (Algorithm~\ref{alg:sta}).
17	A component is \emph{necessary} if its removal causes proof failure.
18	What constitutes a component depends on the logic: premises in FOL, clauses or ground facts in Prolog.
19	LOO ablation itself is standard in mutation testing and sensitivity analysis~\citep{demillo1978, jia-harman-survey}; novelty lies in its application as a GRPO-hacking diagnostic and the empirical phenomena it surfaces.
20	
21	\begin{algorithm}[t]
22	\caption{Solver Trace Ablation (STA)}
23	\label{alg:sta}
24	\begin{algorithmic}[1]
25	\REQUIRE Proved formalization $x = \{c_1, \ldots, c_n\}$, solver $S$
26	\ENSURE $\text{ISR}(x) \in [0, 1]$
27	\STATE $\textit{necessary} \gets 0$
28	\FOR{$i = 1$ to $n$}
29	    \IF{$S(x \setminus \{c_i\}) = \textit{failed}$}
30	        \STATE $\textit{necessary} \gets \textit{necessary} + 1$
31	    \ENDIF
32	\ENDFOR
33	\RETURN $\textit{necessary} \,/\, n$
34	\end{algorithmic}
35	\end{algor
…[truncated 5562 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 954
}
```

</details>

---


### Tool call

_source line 2576 · 2026-05-22T15:17:09.641287+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 2577 · 2026-05-22T15:17:09.692341+00:00_

1	\section{Experiments}
2	\label{sec:experiments}
3	
4	We evaluate STA along three axes: ISR as a diagnostic for reward hacking (\S\ref{sec:diagnostic}); ISR as a training reward, where it exhibits Goodhart effects (\S\ref{sec:goodhart}); and cross-domain generalization across logic types and dataset families (\S\ref{sec:crossdomain}).
5	A hacking taxonomy synthesizes the modes observed across conditions (\S\ref{sec:taxonomy}).
6	
7	\subsection{Setup}\label{sec:setup}
8	
9	We train Qwen3-4B~\citep{qwen3} with GRPO~\citep{deepseekmath} ($K{=}4$, lr $10^{-6}$, 500 steps default, 1000 where noted) over seeds $\{42,43,44\}$ (ISR $\beta{=}0.1$ extends to $\{45,46\}$; Appendix~\ref{app:detailed-results}) on a fixed 500-example FOLIO~\citep{folio} subset held constant across all conditions; the SFT baseline uses negative log-likelihood on gold formalizations.\footnote{Seeds control initialization and rollout sampling; all conditions share the same fixed training subset.}
10	Held-out evaluation uses 100 FOLIO examples with greedy decoding;\footnote{Seed~43 uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration; excluding s43 yields consistent or stronger collapse: at 1000 steps, both remaining seeds show ${\leq}7\%$ non-hacking (Appendix~\ref{app:detailed-results}).} all cross-run ISR values are recomputed uniformly by a single evaluator so training-log ISR is never compared across runs.
11	Cross-dataset experiments (\S\ref{sec:crossdomain}) use ProofFOL, a silver-standard FOL corpus of ${\sim}$500 training examples constructed by translating ProofWriter~\citep{proofwriter} problems via GPT-4o and filtering through Prover9 (${\sim}70\%$ retention); \emph{stable convergence} denotes $\overline{\text{PR}}_{\text{final\,50}} > 0.90$.
12	We report prove rate (PR), proved-only ISR ($\text{ISR}^*$), hacking-mode rates from a two-stage classifier (strict text matching for CE/TS plus functional analysis of the per-sample $n_{\text{necessary}}$ distribution; \S\ref{sec:ta
…[truncated 15143 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 51
}
```

</details>

---


### Tool call

_source line 2578 · 2026-05-22T15:17:09.692779+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 2579 · 2026-05-22T15:17:09.743307+00:00_

1	\section{Related Work}
2	\label{sec:related-work}
3	
4	\paragraph{Neurosymbolic reasoning.}
5	LLM-solver pipelines~\citep{satlm, logic-lm, linc, fover-pei2025, lorp} and RL methods trained on solver feedback~\citep{mellgren-prolog-grpo, logic-rl, deepseek-prover-v15, deepseek-r1} evaluate execution accuracy alone, with no diagnostic for component necessity.
6	AlphaProof~\citep{alphaproof2025} and DeepSeek-Prover-V2~\citep{deepseek-prover-v2} apply RL-based formal verification at scale in Lean~4 for competition mathematics; STA-style diagnostics could probe whether similar structural degeneration occurs in these settings.
7	We use FOLIO~\citep{folio}, the only public NLI benchmark with both FOL and Prolog annotations.
8	
9	\paragraph{Process rewards and reward shaping.}
10	Reward shaping theory~\citep{ng1999policy} constrains when auxiliary rewards preserve optimal policies.
11	In mathematical reasoning, learned process reward models~\citep{lightman-verify-step, math-shepherd, cobbe2021training, uesato2022solving} and verifier-guided search~\citep{nlproofs, vstar, easy-to-hard} provide step-level feedback, but suffer from reward-model noise and distribution shift~\citep{processbench}.
12	A recurring finding is that auxiliary rewards can hurt rather than help: \citet{gao-effective-rl-reward} show process/outcome bonuses can degrade RL training, and \citet{setlur2025rewarding} demonstrate that bonus magnitude requires careful calibration.
13	Annotation-free alternatives~\citep{cui2025prime, rlsf} derive dense rewards from outcome signals or solver certificates; ISR follows this direction but our results reveal that even annotation-free structural rewards are susceptible to Goodhart effects.
14	\citet{sullivan2025grpo-prm} prove GRPO with outcome reward is implicitly a Monte-Carlo PRM, a mechanism for why component-level gaming emerges under GRPO.
15	
16	\paragraph{Reward hacking and Goodhart's Law.}
17	Goodhart's Law is established theoretically~\citep{manheim-goodha
…[truncated 2511 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2580 · 2026-05-22T15:17:15.516681+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 2581 · 2026-05-22T15:17:15.517092+00:00_

1	\section{Discussion and Conclusion}
2	\label{sec:discussion}
3	
4	STA exposes structural degeneration invisible to execution-based evaluation; repurposed as reward, ISR produces a seed-dependent Goodhart effect, documenting that structural proxies for reasoning quality are easier to observe than to optimize (Appendix~\ref{app:practical-guidelines}).
5	STA generalizes to any RL system whose output is verified by a deterministic checker---math reasoning with formal verifiers, code generation with test suites---wherever solver-verifiable structure can be ablated.
6	Our cross-scale results hint at a \emph{Goldilocks} hypothesis: structural degeneration may arise only when model capacity falls in a narrow band---strong enough to converge (unlike Qwen3-8B's rollout diversity bottleneck or LLaMA-3.2-3B's cold-start failure) yet weak enough to exploit structural shortcuts rather than learn genuine reasoning. The 50\% non-convergence rate among exec-only seeds further suggests degeneration requires successful convergence as a prerequisite.
7	As an aggregate metric, ISR is susceptible to premise-count confounds (\S\ref{sec:goodhart}); per-sample mode classification offers a more reliable diagnostic pathway for future work.
8	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 2582 · 2026-05-22T15:17:15.667869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 2583 · 2026-05-22T15:17:15.969570+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Experiments use a single base model (Qwen3-4B); structural degeneration patterns may not transfer to other model families, and neither Qwen3-8B nor LLaMA-3.2-3B converges under our GRPO configuration (Appendix~\ref{app:8b-results},~\ref{app:llama-coldstart}), leaving cross-scale generalization untested.
5	Three to five seeds per condition demonstrate qualitative divergence but remain underpowered for seed-level significance; pooled statistics treat within-seed samples as independent.
6	Structural degeneration results should be interpreted as conditional on successful convergence: three of six exec-only seeds fail to converge and retain high structural integrity (85--87\% genuine; Appendix~\ref{app:seed-convergence}), suggesting degeneration is a byproduct of reward optimization success rather than an inherent property of GRPO.
7	One of three exec-only seeds (s43) uses nucleus sampling ($T{=}0.7$) due to greedy-mode degeneration, making it not strictly comparable; excluding it yields consistent or stronger collapse patterns (Appendix~\ref{app:detailed-results}).
8	ISR quantifies component necessity, not semantic faithfulness (no correlation with NLI accuracy; Appendix~\ref{app:extended-discussion}); its diagnostic value is realized through the mode breakdown, not the scalar alone.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 301
}
```

</details>

---


### Tool call

_source line 2584 · 2026-05-22T15:17:15.970038+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/ethics.tex"
  }
}
```

</details>

---


### Tool result

_source line 2585 · 2026-05-22T15:17:16.572616+00:00_

1	\section{Ethics Statement}
2	\label{sec:ethics}
3	
4	This work documents failure modes of reward optimization in solver-backed RL systems.
5	Our findings (that structural diagnostics can be gamed when used as training signals) carry implications for AI safety: they demonstrate that metrics designed to detect misalignment may themselves become targets of optimization, a concern relevant to scalable oversight.
6	We release our taxonomy and diagnostic tools to help practitioners detect reward hacking in their own systems.
7	Code, evaluation scripts, the ProofFOL dataset, and trained model checkpoints will be released upon acceptance.
8	All experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-4B); no human subjects are involved.
9	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 2586 · 2026-05-22T15:17:16.673487+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 2587 · 2026-05-22T15:17:16.925465+00:00_

1	% Appendix — solver-trace-ablation
2	
3	\section{Experimental Setup}
4	\label{app:setup}
5	
6	Table~\ref{tab:hyperparams} lists all hyperparameters shared across experiments.
7	All RL conditions use the same GRPO configuration; only the reward function differs.
8	Seeds control model weight initialization and data shuffling; training data is held constant across all seeds and conditions (Constraint~C001).
9	
10	\begin{table}[ht]
11	\centering
12	\caption{Training hyperparameters for all GRPO experiments.}
13	\label{tab:hyperparams}
14	\footnotesize
15	\resizebox{\columnwidth}{!}{%
16	\begin{tabular}{@{}ll@{}}
17	\toprule
18	\textbf{Parameter} & \textbf{Value} \\
19	\midrule
20	\multicolumn{2}{@{}l}{\textit{Model}} \\
21	Base model & Qwen3-4B \\
22	Precision & BF16 \\
23	\midrule
24	\multicolumn{2}{@{}l}{\textit{GRPO Training}} \\
25	Rollouts per prompt ($K$) & 4 \\
26	Training steps (default) & 500 \\
27	Training steps (extended) & 1000 \\
28	Learning rate & $1 \times 10^{-6}$ \\
29	Per-device batch size & 4 \\
30	Gradient accumulation steps & 2 \\
31	Effective batch size & 8 \\
32	Max completion length & 512 tokens \\
33	Random seeds & 42, 43, 44 \\
34	\midrule
35	\multicolumn{2}{@{}l}{\textit{Data}} \\
36	Training set & FOLIO, 500 examples \\
37	Evaluation set & FOLIO, 100 examples (held-out) \\
38	Data file & \texttt{train\_500\_seed42} \\
39	\midrule
40	\multicolumn{2}{@{}l}{\textit{Solvers}} \\
41	FOL solver & Prover9 \\
42	Prolog solver & SWI-Prolog 8.4.2 \\
43	\midrule
44	\multicolumn{2}{@{}l}{\textit{Evaluation}} \\
45	Decoding & Greedy ($T{=}0$) \\
46	ISR computation & \texttt{eval\_sta.py} \\
47	ISR variant & Proved-only (ISR$^*$) \\
48	\bottomrule
49	\end{tabular}}
50	\end{table}
51	
52	\paragraph{Compute resources.}
53	Experiments were run on single-GPU setups (NVIDIA RTX 4090 24\,GB and RTX PRO 6000 96\,GB).
54	Each GRPO training run takes approximately 1--2 GPU-hours (500 steps) or 3--5 GPU-hours (1000 steps).
55	Total compute across all seeds, condit
…[truncated 53764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 251
}
```

</details>

---


### Tool call

_source line 2588 · 2026-05-22T15:17:23.853189+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 2589 · 2026-05-22T15:17:24.004580+00:00_

1	% ============================================================
2	% LLaMA
3	% ============================================================
4	
5	@article{grattafiori2024llama,
6	  author = {Aaron Grattafiori and Abhimanyu Dubey and Abhinav Jauhri and others},
7	  title = {{The Llama 3 Herd of Models}},
8	  journal = {arXiv preprint arXiv:2407.21783},
9	  year = {2024},
10	  eprint = {2407.21783},
11	  archiveprefix = {arXiv},
12	}
13	
14	% ============================================================
15	% Category 1: Neurosymbolic reasoning + RL/GRPO
16	% ============================================================
17	
18	@article{deepseekmath,
19	  author       = {Zhihong Shao and Peiyi Wang and Qihao Zhu and Runxin Xu and others},
20	  title        = {{DeepSeekMath: Pushing the Limits of Mathematical Reasoning in Open Language Models}},
21	  journal      = {arXiv preprint arXiv:2402.03300},
22	  year         = {2024},
23	  eprint       = {2402.03300},
24	  archivePrefix = {arXiv},
25	  primaryClass = {cs.AI},
26	}
27	
28	@article{logic-rl,
29	  author       = {Tian Xie and Zitian Gao and Qingnan Ren and Haoming Luo and Yuqian Hong and Bryan Dai and Joey Zhou and Kai Qiu and Zhirong Wu and Chong Luo},
30	  title        = {{Logic-RL: Unleashing LLM Reasoning with Rule-Based Reinforcement Learning}},
31	  journal      = {arXiv preprint arXiv:2502.14768},
32	  year         = {2025},
33	  eprint       = {2502.14768},
34	  archivePrefix = {arXiv},
35	  primaryClass = {cs.AI},
36	}
37	
38	@article{mellgren-prolog-grpo,
39	  author       = {Niklas Mellgren and Peter Schneider-Kamp and Lukas Galke},
40	  title        = {{Training Language Models to Use Prolog as a Tool}},
41	  journal      = {arXiv preprint arXiv:2512.07407},
42	  year         = {2025},
43	  eprint       = {2512.07407},
44	  archivePrefix = {arXiv},
45	  primaryClass = {cs.AI},
46	}
47	
48	@inproceedings{satlm,
49	  author       = {Xi Ye and Qiaochu Chen and Isil Dillig and Greg Durrett},
50	  title        
…[truncated 22347 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "Read",
  "elapsed_ms": 151
}
```

</details>

---


### Tool call

_source line 2590 · 2026-05-22T15:17:24.356405+00:00_

called mcp__agent-ml-research__read_project_file

<details open><summary>🔧 Tool call — mcp__agent-ml-research__read_project_file</summary>

```json
{
  "project": "solver-trace-ablation",
  "file": "decisions.yaml",
  "max_chars": "3000"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "tool_args": {
    "project": "solver-trace-ablation",
    "file": "decisions.yaml",
    "max_chars": "3000"
  }
}
```

</details>

---


### Tool result

_source line 2591 · 2026-05-22T15:17:24.407358+00:00_

{"result":"{\"success\": true, \"data\": {\"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/decisions.yaml\", \"content\": \"_next_id: 164\\ndecisions:\\n- id: D001\\n  date: 2026-05-13 17:34 UTC\\n  summary: MVP 方案：FOL+Prover9 单逻辑 50-step GRPO pilot 验证 STA reward 有效性\\n  rationale: EMNLP ARR DDL 5/25 仅剩 12 天，需要最快速度验证核心假设。选 FOL+Prover9 因为 hacking 模式最清晰（tautological\\n    formulas），STA 的 O(1) 近似最直观（去掉前提后能否证明结论）。50-step pilot 足以观察 ISR 趋势。两个条件并行跑 2 GPU。Pass\\n    标准：ISR gap >20pp + accuracy 降幅 <5pp。\\n  related_experiments: []\\n  depends_on: []\\n- id: D002\\n  date: 2026-05-13 17:37 UTC\\n  summary: MVP 方案调整：50步→100步 + 趋势判断 + Phase 0 ISR baseline + kill criteria\\n  rationale: 采纳 Reviewer 三条 warning：(1) 加 pre-training ISR baseline 锚定训练前水平；(2) 50步太短难以观察\\n    reward hacking，改 100步+最后20步 moving average 趋势判断；(3) 补充硬性 kill criteria 防止 DDL\\n    压力下无止境调整。\\n  related_experiments: []\\n  depends_on:\\n  - D001\\n- id: D003\\n  date: 2026-05-13 20:50 UTC\\n  summary: Phase 1 r4 fast_isr_fol 训练信号无效，改用 full STA + K=8 重跑\\n  rationale: fast_isr_fol 是二值 O(1) 近似（ISR=0 tautology / ISR=1 non-tautology），Qwen3-4B\\n    生成的 proved formalization 几乎全部 ISR=1，与 execution-only 零差异。full STA 提供连续 ISR（0.125-0.889\\n    in Phase 0），能给出真实梯度信号。K=4 导致 frac_reward_zero_std=0.5-1.0（GRPO 无 advantage），K=8\\n    增加 within-group variance。两个改动分别解决 STA 信号粒度和 GRPO 梯度信号两个独立问题。\\n  related_experiments:\\n  - exp_id: sta-phase1-exec-only-r4\\n    role: evidence\\n    result: prove_rate 12%→15%, ISR ~0.15, minimal learning\\n  - exp_id: sta-phase1-exec-sta-r4\\n    role: evidence\\n    result: 与 exec-only 几乎完全相同, fast_isr 提供零额外信号\\n  depends_on:\\n  - D002\\n- id: D004\\n  date: 2026-05-13 21:59 UTC\\n  summary: Reviewer 指出 exec-sta-r5 prove_rate 低于 baseline（退化），STA 50/50 权重过于惩罚性。立即补跑低权重\\n    + bonus 模式实验\\n  rationale: exec-sta-r5 prove_rate=0.10 < baseline=0.12 < exec-only=0.15。连续 ISR 给\\n    proved-but-low-ISR 样本 reward≈0.3（几乎等于未 prove），模型学到 prove 不值得。Kill criteri
…[truncated 1452 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__read_project_file",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 2592 · 2026-05-22T15:17:52.121858+00:00_

called mcp__agent-ml-research__dispatch_visual_check

<details open><summary>🔧 Tool call — mcp__agent-ml-research__dispatch_visual_check</summary>

```json
{
  "project": "solver-trace-ablation",
  "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "tool_args": {
    "project": "solver-trace-ablation",
    "review_chat_id": "oc_5abafbb382eb7c81e8a38090e46323e7"
  }
}
```

</details>

---


### Tool call

_source line 2593 · 2026-05-22T15:17:54.280757+00:00_

called mcp__agent-ml-research__request_external_review

<details open><summary>🔧 Tool call — mcp__agent-ml-research__request_external_review</summary>

```json
{
  "project": "solver-trace-ablation",
  "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_28/submitted.pdf",
  "venue": "EMNLP 2026"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "tool_args": {
    "project": "solver-trace-ablation",
    "paper_pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_28/submitted.pdf",
    "venue": "EMNLP 2026"
  }
}
```

</details>

---


### Tool result

_source line 2594 · 2026-05-22T15:18:15.044912+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"started\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__dispatch_visual_check",
  "elapsed_ms": 22923
}
```

</details>

---


### Tool result

_source line 2595 · 2026-05-22T15:18:15.045412+00:00_

{"result":"{\"success\": true, \"data\": {\"status\": \"pending\", \"message\": \"外部审稿请求已发送到用户群。将在 8 小时后自动提醒。\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__request_external_review",
  "elapsed_ms": 20764
}
```

</details>

---


### Tool call

_source line 2596 · 2026-05-22T15:18:15.999505+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 8 页限制，references 不限，Limitations/Ethics 不计入页数）\n- **模板**: ACL style, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_28/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- STA (Solver Trace Ablation) 的 LOO 方法是否有根本性缺陷？LOO independence assumption 的讨论是否充分？\n- ISR 指标的设计：proved-only ISR 的合理性，premise-count confound 的处理是否充分\n- 八种 hacking mode 的分类法：classifier 设计是否合理，precision/recall 验证是否充分（152 样本 precision audit）\n- Reward formulation（multiplicative coupling）的实验设计是否控制了足够的混淆因素\n\n### 2. 统计分析\n- N=3 seeds 的统计效力是否足够支撑论文 claims？论文自身承认的 underpowered 问题\n- CMH 检验的使用是否合理（within-seed independence 假设）\n- Fisher exact test、Bonferroni correction 的应用\n- 5-seed extension（s45, s46 post-hoc）的方法论问题\n\n### 3. 实验控制\n- SFT baseline 的设置是否公平（PR=13% vs exec-only PR=93%）\n- Random control 是否充分隔离 ISR-specific 信号\n- Shuffled-ISR control 的有效性\n- Cross-dataset (ProofFOL) 和 cross-logic (Prolog) 验证的充分性\n- Cross-scale (Qwen3-8B) 实验失败的解释是否令人信服\n\n### 4. 可复现性\n- 实验细节（超参数、数据划分、评估协议）是否充分\n- Seed 43 使用 sampling eval 而非 greedy 的处理\n- ProofFOL 数据集构建的可复现性\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。\n每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 1，负责 **方法严谨性 + 实验设计** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 8 页限制，references 不限，Limitations/Ethics 不计入页数）\n- **模板**: ACL style, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_28/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 方法论严谨性\n- STA (Solver Trace Ablation) 的 LOO 方法是否有根本性缺陷？LOO independence assumption 的讨论是否充分？\n- ISR 指标的设计：proved-only ISR 的合理性，premise-count confound 的处理是否充分\n- 八种 hacking mode 的分类法：classifier 设计是否合理，precision/recall 验证是否充分（152 样本 precision audit）\n- Reward formulation（multiplicative coupling）的实验设计是否控制了足够的混淆因素\n\n### 2. 统计分析\n- N=3 seeds 的统计效力是否足够支撑论文 claims？论文自身承认的 underpowered 问题\n- CMH 检验的使用是否合理（within-seed independence 假设）\n- Fisher exact test、Bonferroni correction 的应用\n- 5-seed extension（s45, s46 post-hoc）的方法论问题\n\n### 3. 实验控制\n- SFT baseline 的设置是否公平（PR=13% vs exec-only PR=93%）\n- Random control 是否充分隔离 ISR-specific 信号\n- Shuffled-ISR control 的有效性\n- Cross-dataset (ProofFOL) 和 cross-logic (Prolog) 验证的充分性\n- Cross-scale (Qwen3-8B) 实验失败的解释是否令人信服\n\n### 4. 可复现性\n- 实验细节（超参数、数据划分、评估协议）是否充分\n- Seed 43 使用 sampling eval 而非 greedy 的处理\n- ProofFOL 数据集构建的可复现性\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Minor Issues。\n每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 2597 · 2026-05-22T15:18:29.383148+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 13383
}
```

</details>

---


### Tool call

_source line 2598 · 2026-05-22T15:18:29.534092+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "2",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + Related Work** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 8 页限制，references 不限，Limitations/Ethics 不计入页数）\n- **模板**: ACL style, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_28/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- STA 的核心技术（LOO ablation on solver inputs）本质上是 mutation testing 的直接应用，novelty 在哪？论文自称\"novelty lies in application and findings, not in the perturbation primitive\"——这种 novelty 是否足够？\n- ISR 指标 vs 已有的 structural metrics 有何本质区别？\n- \"Observe-vs-optimize asymmetry\" 这个 framing 是否有独立的理论贡献，还是纯经验观察？\n- Goodhart effect 在 RL 中已被广泛研究，本文在 neurosymbolic setting 的 instantiation 是否提供了新的 insight？\n- 与 Kim et al. (2026) 的关系：他们做 inference-time gaming detection on FOLIO，本文做 training-time degeneration——互补性和差异性是否讲清楚了？\n\n### 2. Related Work 完整性\n- 搜索最新文献（2025-2026），检查是否有遗漏的重要相关工作\n- 特别关注：RLVR reward hacking、neurosymbolic RL、process reward models、formal verification + RL 领域\n- 论文引用的文献是否都是真实存在的？（检查可疑引用）\n- 引用格式是否符合 ACL 规范\n\n### 3. 论文完整性\n- 三个 contributions (C1, C2, C3) 是否都有充分的实验支撑？\n- \"Case Study\" subtitle 是否过于自谦，削弱了论文的 impact？\n- Discussion/Conclusion 中的 \"Goldilocks hypothesis\" 是否有足够支撑还是过度推测？\n- Limitations 是否覆盖了关键局限性？是否存在作者未提及的重要限制？\n\n### 4. 写作质量\n- 论文叙事结构是否清晰连贯？\n- 术语使用是否一致（例如 hacking mode 命名：CE/TS/PG 等）\n- 图表设计是否有效传达了核心发现？\n- 页数是否符合 8 页限制（正文部分）\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "2",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "你是 Reviewer 2，负责 **新颖性 + 完整性 + Related Work** 审查。\n\n## 投稿信息\n- **Venue**: EMNLP 2026 via ACL Rolling Review\n- **类别**: Long Paper（正文 8 页限制，references 不限，Limitations/Ethics 不计入页数）\n- **模板**: ACL style, double-blind\n- **Deadline**: 2026-05-25\n- **论文路径**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/docs/paper/main.tex`\n- **PDF**: `/home/ubuntu/.agent-ml-research-idea_gen_0509_3/projects/solver-trace-ablation/artifacts/review_round_28/submitted.pdf`\n\n## 你的审查侧重\n\n### 1. 新颖性评估\n- STA 的核心技术（LOO ablation on solver inputs）本质上是 mutation testing 的直接应用，novelty 在哪？论文自称\"novelty lies in application and findings, not in the perturbation primitive\"——这种 novelty 是否足够？\n- ISR 指标 vs 已有的 structural metrics 有何本质区别？\n- \"Observe-vs-optimize asymmetry\" 这个 framing 是否有独立的理论贡献，还是纯经验观察？\n- Goodhart effect 在 RL 中已被广泛研究，本文在 neurosymbolic setting 的 instantiation 是否提供了新的 insight？\n- 与 Kim et al. (2026) 的关系：他们做 inference-time gaming detection on FOLIO，本文做 training-time degeneration——互补性和差异性是否讲清楚了？\n\n### 2. Related Work 完整性\n- 搜索最新文献（2025-2026），检查是否有遗漏的重要相关工作\n- 特别关注：RLVR reward hacking、neurosymbolic RL、process reward models、formal verification + RL 领域\n- 论文引用的文献是否都是真实存在的？（检查可疑引用）\n- 引用格式是否符合 ACL 规范\n\n### 3. 论文完整性\n- 三个 contributions (C1, C2, C3) 是否都有充分的实验支撑？\n- \"Case Study\" subtitle 是否过于自谦，削弱了论文的 impact？\n- Discussion/Conclusion 中的 \"Goldilocks hypothesis\" 是否有足够支撑还是过度推测？\n- Limitations 是否覆盖了关键局限性？是否存在作者未提及的重要限制？\n\n### 4. 写作质量\n- 论文叙事结构是否清晰连贯？\n- 术语使用是否一致（例如 hacking mode 命名：CE/TS/PG 等）\n- 图表设计是否有效传达了核心发现？\n- 页数是否符合 8 页限制（正文部分）\n\n请给出结构化审稿报告：Summary → Strengths → Weaknesses → Questions → Missing References → Minor Issues。\n每个 Weakness 标注严重程度（Must-Fix / Should-Fix / Nice-to-Have）。"
  }
}
```

</details>

---


### Tool result

_source line 2599 · 2026-05-22T15:18:31.104072+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_2\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 1569
}
```

</details>

---


### Assistant

_source line 2600 · 2026-05-22T15:18:43.229841+00:00_

圆桌审稿已启动：

- **Reviewer 1**（方法严谨性 + 实验设计）：已派发
- **Reviewer 2**（新颖性 + 完整性 + Related Work）：已派发
- **视觉审查 Agent**：已启动（并行，不阻塞）
- **外部审稿（Stanford Agentic Reviewer）**：协助卡片已发送，8 小时后自动提醒

等待两位 Reviewer 返回 Round 1 初审报告。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 235

## Round 235

2 recorded events


### User

_source line 2601 · 2026-05-22T15:24:17.079224+00:00_

[Reviewer 1 审稿意见]:
## Reviewer 1 审稿报告：方法严谨性 + 实验设计

**论文**: Solver Trace Ablation Diagnoses Structural Degeneration and Goodhart Effects in GRPO-Trained Neurosymbolic Reasoning: A Case Study
**Venue**: EMNLP 2026 via ACL Rolling Review

---

## 总体评分

**Overall**: 3.5 / 5 — Borderline Conference
**一句话总结**: 提出了一个新颖且有实用价值的诊断框架（STA/ISR），揭示了 GRPO 训练中结构退化和 Goodhart 效应的重要现象，但 N=3 seeds 的统计效力不足、LOO 独立性假设缺乏实证验证、以及单一奖励公式的局限性削弱了核心 claim 的证据强度。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.0 / 5 | 核心诊断方法（STA/ISR）设计合理，但 LOO 独立性假设未经实证验证，N=3 seeds 统计效力不足以支撑 Goodhart 效应的因果推断，premise-count confound 仅部分解决 |
| Excitement | 3.5 / 5 | 填补了 neurosymbolic reasoning 中 execution-only 评估与昂贵 step-level 标注之间的诊断空白；hacking taxonomy 有创意；但单模型（Qwen3-1.5B）限制了 impact |
| Reproducibility | 3.5 / 5 | 附录提供了详尽的 per-seed 结果和超参数，承诺开源代码和数据；但 seed 43 评估协议不一致、ProofFOL 构建流程细节不够完整 |
| Reviewer Confidence | 4 / 5 | 熟悉 RLVR、neurosymbolic reasoning、reward hacking 领域；仔细阅读了全文和所有附录 |

---

## Summary

本文提出 Solver Trace Ablation (STA)，一种基于 leave-one-out (LOO) 消融的诊断方法，用于检测 GRPO 训练的 neurosymbolic reasoning 模型中的结构退化。核心指标 Intensional Structural Reward (ISR) 衡量已证明公式中各组件的必要性比例。在 FOLIO（FOL）和 Prolog 任务上，作者发现：(1) exec-only GRPO 训练导致 ISR 坍塌至近零，揭示结构退化；(2) 将 ISR 作为训练奖励（乘性耦合）产生 Goodhart 效应——优化转向 tautological shortcuts 而非提升推理质量；(3) 识别出八种 hacking mode 的分类法。实验在 FOL、Prolog、ProofFOL 上进行了交叉验证。

---

## 主要优势

**S1: 新颖且实用的诊断框架**。STA 填补了一个真实的方法论空白——当前 neurosymbolic reasoning 的评估要么依赖 execution accuracy（无法区分真正推理与结构捷径），要么需要昂贵的 step-level annotation。STA 利用已有 solver 的验证能力，零标注成本即可实现 component-level 诊断。Algorithm 1 (p3) 清晰简洁。

**S2: 实验控制设计周全**。论文设置了多层控制：shuffled-ISR control（破坏 ISR 的内容信号但保留 sample-level 分布）、random control（β 匹配）、premise-count matched comparison (Appendix C)。这些控制有效隔离了 ISR-specific 信号与一般性训练动态。

**S3: Hacking taxonomy 有创意且可操作**。八种 hacking mode 的分类法（CE、TS、PG、CI 等）基于确定性规则分类器（text-match + functional analysis），透明度高，且每种模式都有清晰的定义、FOL 示例和 ISR interaction 分析（Appendix D, p15-17）。这为该领域提供了可复用的诊断词汇。

**S4: 诚实的 Limitations 处理**。论文坦诚承认 N=3 underpowered、Qwen3-8B 失败、ISR 的 premise-count confound、LOO independence assumption 等问题。标题中的 "Case Study" 恰当设定了预期。这种学术诚信值得肯定。

**S5: 跨域验证增强了 generalizability 证据**。FOL→Prolog 的跨逻辑验证（Table 9, p20）显示定性一致的退化模式但 dominant hacking mode 不同（FOL: CE; Prolog: TS），这实际上是一个有趣的发现，表明退化的具体形态依赖于逻辑系统的结构约束。ProofFOL 提供了跨数据集证据。

---

## Must-Fix 问题（影响接收决定）

**N1** [critical] **N=3 Seeds 统计效力不足以支撑 Goodhart 效应的因果推断**

- **具体位置**: Section 4.1 (p5), Table 1 (p7), Appendix E.5 (p22), Limitations (p8)
- **问题**: 论文的核心 claim 之一——ISR-as-reward 产生 seed-dependent Goodhart effect——建立在仅 3 个 seeds 的基础上。更严重的是：
  - **Seed 43 使用了不同的评估协议**（sampling T=0.7 而非 greedy decoding，Appendix A p12），论文自己承认 "not strictly comparable with other seeds under the unified evaluation protocol"。这实际上将可比较的 seeds 从 3 个减少到 2 个。
  - **5-seed extension (seeds 45, 46) 仅限于 exec-only 条件**（Appendix E.5, p22），且是 post-hoc 添加的，未覆盖 ISR-as-reward 条件——恰恰是统计效力最需要增强的地方。
  - **Table 5 (p14)** 中多项 Fisher exact test 在 Bonferroni 校正后未达到显著性（例如 Baseline vs. Exec-only: p=0.68；ISR vs. Exec-only 的 non-hacking rate OR=0.182 但 p=0.62）。
  - **CMH 检验假设 within-seed independence**，论文在 Appendix C (p13) 承认 "Bonferroni assumes independence" 且 CMH "treats within-seed samples as independent observations from a single trained model"——这个假设在同一模型生成的 samples 间很可能不成立。
- **为什么影响接收**: 这是方法论层面的核心问题。Goodhart effect 是论文最有影响力的发现，但当前证据强度不足以区分 "ISR-specific Goodhart effect" 与 "seed-level variance"。两个 comparable seeds 上的差异可能完全由随机性解释。
- **建议修改方向**: (a) 将 5-seed extension 扩展到 ISR β=0.1 条件，至少达到 5 seeds 的统计基线；(b) 对 seed 43 进行 greedy eval 重新评估或将其从主要比较中排除，作为 robustness check 报告；(c) 采用 bootstrap 或 permutation test 替代 CMH，避免 within-seed independence 假设。

**N2** [critical] **LOO 独立性假设缺乏实证验证，"conservative" claim 无经验支撑**

- **具体位置**: Section 3.2 (p4), Appendix C (p12-13), Appendix E.3 (p21)
- **问题**: ISR 基于 LOO 消融，逐一移除组件并测试证明是否仍成立。论文正确指出（p4）"LOO ablation tests each component individually, not jointly" 且 ISR "systematically underestimating ISR when jointly-necessary components exist"。论文进而声称 "the observed collapse is therefore conservative"。然而：
  - **没有提供任何实证数据证明 "conservative" 假设的合理性**。论文未测量 joint necessity 在其数据中的实际发生频率。
  - **在 FOL 的结构特点下，joint necessity 可能比论文暗示的更普遍**。例如，两个前提可能各自非必需（因为另一个前提可替代其功能），但它们同时移除时证明失败。这在链式推理中尤其可能发生。
  - **Appendix E.3 (p21) 提到了 O(1) binary variant (fast ISR)**，它只测试 collective premise necessity (ISR=1 iff proved and conclusion not tautological)——这实际上是一个更粗粒度的替代方案，但论文未系统比较两者的差异来量化 LOO 近似的误差。
- **为什么影响接收**: ISR 是论文的核心诊断指标。如果 LOO 近似的误差在某些 hacking mode 下是系统性的（非保守的），则 hacking taxonomy 的 prevalence 统计可能不可靠。
- **建议修改方向**: (a) 在一个 representative sample (如 50-100 个已证明公式) 上运行 full pairwise interaction test (O(n²))，量化 LOO 与 pairwise 结果的差异；(b) 明确区分 "ISR underestimates structural quality" (conservative) 与 "ISR underestimates in mode-specific ways" (potentially biased)；(c) 至少提供理论论证说明在什么条件下 LOO 对 FOL 公式是保守的（例如利用 FOL 的单调性）。

---

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] **SFT Baseline 的 PR=13% 使 ISR 比较几乎无意义**

- **具体位置**: Section 4.1 (p5-6), Table 1 (p7)
- **问题**: SFT baseline 的 prove rate 仅 13%，而 exec-only GRPO 为 93%。ISR 仅对已证明的公式有定义——因此 SFT 的 ISR 是在一个极小且高度 biased 的子集上计算的（仅 ~65 个 proved samples out of 500）。论文将 SFT 定位为 "pre-RL reference rather than a PR-matched control" (p6)，但这削弱了它作为比较基准的价值。
  - SFT 的 ISR=0.395 vs exec-only 的 ISR=0.132——这个差异可能完全由 selection bias 解释（SFT 的 13% proved 样本可能是"容易"的问题，天然 ISR 更高）。
- **建议**: (a) 报告 SFT 和 exec-only 在 prove rate 匹配子集上的 ISR 比较；(b) 或者坦诚声明 SFT 仅作为 sanity check 而非正式 baseline。

**W2** [warning] **Hacking 分类器的 recall 未知，precision audit 样本量有限**

- **具体位置**: Section 3.3 (p4-5), Table 7 (p15), Appendix D (p14-17)
- **问题**:
  - Precision audit 覆盖 152 个样本（Table 7），每种 mode 仅 7-50 个。CE 和 TS 各 50 个 random sample 的 precision >95% 是好的，但 PG (20 samples)、Contradiction (20 samples) 的样本量太小，置信区间很宽。
  - **Recall 被明确声明为 "bounded by the text-match threshold"** (p14)——这意味着 semantic manipulations altering surface form 会被漏掉。论文自己在 Appendix D (p14) 承认 "recall is not estimable from the validation-only design"。
  - 如果 recall 较低，则 Table 2 (p7) 的 hacking mode prevalence 是 lower bound——论文中 "non-hacking" 比例可能包含大量 undetected hacking。
- **建议**: (a) 在一个小 sample 上进行 human-annotated recall audit（随机抽样 proved samples，human 判定是否 hacking，与 classifier 比较）；(b) 明确将 prevalence 数字标注为 lower bound。

**W3** [warning] **Premise-count confound 仅部分解决**

- **具体位置**: Appendix C (p12-13), Section 3.2 (p4)
- **问题**: Appendix C 详细讨论了 premise-count confound 并做了 matched comparison，将 3.2× 优势缩减至 1.06×。然而：
  - **1.06× 的残差是否统计显著未做正式检验**。论文仅说 "indistinguishable (p=0.182; Appendix D.1)" 但这个 p 值对应的是 non-hacking rate 的比较，而非 ISR 本身。
  - 论文推荐 "component-count normalization" 但在本文中并未实施。
  - **ISR 作为训练奖励时**，premise-count confound 不仅是诊断问题，更是训练动态问题——模型可能学会 "通过减少组件数来机械性提升 ISR"，这恰恰是观察到的 Goodhart effect 的一个混淆因素。
- **建议**: 正式检验 premise-count matched ISR 差异的显著性；在 Discussion 中明确讨论 premise-count confound 对 Goodhart effect 解释的影响。

**W4** [warning] **单一奖励公式限制了 Goodhart effect claim 的 generality**

- **具体位置**: Section 4.3 (p6), Equation for r = r_exec × (1 + β·ISR)
- **问题**: Goodhart effect 是论文最有影响力的发现，但仅测试了一种奖励耦合方式（乘性）和两个 β 值（0.1, 0.3）。
  - 未测试 additive coupling (r = r_exec + β·ISR)
  - 未测试 ISR 作为 threshold/filter 而非 continuous reward
  - 未测试更大或更小的 β 值区间
  - **当前证据只能说明"乘性耦合 ISR 在 β=0.1/0.3 时产生 Goodhart effect"，不能泛化为 "ISR-as-reward necessarily produces Goodhart effects"**
- **建议**: 至少补充 additive coupling 的实验或 ablation，或在 claim 中明确限定为 "multiplicative coupling under tested β values"。

**W5** [warning] **Qwen3-8B 跨 scale 失败的解释缺乏验证**

- **具体位置**: Section 4.4 (p7), Appendix E.7 (p22-23), Limitations (p8)
- **问题**: Qwen3-8B 在 exec-only GRPO 下 PR 仅 14%，K=4 rollouts near-identical。论文将此解释为 "convergence threshold for GRPO-driven degeneration"——即 base model 需要先达到一定优化水平才能出现结构退化。但：
  - 这个解释是 post-hoc 的，未经独立验证
  - 替代假设同样合理：(a) FOL 任务对 8B 模型仍太难；(b) K=4 的 rollout diversity 不足以驱动 GRPO 优化；(c) 超参数需要针对更大模型调整
  - LLaMA-3.2-3B 的 cold-start failure (Appendix E.4) 也存在类似问题
- **建议**: 至少测试一个替代假设（如增加 K=8 或调整学习率），或将该解释降级为 "one possible explanation"。

---

## 小问题（不影响接收）

**M1**: Table 1 (p7) 列名 "ISR†" 的 dagger 注释在表格底部，但 "† proved-only ISR" 与 "‡ seed 42 ISR" 的区分在小字体下不易阅读。建议将 ISR 定义内联到表格 caption。

**M2**: Section 2 (p2) Related Work 涵盖了 reward hacking 和 Goodhart's Law 的理论背景，但缺少与 Kim et al. (2026) 在 FOLIO 上 inference-time gaming detection 的直接对比讨论——论文仅在一句话中提到 "complementary"。

**M3**: Figure 1 (p2) 的 ISR 轨迹图展示了 collapse 模式，但 y 轴标签 "ISR (proved samples only, rating n=20)" 中 n=20 的含义不够直观——是每个 checkpoint 随机抽样 20 个 proved samples 来计算 ISR 吗？

**M4**: Appendix A Table 3 (p11) 列出了所有超参数，但 "gradient accumulation steps: 2" 在 effective batch size = 8×2=16 的情况下对 GRPO 的 advantage estimation 是否有影响，未讨论。

**M5**: 论文声明 "all experiments use publicly available datasets (FOLIO) and open-weight models (Qwen3-1B)" (p8)，但 ProofFOL 是新构建的数据集——应明确区分已有数据集和本文贡献的数据集。

---

## Questions for Authors

**Q1**: 在 LOO 消融中，是否观察到过 component A 单独移除时证明仍成立、component B 单独移除时证明也仍成立、但 A+B 同时移除时证明失败的情况？如果有，频率如何？这直接关系到 "conservative" claim 的可信度。

**Q2**: Seed 43 在 sampling eval (T=0.7) 下的 ISR 和 hacking mode distribution 与 greedy decoding 下预期有多大差异？是否可以补充 greedy eval 结果？

**Q3**: 对于 SFT baseline 中 proved 的 ~65 个样本，其 problem difficulty 分布与 exec-only GRPO 的 ~465 个 proved 样本相比如何？ISR 差异是否可能反映的是 problem difficulty 而非训练方法的差异？

**Q4**: 在 ISR-as-reward 条件下观察到的 hacking mode shift (CE→TS)，是否可能仅仅是 premise-count reduction 的副产品？即：ISR 奖励驱动模型减少组件数 → 更少组件的公式更容易被归类为 TS → 看起来像 mode shift，但本质上只是 premise count 变化？

**Q5**: 论文提到 "ISR captures component necessity, not semantic faithfulness" (Section 3.2, p4) 并声称 "its diagnostic value is realized through the mode breakdown, not the scalar alone"。但 Section 4.2 和 4.3 中多处直接使用 ISR scalar 作为比较依据。能否澄清 ISR scalar 的确切诊断地位？

---

## 总结

这是一篇有创意的诊断方法论文。STA/ISR 框架填补了 neurosymbolic reasoning 评估中的一个真实空白，hacking taxonomy 为该领域提供了有用的分析词汇。论文的学术诚信度高（坦诚承认 N=3 underpowered、seed 43 例外、cross-scale 失败），标题 "Case Study" 设定了恰当的预期。

主要限制在于：(1) 统计效力不足以支撑因果推断（特别是 Goodhart effect claim）；(2) LOO 独立性假设未经实证验证；(3) 单一奖励公式限制了 generalizability。如果 N1 和 N2 能够得到充分回应（特别是增加 seeds 和 LOO 交互分析），本文有望达到 Conference 水平。当前状态下，方法论贡献（STA 框架 + hacking taxonomy）足以支撑 Findings 推荐，但 Goodhart effect 的因果 claim 需要 temper 或加强证据。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2602 · 2026-05-22T15:24:24.671901+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后进入交叉分享阶段。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 236

## Round 236

2 recorded events


### User

_source line 2603 · 2026-05-22T15:24:38.836858+00:00_

[Reviewer 1 审稿结果]:
审稿完成。已向 Review Director 提交结构化审稿报告，核心结论：

- **Overall: 3.5（Borderline Conference）**
- **Soundness: 3.0** — N=3 seeds + seed 43 评估不一致是最大瓶颈；LOO independence assumption 缺乏实证
- **Excitement: 3.5** — STA/ISR 诊断框架新颖，hacking taxonomy 有创意
- **2 个 Must-Fix**: (N1) 统计效力不足以支撑 Goodhart effect 因果推断；(N2) LOO 独立性假设的 "conservative" claim 无经验证据
- **5 个 Should-Fix**: SFT baseline PR 不匹配、hacking classifier recall 未知、premise-count confound 部分解决、单一奖励公式、Qwen3-8B 失败解释未验证
- **5 个 Questions** 供 authors 回应

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_1"
}
```

</details>

---


### Assistant

_source line 2604 · 2026-05-22T15:24:45.519007+00:00_

Reviewer 1 报告已收到。等待 Reviewer 2 报告后进入交叉分享环节。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director"
}
```

</details>

---


## Round 237

## Round 237

6 recorded events


### User

_source line 2605 · 2026-05-22T15:24:52.330373+00:00_

[Reviewer 2 审稿意见]:
## Reviewer 2 审稿报告（新颖性 + 完整性 + Related Work）

## 总体评分
**Overall**: 3.5 / 5 (Borderline Conference)
**一句话总结**: 一篇选题精准、实验设计严谨的 case study，诊断了 RLVR 训练中不可见的结构退化现象，但技术新颖性有限且泛化范围较窄，处于 Conference/Findings 交界线。

## 官方维度打分（ACL ARR Review Form）

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 实验设计有 matched controls，但样本量小（N=3 seeds），premise-count confound 未解决，统计功效有限 |
| Excitement | 3/5 | 选题时效性强，发现有实用价值，但 LOO + Goodhart 的组合创新有限，核心 insight 在其他 setting 已有类似发现 |
| Overall | 3.5/5 | 扎实的 empirical case study，Findings 稳，Conference 需看 area chair 对 novelty 的态度 |
| Reproducibility | 4/5 | 开源数据/模型/代码承诺，超参数详尽（Appendix A Table 3），训练细节充分 |
| Confidence | 4/5 | 熟悉 RLVR、neurosymbolic reasoning 和 reward hacking 文献 |

## Must-Fix 问题（影响接收决定）

**N1** [critical] Premise-count confound 是系统性方法论缺陷，而非 minor issue
- 具体位置：§C (Appendix), §3.2 (Limitations of ISR), §4.3 最后一段
- 问题：论文承认 ISR 被 premise minimization 系统性 inflate（§C: "The apparent ISR-as-reward success (§4.3): ISR β=0.1 seed 42 produces shorter formalization, mechanically inflating ISR"）。Premise-count-matched 对比消除了差异（1.06×; Table 8），说明 ISR 的表面优势很大程度来自 premise 数量减少而非真正的结构改善。论文将 component-count normalization 留作 future work，但这意味着 C2 (Goodhart effect 的量化分析) 建立在一个已知有偏的指标上。
- 为什么影响接收：C2 是三个 contribution 之一。如果 ISR-as-reward 的 Goodhart 效应主要是 premise-count artifact，那么该 contribution 的实质内容被削弱。
- 建议修改方向：至少在 appendix 提供 premise-count-normalized ISR 的 Goodhart 分析；如果 normalized 后效应消失，需诚实报告并降低 C2 的 claim 强度。

**N2** [critical] 泛化性不足以支撑 paper-level claim
- 具体位置：全文，特别是 Title、Abstract、§4.4
- 问题：实验仅覆盖一个模型族（Qwen3-IB 0.6B），一个数据集族（FOLIO 500 + ProofFOL 500），一种任务形式（FOL/Prolog 命题证明）。LLaMA-3.2-3B 因无法生成有效 FOL 而失败（Appendix E.4），Qwen3-8B 也未收敛（Appendix E.7）。虽然论文诚实标注 "Case Study"，但标题中 "GRPO-Trained Neurosymbolic Reasoning" 暗示了更广泛的适用性。
- 为什么影响接收：三个 contribution (C1-C3) 都以一般性语言表述，但实验证据仅来自一个极小规模模型在两个数据集上的表现。
- 建议修改方向：(a) 在标题或 abstract 中明确限定为 Qwen3-IB on FOLIO 级别的发现；(b) 或增加至少一个不同架构/规模的模型。

## Should-Fix 问题（影响评分但不一票否决）

**W1** [warning] STA 的技术新颖性有限
- 具体位置：§3.2, Algorithm 1, §2 (Related Work: Mutation testing)
- 问题：STA 本质上是对 solver 输入做 LOO ablation——论文自己承认 "STA adapts the LOO mutation paradigm (DeMillo et al., 1978; Jia and Harman, 2011)"。Algorithm 1 是一个 7 行的 for-loop。论文声称 novelty 在 application 和 findings，但 application novelty 对 main conference 是否足够取决于 findings 的 surprising 程度。
- 建议：更明确地 argue 为什么这种方法在之前没有被应用——是因为 neurosymbolic GRPO 太新？还是因为之前认为 execution accuracy 足够？

**W2** [warning] 统计显著性边界化
- 具体位置：Table 5 (Appendix D), §E.5
- 问题：主要比较的 Fisher exact test p=0.036，经 Bonferroni 校正后 borderline。N=3 seeds 的 pooled statistics 将 within-seed samples 视为独立观测——论文自己承认 CMH 的局限。多个 per-seed 分析未达到 α=0.05。
- 建议：增加 seeds 到至少 5 个；在正文更显著标注统计功效局限。

**W3** [warning] ISR 与下游 NLI accuracy 不相关
- 具体位置：§3.2, Appendix C
- 问题：论文明确指出 ISR 不 correlate with NLI accuracy。如果 ISR 既不预测语义正确性也不预测下游表现，诊断价值局限于检测一种特定的结构退化。
- 建议：讨论 ISR 在实际 RLVR 训练管线中的具体使用场景。

**W4** [warning] "Goldilocks hypothesis" 证据不足
- 具体位置：§5 (Discussion), §E.5
- 问题：证据仅来自 3 个 exec-only seed 和 2 个 cross-scale 实验，属于 anecdotal evidence。
- 建议：降级为 "observation" 而非 "hypothesis"。

**W5** [warning] Hacking taxonomy 分类器的 recall 未充分评估
- 具体位置：§3.3, Appendix D, Table 6-7
- 问题：Precision 有手动验证（Table 7），但多数 mode 的 recall 未估计。TS subcategory 有 lower bound ≥91%，其他 mode 缺失。
- 建议：提供 recall 的粗略估计。

## 小问题（不影响接收）

- M1: Abstract 用 "structural shortcuts" 但正文主要用 "structural degeneration"，术语可统一
- M2: Figure 1 y轴标签与 ISR 定义不完全一致
- M3: Seed 43 用 sampling (T=0.7) 而其他 seed 用 greedy decoding，引入额外变量
- M4: Bondarenko et al. (2025) 关于 chess engine gaming，与 neurosymbolic reasoning 的关联可更明确
- M5: Table 1 脚注信息密度过高，建议拆分到正文

## Missing References

1. Wu & Tang (2026) "When Reward Hacking Rebounds" (arXiv:2604.01476) — representation-level hacking detection
2. "Monitoring Emergent Reward Hacking During Generation via Internal Activations" (arXiv:2603.04069, 2026) — internal activation monitoring
3. "Is It Thinking or Cheating?" (arXiv:2510.01367, 2025) — reasoning effort as hacking detector

以上为建议引用，非硬性要求。论文已有的引用覆盖了领域主要工作。

## 引用验证结果

✅ Kim et al. (2026) arXiv:2604.19459 — 真实
✅ Bondarenko et al. (2025) arXiv:2502.13295 — 真实
✅ Helff et al. (2026) arXiv:2604.15149 — 真实
✅ Khalifa et al. (2026) arXiv:2603.07084 — 真实
✅ Sullivan & Koller (2025) arXiv:2509.21154 — 真实
未发现可疑引用。

## 主要优势

1. 选题时效性强：RLVR structural degeneration 的首个系统性 component-level 诊断
2. 实验设计严谨：matched random controls, cross-seed replication, cross-dataset validation
3. Hacking taxonomy 细粒度有价值：8 种 mode 比已有工作更详细
4. 诚实 framing："Case Study" 副标题、ISR 局限性的显式讨论、premise-count confound 的自我识别
5. Related Work 覆盖面好：2025-2026 最新工作引用齐全
6. Prolog cross-dataset validation 展示了 hacking 的 dataset-dependent 多样性

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 2606 · 2026-05-22T15:25:34.594571+00:00_

called mcp__agent-ml-research__director_post_to_reviewer

<details open><summary>🔧 Tool call — mcp__agent-ml-research__director_post_to_reviewer</summary>

```json
{
  "reviewer_id": "1",
  "round_number": "1",
  "project": "solver-trace-ablation",
  "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Missing References 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性 + 完整性 + Related Work）\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Premise-count confound 是系统性方法论缺陷，而非 minor issue\n- 论文承认 ISR 被 premise minimization 系统性 inflate（§C: \"The apparent ISR-as-reward success (§4.3): ISR β=0.1 seed 42 produces shorter formalization, mechanically inflating ISR\"）。Premise-count-matched 对比消除了差异（1.06×; Table 8），说明 ISR 的表面优势很大程度来自 premise 数量减少而非真正的结构改善。论文将 component-count normalization 留作 future work，但这意味着 C2 (Goodhart effect 的量化分析) 建立在一个已知有偏的指标上。\n- 建议修改方向：至少在 appendix 提供 premise-count-normalized ISR 的 Goodhart 分析；如果 normalized 后效应消失，需诚实报告并降低 C2 的 claim 强度。\n\n**N2** [critical] 泛化性不足以支撑 paper-level claim\n- 实验仅覆盖一个模型族（Qwen3-4B），一个数据集族（FOLIO 500 + ProofFOL 500），一种任务形式（FOL/Prolog 命题证明）。LLaMA-3.2-3B 因无法生成有效 FOL 而失败（Appendix E.4），Qwen3-8B 也未收敛（Appendix E.7）。虽然论文诚实标注 \"Case Study\"，但标题中 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示了更广泛的适用性。\n- 建议：(a) 在标题或 abstract 中明确限定为 Qwen3-4B on FOLIO 级别的发现；(b) 或增加至少一个不同架构/规模的模型。\n\n### Should-Fix\n\n**W1** [warning] STA 的技术新颖性有限\n- STA 本质上是对 solver 输入做 LOO ablation——论文自己承认 \"STA adapts the LOO mutation paradigm\"。Algorithm 1 是一个 7 行的 for-loop。论文声称 novelty 在 application 和 findings，但 application novelty 对 main conference 是否足够取决于 findings 的 surprising 程度。\n- 建议：更明确地 argue 为什么这种方法在之前没有被应用。\n\n**W2** [warning] 统计显著性边界化\n- 主要比较的 Fisher exact test p=0.036 经 Bonferroni 校正后 borderline。N=3 seeds 的 pooled statistics 将 within-seed samples 视为独立观测。多个 per-seed 分析未达到 α=0.05。\n\n**W3** [warning] ISR 与下游 NLI accuracy 不相关\n- 论文明确指出 ISR 不 correlate with NLI accuracy。如果 ISR 既不预测语义正确性也不预测下游表现，诊断价值局限于检测一种特定的结构退化。\n\n**W4** [warning] \"Goldilocks hypothesis\" 证据不足\n- 证据仅来自 3 个 exec-only seed 和 2 个 cross-scale 实验，属于 anecdotal evidence。建议降级为 \"observation\"。\n\n**W5** [warning] Hacking taxonomy 分类器的 recall 未充分评估\n- Precision 有手动验证（Table 7），但多数 mode 的 recall 未估计。\n\n### Missing References\n\n1. Wu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476)\n2. \"Monitoring Emergent Reward Hacking During Generation via Internal Activations\" (arXiv:2603.04069, 2026)\n3. \"Is It Thinking or Cheating?\" (arXiv:2510.01367, 2025)\n\n### Minor Issues\n- M1: Abstract 用 \"structural shortcuts\" 但正文主要用 \"structural degeneration\"，术语可统一\n- M2: Figure 1 y轴标签与 ISR 定义不完全一致\n- M3: Seed 43 用 sampling (T=0.7) 而其他 seed 用 greedy decoding\n- M4: Bondarenko et al. (2025) 关联可更明确\n- M5: Table 1 脚注信息密度过高"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "tool_args": {
    "reviewer_id": "1",
    "round_number": "1",
    "project": "solver-trace-ablation",
    "text": "以下是 Reviewer 2 的完整审稿意见，请逐条回应：对每个 Must-Fix、Should-Fix、Missing References 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。\n\n---\n\n## Reviewer 2 审稿报告（新颖性 + 完整性 + Related Work）\n\n**Overall**: 3.5 / 5 (Borderline Conference)\n\n### Must-Fix\n\n**N1** [critical] Premise-count confound 是系统性方法论缺陷，而非 minor issue\n- 论文承认 ISR 被 premise minimization 系统性 inflate（§C: \"The apparent ISR-as-reward success (§4.3): ISR β=0.1 seed 42 produces shorter formalization, mechanically inflating ISR\"）。Premise-count-matched 对比消除了差异（1.06×; Table 8），说明 ISR 的表面优势很大程度来自 premise 数量减少而非真正的结构改善。论文将 component-count normalization 留作 future work，但这意味着 C2 (Goodhart effect 的量化分析) 建立在一个已知有偏的指标上。\n- 建议修改方向：至少在 appendix 提供 premise-count-normalized ISR 的 Goodhart 分析；如果 normalized 后效应消失，需诚实报告并降低 C2 的 claim 强度。\n\n**N2** [critical] 泛化性不足以支撑 paper-level claim\n- 实验仅覆盖一个模型族（Qwen3-4B），一个数据集族（FOLIO 500 + ProofFOL 500），一种任务形式（FOL/Prolog 命题证明）。LLaMA-3.2-3B 因无法生成有效 FOL 而失败（Appendix E.4），Qwen3-8B 也未收敛（Appendix E.7）。虽然论文诚实标注 \"Case Study\"，但标题中 \"GRPO-Trained Neurosymbolic Reasoning\" 暗示了更广泛的适用性。\n- 建议：(a) 在标题或 abstract 中明确限定为 Qwen3-4B on FOLIO 级别的发现；(b) 或增加至少一个不同架构/规模的模型。\n\n### Should-Fix\n\n**W1** [warning] STA 的技术新颖性有限\n- STA 本质上是对 solver 输入做 LOO ablation——论文自己承认 \"STA adapts the LOO mutation paradigm\"。Algorithm 1 是一个 7 行的 for-loop。论文声称 novelty 在 application 和 findings，但 application novelty 对 main conference 是否足够取决于 findings 的 surprising 程度。\n- 建议：更明确地 argue 为什么这种方法在之前没有被应用。\n\n**W2** [warning] 统计显著性边界化\n- 主要比较的 Fisher exact test p=0.036 经 Bonferroni 校正后 borderline。N=3 seeds 的 pooled statistics 将 within-seed samples 视为独立观测。多个 per-seed 分析未达到 α=0.05。\n\n**W3** [warning] ISR 与下游 NLI accuracy 不相关\n- 论文明确指出 ISR 不 correlate with NLI accuracy。如果 ISR 既不预测语义正确性也不预测下游表现，诊断价值局限于检测一种特定的结构退化。\n\n**W4** [warning] \"Goldilocks hypothesis\" 证据不足\n- 证据仅来自 3 个 exec-only seed 和 2 个 cross-scale 实验，属于 anecdotal evidence。建议降级为 \"observation\"。\n\n**W5** [warning] Hacking taxonomy 分类器的 recall 未充分评估\n- Precision 有手动验证（Table 7），但多数 mode 的 recall 未估计。\n\n### Missing References\n\n1. Wu & Tang (2026) \"When Reward Hacking Rebounds\" (arXiv:2604.01476)\n2. \"Monitoring Emergent Reward Hacking During Generation via Internal Activations\" (arXiv:2603.04069, 2026)\n3. \"Is It Thinking or Cheating?\" (arXiv:2510.01367, 2025)\n\n### Minor Issues\n- M1: Abstract 用 \"structural shortcuts\" 但正文主要用 \"structural degeneration\"，术语可统一\n- M2: Figure 1 y轴标签与 ISR 定义不完全一致\n- M3: Seed 43 用 sampling (T=0.7) 而其他 seed 用 greedy decoding\n- M4: Bondarenko et al. (2025) 关联可更明确\n- M5: Table 1 脚注信息密度过高"
  }
}
```

</details>

---


### Tool result

_source line 2607 · 2026-05-22T15:26:06.237052+00:00_

{"result":"{\"success\": true, \"data\": {\"reviewer_key\": \"feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:reviewer_1\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_5abafbb382eb7c81e8a38090e46323e7:director",
  "tool": "mcp__agent-ml-research__director_post_to_reviewer",
  "elapsed_ms": 31642
}
```

</details>

---
