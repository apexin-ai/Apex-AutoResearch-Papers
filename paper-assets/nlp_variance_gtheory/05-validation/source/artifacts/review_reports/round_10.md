---
round: 10
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-25T21:41:00.416972+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 11 (Fresh Review)

**项目**: nlp_variance_gtheory
**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models
**目标 venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性 + 实验设计; R2: 新颖性 + 完整性 + 写作质量）
**审稿流程**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即达共识）

---

## Summary

本文将教育测量领域的概化理论（G-theory）系统应用于 LLM 评估，通过 Henderson Method I 对 8 个 7–9B 开源模型在 5 个 benchmark 上约 230 万条二值记录进行方差分量分解。核心发现：model×item 交互是主导非残差方差源（MC 30–36%, FF 15–17%），表明模型主要在"哪些题目难"上分歧而非整体能力差异。D-study 投影将可复现性预算从 552 降至 178 items（3-prompt × 3-seed 设计），但总评估量相应增长 2.9×。论文附有 9 项稳健性检验和开源 G-theory pipeline。

---

## Strengths

**S1 [方法新颖性]** 首次将 G-theory 完整工作流（G-study + D-study budgets）系统应用于 LLM 评估。相比 Messing (2026) 的 5 facets × 1 benchmark，扩展到 7 facets × 5 benchmarks + D-study 预算投影，填补了跨格式方差比较和可操作预算建议的空白。[AGREE: R1-S1, R2-S1]

**S2 [实验规模]** 7 facet × 8 model × 5 benchmark 的全因子/准全因子设计（exp-001: 460,800 records; exp-002: 2,304,000 records）是该领域迄今最大规模的多面交叉方差分析。设计矩阵（Table 2）清晰可复现。[AGREE: R1-S2, R2-S1]

**S3 [稳健性检验]** Appendix A 提供 9 项独立稳健性分析（GLMM ρ=1.0、REML <0.5pp、probit simulation、null calibration ratio=1.0008、LOMO max|ΔG|=0.030、accuracy-range stability r=−0.048、CI method comparison、facet specification sensitivity、reduced crossing validation ΔG=0.0008），系统覆盖估计方法、数据分布、样本稳定性。两位 Reviewer 一致认为"堪称典范"。[AGREE: R1-S3, R2-S3]

**S4 [核心洞察]** model×item 交互主导（§4.2, Table 5）是非直觉但重要的发现。MMLU 学科粒度分析（Table 12）验证了 knowledge vs. reasoning 维度的梯度（G_item: 0.614–0.930）。[AGREE: R1-S4, R2 implicitly via S2]

**S5 [IRT+G-theory 互补性]** Table 7 中 IRT 116 items 在 single-condition 下 G=0.457、multi-facet 下 G=0.895，证明 item selection 和 protocol optimization 是正交的独立优化维度。两位 Reviewer 一致认为这是全文最有说服力的单一结果。[AGREE: R1-S5, R2-S5]

**S6 [实用产出]** 开源 G-theory pipeline 和 D-study calculator、推荐的 3×3 设计方案（§4.5）、per-benchmark 预算表（Table 9）具有直接实用价值。[AGREE: R1-S5, R2-S2]

**S7 [Binary data 透明度]** §3.5 明确标注 binary scoring 假设，probit simulation 量化 binarization 代价（+36% budget），partial-credit 和 text-exact-match 对比展示 metric conditionality。[AGREE: R1-S6, R2-S4]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1 [critical]: "10× fewer items" framing 隐藏总评估量增长** [R2-W1, R1 AGREE]
- Abstract 仅报告 item reduction（"from over 1,000 to roughly 100"），未提 total evaluations 增长
- Full multi-facet: items 552→55 (10×)，但 total evaluations 552→71,280 (129×)
- 推荐的 3×3 设计在 §4.5 已披露 "2.9× total-evaluation increase for a 3.1× item reduction"，但 abstract 和 Figure 1 overview 未提及
- R1 补充：severity 介于 critical/warning，因正文已披露且 3×3 的 2.9× overhead 在实际 GPU 时间上可接受
- **修改要求**: Abstract 和 Contribution C1 中对称报告 item reduction 和 total evaluation overhead（至少对推荐的 3×3 设计）

**MF-2 [critical]: Binary scoring scope 未在 title/abstract 中充分限定** [R2-W2, R1 AGREE]
- Title "Reproducibility Budgets for Open-Weight LLM Evaluation" 暗示通用适用性
- 但所有发现严格受限于 binary correctness scoring
  - Text-exact-match: G 0.936 → 0.007（方差结构完全改变）
  - Partial-credit (GSM8K): G 0.86 → 0.77（显著退化）
- R1 补充：MC benchmarks 的 binary scoring 是标准做法，问题主要在 FF benchmarks 和更广泛的评测场景（code generation、open-ended QA、LLM-as-judge、preference ranking）
- **修改要求**: Title 添加限定语（如 "under Binary Correctness Scoring"）或 abstract 首段明确声明 scope；§3.5 增加不适用场景列表

**MF-3 [critical]: G_item 与 model ranking reliability 之间的概念鸿沟** [R2-W3 critical, R1-W6 warning → 交叉后 R2 建议升级为 near-critical, R1 AGREE]
- 论文以 items 为 object of measurement（§3.1），G_item 衡量 item-level 跨条件泛化能力
- 但 benchmark 用户关心的是 model ranking reliability: "用 178 items 排出的模型顺序是否可重复？"
- G_item ≥ 0.80 保证 item scores 在不同 prompt/seed 下一致，**不直接等同于** model ranking 稳定
- 论文提供间接证据（LOMO Table 4: max|ΔG|=0.030; κ=0.33–0.46），但未直接量化 model ranking stability
- R1 解释：当 model×item (30–36%) >> model main effect (3–5%)，model ranking stability 会低于 G_item 所暗示的水平
- **修改要求**: 补充 model ranking stability 分析（G_model 计算、Kendall's W 或 bootstrap 排名一致性）；讨论 G_item ≥ 0.80 蕴含 model ranking reliability 的条件

**MF-4 [critical]: 格式关联模式在结论中从 "exploratory" 升级为 "established"** [R1-W1, R2-W4 → 双向 AGREE on Conclusion overclaim]
- §4.3 明确标记为 "exploratory" 和 "descriptive observation"（permutation p=0.10, n=5, benchmark-level CI spans zero）
- 但 §5 Conclusion 写 "The variance structure is format-dependent...motivating per-format budget calibration"，完全去掉了 "exploratory" 限定词
- Table 9 按 MC/FF 分列 D-study 预算，实际上将 p=0.10 的探索性发现用于实践推荐
- **修改要求**: Conclusion 保留 "exploratory/preliminary" 限定词；Table 9 加注 "based on n=5 benchmarks; format-specific calibration requires replication"；C3 降级标注 "preliminary"

**MF-5 [critical]: Bootstrap CI 仅捕获 item-level 不确定性，D-study 预算 CI 被低估** [R1-W2, R2 AGREE with nuance]
- Table 9 的 95% CI（如 MMLU: [76, 116]）仅反映 item-level resampling
- LOMO max|ΔG|=0.030 对应 ~23% 预算变化（Appendix B Figure 9），但 model-level uncertainty 从未与 item-level CI 联合量化
- 论文自己承认："Bootstrap CIs capture item-sampling variability conditional on these 8 specific models"（Appendix A）
- R2 补充 nuance：n_model=8 做 model-level bootstrap 方差极大，更实用做法是报告 sensitivity band
- **修改要求**: Table 9 标题/脚注标注 CI 仅反映 item-level variability；正文讨论 combined uncertainty 量级（item CI ~20% + model uncertainty ~23%）

### Should-Fix（影响评分但不一票否决）

**SF-1 [warning]: Model 作为 quasi-random facet 的辩护链不完整** [R1-W3, R2 AGREE]
- 引用 Meredith (1993)/Putnick (2016) 不恰当（关于 measurement invariance，非 facet sampling）
- LOMO 和 four-model subset 是 within-sample stability checks，不等于 out-of-sample generalization
- FF 的 7.3% error（MATH, Table 11）是非 trivial 偏差
- Fixed vs. random 对比（Table 10: ΔG=0.077–0.113）的保守性论证有效，但核心问题不在 specification 而在 representativeness
- **修改建议**: 替换引用为 Brennan (2001 Ch.4-5)；讨论 exchangeability 假设的可检验条件；单独讨论 FF benchmarks 较大预测偏差

**SF-2 [warning]: D-study 投影的时间不变性假设未被讨论** [R1-W4, R2 AGREE]
- §4.5 仅一句话 "All projections assume the 2024–2025 model generation"
- Scale validation (§4.6) 检验参数规模泛化，但无时间维度证据
- LLM 架构和训练数据变化极快，model×item interaction 可能随模型同质化下降
- **修改建议**: 增加一段讨论哪些方差分量最可能随模型代际变化，以及对预算的影响方向

**SF-3 [warning]: Partial-credit 影响被低估且仅 GSM8K 单 benchmark 验证** [R1-W5 + R2-W7, 双向 AGREE]
- GSM8K partial-credit G 从 0.86 降至 0.77（ΔG=−0.135），降幅超过许多论文中详细讨论的效应
- 48.1% incorrect responses 有正确中间步骤但错误问题理解（Appendix A）
- 仅 GSM8K 一个 benchmark 的 step-level partial credit，MATH 未分析
- 现实中越来越多 LLM 评估采用 partial-credit 或连续评分
- **修改建议**: 限定为 "GSM8K step-level partial credit 下初步观察到"；正文（而非仅附录）更 prominently 讨论 partial-credit 影响

**SF-4 [warning]: Conclusion 缺乏 practical adoption pathway** [R2-W6, R1 部分 REBUT — 分歧]
- §5 仅 4 句话，覆盖核心结论和 3 条实践建议，但缺少：benchmark 开发者如何集成 G-theory pipeline、leaderboard 影响、IRT pipeline 集成路径、future work
- R1 认为 8 页限制下简洁合理，但同意可加 1-2 句 adoption pathway
- **修改建议**: 至少增加 1-2 句 practical adoption pathway

**SF-5 [warning]: Table 6 caption 中 MC vs FF 报告不同统计量** [R2-W5, R1 AGREE]
- "prompt†" 行对 MC 报告 prompt×item interaction，对 FF 报告 prompt main effect
- 同一行代表不同统计量，违反表格一致性原则
- **修改建议**: 拆为两行（prompt_main, prompt×item），或用更清晰标注

**SF-6 [warning]: Table 1 与 Messing (2026) 的 positioning 对比需注明范式差异** [R2-W12, R1 AGREE]
- Messing: LLM-as-judge, single benchmark, judge identity 43.8%
- 本文: generation-based scoring, 5 benchmarks
- 简单的 facet 数量对比（5 vs 7）可能高估增量贡献
- **修改建议**: Table 1 caption 加注评测范式差异

### Minor（不影响接收）

**M-1**: Abstract 约 201 词，超 EMNLP 2026 的 200 词硬性限制。必须删减。[R2-W9, R1 AGREE]

**M-2**: Abstract 数字密度（20+ 数值）是否影响可读性——分歧。R2 认为应精简至 3-4 个；R1 认为 methods paper 惯例允许。[R2-W10, R1 REBUT]

**M-3**: `\enlargethispage{1\baselineskip}` 排版 hack，实际投稿常见但可能引起格式审查。[R2-W11, R1 AGREE]

**M-4**: "quasi-random facet" 非 G-theory 标准术语，应改用 "treated as random" 并引用 Brennan (2001 Ch.4)。[R1-M3, R2 AGREE]

**M-5**: Benchmark contamination 机制未讨论：contamination 使所有模型答对的 items 的 model×item=0，可能系统性低估 clean benchmarks 上的 model×item 比例。[R1-M4, R2 W8]

**M-6**: exp-002 reduced crossing validation 仅基于 MMLU，其他 4 个 benchmark 的 precision×benchmark 交互无法检验。[R1-M1]

---

## Reviewer Consensus（所有 Reviewer 达成共识的关键问题）

| # | 问题 | 状态 | R1 | R2 |
|---|------|------|-----|-----|
| 1 | "10× fewer items" framing 隐藏 total eval 增长 | [AGREE] | W1 触及→AGREE R2-W1 | W1 critical |
| 2 | Binary scoring scope 未限定 | [AGREE] | AGREE R2-W2 | W2 critical |
| 3 | G_item vs model ranking 概念鸿沟 | [AGREE] | W6 warning→AGREE R2-W3 | W3 critical |
| 4 | Format pattern Conclusion overclaim | [AGREE] | W1 critical | W4 warning→AGREE R1-W1 |
| 5 | Bootstrap CI 仅 item-level | [AGREE] | W2 critical | AGREE with nuance |
| 6 | Quasi-random facet 辩护不完整 | [AGREE] | W3 warning | AGREE |
| 7 | D-study temporal invariance 未讨论 | [AGREE] | W4 warning | AGREE |
| 8 | Partial-credit 单 benchmark + 影响低估 | [AGREE] | W5 warning | W7 warning + AGREE |
| 9 | Table 6 混合统计量 | [AGREE] | AGREE R2-W5 | W5 warning |
| 10 | Abstract 超 200 词限制 | [AGREE] | AGREE | W9 minor |

---

## Reviewer Divergence（分歧点及各方理由）

| # | 问题 | R1 立场 | R2 立场 | 解读 |
|---|------|---------|---------|------|
| 1 | §4.3 format-associated 占 ~1 页是否失衡 | [REBUT] 描述性价值足够，Figure 7-8 提供机制解释（difficulty dispersion, ρ=0.82），MMLU subject-level (n=10, p=0.005) 提供 converging evidence | [AGREE] 应压缩为一段，Figure 7-8 移入 appendix | 非关键分歧：两位均同意 Conclusion 应保留 "exploratory"，分歧仅在 §4.3 正文篇幅。R1 的 mechanism interpretation 论证有一定说服力 |
| 2 | Conclusion 是否需要扩展 | [REBUT] 8 页限制下简洁合理，但同意加 1-2 句 adoption pathway | 应扩展至 2-3 段，含 benchmark 开发者建议、future work | 非关键分歧：两位均同意至少需要 adoption pathway 讨论 |
| 3 | Abstract 数字密度 | [REBUT] Methods paper 惯例允许高数值密度 | 建议保留 2-3 个核心数值 | 风格分歧，非实质性问题 |
| 4 | MMLU-Redux/Pro 是否为 critical omission | [REBUT] 与方差分解框架关联有限，200-item stratified sample 已控制质量 | MMLU-Redux 影响 item-level 方差分解解读 | R2 的论点更有说服力：如果部分 MMLU items 标注错误，item difficulty 方差分解混入数据质量伪影 |

---

## Questions（需要作者澄清）

**Q1 [R1-Q1, R2-Q1]**: G_item ≥ 0.80 在什么条件下保证 model ranking stability？如果用户仅评估 1 个模型，D-study 预算应如何调整？（§4.1 单模型分析与 Table 9 cross-model 分析使用不同方差结构，论文应更明确区分这两个使用场景。）

**Q2 [R1-Q2]**: Probit simulation ρ=0.732 支持 ranking recovery 但不支持精确定量估计。binarization +36% budget 论证了保守性（误差方向安全），但 D-study 预算的 quantitative precision 如何评估？

**Q3 [R2-Q2]**: 推荐的 3×3 设计（178 items × 9 conditions = 1,602 evaluations）在单 GPU 上的实际 wall-clock time？对需评估大量模型的 leaderboard 是否可行？

**Q4 [R1-Q3]**: Scale validation 仅覆盖 dense architectures（Qwen, Llama）。MoE 架构（Mixtral, DeepSeek-MoE）的 routing 机制可能引入额外 model×item 交互，是否有任何 MoE 证据？

**Q5 [R1-Q4]**: Ordering facet 在非 MMLU benchmarks 上 σ²=0——论文已说明 "retained for design balance"（§3.3），但 ARC/HellaSwag（MC）的 few-shot demo ordering 可能影响 in-context learning，未变异 ordering 意味着这两个 benchmark 可能低估了 ordering-related 交互。

---

## Missing References

**两位 Reviewer 共识：**
- Cronbach, L. J., Gleser, G. C., Nanda, H., & Rajaratnam, N. (1972). *The Dependability of Behavioral Measurements*. — G-theory 奠基文献，应引用
- Contamination 检测文献 (如 Shi et al. 2023, Golchin & Surdeanu 2024) — Limitations 提及 contamination 但未引用

**R2 建议（R1 部分同意）：**
- MMLU-Redux (Gema et al., 2024) — 识别 MMLU 错误标注，可能影响 item-level 方差分解解读
- MMLU-Pro (Wang et al., 2024) — 10 选项 MMLU 变体，降低 guessing variance

**R1 建议（R2 部分同意）：**
- Webb, Shavelson, & Haertel (2006) — G-theory 在 non-standard data 上的应用综述

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用）。

---

## Visual Layout Check（非评分项）

状态：**已完成** (2026-05-25T21:18–21:21, 约 3 分钟)

**Warnings (3):**
1. **Page 15**: 末页大面积空白（~85% 留白）。Appendix H "Use of AI Assistants" 仅 3 个 bullet point，页面利用率极低。建议与前一个 appendix 合并。
2. **Page 7**: 单页 4 个 display items（Table 5, Table 6, Figure 7, Figure 8），视觉密度过高。Figure 7 尺寸偏小，bar label 和 axis text 打印时可能难以辨认。
3. **Page 8**: 3 张表格（Tables 7-9）+ Conclusion + Limitations 挤在同一页，排版紧凑。Table 8 行间距窄。

**Info (10):**
- Figure 1（page 2）pipeline 概览图位置合理，色块区分清晰，title-abstract-figure story 一致
- Figure 6 heatmap（page 6）数值标注已有（好），但字号偏小（~7pt），灰度打印颜色区分度可能不足
- Figure 3（page 3）信息密度偏低，可考虑与 Table 1 合并
- Pages 10-11 Appendix A 连续纯文本无 display item，可读性一般
- 正文 8 页 17 个 display items（~2.1/页），总量偏多
- 所有表格使用 booktabs 风格，格式专业统一
- 公式渲染正确，无 LaTeX 错误或 margin 溢出
- 参考文献格式统一，无未解析引用
- 无 section heading 孤悬页底

---

## Overall Assessment

### 评分: **3.5** (Borderline Conference)

| 维度 | R1 | R2 | 合并 |
|------|-----|-----|------|
| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
| Excitement | 3.5/5 | 3.0/5 | **3.25/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4/5 | 4/5 | **4/5** |

### 总评理由

本文在方法论框架（G-theory→LLM evaluation）、实验规模（2.3M records, 7 facets × 8 models × 5 benchmarks）和稳健性检验（9 项）方面达到高标准。核心发现（model×item interaction dominance + D-study budgets + IRT 互补性）具有实用价值和理论启发性。

将其评为 **Borderline Conference (3.5)** 而非 Conference (4.0) 的原因是五个 Must-Fix 问题的叠加：

1. **Framing 失衡**: "10× fewer items" 隐藏了 total evaluations 增长（MF-1），format-associated pattern 从 exploratory 升级为 established（MF-4）——presentation 问题而非 methodological flaws
2. **Scope 限制**: Binary scoring 的严格限定未在 title/abstract 中体现（MF-2），使论文的适用范围比表面呈现的窄得多
3. **概念鸿沟**: G_item 与 model ranking reliability 之间的映射缺乏直接分析（MF-3），使核心实用价值——"reproducibility budgets"——的解释框架不完整
4. **CI 透明度**: D-study 预算的 CI 仅反映 item-level uncertainty，model-level uncertainty 未被联合量化（MF-5）

**关键判断**: 所有 Must-Fix 问题均为 framing/scope/presentation 问题或可通过补充分析解决，而非基础方法论缺陷。论文的实验设计、方差分解方法论和稳健性检验本身是扎实的。如果修订中解决 MF-1 至 MF-5 并改善 SF-1 至 SF-6，本文有清晰的路径达到 **Conference (4.0)** 水平。当前版本是 **strong Findings candidate**。

---

## Detailed Comments

### 按优先级排列的修改路线图

**P0 (修改后可达 4.0 的关键项)**:
1. Abstract + C1: 对称报告 item reduction 和 total evaluation overhead（MF-1）
2. Title 或 abstract 首段: 明确 binary scoring scope（MF-2）
3. §4.5 或新 Discussion: 补充 G_model 计算或 model ranking stability 分析（MF-3）
4. §5 Conclusion: 保留 "exploratory" 限定词；Table 9 加注（MF-4）
5. Table 9 标题/脚注: 标注 CI 仅反映 item-level variability（MF-5）

**P1 (显著改善论文质量)**:
6. §3.6: 替换 Meredith/Putnick 引用为 Brennan (2001 Ch.4-5)，讨论 exchangeability 条件（SF-1）
7. §4.5 或 Limitations: 增加方差分量 temporal stability 讨论（SF-2）
8. §3.5: 将 partial-credit 限定为 "GSM8K step-level" 初步观察（SF-3）
9. §5: 增加 1-2 句 practical adoption pathway（SF-4）
10. Table 6: 拆行或改善标注（SF-5）

**P2 (Polish)**:
11. Abstract 删减至 ≤ 200 词（M-1，格式硬约束）
12. 补充 Cronbach et al. (1972)；考虑 MMLU-Redux（M-5, Missing Refs）
13. "quasi-random" → 标准术语（M-4）
14. 讨论 contamination 对 model×item 估计的方向性影响（M-5）