# Reviewer 2 coordination — Part 2 of 2

**Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models** · Conversation logs

[← Part 1](part-001.md) · [Transcript overview](../reviewer-2-coordination.md) · [Structured JSON](../../../sessions/34/342fb8967df976c78279.json)

## Round 14

### Tool call

_source line 564 · 2026-05-22T14:40:14.500840+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 的逐条交叉回应\n\n---\n\n## Must-Fix\n\n### [AGREE] R1-N1: Model exchangeability 论证存在关键缺口\n\nR1 的核心论点成立。论文在 Section 3.1 (p.3) 明确承认 8 个模型是 purposively selected 并引用 Meredith (1993) 和 Pautick & Brennan (2016) 作为 quasi-random facet 的理论支撑，但引用本身不能替代实证验证。\n\nR1 对三个证据的批评合理：\n- **LOMO** (Table 5, Appendix A, p.11, CV ≤ 1.25%)：证明内部一致性（移除任一模型后 G 稳定），不证明对 model universe 的代表性。\n- **Forward prediction** (4→8, |ΔG| = 0.035)：从同一 8-model pool 的子集预测全集，属 within-sample interpolation 而非 out-of-sample generalization。R1 对此性质的判定准确。\n- **Limitations (Section 6)** 承认了范围限制（\"results may not generalize to API-based, base, or >9B models\"），但 Section 4.5 和 Section 5 的 D-study 建议未附带明确的 universe 限定。\n\n**补充观察**：Table 2 (p.6) 中 model 主效应仅 2.5%，反映 7-9B instruct 模型内的窄能力范围。若加入能力差异更大的模型（如 1B/70B），model variance 增加会同时改变 model×item 交互结构（当前 30.2%），D-study budgets 可能需要根本性调整。这与我的 W2 高度一致。\n\n值得注意的是 Appendix A Table 6 (p.12) 对比了 random vs fixed model 的 G 系数（ΔG = 0.077-0.113），表明 random model 假设产生 conservative budgets。这提供了一定的 sensitivity 信息，但仍非外部代表性验证。R1 建议的 held-out model validation 是最直接的改进路径。\n\n---\n\n### [AGREE] R1-N2: Format-associated pattern 呈现层级与统计证据强度严重不匹配\n\n这是 R1 审稿中最锐利的观察，我完全同意。\n\n论文在 Section 4.3 (p.7) 自己承认了统计限制：permutation test resolution floor 为 p = 0.10，CI spans zero ([-1.7, 5.1], df = 3)，并使用了 \"descriptive observation\" 措辞。但 R1 精准指出了 **framing 与证据的结构性不匹配**：\n\n1. **Abstract** 中 \"observe a format-associated pattern in variance concentration\" 与经过严格验证的发现（如 precision separability: Section 4.4, ΔG < 0.1%）获得同等叙事权重\n2. **Section 1 Contributions** 将其列为三大贡献之一\n3. **Section 4.3** 获得完整章节 + Table 3 + Figure 3 的呈现空间——与 Section 4.4 (precision separability) 等量\n\n从统计学角度：MC(3) vs FF(2) 的二分法仅有 C(5,2) = 10 种排列，最小 p-value = 1/10 = 0.10，在 α = 0.05 下**设计上就无法拒绝原假设**。这不是 sample size 不够大——是 n = 5 benchmarks 的 fundamental design constraint。\n\n**与我 W5 的关系**：我在自己的审稿中从 \"解释性深度不足\" 角度批评了该分析（未分析 item 特征如何驱动 MC/FF 差异）。R1 从更根本的层面切入——即使解释性分析再深入，n = 5 的统计基础也不支持将其作为论文贡献。R1 的批评比我的更有力。\n\nR1 建议降级为 \"Exploratory observation\" 并在 Abstract 使用更谨慎语言，我完全赞同。\n\n---\n\n## Should-Fix\n\n### [AGREE] R1-W1: Binary scoring limitation 影响可能被低估\n\nR1 精确引用了 Appendix A (p.12) 的 GSM8K partial-credit pilot：prompt variance 从 25.5% → 1.2%，residual 28.2% → 46.6%，G 从 0.770 → 0.553。方差结构发生了**根本性**变化，而非微小调整。\n\nR1 指出的两个关键缺口：\n1. Pilot 仅用 1 个模型（Llama-3.1-8B-Instruct），无法估计 model-related 分量——而 model×item 是 binary scoring 下的第二大方差源（30.2%, Table 2）\n2. Section 5 Conclusion 的 D-study budgets 未限定适用范围为 binary scoring\n\n**补充**：Section 3.5 (p.5) 末尾确实写了 \"D-study budgets do not transfer to finer-grained scoring rubrics\"，但这一关键限定出现在 Binary Data Assumptions 段落末尾，实践者更可能从 Abstract 和 Conclusion 获取行动指南——那里没有此限定。这与我的 W4 高度一致。\n\n---\n\n### [AGREE] R1-W2: D-study projection invariance 假设讨论不充分\n\nR1 提出的三个 invariance 威胁（item pool expansion、model universe expansion、temporal drift）确实未充分展开。\n\n论文在 Section 4.5 (p.8) 说 \"all projections should be treated as order-of-magnitude guides\"，但此 caveat 缺乏量化支撑。这与我的 W2（target universe 窄但 framing 宽）和 R1-N1（model exchangeability）形成共振——三个独立审稿关切指向同一根源问题：D-study 建议的泛化边界不清晰。\n\n---\n\n### [AGREE] R1-W3: 200-item stratified sample 代表性验证不完整\n\nR1 区分 sampling variance 和 representativeness 的方法论观点正确。CV = 3.1% 验证的是重复抽样的稳定性，不证明 10/57 subjects 代表 MMLU 的完整分布。\n\n**但我认为严重程度低于 R1 暗示的**：\n- Appendix A (p.12) 的 reduced crossing validation 显示 exp-002 子集与 exp-001 全设计的 G 差异仅 0.0068\n- 分层抽样覆盖 4 个学科领域（STEM, humanities, social sciences, professional）\n- D-study 建议定位为 \"order-of-magnitude guides\"\n\n整体判断：合理关切但非 critical 级别。\n\n---\n\n### [AGREE] R1-W4: exp-002 跨基准设计不对称性\n\n与我的 Q4 一致。具体问题：\n\n1. **Ordering** 仅在 MMLU 操控（Section 3.3, p.5），其余 4 个 benchmark 不含此 facet\n2. **Prompt template** 在 MC 和 FF 间含义不同：MC 的变体是选项呈现格式（如 \"A/B/C/D\" vs 编号），FF 的变体涉及指令措辞（如 chain-of-thought vs direct，见 Appendix E, p.14）\n\n论文在 Table 3 (p.7) 注释中部分处理了这一问题：MC 中 \"Prompt\" 行报告 prompt main effect（~1%），FF 中报告 prompt main effect 被 residual 吸收（因 free-form generation variability）。但这种解释无法完全消除 **format effect 与 facet-specific effect 的混淆**。\n\n---\n\n## Minor\n\n### [AGREE] R1-M1: seed 42 选择理由\n\n合理问题。Section 3.2 (p.4) 提到 seed 为 \"random seeds, σ = ...\" 但未解释固定 seed 的具体选择。简要说明（如 \"arbitrary fixed seed for CUDA-level nondeterminism control\"）即可。\n\n### [AGREE] R1-M2: Table 2 \"all others: 0.0\" 改 \"<0.1%\"\n\n\"0.0\" 暗示精确为零，实际是四舍五入到一位小数。\"<0.1%\" 更诚实。\n\n### [REBUT] R1-M3: Section 4.6 scale validation 仅 Qwen 家族\n\nR1 说 \"仅 Qwen 家族\"——但 Section 4.6 (p.8) 的标题已是 **\"Preliminary** Scale Validation\"，论文对此分析的定位就是初步验证，而非完整结论。论文也明确写了 \"extensions to 70B+ models remains for future work\"。对一个标注为 \"Preliminary\" 的分析批评其范围不足，标准不对称。\n\n不过，**论文可以更明确说明此验证的局限**——例如 \"本验证仅覆盖 Qwen 架构家族内的 scale 变化，跨架构和跨 scale 的 exchangeability 需要未来工作验证\"。\n\n### [AGREE] R1-M4: Appendix E prompt templates 标注设计理由\n\nAppendix E (p.14) 列出了 6 个 MC 模板和约 6 个 FF 模板，但未解释变体设计背后的理由（如为什么选择 \"A/B/C/D\" vs \"1/2/3/4\" 的选项格式变体，或 \"Let's think step by step\" vs \"Solve this\" 的指令变体）。补充设计理由会增强 prompt universe 的 face validity。\n\n---\n\n## Questions\n\n### R1-Q1: GLMM vs Henderson I 绝对值差异\n\nAppendix A (p.11) 报告 \"all variance components differ by <0.3 percentage points\"，最大差异在 residual (0.47pp)。对于大方差分量（如 item_id = 37.9%），0.3pp 可忽略（<1% 相对误差）。但对于小分量（如 model = 2.5%），0.3pp = 12% 相对误差。**建议论文同时报告绝对值和相对值**以便读者判断实际影响。\n\n### R1-Q2: Model 视为 fixed facet 的影响\n\nAppendix A Table 6 (p.12) 直接回答了此问题：random vs fixed model 的 ΔG = 0.077-0.113。Fixed model 下 G 更高（model variance 不计入误差项），D-study budgets 更宽松。这说明 **random model 假设产生 conservative budgets**——R1 N1 的 exchangeability 担忧在 budget 方向上是安全的（不会导致 over-optimistic 建议），但在方差分解的解释性上仍是缺口。\n\n### R1-Q3: |ΔG| = 0.035 的实际意义\n\n好问题。|ΔG| = 0.035 从 G ≈ 0.935 到 ≈ 0.970（或反向），在 D-study 层面可能对应 10-20% 的 item 数变化。**论文应提供 budget sensitivity 分析**：给定 ΔG = ±0.035，D-study 预算从 55 items 变化到多少？这比仅报告 ΔG 更有实践意义。\n\n### R1-Q4: 多模型 partial-credit 实验\n\n全模型 partial-credit 实验需要定义跨 benchmark 的统一 rubric（GSM8K/MATH 的 step-by-step reasoning evaluation），工作量接近当前论文全文。作为 future work 处理合理。但 **Section 5 Conclusion 应更明确提及此方向**，而非仅在 Appendix A 提及。\n\n### R1-Q5: \"Order-of-magnitude guides\" 的量化含义\n\n同意 R1 的追问。\"Order-of-magnitude\" 在不同领域含义差异大（物理学 = ×10, 工程 = ×2-3）。Section 4.5 (p.8) 中 bootstrap CIs 已提供了 budget 范围（如 \"55-item single-model and 93-item cross-model budgets answer different practical questions. Bootstrap CIs (71-162 items)\"），但**未将此 CI 与 \"order-of-magnitude\" 术语显式关联**。建议明确：order-of-magnitude ≈ 预算的 95% CI 范围（约 ×1.5-3×）。\n\n### R1-Q6: Reduced crossing validation 跨 benchmark 验证\n\nAppendix A (p.12) 的 reduced crossing validation 确实覆盖了 5 个 benchmarks（使用 exp-002 BF16 subset），验证了 reduced crossing 保留方差结构（ΔG = 0.0068）。但 R1 的深层问题——**D-study budget predictions 在每个 benchmark 上的 calibration**——论文未独立验证。Table 7 (Appendix B) 提供了跨 benchmark 的 D-study 预算，但这些是 projections 而非经验验证。\n\n---\n\n## Missing References\n\n### [AGREE] R1-Missing: Cardinet, Johnson & Pini (2010)\n\n\"Applying Generalizability Theory using EduG\" 是 G-theory 应用层面的标准参考，特别是 D-study 设计优化部分。补充此引用会增强论文在教育测量社区的 credibility。\n\nR1 \"未发现 critical missing references\" 的判断我同意。论文的引用覆盖面在同类工作中已属完善。\n\n**补充**：我在自己的审稿中建议补充 lm-evaluation-harness (Gao et al., 2024) 的引用。论文的实践建议（3×3 设计、budget 计算器）应与社区的 de facto 评估工具对话——实践者在 lm-eval-harness 中实施多 facet 设计时会遇到的具体工程约束值得讨论。\n\n---\n\n## 总结：两位 Reviewer 的共识与分歧\n\n**高度共识区域**（两位 Reviewer 独立到达相同结论）：\n1. **Model exchangeability**：R1-N1 ≈ R2-W2——target universe 窄但 framing 宽\n2. **Binary scoring limitation**：R1-W1 ≈ R2-W4——partial-credit 方差结构根本不同\n3. **D-study budget 泛化边界**：R1-W2 ≈ R2-W2——invariance 假设讨论不充分\n4. **跨 benchmark 设计不对称**：R1-W4 ≈ R2-Q4\n\n**R1 独有的强观点**：\n- **N2** (format pattern 统计证据不足): 这是我遗漏的关键角度——n = 5 的 fundamental design constraint 使得 MC/FF 对比在统计上不可能达到显著性。我在 W5 中仅从解释深度批评，R1 从根基切入，更有力。\n\n**R2 独有的强观点**：\n- **W1** (\"10× fewer items\" framing 隐藏总评估量增长): R1 未触及此问题。55 items × 1,296 conditions = 71,280 总评估量 vs single-condition 的 552——这个 129× 的总成本增长在 Abstract 的 framing 中被 \"proportional increase\" 模糊化。论文在 Section 4.5 (p.8) 报告了推荐 3×3 设计的 179 items（总计 1,611 evaluations），但 Abstract 用的是 55-item 数字。\n\n**Overall Assessment 一致性**：两位 Reviewer 均给出 3.5/5 (Borderline Conference)，核心判断一致——实验执行扎实但新颖性有限、关键 claim 的 framing 存在问题。\n",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 的逐条交叉回应\n\n---\n\n## Must-Fix\n\n### [AGREE] R1-N1: Model exchangeability 论证存在关键缺口\n\nR1 的核心论点成立。论文在 Section 3.1 (p.3) 明确承认 8 个模型是 purposively selected 并引用 Meredith (1993) 和 Pautick & Brennan (2016) 作为 quasi-random facet 的理论支撑，但引用本身不能替代实证验证。\n\nR1 对三个证据的批评合理：\n- **LOMO** (Table 5, Appendix A, p.11, CV ≤ 1.25%)：证明内部一致性（移除任一模型后 G 稳定），不证明对 model universe 的代表性。\n- **Forward prediction** (4→8, |ΔG| = 0.035)：从同一 8-model pool 的子集预测全集，属 within-sample interpolation 而非 out-of-sample generalization。R1 对此性质的判定准确。\n- **Limitations (Section 6)** 承认了范围限制（\"results may not generalize to API-based, base, or >9B models\"），但 Section 4.5 和 Section 5 的 D-study 建议未附带明确的 universe 限定。\n\n**补充观察**：Table 2 (p.6) 中 model 主效应仅 2.5%，反映 7-9B instruct 模型内的窄能力范围。若加入能力差异更大的模型（如 1B/70B），model variance 增加会同时改变 model×item 交互结构（当前 30.2%），D-study budgets 可能需要根本性调整。这与我的 W2 高度一致。\n\n值得注意的是 Appendix A Table 6 (p.12) 对比了 random vs fixed model 的 G 系数（ΔG = 0.077-0.113），表明 random model 假设产生 conservative budgets。这提供了一定的 sensitivity 信息，但仍非外部代表性验证。R1 建议的 held-out model validation 是最直接的改进路径。\n\n---\n\n### [AGREE] R1-N2: Format-associated pattern 呈现层级与统计证据强度严重不匹配\n\n这是 R1 审稿中最锐利的观察，我完全同意。\n\n论文在 Section 4.3 (p.7) 自己承认了统计限制：permutation test resolution floor 为 p = 0.10，CI spans zero ([-1.7, 5.1], df = 3)，并使用了 \"descriptive observation\" 措辞。但 R1 精准指出了 **framing 与证据的结构性不匹配**：\n\n1. **Abstract** 中 \"observe a format-associated pattern in variance concentration\" 与经过严格验证的发现（如 precision separability: Section 4.4, ΔG < 0.1%）获得同等叙事权重\n2. **Section 1 Contributions** 将其列为三大贡献之一\n3. **Section 4.3** 获得完整章节 + Table 3 + Figure 3 的呈现空间——与 Section 4.4 (precision separability) 等量\n\n从统计学角度：MC(3) vs FF(2) 的二分法仅有 C(5,2) = 10 种排列，最小 p-value = 1/10 = 0.10，在 α = 0.05 下**设计上就无法拒绝原假设**。这不是 sample size 不够大——是 n = 5 benchmarks 的 fundamental design constraint。\n\n**与我 W5 的关系**：我在自己的审稿中从 \"解释性深度不足\" 角度批评了该分析（未分析 item 特征如何驱动 MC/FF 差异）。R1 从更根本的层面切入——即使解释性分析再深入，n = 5 的统计基础也不支持将其作为论文贡献。R1 的批评比我的更有力。\n\nR1 建议降级为 \"Exploratory observation\" 并在 Abstract 使用更谨慎语言，我完全赞同。\n\n---\n\n## Should-Fix\n\n### [AGREE] R1-W1: Binary scoring limitation 影响可能被低估\n\nR1 精确引用了 Appendix A (p.12) 的 GSM8K partial-credit pilot：prompt variance 从 25.5% → 1.2%，residual 28.2% → 46.6%，G 从 0.770 → 0.553。方差结构发生了**根本性**变化，而非微小调整。\n\nR1 指出的两个关键缺口：\n1. Pilot 仅用 1 个模型（Llama-3.1-8B-Instruct），无法估计 model-related 分量——而 model×item 是 binary scoring 下的第二大方差源（30.2%, Table 2）\n2. Section 5 Conclusion 的 D-study budgets 未限定适用范围为 binary scoring\n\n**补充**：Section 3.5 (p.5) 末尾确实写了 \"D-study budgets do not transfer to finer-grained scoring rubrics\"，但这一关键限定出现在 Binary Data Assumptions 段落末尾，实践者更可能从 Abstract 和 Conclusion 获取行动指南——那里没有此限定。这与我的 W4 高度一致。\n\n---\n\n### [AGREE] R1-W2: D-study projection invariance 假设讨论不充分\n\nR1 提出的三个 invariance 威胁（item pool expansion、model universe expansion、temporal drift）确实未充分展开。\n\n论文在 Section 4.5 (p.8) 说 \"all projections should be treated as order-of-magnitude guides\"，但此 caveat 缺乏量化支撑。这与我的 W2（target universe 窄但 framing 宽）和 R1-N1（model exchangeability）形成共振——三个独立审稿关切指向同一根源问题：D-study 建议的泛化边界不清晰。\n\n---\n\n### [AGREE] R1-W3: 200-item stratified sample 代表性验证不完整\n\nR1 区分 sampling variance 和 representativeness 的方法论观点正确。CV = 3.1% 验证的是重复抽样的稳定性，不证明 10/57 subjects 代表 MMLU 的完整分布。\n\n**但我认为严重程度低于 R1 暗示的**：\n- Appendix A (p.12) 的 reduced crossing validation 显示 exp-002 子集与 exp-001 全设计的 G 差异仅 0.0068\n- 分层抽样覆盖 4 个学科领域（STEM, humanities, social sciences, professional）\n- D-study 建议定位为 \"order-of-magnitude guides\"\n\n整体判断：合理关切但非 critical 级别。\n\n---\n\n### [AGREE] R1-W4: exp-002 跨基准设计不对称性\n\n与我的 Q4 一致。具体问题：\n\n1. **Ordering** 仅在 MMLU 操控（Section 3.3, p.5），其余 4 个 benchmark 不含此 facet\n2. **Prompt template** 在 MC 和 FF 间含义不同：MC 的变体是选项呈现格式（如 \"A/B/C/D\" vs 编号），FF 的变体涉及指令措辞（如 chain-of-thought vs direct，见 Appendix E, p.14）\n\n论文在 Table 3 (p.7) 注释中部分处理了这一问题：MC 中 \"Prompt\" 行报告 prompt main effect（~1%），FF 中报告 prompt main effect 被 residual 吸收（因 free-form generation variability）。但这种解释无法完全消除 **format effect 与 facet-specific effect 的混淆**。\n\n---\n\n## Minor\n\n### [AGREE] R1-M1: seed 42 选择理由\n\n合理问题。Section 3.2 (p.4) 提到 seed 为 \"random seeds, σ = ...\" 但未解释固定 seed 的具体选择。简要说明（如 \"arbitrary fixed seed for CUDA-level nondeterminism control\"）即可。\n\n### [AGREE] R1-M2: Table 2 \"all others: 0.0\" 改 \"<0.1%\"\n\n\"0.0\" 暗示精确为零，实际是四舍五入到一位小数。\"<0.1%\" 更诚实。\n\n### [REBUT] R1-M3: Section 4.6 scale validation 仅 Qwen 家族\n\nR1 说 \"仅 Qwen 家族\"——但 Section 4.6 (p.8) 的标题已是 **\"Preliminary** Scale Validation\"，论文对此分析的定位就是初步验证，而非完整结论。论文也明确写了 \"extensions to 70B+ models remains for future work\"。对一个标注为 \"Preliminary\" 的分析批评其范围不足，标准不对称。\n\n不过，**论文可以更明确说明此验证的局限**——例如 \"本验证仅覆盖 Qwen 架构家族内的 scale 变化，跨架构和跨 scale 的 exchangeability 需要未来工作验证\"。\n\n### [AGREE] R1-M4: Appendix E prompt templates 标注设计理由\n\nAppendix E (p.14) 列出了 6 个 MC 模板和约 6 个 FF 模板，但未解释变体设计背后的理由（如为什么选择 \"A/B/C/D\" vs \"1/2/3/4\" 的选项格式变体，或 \"Let's think step by step\" vs \"Solve this\" 的指令变体）。补充设计理由会增强 prompt universe 的 face validity。\n\n---\n\n## Questions\n\n### R1-Q1: GLMM vs Henderson I 绝对值差异\n\nAppendix A (p.11) 报告 \"all variance components differ by <0.3 percentage points\"，最大差异在 residual (0.47pp)。对于大方差分量（如 item_id = 37.9%），0.3pp 可忽略（<1% 相对误差）。但对于小分量（如 model = 2.5%），0.3pp = 12% 相对误差。**建议论文同时报告绝对值和相对值**以便读者判断实际影响。\n\n### R1-Q2: Model 视为 fixed facet 的影响\n\nAppendix A Table 6 (p.12) 直接回答了此问题：random vs fixed model 的 ΔG = 0.077-0.113。Fixed model 下 G 更高（model variance 不计入误差项），D-study budgets 更宽松。这说明 **random model 假设产生 conservative budgets**——R1 N1 的 exchangeability 担忧在 budget 方向上是安全的（不会导致 over-optimistic 建议），但在方差分解的解释性上仍是缺口。\n\n### R1-Q3: |ΔG| = 0.035 的实际意义\n\n好问题。|ΔG| = 0.035 从 G ≈ 0.935 到 ≈ 0.970（或反向），在 D-study 层面可能对应 10-20% 的 item 数变化。**论文应提供 budget sensitivity 分析**：给定 ΔG = ±0.035，D-study 预算从 55 items 变化到多少？这比仅报告 ΔG 更有实践意义。\n\n### R1-Q4: 多模型 partial-credit 实验\n\n全模型 partial-credit 实验需要定义跨 benchmark 的统一 rubric（GSM8K/MATH 的 step-by-step reasoning evaluation），工作量接近当前论文全文。作为 future work 处理合理。但 **Section 5 Conclusion 应更明确提及此方向**，而非仅在 Appendix A 提及。\n\n### R1-Q5: \"Order-of-magnitude guides\" 的量化含义\n\n同意 R1 的追问。\"Order-of-magnitude\" 在不同领域含义差异大（物理学 = ×10, 工程 = ×2-3）。Section 4.5 (p.8) 中 bootstrap CIs 已提供了 budget 范围（如 \"55-item single-model and 93-item cross-model budgets answer different practical questions. Bootstrap CIs (71-162 items)\"），但**未将此 CI 与 \"order-of-magnitude\" 术语显式关联**。建议明确：order-of-magnitude ≈ 预算的 95% CI 范围（约 ×1.5-3×）。\n\n### R1-Q6: Reduced crossing validation 跨 benchmark 验证\n\nAppendix A (p.12) 的 reduced crossing validation 确实覆盖了 5 个 benchmarks（使用 exp-002 BF16 subset），验证了 reduced crossing 保留方差结构（ΔG = 0.0068）。但 R1 的深层问题——**D-study budget predictions 在每个 benchmark 上的 calibration**——论文未独立验证。Table 7 (Appendix B) 提供了跨 benchmark 的 D-study 预算，但这些是 projections 而非经验验证。\n\n---\n\n## Missing References\n\n### [AGREE] R1-Missing: Cardinet, Johnson & Pini (2010)\n\n\"Applying Generalizability Theory using EduG\" 是 G-theory 应用层面的标准参考，特别是 D-study 设计优化部分。补充此引用会增强论文在教育测量社区的 credibility。\n\nR1 \"未发现 critical missing references\" 的判断我同意。论文的引用覆盖面在同类工作中已属完善。\n\n**补充**：我在自己的审稿中建议补充 lm-evaluation-harness (Gao et al., 2024) 的引用。论文的实践建议（3×3 设计、budget 计算器）应与社区的 de facto 评估工具对话——实践者在 lm-eval-harness 中实施多 facet 设计时会遇到的具体工程约束值得讨论。\n\n---\n\n## 总结：两位 Reviewer 的共识与分歧\n\n**高度共识区域**（两位 Reviewer 独立到达相同结论）：\n1. **Model exchangeability**：R1-N1 ≈ R2-W2——target universe 窄但 framing 宽\n2. **Binary scoring limitation**：R1-W1 ≈ R2-W4——partial-credit 方差结构根本不同\n3. **D-study budget 泛化边界**：R1-W2 ≈ R2-W2——invariance 假设讨论不充分\n4. **跨 benchmark 设计不对称**：R1-W4 ≈ R2-Q4\n\n**R1 独有的强观点**：\n- **N2** (format pattern 统计证据不足): 这是我遗漏的关键角度——n = 5 的 fundamental design constraint 使得 MC/FF 对比在统计上不可能达到显著性。我在 W5 中仅从解释深度批评，R1 从根基切入，更有力。\n\n**R2 独有的强观点**：\n- **W1** (\"10× fewer items\" framing 隐藏总评估量增长): R1 未触及此问题。55 items × 1,296 conditions = 71,280 总评估量 vs single-condition 的 552——这个 129× 的总成本增长在 Abstract 的 framing 中被 \"proportional increase\" 模糊化。论文在 Section 4.5 (p.8) 报告了推荐 3×3 设计的 179 items（总计 1,611 evaluations），但 Abstract 用的是 55-item 数字。\n\n**Overall Assessment 一致性**：两位 Reviewer 均给出 3.5/5 (Borderline Conference)，核心判断一致——实验执行扎实但新颖性有限、关键 claim 的 framing 存在问题。\n",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 565 · 2026-05-22T14:40:18.316637+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3815
}
```

</details>

---


### Tool call

_source line 566 · 2026-05-22T14:40:33.353177+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 567 · 2026-05-22T14:40:33.353613+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_6/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 568 · 2026-05-22T14:40:42.565613+00:00_

交叉回应已提交。要点总结：

- **R1 的 8 个观点中，同意 7 个，仅反驳 1 个**（M3：Section 4.6 已标注为 "Preliminary"，对初步验证批评范围不足标准不对称）
- **两位 Reviewer 的高共识区域**：model exchangeability 缺口、binary scoring limitation、D-study 泛化边界、跨 benchmark 设计不对称——四个问题独立到达相同结论
- **R1 最强观点 N2**（format pattern n=5 统计不可能显著）比我的 W5（解释深度不足）更根本，我明确承认
- **R2 独有贡献 W1**（"10× fewer items" 隐藏 129× 总成本增长）R1 未触及，但 Section 4.5 实际报告了 3×3 设计需 179 items（总 1,611 evaluations），部分缓解了 Abstract framing 问题
- **两位 Reviewer 均给出 3.5/5**，核心判断一致

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 15

## Round 15

74 recorded events


### User

_source line 569 · 2026-05-22T15:07:47.120992+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责**新颖性与完整性**审查。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ACL Rolling Review 统一审稿）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，Long paper 正文 ≤8 页，参考文献不限，Limitations 必写（不计入页数），Ethics 可选（不计入页数）
- **匿名**: Double-blind

## 论文文件
- LaTeX: `projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf`

## 你的审查侧重

重点评估以下方面：

1. **增量贡献 vs Messing (2026)**：Messing 应用 G-theory 到 LLM 评测（TEE framework, judge identity 43.8%），本文声称三个增量方向（infrastructure facets, cross-benchmark, D-study budgets）——这些增量是否构成足够的 novelty？§2 Positioning 段落的差异化是否令人信服？
2. **Contribution framing**：三个 Contributions（D-study budgets, precision separability, practitioner toolkit）的权重和层级是否合理？是否有 overclaiming 风险？
3. **Related work 覆盖**：是否遗漏重要相关工作？特别检查 LLM evaluation variance、G-theory 应用、IRT for benchmarking、efficient evaluation 四个方向。
4. **Writing quality**：Abstract 的信息密度和可读性、Introduction 的叙事流畅度、Section 间的逻辑衔接、Conclusion 是否充分总结核心发现。
5. **格式合规**：是否符合 EMNLP 2026 / ARR 格式要求（页数、匿名、引用格式、Limitations section）？是否有 de-anonymization 风险？
6. **"10× fewer items" framing**：Abstract 中 "55 vs 552 items" 的报告绑定 1,296 conditions；推荐的 3×3=9 conditions 下 item budget (178) 的呈现是否透明？是否存在误导读者的风险？
7. **FF benchmarks 高 residual variance (40-44%)**：跨 benchmark 分析是否缺乏解释性深度？未分析 item 特征如何预测 model×item 交互是否是一个重大遗漏？

请按 ARR 审稿标准给出完整审稿意见，包括 Summary、Strengths、Weaknesses（逐条编号）、Questions、Missing References、Overall Assessment。Weaknesses 必须严格、具体，引用论文具体 Section/Table/Figure。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 570 · 2026-05-22T15:07:53.920924+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_2_0518f4eb/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_2_0518f4eb/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 571 · 2026-05-22T15:07:54.824691+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_2_0518f4eb.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 903
}
```

</details>

---


### Tool call

_source line 572 · 2026-05-22T15:07:54.925492+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 573 · 2026-05-22T15:07:54.976039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 574 · 2026-05-22T15:07:59.800158+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL Rolling Review 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 575 · 2026-05-22T15:08:00.854159+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 576 · 2026-05-22T15:08:01.767502+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 577 · 2026-05-22T15:08:07.244252+00:00_

Web search results for query: "ACL Rolling Review 2026 reviewer guidelines review form criteria"

Links: [{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL Rolling Review 2026. Here are the key results:

## Reviewer Guidelines

The ACL Rolling Review asks reviewers to (1) read the paper and get the first impression, (2) search for related work, not deliberately trying to find that particular submission. If you feel qualified to review some aspects of the paper but not others, please state in the review if you did not check some major parts, such as proofs.

Reviewers are provided with a checklist to flag the problems that other people may have
…[truncated 1108 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7444
}
```

</details>

---


### Tool result

_source line 578 · 2026-05-22T15:08:08.654402+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 466.7}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 497.2}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.9}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 548.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.4}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 504.6}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.0}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 553.9}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7800
}
```

</details>

---


### Tool result

_source line 579 · 2026-05-22T15:08:08.654897+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Analysis}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 6887
}
```

</details>

---


### Tool call

_source line 580 · 2026-05-22T15:08:18.364554+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-14",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-14",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 581 · 2026-05-22T15:08:18.866828+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 566.3}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 413.5}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 301.5}], \"total_pages\": 14, \"rendered_pages\": 4, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 582 · 2026-05-22T15:08:22.730256+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form with all criteria dimensions, scoring scales, and descriptions. I need: 1) All rating dimensions (soundness, excitement, etc.) with their scale descriptions, 2) Overall assessment scale, 3) Any specific guidance on what constitutes each score level."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form with all criteria dimensions, scoring scales, and descriptions. I need: 1) All rating dimensions (soundness, excitement, etc.) with their scale descriptions, 2) Overall assessment scale, 3) Any specific guidance on what constitutes each score level."
  }
}
```

</details>

---


### Tool call

_source line 583 · 2026-05-22T15:08:23.081617+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 584 · 2026-05-22T15:08:23.182366+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 585 · 2026-05-22T15:08:28.977521+00:00_

# ACL Rolling Review Form - Complete Scoring Structure

## Rating Dimensions

### 1. Reviewer Confidence
**Scale: 1-5**
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: Quite sure; unlikely to miss critical details
- 3: Pretty sure, but may have missed some specifics
- 2: Can defend evaluation, but likely missed details
- 1: Outside expertise area or paper too difficult to assess

### 2. Soundness
**Scale: 1-5 (with .5 increments)**
- 5: "This study is one of the most thorough I have seen"
- 4: Strong support for claims; additional experiments optional
- 3: Sufficient support for main claims; minor details need work
- 2: Main claims lack sufficient support; major technical issues
- 1: "Not yet sufficiently thorough to warrant publication"

### 3. Excitement
**Scale: 1-5 (with .5 increments)**
- 5: "I would recommend this paper to others and/or attend its presentation"
- 4: Would mention to others; effort to attend presentation
- 3: Might mention points; attend if time permits
- 2: Doesn't resonate with reviewer but may interest others
- 1: "does not resonate with me" and unlikely to interest broader community

### 4. Overall Assessment
**Scale: 1-5 (with .5 increments)**
- 5: Consider for Award (top 2.5%)
- 4.5: Borderline Award
- 4: Conference acceptance
- 3.5: Borderline Conference
- 3: Findings track acceptance
- 2.5: Borderline Findings
- 2: Resubmit next cycle
- 1.5: Resubmit after next cycle
- 1: Do not resubmit

## Additional Evaluation Areas

**Reproducibility**: 1-5 scale measuring result replication feasibility

**Datasets**: 1-5 scale assessing value to research community

**Software**: 1-5 scale evaluating utility for others

**Author Identity Knowledge**: 1-5 scale for blinding integrity

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 6247
}
```

</details>

---


### Tool call

_source line 586 · 2026-05-22T15:08:32.641784+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 587 · 2026-05-22T15:08:33.094305+00:00_

1	Large Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. No study has simultaneously crossed infrastructure and methodology facets in a unified factorial design across benchmarks. We apply Generalizability theory (G-theory) in a crossed design with up to seven facets across eight open-weight 7--9B parameter instruction-tuned models and five benchmarks, totaling approximately 2.3 million cross-model evaluation records. A recommended 3-prompt $\times$ 3-seed design requires 178 items (1,602 total evaluations per model) for a generalizability coefficient $G \geq 0.80$, versus 552 items under single-condition evaluation---a 3.1$\times$ item reduction; full multi-facet designs further reduce to 55 items at 1,296 conditions per item. Cross-model projections confirm item reductions exceed 10$\times$ across all five benchmarks (for the studied 7--9B model class under binary scoring). Under binary scoring, BF16 and FP16 numerical precisions are functionally interchangeable ($<$0.1\% interaction). Model$\times$item interaction (up to 36\%) is the second-largest component in cross-model analysis, indicating that models differ primarily in which items they find difficult. We observe suggestive but statistically underpowered format-associated differences in variance concentration that warrant investigation with larger benchmark samples. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 452
}
```

</details>

---


### Tool call

_source line 588 · 2026-05-22T15:08:33.094761+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 589 · 2026-05-22T15:08:34.100809+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	In our analysis of five benchmarks, item selection drives 34--38\% of evaluation variance on multiple-choice tasks while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from a factorial analysis of approximately 2.3 million evaluation records, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No study has simultaneously crossed infrastructure and methodology facets in a unified factorial design across benchmarks to decompose these sources, quantify their interactions, and compare the resulting variance structure.
5	
6	Existing studies examine individual variance sources in isolation. \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} documented 50--76\% accuracy swings from prompt formatting; \citet{yuan2025layercast} showed up to 9\% variation from numerical precision; \citet{pezeshkpour2024ordering}, \citet{dodge2020finetuning}, and \citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (j
…[truncated 2876 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool call

_source line 590 · 2026-05-22T15:08:34.101280+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 591 · 2026-05-22T15:08:34.502843+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Several subsequent studies applied similar decomposition logic to specific facets of model evaluation \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark (judge identity: 43.8\%; see Positioning below for detailed comparison). \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Holistic evaluation frameworks \citep{liang2023helm} standardize multi-scenario comparison but do not decompose variance sources. \citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \citet{burnell2023rethink} called for rethinking evaluation reporting standards in AI. Recently, G-theory has been applied to LLM-based writing assessment \citep{wei2025gtheory} and annotation reliability \citep{varannot2025gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by crossing seven facets across five benchmarks, enabling direct comparison of variance structures
…[truncated 4128 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 592 · 2026-05-22T15:08:34.503185+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 593 · 2026-05-22T15:08:35.005515+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing varia
…[truncated 10592 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 594 · 2026-05-22T15:08:35.005869+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/sections/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 595 · 2026-05-22T15:08:35.507985+00:00_

1	\section{Experiments}
2	
3	We apply the G-theory framework from Section~3 to a fully crossed evaluation design spanning multiple models, benchmarks, and methodological facets. All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on NVIDIA RTX PRO 6000 GPUs (96GB). Binary correctness (1/0) serves as the primary outcome measure throughout; generation-based scoring avoids the log-likelihood artifacts identified by \citet{hua2025flaw}.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 239,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 61.1\% of total variance, with the residual term contributing 19.5\%. All main facet effects are negligible ($<$1\% each): prompt template 0.3\%, temperature 0.2\%, precision 0.1\%, seed $<$0.1\%, ordering $<$0.1\%. The interesting structure appears in item-conditional interactions: precision$\times$item contributes 7.2\%, temperature$\times$item 6.9\%, and prompt$\times$item 5.7\%. This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.918$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 72 items in thi
…[truncated 11953 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 596 · 2026-05-22T15:08:35.558573+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 597 · 2026-05-22T15:08:35.960451+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	A recommended 3-prompt $\times$ 3-seed design reduces item requirements from 552 to 178 for $G \geq 0.80$ (full multi-facet: 55 items), confirmed across all five benchmarks (bootstrap CIs exceed 10$\times$; budgets validated for 7--9B models under binary scoring). We observe suggestive but underpowered format-associated differences warranting larger benchmark samples. A minimal upgrade---two prompt variants---yields the steepest per-condition reliability gain (Appendix~\ref{app:intermediate_dstudy}); code, data, and a D-study calculator will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 598 · 2026-05-22T15:08:35.960767+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 599 · 2026-05-22T15:08:36.312264+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based, base, or $>$9B models. The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. A pilot partial-credit analysis confirms that scoring granularity fundamentally reshapes variance structure (Appendix~\ref{app:robustness}); extending to continuous rubrics (F1, BLEU) is a priority for future work. Our design varies few-shot example ordering but not example identity, a known variance source. Reduced-crossing validation and item resampling (CV = 3.1\%) cover MMLU only.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 600 · 2026-05-22T15:08:36.312640+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 601 · 2026-05-22T15:08:36.363178+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings; \texttt{item\_id} dominant in all 100 replications).
14	
15	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. The agreement indi
…[truncated 16021 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 602 · 2026-05-22T15:08:42.135557+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 603 · 2026-05-22T15:08:42.687676+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 604 · 2026-05-22T15:08:43.040950+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 605 · 2026-05-22T15:08:43.041409+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 606 · 2026-05-22T15:08:44.049026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1361
}
```

</details>

---


### Tool result

_source line 607 · 2026-05-22T15:08:44.050371+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 608 · 2026-05-22T15:08:44.050701+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 609 · 2026-05-22T15:08:44.352278+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 610 · 2026-05-22T15:08:44.854708+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool result

_source line 611 · 2026-05-22T15:08:45.106880+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 754
}
```

</details>

---


### Tool call

_source line 612 · 2026-05-22T15:08:48.417802+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 613 · 2026-05-22T15:08:48.870421+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 614 · 2026-05-22T15:08:49.774992+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1357
}
```

</details>

---


### Tool result

_source line 615 · 2026-05-22T15:08:49.776342+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 616 · 2026-05-22T15:08:49.776631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 617 · 2026-05-22T15:08:50.278148+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 618 · 2026-05-22T15:08:50.730411+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 953
}
```

</details>

---


### Tool call

_source line 619 · 2026-05-22T15:08:50.730811+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 620 · 2026-05-22T15:08:51.183936+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 905
}
```

</details>

---


### Tool call

_source line 621 · 2026-05-22T15:08:51.184345+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 622 · 2026-05-22T15:08:52.190868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1460
}
```

</details>

---


### Tool result

_source line 623 · 2026-05-22T15:08:52.192857+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 624 · 2026-05-22T15:08:52.193338+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 625 · 2026-05-22T15:08:52.696052+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 626 · 2026-05-22T15:08:53.400221+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1206
}
```

</details>

---


### Tool result

_source line 627 · 2026-05-22T15:08:53.404267+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 628 · 2026-05-22T15:08:53.404631+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 629 · 2026-05-22T15:08:53.757722+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 353
}
```

</details>

---


### Tool call

_source line 630 · 2026-05-22T15:09:00.682568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 631 · 2026-05-22T15:09:01.134223+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
14	
15	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: te
…[truncated 11675 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 632 · 2026-05-22T15:09:01.134702+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "references.*",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "references.*",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 633 · 2026-05-22T15:09:01.185036+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 634 · 2026-05-22T15:13:43.041787+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewerguidelines",
  "prompt": "Extract the complete reviewer guidelines, including: 1) What reviewers should evaluate, 2) Guidelines on novelty assessment, 3) Guidance on what constitutes a strong vs weak paper, 4) Any specific instructions about Findings vs Conference distinction, 5) Guidelines about assessing incremental contributions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewerguidelines",
    "prompt": "Extract the complete reviewer guidelines, including: 1) What reviewers should evaluate, 2) Guidelines on novelty assessment, 3) Guidance on what constitutes a strong vs weak paper, 4) Any specific instructions about Findings vs Conference distinction, 5) Guidelines about assessing incremental contributions."
  }
}
```

</details>

---


### Tool result

_source line 635 · 2026-05-22T15:13:50.519078+00:00_

# ARR Reviewer Guidelines Summary

## 1) What Reviewers Should Evaluate

Reviewers assess papers across multiple dimensions:

- **Soundness**: Technical validity and methodological rigor
- **Excitement**: Personal interest and subjective appeal
- **Overall recommendation**: Composite judgment reflecting soundness, novelty, and potential impact

Reviewers must evaluate whether papers answer their stated research questions appropriately and whether evidence sufficiently supports claims made.

## 2) Novelty Assessment Guidelines

The guidelines caution against common novelty-related pitfalls:

- Avoid dismissing findings as "not surprising" simply because they seem obvious in retrospect
- Require specific references when claiming lack of novelty: "Highly similar work X and Y has been published [3+ months prior]"
- Recognize that reproduction, reimplementation, and analysis studies are valid contributions within scope
- Avoid expecting SOTA results as a prerequisite for acceptance

The document notes: "SOTA results are neither necessary nor sufficient for a scientific contribution."

## 3) Strong vs. Weak Paper Indicators

**Strong papers demonstrate:**
- Clear research questions with appropriate scope
- Sufficient evidence for stated claims
- Technical soundness in methodology and proofs
- Fair representation of related work
- Appropriate statistical rigor and significance assessment

**Weak papers may exhibit:**
- Vague or unclear contributions
- Missing or misrepresented citations
- Insufficient detail for reproducibility
- Undisclosed data quality issues
- Overclaimed or misleading framing

## 4) Findings vs. Conference Distinction

The guidelines provide limited explicit guidance on this distinction. They note that "All papers recommended for Findings and main conferences are expected to be sufficiently sound and reproducible," but differentiation criteria appear venue-dependent rather than reviewer-prescribed.

## 5) Incremental Contributions Assessment

The guide
…[truncated 507 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7477
}
```

</details>

---


### Tool call

_source line 636 · 2026-05-22T15:16:07.605857+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 — 新颖性与完整性审查\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论执行扎实、鲁棒性验证充分，但相对 Messing (2026) 的增量贡献有限，\"10× fewer items\" 的 framing 掩盖了总评估成本的大幅增加，FF benchmarks 40-44% 的残差方差未得到分析。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Henderson Method I + 9项鲁棒性分析验证充分；但 FF 高残差未分析、数据污染混淆未讨论、总评估成本 framing 不够透明 |\n| Excitement | 3/5 | D-study budget 框架实用，但核心方法论来自 Messing (2026)，主要发现为零效应（infrastructure negligible）或统计效力不足（format comparison p=0.10） |\n| Reproducibility | 4/5 | 设计矩阵、模型标识符、vLLM 版本、prompt 模板全部公开；代码和数据承诺发布；唯一限制是 item 重抽样稳定性仅验证了 MMLU 的 10 个 subjects |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"10× fewer items\" headline 掩盖总评估成本的 100-200× 增加\n- 具体位置：Abstract 第4-5句, Introduction Figure 1 caption, §4.5 Table 4, Appendix Table 7\n- 问题：Abstract 以 \"55 vs 552 items\" 为核心 headline，cross-model projections 声称 \"item reductions exceed 10× across all five benchmarks\"。但总评估量的对比完全不同：\n  - 单模型 full multi-facet: 55 items × 1,296 conditions = **71,280 evaluations** vs single-condition 552 × 1 = **552 evaluations** → 129× 更多评估量\n  - Cross-model (Table 7, MMLU): 93 items × 2,304 conditions = **214,272 evaluations** vs 1,216 × 1 = **1,216 evaluations** → 176× 更多评估量\n  - 推荐的 3×3 设计 (178 items × 9 = 1,602 evals vs 552 evals) 相对合理 (2.9× 更多评估量换取 3.1× 更少 items)，但这个 3.1× 远不如 headline 的 10×\n- Abstract 确实提到了 \"1,296 conditions per item\" 和 \"1,602 total evaluations per model\"，但 10× headline 的信息优先级远高于这些细节。一个粗心的读者（或 leaderboard 维护者）可能认为 multi-facet evaluation 比 single-condition 更\"便宜\"。\n- 为什么影响接收：这是论文最核心的 practical claim。如果读者误以为 multi-facet 整体更便宜，会对框架的实际部署产生根本性误解。论文的 value proposition 其实是 \"同等 reliability 下更少 items（但更多 conditions per item）\"——这需要前提条件：items 是瓶颈（如构建新 benchmark），而非 compute 是瓶颈（如使用现有 benchmark）。\n- 建议修改方向：\n  (a) 在 Abstract 和 Introduction 中明确报告总评估量对比（items × conditions），而非仅报告 item reduction ratio\n  (b) 讨论 \"items as bottleneck vs compute as bottleneck\" 的适用场景\n  (c) 将推荐的 3×3 设计（3.1×, 2.9× 更多评估量）作为 headline，而非 full multi-facet 的 10×\n\n**N2** [critical] 相对 Messing (2026) 的增量贡献需要更强的 justification\n- 具体位置：§2 Positioning 段落, §1 Contributions 列表\n- 问题：Messing (2026) 已将 G-theory 引入 LLM 评测（TEE framework, judge identity 43.8%）。本文声称三个增量方向：\n  - (i) 将 judge identity 替换为 infrastructure facets → 但主要发现是这些 facets 都 negligible（<1%）。确认零效应有价值，但 excitement 有限。\n  - (ii) 跨 5 个 benchmark 比较 variance structure → 但 format-associated difference 在 benchmark-level CI 跨零（[-1.7, 5.1], §4.3），置换检验 p=0.10 达到分辨率下限。论文诚实标注为 \"exploratory\" 和 \"suggestive but underpowered\"，但这意味着 cross-benchmark comparison 的核心发现尚未达到可发表的统计标准。\n  - (iii) D-study budgets → 这是最强贡献，将 variance components 转化为可操作的 item budgets。但 D-study 是 G-theory 的标准操作（Shavelson & Webb 1991, Ch. 4），methodological innovation 有限。\n- §2 Positioning 段落写得清晰，差异化表述合理。但 \"complementary\" 定位意味着本文是 Messing 的应用延伸而非独立创新。\n- 为什么影响接收：ARR guidelines 明确肯定 \"systematic analyses\" 的价值，但 main conference 对 novelty 有较高期待。三个增量中两个（infrastructure null effects, underpowered format comparison）单独不构成 sufficient novelty；D-study budgets 是实用贡献但方法论层面是标准操作。\n- 建议修改方向：\n  (a) 将 D-study budget 的 practical framing 加强——不仅是 \"需要多少 items\"，而是一个完整的 evaluation design optimization 框架\n  (b) 如果 format comparison 有更多 benchmarks 的数据，建议纳入以提高统计效力\n  (c) 考虑更深入地分析 model×item interaction 的含义（见 N3），以增加分析深度\n\n**N3** [critical] FF benchmarks 40-44% 残差方差缺乏解释性分析\n- 具体位置：§4.3 Table 3 (GSM8K residual 39.9%, MATH 43.9%), experiments.tex line 46\n- 问题：FF benchmarks 的残差方差是所有 components 中最大的（MATH 43.9% > item 24.0%），这意味着 G-theory 模型对 FF benchmarks 的解释力严重不足。论文承认 \"likely reflect sources not captured by our facets: chain-of-thought path diversity, generation stochasticity, and answer extraction heuristics\" 但未做任何分析验证这些假设。\n- 具体缺失：\n  (a) 未分析 item 特征（难度、长度、topic、reasoning steps 数量）如何预测 model×item interaction 或残差大小\n  (b) 未尝试将 CoT path diversity 量化为可测量的 variance source\n  (c) 未讨论 G-theory 是否适合 FF benchmarks——当最大 component 是残差时，模型本身可能 underspecified\n- 论文 §4.3 末段讨论了 difficulty heterogeneity (std(p_i)) 与 item variance share 的相关性 (ρ=0.82, p=0.089)，这是一个有启发性的分析方向，但止步于相关性，未深入到 item-level predictors。\n- 为什么影响接收：FF benchmarks（GSM8K, MATH）是当前 LLM 评测的核心任务。如果 G-theory 框架对这类任务有 40%+ 的 unexplained variance，框架的 practical value 大打折扣。D-study budgets 基于 variance components 的准确估计——当残差占主导时，budgets 的可靠性存疑。\n- 建议修改方向：\n  (a) 对 FF benchmarks 做 item-level regression：用 item difficulty, length, number of reasoning steps 等 features 预测 residual magnitude\n  (b) 量化 CoT path diversity（e.g., 同一 item 在不同 conditions 下 CoT 路径的 ROUGE/BERTScore variation）\n  (c) 明确讨论 G-theory 对 FF benchmarks 的适用性边界\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 数据污染作为 model×item interaction 的混淆变量未被讨论\n- 具体位置：§4.2, §4.3 Table 3（model×item 30-36%）, §3.6\n- 问题：8 个模型在 MMLU、ARC、GSM8K 等广泛使用的 benchmark 上的 model×item interaction (30-36%) 被解释为 \"models differ primarily in which items they find difficult\"，归因于 architecture-specific capability profiles (§3.1) 和 differential item functioning。但 2024-2025 generation 的 LLM 普遍存在 benchmark 数据污染问题——如果某些模型在 pretraining 时见过特定 MMLU 题目，这些 items 对该模型会 \"spuriously easy\"，产生与 genuine DIF 无法区分的 model×item interaction。\n- 论文未引用任何 data contamination 文献（如 Golchin & Surdeanu 2023, Sainz et al. 2023 等）。\n- 建议：在 Limitations 或 §4.2 讨论 contamination 作为 model×item interaction 的 potential confound，并建议未来用 held-out items 做 robustness check。\n\n**W2** [warning] Contribution 层级权重不均\n- 具体位置：§1 Contributions 列表\n- 问题：三个贡献中，C1（D-study budgets）是核心贡献，但 C2（precision separability）本质上是一个 null result（\"BF16/FP16 negligible\"），C3（practitioner toolkit）是软件工程贡献。在 main conference paper 的贡献框架中，三者并列呈现给人 overclaiming 的印象。\n- C2 被诚实标注为 \"confirmatory\"，这很好。但 BF16 和 FP16 的 representational capacity 对 inference 高度相似，这个零效应对该领域专家来说不 surprising。\n- 建议：将 C2 降格为 findings within C1 的 framework，或在 framing 上更明确地将 C1 作为 primary contribution，C2/C3 作为 supporting。\n\n**W3** [warning] ARC model×prompt 异常 (8.0%) 未讨论\n- 具体位置：§4.3 Table 3, ARC 列\n- 问题：ARC-Challenge 的 model×prompt interaction 为 8.0%，远高于其他 MC benchmarks（MMLU 1.6%, HellaSwag 0.6%）。这表明某些模型对 ARC 的 prompt 格式特别敏感，但论文完全没有讨论这个异常值。这可能与 ARC 的 item 特性（science questions, 更短的选项）有关，也可能反映某些模型的 few-shot learning 对 ARC format 的脆弱性。\n- 建议：在 §4.3 加一句讨论 ARC 的 model×prompt anomaly 及其可能原因。\n\n**W4** [warning] Conclusion 过于简短\n- 具体位置：§5 Conclusion（仅一段，约 5 句）\n- 问题：Conclusion 仅重复了数字结果（178 vs 552, 55 items, 10×），未充分讨论：(a) 对 NLP 评测实践的具体影响，(b) 何时应该/不应该使用 multi-facet evaluation，(c) 与 IRT-based evaluation 的互补关系的 implications，(d) format-conditional variance structure 对 benchmark design 的启示。\n- 建议：扩充 Conclusion 至 2-3 段，包含 practical implications 和 future directions。\n\n**W5** [warning] Cross-benchmark 比较受非对称设计限制\n- 具体位置：§3.3, §4.3 第末段\n- 问题：论文在 §4.3 末段诚实指出 \"The factorial design is not fully symmetric: ordering applies only to MC...and prompt templates serve format-specific functions\"。但这个非对称性对 format comparison 的影响未量化。MC 的 prompt templates 变化 option layout (lettered vs numbered)，而 FF 的 prompt templates 变化 CoT elicitation strategy——这是两个 qualitatively different 的 manipulation。将两者产生的 prompt×item variance 直接对比可能混淆 format effect 和 manipulation type effect。Ordering facet 对所有非 MMLU benchmarks 结构性为零，实际上提供了 4× replication 而非 4 个 independent conditions。\n- 建议：讨论这一非对称性对 variance component 估计的 potential impact，或在 Limitations 中更明确地 caveat format comparison。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.1 Design 段落：single-model G-study 描述为 \"yielding 259,200 binary observations\"，但 §3.2 的 sample sizes 段说 \"259,200 binary observations across 1,296 fully balanced conditions\"。而 Table 1 显示 exp-001 总记录为 460,800†（8 models BF16 subset）。建议统一数字表述，避免混淆单模型和多模型的记录数。\n- §3.1：\"person×item DIF reflects unidirectional person responses to items, whereas model×item DIF in LLM evaluation simultaneously reflects architecture-specific capability profiles—a dual interpretation\" 这段 semantic distinction 表述不够清晰——educational measurement 的 DIF 也是 bidirectional 的（不同 demographic groups 对同一 item 的差异表现）。建议精确化 \"dual interpretation\" 的含义。\n- Appendix A, Inter-model agreement 段：\"HellaSwag uses six models (κ = 0.332) due to missing OLMo and Yi data\" — 缺失两个模型的原因未解释。如果是技术原因（模型不支持 HellaSwag format），应简要说明。\n- Abstract 中 \"approximately 2.3 million cross-model evaluation records\" 与 Table 1 的 2,304,000 (exp-002) + 460,800 (exp-001) = 2,764,800 不完全对应。建议核实或注释。\n\n---\n\n## Questions to Authors\n\n1. 请提供 Table 4 和 Table 7 中每个 design 的 **总评估量** (items × conditions) 对比，以使读者能直接比较 total evaluation cost 而非仅比较 item count。\n2. 在 model×item interaction 的分析中，是否考虑过 **data contamination** 作为 confound？如果部分模型在 pretraining 中见过 MMLU 题目，model×item interaction 的 30-36% 中有多少可能来自 contamination 而非 genuine capability difference？\n3. ARC-Challenge 的 model×prompt interaction (8.0%) 显著高于其他 MC benchmarks (<1.6%)。作者如何解释这个异常？\n4. 对于 FF benchmarks 的 40-44% 残差方差，是否有任何 item-level feature 能预测残差的大小？例如，推理步数较多的 GSM8K items 是否有更大的 residual？\n5. 论文推荐 3×3 design (9 conditions, 178 items)，这需要 1,602 evaluations per model。在什么场景下，practitioners 应该选择 (a) single-condition 552 items 而非 (b) 3×3 的 178 items？请讨论 use case 的 trade-off。\n\n---\n\n## Missing References\n\n- **Data contamination literature**: Golchin & Surdeanu (2023), Sainz et al. (2023) 等关于 LLM benchmark contamination 的工作。鉴于 model×item interaction 是本文核心发现之一，contamination confound 不可忽略。\n- **DynaBench** (Kiela et al., 2021): Dynamic benchmarking 作为 evaluation variance 的另一种应对策略。\n- 未发现其他重大遗漏。Related Work 对 variance decomposition、IRT、prompt sensitivity、G-theory foundations 四个方向的覆盖较为完整。\n\n---\n\n## 主要优势\n\n- **S1: 实验规模和设计严谨性**。2.3M records, 7 facets fully crossed, 8 architecture families, 5 benchmarks——这是目前最大规模的 LLM evaluation variance decomposition study。The factorial design enables interaction estimation that piecemeal studies cannot achieve。\n- **S2: 鲁棒性验证异常充分**。9 项分析（GLMM complement ρ=1.0, REML/Henderson 一致性 <0.5pp, item resampling CV=3.1%, LOMO 稳定性 CV≤1.25%, null calibration, probit simulation, etc.）远超同类论文的验证深度。\n- **S3: 诚实的统计报告**。Format comparison 标注为 \"exploratory\" and \"suggestive but underpowered\"（p=0.10）；binary scoring conditionality 贯穿全文；random-model G 作为 conservative specification 报告；partial-credit pilot 明确展示了 scoring granularity 的影响。这种诚实性在当前 ML 文献中难得。\n- **S4: Practical D-study gradient（Appendix C）**。从 single-condition 到 full multi-facet 的 7 级 adoption gradient (Table 9) 让 practitioners 可以根据自己的 compute budget 选择合适的 design level。3×3 \"minimal sufficient\" 推荐特别实用。\n- **S5: IRT 互补性的清晰论证**。§4.5 中 IRT 116 items 在 single-condition 下 G=0.457 但在 multi-facet 下 G=0.895 的对比，有力论证了 item selection 和 evaluation design 是 orthogonal dimensions。\n- **S6: 格式完全合规**。正文 ≤8 页（§1-5 在第 8 页结束），Limitations 独立一节，Anonymous ACL submission 匿名，ACL 模板正确使用，无 de-anonymization 风险。\n\n---\n\n## Reviewer Confidence: 4/5\n我对 G-theory methodology, LLM evaluation, 和 psychometrics 的相关文献较为熟悉，仔细阅读了全文和附录。对 binary data 的 Henderson Method I 估计量性质不如连续数据场景熟悉。",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 — 新颖性与完整性审查\n\n---\n\n## 总体评分\n**Overall**: 3.5 (Borderline Conference)\n**一句话总结**: 方法论执行扎实、鲁棒性验证充分，但相对 Messing (2026) 的增量贡献有限，\"10× fewer items\" 的 framing 掩盖了总评估成本的大幅增加，FF benchmarks 40-44% 的残差方差未得到分析。\n\n---\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 3.5/5 | Henderson Method I + 9项鲁棒性分析验证充分；但 FF 高残差未分析、数据污染混淆未讨论、总评估成本 framing 不够透明 |\n| Excitement | 3/5 | D-study budget 框架实用，但核心方法论来自 Messing (2026)，主要发现为零效应（infrastructure negligible）或统计效力不足（format comparison p=0.10） |\n| Reproducibility | 4/5 | 设计矩阵、模型标识符、vLLM 版本、prompt 模板全部公开；代码和数据承诺发布；唯一限制是 item 重抽样稳定性仅验证了 MMLU 的 10 个 subjects |\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] \"10× fewer items\" headline 掩盖总评估成本的 100-200× 增加\n- 具体位置：Abstract 第4-5句, Introduction Figure 1 caption, §4.5 Table 4, Appendix Table 7\n- 问题：Abstract 以 \"55 vs 552 items\" 为核心 headline，cross-model projections 声称 \"item reductions exceed 10× across all five benchmarks\"。但总评估量的对比完全不同：\n  - 单模型 full multi-facet: 55 items × 1,296 conditions = **71,280 evaluations** vs single-condition 552 × 1 = **552 evaluations** → 129× 更多评估量\n  - Cross-model (Table 7, MMLU): 93 items × 2,304 conditions = **214,272 evaluations** vs 1,216 × 1 = **1,216 evaluations** → 176× 更多评估量\n  - 推荐的 3×3 设计 (178 items × 9 = 1,602 evals vs 552 evals) 相对合理 (2.9× 更多评估量换取 3.1× 更少 items)，但这个 3.1× 远不如 headline 的 10×\n- Abstract 确实提到了 \"1,296 conditions per item\" 和 \"1,602 total evaluations per model\"，但 10× headline 的信息优先级远高于这些细节。一个粗心的读者（或 leaderboard 维护者）可能认为 multi-facet evaluation 比 single-condition 更\"便宜\"。\n- 为什么影响接收：这是论文最核心的 practical claim。如果读者误以为 multi-facet 整体更便宜，会对框架的实际部署产生根本性误解。论文的 value proposition 其实是 \"同等 reliability 下更少 items（但更多 conditions per item）\"——这需要前提条件：items 是瓶颈（如构建新 benchmark），而非 compute 是瓶颈（如使用现有 benchmark）。\n- 建议修改方向：\n  (a) 在 Abstract 和 Introduction 中明确报告总评估量对比（items × conditions），而非仅报告 item reduction ratio\n  (b) 讨论 \"items as bottleneck vs compute as bottleneck\" 的适用场景\n  (c) 将推荐的 3×3 设计（3.1×, 2.9× 更多评估量）作为 headline，而非 full multi-facet 的 10×\n\n**N2** [critical] 相对 Messing (2026) 的增量贡献需要更强的 justification\n- 具体位置：§2 Positioning 段落, §1 Contributions 列表\n- 问题：Messing (2026) 已将 G-theory 引入 LLM 评测（TEE framework, judge identity 43.8%）。本文声称三个增量方向：\n  - (i) 将 judge identity 替换为 infrastructure facets → 但主要发现是这些 facets 都 negligible（<1%）。确认零效应有价值，但 excitement 有限。\n  - (ii) 跨 5 个 benchmark 比较 variance structure → 但 format-associated difference 在 benchmark-level CI 跨零（[-1.7, 5.1], §4.3），置换检验 p=0.10 达到分辨率下限。论文诚实标注为 \"exploratory\" 和 \"suggestive but underpowered\"，但这意味着 cross-benchmark comparison 的核心发现尚未达到可发表的统计标准。\n  - (iii) D-study budgets → 这是最强贡献，将 variance components 转化为可操作的 item budgets。但 D-study 是 G-theory 的标准操作（Shavelson & Webb 1991, Ch. 4），methodological innovation 有限。\n- §2 Positioning 段落写得清晰，差异化表述合理。但 \"complementary\" 定位意味着本文是 Messing 的应用延伸而非独立创新。\n- 为什么影响接收：ARR guidelines 明确肯定 \"systematic analyses\" 的价值，但 main conference 对 novelty 有较高期待。三个增量中两个（infrastructure null effects, underpowered format comparison）单独不构成 sufficient novelty；D-study budgets 是实用贡献但方法论层面是标准操作。\n- 建议修改方向：\n  (a) 将 D-study budget 的 practical framing 加强——不仅是 \"需要多少 items\"，而是一个完整的 evaluation design optimization 框架\n  (b) 如果 format comparison 有更多 benchmarks 的数据，建议纳入以提高统计效力\n  (c) 考虑更深入地分析 model×item interaction 的含义（见 N3），以增加分析深度\n\n**N3** [critical] FF benchmarks 40-44% 残差方差缺乏解释性分析\n- 具体位置：§4.3 Table 3 (GSM8K residual 39.9%, MATH 43.9%), experiments.tex line 46\n- 问题：FF benchmarks 的残差方差是所有 components 中最大的（MATH 43.9% > item 24.0%），这意味着 G-theory 模型对 FF benchmarks 的解释力严重不足。论文承认 \"likely reflect sources not captured by our facets: chain-of-thought path diversity, generation stochasticity, and answer extraction heuristics\" 但未做任何分析验证这些假设。\n- 具体缺失：\n  (a) 未分析 item 特征（难度、长度、topic、reasoning steps 数量）如何预测 model×item interaction 或残差大小\n  (b) 未尝试将 CoT path diversity 量化为可测量的 variance source\n  (c) 未讨论 G-theory 是否适合 FF benchmarks——当最大 component 是残差时，模型本身可能 underspecified\n- 论文 §4.3 末段讨论了 difficulty heterogeneity (std(p_i)) 与 item variance share 的相关性 (ρ=0.82, p=0.089)，这是一个有启发性的分析方向，但止步于相关性，未深入到 item-level predictors。\n- 为什么影响接收：FF benchmarks（GSM8K, MATH）是当前 LLM 评测的核心任务。如果 G-theory 框架对这类任务有 40%+ 的 unexplained variance，框架的 practical value 大打折扣。D-study budgets 基于 variance components 的准确估计——当残差占主导时，budgets 的可靠性存疑。\n- 建议修改方向：\n  (a) 对 FF benchmarks 做 item-level regression：用 item difficulty, length, number of reasoning steps 等 features 预测 residual magnitude\n  (b) 量化 CoT path diversity（e.g., 同一 item 在不同 conditions 下 CoT 路径的 ROUGE/BERTScore variation）\n  (c) 明确讨论 G-theory 对 FF benchmarks 的适用性边界\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] 数据污染作为 model×item interaction 的混淆变量未被讨论\n- 具体位置：§4.2, §4.3 Table 3（model×item 30-36%）, §3.6\n- 问题：8 个模型在 MMLU、ARC、GSM8K 等广泛使用的 benchmark 上的 model×item interaction (30-36%) 被解释为 \"models differ primarily in which items they find difficult\"，归因于 architecture-specific capability profiles (§3.1) 和 differential item functioning。但 2024-2025 generation 的 LLM 普遍存在 benchmark 数据污染问题——如果某些模型在 pretraining 时见过特定 MMLU 题目，这些 items 对该模型会 \"spuriously easy\"，产生与 genuine DIF 无法区分的 model×item interaction。\n- 论文未引用任何 data contamination 文献（如 Golchin & Surdeanu 2023, Sainz et al. 2023 等）。\n- 建议：在 Limitations 或 §4.2 讨论 contamination 作为 model×item interaction 的 potential confound，并建议未来用 held-out items 做 robustness check。\n\n**W2** [warning] Contribution 层级权重不均\n- 具体位置：§1 Contributions 列表\n- 问题：三个贡献中，C1（D-study budgets）是核心贡献，但 C2（precision separability）本质上是一个 null result（\"BF16/FP16 negligible\"），C3（practitioner toolkit）是软件工程贡献。在 main conference paper 的贡献框架中，三者并列呈现给人 overclaiming 的印象。\n- C2 被诚实标注为 \"confirmatory\"，这很好。但 BF16 和 FP16 的 representational capacity 对 inference 高度相似，这个零效应对该领域专家来说不 surprising。\n- 建议：将 C2 降格为 findings within C1 的 framework，或在 framing 上更明确地将 C1 作为 primary contribution，C2/C3 作为 supporting。\n\n**W3** [warning] ARC model×prompt 异常 (8.0%) 未讨论\n- 具体位置：§4.3 Table 3, ARC 列\n- 问题：ARC-Challenge 的 model×prompt interaction 为 8.0%，远高于其他 MC benchmarks（MMLU 1.6%, HellaSwag 0.6%）。这表明某些模型对 ARC 的 prompt 格式特别敏感，但论文完全没有讨论这个异常值。这可能与 ARC 的 item 特性（science questions, 更短的选项）有关，也可能反映某些模型的 few-shot learning 对 ARC format 的脆弱性。\n- 建议：在 §4.3 加一句讨论 ARC 的 model×prompt anomaly 及其可能原因。\n\n**W4** [warning] Conclusion 过于简短\n- 具体位置：§5 Conclusion（仅一段，约 5 句）\n- 问题：Conclusion 仅重复了数字结果（178 vs 552, 55 items, 10×），未充分讨论：(a) 对 NLP 评测实践的具体影响，(b) 何时应该/不应该使用 multi-facet evaluation，(c) 与 IRT-based evaluation 的互补关系的 implications，(d) format-conditional variance structure 对 benchmark design 的启示。\n- 建议：扩充 Conclusion 至 2-3 段，包含 practical implications 和 future directions。\n\n**W5** [warning] Cross-benchmark 比较受非对称设计限制\n- 具体位置：§3.3, §4.3 第末段\n- 问题：论文在 §4.3 末段诚实指出 \"The factorial design is not fully symmetric: ordering applies only to MC...and prompt templates serve format-specific functions\"。但这个非对称性对 format comparison 的影响未量化。MC 的 prompt templates 变化 option layout (lettered vs numbered)，而 FF 的 prompt templates 变化 CoT elicitation strategy——这是两个 qualitatively different 的 manipulation。将两者产生的 prompt×item variance 直接对比可能混淆 format effect 和 manipulation type effect。Ordering facet 对所有非 MMLU benchmarks 结构性为零，实际上提供了 4× replication 而非 4 个 independent conditions。\n- 建议：讨论这一非对称性对 variance component 估计的 potential impact，或在 Limitations 中更明确地 caveat format comparison。\n\n---\n\n## 小问题（不影响接收）\n\n- §4.1 Design 段落：single-model G-study 描述为 \"yielding 259,200 binary observations\"，但 §3.2 的 sample sizes 段说 \"259,200 binary observations across 1,296 fully balanced conditions\"。而 Table 1 显示 exp-001 总记录为 460,800†（8 models BF16 subset）。建议统一数字表述，避免混淆单模型和多模型的记录数。\n- §3.1：\"person×item DIF reflects unidirectional person responses to items, whereas model×item DIF in LLM evaluation simultaneously reflects architecture-specific capability profiles—a dual interpretation\" 这段 semantic distinction 表述不够清晰——educational measurement 的 DIF 也是 bidirectional 的（不同 demographic groups 对同一 item 的差异表现）。建议精确化 \"dual interpretation\" 的含义。\n- Appendix A, Inter-model agreement 段：\"HellaSwag uses six models (κ = 0.332) due to missing OLMo and Yi data\" — 缺失两个模型的原因未解释。如果是技术原因（模型不支持 HellaSwag format），应简要说明。\n- Abstract 中 \"approximately 2.3 million cross-model evaluation records\" 与 Table 1 的 2,304,000 (exp-002) + 460,800 (exp-001) = 2,764,800 不完全对应。建议核实或注释。\n\n---\n\n## Questions to Authors\n\n1. 请提供 Table 4 和 Table 7 中每个 design 的 **总评估量** (items × conditions) 对比，以使读者能直接比较 total evaluation cost 而非仅比较 item count。\n2. 在 model×item interaction 的分析中，是否考虑过 **data contamination** 作为 confound？如果部分模型在 pretraining 中见过 MMLU 题目，model×item interaction 的 30-36% 中有多少可能来自 contamination 而非 genuine capability difference？\n3. ARC-Challenge 的 model×prompt interaction (8.0%) 显著高于其他 MC benchmarks (<1.6%)。作者如何解释这个异常？\n4. 对于 FF benchmarks 的 40-44% 残差方差，是否有任何 item-level feature 能预测残差的大小？例如，推理步数较多的 GSM8K items 是否有更大的 residual？\n5. 论文推荐 3×3 design (9 conditions, 178 items)，这需要 1,602 evaluations per model。在什么场景下，practitioners 应该选择 (a) single-condition 552 items 而非 (b) 3×3 的 178 items？请讨论 use case 的 trade-off。\n\n---\n\n## Missing References\n\n- **Data contamination literature**: Golchin & Surdeanu (2023), Sainz et al. (2023) 等关于 LLM benchmark contamination 的工作。鉴于 model×item interaction 是本文核心发现之一，contamination confound 不可忽略。\n- **DynaBench** (Kiela et al., 2021): Dynamic benchmarking 作为 evaluation variance 的另一种应对策略。\n- 未发现其他重大遗漏。Related Work 对 variance decomposition、IRT、prompt sensitivity、G-theory foundations 四个方向的覆盖较为完整。\n\n---\n\n## 主要优势\n\n- **S1: 实验规模和设计严谨性**。2.3M records, 7 facets fully crossed, 8 architecture families, 5 benchmarks——这是目前最大规模的 LLM evaluation variance decomposition study。The factorial design enables interaction estimation that piecemeal studies cannot achieve。\n- **S2: 鲁棒性验证异常充分**。9 项分析（GLMM complement ρ=1.0, REML/Henderson 一致性 <0.5pp, item resampling CV=3.1%, LOMO 稳定性 CV≤1.25%, null calibration, probit simulation, etc.）远超同类论文的验证深度。\n- **S3: 诚实的统计报告**。Format comparison 标注为 \"exploratory\" and \"suggestive but underpowered\"（p=0.10）；binary scoring conditionality 贯穿全文；random-model G 作为 conservative specification 报告；partial-credit pilot 明确展示了 scoring granularity 的影响。这种诚实性在当前 ML 文献中难得。\n- **S4: Practical D-study gradient（Appendix C）**。从 single-condition 到 full multi-facet 的 7 级 adoption gradient (Table 9) 让 practitioners 可以根据自己的 compute budget 选择合适的 design level。3×3 \"minimal sufficient\" 推荐特别实用。\n- **S5: IRT 互补性的清晰论证**。§4.5 中 IRT 116 items 在 single-condition 下 G=0.457 但在 multi-facet 下 G=0.895 的对比，有力论证了 item selection 和 evaluation design 是 orthogonal dimensions。\n- **S6: 格式完全合规**。正文 ≤8 页（§1-5 在第 8 页结束），Limitations 独立一节，Anonymous ACL submission 匿名，ACL 模板正确使用，无 de-anonymization 风险。\n\n---\n\n## Reviewer Confidence: 4/5\n我对 G-theory methodology, LLM evaluation, 和 psychometrics 的相关文献较为熟悉，仔细阅读了全文和附录。对 binary data 的 Henderson Method I 估计量性质不如连续数据场景熟悉。",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 637 · 2026-05-22T15:16:11.221011+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3615
}
```

</details>

---


### Tool call

_source line 638 · 2026-05-22T15:16:15.077010+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 639 · 2026-05-22T15:16:15.127641+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 640 · 2026-05-22T15:16:18.942917+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_7/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 641 · 2026-05-22T15:16:18.993590+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 642 · 2026-05-22T15:16:28.752234+00:00_

审稿完成。核心判断：**Overall 3.5 (Borderline Conference)**。

三个 Must-Fix 问题：
1. "10× fewer items" headline 掩盖了 100-200× 的总评估量增加，需要在 Abstract/Intro 中明确报告 items × conditions 的总成本对比
2. 相对 Messing (2026) 的三个增量贡献中，infrastructure facets 是零效应确认、format comparison 统计效力不足 (p=0.10)、D-study 是 G-theory 标准操作——需要更强的 novelty justification
3. FF benchmarks 40-44% 残差方差是最大 component 却完全未分析，限制了框架对 GSM8K/MATH 等核心任务的实用价值

主要优势：实验规模大 (2.3M records)、鲁棒性验证异常充分 (9 项分析)、统计报告诚实 (exploratory/confirmatory 区分)、3×3 practical design gradient 实用。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 16

## Round 16

8 recorded events


### User

_source line 643 · 2026-05-22T15:17:35.876782+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1（方法严谨性审查）的完整审稿意见。请逐条回应其 Must-Fix 和 Should-Fix 问题：对每条用 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 完整审稿意见

**Overall**: 3.5 (Borderline Conference)

### Must-Fix 问题

**N1** [critical] Henderson Method I 在 binary 数据上的验证深度不足
- Probit simulation Spearman=0.73 仅为中等相关，约 47% ranking variance 未被保留。未报告各方差分量 point estimate 的 bias/RMSE。
- GLMM complement 的验证标准过松："orderings ≥ 1.0" 仅要求 7 个分组排序一致，未检验各方差分量比例是否一致。item 占 35% vs 55% 都可能满足排序不变但导致完全不同的 D-study budgets。
- 如果 binary scoring 下 Henderson Method I 的 estimates 存在系统性 bias，所有 D-study budget 推荐的数值可靠性无法保证。

**N2** [critical] D-study 方差分量不变性假设缺乏充分验证
- Forward prediction (Table 8) 从 4 个 exp-001 models 预测 8 个 models：MC |ΔG|≤0.029, FF |ΔG|≤0.065。但这 4 个模型是 8 个模型的子集——in-sample cross-validation 而非 out-of-sample validation。
- LOMO stability (Table 5) 是 benchmark-level 稳定性，不直接验证 item pool expansion 不变性。
- Temporal drift 无任何 empirical evidence。
- 核心实用价值在于 D-study budget 推荐，如果方差分量在 model universe 扩展后变化，推荐便不可用。

**N3** [critical] 标题 overclaiming：scope 远窄于 "Open-Weight LLM Evaluation"
- Models: 仅 8 个 7-9B instruction-tuned models
- Scoring: 仅 binary correctness，partial-credit pilot 显示方差结构根本性改变 (G: 0.770→0.523, ρ=0.26)
- Benchmarks: 5 个 closed-ended benchmarks，不含 open-ended generation、code generation
- 标题应增加限定

### Should-Fix 问题

**W1** Partial-credit pilot 发现未被充分讨论。Binary vs partial credit: prompt variance 25.5%→1.2%, residual 28.2%→46.9%, ρ=0.26。这意味着 binary scoring 下 "item difficulty dominates" 可能是 binary threshold 的 artifact。
**W2** §4.3 Format analysis 统计基础薄弱：n=5, p=0.10 是最小可能 p 值；MC/FF 设计不对称——prompt semantics 和 ordering 差异混淆 format effect。
**W3** 8 个 quasi-random models 的辩护不充分：Table 6 仅说明 8 个模型内差异有限，不能证明代表 target universe。
**W4** Bootstrap CI 的 item-level resampling 忽略 model-level clustering，可能产生过窄的 CI。

### Missing References
- Cardinet, Johnson & Pini (2010) "Applying Generalizability Theory using EduG" 关于 dichotomous data
- Kiela et al. (2021) "Dynabench" 关于 benchmark temporal drift

---

请对以上每条 N1-N3、W1-W4 逐条给出 [AGREE] 或 [REBUT] 回应。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 644 · 2026-05-22T15:19:11.697215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex",
  "offset": "0",
  "limit": "70"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex",
    "offset": "0",
    "limit": "70"
  }
}
```

</details>

---


### Tool result

_source line 645 · 2026-05-22T15:19:12.200356+00:00_

0	\appendix
1	\section{Additional Robustness Analyses}
2	\label{app:robustness}
3	
4	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
5	
6	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
7	
8	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
9	
10	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
11	
12	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings; \texttt{item\_id} dominant in all 100 replications).
13	
14	\paragraph{CI method comparison.} Bootstrap (1,000 item-level resamples with replacement) and delete-1 jackknife confidence intervals agree closely: width ratios range from 0.96 to 1.04 across all variance components. The agreement indic
…[truncated 5735 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 646 · 2026-05-22T15:19:12.351620+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex",
  "offset": "70",
  "limit": "15"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex",
    "offset": "70",
    "limit": "15"
  }
}
```

</details>

---


### Tool result

_source line 647 · 2026-05-22T15:19:12.402197+00:00_

70	
71	\subsection{Binary Data Assumptions}
72	\label{sec:binary}
73	
74	Standard G-theory assumes continuous, approximately normal outcome data \cite{shavelson1991generalizability}. Our binary correctness scores (0/1) violate this assumption. We establish robustness through simulation and estimator properties, with two additional analyses (GLMM complement, accuracy-range stability) in Appendix~\ref{app:robustness}.
75	
76	Henderson Method~I produces unbiased estimates for balanced designs regardless of outcome distribution \cite[Ch.~12]{brennan2001generalizability}, and REML estimates differ by $<$0.5pp on all components. A probit simulation, GLMM complement ($\rho = 1.0$), and accuracy-range analysis all confirm robustness (Appendix~\ref{app:robustness}).
77	
78	All findings in this paper are conditioned on binary correctness scoring. This measurement resolution collapses continuous generation quality into a pass/fail outcome, which may mask finer-grained variance sources (e.g., partial credit, reasoning quality) that would emerge under richer scoring rubrics. The text-exact-match comparison in \S4.1 ($G = 0.007$ vs.\ $0.936$) illustrates how scoring metric can fundamentally reshape variance structure. A partial-credit pilot on GSM8K confirms this conditionality: $G_\text{item}$ drops from 0.76 to 0.55, and item difficulty rankings change substantially ($\rho = 0.26$; Appendix~\ref{app:robustness}), indicating that D-study budgets do not transfer to finer-grained scoring rubrics.
79	
80	Our target universe comprises open-weight, instruction-tuned models in the 7--9B parameter range (eight architecture families); results may not generalize to API-based, base, or $>$9B models. Our eight purposively selected models are treated as a quasi-random facet \cite{meredith1993measurement, putnick2016measurement}. We report $G$ under random-model assumptions, the more conservative specification: across five benchmarks, treating models as fixed yields $G_\text{fixed}$ of 0.951
…[truncated 893 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 648 · 2026-05-22T15:20:35.076637+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "## Reviewer 2 对 Reviewer 1 的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R1-N1: Henderson Method I 在 binary 数据上的验证深度不足**\n\nR1 正确指出了两个单独分析的局限性——probit simulation ρ=0.732 和 GLMM 仅检验排序——但忽略了论文提供的更强证据链，综合起来足以支撑 binary data 的可靠性：\n\n1. **理论保证**：Henderson Method I 对 balanced designs 产生**无偏估计**，无论数据分布如何（Brennan 2001, Ch. 12，§3.5 和 Appendix A 均引用）。这不是实验发现而是数学性质。R1 担心的\"系统性 bias\"在理论层面已被排除。Binary 数据影响的是估计量的 *efficiency*（精度），而非 *bias*——CI 已覆盖精度问题。\n\n2. **REML magnitude check**：R1 称 GLMM 仅检验排序，这对 GLMM 分析是对的。但 Appendix A Estimator Robustness 段明确报告了 REML 与 Henderson 的**幅度一致性**：所有方差分量差异 <0.5pp，substantive components（item, model×item, model）差异 <0.3pp。这直接回应了\"item 占 35% vs 55% 都满足排序但 D-study budgets 不同\"的担忧——两个估计量的幅度几乎相同。\n\n3. **Null calibration**：Appendix A 报告 observed-to-null variance ratio = 1.0008，且 null simulation 的 item variance 仅 0.08%（vs observed 58.4%），差三个数量级。这直接检验了 bias。\n\n4. **Probit ρ=0.732 的正确解读**：该模拟比较的是 dichotomized vs continuous data 的方差分量排名。ρ=0.732 反映的是 dichotomization 本身造成的信息损失（将连续数据二值化必然损失排名精度），不是 Henderson Method I 的 estimator bias。item_id 在全部 100 次重复中保持 dominant，说明关键排名稳定。\n\n综合看，论文提供了：理论无偏保证 + REML 幅度验证 <0.5pp + null calibration ratio 1.0008 + probit 关键排名稳定性 + GLMM 排序一致性。R1 孤立评价单个分析的弱点是合理的，但忽略了证据链的整体强度。\n\n**唯一值得补充的**：论文确实未报告 probit simulation 各分量的 bias/RMSE（R1 此点正确），增加这些数字可以让证据链更完整，但缺少它们不构成对结论的实质性威胁。\n\n---\n\n**[AGREE] R1-N2: D-study 方差分量不变性假设缺乏充分验证**\n\nR1 正确指出核心问题：forward prediction（Table 8）的 4 个模型（DeepSeek, Llama, Mistral, Qwen3）是 8 个模型的子集，这是 in-sample cross-validation 而非 out-of-sample validation。这确实限制了 D-study budget 推荐的外部有效性。\n\n不过需要两点补充：\n\n1. 论文已显式 caveat：\"All projections assume the 2024-2025 model generation; we recommend periodic re-estimation as models evolve\"（§4.5）。这是适当的限定。\n\n2. Random-model G 作为 conservative specification 报告（§3.6, Table 6），D-study budgets 是 upper bounds——practitioners 使用这些 budgets 不会 under-sample。这在一定程度上缓解了外推风险。\n\n但 R1 关于 temporal drift 无任何 empirical evidence 的指出完全正确。如果未来 2026 generation 模型的方差结构变化（比如因为更好的 instruction tuning 导致 model×item interaction 降低），当前 budgets 可能 over-conservative 或 under-conservative。这是实用价值的真实限制。\n\n建议：在 Limitations 中更明确地承认 forward prediction 的 in-sample 性质，并讨论 temporal drift 的具体风险。\n\n---\n\n**[REBUT] R1-N3: 标题 overclaiming**\n\n部分同意，但不认为构成 critical 级别问题。\n\nR1 列举三个 scope 限制：(a) 8 个 7-9B 模型, (b) binary scoring, (c) 5 个 closed-ended benchmarks。这些限制全部在 Abstract 第一句后即被明确（\"eight open-weight 7–9B parameter instruction-tuned models and five benchmarks\"），§3.5-3.6 和 Limitations section 反复强调。标题使用 \"Open-Weight LLM Evaluation\" 是 factually accurate 的（所有模型确实是 open-weight LLMs），且论文的 *methodology*（G-theory + D-study framework）确实适用于任何 open-weight LLM evaluation 场景——scope 限制的是 *empirical findings*，不是 *framework*。\n\n相比之下，NLP 领域大量论文标题使用远超实验范围的表述（如在 3 个 benchmark 上测试称 \"LLM Evaluation\"），本文的 scope 表述在领域惯例中属于正常范围。\n\n**降级为 Should-Fix**：标题可改为 \"Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis of 7–9B Models\" 以增加信息量，但将此视为 Must-Fix/critical 是过度的。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Partial-credit pilot 发现未被充分讨论**\n\n同意此点。但需纠正 R1 的数字：论文报告 G: 0.759→0.553（Appendix A），而非 R1 所引 \"0.770→0.523\"。无论确切数字，核心观察一致：binary scoring 下 \"item difficulty dominates\" 确实可能部分是 binary threshold 的 artifact，因为 partial credit 下 prompt variance 从 25.5% 降到 1.2%（Appendix A），说明 binary 的 pass/fail 切分人为放大了 prompt sensitivity。\n\n论文在 §3.5 已明确 condition all claims on binary scoring，并说明 \"D-study budgets do not transfer to finer-grained scoring rubrics\"。这是诚实的处理。但 R1 的深层关切有道理：如果未来 benchmarks 逐步采用 partial-credit/rubric scoring（趋势明显），当前的 binary-based budgets 的长期价值受限。建议在 Discussion 中更深入讨论 scoring granularity 的影响和 binary scoring 的 artifact 风险。\n\n**[AGREE] R1-W2: Format analysis 统计基础薄弱**\n\n完全同意。这与我自己的 W5 一致。n=5, p=0.10 是组合分辨率下限，MC/FF 的 prompt semantics 和 ordering 非对称性混淆 format effect。论文诚实标注为 exploratory 但标题和 abstract 对 format comparison 的呈现可能给读者留下过强的印象。\n\n**[AGREE] R1-W3: 8 个 quasi-random models 的辩护不充分**\n\n部分同意。LOMO（Table 5, CV ≤ 1.25%）和 Cohen's κ (mean 0.33–0.46) 证明了 *internal consistency*，但无法证明 *representativeness*。论文选择 8 个 architecture families 是 purposive sampling，quasi-random 处理依赖 exchangeability 假设（Meredith 1993），而 exchangeability 在 8 个特定模型上无法实证检验。\n\n不过，论文使用 random-model G（conservative）和 LOMO 的做法在 practical constraints 下是合理的——不可能穷举所有 7-9B 模型。建议增加对 quasi-random assumption 的局限性讨论（什么条件下可能失效：如果某 architecture family 的 model×item profile 系统性不同于现有 8 个模型），但不必要求完全解决这个问题。\n\n**[AGREE] R1-W4: Bootstrap CI 的 item-level resampling 忽略 model-level clustering**\n\n技术上完全正确。Item-level bootstrap 只捕获 item sampling variability，不捕获 model sampling variability。如果使用不同的 8 个模型，方差分量可能不同，但当前 CI 不反映这一不确定性。\n\nLOMO 分析（CV ≤ 1.25%）部分回应了 model-level uncertainty，但 LOMO 是 jackknife 而非 bootstrap，且只有 8 个 leave-one-out 子集，自由度很低。真正的 model-level bootstrap 需要 resample models with replacement（8^8 ≈ 1.7M 可能组合），但 8 个模型的 bootstrap 本身精度有限。\n\n建议论文在 CI 报告中注明 \"item-level uncertainty only; model-level uncertainty is addressed by LOMO (Table 5) but not incorporated into bootstrap CIs\"。\n\n---\n\n### Missing References\n\n**[AGREE]** Cardinet, Johnson & Pini (2010) 是 G-theory 应用于 dichotomous data 的重要参考，应当引用。\n\n**[AGREE]** Kiela et al. (2021) DynaBench 与 temporal drift 讨论相关。这与我自己的 missing references 中缺少 data contamination 文献的关切方向一致——都涉及 benchmark 和 model 随时间变化的问题。\n\n---\n\n### 总结\n\nR1 的 9 个问题中，我同意 6 个（N2, W1-W4, Missing Refs），部分反驳 2 个（N1, N3），对 N1 的反驳是最实质性的——R1 低估了论文的 binary validation 证据链强度，特别是遗漏了 Henderson Method I 的理论无偏性保证和 REML magnitude agreement。N3 的严重程度应降级。N2 是双方共识最强的 critical issue——D-study budgets 的外部有效性确实需要更强的 validation。",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "## Reviewer 2 对 Reviewer 1 的逐条回应\n\n---\n\n### Must-Fix 问题\n\n**[REBUT] R1-N1: Henderson Method I 在 binary 数据上的验证深度不足**\n\nR1 正确指出了两个单独分析的局限性——probit simulation ρ=0.732 和 GLMM 仅检验排序——但忽略了论文提供的更强证据链，综合起来足以支撑 binary data 的可靠性：\n\n1. **理论保证**：Henderson Method I 对 balanced designs 产生**无偏估计**，无论数据分布如何（Brennan 2001, Ch. 12，§3.5 和 Appendix A 均引用）。这不是实验发现而是数学性质。R1 担心的\"系统性 bias\"在理论层面已被排除。Binary 数据影响的是估计量的 *efficiency*（精度），而非 *bias*——CI 已覆盖精度问题。\n\n2. **REML magnitude check**：R1 称 GLMM 仅检验排序，这对 GLMM 分析是对的。但 Appendix A Estimator Robustness 段明确报告了 REML 与 Henderson 的**幅度一致性**：所有方差分量差异 <0.5pp，substantive components（item, model×item, model）差异 <0.3pp。这直接回应了\"item 占 35% vs 55% 都满足排序但 D-study budgets 不同\"的担忧——两个估计量的幅度几乎相同。\n\n3. **Null calibration**：Appendix A 报告 observed-to-null variance ratio = 1.0008，且 null simulation 的 item variance 仅 0.08%（vs observed 58.4%），差三个数量级。这直接检验了 bias。\n\n4. **Probit ρ=0.732 的正确解读**：该模拟比较的是 dichotomized vs continuous data 的方差分量排名。ρ=0.732 反映的是 dichotomization 本身造成的信息损失（将连续数据二值化必然损失排名精度），不是 Henderson Method I 的 estimator bias。item_id 在全部 100 次重复中保持 dominant，说明关键排名稳定。\n\n综合看，论文提供了：理论无偏保证 + REML 幅度验证 <0.5pp + null calibration ratio 1.0008 + probit 关键排名稳定性 + GLMM 排序一致性。R1 孤立评价单个分析的弱点是合理的，但忽略了证据链的整体强度。\n\n**唯一值得补充的**：论文确实未报告 probit simulation 各分量的 bias/RMSE（R1 此点正确），增加这些数字可以让证据链更完整，但缺少它们不构成对结论的实质性威胁。\n\n---\n\n**[AGREE] R1-N2: D-study 方差分量不变性假设缺乏充分验证**\n\nR1 正确指出核心问题：forward prediction（Table 8）的 4 个模型（DeepSeek, Llama, Mistral, Qwen3）是 8 个模型的子集，这是 in-sample cross-validation 而非 out-of-sample validation。这确实限制了 D-study budget 推荐的外部有效性。\n\n不过需要两点补充：\n\n1. 论文已显式 caveat：\"All projections assume the 2024-2025 model generation; we recommend periodic re-estimation as models evolve\"（§4.5）。这是适当的限定。\n\n2. Random-model G 作为 conservative specification 报告（§3.6, Table 6），D-study budgets 是 upper bounds——practitioners 使用这些 budgets 不会 under-sample。这在一定程度上缓解了外推风险。\n\n但 R1 关于 temporal drift 无任何 empirical evidence 的指出完全正确。如果未来 2026 generation 模型的方差结构变化（比如因为更好的 instruction tuning 导致 model×item interaction 降低），当前 budgets 可能 over-conservative 或 under-conservative。这是实用价值的真实限制。\n\n建议：在 Limitations 中更明确地承认 forward prediction 的 in-sample 性质，并讨论 temporal drift 的具体风险。\n\n---\n\n**[REBUT] R1-N3: 标题 overclaiming**\n\n部分同意，但不认为构成 critical 级别问题。\n\nR1 列举三个 scope 限制：(a) 8 个 7-9B 模型, (b) binary scoring, (c) 5 个 closed-ended benchmarks。这些限制全部在 Abstract 第一句后即被明确（\"eight open-weight 7–9B parameter instruction-tuned models and five benchmarks\"），§3.5-3.6 和 Limitations section 反复强调。标题使用 \"Open-Weight LLM Evaluation\" 是 factually accurate 的（所有模型确实是 open-weight LLMs），且论文的 *methodology*（G-theory + D-study framework）确实适用于任何 open-weight LLM evaluation 场景——scope 限制的是 *empirical findings*，不是 *framework*。\n\n相比之下，NLP 领域大量论文标题使用远超实验范围的表述（如在 3 个 benchmark 上测试称 \"LLM Evaluation\"），本文的 scope 表述在领域惯例中属于正常范围。\n\n**降级为 Should-Fix**：标题可改为 \"Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis of 7–9B Models\" 以增加信息量，但将此视为 Must-Fix/critical 是过度的。\n\n---\n\n### Should-Fix 问题\n\n**[AGREE] R1-W1: Partial-credit pilot 发现未被充分讨论**\n\n同意此点。但需纠正 R1 的数字：论文报告 G: 0.759→0.553（Appendix A），而非 R1 所引 \"0.770→0.523\"。无论确切数字，核心观察一致：binary scoring 下 \"item difficulty dominates\" 确实可能部分是 binary threshold 的 artifact，因为 partial credit 下 prompt variance 从 25.5% 降到 1.2%（Appendix A），说明 binary 的 pass/fail 切分人为放大了 prompt sensitivity。\n\n论文在 §3.5 已明确 condition all claims on binary scoring，并说明 \"D-study budgets do not transfer to finer-grained scoring rubrics\"。这是诚实的处理。但 R1 的深层关切有道理：如果未来 benchmarks 逐步采用 partial-credit/rubric scoring（趋势明显），当前的 binary-based budgets 的长期价值受限。建议在 Discussion 中更深入讨论 scoring granularity 的影响和 binary scoring 的 artifact 风险。\n\n**[AGREE] R1-W2: Format analysis 统计基础薄弱**\n\n完全同意。这与我自己的 W5 一致。n=5, p=0.10 是组合分辨率下限，MC/FF 的 prompt semantics 和 ordering 非对称性混淆 format effect。论文诚实标注为 exploratory 但标题和 abstract 对 format comparison 的呈现可能给读者留下过强的印象。\n\n**[AGREE] R1-W3: 8 个 quasi-random models 的辩护不充分**\n\n部分同意。LOMO（Table 5, CV ≤ 1.25%）和 Cohen's κ (mean 0.33–0.46) 证明了 *internal consistency*，但无法证明 *representativeness*。论文选择 8 个 architecture families 是 purposive sampling，quasi-random 处理依赖 exchangeability 假设（Meredith 1993），而 exchangeability 在 8 个特定模型上无法实证检验。\n\n不过，论文使用 random-model G（conservative）和 LOMO 的做法在 practical constraints 下是合理的——不可能穷举所有 7-9B 模型。建议增加对 quasi-random assumption 的局限性讨论（什么条件下可能失效：如果某 architecture family 的 model×item profile 系统性不同于现有 8 个模型），但不必要求完全解决这个问题。\n\n**[AGREE] R1-W4: Bootstrap CI 的 item-level resampling 忽略 model-level clustering**\n\n技术上完全正确。Item-level bootstrap 只捕获 item sampling variability，不捕获 model sampling variability。如果使用不同的 8 个模型，方差分量可能不同，但当前 CI 不反映这一不确定性。\n\nLOMO 分析（CV ≤ 1.25%）部分回应了 model-level uncertainty，但 LOMO 是 jackknife 而非 bootstrap，且只有 8 个 leave-one-out 子集，自由度很低。真正的 model-level bootstrap 需要 resample models with replacement（8^8 ≈ 1.7M 可能组合），但 8 个模型的 bootstrap 本身精度有限。\n\n建议论文在 CI 报告中注明 \"item-level uncertainty only; model-level uncertainty is addressed by LOMO (Table 5) but not incorporated into bootstrap CIs\"。\n\n---\n\n### Missing References\n\n**[AGREE]** Cardinet, Johnson & Pini (2010) 是 G-theory 应用于 dichotomous data 的重要参考，应当引用。\n\n**[AGREE]** Kiela et al. (2021) DynaBench 与 temporal drift 讨论相关。这与我自己的 missing references 中缺少 data contamination 文献的关切方向一致——都涉及 benchmark 和 model 随时间变化的问题。\n\n---\n\n### 总结\n\nR1 的 9 个问题中，我同意 6 个（N2, W1-W4, Missing Refs），部分反驳 2 个（N1, N3），对 N1 的反驳是最实质性的——R1 低估了论文的 binary validation 证据链强度，特别是遗漏了 Henderson Method I 的理论无偏性保证和 REML magnitude agreement。N3 的严重程度应降级。N2 是双方共识最强的 critical issue——D-study budgets 的外部有效性确实需要更强的 validation。",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 649 · 2026-05-22T15:20:38.588630+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3511
}
```

</details>

---


### Assistant

_source line 650 · 2026-05-22T15:20:42.999294+00:00_

交叉回应已提交。

核心判断：R1 的 9 条意见中同意 6 条，实质性反驳 2 条（N1 低估了 Henderson Method I 的理论无偏保证 + REML magnitude agreement；N3 严重程度应降级），N2（D-study 外部有效性）是双方共识最强的 critical issue。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 17

## Round 17

54 recorded events


### User

_source line 651 · 2026-05-23T01:03:19.859565+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责审查 **新颖性 + 完整性 + 写作质量**。

## 论文信息
- **标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models
- **论文路径**: projects/nlp_variance_gtheory/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf

## 目标 Venue
- **EMNLP 2026**（通过 ARR 统一审稿）
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，正文 ≤8 页，References 不限，Limitations 必需且不计页数
- **匿名**: Double-blind
- **评分标准**: 5=Award, 4.5=Borderline Award, 4=Conference, 3.5=Borderline Conference, 3=Findings, 2.5=Borderline Findings, 2=Resubmit next cycle, 1.5=Resubmit after next cycle, 1=Do not resubmit

## 你的审查侧重

### 1. 新颖性与增量贡献
- 与 Messing (2026) 的关键区别：Messing 在单个 benchmark 上用 TEE 框架分解 5 个方法论 facet（judge identity 43.8%）。本文声称三个扩展方向——(i) 替换 judge 为 model + infrastructure facets，(ii) 跨 5 个 benchmarks，(iii) D-study budgets。这些扩展的增量贡献是否足够 EMNLP main conference？
- C1 (D-study budgets) 是核心贡献——"3-prompt × 3-seed design, G≥0.80 with 178 items" 的实用价值评估
- C2 (precision separability) 是 null result——是否值得作为独立 contribution？
- Format-associated pattern 标注 exploratory，n=5, p=0.10——这个发现的价值和呈现方式是否合理？

### 2. Related Work 覆盖度
- 方差分解方向：Bouthillier et al. (2021), Dodge et al. (2020), Henderson et al. (2018), Magnusson et al. (2023), Messing (2026), Madaan et al. (2024) — 是否全覆盖？
- IRT 方向：Lalor et al. (2019), Rodriguez et al. (2021), Maia Polo et al. (2024), Zhou et al. (2026), Li et al. (2025) — positioning 是否清晰？
- Psychometrics：Shavelson & Webb (1991), Brennan (2001), Cardinet et al. (2010) — G-theory 经典文献是否充分？
- 是否遗漏重要相关工作？特别是 2025-2026 年的新工作

### 3. Framing 与 Claims 合理性
- Abstract 数字密度——是否过密？核心 message 是否清晰？
- "3.1× item reduction" headline——结合实际总评估量（1,602 vs 552），framing 是否准确？
- 标题包含 "7–9B Instruction-Tuned Models"——scope 限定是否清晰传达？
- Contributions 列表层级——C1/C2 是否适当区分主次？

### 4. 写作质量
- 论文结构和节奏：Introduction 是否有效 motivate？Method 是否清晰？Results 是否聚焦？
- Conclusion 长度和深度——是否充分讨论 practical implications 和 future directions？
- Limitations section——是否涵盖关键限制（binary scoring、model sample、temporal drift、cross-family generalization）？
- 表格和图表质量：Figure 1-5, Table 1-12——是否信息密度适当、标注清晰？
- 语言质量：是否有 AI-generated 风格痕迹？术语使用是否一致？

### 5. 格式合规
- 页数：正文 ≤8 页
- 匿名性检查：是否有泄露身份的线索（arXiv 引用、致谢、代码链接等）？
- 引用格式：natbib 兼容？是否有格式不一致？

请按以下结构输出审稿报告：
1. **Summary**（2-3 句）
2. **Strengths**（逐条，标 [S1], [S2]...）
3. **Weaknesses**（逐条，标 [W1], [W2]...，每条标注 severity: Must-Fix / Should-Fix / Minor）
4. **Questions**（需作者澄清）
5. **Missing References**（如有）
6. **Overall Assessment**（评分 + 置信度 + 1 段总评）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 652 · 2026-05-23T01:03:29.265938+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 653 · 2026-05-23T01:03:29.316703+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 654 · 2026-05-23T01:03:32.658916+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 655 · 2026-05-23T01:03:34.516720+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 656 · 2026-05-23T01:03:43.212750+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what I found:

## Review Form Criteria

For ARR papers, the main criteria for Findings are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## R
…[truncated 1078 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10553
}
```

</details>

---


### Tool result

_source line 657 · 2026-05-23T01:03:44.566782+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 470.6}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 517.5}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 579.4}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 526.4}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.1}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 500.2}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.3}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 550.8}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 10050
}
```

</details>

---


### Tool call

_source line 658 · 2026-05-23T01:03:51.345516+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment, Soundness, Excitement/Novelty, Reproducibility, and any other rated dimensions."
  }
}
```

</details>

---


### Tool call

_source line 659 · 2026-05-23T01:03:52.251088+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 660 · 2026-05-23T01:03:52.705375+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 661 · 2026-05-23T01:03:53.561543+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1310
}
```

</details>

---


### Tool result

_source line 662 · 2026-05-23T01:03:53.565768+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 663 · 2026-05-23T01:03:53.566119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool call

_source line 664 · 2026-05-23T01:03:54.521265+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 665 · 2026-05-23T01:03:54.572724+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1006
}
```

</details>

---


### Tool result

_source line 666 · 2026-05-23T01:03:58.694776+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: "Positive that my evaluation is correct. I read the paper very carefully"
- 4: "Quite sure" with unlikely but conceivable missed details
- 3: "Pretty sure, but there's a chance I missed something"
- 2: "Willing to defend my evaluation, but it is fairly likely that I missed some details"
- 1: "Not my area, or paper is very hard to understand"

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: "Excellent: This study is one of the most thorough I have seen"
- 4: "Strong: This study provides sufficient support for all of its claims"
- 3: "Acceptable: This study provides sufficient support for its main claims"
- 2: "Poor: Some of the main claims are not sufficiently supported"
- 1: "Major Issues: This study is not yet sufficiently thorough to warrant publication"

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: "Highly Exciting: I would recommend this paper to others"
- 4: "Exciting: I would mention this paper to others"
- 3: "Interesting: I might mention some points of this paper"
- 2: "Potentially Interesting: this paper does not resonate with me"
- 1: "Not Exciting: this paper does not resonate with me"

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: "Consider for Award" (top 2.5%)
- 4: "Conference: I think this paper could be accepted"
- 3: "Findings: I think this paper could be accepted to the Findings"
- 2: "Resubmit next cycle" (needs substantial revisions)
- 1: "Do not resubmit"

## 5. **Reproducibility**
Scale: 1-5
- 5: "They could easily reproduce the results"
- 4: "They could mostly reproduce the results"
- 3: "They could reproduce the results with some difficulty"
- 2: "They would be hard pressed to reproduce the results"
- 1: "They would not be able to reproduce the results"

## 6. **Datasets** (if applicable)
Scale: 1-5
- 5: "Enabling: should affect other people's choice of research projects"
- 4: "Useful: I would recommend the n
…[truncated 719 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 7349
}
```

</details>

---


### Tool result

_source line 667 · 2026-05-23T01:03:59.296997+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.8}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.3}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 427.5}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 390.8}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 31.0}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 4775
}
```

</details>

---


### Tool call

_source line 668 · 2026-05-23T01:04:04.822262+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 669 · 2026-05-23T01:04:05.325583+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 670 · 2026-05-23T01:04:05.781780+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 671 · 2026-05-23T01:04:05.782176+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 672 · 2026-05-23T01:04:06.689588+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1364
}
```

</details>

---


### Tool result

_source line 673 · 2026-05-23T01:04:06.741593+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 959
}
```

</details>

---


### Tool call

_source line 674 · 2026-05-23T01:04:06.742229+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 675 · 2026-05-23T01:04:07.244362+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 676 · 2026-05-23T01:04:07.294971+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 677 · 2026-05-23T01:04:07.861740+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 566
}
```

</details>

---


### Tool call

_source line 678 · 2026-05-23T01:04:13.383957+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool call

_source line 679 · 2026-05-23T01:04:13.887553+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 680 · 2026-05-23T01:04:14.841884+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1457
}
```

</details>

---


### Tool result

_source line 681 · 2026-05-23T01:04:14.842993+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 682 · 2026-05-23T01:04:14.843254+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 683 · 2026-05-23T01:04:15.297980+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 684 · 2026-05-23T01:04:15.851657+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1008
}
```

</details>

---


### Tool call

_source line 685 · 2026-05-23T01:04:15.852061+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 686 · 2026-05-23T01:04:19.066084+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3768
}
```

</details>

---


### Tool result

_source line 687 · 2026-05-23T01:04:19.067035+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 3214
}
```

</details>

---


### Tool call

_source line 688 · 2026-05-23T01:04:19.167659+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 689 · 2026-05-23T01:04:19.319221+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 690 · 2026-05-23T01:04:19.924843+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 757
}
```

</details>

---


### Tool result

_source line 691 · 2026-05-23T01:04:20.027792+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 708
}
```

</details>

---


### Tool call

_source line 692 · 2026-05-23T01:09:01.893547+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Alzahrani \"benchmarks as microscopes\" model metrology EMNLP 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Alzahrani \"benchmarks as microscopes\" model metrology EMNLP 2024"
  }
}
```

</details>

---


### Tool call

_source line 693 · 2026-05-23T01:09:02.848279+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "Zheng Chiang \"judging LLM-as-a-judge\" MT-bench chatbot arena NeurIPS 2024"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "Zheng Chiang \"judging LLM-as-a-judge\" MT-bench chatbot arena NeurIPS 2024"
  }
}
```

</details>

---


### Tool call

_source line 694 · 2026-05-23T01:09:03.149610+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR review form 2025 2026 overall assessment soundness excitement scoring dimensions"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR review form 2025 2026 overall assessment soundness excitement scoring dimensions"
  }
}
```

</details>

---


### Tool result

_source line 695 · 2026-05-23T01:09:07.970028+00:00_

Web search results for query: "Zheng Chiang "judging LLM-as-a-judge" MT-bench chatbot arena NeurIPS 2024"

Links: [{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/pdf/2306.05685"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://proceedings.neurips.cc/paper_files/paper/2023/hash/91f18a1287b398d378ef22505bf41832-Abstract-Datasets_and_Benchmarks.html"},{"title":"[PDF] Judging LLM-as-a-judge with MT-Bench and Chatbot Arena | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Judging-LLM-as-a-judge-with-MT-Bench-and-Chatbot-Zheng-Chiang/a0a79dad89857a96f8f71b14238e5237cbfc4787"},{"title":"[2306.05685] Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/abs/2306.05685"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://arxiv.org/html/2306.05685v4"},{"title":"NeurIPS Poster Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena","url":"https://neurips.cc/virtual/2023/poster/73434"},{"title":"Figure 16 from Judging LLM-as-a-judge with MT-Bench and Chatbot Arena | Semantic Scholar","url":"https://www.semanticscholar.org/paper/Judging-LLM-as-a-judge-with-MT-Bench-and-Chatbot-Zheng-Chiang/a0a79dad89857a96f8f71b14238e5237cbfc4787/figure/22"},{"title":"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | OpenReview","url":"https://openreview.net/forum?id=uccHPGDlao"},{"title":"Judging LLM-as-a-judge with MT-bench and Chatbot Arena | Proceedings of the 37th International Conference on Neural Information Processing Systems","url":"https://dl.acm.org/doi/10.5555/3666122.3668142"}]

Based on the search results, I found the paper you're looking for:

"Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" was published by Lianmin Zheng, Wei-Lin Chiang, Ying Sheng, Siyuan Zhuang, Zhanghao Wu, Yonghao Zhuang, Zi Lin, Zhuohan Li, Dacheng Li, Eric P. Xing, Hao Zhang, Joseph E Gonzalez, and Ion Stoica at NeurIPS 2023 in the Datasets and B
…[truncated 764 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 5121
}
```

</details>

---


### Tool result

_source line 696 · 2026-05-23T01:09:09.426700+00:00_

Web search results for query: "Alzahrani "benchmarks as microscopes" model metrology EMNLP 2024"

Links: [{"title":"Benchmarks as Microscopes: A Call for Model Metrology","url":"https://saxon.me/doc/metrology.pdf"},{"title":"[2407.16711] Benchmarks as Microscopes: A Call for Model Metrology","url":"https://arxiv.org/abs/2407.16711"},{"title":"Preprint, accepted as a conference paper at COLM 2024","url":"https://www.arxiv.org/pdf/2407.16711v1"},{"title":"Benchmarks as Microscopes: A Call for Model Metrology","url":"https://arxiv.org/pdf/2407.16711"},{"title":"[Literature Review] Benchmarks as Microscopes: A Call for Model Metrology","url":"https://www.themoonlight.io/en/review/benchmarks-as-microscopes-a-call-for-model-metrology"},{"title":"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards - ACL Anthology","url":"https://aclanthology.org/2024.acl-long.744/"}]

Based on the search results, here's what I found:

The paper "Benchmarks as Microscopes: A Call for Model Metrology" was authored by Michael Saxon, Ari Holtzman, Peter West, William Yang Wang, and Naomi Saphra. However, the paper was not published at EMNLP 2024. Instead, it was accepted as a conference paper at COLM 2024.

The paper addresses a critical issue in language model evaluation: Static benchmarks inevitably saturate without providing confidence in the deployment tolerances of LM-based systems, but developers nonetheless claim that their models have generalized traits such as reasoning or open-domain language understanding based on these flawed metrics.

The core proposal is that a new discipline of model metrology is needed—one which focuses on how to generate benchmarks that predict performance under deployment.

Regarding Alzahrani specifically, the search results show that Norah Alzahrani co-authored a different 2024 paper titled "When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards" published at ACL 2024, which appear
…[truncated 164 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7533
}
```

</details>

---


### Tool result

_source line 697 · 2026-05-23T01:09:13.744992+00:00_

Web search results for query: "ACL ARR review form 2025 2026 overall assessment soundness excitement scoring dimensions"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/reviewerguidelines.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewerguidelines.md"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"🎪 ACL 2025 Reviews Are Out: To Rebut or Flee? The Harsh Reality of NLP’s \"Publish or Perish\" Circus | CSPaper Forum","url":"https://forum.cspaper.org/topic/27/acl-2025-reviews-are-out-to-rebut-or-flee-the-harsh-reality-of-nlp-s-publish-or-perish-circus"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL ARR 2025 May | OpenReview","url":"https://openreview.net/group?id=aclweb.org%2FACL%2FARR%2F2025%2FMay"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"}]

Based on the search results, here's information about the ACL ARR review form for 2025-2026:

## Review Scoring Dimensions

Starting with February 2025, ARR reviewers are asked to provide three scores: soundness, excitement, and overall recommendation.

### Soundness Score
Soundness scores must be justified by the text of the review. For experimental papers, reviewers should consider the depth and/or breadth of the research questions investigated, technical soundness of experiments, and methodological validity of evaluation. For position papers and surveys, they should consider whether the current state of the field is adequa
…[truncated 817 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 10595
}
```

</details>

---


### Tool call

_source line 698 · 2026-05-23T01:12:13.874661+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿报告\n\n**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models\n**Venue**: EMNLP 2026 (via ACL ARR)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 1. Summary\n\n本文将 Generalizability Theory (G-theory) 应用于 LLM 评估方差分解，使用 8 个 7–9B 开源指令微调模型和 5 个 benchmark（~230 万条记录），跨 7 个 facet（item, model, precision, prompt, template, seed, ordering）进行全交叉因子设计。核心贡献是 D-study 预算框架：3-prompt × 3-seed 设计以 178 items 达到 G ≥ 0.80，相比 552 items 的单条件设计减少 3.1× 的 item 需求。次要发现包括精度可分离性受限于 binary scoring（C2）和 MC/FF 格式关联方差模式（exploratory）。该工作扩展了 Messing (2026) 从单 benchmark 到跨 benchmark 的 G-theory 应用。\n\n---\n\n## 2. Strengths\n\n**[S1] 严谨的实验设计与验证闭环**\nexp-001 的全交叉因子设计（7 facets, 460,800 records）和 exp-002 的系统性 reduced crossing（5 benchmarks, 2,304,000 records）设计合理。关键的是，作者验证了 reduced crossing 保留了方差结构（ΔG = 0.0008, Appendix A），而非简单假设。这是扎实的实证工作。\n\n**[S2] 示范级的 robustness analyses**\nAppendix A 覆盖了几乎所有可预见的方法论质疑：GLMM 补充分析、accuracy-range stability、Henderson Method I vs. REML 对比、probit simulation（259,200 条件下 binary/continuous rankings τ = 0.81）、null calibration（100 replications, observed-to-null ratio = 1.0008）、facet specification sensitivity、reduced crossing validation、以及 LOMO leave-one-model-out stability。这种预防性的 robustness 检验远超大多数投稿。\n\n**[S3] D-study 预算的实用价值**\nTable 4 和 Table 7 提供了可直接操作的评估设计指南，区分了 item-minimizing（multi-facet）和 evaluation-minimizing（single-condition）两种策略。Figure 1 的 D-study 曲线直观展示了 G coefficient 随 item 数量和条件数的变化。Section 5 对两种策略的适用场景描述清晰：expert-crafted benchmarks 适合 multi-facet，compute-constrained 场景适合 single-condition。\n\n**[S4] Related work positioning 清晰**\n论文准确定位了与 Messing (2026) 的三个差异化方向，并系统覆盖了 IRT 方向（Lalor et al., 2019; Rodriguez et al., 2021; Maia Polo et al., 2024; Zhou et al., 2026; Li et al., 2025）、方差分解方向（Bouthillier et al., 2021; Dodge et al., 2020; Henderson et al., 2018）、以及 psychometrics 经典文献（Shavelson & Webb, 1991; Brennan, 2001; Cardinet et al., 2010）。Section 2 的 \"Positioning\" 段落简洁有效。\n\n**[S5] Limitations section 诚实且全面**\nSection 6 主动覆盖了 temporal correlation、model exchangeability、binary scoring constraint、benchmark sample size (n=5)、few-shot ordering vs. identity、cross-validation 限制（仅 MMLU）、以及 contamination 对预算估计的影响。这种自我评估的深度反映了作者对方法论局限的清醒认识。\n\n---\n\n## 3. Weaknesses\n\n**[W1] Must-Fix: \"3.1× item reduction\" 标题 framing 具有误导性**\n\n- **具体位置**: Abstract (\"a 3.1× item reduction over single-condition designs\"), Section 1 (\"a 3.1× item reduction from 552 single-condition items\"), Section 5\n- **问题**: 论文以 \"3.1× item reduction\"（552 → 178 items）作为核心 headline，但推荐的 3-prompt × 3-seed 设计实际需要 178 × 9 = 1,602 次评估/模型，而 baseline 单条件设计仅需 552 次评估。**总计算成本增加了约 2.9×**（1,602/552）。对于一篇关于评估 *budget* 的论文，将 item count 下降包装为 \"reduction\" 而淡化总评估量上升，存在系统性误导。\n- **为什么影响接收**: 如果 reviewer 或读者基于标题理解为\"用更少的资源获得同等可靠性\"，而实际结论是\"用更多的资源获得更高可靠性但覆盖更少的 items\"，论文的 practical claim 会被实质性削弱。Section 5 的确承认了这一 tradeoff（\"multi-facet designs minimize item count... more items under fewer conditions suit compute-constrained evaluation\"），但这一关键区分被埋在结论段中，Abstract 和 Introduction 完全未提及。\n- **建议修改方向**: 在 Abstract 和 Introduction 中明确呈现 tradeoff：\"178 items × 9 conditions (1,602 evaluations) achieves G ≥ 0.80, trading 2.9× more total evaluations for 3.1× fewer unique items with substantially higher measurement reliability compared to 552 single-condition evaluations.\" 或引入 \"cost-per-G-point\" 指标使对比更公正。\n\n**[W2] Should-Fix: C2（precision separability）作为独立 contribution 过于单薄**\n\n- **具体位置**: Section 4.4, Contributions list (Section 1)\n- **问题**: C2 的核心发现——BF16/FP16 在 binary scoring 下功能上不可区分（<0.1% interaction），precision×temperature interaction 仅 1.3%——本质上是 binary scoring 信息损失的直接推论。当两种精度在 ≥99% 的 items 上给出相同的 0/1 判断时，方差分析当然无法区分它们。这是一个确认性结果而非发现。论文引用的 Yuan et al. (2025) 已报告 up to 9% accuracy variation from numerical precision，但在 binary 0/1 粒度下这些差异被压缩。将此包装为独立 contribution（与 C1 并列命名）夸大了工作的贡献范围。\n- **建议**: 将 C2 降级为 C1 方差分解结果的一个子发现（\"notably, precision effects are negligible under binary scoring\"），而非独立命名的 contribution。\n\n**[W3] Should-Fix: Format-associated variance patterns 统计效力不足且呈现方式过于积极**\n\n- **具体位置**: Section 4.3, Table 3\n- **问题**: MC vs. FF 方差模式对比基于 n = 5 benchmarks（3 MC, 2 FF），使用 p = 0.10 作为显著性阈值。论文承认 \"exploratory\" 和 \"hypothesis-generating\"，但仍有以下问题：\n  - (a) Spearman ρ = 0.82 (p = 0.089, n = 5) 在任何传统阈值下都不显著；\n  - (b) 论文另报 cross-benchmark Spearman ρ = 0.90 (p = 0.006, n = 10)，但这是 within-MMLU 10 subjects 的结果，**不是独立的 cross-benchmark 证据**，两者被混淆呈现；\n  - (c) MC vs. FF 的方差差异可能反映 benchmark 构建质量、难度分布、选项数量等混淆因素，而非格式本身。\n- **建议**: 明确分离 within-MMLU subject-level 证据和 cross-benchmark 证据；承认 n = 5 本质上无统计效力区分格式效应与 benchmark 特异性效应；考虑控制 item difficulty 分布后的残差分析。\n\n**[W4] Should-Fix: 相对于 Messing (2026) 的增量贡献边界性**\n\n- **具体位置**: Section 2 (Positioning paragraph)\n- **问题**: 三个扩展方向逐一审视——(i) 将 judge identity 替换为 infrastructure facets (seed, ordering, temperature) 是 facet 替换而非方法论创新，G-theory 框架不变；(ii) 从 1 个 benchmark 扩展到 5 个增加了 scope 但方差分解的核心故事高度一致（item 主效应在所有 benchmark 上都占主导）；(iii) D-study budget projections 是 G-theory 的标准产出（D-study 是 psychometrics 教科书内容，见 Brennan 2001 Ch. 4），并非方法论贡献。三者叠加的增量价值是否足够 EMNLP main conference 是核心问题。\n- **为什么影响评分**: excitement 维度。论文是对已有方法论在新领域的 competent application，但缺乏方法论创新或出人意料的发现。\"Item selection dominates variance\" 与 \"replication conditions improve reliability\" 都是预期结论。\n- **潜在反驳**: 作者可论证 (a) cross-benchmark D-study 提供了 Messing 无法给出的实用设计指南，(b) format-associated pattern（虽然 underpowered）开辟了新的研究方向，(c) infrastructure facets 的独立分析回答了不同于 judge-based evaluation 的问题。\n\n**[W5] Should-Fix: Abstract 数字密度过高，核心 message 被淹没**\n\n- **具体位置**: Abstract\n- **问题**: Abstract 包含至少 20 个具体数值：7–9B, 8 models, 5 benchmarks, 2.3 million, 34–38%, 3-prompt, 3-seed, G ≥ 0.80, 178 items, 1,602, 3.1×, 552, 1,296-condition, 36%, <0.1%, 24-parameter, GB-72B, 0.96, BF16, FP16 等。读者在首次阅读时难以提取核心 message。\n- **建议**: 保留 3–4 个最关键数字（G ≥ 0.80, 178 items, item variance 占比, cross-benchmark consistency），其余移入正文。一个好的 abstract 应让读者在 30 秒内理解 \"so what\"。\n\n**[W6] Minor: Conclusion (Section 5) 对实用影响讨论不足**\n\n- **具体位置**: Section 5（约 1/3 页）\n- **问题**: 作为一篇定位于提供 practical guidance 的论文，Conclusion 未讨论：(a) 现有 benchmark 套件是否应据此重组（如 MMLU 的 subject 子集优化）；(b) benchmark 开发者 vs. 使用者应如何分别应用这些预算；(c) 对 leaderboard 运营的具体建议。\n- **建议**: 扩展 Conclusion 或添加 Discussion section 讨论 practical implications。\n\n**[W7] Minor: Model main effect 仅 2.8%（Table 2）引发 generalizability 疑问**\n\n- **具体位置**: Table 2, Section 4.1\n- **问题**: 8 个模型的 model main effect 仅 2.8%，意味着这些模型在整体准确率上几乎不可区分。虽然 model×item interaction 为 25% 表明模型在不同 items 上有差异化表现，但 model main effect 如此之低提示模型样本可能过于同质（均为 7–9B instruction-tuned）。D-study budgets 是否泛化到更多样的模型组合（如 1B vs. 70B, base vs. RLHF, open vs. API）是未解答的关键问题。\n- **Section 4.6 的 preliminary 72B validation 部分回应了此问题**，但仅限单架构（Qwen2.5），证据有限。\n\n**[W8] Minor: Anonymous arXiv 自引可能破坏匿名性**\n\n- **具体位置**: References, \"Anonymous. 2025. Variance-aware LLM annotation. arXiv preprint arXiv:2601.02310.\"\n- **问题**: 以 \"Anonymous\" 引用含可解析 arXiv ID 的论文，技术上符合 double-blind 政策，但 reviewer 可通过 arXiv URL 查找作者身份。建议评估此引用是否为必要引用，或可用已发表工作的内容替代。\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** Table 4 显示 multi-facet 3×3 设计需 1,602 evaluations，单条件设计仅需 552。能否提供具体的 GPU-hours 或 API 成本对比，明确在何种场景下 multi-facet 设计优于单条件设计（尽管总成本更高）？\n\n**Q2.** Model main effect 仅 2.8%（Table 2）。D-study budgets 是否泛化到比较更多样模型集合的场景（如不同规模、不同训练范式、API 模型）？Table 5 的 LOMO analysis 是否能回答此问题？\n\n**Q3.** Section 3.5 验证了 binary scoring 假设，但 Appendix A 确认 partial credit \"fundamentally reshapes variance structure\"。鉴于很多现代 benchmark 使用非 binary 评分（如 BLEU, F1, rubric-based），这些基于 binary scoring 的 budgets 对此类场景的参考价值如何？\n\n**Q4.** Section 4.3 的 MC vs. FF 方差模式是否可能反映 benchmark 构建差异（如 item 质量、difficulty 分布、domain 覆盖）而非格式本身？是否考虑过控制 item difficulty 后的残差分析？\n\n**Q5.** References 中 \"Anonymous. 2025\" 是否为作者自己的工作？如果是，能否以更好地保护匿名性的方式引用？\n\n---\n\n## 5. Missing References\n\nRelated work 覆盖总体充分。以下两篇可能值得补充：\n\n1. **Saxon et al. (2024)** — \"Benchmarks as Microscopes: A Call for Model Metrology\" (COLM 2024). 直接相关于论文的 measurement-theoretic framing——提出 benchmark 应从计量学（metrology）角度设计，与本文 G-theory 的 measurement reliability 视角互补。\n\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards\" (ACL 2024). 讨论 leaderboard 排名对评估方法论选择的敏感性，与本文 prompt/seed/ordering 导致排名变化的发现直接相关。\n\n---\n\n## 6. Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 (Strong) | 实验设计严谨，全交叉因子 + reduced crossing 验证充分。Henderson Method I 使用得当，robustness analyses 覆盖面广（GLMM, probit simulation, null calibration, LOMO）。主要扣分点：binary scoring 限制了方差分解的适用范围；model sample 较同质。 |\n| **Excitement** | 2.5/5 (Potentially Interesting) | 应用已有 psychometric 框架（G-theory）到 LLM 评估——方法论本身非新。核心发现（item dominates variance, replication improves reliability）在预期范围内。D-study budgets 有实用价值但非 surprising。C2 是确认性结果，C3 underpowered。 |\n| **Reproducibility** | 4/5 | 实验设置描述详细（Appendix G models/prompts, Table 1 design matrix）。承诺发布代码/数据/D-study calculator。vLLM 0.9.2 + CUDA-level nondeterminism 控制。MMLU stratified sampling 清晰。扣分点：cross-validation 仅限 MMLU (CV=3.1%)。 |\n| **Confidence** | 4/5 | 我对 G-theory 方法论和 LLM 评估领域有充分了解，仔细阅读了全文和所有附录。 |\n\n### Overall Assessment: **3.5 (Borderline Conference)**\n\n本文是 G-theory 在 LLM 评估领域的一项方法论 competent、实验严谨的实证工作。D-study 预算框架（C1）是最强贡献，为评估设计提供了可操作的指导。但工作的新颖性有限——相对于 Messing (2026)，使用相同框架、不同 facets、更多 benchmarks，属于 systematic extension 而非 methodological advance。\"3.1× item reduction\" headline 掩盖了总评估量 2.9× 增加的事实（W1），需要根本性 reframing。三个 contributions 中 C2（precision separability）是预期结论，C3（format-associated patterns）统计效力不足——实际上只有 C1 是 substantive contribution。Scope 受限于 8 个同质 7-9B 模型和 binary scoring，限制了 generalizability。\n\n**使论文达到 Conference (4.0) 需要**：(1) 透明呈现评估成本 tradeoff 而非仅 item reduction；(2) 将 C2 降级为子发现、C3 更显著地标注为 preliminary observation；(3) 扩展 Conclusion/Discussion 的 practical implications；(4) 如果能补充 partial credit scoring 的完整分析，将显著增强贡献。\n\n**当前适合 Findings**：soundness 足够，practical value 有，但 excitement 和 novelty 未达 main conference 阈值。3.5 分反映在 Borderline Conference / strong Findings 的边界上。\n",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿报告\n\n**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models\n**Venue**: EMNLP 2026 (via ACL ARR)\n**审查侧重**: 新颖性 + 完整性 + 写作质量\n\n---\n\n## 1. Summary\n\n本文将 Generalizability Theory (G-theory) 应用于 LLM 评估方差分解，使用 8 个 7–9B 开源指令微调模型和 5 个 benchmark（~230 万条记录），跨 7 个 facet（item, model, precision, prompt, template, seed, ordering）进行全交叉因子设计。核心贡献是 D-study 预算框架：3-prompt × 3-seed 设计以 178 items 达到 G ≥ 0.80，相比 552 items 的单条件设计减少 3.1× 的 item 需求。次要发现包括精度可分离性受限于 binary scoring（C2）和 MC/FF 格式关联方差模式（exploratory）。该工作扩展了 Messing (2026) 从单 benchmark 到跨 benchmark 的 G-theory 应用。\n\n---\n\n## 2. Strengths\n\n**[S1] 严谨的实验设计与验证闭环**\nexp-001 的全交叉因子设计（7 facets, 460,800 records）和 exp-002 的系统性 reduced crossing（5 benchmarks, 2,304,000 records）设计合理。关键的是，作者验证了 reduced crossing 保留了方差结构（ΔG = 0.0008, Appendix A），而非简单假设。这是扎实的实证工作。\n\n**[S2] 示范级的 robustness analyses**\nAppendix A 覆盖了几乎所有可预见的方法论质疑：GLMM 补充分析、accuracy-range stability、Henderson Method I vs. REML 对比、probit simulation（259,200 条件下 binary/continuous rankings τ = 0.81）、null calibration（100 replications, observed-to-null ratio = 1.0008）、facet specification sensitivity、reduced crossing validation、以及 LOMO leave-one-model-out stability。这种预防性的 robustness 检验远超大多数投稿。\n\n**[S3] D-study 预算的实用价值**\nTable 4 和 Table 7 提供了可直接操作的评估设计指南，区分了 item-minimizing（multi-facet）和 evaluation-minimizing（single-condition）两种策略。Figure 1 的 D-study 曲线直观展示了 G coefficient 随 item 数量和条件数的变化。Section 5 对两种策略的适用场景描述清晰：expert-crafted benchmarks 适合 multi-facet，compute-constrained 场景适合 single-condition。\n\n**[S4] Related work positioning 清晰**\n论文准确定位了与 Messing (2026) 的三个差异化方向，并系统覆盖了 IRT 方向（Lalor et al., 2019; Rodriguez et al., 2021; Maia Polo et al., 2024; Zhou et al., 2026; Li et al., 2025）、方差分解方向（Bouthillier et al., 2021; Dodge et al., 2020; Henderson et al., 2018）、以及 psychometrics 经典文献（Shavelson & Webb, 1991; Brennan, 2001; Cardinet et al., 2010）。Section 2 的 \"Positioning\" 段落简洁有效。\n\n**[S5] Limitations section 诚实且全面**\nSection 6 主动覆盖了 temporal correlation、model exchangeability、binary scoring constraint、benchmark sample size (n=5)、few-shot ordering vs. identity、cross-validation 限制（仅 MMLU）、以及 contamination 对预算估计的影响。这种自我评估的深度反映了作者对方法论局限的清醒认识。\n\n---\n\n## 3. Weaknesses\n\n**[W1] Must-Fix: \"3.1× item reduction\" 标题 framing 具有误导性**\n\n- **具体位置**: Abstract (\"a 3.1× item reduction over single-condition designs\"), Section 1 (\"a 3.1× item reduction from 552 single-condition items\"), Section 5\n- **问题**: 论文以 \"3.1× item reduction\"（552 → 178 items）作为核心 headline，但推荐的 3-prompt × 3-seed 设计实际需要 178 × 9 = 1,602 次评估/模型，而 baseline 单条件设计仅需 552 次评估。**总计算成本增加了约 2.9×**（1,602/552）。对于一篇关于评估 *budget* 的论文，将 item count 下降包装为 \"reduction\" 而淡化总评估量上升，存在系统性误导。\n- **为什么影响接收**: 如果 reviewer 或读者基于标题理解为\"用更少的资源获得同等可靠性\"，而实际结论是\"用更多的资源获得更高可靠性但覆盖更少的 items\"，论文的 practical claim 会被实质性削弱。Section 5 的确承认了这一 tradeoff（\"multi-facet designs minimize item count... more items under fewer conditions suit compute-constrained evaluation\"），但这一关键区分被埋在结论段中，Abstract 和 Introduction 完全未提及。\n- **建议修改方向**: 在 Abstract 和 Introduction 中明确呈现 tradeoff：\"178 items × 9 conditions (1,602 evaluations) achieves G ≥ 0.80, trading 2.9× more total evaluations for 3.1× fewer unique items with substantially higher measurement reliability compared to 552 single-condition evaluations.\" 或引入 \"cost-per-G-point\" 指标使对比更公正。\n\n**[W2] Should-Fix: C2（precision separability）作为独立 contribution 过于单薄**\n\n- **具体位置**: Section 4.4, Contributions list (Section 1)\n- **问题**: C2 的核心发现——BF16/FP16 在 binary scoring 下功能上不可区分（<0.1% interaction），precision×temperature interaction 仅 1.3%——本质上是 binary scoring 信息损失的直接推论。当两种精度在 ≥99% 的 items 上给出相同的 0/1 判断时，方差分析当然无法区分它们。这是一个确认性结果而非发现。论文引用的 Yuan et al. (2025) 已报告 up to 9% accuracy variation from numerical precision，但在 binary 0/1 粒度下这些差异被压缩。将此包装为独立 contribution（与 C1 并列命名）夸大了工作的贡献范围。\n- **建议**: 将 C2 降级为 C1 方差分解结果的一个子发现（\"notably, precision effects are negligible under binary scoring\"），而非独立命名的 contribution。\n\n**[W3] Should-Fix: Format-associated variance patterns 统计效力不足且呈现方式过于积极**\n\n- **具体位置**: Section 4.3, Table 3\n- **问题**: MC vs. FF 方差模式对比基于 n = 5 benchmarks（3 MC, 2 FF），使用 p = 0.10 作为显著性阈值。论文承认 \"exploratory\" 和 \"hypothesis-generating\"，但仍有以下问题：\n  - (a) Spearman ρ = 0.82 (p = 0.089, n = 5) 在任何传统阈值下都不显著；\n  - (b) 论文另报 cross-benchmark Spearman ρ = 0.90 (p = 0.006, n = 10)，但这是 within-MMLU 10 subjects 的结果，**不是独立的 cross-benchmark 证据**，两者被混淆呈现；\n  - (c) MC vs. FF 的方差差异可能反映 benchmark 构建质量、难度分布、选项数量等混淆因素，而非格式本身。\n- **建议**: 明确分离 within-MMLU subject-level 证据和 cross-benchmark 证据；承认 n = 5 本质上无统计效力区分格式效应与 benchmark 特异性效应；考虑控制 item difficulty 分布后的残差分析。\n\n**[W4] Should-Fix: 相对于 Messing (2026) 的增量贡献边界性**\n\n- **具体位置**: Section 2 (Positioning paragraph)\n- **问题**: 三个扩展方向逐一审视——(i) 将 judge identity 替换为 infrastructure facets (seed, ordering, temperature) 是 facet 替换而非方法论创新，G-theory 框架不变；(ii) 从 1 个 benchmark 扩展到 5 个增加了 scope 但方差分解的核心故事高度一致（item 主效应在所有 benchmark 上都占主导）；(iii) D-study budget projections 是 G-theory 的标准产出（D-study 是 psychometrics 教科书内容，见 Brennan 2001 Ch. 4），并非方法论贡献。三者叠加的增量价值是否足够 EMNLP main conference 是核心问题。\n- **为什么影响评分**: excitement 维度。论文是对已有方法论在新领域的 competent application，但缺乏方法论创新或出人意料的发现。\"Item selection dominates variance\" 与 \"replication conditions improve reliability\" 都是预期结论。\n- **潜在反驳**: 作者可论证 (a) cross-benchmark D-study 提供了 Messing 无法给出的实用设计指南，(b) format-associated pattern（虽然 underpowered）开辟了新的研究方向，(c) infrastructure facets 的独立分析回答了不同于 judge-based evaluation 的问题。\n\n**[W5] Should-Fix: Abstract 数字密度过高，核心 message 被淹没**\n\n- **具体位置**: Abstract\n- **问题**: Abstract 包含至少 20 个具体数值：7–9B, 8 models, 5 benchmarks, 2.3 million, 34–38%, 3-prompt, 3-seed, G ≥ 0.80, 178 items, 1,602, 3.1×, 552, 1,296-condition, 36%, <0.1%, 24-parameter, GB-72B, 0.96, BF16, FP16 等。读者在首次阅读时难以提取核心 message。\n- **建议**: 保留 3–4 个最关键数字（G ≥ 0.80, 178 items, item variance 占比, cross-benchmark consistency），其余移入正文。一个好的 abstract 应让读者在 30 秒内理解 \"so what\"。\n\n**[W6] Minor: Conclusion (Section 5) 对实用影响讨论不足**\n\n- **具体位置**: Section 5（约 1/3 页）\n- **问题**: 作为一篇定位于提供 practical guidance 的论文，Conclusion 未讨论：(a) 现有 benchmark 套件是否应据此重组（如 MMLU 的 subject 子集优化）；(b) benchmark 开发者 vs. 使用者应如何分别应用这些预算；(c) 对 leaderboard 运营的具体建议。\n- **建议**: 扩展 Conclusion 或添加 Discussion section 讨论 practical implications。\n\n**[W7] Minor: Model main effect 仅 2.8%（Table 2）引发 generalizability 疑问**\n\n- **具体位置**: Table 2, Section 4.1\n- **问题**: 8 个模型的 model main effect 仅 2.8%，意味着这些模型在整体准确率上几乎不可区分。虽然 model×item interaction 为 25% 表明模型在不同 items 上有差异化表现，但 model main effect 如此之低提示模型样本可能过于同质（均为 7–9B instruction-tuned）。D-study budgets 是否泛化到更多样的模型组合（如 1B vs. 70B, base vs. RLHF, open vs. API）是未解答的关键问题。\n- **Section 4.6 的 preliminary 72B validation 部分回应了此问题**，但仅限单架构（Qwen2.5），证据有限。\n\n**[W8] Minor: Anonymous arXiv 自引可能破坏匿名性**\n\n- **具体位置**: References, \"Anonymous. 2025. Variance-aware LLM annotation. arXiv preprint arXiv:2601.02310.\"\n- **问题**: 以 \"Anonymous\" 引用含可解析 arXiv ID 的论文，技术上符合 double-blind 政策，但 reviewer 可通过 arXiv URL 查找作者身份。建议评估此引用是否为必要引用，或可用已发表工作的内容替代。\n\n---\n\n## 4. Questions for Authors\n\n**Q1.** Table 4 显示 multi-facet 3×3 设计需 1,602 evaluations，单条件设计仅需 552。能否提供具体的 GPU-hours 或 API 成本对比，明确在何种场景下 multi-facet 设计优于单条件设计（尽管总成本更高）？\n\n**Q2.** Model main effect 仅 2.8%（Table 2）。D-study budgets 是否泛化到比较更多样模型集合的场景（如不同规模、不同训练范式、API 模型）？Table 5 的 LOMO analysis 是否能回答此问题？\n\n**Q3.** Section 3.5 验证了 binary scoring 假设，但 Appendix A 确认 partial credit \"fundamentally reshapes variance structure\"。鉴于很多现代 benchmark 使用非 binary 评分（如 BLEU, F1, rubric-based），这些基于 binary scoring 的 budgets 对此类场景的参考价值如何？\n\n**Q4.** Section 4.3 的 MC vs. FF 方差模式是否可能反映 benchmark 构建差异（如 item 质量、difficulty 分布、domain 覆盖）而非格式本身？是否考虑过控制 item difficulty 后的残差分析？\n\n**Q5.** References 中 \"Anonymous. 2025\" 是否为作者自己的工作？如果是，能否以更好地保护匿名性的方式引用？\n\n---\n\n## 5. Missing References\n\nRelated work 覆盖总体充分。以下两篇可能值得补充：\n\n1. **Saxon et al. (2024)** — \"Benchmarks as Microscopes: A Call for Model Metrology\" (COLM 2024). 直接相关于论文的 measurement-theoretic framing——提出 benchmark 应从计量学（metrology）角度设计，与本文 G-theory 的 measurement reliability 视角互补。\n\n2. **Alzahrani et al. (2024)** — \"When Benchmarks are Targets: Revealing the Sensitivity of Large Language Model Leaderboards\" (ACL 2024). 讨论 leaderboard 排名对评估方法论选择的敏感性，与本文 prompt/seed/ordering 导致排名变化的发现直接相关。\n\n---\n\n## 6. Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 4/5 (Strong) | 实验设计严谨，全交叉因子 + reduced crossing 验证充分。Henderson Method I 使用得当，robustness analyses 覆盖面广（GLMM, probit simulation, null calibration, LOMO）。主要扣分点：binary scoring 限制了方差分解的适用范围；model sample 较同质。 |\n| **Excitement** | 2.5/5 (Potentially Interesting) | 应用已有 psychometric 框架（G-theory）到 LLM 评估——方法论本身非新。核心发现（item dominates variance, replication improves reliability）在预期范围内。D-study budgets 有实用价值但非 surprising。C2 是确认性结果，C3 underpowered。 |\n| **Reproducibility** | 4/5 | 实验设置描述详细（Appendix G models/prompts, Table 1 design matrix）。承诺发布代码/数据/D-study calculator。vLLM 0.9.2 + CUDA-level nondeterminism 控制。MMLU stratified sampling 清晰。扣分点：cross-validation 仅限 MMLU (CV=3.1%)。 |\n| **Confidence** | 4/5 | 我对 G-theory 方法论和 LLM 评估领域有充分了解，仔细阅读了全文和所有附录。 |\n\n### Overall Assessment: **3.5 (Borderline Conference)**\n\n本文是 G-theory 在 LLM 评估领域的一项方法论 competent、实验严谨的实证工作。D-study 预算框架（C1）是最强贡献，为评估设计提供了可操作的指导。但工作的新颖性有限——相对于 Messing (2026)，使用相同框架、不同 facets、更多 benchmarks，属于 systematic extension 而非 methodological advance。\"3.1× item reduction\" headline 掩盖了总评估量 2.9× 增加的事实（W1），需要根本性 reframing。三个 contributions 中 C2（precision separability）是预期结论，C3（format-associated patterns）统计效力不足——实际上只有 C1 是 substantive contribution。Scope 受限于 8 个同质 7-9B 模型和 binary scoring，限制了 generalizability。\n\n**使论文达到 Conference (4.0) 需要**：(1) 透明呈现评估成本 tradeoff 而非仅 item reduction；(2) 将 C2 降级为子发现、C3 更显著地标注为 preliminary observation；(3) 扩展 Conclusion/Discussion 的 practical implications；(4) 如果能补充 partial credit scoring 的完整分析，将显著增强贡献。\n\n**当前适合 Findings**：soundness 足够，practical value 有，但 excitement 和 novelty 未达 main conference 阈值。3.5 分反映在 Borderline Conference / strong Findings 的边界上。\n",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 699 · 2026-05-23T01:12:17.640123+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3765
}
```

</details>

---


### Tool call

_source line 700 · 2026-05-23T01:12:22.018398+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
  "max_results": "1"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__cleanup_pdf_images",
    "max_results": "1"
  }
}
```

</details>

---


### Tool result

_source line 701 · 2026-05-23T01:12:22.119365+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 702 · 2026-05-23T01:12:26.688890+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 703 · 2026-05-23T01:12:26.739522+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 704 · 2026-05-23T01:12:36.041991+00:00_

审稿报告已提交至 Review Director。

**核心判断：Overall 3.5（Borderline Conference）**

主要发现：
- **最强贡献是 D-study 预算框架 (C1)**，但 "3.1× item reduction" 标题掩盖了总评估量实际增加 2.9× 的事实（Must-Fix）
- **C2（precision separability）是预期确认而非新发现**，建议降级为子发现
- **C3（format-associated patterns）n=5, p=0.10，统计效力不足**
- **相对 Messing (2026) 增量有限**——同一框架、不同 facets、更多 benchmarks，属 systematic extension
- **Soundness 4/5**（robustness analyses 极为出色），**Excitement 2.5/5**（方法论非新、核心发现在预期范围内）
- 建议补充 Saxon et al. (2024, COLM) 和 Alzahrani et al. (2024, ACL) 两篇缺失引用

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 18

## Round 18

14 recorded events


### User

_source line 705 · 2026-05-23T01:13:42.010194+00:00_

[Round 1 审稿请求]:
## 交叉分享：Reviewer 1 的完整审稿意见

请逐条回应 Reviewer 1 的每个 Weakness 和 Question：
- **[AGREE]** 同意并说明理由
- **[REBUT]** 反驳并提供证据（cite 具体 Section/Table/Figure）

---

以下是 Reviewer 1 的完整审稿意见：

### Strengths

**[S1]** 首次在 LLM 评估中同时交叉 infrastructure（precision、temperature、ordering）和 methodology（prompt、seed）facets 进行 G-theory 分析，填补了现有文献仅处理单一维度方差的空白（§1, §2）。

**[S2]** 实验规模大且设计严谨：exp-001 完全交叉设计覆盖 460,800 条记录（Table 1），exp-002 扩展至 5 个 benchmark 的 2,304,000 条记录。完整 factorial 设计使方差分量可无混淆地估计。

**[S3]** 实用价值突出：D-study reproducibility budget（Table 4, Figure 1）为 benchmark 设计者和评估实践者提供了可直接使用的 item 数量指南，承诺开源 G-theory pipeline 和 D-study calculator。

**[S4]** Appendix A 的 robustness 分析极为全面：GLMM complement（ρ=1.0 rank preservation）、accuracy-range stability、REML（CV < 3.1%）、null calibration（observed/null = 1.0008）、facet sensitivity、LOMO stability（40 subsets，Table 5）——远超大多数投稿的 sensitivity 分析深度。

**[S5]** Item difficulty heterogeneity 分析（§4.3, Appendix D-F）揭示了 MC vs FF benchmark 的方差结构差异（item-dominated vs distributed），为 benchmark 设计提供了有意义的 typology。

### Weaknesses

**[W1] [Should-Fix] Henderson Method I 在 binary 数据上的适用性论证不充分**
- 具体位置：§3.5, Appendix A
- 问题：Henderson Method I 假设连续正态数据。论文的 probit simulation 报告 Spearman ρ = 0.732，仅为中等相关，但论文定性为 "robustness"。Bias 报告仅限于特定 difficulty stratum（|bias| = 0.28–0.37 for p ∈ [0.5, 0.8]），缺少对极端 difficulty items 的 bias/RMSE 完整报告。GLMM complement 显示 rank preservation ρ = 1.0，但 rank correlation ≠ magnitude agreement——若 variance components 绝对值存在系统性偏移，D-study budget 的具体数字可能偏离。
- 建议：补充 probit simulation 的完整 bias/RMSE 分解（按 difficulty quintile），明确 D-study budget 在 GLMM 框架下的对应数值。

**[W2] [Should-Fix] Forward prediction（Table 8）为 in-sample 验证，非 out-of-sample**
- 具体位置：§4.5, Table 8
- 问题：4-model subset（DeepSeek, Llama, Mistral, Qwen3）是 8-model 全集的子集。从子集估计方差分量后预测全集 G 系数，本质上是 in-sample cross-validation。Error 范围 0.96–6.88% 看似不大，但 in-sample 设计 inherently 低估 prediction error。LOMO 是 leave-one-model-out（7→8），同样非 truly held-out families。
- 建议：明确标注为 in-sample consistency check；更理想的做法是用 non-overlapping model pairs 做 split-half cross-validation。

**[W3] [Should-Fix] Scale validation 局限于 Qwen2.5 单一架构家族**
- 具体位置：§4.6
- 问题：Within-family validation（Qwen2.5 3B/7B/72B）显示 variance structure 在 scale 上稳定，但同一家族共享 training recipe 和 tokenizer，item difficulty profile 可能高度相关。论文 claim "preliminary evidence that budgets generalize beyond the 7–9B range" 缺乏 cross-family 支撑。
- 建议：明确 "within-family only" 限制；如有数据补充 Llama-3.1 8B→70B 验证。

**[W4] [Should-Fix] Partial-credit scoring sensitivity 对发现影响讨论不足**
- 具体位置：§4.4, §5
- 问题：Binary → partial-credit 导致 G 从 0.76→0.55，ρ = 0.26。所有 D-study budgets、format-associated patterns 都 conditioned on binary scoring，但 Conclusion 仅一句带过。当前许多重要 benchmark 使用 non-binary scoring（GSM8K 部分评分、LLM-as-judge）。
- 建议：在 Conclusion/Limitations 中明确所有 budgets 仅对 binary correctness scoring 有效。

**[W5] [Should-Fix] Data contamination 作为 model×item interaction（30–36%）的混淆变量讨论不足**
- 具体位置：§6
- 问题：Model×item interaction 是第二大方差来源（up to 36%），但 data contamination 可能 inflate 该分量。论文仅提供间接证据（"三个独立 MC benchmarks"），未做 contamination detection。
- 建议：讨论 contamination 如何影响 variance decomposition；引用相关检测方法并解释为何未采用。

**[W6] [Minor] Format-associated pattern（§4.3）n=5, p=0.10，exploratory 但叙事权重过大**
- 问题：MC vs FF 对比基于 n=5，permutation p=0.10，但占约大半页篇幅且被提升为 C1 核心组成。混淆变量（prompt semantics、scoring 方式差异）讨论不完整。
- 建议：缩短 §4.3 或降级为 preliminary observation。

**[W7] [Minor] C2（precision separability）本质为 null result，与 C1 并列有 overclaiming 之嫌**
- 问题：BF16/FP16 interchangeable（< 0.1% interaction）不令人惊讶，列为 main contribution 权重过高。
- 建议：降级为 additional finding 或合并入 C1。

**[W8] [Minor] Bootstrap CI 仅 item-level resampling，model-facet uncertainty 可能被低估**
- 问题：Model facet 仅 8 levels + purposively selected。Item-level bootstrap 不能捕获 "换一组 models" 的 uncertainty。
- 建议：明确 CI 仅反映 item-sampling variability。

**[W9] [Minor] "3.1× item reduction" framing 未凸显总评估量从 552 增至 1,602（增加 2.9×）**
- 建议：在 Abstract 中平衡呈现 item reduction 和 total evaluation increase。

### Questions

**Q1.** Table 8 的 4 models 是 8 models 子集。是否有能力做 truly held-out 验证——例如用 exp-001 方差分量预测 exp-002 中某个全新 benchmark 的 G 系数？

**Q2.** Probit simulation ρ = 0.732：能否报告 variance components 的 MAPE 而非仅 rank correlation？对 D-study budget，magnitude accuracy 比 rank preservation 更关键。

**Q3.** Partial-credit G = 0.55, ρ = 0.26 是基于 GSM8K 单一 benchmark 吗？是否有其他 benchmark 上的验证？

**Q4.** LOMO Table 5 中 MATH 的 CV = 0.919——请澄清此为何种 quantity 的 coefficient of variation？若 CV 接近 1.0 是否反映 model facet 在该 benchmark 上高度不稳定？

**Q5.** FF benchmarks 残差 39.9–43.9%。是否考虑过 3-parameter IRT 的 guessing parameter 对 MC benchmarks 残差的解释？

### Missing References

- Oren et al. (2024) "Proving Test Set Contamination in Black Box Language Models"
- Brennan (2001, Ch. 12) 对 dichotomous data 的 G-theory 处理

### Overall Assessment
**Overall: 3.5 — Borderline Conference**, Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 706 · 2026-05-23T01:15:17.180686+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "5,7,8,11,12",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "5,7,8,11,12",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 707 · 2026-05-23T01:15:17.984558+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 484.1}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 503.5}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 492.3}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 585.6}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 498.8}], \"total_pages\": 16, \"rendered_pages\": 5, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 708 · 2026-05-23T01:15:23.964742+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool call

_source line 709 · 2026-05-23T01:15:24.466930+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 710 · 2026-05-23T01:15:24.970261+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1005
}
```

</details>

---


### Tool call

_source line 711 · 2026-05-23T01:15:25.021009+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool result

_source line 712 · 2026-05-23T01:15:25.122808+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 655
}
```

</details>

---


### Tool result

_source line 713 · 2026-05-23T01:15:25.626442+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 605
}
```

</details>

---


### Tool call

_source line 714 · 2026-05-23T01:18:00.389795+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### [REBUT] R1-W1: Henderson Method I 在 binary 数据上的适用性\n\nR1 称 \"Henderson Method I 假设连续正态数据\"——这一前提不准确。论文 Appendix A 明确引用 Brennan (2001, Ch. 12) 指出 **\"Henderson Method I produces unbiased estimates for balanced designs regardless of outcome distribution\"**。Henderson Method I 是基于均方的 ANOVA 估计器，对平衡设计的点估计不依赖分布假设，这是 G-theory 文献的标准结论。\n\n**但我同意 R1 关于报告完整性的诉求**。probit simulation 的 Spearman ρ = 0.732 确实仅为中等相关，论文对此的解读偏乐观（称之为 \"robustness\"）。更重要的是，|bias| = 0.28–0.37 仅报告了 p ∈ [0.5, 0.8] 的 difficulty stratum，缺少极端 difficulty（p < 0.3 或 p > 0.9）的完整 bias/RMSE 分解。鉴于 MATH benchmark 的 mean accuracy 较低，extreme difficulty items 正是最需要 bias 报告的区间。\n\n**总结**：Henderson Method I 的分布无关性已在 Appendix A 论证（R1 可能未注意到），但 bias 报告的覆盖范围确实不完整。建议作者补充 full difficulty quintile 的 bias/RMSE 分解。Severity 应为 Should-Fix 而非影响核心方法论有效性的根本问题。\n\n---\n\n### [AGREE] R1-W2: Forward prediction 为 in-sample 验证\n\nR1 正确指出 Table 8 的 4-model subset（DeepSeek, Llama, Mistral, Qwen3）与 8-model 全集共享相同的 items、prompts、seeds 和 orderings。从子集方差分量预测全集 G 本质上是 **internal consistency check**，而非 out-of-sample prediction。Error 范围 0.96–6.88% 因此可能低估真实预测误差。\n\nLOMO（Table 5）虽然更接近 held-out 验证，但 leave-one-model-out 仍保留了 7/8 的模型重叠，不构成 truly independent validation。\n\nR1 建议 \"用 non-overlapping model pairs 做 split-half cross-validation\" 是合理的，但需注意只有 8 models 的情况下 split-half 仅有 4 vs. 4，方差估计会非常不稳定。更有价值的验证可能是 **用 exp-001 的方差分量预测 exp-002 中新 benchmark 的 G**（R1-Q1），但这需要假设方差结构跨 benchmark 稳定，而 Table 3 的 MC vs. FF 差异恰好质疑了这一假设。\n\n**建议**：论文应将 Table 8 重新标注为 \"internal consistency check\" 而非 \"forward prediction validation\"。\n\n---\n\n### [AGREE] R1-W3: Scale validation 局限于 Qwen2.5\n\n完全同意。Within-family validation（Qwen2.5 3B/7B/72B）共享 training recipe、tokenizer 和数据混合策略，item difficulty profile 高度相关。Section 4.6 的 claim \"preliminary evidence that budgets generalize beyond the 7–9B range\" 超出了证据支撑范围——准确表述应为 \"within Qwen2.5 family, variance structure is scale-invariant\"。\n\n补充观点：即使 Llama-3.1 8B→70B 的数据可用（如 R1 建议），仍然只是两个家族的 within-family 证据。真正的 cross-family scale validation 需要 3+ 架构家族 × 2+ scales 的交叉设计，这在当前资源下可能不可行但应在 Limitations 中明确说明。\n\n---\n\n### [AGREE] R1-W4: Partial-credit scoring 影响讨论不足\n\n同意。这是我自己审稿中也标记的问题（我的 W2 从不同角度涉及此点）。关键数据：binary → partial-credit 使 G 从 0.76 降至 0.55（Appendix A），且 ρ = 0.26 表明方差分量的相对排序也发生了根本性变化。这意味着 **所有 D-study budgets、format-associated patterns、以及 precision separability 结论都严格绑定于 binary correctness scoring**。\n\nSection 5 仅一句 \"partial credit analysis confirms that finer-grained rubrics require independent calibration (§3.5)\" 明显不足。当前 LLM 评估越来越多使用 LLM-as-judge、rubric-based scoring 和部分评分，这一限制的实际影响远大于论文当前呈现的权重。\n\n**建议**：在 Section 5 或 Limitations 中用 2-3 句明确所有 budgets 仅对 binary correctness 有效，并讨论 partial-credit 场景下的预期偏移方向。\n\n---\n\n### [AGREE] R1-W5: Contamination 作为 model×item interaction 混淆变量\n\n部分同意。R1 的核心论点成立：model×item interaction 高达 25–36%，而 differential contamination（不同模型在训练时接触了不同的 benchmark items）是这一分量的可信 confound。论文的间接证据（\"三个独立 MC benchmarks 方差结构一致\"）是必要但不充分的——**一致的 contamination 模式也能产生一致的方差结构**。\n\n但我认为论文 Section 6 中的一个论点值得更多关注：**\"Contamination affects absolute budget estimates but has limited impact on the multi-facet vs. single-condition budget ratio, since both designs are equally exposed to contaminated items.\"** 这个论点在逻辑上成立——如果 contamination 等比例地 inflate 了所有设计的 model×item interaction，则设计之间的相对效率比较不受影响。这一论点应在正文而非 Limitations 中更突出地呈现。\n\nR1 建议引用 Oren et al. (2024) 关于 contamination detection 的工作是合理的，但 contamination detection 方法在 open-weight 7–9B models 上的可靠性本身也有争议。\n\n---\n\n### [AGREE] R1-W6: Format-associated pattern 叙事权重过大\n\n完全同意，这与我的 W3 判断一致。n=5, permutation p=0.10 的分析占据约大半页篇幅并被隐含提升为核心发现之一，与其统计效力严重不匹配。\n\n补充我的 W3 中的一个额外论点：论文报告的 cross-benchmark Spearman ρ = 0.90 (p = 0.006, n = 10) 实际上是 **within-MMLU 的 10 subjects 分析**，而非独立的 cross-benchmark 证据。论文在呈现时混合了这两个层级的证据，可能让读者误以为有更强的跨 benchmark 支撑。\n\n---\n\n### [AGREE] R1-W7: C2 本质为 null result\n\n完全同意，与我的 W2 判断完全一致。BF16/FP16 在 binary scoring 下 <0.1% interaction 是 binary quantization 的必然结果，不构成 surprising finding。将其与 C1（D-study budgets）并列为独立 contribution 存在 overclaiming。\n\n---\n\n### [AGREE] R1-W8: Bootstrap CI 仅反映 item-sampling variability\n\n同意。8 models 是 purposively selected（非随机抽样），item-level bootstrap 无法捕获 \"换一组模型\" 的 uncertainty。论文应明确：**CIs 反映的是 item-sampling variability 条件于这 8 个特定模型的选择**，而非对更广泛模型总体的推断。\n\n这一点与 W3（model main effect 仅 2.8%）和 W7（model sample 同质性）形成呼应——如果模型样本本身不具代表性，那么条件于该样本的 CIs 的外部有效性更需质疑。\n\n---\n\n### [AGREE] R1-W9: \"3.1× item reduction\" framing\n\n完全同意，与我的 W1（Must-Fix）判断一致。Abstract 和 Introduction 应同时呈现 item reduction (3.1×) 和 total evaluation increase (~2.9×)。这是一篇关于 \"budget\" 的论文——只报告 budget 的一个维度是系统性误导。\n\n---\n\n## Questions 回应\n\n### R1-Q1: Truly held-out 验证\n\n好问题。用 exp-001（MMLU-only）的方差分量预测 exp-002 中其他 benchmark 的 G 是更有意义的外部验证。但正如 Table 3 显示的 MC vs. FF 方差结构差异，跨 benchmark 的方差分量可迁移性本身是一个 open question。如果预测误差大，它揭示的恰好是 format-associated pattern 的影响；如果预测误差小，则强化了 D-study budgets 的泛化性。无论结果如何都有信息价值，建议作者补充。\n\n### R1-Q2: Variance components 的 MAPE\n\n同意这比 rank correlation 更有价值。ρ = 0.732 只说明相对排序的保持程度，但 D-study budget 的具体数字（如 \"178 items\"）依赖于方差分量的 **绝对值准确性**。报告 MAPE 或 mean absolute bias by component 会显著增强 Section 3.5 和 Appendix A 的论证力度。\n\n### R1-Q3: Partial-credit validation 是否仅限 GSM8K\n\n根据 Section 4.4 的描述，partial-credit 分析基于 \"text-exact-match scoring\" 场景（将 binary correctness 替换为 partial credit）。论文提到 \"under text-exact-match, a precision×temperature interaction emerges at 1.3%\"，但未明确说明是哪个 benchmark。如果仅限 GSM8K，则 partial-credit 结论的泛化性进一步受限。建议作者澄清。\n\n### R1-Q4: MATH 的 LOMO CV\n\nTable 5 显示 MATH 的 CV 在各 benchmark 中最高。高 CV 表明 model facet 对 MATH 的方差分解影响最大——移除某个模型会较显著地改变 G 估计。这与 MATH 作为高难度 benchmark（mean accuracy 较低）、模型间差异更明显的特征一致。但 CV 仍低于 ~1.3%，绝对意义上不构成不稳定。\n\n### R1-Q5: 3-parameter IRT guessing parameter\n\n有趣的视角。MC benchmarks 的 guessing floor（如 4-choice 为 25%）确实会压缩 residual variance——在 p ≈ 0.25 附近的 items 可能有大量 \"guessing correct\"，这会被 binary scoring 当作 true knowledge。这与 Appendix F 中 MC benchmarks 的 item difficulty heterogeneity（较高 dispersion，0.27–0.31）是一致的。但 G-theory 框架不建模 guessing parameter——这属于 IRT 框架的优势领域。论文 Section 2 已将自身定位为与 IRT 互补而非替代，因此不建模 guessing 是方法论选择而非遗漏，但值得在 discussion 中提及。\n\n---\n\n## Missing References 回应\n\n**[REBUT] Brennan (2001, Ch. 12)**：论文已在 Appendix A 中明确引用——\"Henderson Method I produces unbiased estimates for balanced designs regardless of outcome distribution (Brennan, 2001, Ch. 12)\"。R1 可能在阅读 Appendix 时遗漏了这一引用。\n\n**[AGREE] Oren et al. (2024)**：鉴于 R1-W5 关于 contamination 的讨论，引用 contamination detection 方法论的文献是合理的补充。\n\n---\n\n## 与 Reviewer 1 的共识与分歧总结\n\n| R1 Issue | R2 判断 | 备注 |\n|----------|--------|------|\n| W1 Henderson binary | **部分 REBUT** | Henderson Method I 分布无关性已论证；但 bias 报告不完整 |\n| W2 In-sample validation | **AGREE** | Table 8 应重标为 \"consistency check\" |\n| W3 Qwen2.5 only | **AGREE** | Within-family ≠ cross-family |\n| W4 Partial-credit | **AGREE** | 与我的 W2 呼应 |\n| W5 Contamination | **AGREE**（部分） | budget ratio 论点有一定说服力 |\n| W6 Format pattern weight | **AGREE** | 与我的 W3 一致 |\n| W7 C2 overclaiming | **AGREE** | 与我的 W2 一致 |\n| W8 Bootstrap CI scope | **AGREE** | CIs 条件于这 8 个模型 |\n| W9 3.1× framing | **AGREE** | 与我的 W1 一致 |\n\n**两位 Reviewer 的核心共识**：(1) \"3.1× item reduction\" framing 需要 rebalance；(2) C2 应降级；(3) format-associated pattern 统计效力不足但叙事权重过大；(4) partial-credit limitation 讨论不充分。\n\n**R1 独有的有价值贡献**：W1 关于 probit simulation bias 报告覆盖不完整（虽然方法论前提不准确，但实质诉求有效）；W2 关于 \"forward prediction\" 标签不准确；W5 关于 contamination 的具体分析；W8 关于 CI 仅反映 item-sampling variability。\n\n**我独有的补充视角**：Abstract 数字密度问题（我的 W5）；Conclusion practical implications 不足（我的 W6）；model main effect 2.8% 对 D-study budget 泛化性的影响（我的 W7）；Anonymous 自引的匿名性风险（我的 W8）。\n",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### [REBUT] R1-W1: Henderson Method I 在 binary 数据上的适用性\n\nR1 称 \"Henderson Method I 假设连续正态数据\"——这一前提不准确。论文 Appendix A 明确引用 Brennan (2001, Ch. 12) 指出 **\"Henderson Method I produces unbiased estimates for balanced designs regardless of outcome distribution\"**。Henderson Method I 是基于均方的 ANOVA 估计器，对平衡设计的点估计不依赖分布假设，这是 G-theory 文献的标准结论。\n\n**但我同意 R1 关于报告完整性的诉求**。probit simulation 的 Spearman ρ = 0.732 确实仅为中等相关，论文对此的解读偏乐观（称之为 \"robustness\"）。更重要的是，|bias| = 0.28–0.37 仅报告了 p ∈ [0.5, 0.8] 的 difficulty stratum，缺少极端 difficulty（p < 0.3 或 p > 0.9）的完整 bias/RMSE 分解。鉴于 MATH benchmark 的 mean accuracy 较低，extreme difficulty items 正是最需要 bias 报告的区间。\n\n**总结**：Henderson Method I 的分布无关性已在 Appendix A 论证（R1 可能未注意到），但 bias 报告的覆盖范围确实不完整。建议作者补充 full difficulty quintile 的 bias/RMSE 分解。Severity 应为 Should-Fix 而非影响核心方法论有效性的根本问题。\n\n---\n\n### [AGREE] R1-W2: Forward prediction 为 in-sample 验证\n\nR1 正确指出 Table 8 的 4-model subset（DeepSeek, Llama, Mistral, Qwen3）与 8-model 全集共享相同的 items、prompts、seeds 和 orderings。从子集方差分量预测全集 G 本质上是 **internal consistency check**，而非 out-of-sample prediction。Error 范围 0.96–6.88% 因此可能低估真实预测误差。\n\nLOMO（Table 5）虽然更接近 held-out 验证，但 leave-one-model-out 仍保留了 7/8 的模型重叠，不构成 truly independent validation。\n\nR1 建议 \"用 non-overlapping model pairs 做 split-half cross-validation\" 是合理的，但需注意只有 8 models 的情况下 split-half 仅有 4 vs. 4，方差估计会非常不稳定。更有价值的验证可能是 **用 exp-001 的方差分量预测 exp-002 中新 benchmark 的 G**（R1-Q1），但这需要假设方差结构跨 benchmark 稳定，而 Table 3 的 MC vs. FF 差异恰好质疑了这一假设。\n\n**建议**：论文应将 Table 8 重新标注为 \"internal consistency check\" 而非 \"forward prediction validation\"。\n\n---\n\n### [AGREE] R1-W3: Scale validation 局限于 Qwen2.5\n\n完全同意。Within-family validation（Qwen2.5 3B/7B/72B）共享 training recipe、tokenizer 和数据混合策略，item difficulty profile 高度相关。Section 4.6 的 claim \"preliminary evidence that budgets generalize beyond the 7–9B range\" 超出了证据支撑范围——准确表述应为 \"within Qwen2.5 family, variance structure is scale-invariant\"。\n\n补充观点：即使 Llama-3.1 8B→70B 的数据可用（如 R1 建议），仍然只是两个家族的 within-family 证据。真正的 cross-family scale validation 需要 3+ 架构家族 × 2+ scales 的交叉设计，这在当前资源下可能不可行但应在 Limitations 中明确说明。\n\n---\n\n### [AGREE] R1-W4: Partial-credit scoring 影响讨论不足\n\n同意。这是我自己审稿中也标记的问题（我的 W2 从不同角度涉及此点）。关键数据：binary → partial-credit 使 G 从 0.76 降至 0.55（Appendix A），且 ρ = 0.26 表明方差分量的相对排序也发生了根本性变化。这意味着 **所有 D-study budgets、format-associated patterns、以及 precision separability 结论都严格绑定于 binary correctness scoring**。\n\nSection 5 仅一句 \"partial credit analysis confirms that finer-grained rubrics require independent calibration (§3.5)\" 明显不足。当前 LLM 评估越来越多使用 LLM-as-judge、rubric-based scoring 和部分评分，这一限制的实际影响远大于论文当前呈现的权重。\n\n**建议**：在 Section 5 或 Limitations 中用 2-3 句明确所有 budgets 仅对 binary correctness 有效，并讨论 partial-credit 场景下的预期偏移方向。\n\n---\n\n### [AGREE] R1-W5: Contamination 作为 model×item interaction 混淆变量\n\n部分同意。R1 的核心论点成立：model×item interaction 高达 25–36%，而 differential contamination（不同模型在训练时接触了不同的 benchmark items）是这一分量的可信 confound。论文的间接证据（\"三个独立 MC benchmarks 方差结构一致\"）是必要但不充分的——**一致的 contamination 模式也能产生一致的方差结构**。\n\n但我认为论文 Section 6 中的一个论点值得更多关注：**\"Contamination affects absolute budget estimates but has limited impact on the multi-facet vs. single-condition budget ratio, since both designs are equally exposed to contaminated items.\"** 这个论点在逻辑上成立——如果 contamination 等比例地 inflate 了所有设计的 model×item interaction，则设计之间的相对效率比较不受影响。这一论点应在正文而非 Limitations 中更突出地呈现。\n\nR1 建议引用 Oren et al. (2024) 关于 contamination detection 的工作是合理的，但 contamination detection 方法在 open-weight 7–9B models 上的可靠性本身也有争议。\n\n---\n\n### [AGREE] R1-W6: Format-associated pattern 叙事权重过大\n\n完全同意，这与我的 W3 判断一致。n=5, permutation p=0.10 的分析占据约大半页篇幅并被隐含提升为核心发现之一，与其统计效力严重不匹配。\n\n补充我的 W3 中的一个额外论点：论文报告的 cross-benchmark Spearman ρ = 0.90 (p = 0.006, n = 10) 实际上是 **within-MMLU 的 10 subjects 分析**，而非独立的 cross-benchmark 证据。论文在呈现时混合了这两个层级的证据，可能让读者误以为有更强的跨 benchmark 支撑。\n\n---\n\n### [AGREE] R1-W7: C2 本质为 null result\n\n完全同意，与我的 W2 判断完全一致。BF16/FP16 在 binary scoring 下 <0.1% interaction 是 binary quantization 的必然结果，不构成 surprising finding。将其与 C1（D-study budgets）并列为独立 contribution 存在 overclaiming。\n\n---\n\n### [AGREE] R1-W8: Bootstrap CI 仅反映 item-sampling variability\n\n同意。8 models 是 purposively selected（非随机抽样），item-level bootstrap 无法捕获 \"换一组模型\" 的 uncertainty。论文应明确：**CIs 反映的是 item-sampling variability 条件于这 8 个特定模型的选择**，而非对更广泛模型总体的推断。\n\n这一点与 W3（model main effect 仅 2.8%）和 W7（model sample 同质性）形成呼应——如果模型样本本身不具代表性，那么条件于该样本的 CIs 的外部有效性更需质疑。\n\n---\n\n### [AGREE] R1-W9: \"3.1× item reduction\" framing\n\n完全同意，与我的 W1（Must-Fix）判断一致。Abstract 和 Introduction 应同时呈现 item reduction (3.1×) 和 total evaluation increase (~2.9×)。这是一篇关于 \"budget\" 的论文——只报告 budget 的一个维度是系统性误导。\n\n---\n\n## Questions 回应\n\n### R1-Q1: Truly held-out 验证\n\n好问题。用 exp-001（MMLU-only）的方差分量预测 exp-002 中其他 benchmark 的 G 是更有意义的外部验证。但正如 Table 3 显示的 MC vs. FF 方差结构差异，跨 benchmark 的方差分量可迁移性本身是一个 open question。如果预测误差大，它揭示的恰好是 format-associated pattern 的影响；如果预测误差小，则强化了 D-study budgets 的泛化性。无论结果如何都有信息价值，建议作者补充。\n\n### R1-Q2: Variance components 的 MAPE\n\n同意这比 rank correlation 更有价值。ρ = 0.732 只说明相对排序的保持程度，但 D-study budget 的具体数字（如 \"178 items\"）依赖于方差分量的 **绝对值准确性**。报告 MAPE 或 mean absolute bias by component 会显著增强 Section 3.5 和 Appendix A 的论证力度。\n\n### R1-Q3: Partial-credit validation 是否仅限 GSM8K\n\n根据 Section 4.4 的描述，partial-credit 分析基于 \"text-exact-match scoring\" 场景（将 binary correctness 替换为 partial credit）。论文提到 \"under text-exact-match, a precision×temperature interaction emerges at 1.3%\"，但未明确说明是哪个 benchmark。如果仅限 GSM8K，则 partial-credit 结论的泛化性进一步受限。建议作者澄清。\n\n### R1-Q4: MATH 的 LOMO CV\n\nTable 5 显示 MATH 的 CV 在各 benchmark 中最高。高 CV 表明 model facet 对 MATH 的方差分解影响最大——移除某个模型会较显著地改变 G 估计。这与 MATH 作为高难度 benchmark（mean accuracy 较低）、模型间差异更明显的特征一致。但 CV 仍低于 ~1.3%，绝对意义上不构成不稳定。\n\n### R1-Q5: 3-parameter IRT guessing parameter\n\n有趣的视角。MC benchmarks 的 guessing floor（如 4-choice 为 25%）确实会压缩 residual variance——在 p ≈ 0.25 附近的 items 可能有大量 \"guessing correct\"，这会被 binary scoring 当作 true knowledge。这与 Appendix F 中 MC benchmarks 的 item difficulty heterogeneity（较高 dispersion，0.27–0.31）是一致的。但 G-theory 框架不建模 guessing parameter——这属于 IRT 框架的优势领域。论文 Section 2 已将自身定位为与 IRT 互补而非替代，因此不建模 guessing 是方法论选择而非遗漏，但值得在 discussion 中提及。\n\n---\n\n## Missing References 回应\n\n**[REBUT] Brennan (2001, Ch. 12)**：论文已在 Appendix A 中明确引用——\"Henderson Method I produces unbiased estimates for balanced designs regardless of outcome distribution (Brennan, 2001, Ch. 12)\"。R1 可能在阅读 Appendix 时遗漏了这一引用。\n\n**[AGREE] Oren et al. (2024)**：鉴于 R1-W5 关于 contamination 的讨论，引用 contamination detection 方法论的文献是合理的补充。\n\n---\n\n## 与 Reviewer 1 的共识与分歧总结\n\n| R1 Issue | R2 判断 | 备注 |\n|----------|--------|------|\n| W1 Henderson binary | **部分 REBUT** | Henderson Method I 分布无关性已论证；但 bias 报告不完整 |\n| W2 In-sample validation | **AGREE** | Table 8 应重标为 \"consistency check\" |\n| W3 Qwen2.5 only | **AGREE** | Within-family ≠ cross-family |\n| W4 Partial-credit | **AGREE** | 与我的 W2 呼应 |\n| W5 Contamination | **AGREE**（部分） | budget ratio 论点有一定说服力 |\n| W6 Format pattern weight | **AGREE** | 与我的 W3 一致 |\n| W7 C2 overclaiming | **AGREE** | 与我的 W2 一致 |\n| W8 Bootstrap CI scope | **AGREE** | CIs 条件于这 8 个模型 |\n| W9 3.1× framing | **AGREE** | 与我的 W1 一致 |\n\n**两位 Reviewer 的核心共识**：(1) \"3.1× item reduction\" framing 需要 rebalance；(2) C2 应降级；(3) format-associated pattern 统计效力不足但叙事权重过大；(4) partial-credit limitation 讨论不充分。\n\n**R1 独有的有价值贡献**：W1 关于 probit simulation bias 报告覆盖不完整（虽然方法论前提不准确，但实质诉求有效）；W2 关于 \"forward prediction\" 标签不准确；W5 关于 contamination 的具体分析；W8 关于 CI 仅反映 item-sampling variability。\n\n**我独有的补充视角**：Abstract 数字密度问题（我的 W5）；Conclusion practical implications 不足（我的 W6）；model main effect 2.8% 对 D-study budget 泛化性的影响（我的 W7）；Anonymous 自引的匿名性风险（我的 W8）。\n",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 715 · 2026-05-23T01:18:04.260510+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3870
}
```

</details>

---


### Tool call

_source line 716 · 2026-05-23T01:18:09.386572+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 717 · 2026-05-23T01:18:09.386908+00:00_

{"result":"{\"success\": true, \"data\": {\"deleted\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_8/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 0
}
```

</details>

---


### Assistant

_source line 718 · 2026-05-23T01:18:14.595910+00:00_

交叉回应已提交。对 Reviewer 1 的 9 个 Weaknesses 逐条回应：1 个部分 REBUT（W1：Henderson Method I 的分布无关性已在 Appendix A 论证，但 bias 报告确实不完整），其余 8 个 AGREE。两位 Reviewer 在四个核心问题上形成共识：3.1× framing 误导、C2 应降级、format pattern 统计效力不足、partial-credit limitation 讨论不充分。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 19

## Round 19

66 recorded events


### User

_source line 719 · 2026-05-23T02:29:34.913252+00:00_

[Round 1 审稿请求]:
你是 Reviewer 2，负责 **新颖性与完整性** 审查。

## 论文信息
- **标题**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7–9B Instruction-Tuned Models
- **Venue**: EMNLP 2026 (via ARR)
- **截止日期**: 2026-05-25
- **格式**: ACL 模板，long paper，正文 8 页限制，参考文献不限，double-blind
- **论文路径**: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
- **PDF**: /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf

## 你的审查侧重

重点审查以下方面：

1. **增量贡献**：相对于 Messing et al. (2026) TEE framework 的增量贡献是否充分？三个扩展方向（infrastructure facets, cross-benchmark, D-study budgets）是否构成独立的 methodological advance 还是仅为 scale-up？
2. **Novelty 评估**：G-theory 是心理测量学成熟框架，将其应用于 LLM evaluation 的 novelty 在哪里？D-study projection 是否仅为教科书操作？
3. **Framing 与 claim 强度**：Abstract/Introduction 的 claim 是否与实验证据匹配？特别关注 (a) '3.1× item reduction' 是否隐藏了 total evaluation 增长; (b) format-associated pattern (n=5, p=0.10) 是否 overclaimed; (c) precision separability 作为独立贡献是否 trivial
4. **Related Work 覆盖**：IRT 文献（TinyBenchmarks, PSN-IRT）、evaluation frameworks (HELM, DynaBench)、variance decomposition 文献是否完整？是否有重要遗漏？
5. **写作质量**：Abstract 数字密度是否过高？Conclusion 是否充分讨论 practical implications？整体叙事流畅性和读者友好性
6. **Contribution 结构**：两个 contributions 的层级关系是否清晰？C2 (format-associated) 降级为 exploratory 是否恰当？
7. **格式合规**：8 页限制、匿名性、引用格式

请给出完整的 Strengths、Weaknesses (Must-Fix / Should-Fix / Minor)、Questions，以及 Overall Assessment 评分（按 EMNLP 2026 ARR 标准：5=Award, 4=Conference, 3=Findings, 2=Resubmit, 1=Do not resubmit）。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 720 · 2026-05-23T02:29:41.969986+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:WebSearch,WebFetch,mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 721 · 2026-05-23T02:29:41.970312+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 722 · 2026-05-23T02:29:46.941766+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 723 · 2026-05-23T02:29:49.301570+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-10",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-10",
    "dpi": "150"
  }
}
```

</details>

---


### Tool call

_source line 724 · 2026-05-23T02:29:50.155290+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 725 · 2026-05-23T02:29:53.973809+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"ACL Rolling Review | ACL Member Portal","url":"https://www.aclweb.org/portal/content/acl-rolling-review"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"aclrollingreview/reviewing.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/reviewing.md"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"}]

I found information about ACL ARR 2026 reviewer guidelines, review form, and criteria. Here are the key findings:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility. Conference recommendations may also consider novelty, impact and other factors.

The review 
…[truncated 1278 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 7032
}
```

</details>

---


### Tool result

_source line 726 · 2026-05-23T02:29:55.533322+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 467.2}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 505.0}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 576.8}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 538.9}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 488.7}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.3}, {\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 502.4}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 501.7}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 561.3}, {\"page\":
…[truncated 438 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 6231
}
```

</details>

---


### Tool result

_source line 727 · 2026-05-23T02:29:55.533725+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	
11	\usepackage{graphicx}
12	\usepackage{amsmath,amssymb}
13	\usepackage{booktabs}
14	\usepackage{multirow}
15	\usepackage{xcolor}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\input{conclusion}
44	
45	% === LIMITATIONS ===
46	\input{limitations}
47	
48	\bibliography{references}
49	
50	% === APPENDIX ===
51	\input{appendix}
52	
53	\end{document}
54	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 5378
}
```

</details>

---


### Tool call

_source line 728 · 2026-05-23T02:30:02.155689+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form: all scoring dimensions, their scales, and descriptions. Include Overall Assessment scale, Soundness, Excitement/Novelty, Reproducibility, and any other dimensions."
  }
}
```

</details>

---


### Tool call

_source line 729 · 2026-05-23T02:30:03.159467+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 730 · 2026-05-23T02:30:03.510679+00:00_

1	Large Language Model (LLM) evaluation results vary across reproductions, but variance sources interact, and their relative importance shifts with the benchmark format. We apply Generalizability theory (G-theory) in a fully crossed design with up to seven facets across eight open-weight instruction-tuned models (7--9B parameters) and five benchmarks, totaling approximately 2.3 million evaluation records. D-study projections show that a recommended multi-condition design achieves $G \geq 0.80$ with 178 items (1,602 evaluations per model), a 3.1$\times$ item reduction over single-condition designs (552 items, 552 evaluations)---trading approximately 3$\times$ more evaluations per item for 3$\times$ fewer items, a tradeoff that favors multi-condition designs when item construction is costly. Model$\times$item interaction (up to 36\%) indicates that models differ primarily in which items they find difficult, not in overall ability. Preliminary validation across a 3B--72B parameter range confirms stable variance structure within one architecture family. We release an open-source G-theory pipeline and D-study budget calculator for evaluation design optimization.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 731 · 2026-05-23T02:30:03.661408+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 732 · 2026-05-23T02:30:04.012578+00:00_

1	\section{Introduction}
2	\label{sec:introduction}
3	
4	In our analysis of five benchmarks, item selection drives 34--38\% of evaluation variance on multiple-choice tasks while prompt wording is negligible ($<$3\%). On the free-form reasoning task GSM8K, the structure shifts: model$\times$prompt interaction alone accounts for approximately 9\%, while item selection drops to 17\%. These numbers, drawn from a factorial analysis of approximately 2.3 million evaluation records, reveal that the variance structure of LLM evaluation is not a fixed property of the pipeline but shifts qualitatively with the response format. Current evaluation practice treats variance sources as independent nuisance factors and controls them one at a time: one study perturbs prompts, another varies precision, a third changes item subsets. This piecemeal approach cannot capture interactions between sources, nor can it predict how the relative importance of each source changes across evaluation settings. Leaderboard rankings built on single-condition evaluations are therefore sensitive to methodological choices that remain unreported and uncontrolled \citep{rodriguez2021leaderboards, dehghani2021benchmark}. No study has simultaneously crossed infrastructure and methodology facets in a unified factorial design across benchmarks to decompose these sources, quantify their interactions, and compare the resulting variance structure.
5	
6	Existing studies examine individual variance sources in isolation. \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} documented 50--76\% accuracy swings from prompt formatting; \citet{yuan2025layercast} showed up to 9\% variation from numerical precision; \citet{pezeshkpour2024ordering}, \citet{dodge2020finetuning}, and \citet{henderson2018deep} documented ordering and hyperparameter sensitivity---each holding other factors fixed. \citet{messing2026hidden} applied G-theory to LLM evaluation across five methodology facets on a single benchmark (j
…[truncated 2725 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 733 · 2026-05-23T02:30:04.012939+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 734 · 2026-05-23T02:30:04.464257+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Decomposition in ML/NLP Evaluation.}
5	Factorial decomposition of evaluation variance has roots in the ML reproducibility literature. \citet{bouthillier2021accounting} introduced an ANOVA-based template that decomposes benchmark variance across implementation details, hyperparameters, and data splits, establishing that design choices account for a substantial share of reproducibility failures. Subsequent studies applied similar decomposition to specific evaluation facets \citep{dodge2020finetuning, henderson2018deep, magnusson2023reproducibility}. \citet{messing2026hidden} brought Generalizability theory into LLM evaluation, decomposing variance across five methodology facets on a single benchmark (judge identity: 43.8\%; see Positioning below for detailed comparison). \citet{madaan2024quantifying} proposed per-factor variance metrics for LLM evaluation benchmarks but did not cross factors simultaneously. Holistic evaluation frameworks \citep{liang2023helm, kiela2021dynabench} standardize multi-scenario comparison but do not decompose variance sources. \citet{blackwell2024towards} quantified uncertainty in benchmark scores, and \citet{qian2026benchmark} conducted systematic meta-evaluation of LLM benchmarks; \citet{burnell2023rethink} called for rethinking evaluation reporting standards; \citet{saxon2024metrology} advocated model metrology as a framework for rigorous benchmark design. Recently, G-theory has been applied to LLM-based writing assessment \citep{wei2025gtheory} and annotation reliability \citep{varannot2025gtheory}, but these studies address scoring consistency rather than benchmark evaluation variance. \citet{kunievsky2025intent} proposed an alternative decomposition that separates intent uncertainty, articulation variance, and model uncertainty, but this framework does not cross infrastructure and methodology facets in a factorial design. Our work extends these approaches by cross
…[truncated 4261 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 735 · 2026-05-23T02:30:04.464674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 736 · 2026-05-23T02:30:04.968949+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. This prospective capability distinguishes G-theory from classical ANOVA: rather than only attributing varia
…[truncated 10670 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 504
}
```

</details>

---


### Tool call

_source line 737 · 2026-05-23T02:30:04.969451+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 738 · 2026-05-23T02:30:05.976509+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 739 · 2026-05-23T02:30:06.077799+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1108
}
```

</details>

---


### Tool call

_source line 740 · 2026-05-23T02:30:06.078203+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 741 · 2026-05-23T02:30:07.992339+00:00_

# ACL Rolling Review Form - Scoring Dimensions

## 1. **Reviewer Confidence**
Scale: 1-5
- 5: Positive evaluation; careful reading and familiar with related work
- 4: Quite sure; important points checked carefully
- 3: Pretty sure; general familiarity but details not carefully verified
- 2: Willing to defend evaluation; likely missed some details
- 1: Outside expertise area or paper very difficult to understand

## 2. **Soundness**
Scale: 1-5 (with .5 increments)
- 5: Excellent; one of most thorough studies of its type
- 4: Strong; sufficient support for claims
- 3: Acceptable; main claims adequately supported
- 2: Poor; main claims lack sufficient support
- 1: Major Issues; insufficiently thorough for publication

## 3. **Excitement**
Scale: 1-5 (with .5 increments)
- 5: Highly Exciting; would recommend to others
- 4: Exciting; would mention to colleagues
- 3: Interesting; might mention or attend presentation
- 2: Potentially Interesting; limited personal resonance
- 1: Not Exciting; lacks community relevance

## 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
- 5: Consider for Award (top 2.5%)
- 4: Conference acceptance
- 3: Findings acceptance
- 2: Substantial revisions needed
- 1: Do not resubmit or not relevant

## 5. **Reproducibility**
Scale: 1-5
- 5: Results easily reproducible
- 4: Mostly reproducible with minor variations
- 3: Reproducible with difficulty
- 2: Hard to reproduce; data unavailable
- 1: Cannot reproduce

## 6. **Datasets & Software**
Scale: 1-5 each
- 5: Enabling; affects research choices
- 4: Useful; recommended for ongoing work
- 3: Potentially useful
- 2: Documentary value only
- 1: No usable materials

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 5836
}
```

</details>

---


### Tool result

_source line 742 · 2026-05-23T02:30:07.993895+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2017
}
```

</details>

---


### Tool result

_source line 743 · 2026-05-23T02:30:08.345976+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2267
}
```

</details>

---


### Tool call

_source line 744 · 2026-05-23T02:30:12.777724+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 745 · 2026-05-23T02:30:13.129683+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	
7	We first establish the variance structure within a single model (Llama-3.1-8B-Instruct) on MMLU to isolate methodological facet contributions before introducing cross-model variation.
8	
9	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
10	
11	\paragraph{Results.} Under binary scoring, item difficulty (\texttt{item\_id}) accounts for 58.4\% of total variance, with the residual term contributing 23.1\%. All main facet effects are negligible ($<$1\% each): precision 0.9\%, prompt template, temperature, seed, and ordering each $<$0.5\%. The interesting structure appears in item-conditional interactions: prompt$\times$item is the largest at 5.5\%, followed by seed$\times$item (4.7\%), precision$\times$item (3.3\%), temperature$\times$item (2.9\%), and ordering$\times$item (0.8\%). This pattern indicates that methodological choices do not shift performance uniformly across items; instead, specific items are differentially sensitive to specific facets---prompt template variation produces the largest item-conditional effect.
12	
13	The resulting generalizability coefficient is $G_\text{item} = 0.936$, indicating that 200 items under multi-facet conditions produce highly reliable rankings. A D-study projection shows $G \geq 0.80$ is achievable with as few as 55 items in this multi-facet design.
14	
15	For text-exact-match scoring (requiring verbatim string matches), the variance structure shifts dramatically: te
…[truncated 11477 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 351
}
```

</details>

---


### Tool call

_source line 746 · 2026-05-23T02:30:13.130119+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 747 · 2026-05-23T02:30:13.632208+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	A recommended 3-prompt $\times$ 3-seed design reduces item requirements from 552 to 178 for $G \geq 0.80$, confirmed across five benchmarks under binary scoring. Multi-facet designs minimize item count when item construction is costly; single-condition designs with more items suit compute-constrained settings. All budgets assume binary scoring; finer-grained rubrics require independent calibration (\S\ref{sec:binary}). Suggestive format-associated differences warrant larger benchmark samples; extending to other model scales and continuous metrics is a priority. Code, data, and a D-study calculator will be released upon publication.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 748 · 2026-05-23T02:30:13.632589+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 749 · 2026-05-23T02:30:14.135676+00:00_

1	\section{Limitations}
2	\label{sec:limitations}
3	
4	Our eight models share the 2024--2025 instruction-tuning paradigm; temporal correlation may limit exchangeability, and results do not generalize to API-based or base models. Preliminary within-family 72B validation (\S4.6) suggests stable variance structure across scales, but is limited to a single architecture (Qwen2.5); the Qwen2.5 family shares training recipes and tokenizer, so validating with architecturally distinct families (e.g., Llama-3 70B, Mistral-Large) is necessary before extrapolating budget recommendations to arbitrary model families. The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$); other formats (code generation, multi-turn dialogue) may differ. All D-study budgets reported in this paper are strictly valid only under binary correctness scoring. Our partial-credit pilot (GSM8K only, single model) shows $G$ drops from 0.76 to 0.55 with $\rho = 0.26$ for item rankings, indicating budgets do not transfer to finer-grained scoring rubrics; the partial-credit analysis is limited to a single benchmark and single model, and its generalizability is unknown. Our design varies few-shot example ordering but not example identity, a known variance source. All eight models may have encountered benchmark items during pre-training; differential contamination across architectures could inflate model$\times$item interaction \citep{golchin2023contamination, oren2024proving}, though consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver. Contamination affects absolute budget estimates but has limited impact on the multi-facet vs.\ single-condition budget \emph{ratio}, since both designs are equally exposed to contaminated items.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 503
}
```

</details>

---


### Tool call

_source line 750 · 2026-05-23T02:30:14.139324+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 751 · 2026-05-23T02:30:15.544596+00:00_

1	\appendix
2	\section{Additional Robustness Analyses}
3	\label{app:robustness}
4	
5	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
6	
7	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
8	
9	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
10	
11	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
12	
13	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. This an
…[truncated 22080 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool call

_source line 752 · 2026-05-23T02:30:15.695479+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 753 · 2026-05-23T02:30:16.099332+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 754 · 2026-05-23T02:30:16.556230+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 860
}
```

</details>

---


### Tool call

_source line 755 · 2026-05-23T02:30:16.556682+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool call

_source line 756 · 2026-05-23T02:30:17.313955+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 757 · 2026-05-23T02:30:17.719490+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1620
}
```

</details>

---


### Tool result

_source line 758 · 2026-05-23T02:30:19.181225+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2624
}
```

</details>

---


### Tool result

_source line 759 · 2026-05-23T02:30:20.038061+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2724
}
```

</details>

---


### Tool call

_source line 760 · 2026-05-23T02:30:25.461316+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 761 · 2026-05-23T02:30:26.013674+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 762 · 2026-05-23T02:30:26.065026+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 603
}
```

</details>

---


### Tool call

_source line 763 · 2026-05-23T02:30:26.467568+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool result

_source line 764 · 2026-05-23T02:30:27.021580+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1007
}
```

</details>

---


### Tool call

_source line 765 · 2026-05-23T02:30:27.021986+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/references.bib"
  }
}
```

</details>

---


### Tool result

_source line 766 · 2026-05-23T02:30:27.122857+00:00_

1	% references.bib — auto-generated from literature_map.yaml (29 cited papers)
2	% Last synced: 2026-05-21
3	
4	% ====== G-Theory & Evaluation Variance ======
5	
6	@article{messing2026hidden,
7	  title={Hidden Measurement Error in {LLM} Pipelines Distorts Annotation, Evaluation, and Benchmarking},
8	  author={Messing, Solomon},
9	  year={2026},
10	  journal={arXiv preprint arXiv:2604.11581},
11	  url={https://arxiv.org/abs/2604.11581}
12	}
13	
14	@article{wei2025gtheory,
15	  title={Exploring {LLM} Autoscoring Reliability in Large-Scale Writing Assessments Using Generalizability Theory},
16	  author={Song, Dan and Lee, Won-Chan and Jiao, Hong},
17	  year={2025},
18	  journal={arXiv preprint arXiv:2507.19980},
19	  url={https://arxiv.org/abs/2507.19980}
20	}
21	
22	@article{madaan2024quantifying,
23	  title={Quantifying Variance in Evaluation Benchmarks},
24	  author={Madaan, Lovish and Bhatia, Samarth and Tulio Ribeiro, Marco and Roth, Dan},
25	  year={2024},
26	  journal={arXiv preprint arXiv:2406.10229},
27	  url={https://arxiv.org/abs/2406.10229}
28	}
29	
30	@inproceedings{bouthillier2021accounting,
31	  title={Accounting for Variance in Machine Learning Benchmarks},
32	  author={Bouthillier, Xavier and Delaunay, Pierre and Bronzi, Mirko and Trofimov, Assya and Nichyporuk, Brennan and Szeto, Justin and Sepahvand, Nazanin Mohammadi and Raff, Edward and Madan, Kshitij and Voleti, Vikram and Kahou, Samira Ebrahimi and Michalski, Vincent and Arbel, Tal and Pal, Chris and Varoquaux, Ga{\"e}l and Vincent, Pascal},
33	  booktitle={Proceedings of Machine Learning and Systems (MLSys)},
34	  year={2021},
35	  url={https://arxiv.org/abs/2103.03098}
36	}
37	
38	@book{shavelson1991generalizability,
39	  title={Generalizability Theory: A Primer},
40	  author={Shavelson, Richard J. and Webb, Noreen M.},
41	  year={1991},
42	  publisher={SAGE Publications},
43	  isbn={978-0-8039-3744-4}
44	}
45	
46	@book{brennan2001generalizability,
47	  title={Generalizability Theory},
48	  aut
…[truncated 21710 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool result

_source line 767 · 2026-05-23T02:30:27.123758+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 656
}
```

</details>

---


### Tool call

_source line 768 · 2026-05-23T02:30:33.957552+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "11-16",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "11-16",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 769 · 2026-05-23T02:30:34.560180+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 580.8}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 546.0}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 469.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 423.1}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 418.2}, {\"page\": 16, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p16.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 118.1}], \"total_pages\": 16, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 602
}
```

</details>

---


### Tool call

_source line 770 · 2026-05-23T02:30:38.007019+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 771 · 2026-05-23T02:30:38.810226+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 803
}
```

</details>

---


### Tool call

_source line 772 · 2026-05-23T02:30:38.961190+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool call

_source line 773 · 2026-05-23T02:30:39.312703+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 774 · 2026-05-23T02:30:39.766338+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 805
}
```

</details>

---


### Tool call

_source line 775 · 2026-05-23T02:30:39.766762+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool result

_source line 776 · 2026-05-23T02:30:40.271373+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 958
}
```

</details>

---


### Tool call

_source line 777 · 2026-05-23T02:30:40.271797+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 778 · 2026-05-23T02:30:40.824149+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1057
}
```

</details>

---


### Tool call

_source line 779 · 2026-05-23T02:30:40.824562+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p16.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_9/_pdf_images/submitted_p16.png"
  }
}
```

</details>

---


### Tool result

_source line 780 · 2026-05-23T02:30:40.926968+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 102
}
```

</details>

---


### Tool result

_source line 781 · 2026-05-23T02:30:41.028039+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 756
}
```

</details>

---


### Tool call

_source line 782 · 2026-05-23T02:34:29.941789+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 — 新颖性与完整性审查\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 一篇执行严谨、鲁棒性分析充分的大规模实证研究，D-study 预算工具具有实际价值；但核心方法论为教科书级 G-theory 操作在新数据上的应用，相对于 Messing (2026) TEE 的增量创新有限，format-associated finding 统计力度不足以支撑独立贡献。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨（全交叉因子、Henderson Method I + bootstrap CI）；9 项鲁棒性分析覆盖估计器、二值数据假设、模型留一法等；binary scoring conditionality 透明披露且有 partial-credit pilot 验证。主要扣分：quasi-random model facet 假设在 8 个同代模型上的可迁移性有限 |\n| Excitement | 3/5 | G-theory 是成熟框架，应用于 LLM 评估的开创性已被 Messing (2026) 占据；本文的三个扩展方向（infrastructure facets, cross-benchmark, D-study budgets）是 solid incremental work 但非 paradigm shift；D-study budget 作为实用工具有价值但概念上是 textbook G-theory 的标准操作 |\n| Reproducibility | 4/5 | 模型全部开源可获取，实验设计（facet levels、prompt templates）在正文+附录完整公开；承诺发布 G-theory pipeline 和 D-study calculator；扣分：200 items 的具体采样过程（seed 42、10/57 subjects）需发布 item list 才能完全复现 |\n| Overall | 3.5/5 | 高质量的实证工作，适合 Findings；Conference 接收需要更强的方法论创新或更具结论性的 format-associated finding |\n\n**Reviewer Confidence**: 4/5（熟悉 G-theory、IRT 和 LLM evaluation 文献）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 相对于 Messing (2026) TEE 的增量贡献定位不够清晰——方法论创新 vs. scale-up 界限模糊\n\n- 具体位置：Section 1 (Introduction, Contributions), Section 2 (Positioning paragraph)\n- 问题：论文在 Positioning paragraph（Section 2 末尾）列出三个扩展方向：(i) infrastructure facets 替代 judge identity, (ii) cross-benchmark comparison, (iii) D-study budgets。但这三个方向在方法论层面的创新程度不同，论文未加区分：\n  - 扩展 (i) 本质上是将 G-theory 应用于不同的 facet 集合（precision, seed, ordering 替代 judge identity），facet 选择不同≠方法论不同\n  - 扩展 (ii) 是实验规模的增加（1 benchmark → 5 benchmarks），是 scale-up 而非新方法\n  - 扩展 (iii) D-study projection 是 G-theory 的标准操作（Brennan 2001, Ch. 4），教科书级别\n  \n  唯一接近方法论创新的是：将 IRT item selection 和 G-theory protocol optimization 证明为正交互补（Table 4，IRT 116 items 在 single-condition 下 G=0.457 vs. multi-facet 下 G=0.895）。但这个发现被埋在 §4.5 的一个段落中，未在 Contributions 中突出。\n- 为什么影响接收：如果三个扩展都是 scale-up，论文的 novelty 不足以支撑 Conference 级别；如果 IRT+G-theory 互补性是独立贡献，需要在 Contributions 中明确提升\n- 建议修改方向：(a) 在 Contributions 中将 IRT+G-theory 互补性分析提升为独立贡献点或明确标注为 C1 的关键子结论；(b) 在 Positioning 段落中对三个扩展方向分别标注方法论层级（methodological extension vs. empirical scale-up），坦诚说明哪些是新方法、哪些是已有方法的新应用\n\n**N2** [critical] Binary scoring conditionality 严重限制 D-study budget 的实际适用范围，但 title 和 abstract 的表述暗示了更广的适用性\n\n- 具体位置：Title, Abstract, §3.5, §4.1, Appendix A (Scoring metric sensitivity)\n- 问题：论文标题 \"Reproducibility Budgets for Open-Weight LLM Evaluation\" 暗示 budgets 适用于通用 LLM evaluation。但 partial-credit pilot（Appendix A）显示 binary → partial credit 后 G 从 0.76 降至 0.55、item difficulty ranking ρ=0.26（几乎无关），说明 budget 在 binary scoring 之外完全不适用。§3.5 和 §4.1 的 text-exact-match 实验更极端（G=0.936 vs. 0.007）。这意味着：\n  - 论文的核心产出（178 items, 3×3 design）仅对 binary correctness scoring 有效\n  - 实际 LLM evaluation 中很多场景使用 continuous scoring（如 MT-Bench、AlpacaEval 的 win rate、LLM-as-judge 评分），论文的 budgets 对这些场景没有指导价值\n  - Title 和 abstract 均未限定 \"under binary scoring\"\n- 为什么影响接收：如果适用范围仅限 binary scoring，论文 impact 显著缩窄；如果 title 误导读者认为 budgets 通用适用，是 framing 问题\n- 建议修改方向：(a) Title 中加入 \"under Binary Scoring\" 或 \"for Binary Benchmarks\" 限定；(b) Abstract 首句即声明 binary scoring scope；(c) Discussion 中明确列出不适用的 evaluation 场景（LLM-as-judge, continuous scoring, preference ranking）\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"3.1× item reduction\" 的 framing 掩盖了 total evaluation 增长\n\n- 具体位置：Abstract（第 3-4 句）, §1 Contribution C1, §4.5\n- 问题：Abstract 写 \"a 3.1× item reduction over single-condition designs (552 items, 552 evaluations)---trading approximately 3× more evaluations per item for 3× fewer items\"——从 552 evaluations（single-condition）增加到 1,602 evaluations（3-prompt×3-seed，178 items × 9 conditions）。虽然论文确实披露了这个 tradeoff（\"trading approximately 3× more evaluations per item\"），但 framing 优先强调 item reduction 而非 total evaluation increase 可能误导快速阅读者。特别是 Introduction 中 Contribution C1 只写 \"a 3.1× reduction over single-condition designs (552 items)\" 而未提及 total evaluations 从 552 增加到 1,602。\n- 建议：在 Contribution C1 中加入 total evaluation count 对比（552 → 1,602 total evaluations, 2.9× increase），让读者一眼看到完整 tradeoff\n\n**W2** [warning] Format-associated variance pattern (C2) 占用大量篇幅但统计支撑不足\n\n- 具体位置：§4.3 (整个 subsection, 约 1 页), Figure 3, Table 3\n- 问题：C2 的 benchmark-level 检验力极低：n=5, exhaustive permutation p=0.10（C(5,3)=10 种分法的 floor），benchmark-level CI 跨越零 [-1.7, 5.1]。论文正确标注了 \"exploratory\"，但 §4.3 占据约 1 页正文，包含对 HellaSwag 异常的详细讨论、tautology 反驳、difficulty dispersion 分析等。这些分析本身质量不错，但对于一个 p=0.10 的 exploratory observation，这个篇幅在 8 页限制下显得奢侈——相当于正文的 12.5%。这些内容可以压缩或移至附录，将正文空间给予更有结论性的 C1 分析。\n- 建议：§4.3 主文保留 1 段核心发现（MC 68-72% vs. FF 31-41%, exploratory, p=0.10），将 HellaSwag 例外讨论、tautology 反驳、difficulty dispersion 分析移至附录\n\n**W3** [warning] Conclusion 过于简短，缺乏 practical implications 讨论\n\n- 具体位置：Section 5（仅 1 段，约 5 行）\n- 问题：对于一篇提出 \"reproducibility budgets\" 的论文，Conclusion 应讨论：(a) 实际部署这些 budgets 的路径（如何集成到 lm-evaluation-harness、HELM 等现有框架）；(b) 对 benchmark 设计者的具体建议（何时选 multi-facet vs. single-condition）；(c) 对 leaderboard 运营者的影响。当前 Conclusion 仅复述了 3×3 design 的数字和 binary scoring 限制，缺乏 forward-looking discussion。\n- 建议：扩展 Conclusion 至 2-3 段，增加 practitioner-oriented 讨论\n\n**W4** [warning] Related Work 缺少对 evaluation harness 实现层面文献的讨论\n\n- 具体位置：Section 2\n- 问题：论文的 D-study budgets 直接关系到评估框架的实际设计。但 Related Work 未讨论以下实际相关的工作：\n  - EleutherAI lm-evaluation-harness（Biderman et al. 2024 被引用但仅从 seed/training sensitivity 角度，未讨论其 evaluation protocol 设计如何与本文 multi-facet 建议整合）\n  - MMLU-Redux (Gema et al. 2024) 和 MMLU-Pro (Wang et al. 2024)——这些是 MMLU 的修订版本，直接影响本文 200-item sampling 的代表性问题\n  - OpenCompass 和其他中文 evaluation 框架（如果论文声称 \"open-weight LLM evaluation\" 的通用性）\n- 建议：在 Related Work 或 Limitations 中增加 1-2 句讨论 evaluation harness 整合和 MMLU 变体\n\n**W5** [warning] Model 样本的时间同质性可能高估 model×item interaction 的稳定性\n\n- 具体位置：§3.5 (Model Facet), §6 (Limitations, 第一句)\n- 问题：8 个模型全部来自 2024-2025 训练周期，共享指令微调范式。Limitations 承认了这一点，但未充分讨论其对 variance decomposition 的具体影响。如果 2024-2025 代模型在训练数据上有高度重叠（pre-training corpus 相似），model×item interaction（30-36%）可能部分反映训练数据共性而非真正的架构差异。这与 contamination concern（§6 末尾提及）相关但不同——即使没有 benchmark contamination，相似的训练数据也会导致相似的 DIF profiles。Leave-one-model-out 分析（CV ≤ 1.25%）确认了当前 8 个模型内的稳定性，但不能外推到 2026+ 代模型。\n- 建议：在 Limitations 中增加 1-2 句明确讨论 training data overlap 与 model×item interaction 的关系，以及 budget 推荐对未来模型代的有效期\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 数字密度过高（2.3M, 178, 1602, 3.1×, 552, 36%, G≥0.80, 3B-72B 在短短 6 行内），建议精简至 3-4 个关键数字，将其余移至 Introduction\n- **M2**: Table 3 中 \"prompt\" 行在 MC 和 FF 下含义不同（MC = prompt×item interaction, FF = prompt main effect），尽管 caption 有说明，但行标签一致容易误读。建议使用不同行标签或分行\n- **M3**: Appendix 中 Table 5 (LOMO stability) 标注为 \"Table 5\" 但 main text Table 4 之后应为 Table 5。编号看起来正确，但建议验证交叉引用\n- **M4**: §4.4 (Precision Separability) 仅 2 句话，作为独立 subsection 过短。考虑合并到 §4.1 或 §4.5\n- **M5**: Figure 1 (teaser) 中 y 轴标签 \"Generalizability Coefficient\" 字体偏小，在打印版可能难以辨认\n\n---\n\n## Questions for Authors\n\n1. **IRT+G-theory 互补性**：Table 4 显示 IRT-selected 116 items 在 multi-facet 下 G=0.895。这是否意味着最优策略是先用 IRT 选 item、再用 G-theory 优化 protocol？如果是，建议在 Contribution 中明确提出这一 pipeline。\n\n2. **Partial-credit scoring 的 follow-up 优先级**：鉴于 partial-credit pilot 显示 G 大幅下降（0.76→0.55）且 item ranking 几乎无关（ρ=0.26），是否有计划扩展到 LLM-as-judge continuous scoring？这将显著扩大论文的适用范围。\n\n3. **Contamination 的定量检验**：§6 提到 \"consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver\"。是否可以对 8 个模型分别运行 contamination detection（如 Oren et al. 2024 的方法），提供直接证据？\n\n4. **72B 验证**：§4.6 的 Qwen2.5 within-family 验证显示 model×item=38.5% > item=35.7%。但仅 3 个模型（3B/7B/72B）不足以估计 G。是否有计划增加其他 architecture 的 72B 模型（如 Llama-3 70B）进行 cross-family 验证？\n\n---\n\n## 主要优势\n\n1. **实验规模与设计严谨性**：2.3M 条记录、7 facets、8 models、5 benchmarks 的全交叉因子设计在 LLM evaluation 方差分析文献中属最大规模之一。Henderson Method I + 1,000 resample bootstrap CI 的统计方法选择恰当。\n\n2. **鲁棒性分析极为充分**：9 项独立分析（GLMM complement, REML comparison, probit simulation, LOMO, null calibration, CI method comparison, facet specification sensitivity, accuracy-range stability, reduced crossing validation）覆盖了 reviewer 可能提出的几乎所有方法论质疑。这是论文最强的技术优势。\n\n3. **实用产出**：D-study budget calculator 和 intermediate design gradient（Table 9, Appendix C）为 evaluation practitioners 提供了即时可用的决策工具。特别是 \"minimal upgrade (2 prompts)\" 从 G=0.592 到 G=0.692 的 steep gain 是对社区非常有价值的实用 insight。\n\n4. **Binary scoring conditionality 的透明处理**：论文在 §3.5 首次声明、§4.1 用 text-exact-match 实验佐证、Appendix A 用 partial-credit pilot 验证、§4.3 再次提醒——对关键限制的多次、多角度披露远超同类论文水平。\n\n5. **IRT+G-theory 互补性分析**（Table 4）：证明 item selection（IRT）和 protocol optimization（G-theory）是正交的——IRT 116 items 在 single-condition 下 G=0.457 但在 multi-facet 下 G=0.895——这是一个值得独立发表的 insight。\n\n6. **定位诚实**：Positioning paragraph 对 Messing (2026) 的对比清晰且公允（\"TEE characterizes judge selection, while we characterize item-and-protocol selection\"），未试图过度区分。\n\n---\n\n**总结**: 一篇实验执行和鲁棒性分析达到高标准的实证研究，D-study budgets 具有实际价值。核心不足在于方法论创新有限（G-theory 和 D-study 均为教科书操作）、binary scoring conditionality 严重限制适用范围但 title 未反映、以及 C2 (format-associated pattern) 统计支撑不足。建议：Conference 接收需要 (a) 更清晰地定位方法论创新点（尤其是 IRT+G-theory 互补性），(b) title/abstract 中限定 binary scoring scope。当前版本更适合 Findings。\n",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 — 新颖性与完整性审查\n\n---\n\n## 总体评分\n**Overall**: 3.5 / 5 — Borderline Conference\n**一句话总结**: 一篇执行严谨、鲁棒性分析充分的大规模实证研究，D-study 预算工具具有实际价值；但核心方法论为教科书级 G-theory 操作在新数据上的应用，相对于 Messing (2026) TEE 的增量创新有限，format-associated finding 统计力度不足以支撑独立贡献。\n\n## 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| Soundness | 4/5 | 实验设计严谨（全交叉因子、Henderson Method I + bootstrap CI）；9 项鲁棒性分析覆盖估计器、二值数据假设、模型留一法等；binary scoring conditionality 透明披露且有 partial-credit pilot 验证。主要扣分：quasi-random model facet 假设在 8 个同代模型上的可迁移性有限 |\n| Excitement | 3/5 | G-theory 是成熟框架，应用于 LLM 评估的开创性已被 Messing (2026) 占据；本文的三个扩展方向（infrastructure facets, cross-benchmark, D-study budgets）是 solid incremental work 但非 paradigm shift；D-study budget 作为实用工具有价值但概念上是 textbook G-theory 的标准操作 |\n| Reproducibility | 4/5 | 模型全部开源可获取，实验设计（facet levels、prompt templates）在正文+附录完整公开；承诺发布 G-theory pipeline 和 D-study calculator；扣分：200 items 的具体采样过程（seed 42、10/57 subjects）需发布 item list 才能完全复现 |\n| Overall | 3.5/5 | 高质量的实证工作，适合 Findings；Conference 接收需要更强的方法论创新或更具结论性的 format-associated finding |\n\n**Reviewer Confidence**: 4/5（熟悉 G-theory、IRT 和 LLM evaluation 文献）\n\n---\n\n## Must-Fix 问题（影响接收决定）\n\n**N1** [critical] 相对于 Messing (2026) TEE 的增量贡献定位不够清晰——方法论创新 vs. scale-up 界限模糊\n\n- 具体位置：Section 1 (Introduction, Contributions), Section 2 (Positioning paragraph)\n- 问题：论文在 Positioning paragraph（Section 2 末尾）列出三个扩展方向：(i) infrastructure facets 替代 judge identity, (ii) cross-benchmark comparison, (iii) D-study budgets。但这三个方向在方法论层面的创新程度不同，论文未加区分：\n  - 扩展 (i) 本质上是将 G-theory 应用于不同的 facet 集合（precision, seed, ordering 替代 judge identity），facet 选择不同≠方法论不同\n  - 扩展 (ii) 是实验规模的增加（1 benchmark → 5 benchmarks），是 scale-up 而非新方法\n  - 扩展 (iii) D-study projection 是 G-theory 的标准操作（Brennan 2001, Ch. 4），教科书级别\n  \n  唯一接近方法论创新的是：将 IRT item selection 和 G-theory protocol optimization 证明为正交互补（Table 4，IRT 116 items 在 single-condition 下 G=0.457 vs. multi-facet 下 G=0.895）。但这个发现被埋在 §4.5 的一个段落中，未在 Contributions 中突出。\n- 为什么影响接收：如果三个扩展都是 scale-up，论文的 novelty 不足以支撑 Conference 级别；如果 IRT+G-theory 互补性是独立贡献，需要在 Contributions 中明确提升\n- 建议修改方向：(a) 在 Contributions 中将 IRT+G-theory 互补性分析提升为独立贡献点或明确标注为 C1 的关键子结论；(b) 在 Positioning 段落中对三个扩展方向分别标注方法论层级（methodological extension vs. empirical scale-up），坦诚说明哪些是新方法、哪些是已有方法的新应用\n\n**N2** [critical] Binary scoring conditionality 严重限制 D-study budget 的实际适用范围，但 title 和 abstract 的表述暗示了更广的适用性\n\n- 具体位置：Title, Abstract, §3.5, §4.1, Appendix A (Scoring metric sensitivity)\n- 问题：论文标题 \"Reproducibility Budgets for Open-Weight LLM Evaluation\" 暗示 budgets 适用于通用 LLM evaluation。但 partial-credit pilot（Appendix A）显示 binary → partial credit 后 G 从 0.76 降至 0.55、item difficulty ranking ρ=0.26（几乎无关），说明 budget 在 binary scoring 之外完全不适用。§3.5 和 §4.1 的 text-exact-match 实验更极端（G=0.936 vs. 0.007）。这意味着：\n  - 论文的核心产出（178 items, 3×3 design）仅对 binary correctness scoring 有效\n  - 实际 LLM evaluation 中很多场景使用 continuous scoring（如 MT-Bench、AlpacaEval 的 win rate、LLM-as-judge 评分），论文的 budgets 对这些场景没有指导价值\n  - Title 和 abstract 均未限定 \"under binary scoring\"\n- 为什么影响接收：如果适用范围仅限 binary scoring，论文 impact 显著缩窄；如果 title 误导读者认为 budgets 通用适用，是 framing 问题\n- 建议修改方向：(a) Title 中加入 \"under Binary Scoring\" 或 \"for Binary Benchmarks\" 限定；(b) Abstract 首句即声明 binary scoring scope；(c) Discussion 中明确列出不适用的 evaluation 场景（LLM-as-judge, continuous scoring, preference ranking）\n\n---\n\n## Should-Fix 问题（影响评分但不一票否决）\n\n**W1** [warning] \"3.1× item reduction\" 的 framing 掩盖了 total evaluation 增长\n\n- 具体位置：Abstract（第 3-4 句）, §1 Contribution C1, §4.5\n- 问题：Abstract 写 \"a 3.1× item reduction over single-condition designs (552 items, 552 evaluations)---trading approximately 3× more evaluations per item for 3× fewer items\"——从 552 evaluations（single-condition）增加到 1,602 evaluations（3-prompt×3-seed，178 items × 9 conditions）。虽然论文确实披露了这个 tradeoff（\"trading approximately 3× more evaluations per item\"），但 framing 优先强调 item reduction 而非 total evaluation increase 可能误导快速阅读者。特别是 Introduction 中 Contribution C1 只写 \"a 3.1× reduction over single-condition designs (552 items)\" 而未提及 total evaluations 从 552 增加到 1,602。\n- 建议：在 Contribution C1 中加入 total evaluation count 对比（552 → 1,602 total evaluations, 2.9× increase），让读者一眼看到完整 tradeoff\n\n**W2** [warning] Format-associated variance pattern (C2) 占用大量篇幅但统计支撑不足\n\n- 具体位置：§4.3 (整个 subsection, 约 1 页), Figure 3, Table 3\n- 问题：C2 的 benchmark-level 检验力极低：n=5, exhaustive permutation p=0.10（C(5,3)=10 种分法的 floor），benchmark-level CI 跨越零 [-1.7, 5.1]。论文正确标注了 \"exploratory\"，但 §4.3 占据约 1 页正文，包含对 HellaSwag 异常的详细讨论、tautology 反驳、difficulty dispersion 分析等。这些分析本身质量不错，但对于一个 p=0.10 的 exploratory observation，这个篇幅在 8 页限制下显得奢侈——相当于正文的 12.5%。这些内容可以压缩或移至附录，将正文空间给予更有结论性的 C1 分析。\n- 建议：§4.3 主文保留 1 段核心发现（MC 68-72% vs. FF 31-41%, exploratory, p=0.10），将 HellaSwag 例外讨论、tautology 反驳、difficulty dispersion 分析移至附录\n\n**W3** [warning] Conclusion 过于简短，缺乏 practical implications 讨论\n\n- 具体位置：Section 5（仅 1 段，约 5 行）\n- 问题：对于一篇提出 \"reproducibility budgets\" 的论文，Conclusion 应讨论：(a) 实际部署这些 budgets 的路径（如何集成到 lm-evaluation-harness、HELM 等现有框架）；(b) 对 benchmark 设计者的具体建议（何时选 multi-facet vs. single-condition）；(c) 对 leaderboard 运营者的影响。当前 Conclusion 仅复述了 3×3 design 的数字和 binary scoring 限制，缺乏 forward-looking discussion。\n- 建议：扩展 Conclusion 至 2-3 段，增加 practitioner-oriented 讨论\n\n**W4** [warning] Related Work 缺少对 evaluation harness 实现层面文献的讨论\n\n- 具体位置：Section 2\n- 问题：论文的 D-study budgets 直接关系到评估框架的实际设计。但 Related Work 未讨论以下实际相关的工作：\n  - EleutherAI lm-evaluation-harness（Biderman et al. 2024 被引用但仅从 seed/training sensitivity 角度，未讨论其 evaluation protocol 设计如何与本文 multi-facet 建议整合）\n  - MMLU-Redux (Gema et al. 2024) 和 MMLU-Pro (Wang et al. 2024)——这些是 MMLU 的修订版本，直接影响本文 200-item sampling 的代表性问题\n  - OpenCompass 和其他中文 evaluation 框架（如果论文声称 \"open-weight LLM evaluation\" 的通用性）\n- 建议：在 Related Work 或 Limitations 中增加 1-2 句讨论 evaluation harness 整合和 MMLU 变体\n\n**W5** [warning] Model 样本的时间同质性可能高估 model×item interaction 的稳定性\n\n- 具体位置：§3.5 (Model Facet), §6 (Limitations, 第一句)\n- 问题：8 个模型全部来自 2024-2025 训练周期，共享指令微调范式。Limitations 承认了这一点，但未充分讨论其对 variance decomposition 的具体影响。如果 2024-2025 代模型在训练数据上有高度重叠（pre-training corpus 相似），model×item interaction（30-36%）可能部分反映训练数据共性而非真正的架构差异。这与 contamination concern（§6 末尾提及）相关但不同——即使没有 benchmark contamination，相似的训练数据也会导致相似的 DIF profiles。Leave-one-model-out 分析（CV ≤ 1.25%）确认了当前 8 个模型内的稳定性，但不能外推到 2026+ 代模型。\n- 建议：在 Limitations 中增加 1-2 句明确讨论 training data overlap 与 model×item interaction 的关系，以及 budget 推荐对未来模型代的有效期\n\n---\n\n## 小问题（不影响接收）\n\n- **M1**: Abstract 数字密度过高（2.3M, 178, 1602, 3.1×, 552, 36%, G≥0.80, 3B-72B 在短短 6 行内），建议精简至 3-4 个关键数字，将其余移至 Introduction\n- **M2**: Table 3 中 \"prompt\" 行在 MC 和 FF 下含义不同（MC = prompt×item interaction, FF = prompt main effect），尽管 caption 有说明，但行标签一致容易误读。建议使用不同行标签或分行\n- **M3**: Appendix 中 Table 5 (LOMO stability) 标注为 \"Table 5\" 但 main text Table 4 之后应为 Table 5。编号看起来正确，但建议验证交叉引用\n- **M4**: §4.4 (Precision Separability) 仅 2 句话，作为独立 subsection 过短。考虑合并到 §4.1 或 §4.5\n- **M5**: Figure 1 (teaser) 中 y 轴标签 \"Generalizability Coefficient\" 字体偏小，在打印版可能难以辨认\n\n---\n\n## Questions for Authors\n\n1. **IRT+G-theory 互补性**：Table 4 显示 IRT-selected 116 items 在 multi-facet 下 G=0.895。这是否意味着最优策略是先用 IRT 选 item、再用 G-theory 优化 protocol？如果是，建议在 Contribution 中明确提出这一 pipeline。\n\n2. **Partial-credit scoring 的 follow-up 优先级**：鉴于 partial-credit pilot 显示 G 大幅下降（0.76→0.55）且 item ranking 几乎无关（ρ=0.26），是否有计划扩展到 LLM-as-judge continuous scoring？这将显著扩大论文的适用范围。\n\n3. **Contamination 的定量检验**：§6 提到 \"consistent variance structures across three independently constructed MC benchmarks provide indirect evidence against contamination as the sole driver\"。是否可以对 8 个模型分别运行 contamination detection（如 Oren et al. 2024 的方法），提供直接证据？\n\n4. **72B 验证**：§4.6 的 Qwen2.5 within-family 验证显示 model×item=38.5% > item=35.7%。但仅 3 个模型（3B/7B/72B）不足以估计 G。是否有计划增加其他 architecture 的 72B 模型（如 Llama-3 70B）进行 cross-family 验证？\n\n---\n\n## 主要优势\n\n1. **实验规模与设计严谨性**：2.3M 条记录、7 facets、8 models、5 benchmarks 的全交叉因子设计在 LLM evaluation 方差分析文献中属最大规模之一。Henderson Method I + 1,000 resample bootstrap CI 的统计方法选择恰当。\n\n2. **鲁棒性分析极为充分**：9 项独立分析（GLMM complement, REML comparison, probit simulation, LOMO, null calibration, CI method comparison, facet specification sensitivity, accuracy-range stability, reduced crossing validation）覆盖了 reviewer 可能提出的几乎所有方法论质疑。这是论文最强的技术优势。\n\n3. **实用产出**：D-study budget calculator 和 intermediate design gradient（Table 9, Appendix C）为 evaluation practitioners 提供了即时可用的决策工具。特别是 \"minimal upgrade (2 prompts)\" 从 G=0.592 到 G=0.692 的 steep gain 是对社区非常有价值的实用 insight。\n\n4. **Binary scoring conditionality 的透明处理**：论文在 §3.5 首次声明、§4.1 用 text-exact-match 实验佐证、Appendix A 用 partial-credit pilot 验证、§4.3 再次提醒——对关键限制的多次、多角度披露远超同类论文水平。\n\n5. **IRT+G-theory 互补性分析**（Table 4）：证明 item selection（IRT）和 protocol optimization（G-theory）是正交的——IRT 116 items 在 single-condition 下 G=0.457 但在 multi-facet 下 G=0.895——这是一个值得独立发表的 insight。\n\n6. **定位诚实**：Positioning paragraph 对 Messing (2026) 的对比清晰且公允（\"TEE characterizes judge selection, while we characterize item-and-protocol selection\"），未试图过度区分。\n\n---\n\n**总结**: 一篇实验执行和鲁棒性分析达到高标准的实证研究，D-study budgets 具有实际价值。核心不足在于方法论创新有限（G-theory 和 D-study 均为教科书操作）、binary scoring conditionality 严重限制适用范围但 title 未反映、以及 C2 (format-associated pattern) 统计支撑不足。建议：Conference 接收需要 (a) 更清晰地定位方法论创新点（尤其是 IRT+G-theory 互补性），(b) title/abstract 中限定 binary scoring scope。当前版本更适合 Findings。\n",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 783 · 2026-05-23T02:34:33.708249+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3766
}
```

</details>

---


### Assistant

_source line 784 · 2026-05-23T02:34:46.157249+00:00_

审稿意见已提交给 Review Director。

**评分摘要**：Overall 3.5（Borderline Conference），Soundness 4/5，Excitement 3/5，Reproducibility 4/5。

**核心判断**：实验执行和鲁棒性分析达到高标准，D-study budget 工具有实际价值。但两个 must-fix 问题限制了 Conference 接收：(1) 相对 Messing (2026) TEE 的增量贡献在方法论创新 vs. scale-up 之间定位模糊——IRT+G-theory 互补性是最有潜力的独立贡献点但被低估；(2) binary scoring conditionality 严重限制适用范围，但 title/abstract 未反映这一限定。当前版本更适合 Findings。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 20

## Round 20

4 recorded events


### User

_source line 785 · 2026-05-23T02:47:04.425221+00:00_

[Round 1 审稿请求]:
以下是 Reviewer 1 的完整审稿意见，请逐条回应：对每一条 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

## Reviewer 1 — 方法严谨性审查

**Overall**: 3.5 / 5 — Borderline Conference

| 维度 | 分数 | 理由摘要 |
|------|------|----------|
| Soundness | 3.5/5 | 方差分解正确，Henderson Method I 适用性验证充分；但 D-study item budget 公式不完整，binary 数据对投影精度的系统性偏差未量化 |
| Excitement | 3.5/5 | G-theory 应用于 LLM 评估新颖且实用，但核心方法论是成熟框架的领域迁移 |
| Reproducibility | 4/5 | 实验描述详尽，承诺开源；但 D-study 投影公式不完整，外部读者无法独立验证 |

## Must-Fix

**N1** [critical] D-study item budget 计算公式不完整，核心贡献不可独立验证
- Equation 1 定义 G_item 不含 n_p，但 Table 4 报告 n_{G≥0.80}=55/552 随 item 数变化
- 通过反推验证：G(200)=0.592, n_{G≥0.80}=552 → single-item reliability ≈ 0.0072，与 Spearman-Brown 一致
- 论文存在两个不同 G 指标但只明确定义了一个
- 建议：完整给出 D-study 投影公式（含 n_p），区分 per-item G 和 aggregate-score G，提供计算示例

**N2** [critical] Binary scoring 对 D-study 投影精度的系统性影响未量化
- Probit simulation: ρ=0.732, top-5 ordering 仅 79% correct, |bias|=0.28-0.37
- Bootstrap CIs 捕捉抽样变异性，不含 binary scoring 系统偏差
- 建议：从 probit simulation 的 continuous components 计算 D-study projections 并比较

## Should-Fix

**W1** G_item 测量 item 难度可靠性而非模型比较可靠性——概念鸿沟
- σ²_model 仅 2.8%，model-level G 可能显著低于 G_item
- 建议：显式计算 G_model（models 为 object），讨论 G_item ≥ 0.80 是否蕴含 model ranking reliability

**W2** 模型可交换性假设 out-of-sample 验证不足
- LOMO 和 four-model subset 是 within-sample stability，非 out-of-sample
- 72B validation 仅 Qwen2.5 family 内
- 建议：获取 cross-family validation point

**W3** Partial-credit pilot 基于单 benchmark 单 model 但结论陈述过于确定
- "do not transfer" 措辞过强
- 建议：改为 "preliminary evidence suggests limited transferability"

**W4** Format-associated pattern 统计支撑不足且设计不对称
- n=5, p=0.10, CI含零；ordering 仅对 MC 有效；MC/FF prompt 类型不同
- 建议：更明确标注 exploratory/descriptive

## Minor
M1: "all others < 0.1%" 不够精确
M2: 排除 temperature=1.0 可能低估 temperature variance
M3: 单一推理引擎（vLLM 0.9.2）
M4: 200 items 代表性
M5: Few-shot example identity 未作为 facet

## 主要优势
1. 问题意义重大：LLM 评估可复现性是领域痛点
2. 实验规模充分：~230 万 records
3. 鲁棒性验证异常全面：9 项附录分析
4. 实用输出具体可操作：D-study budget recommendations
5. Limitations section 坦诚且全面
6. Subject-level 分析有洞察价值（Table 10）

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 786 · 2026-05-23T02:48:22.437207+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n## Reviewer 2 对 Reviewer 1 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: D-study item budget 公式不完整**\n\n同意这是一个影响可复现性的实质问题。Equation 1（§3.1）定义的 G_item 公式中 σ²_rel 是一个聚合项，但论文未展示 σ²_rel 的完整展开式（即哪些 interaction variance components 除以各自 facet 的 n_k 后求和）。读者需要同时参考 Brennan (2001, Ch. 4) 和论文的 facet 结构才能重建计算过程。Table 4 报告了不同 item 数下的 G 值（55, 178, 552 items for G≥0.80），但从 Equation 1 到这些数字之间的推导步骤是缺失的。\n\n补充 R1 的观察：反推 G(200)=0.592 在 single-condition 下得到 single-item reliability ≈ 0.0072 确实与 Spearman-Brown 公式一致，说明论文的计算是正确的——但正确不等于可验证。论文的核心贡献是 D-study budgets，如果读者无法独立复现这些 budgets，贡献的 impact 打折扣。建议在正文或附录增加一个完整的计算示例（如 MMLU single-model 的 σ²_rel 展开 + n_p 求解过程）。\n\n**[AGREE with nuance] R1-N2: Binary scoring 对 D-study projection 精度的系统偏差**\n\nR1 的核心论点成立：probit simulation 的 ρ=0.732（排除 residual）和 top-5 ordering 79% correct 说明 binary data 的 variance component 估计存在非平凡偏差。R1 正确指出 bootstrap CIs 捕捉的是 item-sampling variability 而非 binary-specific systematic bias。\n\n但我认为 R1 可能略微高估了这个问题的严重性。原因如下：\n\n1. 论文在 Appendix A（Probit simulation）已经透明报告了这些偏差数值，并指出 Henderson Method I 将 Bernoulli-inherent variance 吸收到 residual 中——这是已知行为而非隐藏缺陷\n2. Null calibration（Appendix A）显示 observed-to-null variance ratio = 1.0008，100 replications 中 top-3 component set consistency = 100%，Kendall's τ = 0.81——systematic component **ordering** 在所有 replications 中稳健恢复\n3. D-study budgets 基于的是 component 的相对大小（ratio），而非绝对值。如果 binary scoring 系统性地膨胀所有 components（通过 Bernoulli ceiling），相对 ranking 不变则 budget ratio（如 10×）仍然有效\n\n不过 R1 建议的对比实验（从 probit simulation 的 continuous components 计算 D-study projections 并与 binary 版本比较）确实值得做。这能直接量化 binary scoring 引入的 budget bias，是一个建设性的建议。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: G_item 与 model comparison reliability 的概念鸿沟**\n\n这是一个重要的概念性问题。论文始终以 item 为 object of measurement（G_item），但读者更关心的实际问题往往是 \"这些 items 能否可靠区分模型\"——即 model-level reliability。σ²_model 仅 2.8%（Table 2），意味着 model 间 variance 很小。G_model（以 model 为 object）可能远低于 G_item=0.896。\n\n论文在 §3.1 解释了为什么选择 item 作为 object（\"the goal is to determine how reliably item-level scores generalize across methodological conditions\"），但未讨论 G_item ≥ 0.80 是否蕴含 model ranking 的可靠性。这两个问题的关系在 G-theory 中是明确的（Brennan 2001, Ch. 4），但论文需要向 NLP 读者显式说明。\n\n建议作者在 §4.5 或 Discussion 中增加 G_model 计算结果（即使只是 1-2 句），并讨论 item reliability 和 model ranking reliability 的关系。\n\n**[AGREE] R1-W2: 模型可交换性 out-of-sample 验证不足**\n\n同意 LOMO 和 four-model subset 是 within-sample stability 检查，不等于 out-of-sample generalization。§4.6 的 72B validation 限于 Qwen2.5 family（共享 tokenizer 和训练 recipe），不构成 cross-family validation。\n\n我在自己的审稿意见（R2-W5）中也提出了类似观点：8 个模型的时间同质性（2024-2025 训练周期）可能高估 variance structure 的稳定性。R1 的建议（获取 cross-family validation point，如 Llama-3 70B）与我的建议一致。\n\n**[AGREE] R1-W3: Partial-credit pilot 的 \"do not transfer\" 措辞**\n\n同意。§6 (Limitations) 写 \"budgets do not transfer to finer-grained scoring rubrics\"，但这个结论基于单 benchmark (GSM8K) 单 model (Llama-3.1-8B-Instruct)。改为 \"preliminary evidence suggests limited transferability\" 更符合证据强度。\n\n不过我要补充：partial-credit pilot 的 ρ=0.26（item difficulty ranking）和 G 从 0.76 降至 0.55 的变化幅度已经足够大，即使措辞软化，核心 message 不变——binary scoring budgets 很可能不适用于 continuous scoring。\n\n**[AGREE] R1-W4: Format-associated pattern 统计支撑与设计不对称**\n\n完全同意。我在自己的审稿意见（R2-W2）中对同一问题给出了一致的评估：n=5, p=0.10, CI 含零，加上 ordering facet 仅对 MC 有效、MC/FF prompt 类型不同的设计不对称，使得 format-associated 发现只能作为 descriptive observation。\n\n论文确实标注了 \"exploratory\" 并报告了 permutation p=0.10，这一点处理是透明的。但我在 R2-W2 中额外建议将 §4.3 的详细讨论（HellaSwag 例外、tautology 反驳、difficulty dispersion 分析等）从正文移至附录以节省 8 页空间。R1 未提到这个空间分配问题——这是我的补充。\n\n---\n\n### Minor\n\n**[AGREE] R1-M1**: \"all others < 0.1%\" 确实应报告精确数值或至少 top-2 \"all others\" 的具体值。\n\n**[AGREE] R1-M2**: 排除 temperature=1.0 可能低估 temperature variance。论文使用 0.0/0.3/0.7，而实际部署中 temperature=1.0 较常见。不过 §4.1 的 temperature×item 仅 2.9%，即使加入 1.0 也不太可能改变 dominant component ranking。\n\n**[AGREE] R1-M3**: 单一推理引擎 (vLLM 0.9.2) 是合理的实验控制，但 vLLM 的特定 CUDA kernel 行为可能影响 seed×item 和 residual 的分布。值得在 Limitations 提及。\n\n**[REBUT] R1-M4**: 200 items 代表性——论文已报告 CV=3.1%（三次独立重采样，§3.2）并承认 \"cross-subject generalization remains untested\"（§3.2）。对于 G-study 而言，200 items 在同类文献中属于较大样本（Messing 2026 使用单 benchmark，Bouthillier 2021 使用更少 data points）。虽然 10/57 MMLU subjects 确实限制了外推性，但 subject-level 分析（Table 10, Appendix E）展示了 10 个 subjects 内的变异范围（G_item 从 0.614 到 0.930），说明 200 items 捕捉到了 MMLU 内的实质性异质性。这不是一个 \"fix\" 级别的问题。\n\n**[AGREE] R1-M5**: Few-shot example identity 是已知的 variance source，论文在 §6 (Limitations) 已承认（\"Our design varies few-shot example ordering but not example identity, a known variance source\"），处理恰当。\n\n---\n\n### 对 R1 主要优势评估的回应\n\nR1 列出的 6 项优势全部成立，与我的独立评估高度一致。特别是：\n- 优势 3（鲁棒性验证异常全面）——我在 R2 审稿中也将此列为论文最强技术优势\n- 优势 6（Subject-level 分析有洞察价值）——Table 10 确实是论文的亮点之一，reasoning-heavy subjects 的 G_item 低至 0.614 vs. knowledge-intensive subjects 的 0.930 是一个重要发现\n\n---\n\n### 与 R1 Overall Assessment 的对比\n\nR1 和 R2 均给出 3.5（Borderline Conference），理由相互补充：\n- R1 侧重方法论严谨性（D-study 公式完整性、binary bias 量化）\n- R2 侧重新颖性（vs. Messing 2026 的增量贡献、binary scoring 的适用范围限制）\n- 两位 Reviewer 在以下问题上独立达成一致：format-associated pattern 统计力度不足、out-of-sample model validation 缺失、partial-credit 结论过强\n- 两位 Reviewer 均认为论文的实验规模和鲁棒性分析是突出优势\n\n共识结论：论文当前版本更适合 Findings（Overall 3.0-3.5 区间），Conference 接收需要解决 N1（公式完整性）和 N2（binary bias 量化）两个 critical 问题，以及在 framing 上更准确地限定 binary scoring 适用范围。\n",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n## Reviewer 2 对 Reviewer 1 意见的逐条回应\n\n---\n\n### Must-Fix\n\n**[AGREE] R1-N1: D-study item budget 公式不完整**\n\n同意这是一个影响可复现性的实质问题。Equation 1（§3.1）定义的 G_item 公式中 σ²_rel 是一个聚合项，但论文未展示 σ²_rel 的完整展开式（即哪些 interaction variance components 除以各自 facet 的 n_k 后求和）。读者需要同时参考 Brennan (2001, Ch. 4) 和论文的 facet 结构才能重建计算过程。Table 4 报告了不同 item 数下的 G 值（55, 178, 552 items for G≥0.80），但从 Equation 1 到这些数字之间的推导步骤是缺失的。\n\n补充 R1 的观察：反推 G(200)=0.592 在 single-condition 下得到 single-item reliability ≈ 0.0072 确实与 Spearman-Brown 公式一致，说明论文的计算是正确的——但正确不等于可验证。论文的核心贡献是 D-study budgets，如果读者无法独立复现这些 budgets，贡献的 impact 打折扣。建议在正文或附录增加一个完整的计算示例（如 MMLU single-model 的 σ²_rel 展开 + n_p 求解过程）。\n\n**[AGREE with nuance] R1-N2: Binary scoring 对 D-study projection 精度的系统偏差**\n\nR1 的核心论点成立：probit simulation 的 ρ=0.732（排除 residual）和 top-5 ordering 79% correct 说明 binary data 的 variance component 估计存在非平凡偏差。R1 正确指出 bootstrap CIs 捕捉的是 item-sampling variability 而非 binary-specific systematic bias。\n\n但我认为 R1 可能略微高估了这个问题的严重性。原因如下：\n\n1. 论文在 Appendix A（Probit simulation）已经透明报告了这些偏差数值，并指出 Henderson Method I 将 Bernoulli-inherent variance 吸收到 residual 中——这是已知行为而非隐藏缺陷\n2. Null calibration（Appendix A）显示 observed-to-null variance ratio = 1.0008，100 replications 中 top-3 component set consistency = 100%，Kendall's τ = 0.81——systematic component **ordering** 在所有 replications 中稳健恢复\n3. D-study budgets 基于的是 component 的相对大小（ratio），而非绝对值。如果 binary scoring 系统性地膨胀所有 components（通过 Bernoulli ceiling），相对 ranking 不变则 budget ratio（如 10×）仍然有效\n\n不过 R1 建议的对比实验（从 probit simulation 的 continuous components 计算 D-study projections 并与 binary 版本比较）确实值得做。这能直接量化 binary scoring 引入的 budget bias，是一个建设性的建议。\n\n---\n\n### Should-Fix\n\n**[AGREE] R1-W1: G_item 与 model comparison reliability 的概念鸿沟**\n\n这是一个重要的概念性问题。论文始终以 item 为 object of measurement（G_item），但读者更关心的实际问题往往是 \"这些 items 能否可靠区分模型\"——即 model-level reliability。σ²_model 仅 2.8%（Table 2），意味着 model 间 variance 很小。G_model（以 model 为 object）可能远低于 G_item=0.896。\n\n论文在 §3.1 解释了为什么选择 item 作为 object（\"the goal is to determine how reliably item-level scores generalize across methodological conditions\"），但未讨论 G_item ≥ 0.80 是否蕴含 model ranking 的可靠性。这两个问题的关系在 G-theory 中是明确的（Brennan 2001, Ch. 4），但论文需要向 NLP 读者显式说明。\n\n建议作者在 §4.5 或 Discussion 中增加 G_model 计算结果（即使只是 1-2 句），并讨论 item reliability 和 model ranking reliability 的关系。\n\n**[AGREE] R1-W2: 模型可交换性 out-of-sample 验证不足**\n\n同意 LOMO 和 four-model subset 是 within-sample stability 检查，不等于 out-of-sample generalization。§4.6 的 72B validation 限于 Qwen2.5 family（共享 tokenizer 和训练 recipe），不构成 cross-family validation。\n\n我在自己的审稿意见（R2-W5）中也提出了类似观点：8 个模型的时间同质性（2024-2025 训练周期）可能高估 variance structure 的稳定性。R1 的建议（获取 cross-family validation point，如 Llama-3 70B）与我的建议一致。\n\n**[AGREE] R1-W3: Partial-credit pilot 的 \"do not transfer\" 措辞**\n\n同意。§6 (Limitations) 写 \"budgets do not transfer to finer-grained scoring rubrics\"，但这个结论基于单 benchmark (GSM8K) 单 model (Llama-3.1-8B-Instruct)。改为 \"preliminary evidence suggests limited transferability\" 更符合证据强度。\n\n不过我要补充：partial-credit pilot 的 ρ=0.26（item difficulty ranking）和 G 从 0.76 降至 0.55 的变化幅度已经足够大，即使措辞软化，核心 message 不变——binary scoring budgets 很可能不适用于 continuous scoring。\n\n**[AGREE] R1-W4: Format-associated pattern 统计支撑与设计不对称**\n\n完全同意。我在自己的审稿意见（R2-W2）中对同一问题给出了一致的评估：n=5, p=0.10, CI 含零，加上 ordering facet 仅对 MC 有效、MC/FF prompt 类型不同的设计不对称，使得 format-associated 发现只能作为 descriptive observation。\n\n论文确实标注了 \"exploratory\" 并报告了 permutation p=0.10，这一点处理是透明的。但我在 R2-W2 中额外建议将 §4.3 的详细讨论（HellaSwag 例外、tautology 反驳、difficulty dispersion 分析等）从正文移至附录以节省 8 页空间。R1 未提到这个空间分配问题——这是我的补充。\n\n---\n\n### Minor\n\n**[AGREE] R1-M1**: \"all others < 0.1%\" 确实应报告精确数值或至少 top-2 \"all others\" 的具体值。\n\n**[AGREE] R1-M2**: 排除 temperature=1.0 可能低估 temperature variance。论文使用 0.0/0.3/0.7，而实际部署中 temperature=1.0 较常见。不过 §4.1 的 temperature×item 仅 2.9%，即使加入 1.0 也不太可能改变 dominant component ranking。\n\n**[AGREE] R1-M3**: 单一推理引擎 (vLLM 0.9.2) 是合理的实验控制，但 vLLM 的特定 CUDA kernel 行为可能影响 seed×item 和 residual 的分布。值得在 Limitations 提及。\n\n**[REBUT] R1-M4**: 200 items 代表性——论文已报告 CV=3.1%（三次独立重采样，§3.2）并承认 \"cross-subject generalization remains untested\"（§3.2）。对于 G-study 而言，200 items 在同类文献中属于较大样本（Messing 2026 使用单 benchmark，Bouthillier 2021 使用更少 data points）。虽然 10/57 MMLU subjects 确实限制了外推性，但 subject-level 分析（Table 10, Appendix E）展示了 10 个 subjects 内的变异范围（G_item 从 0.614 到 0.930），说明 200 items 捕捉到了 MMLU 内的实质性异质性。这不是一个 \"fix\" 级别的问题。\n\n**[AGREE] R1-M5**: Few-shot example identity 是已知的 variance source，论文在 §6 (Limitations) 已承认（\"Our design varies few-shot example ordering but not example identity, a known variance source\"），处理恰当。\n\n---\n\n### 对 R1 主要优势评估的回应\n\nR1 列出的 6 项优势全部成立，与我的独立评估高度一致。特别是：\n- 优势 3（鲁棒性验证异常全面）——我在 R2 审稿中也将此列为论文最强技术优势\n- 优势 6（Subject-level 分析有洞察价值）——Table 10 确实是论文的亮点之一，reasoning-heavy subjects 的 G_item 低至 0.614 vs. knowledge-intensive subjects 的 0.930 是一个重要发现\n\n---\n\n### 与 R1 Overall Assessment 的对比\n\nR1 和 R2 均给出 3.5（Borderline Conference），理由相互补充：\n- R1 侧重方法论严谨性（D-study 公式完整性、binary bias 量化）\n- R2 侧重新颖性（vs. Messing 2026 的增量贡献、binary scoring 的适用范围限制）\n- 两位 Reviewer 在以下问题上独立达成一致：format-associated pattern 统计力度不足、out-of-sample model validation 缺失、partial-credit 结论过强\n- 两位 Reviewer 均认为论文的实验规模和鲁棒性分析是突出优势\n\n共识结论：论文当前版本更适合 Findings（Overall 3.0-3.5 区间），Conference 接收需要解决 N1（公式完整性）和 N2（binary bias 量化）两个 critical 问题，以及在 framing 上更准确地限定 binary scoring 适用范围。\n",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 787 · 2026-05-23T02:48:27.372000+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 4934
}
```

</details>

---


### Assistant

_source line 788 · 2026-05-23T02:48:34.390536+00:00_

已提交对 Reviewer 1 的逐条回应。

总结：R1 的 2 个 Must-Fix（D-study 公式完整性、binary bias 量化）均为合理的方法论质疑，我分别给出 [AGREE] 和 [AGREE with nuance]。4 个 Should-Fix 全部 [AGREE]，与我自己的独立发现高度一致。Minor 中对 M4（200 items 代表性）给出 [REBUT]，认为论文已有充分的 within-sample 验证。R1 和 R2 在 Overall 3.5 和核心问题上达成一致——论文当前适合 Findings，Conference 需要补充公式推导和 binary bias 量化。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 21

## Round 21

90 recorded events


### User

_source line 789 · 2026-05-25T21:18:58.553883+00:00_

[Round 11 审稿请求]:
你是 Reviewer 2，负责 **新颖性 + 完整性 + 写作质量** 的审查。

## Venue 信息
- **目标会议**: EMNLP 2026（通过 ARR 统一审稿）
- **ARR 投稿截止**: 2026-05-25
- **页数限制**: Long paper, 正文 8 页，参考文献不限，Limitations 不计入页数
- **模板**: ACL (review option)
- **匿名规则**: Double-blind
- **附录**: 允许，不计入页数，但不应过度使用

## 论文路径
- LaTeX: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex`
- PDF: `/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf`

## 你的审查侧重

请重点审查以下方面：

1. **新颖性与增量贡献**：相对于 Messing (2026) — 5 facets on 1 benchmark, judge identity 43.8%，本文扩展到 7 facets × 5 benchmarks + D-study budgets 是否构成足够的 methodological advance。三个扩展方向（infrastructure facets、cross-benchmark、D-study）各自的贡献层级。IRT+G-theory 互补性 (Table 4) 是否被低估
2. **Framing 与 Claims**：
   - "10× fewer items" / "3.1× reduction" 是否隐藏了 total evaluations 的增长（552→1,602 = 2.9× 增长）
   - Abstract 数字密度（20+ 数值）是否影响可读性
   - Binary scoring scope 是否在 title/abstract 中充分限定
   - G_item 作为 item reliability 与读者关心的 model ranking reliability 之间的概念鸿沟
3. **写作质量**：
   - 结论部分是否过于简短，缺乏 practical implications 和 adoption pathway
   - 正文 8 页限制下，§4.3 format-associated pattern 占约 1 页是否比例失衡（n=5, p=0.10 的探索性发现）
   - Table 3 caption 中 MC vs FF 报告量的标注是否清晰
4. **相关工作覆盖**：
   - 是否遗漏重要文献（evaluation harness 整合、MMLU-Redux/MMLU-Pro 变体、contamination 文献）
   - Positioning table (Table 1) 是否准确反映差异
5. **格式合规**：
   - 是否满足 EMNLP 2026 / ARR 格式要求（ACL template, double-blind, page limit）
   - 匿名性检查：是否有泄露作者身份的线索（代码链接、self-citation 方式）
   - Limitations 章节是否合规（正文内，不在附录）
6. **Partial-credit / scoring conditionality**：
   - 论文声称 "do not transfer" 到 partial-credit 但仅 GSM8K 单 benchmark 验证
   - Binary scoring 的局限性（G 0.936→0.007 for text-exact-match）是否充分声明scope

## Overall Assessment 评分标准 (EMNLP 2026 ARR)
5 = Consider for Award（约前2.5%），4.5 = Borderline Award，4 = Conference（可被主会议接收），3.5 = Borderline Conference，3 = Findings（可被Findings接收），2.5 = Borderline Findings，2 = Resubmit next cycle，1.5 = Resubmit after next cycle，1 = Do not resubmit

请严格按照以下结构输出审稿意见：
- **Summary** (2-3 句)
- **Strengths** (逐条列出，标注 S1, S2, ...)
- **Weaknesses** (逐条列出，标注 W1, W2, ...，分为 Must-Fix / Should-Fix / Minor)
- **Questions** (Q1, Q2, ...)
- **Missing References**
- **Overall Assessment** (评分 + 置信度 + 理由)

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 790 · 2026-05-25T21:19:08.844196+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_2_0518f4eb/.claude/skills/review-reviewer-session-start.skill.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_2_0518f4eb/.claude/skills/review-reviewer-session-start.skill.md"
  }
}
```

</details>

---


### Tool result

_source line 791 · 2026-05-25T21:19:10.199304+00:00_

File does not exist. Note: your current working directory is /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/.claude/sessions/review_reviewer_2_0518f4eb.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1355
}
```

</details>

---


### Tool call

_source line 792 · 2026-05-25T21:19:10.350551+00:00_

called ToolSearch

<details open><summary>🔧 Tool call — ToolSearch</summary>

```json
{
  "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
  "max_results": "4"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "tool_args": {
    "query": "select:mcp__agent-ml-research__pdf_to_images,mcp__agent-ml-research__review_reviewer_post_to_director,WebSearch,WebFetch",
    "max_results": "4"
  }
}
```

</details>

---


### Tool result

_source line 793 · 2026-05-25T21:19:10.451369+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "ToolSearch",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 794 · 2026-05-25T21:19:14.871403+00:00_

called WebSearch

<details open><summary>🔧 Tool call — WebSearch</summary>

```json
{
  "query": "ACL ARR 2026 reviewer guidelines review form criteria"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "tool_args": {
    "query": "ACL ARR 2026 reviewer guidelines review form criteria"
  }
}
```

</details>

---


### Tool call

_source line 795 · 2026-05-25T21:19:16.978649+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "1-6",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "1-6",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 796 · 2026-05-25T21:19:22.984536+00:00_

Web search results for query: "ACL ARR 2026 reviewer guidelines review form criteria"

Links: [{"title":"ARR Reviewer Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewerguidelines"},{"title":"aclrollingreview/cfp.md at main · acl-org/aclrollingreview","url":"https://github.com/acl-org/aclrollingreview/blob/main/cfp.md"},{"title":"Incentives 2026 – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/incentives2026"},{"title":"Review Form – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewform"},{"title":"CALL FOR PAPERS – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/cfp"},{"title":"ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/"},{"title":"ARR Area Chair Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/acguidelines"},{"title":"Authors Guidelines – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/authors"},{"title":"How ARR works – ACL Rolling Review – A peer review platform for the Association for Computational Linguistics","url":"http://aclrollingreview.org/reviewing"}]

I found relevant information about ACL ARR 2026 reviewer guidelines and review form criteria. Here's what the search results show:

## Review Form Criteria

The main criteria for Findings papers are soundness and reproducibility, while conference recommendations may also consider novelty, impact and other factors.

## Recommendation Scores

The review form includes the following scoring options:

- 5 =
…[truncated 901 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebSearch",
  "elapsed_ms": 8113
}
```

</details>

---


### Tool result

_source line 797 · 2026-05-25T21:19:24.091756+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 1, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p1.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 461.1}, {\"page\": 2, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p2.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 756.3}, {\"page\": 3, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p3.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 464.6}, {\"page\": 4, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p4.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 491.2}, {\"page\": 5, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p5.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 487.9}, {\"page\": 6, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p6.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 436.2}], \"total_pages\": 15, \"rendered_pages\": 6, \"dpi\": 150, \"output_dir\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images\"}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 7113
}
```

</details>

---


### Tool call

_source line 798 · 2026-05-25T21:19:30.014756+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p1.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p1.png"
  }
}
```

</details>

---


### Tool call

_source line 799 · 2026-05-25T21:19:30.566956+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p2.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p2.png"
  }
}
```

</details>

---


### Tool result

_source line 800 · 2026-05-25T21:19:31.119772+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1105
}
```

</details>

---


### Tool call

_source line 801 · 2026-05-25T21:19:31.120215+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p3.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p3.png"
  }
}
```

</details>

---


### Tool result

_source line 802 · 2026-05-25T21:19:31.628269+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1061
}
```

</details>

---


### Tool call

_source line 803 · 2026-05-25T21:19:31.628763+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p4.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p4.png"
  }
}
```

</details>

---


### Tool call

_source line 804 · 2026-05-25T21:19:32.535192+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p5.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p5.png"
  }
}
```

</details>

---


### Tool result

_source line 805 · 2026-05-25T21:19:32.888242+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1768
}
```

</details>

---


### Tool call

_source line 806 · 2026-05-25T21:19:33.089968+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p6.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p6.png"
  }
}
```

</details>

---


### Tool result

_source line 807 · 2026-05-25T21:19:33.493587+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1864
}
```

</details>

---


### Tool call

_source line 808 · 2026-05-25T21:19:34.650160+00:00_

called mcp__agent-ml-research__pdf_to_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__pdf_to_images</summary>

```json
{
  "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
  "project": "nlp_variance_gtheory",
  "pages": "7-15",
  "dpi": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "tool_args": {
    "pdf_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/submitted.pdf",
    "project": "nlp_variance_gtheory",
    "pages": "7-15",
    "dpi": "150"
  }
}
```

</details>

---


### Tool result

_source line 809 · 2026-05-25T21:19:34.952926+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2417
}
```

</details>

---


### Tool result

_source line 810 · 2026-05-25T21:19:35.606639+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 2516
}
```

</details>

---


### Tool call

_source line 811 · 2026-05-25T21:19:35.657262+00:00_

called WebFetch

<details open><summary>🔧 Tool call — WebFetch</summary>

```json
{
  "url": "https://aclrollingreview.org/reviewform",
  "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. Include all fields reviewers need to fill out."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "tool_args": {
    "url": "https://aclrollingreview.org/reviewform",
    "prompt": "Extract the complete review form criteria, all scoring dimensions, their scales, and descriptions. Include all fields reviewers need to fill out."
  }
}
```

</details>

---


### Tool result

_source line 812 · 2026-05-25T21:19:35.958659+00:00_

{"result":"{\"success\": true, \"data\": {\"images\": [{\"page\": 7, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p7.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 404.0}, {\"page\": 8, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p8.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 463.8}, {\"page\": 9, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p9.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 577.2}, {\"page\": 10, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p10.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 572.8}, {\"page\": 11, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p11.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 542.1}, {\"page\": 12, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p12.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 454.6}, {\"page\": 13, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p13.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 496.6}, {\"page\": 14, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p14.png\", \"width\": 1241, \"height\": 1754, \"size_kb\": 431.3}, {\"page\": 15, \"path\": \"/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p15.png\", \"width\": 1241, \"height\": 1754, \"size_kb\
…[truncated 241 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__pdf_to_images",
  "elapsed_ms": 1308
}
```

</details>

---


### Tool result

_source line 813 · 2026-05-25T21:19:46.346827+00:00_

# ACL Rolling Review Form: Complete Criteria and Scoring

## Primary Evaluation Dimensions

### 1. **Reviewer Confidence**
Scale: 1-5
- **5**: "Positive that my evaluation is correct. I read the paper very carefully and am familiar with related work."
- **4**: Quite sure with unlikely oversights
- **3**: Pretty sure but possible gaps in detail review
- **2**: Willing to defend evaluation but likely missed details
- **1**: Outside expertise area or paper very difficult to understand

### 2. **Soundness**
Scale: 1-5 (with .5 increments)
Assesses scientific rigor, claim support, and methodological validity.
- **5**: "Excellent: This study is one of the most thorough I have seen"
- **4**: Strong with sufficient support; minor experiments optional
- **3**: Acceptable; main claims supported with minor gaps
- **2**: Poor; major technical/methodological problems
- **1**: Major issues; insufficiently thorough for publication

### 3. **Excitement**
Scale: 1-5 (with .5 increments)
Evaluates subjective appeal including innovation, impact, and relevance.
- **5**: Highly exciting; would recommend widely
- **4**: Exciting; would mention to others
- **3**: Interesting; might mention selectively
- **2**: Potentially interesting to some community members
- **1**: Not exciting; lacks computational linguistics relevance

### 4. **Overall Assessment**
Scale: 1-5 (with .5 increments)
Final recommendation for publication venue:
- **5**: Consider for Award (top 2.5%)
- **4**: Conference acceptance
- **3**: Findings acceptance
- **2**: Resubmit next cycle
- **1**: Do not resubmit

### 5. **Reproducibility**
Scale: 1-5
Ability to replicate results and build future work:
- **5**: Results easily reproducible
- **4**: Mostly reproducible with minor variations
- **3**: Reproducible with difficulty; underspecified parameters
- **2**: Hard to reproduce; unavailable data or insufficient details
- **1**: Results not reproducible

### 6. **Datasets Value**
Scale: 1-5
- **5**: Enabling; affects resear
…[truncated 1168 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "WebFetch",
  "elapsed_ms": 10689
}
```

</details>

---


### Tool call

_source line 814 · 2026-05-25T21:19:52.027658+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p7.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p7.png"
  }
}
```

</details>

---


### Tool result

_source line 815 · 2026-05-25T21:19:52.534348+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 506
}
```

</details>

---


### Tool call

_source line 816 · 2026-05-25T21:19:52.536840+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p8.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p8.png"
  }
}
```

</details>

---


### Tool call

_source line 817 · 2026-05-25T21:19:53.038200+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p9.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p9.png"
  }
}
```

</details>

---


### Tool result

_source line 818 · 2026-05-25T21:19:53.942017+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1405
}
```

</details>

---


### Tool result

_source line 819 · 2026-05-25T21:19:53.993548+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 955
}
```

</details>

---


### Tool call

_source line 820 · 2026-05-25T21:19:53.994007+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p10.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p10.png"
  }
}
```

</details>

---


### Tool call

_source line 821 · 2026-05-25T21:19:54.546889+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p11.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p11.png"
  }
}
```

</details>

---


### Tool result

_source line 822 · 2026-05-25T21:19:54.900609+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 906
}
```

</details>

---


### Tool call

_source line 823 · 2026-05-25T21:19:54.901004+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p12.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p12.png"
  }
}
```

</details>

---


### Tool result

_source line 824 · 2026-05-25T21:19:55.454730+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 907
}
```

</details>

---


### Tool call

_source line 825 · 2026-05-25T21:19:55.455133+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p13.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p13.png"
  }
}
```

</details>

---


### Tool result

_source line 826 · 2026-05-25T21:19:56.311815+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1410
}
```

</details>

---


### Tool result

_source line 827 · 2026-05-25T21:19:56.312920+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 857
}
```

</details>

---


### Tool call

_source line 828 · 2026-05-25T21:19:56.313225+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p14.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p14.png"
  }
}
```

</details>

---


### Tool call

_source line 829 · 2026-05-25T21:19:56.616137+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p15.png"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images/submitted_p15.png"
  }
}
```

</details>

---


### Tool result

_source line 830 · 2026-05-25T21:19:56.617868+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 1
}
```

</details>

---


### Tool result

_source line 831 · 2026-05-25T21:19:56.869470+00:00_



<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 556
}
```

</details>

---


### Tool call

_source line 832 · 2026-05-25T21:20:14.736267+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
  "limit": "150"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex",
    "limit": "150"
  }
}
```

</details>

---


### Tool result

_source line 833 · 2026-05-25T21:20:14.786910+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{graphicx}
13	\usepackage{amsmath,amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\enlargethispage{1\baselineskip}
44	\input{conclusion}
45	
46	% === LIMITATIONS ===
47	\input{limitations}
48	
49	\bibliography{references}
50	
51	% === APPENDIX ===
52	\input{appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 834 · 2026-05-25T21:20:23.598011+00:00_

called Agent

<details open><summary>🔧 Tool call — Agent</summary>

```json
{
  "description": "Read LaTeX source files",
  "subagent_type": "Explore",
  "prompt": "I need to read the LaTeX source files for a paper. The main file is at /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex which imports several files via \\input{}: abstract, introduction, related_work, method, experiments, conclusion, limitations, appendix. \n\nPlease find and read all these .tex files in the same directory (/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/). Report the FULL content of each file - abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, and appendix.tex. I need every line of text for a detailed review."
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Agent",
  "tool_args": {
    "description": "Read LaTeX source files",
    "subagent_type": "Explore",
    "prompt": "I need to read the LaTeX source files for a paper. The main file is at /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex which imports several files via \\input{}: abstract, introduction, related_work, method, experiments, conclusion, limitations, appendix. \n\nPlease find and read all these .tex files in the same directory (/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/). Report the FULL content of each file - abstract.tex, introduction.tex, related_work.tex, method.tex, experiments.tex, conclusion.tex, limitations.tex, and appendix.tex. I need every line of text for a detailed review."
  }
}
```

</details>

---


### Tool call

_source line 835 · 2026-05-25T21:20:25.756586+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper -type f -name \"*.tex\" | sort"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "find /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper -type f -name \"*.tex\" | sort"
  }
}
```

</details>

---


### Tool result

_source line 836 · 2026-05-25T21:20:25.907583+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 837 · 2026-05-25T21:20:30.277907+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 838 · 2026-05-25T21:20:30.480547+00:00_

1	LLM benchmarks are the primary tool for comparing language models, guiding decisions about deployment, funding, and public rankings. Every evaluation involves design choices (prompt template, random seed, numerical precision, answer ordering) that are typically fixed to a single value and assumed inconsequential. Growing evidence challenges this assumption: prompt formatting alone can shift accuracy by up to 76 percentage points, and answer ordering can flip model rankings. Yet each study examines one factor in isolation, leaving unanswered which sources dominate when all vary simultaneously, and how many test items are truly needed for reliable measurement. We address this using Generalizability theory, a psychometric framework for multi-source variance decomposition. In a factorial experiment crossing seven facets across eight open-weight models and five benchmarks (2.3M binary records), we find that the dominant non-residual variance source is not the prompt or the seed but the model$\times$item interaction (30--36\% in multiple-choice benchmarks, 15--17\% in free-form), meaning models disagree on which items are difficult rather than in overall ability. Multi-facet designs absorb this noise, reducing item requirements from over 1,000 to roughly 100. The variance structure is format-dependent: item factors dominate multiple-choice benchmarks but disperse in free-form tasks. We release an open-source G-theory pipeline and D-study calculator\footnote{Code and data are available at \url{https://anonymous.4open.science/r/nlp_variance_gtheory-11E1/}.}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 202
}
```

</details>

---


### Tool call

_source line 839 · 2026-05-25T21:20:30.480909+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 840 · 2026-05-25T21:20:30.481106+00:00_

1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=\textwidth]{fig_overview_pipeline}
4	\caption{Overview of the G-theory evaluation pipeline. A factorial design crossing seven facets across eight models and five benchmarks produces 2.3M binary records. G-study variance decomposition via Henderson Method~I reveals that model$\times$item interaction accounts for up to 36\% of variance. D-study projections translate variance components into design-dependent item budgets: a 3-prompt $\times$ 3-seed design achieves $G \geq 0.80$ with 178 items (3.1$\times$ reduction). Three contributions emerge: reproducibility budgets (C1), dominant model$\times$item interaction (C2), and format-associated variance patterns (C3).}
5	\label{fig:overview}
6	\end{figure*}
7	
8	\section{Introduction}
9	\label{sec:introduction}
10	
11	LLM benchmarks are the standard mechanism for comparing language models. Evaluation results determine which models get deployed in production, which attract continued funding, and which top public leaderboards. A typical evaluation runs each model once under a fixed configuration (one prompt template, one random seed, one precision format) and treats the resulting score as a stable measure of model capability. This practice implicitly assumes that these design choices are inconsequential: that a different prompt wording, a different random seed, or a different answer ordering would yield essentially the same result.
12	
13	A growing body of evidence shows otherwise. Prompt reformatting (rewording instructions without altering their meaning) can shift accuracy by up to 76 percentage points \citep{sclar2024formatting, brittlebench2026}. Reordering answer options can reverse model rankings \citep{pezeshkpour2024ordering}. Numerical precision \citep{yuan2025layercast} and random seeds \citep{dodge2020finetuning, bui2025seeds} each contribute additional instability. However, each study examines one source in isolation, holding all others fixed. This pieceme
…[truncated 4276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 841 · 2026-05-25T21:20:30.681813+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 842 · 2026-05-25T21:20:30.882623+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Sources in LLM Evaluation.}
5	\citet{bouthillier2021accounting} introduced ANOVA-based variance decomposition for ML reproducibility, establishing that design choices account for a substantial share of benchmark variance. Subsequent work isolated individual sources: \citet{yuan2025layercast} documented up to 9\% accuracy variation from numerical precision; \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} found 50--76\% accuracy swings from prompt formatting; \citet{pezeshkpour2024ordering} and \citet{bui2025seeds} documented ordering and seed sensitivity. \citet{messina2026background} formalized CUDA nondeterminism from floating-point non-associativity. Each study holds other factors fixed, precluding interaction estimation. \citet{madaan2024quantifying} proposed per-factor metrics without crossing factors; holistic evaluation frameworks \citep{liang2023helm, gao2024lmeval} reduce implementation variance but do not decompose it. Our work crosses seven facets simultaneously, enabling interaction estimation and cross-format comparison (Figure~\ref{fig:method_comparison}).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig_method_comparison}
10	\caption{Scope comparison with prior multi-facet variance studies. Our work uniquely combines broad facet crossing, multi-benchmark coverage, and D-study budget projections.}
11	\label{fig:method_comparison}
12	\end{figure}
13	
14	\paragraph{IRT and Efficient Benchmarking.}
15	IRT models item difficulty and discrimination to optimize benchmark efficiency \citep{lalor2019irt, rodriguez2021leaderboards}. \citet{polo2024tinybenchmarks} and \citet{zhou2026irt} developed IRT-based subsampling for efficient evaluation; \citet{perlitz2023efficient} and \citet{kipnis2025metabench} explored related compression strategies. These approaches optimize item selection but do not model variance from prompt, seed, or ordering 
…[truncated 2040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 843 · 2026-05-25T21:20:30.882977+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 844 · 2026-05-25T21:20:31.284198+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel} = \sum_i \sigma^2_{p \times f_i} / n_{f_i} + \sigma^2_\text{residual} / \prod_i n_{f_i}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. A D-study projects 
…[truncated 8181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 401
}
```

</details>

---


### Tool call

_source line 845 · 2026-05-25T21:20:31.284585+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 846 · 2026-05-25T21:20:31.284827+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	\label{sec:single_model}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_single_model_variance}
11	\caption{Single-model variance decomposition (Llama-3.1-8B, MMLU). Item difficulty dominates (58.4\%); all main facet effects are $<$1\%. Item-conditional interactions total 17.2\%.}
12	\label{fig:single_model_var}
13	\end{figure}
14	
15	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
16	
17	\paragraph{Results.} Item difficulty dominates at 58.4\%, with residual at 23.1\% (Figure~\ref{fig:single_model_var}). All main facet effects are negligible ($<$1\% each); the interesting structure is in item-conditional interactions (17.2\% total), where prompt$\times$item (5.5\%) is largest. The generalizability coefficient $G_\text{item} = 0.936$ (Eq.~\ref{eq:gcoeff}); D-study projection (Eq.~\ref{eq:dstudy}) gives $G \geq 0.80$ with 55 items.
18	
19	For text-exact-match scoring, temperature dominates at 79.7\% and $G_\text{item}$ collapses to 0.007, motivating our exclusive use of binary correctness.
20	
21	\subsection{Cross-Model Variance}
22	
23	Extending to eight models (BF16 subset, 460,800 records), Table~\ref{tab:cross_model} shows that item difficulty drops from 58.4\% to 37.9\%, while model$\times$item interaction emerges at 30.2\% (up to 36\% in MC benchmarks, 15--17\% in FF; \S\ref{sec:format_conditional}). The model main effect is 3--5\% (MC) and 9--11\% (FF)\footnote{Ranges r
…[truncated 12273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool call

_source line 847 · 2026-05-25T21:20:31.535628+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 848 · 2026-05-25T21:20:31.786500+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	The dominant non-residual variance source in LLM evaluation is the model$\times$item interaction (30--36\% in MC, 15--17\% in FF), revealing that models disagree on which items are difficult rather than differing uniformly in overall ability. Multi-facet evaluation designs absorb this interaction: a 3-prompt $\times$ 3-seed protocol achieves $G \geq 0.80$ with 178 MMLU items versus 552 under single-condition, with cross-benchmark budgets of 93--128 items. The variance structure is format-dependent: MC benchmarks concentrate 68--72\% in item-related components while FF benchmarks disperse to 31--41\%, motivating per-format budget calibration. We recommend three practices: adopt multi-facet designs for published results, report item-level accuracy to expose model$\times$item interaction, and calibrate item budgets per benchmark format.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 250
}
```

</details>

---


### Tool call

_source line 849 · 2026-05-25T21:20:31.786853+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 850 · 2026-05-25T21:20:31.987513+00:00_

1	\section*{Limitations}
2	
3	Our design covers eight 7--9B instruction-tuned models; preliminary 72B validation confirms consistent variance structure, but broader scale and temporal coverage is needed. The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$). All D-study budgets assume binary scoring; partial-credit analysis on GSM8K shows $G$ drops from 0.86 to 0.77, suggesting limited transferability to finer-grained rubrics. Benchmark contamination in pretraining data may inflate item accuracy and compress variance; our design does not control for this source.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 200
}
```

</details>

---


### Tool call

_source line 851 · 2026-05-25T21:20:31.987854+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 852 · 2026-05-25T21:20:32.088541+00:00_

1	\appendix
2	
3	\section{Additional Robustness Analyses}
4	\label{app:robustness}
5	
6	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
7	
8	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
9	
10	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
11	
12	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
13	
14	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. Thi
…[truncated 21784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 853 · 2026-05-25T21:20:32.139281+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex"
  }
}
```

</details>

---


### Tool result

_source line 854 · 2026-05-25T21:20:32.139729+00:00_

1	\documentclass[11pt]{article}
2	
3	\usepackage[review]{acl}
4	
5	\usepackage{times}
6	\usepackage{latexsym}
7	\usepackage[T1]{fontenc}
8	\usepackage[utf8]{inputenc}
9	\usepackage{microtype}
10	\usepackage{inconsolata}
11	
12	\usepackage{graphicx}
13	\usepackage{amsmath,amssymb}
14	\usepackage{booktabs}
15	\usepackage{multirow}
16	
17	\graphicspath{{../../figures/paper/}}
18	
19	\title{Reproducibility Budgets for Open-Weight LLM Evaluation:\\A Generalizability Theory Study of 7--9B Instruction-Tuned Models}
20	
21	\author{Anonymous}
22	
23	\begin{document}
24	\maketitle
25	
26	\begin{abstract}
27	\input{abstract}
28	\end{abstract}
29	
30	% === INTRODUCTION ===
31	\input{introduction}
32	
33	% === RELATED WORK ===
34	\input{related_work}
35	
36	% === METHOD ===
37	\input{method}
38	
39	% === EXPERIMENTS ===
40	\input{experiments}
41	
42	% === CONCLUSION ===
43	\enlargethispage{1\baselineskip}
44	\input{conclusion}
45	
46	% === LIMITATIONS ===
47	\input{limitations}
48	
49	\bibliography{references}
50	
51	% === APPENDIX ===
52	\input{appendix}
53	
54	\end{document}
55	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 0
}
```

</details>

---


### Tool result

_source line 855 · 2026-05-25T21:20:55.785488+00:00_

I have successfully read all the LaTeX source files for the paper. Here is the complete content organized by section:

## Paper: Reproducibility Budgets for Open-Weight LLM Evaluation

### **Main.tex**
The document class uses ACL 11pt article format with standard ML paper packages. Title: "Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Study of 7--9B Instruction-Tuned Models". Files are imported via \input{} commands.

### **Abstract.tex**
Establishes that design choices (prompt template, random seed, numerical precision, answer ordering) significantly impact LLM evaluation. Key finding: model×item interaction dominates variance (30--36% in multiple-choice, 15--17% in free-form). Multi-facet designs reduce item requirements from 1,000+ to ~100. Introduces open-source G-theory pipeline.

### **Introduction.tex**
Opens with benchmark importance for model deployment and funding decisions. States implicit assumption that design choices are inconsequential, then refutes with evidence (prompt can shift accuracy 76pp, answer ordering reverses rankings). Notes piecemeal studies examine single sources in isolation. Proposes G-theory as unified framework. Makes three contributions:
1. Design-dependent reproducibility budgets (up to 10× reduction)
2. Dominant model×item interaction (7--11× larger than model main effect in MC)
3. Format-associated variance patterns (68--72% in MC vs 31--41% in free-form)

### **Related_work.tex**
Four subsections:
- **Variance Sources**: Reviews ANOVA-based decomposition (Bouthillier 2021), individual source isolation studies, notes IRT-based approaches optimize items but don't model prompt/seed/ordering variance
- **IRT and Efficient Benchmarking**: Discusses item efficiency optimization but notes it treats prompt/seed as fixed, leaving variance unmodeled
- **G-Theory Positioning**: Positions work relative to Messing 2026 (extends from 1 benchmark to 5, adds infrastructure facets, provides D-study budgets)
- 
…[truncated 3772 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Agent",
  "elapsed_ms": 32187
}
```

</details>

---


### Tool call

_source line 856 · 2026-05-25T21:21:02.062911+00:00_

called Glob

<details open><summary>🔧 Tool call — Glob</summary>

```json
{
  "pattern": "*.tex",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Glob",
  "tool_args": {
    "pattern": "*.tex",
    "path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper"
  }
}
```

</details>

---


### Tool result

_source line 857 · 2026-05-25T21:21:02.113477+00:00_

/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/main.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex
/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Glob",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 858 · 2026-05-25T21:21:05.930020+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex"
  }
}
```

</details>

---


### Tool result

_source line 859 · 2026-05-25T21:21:06.432293+00:00_

1	LLM benchmarks are the primary tool for comparing language models, guiding decisions about deployment, funding, and public rankings. Every evaluation involves design choices (prompt template, random seed, numerical precision, answer ordering) that are typically fixed to a single value and assumed inconsequential. Growing evidence challenges this assumption: prompt formatting alone can shift accuracy by up to 76 percentage points, and answer ordering can flip model rankings. Yet each study examines one factor in isolation, leaving unanswered which sources dominate when all vary simultaneously, and how many test items are truly needed for reliable measurement. We address this using Generalizability theory, a psychometric framework for multi-source variance decomposition. In a factorial experiment crossing seven facets across eight open-weight models and five benchmarks (2.3M binary records), we find that the dominant non-residual variance source is not the prompt or the seed but the model$\times$item interaction (30--36\% in multiple-choice benchmarks, 15--17\% in free-form), meaning models disagree on which items are difficult rather than in overall ability. Multi-facet designs absorb this noise, reducing item requirements from over 1,000 to roughly 100. The variance structure is format-dependent: item factors dominate multiple-choice benchmarks but disperse in free-form tasks. We release an open-source G-theory pipeline and D-study calculator\footnote{Code and data are available at \url{https://anonymous.4open.science/r/nlp_variance_gtheory-11E1/}.}.
2	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 860 · 2026-05-25T21:21:06.432808+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 861 · 2026-05-25T21:21:06.884211+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	The dominant non-residual variance source in LLM evaluation is the model$\times$item interaction (30--36\% in MC, 15--17\% in FF), revealing that models disagree on which items are difficult rather than differing uniformly in overall ability. Multi-facet evaluation designs absorb this interaction: a 3-prompt $\times$ 3-seed protocol achieves $G \geq 0.80$ with 178 MMLU items versus 552 under single-condition, with cross-benchmark budgets of 93--128 items. The variance structure is format-dependent: MC benchmarks concentrate 68--72\% in item-related components while FF benchmarks disperse to 31--41\%, motivating per-format budget calibration. We recommend three practices: adopt multi-facet designs for published results, report item-level accuracy to expose model$\times$item interaction, and calibrate item budgets per benchmark format.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 862 · 2026-05-25T21:21:06.884580+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/limitations.tex"
  }
}
```

</details>

---


### Tool result

_source line 863 · 2026-05-25T21:21:07.485991+00:00_

1	\section*{Limitations}
2	
3	Our design covers eight 7--9B instruction-tuned models; preliminary 72B validation confirms consistent variance structure, but broader scale and temporal coverage is needed. The benchmark sample ($n = 5$) limits statistical power for format-associated observations ($p = 0.10$). All D-study budgets assume binary scoring; partial-credit analysis on GSM8K shows $G$ drops from 0.86 to 0.77, suggesting limited transferability to finer-grained rubrics. Benchmark contamination in pretraining data may inflate item accuracy and compress variance; our design does not control for this source.
4	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 601
}
```

</details>

---


### Tool call

_source line 864 · 2026-05-25T21:21:07.486444+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/introduction.tex"
  }
}
```

</details>

---


### Tool result

_source line 865 · 2026-05-25T21:21:07.637112+00:00_

1	\begin{figure*}[t]
2	\centering
3	\includegraphics[width=\textwidth]{fig_overview_pipeline}
4	\caption{Overview of the G-theory evaluation pipeline. A factorial design crossing seven facets across eight models and five benchmarks produces 2.3M binary records. G-study variance decomposition via Henderson Method~I reveals that model$\times$item interaction accounts for up to 36\% of variance. D-study projections translate variance components into design-dependent item budgets: a 3-prompt $\times$ 3-seed design achieves $G \geq 0.80$ with 178 items (3.1$\times$ reduction). Three contributions emerge: reproducibility budgets (C1), dominant model$\times$item interaction (C2), and format-associated variance patterns (C3).}
5	\label{fig:overview}
6	\end{figure*}
7	
8	\section{Introduction}
9	\label{sec:introduction}
10	
11	LLM benchmarks are the standard mechanism for comparing language models. Evaluation results determine which models get deployed in production, which attract continued funding, and which top public leaderboards. A typical evaluation runs each model once under a fixed configuration (one prompt template, one random seed, one precision format) and treats the resulting score as a stable measure of model capability. This practice implicitly assumes that these design choices are inconsequential: that a different prompt wording, a different random seed, or a different answer ordering would yield essentially the same result.
12	
13	A growing body of evidence shows otherwise. Prompt reformatting (rewording instructions without altering their meaning) can shift accuracy by up to 76 percentage points \citep{sclar2024formatting, brittlebench2026}. Reordering answer options can reverse model rankings \citep{pezeshkpour2024ordering}. Numerical precision \citep{yuan2025layercast} and random seeds \citep{dodge2020finetuning, bui2025seeds} each contribute additional instability. However, each study examines one source in isolation, holding all others fixed. This pieceme
…[truncated 4276 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 150
}
```

</details>

---


### Tool call

_source line 866 · 2026-05-25T21:21:14.613607+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex"
  }
}
```

</details>

---


### Tool result

_source line 867 · 2026-05-25T21:21:15.116128+00:00_

1	\section{Experiments}
2	
3	All experiments use open-weight 7--9B parameter models evaluated with vLLM~0.9.2 on a single NVIDIA RTX PRO 6000 GPU (96GB) with binary correctness scoring.
4	
5	\subsection{Single-Model Baseline}
6	\label{sec:single_model}
7	
8	\begin{figure}[t]
9	\centering
10	\includegraphics[width=\columnwidth]{fig_single_model_variance}
11	\caption{Single-model variance decomposition (Llama-3.1-8B, MMLU). Item difficulty dominates (58.4\%); all main facet effects are $<$1\%. Item-conditional interactions total 17.2\%.}
12	\label{fig:single_model_var}
13	\end{figure}
14	
15	\paragraph{Design.} The G-study crosses six facets: 200 items $\times$ 3 numerical precisions (BF16, FP16, FP32) $\times$ 6 prompt templates $\times$ 6 random seeds $\times$ 3 temperature levels (0.0, 0.3, 0.7) $\times$ 4 answer orderings, yielding 259,200 binary observations. Variance components are estimated via Henderson Method~I with bootstrap confidence intervals (1,000 resamples).
16	
17	\paragraph{Results.} Item difficulty dominates at 58.4\%, with residual at 23.1\% (Figure~\ref{fig:single_model_var}). All main facet effects are negligible ($<$1\% each); the interesting structure is in item-conditional interactions (17.2\% total), where prompt$\times$item (5.5\%) is largest. The generalizability coefficient $G_\text{item} = 0.936$ (Eq.~\ref{eq:gcoeff}); D-study projection (Eq.~\ref{eq:dstudy}) gives $G \geq 0.80$ with 55 items.
18	
19	For text-exact-match scoring, temperature dominates at 79.7\% and $G_\text{item}$ collapses to 0.007, motivating our exclusive use of binary correctness.
20	
21	\subsection{Cross-Model Variance}
22	
23	Extending to eight models (BF16 subset, 460,800 records), Table~\ref{tab:cross_model} shows that item difficulty drops from 58.4\% to 37.9\%, while model$\times$item interaction emerges at 30.2\% (up to 36\% in MC benchmarks, 15--17\% in FF; \S\ref{sec:format_conditional}). The model main effect is 3--5\% (MC) and 9--11\% (FF)\footnote{Ranges r
…[truncated 12273 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 502
}
```

</details>

---


### Tool call

_source line 868 · 2026-05-25T21:21:15.116508+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/method.tex"
  }
}
```

</details>

---


### Tool result

_source line 869 · 2026-05-25T21:21:15.668625+00:00_

1	\section{Method and Experimental Design}
2	\label{sec:method}
3	
4	\subsection{Generalizability Theory}
5	\label{sec:gtheory}
6	
7	Generalizability theory (G-theory) treats each measurement as one observation from a universe of admissible conditions defined by the crossed facets of an evaluation design \cite{shavelson1991generalizability, brennan2001generalizability}. The \emph{object of measurement} is the entity whose consistency is of interest. In our setting, test items ($p$) serve as the object of measurement, and the goal is to determine how reliably item-level scores generalize across the methodological conditions under which they are collected.
8	
9	A \emph{G-study} decomposes total observed variance into components $\sigma^2_x$ for each facet $x$ and their interactions. Each component quantifies how much variability that source contributes to the overall measurement. Large interaction components (e.g., $\sigma^2_{pM}$ for item-by-model) indicate that facets do not affect items uniformly but instead create differential difficulty profiles. We estimate variance components via Henderson Method~I, an unbiased ANOVA-based estimator for balanced designs \cite[Ch.~3]{brennan2001generalizability}, with 1,000-resample bootstrap confidence intervals \cite{efron1993bootstrap} (item-level resampling with replacement, preserving the fully-crossed structure across all other facets) \cite{li2023bootstrap}.
10	
11	A \emph{D-study} projects the generalizability coefficient under hypothetical designs with different numbers of conditions per facet:
12	\begin{equation}
13	G_\text{item} = \frac{\sigma^2_p}{\sigma^2_p + \sigma^2_\text{rel}}
14	\label{eq:gcoeff}
15	\end{equation}
16	where $\sigma^2_\text{rel} = \sum_i \sigma^2_{p \times f_i} / n_{f_i} + \sigma^2_\text{residual} / \prod_i n_{f_i}$ aggregates all item-by-facet interaction variances, each divided by the number of conditions for the corresponding facets \cite[Ch.~4]{brennan2001generalizability}. A D-study projects 
…[truncated 8181 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 870 · 2026-05-25T21:21:15.669104+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/related_work.tex"
  }
}
```

</details>

---


### Tool result

_source line 871 · 2026-05-25T21:21:15.769561+00:00_

1	\section{Related Work}
2	\label{sec:related}
3	
4	\paragraph{Variance Sources in LLM Evaluation.}
5	\citet{bouthillier2021accounting} introduced ANOVA-based variance decomposition for ML reproducibility, establishing that design choices account for a substantial share of benchmark variance. Subsequent work isolated individual sources: \citet{yuan2025layercast} documented up to 9\% accuracy variation from numerical precision; \citet{sclar2024formatting} and BrittleBench \citep{brittlebench2026} found 50--76\% accuracy swings from prompt formatting; \citet{pezeshkpour2024ordering} and \citet{bui2025seeds} documented ordering and seed sensitivity. \citet{messina2026background} formalized CUDA nondeterminism from floating-point non-associativity. Each study holds other factors fixed, precluding interaction estimation. \citet{madaan2024quantifying} proposed per-factor metrics without crossing factors; holistic evaluation frameworks \citep{liang2023helm, gao2024lmeval} reduce implementation variance but do not decompose it. Our work crosses seven facets simultaneously, enabling interaction estimation and cross-format comparison (Figure~\ref{fig:method_comparison}).
6	
7	\begin{figure}[t]
8	\centering
9	\includegraphics[width=\columnwidth]{fig_method_comparison}
10	\caption{Scope comparison with prior multi-facet variance studies. Our work uniquely combines broad facet crossing, multi-benchmark coverage, and D-study budget projections.}
11	\label{fig:method_comparison}
12	\end{figure}
13	
14	\paragraph{IRT and Efficient Benchmarking.}
15	IRT models item difficulty and discrimination to optimize benchmark efficiency \citep{lalor2019irt, rodriguez2021leaderboards}. \citet{polo2024tinybenchmarks} and \citet{zhou2026irt} developed IRT-based subsampling for efficient evaluation; \citet{perlitz2023efficient} and \citet{kipnis2025metabench} explored related compression strategies. These approaches optimize item selection but do not model variance from prompt, seed, or ordering 
…[truncated 2040 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 872 · 2026-05-25T21:24:44.635841+00:00_

called Bash

<details open><summary>🔧 Tool call — Bash</summary>

```json
{
  "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex | sed 's/\\\\footnote{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g' | sed 's/[{}$~]//g' | wc -w",
  "description": "Count words in abstract excluding LaTeX commands and footnotes"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Bash",
  "tool_args": {
    "command": "cat /home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/abstract.tex | sed 's/\\\\footnote{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*{[^}]*}//g' | sed 's/\\\\[a-zA-Z]*//g' | sed 's/[{}$~]//g' | wc -w",
    "description": "Count words in abstract excluding LaTeX commands and footnotes"
  }
}
```

</details>

---


### Tool result

_source line 873 · 2026-05-25T21:24:44.736581+00:00_

201

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Bash",
  "elapsed_ms": 100
}
```

</details>

---


### Tool call

_source line 874 · 2026-05-25T21:27:11.159823+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 审稿意见 — Round 11 (新颖性 + 完整性 + 写作质量)\n\n## Summary\n\n本文将 Generalizability theory (G-theory) 应用于 LLM 评测方差分解，在 8 个 7–9B 指令微调模型和 5 个 benchmark 上交叉 7 个设计因子（共 2.3M 二值记录），发现 model×item 交互是主导非残差方差源（MC 30–36%，FF 15–17%），多因子设计可将所需 item 数从 500+ 降至 ~100（G ≥ 0.80），MC/FF 格式呈现不同的方差结构。论文提供开源 G-theory 流水线和 D-study 计算器。方法论扎实、鲁棒性验证全面，但在关键 framing 和 scope 声明上存在需要修正的问题。\n\n---\n\n## Strengths\n\n**S1: 实验规模与系统性**\n7 facets × 8 models × 5 benchmarks 的全交叉设计是对 Messing (2026)（5 facets × 1 benchmark）的实质性扩展。2.3M 二值记录为方差分解提供了高置信度估计。\n\n**S2: D-study 预算 — 最具实用价值的贡献**\n将方差分解转化为可操作的 item 预算建议（Table 7, 8, 9），特别是推荐的 3-prompt × 3-seed 设计（178 items, §4.5）给出了平衡成本和可靠性的具体方案。IRT+G-theory 正交互补性（Table 7: IRT 116 items 在 single-condition 下 G=0.457，multi-facet 下 G=0.895）是一个新颖且有说服力的结果。\n\n**S3: 鲁棒性分析堪称典范**\nAppendix A 覆盖了 GLMM complement (ρ=1.0)、accuracy-range stability、Henderson vs REML (<0.5pp)、probit simulation、LOMO (Table 4, CV ≤ 1.25%)、inter-model κ (0.33–0.46)、scoring metric sensitivity 等 9 项检验。这种系统性验证在 NLP 论文中不多见。\n\n**S4: 方法论透明度**\nHenderson Method I 选择的合理性（balanced designs + binary data, §3.5）、notation 清晰（footnote 5）、设计矩阵完整（Table 2）、代码公开。quasi-random facet 处理（§3.6）的 fixed vs. random 对比（G 增加 0.077–0.113）增加了透明度。\n\n**S5: IRT 互补性揭示了一个被忽视的维度**\nTable 7 中 IRT baseline 一行（G=0.457 → 0.895）是全文最有说服力的单一结果，说明 item selection 和 protocol optimization 是独立的优化维度。这对 benchmark 开发者有直接的方法论启示。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical]: \"10× fewer items\" framing 隐藏了 total evaluations 的剧增**\n- Abstract: \"reducing item requirements from over 1,000 to roughly 100\" — 仅描述 item 维度的缩减\n- 实际情况：full multi-facet (1,296 conditions) 下 item 从 552→55（10×），但 total evaluations 从 552→71,280（**129× 增长**）\n- 推荐的 3×3 设计虽然在 §4.5 披露了 \"2.9× total-evaluation increase for a 3.1× item reduction\"，但 abstract 和 Figure 1 overview 都只呈现了 item 维度\n- Title 用 \"Reproducibility Budgets\" 暗示效率提升，但对多数用户而言总计算量才是关键成本\n- **建议**: Abstract 中应同时报告 item reduction 和 total evaluation overhead（至少对推荐的 3×3 设计）\n\n**W2 [critical]: Binary scoring scope 未在 title/abstract 中充分限定**\n- Title: \"Reproducibility Budgets for Open-Weight LLM Evaluation\" — 暗示适用于一般 LLM 评测\n- 但所有发现严格受限于 binary correctness scoring（§3.5）\n- Text-exact-match: G 从 0.936 崩溃到 0.007（§4.1）— 方差结构完全改变\n- Partial-credit (GSM8K): G 从 0.86 降至 0.77（§3.5）— 显著退化\n- 对于实际评测场景（code generation、open-ended QA、rubric-based evaluation），binary scoring 是例外而非常态\n- **建议**: Title 添加限定语（如 \"under Binary Correctness Scoring\"），或 abstract 明确声明 scope\n\n**W3 [critical]: G_item 与 model ranking reliability 之间的概念鸿沟**\n- 论文以 items (p) 为 object of measurement（§3.1），计算 G_item 衡量 item-level 跨条件泛化能力\n- 但 benchmark 用户关心的是 model ranking reliability: \"用 178 items 排出的模型顺序是否可重复？\"\n- G_item ≥ 0.80 保证 item scores 在不同 prompt/seed 下一致，但不直接等同于 model ranking 稳定\n  - 如果所有 model 的 item profile 高度相似但绝对分数接近，高 G_item 仍可能对应不稳定的排名\n- 论文提供了间接证据（LOMO Table 4, κ=0.33–0.46），但未直接计算 rank-order stability 或 G_model\n- **建议**: 增加 model ranking stability 分析（如 Kendall's W 或 bootstrap 排名一致性），或至少讨论 G_item 向 model ranking reliability 的映射条件\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [warning]: §4.3 format-associated patterns 占比失衡**\n- 探索性发现（n=5, permutation p=0.10, benchmark-level CI spans zero）在 8 页正文中占约 1 页（文本 + Table 6 + Figure 7 + Figure 8）\n- 贡献 C3 在 Introduction 中与 C1、C2 并列，但证据强度远不如前两者\n- **建议**: 压缩 §4.3 为一段描述，将 Figure 7 和 Figure 8 移入 appendix；或降低 C3 在 Introduction 中的权重（如标注 \"preliminary\" 或移入 Discussion）\n\n**W5 [warning]: Table 6 caption 中 MC vs FF 不同量的标注易造成混淆**\n- \"prompt†\" 行对 MC 报告 prompt×item interaction，对 FF 报告 prompt main effect\n- 同一行代表不同统计量，读者自然期望同一行表示相同概念\n- Caption 用 † 标注但解释较复杂：\"For MC, reports prompt×item interaction (prompt main effect <1%); for FF, reports prompt main effect (item-conditional interactions absorbed into residual)\"\n- **建议**: 分开两行（prompt_main, prompt×item），或用不同符号/颜色区分\n\n**W6 [warning]: Conclusion (§5) 过于简短，缺乏 practical implications 和 adoption pathway**\n- 全文仅 4 句话，实质是 findings summary 的压缩版\n- 缺失内容：\n  - 对 benchmark 开发者的具体采纳建议（如 \"在 lm-eval-harness 中集成 G-theory pipeline 需要哪些步骤\"）\n  - 对 leaderboard 维护者的实际影响\n  - Future work（larger models、partial-credit scoring、temporal stability）\n  - 与 IRT pipeline 的集成路径\n- 对于一篇提出可操作 \"reproducibility budgets\" 的论文，缺乏 adoption 讨论是显著不足\n\n**W7 [warning]: Partial-credit transferability 仅在 GSM8K 单一 benchmark 上验证**\n- §3.5 声称 partial-credit 下 G 从 0.86 降至 0.77 (ΔG = −0.135)\n- 但仅 GSM8K 一个 benchmark，且使用特定的 step-level partial credit 方案\n- Code evaluation、open-ended generation、rubric-based scoring 可能呈现完全不同的模式\n- **建议**: 明确声明 \"在 GSM8K 的 step-level partial credit 下初步观察到\"，而非泛化为 \"limited transferability to finer-grained rubrics\"\n\n**W8 [warning]: 遗漏重要相关文献**\n- **MMLU-Redux** (Gema et al., 2024): 识别 MMLU 中错误标注和歧义 items，直接影响本文基于 200 MMLU items 的方差分解解释\n- **MMLU-Pro** (Wang et al., 2024): 扩展版 MMLU，10 选项设计降低了 guessing variance\n- **Contamination 文献**: Limitations 提到 contamination 但未引用任何检测/测量论文（如 Shi et al. 2023, Golchin & Surdeanu 2024）\n- 遗漏 MMLU-Redux 影响论文可信度：如果部分 MMLU items 本身有标注错误，item difficulty 的方差分解可能混入了数据质量伪影\n\n### Minor（不影响接收）\n\n**W9 [minor]: Abstract 约 201 词，略超 EMNLP 2026 的 200 词限制**\n- 通过 LaTeX 命令去除后统计为 201 词。需微调删减 1–5 词。\n\n**W10 [minor]: Abstract 数值密度过高（20+ 数值），影响可读性**\n- 包含 \"30–36%\"、\"15–17%\"、\"2.3M\"、\"76 percentage points\"、\"7–9B\"、\"1,000\"、\"100\"、\"seven facets\"、\"eight models\"、\"five benchmarks\" 等\n- 建议保留最核心的 2–3 个数值（model×item 占比、item reduction ratio），其余用定性描述\n\n**W11 [minor]: main.tex line 43 使用 `\\enlargethispage{1\\baselineskip}` 微调页面容量**\n- 虽然仅增加一行，但可能引起格式审查关注\n\n**W12 [minor]: Table 1 (Positioning) 与 Messing (2026) 的对比需注明 facet 差异**\n- Messing 的最大方差源是 judge identity (43.8%)，属于 LLM-as-judge 评测范式\n- 本文使用 generation-based scoring，替换了 judge identity 为 infrastructure facets\n- 两者研究的评测范式不同，简单的 facet 数量对比（5 vs 7）可能高估增量贡献\n\n---\n\n## Questions\n\n**Q1**: 为什么选择 items 而非 models 作为 object of measurement？如果目标是判断哪个模型最好，G_model 是否更直接？G_item ≥ 0.80 在什么条件下能保证 model ranking stability？\n\n**Q2**: 推荐的 3×3 设计（3 prompts × 3 seeds = 9 conditions × 178 items = 1,602 evaluations）在单 GPU 上的实际墙钟时间是多少？对需要评估大量模型的 benchmark leaderboard 是否可行？\n\n**Q3**: 200 items 通过 stratified sampling 选取。方差分解对特定 item 样本的敏感度如何？不同的 200-item 样本是否会产生类似的 G_item？（Appendix A 中的 bootstrap CI 是 item-level resampling，但不等同于完全独立的 item sample。）\n\n**Q4**: Table 1 中与 Messing (2026) 的对比是否公平？Messing 研究的是 LLM-as-judge 场景（judge identity 43.8%），本文研究的是 generation-based scoring。两者的 facet 集合和评测范式不同，仅用 facet 数量和 benchmark 数量对比是否过于简化？\n\n**Q5**: 对于 model facet 的 quasi-random 处理（§3.6），8 个模型是 deliberate selection 而非 random sampling from a population。这一处理的合理性在什么条件下成立？如果模型更新换代（如 2026 年新一代模型），G-study 结果是否仍然适用？\n\n---\n\n## Missing References\n\n1. **MMLU-Redux** (Gema et al., 2024) — 识别 MMLU 错误标注，直接影响 item-level 方差分解解读\n2. **MMLU-Pro** (Wang et al., 2024) — 10 选项 MMLU 变体，降低 guessing variance\n3. **Contamination 检测文献** (如 Shi et al. 2023, Golchin & Surdeanu 2024) — Limitations 提到 contamination 但未引用相关工作\n4. **Evaluation harness 标准化的持续努力** — 论文引用了 lm-eval-harness 但未讨论标准化 harness 如何与本文的 protocol optimization 建议对接\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论扎实，鲁棒性验证全面（S3），但 G_item→model ranking gap（W3）和 binary scope 未充分限定（W2）削弱了实际推论的可靠性 |\n| **Excitement** | 3.0/5 | 对 Messing (2026) 的扩展有价值但主要是 incremental（更多 facets、更多 benchmarks、D-study）；D-study 预算和 IRT 互补性（S2, S5）是最引人注目的贡献 |\n| **Reproducibility** | 4/5 | 匿名代码仓库、详尽的实验设置、Henderson Method I 充分文档化、binary data validation 完善 |\n| **Datasets** | 4/5 | 2.3M 记录的 factorial 数据集对 evaluation methodology 研究社区有价值 |\n| **Software** | 4/5 | 开源 G-theory pipeline 和 D-study calculator 可被复用 |\n| **Reviewer Confidence** | 4/5 | 熟悉 G-theory、psychometrics in NLP、LLM evaluation 文献。仔细阅读了全文和所有 appendix |\n| **Author Identity** | 1/5 | 无法判断作者身份 |\n\n### Overall: **3.5** (Borderline Conference)\n\n**一句话总结**: 方法论扎实、实验规模可观的增量贡献——D-study 预算和 IRT 互补性是最具价值的新发现，但 binary scoring 的 scope 限制、\"10× fewer items\" 的 framing 误导、以及 G_item 与 model ranking reliability 之间的概念鸿沟需要在修订中解决。\n\n**详细理由**: 本文在 Messing (2026) 基础上做了三个方向的扩展（infrastructure facets、cross-benchmark、D-study budgets），其中 D-study 预算是最具实用价值的贡献（S2），IRT 互补性发现（S5）对 benchmark 开发有直接启示。鲁棒性分析（S3）达到了高标准。然而：(1) G_item 与 model ranking reliability 之间缺乏直接桥接（W3），使得 \"reproducibility budgets\" 的实际含义不够清晰；(2) abstract 和 title 的 framing 在 scope（W2: binary scoring only）和效率（W1: total evaluations 增长）两个维度上产生误导；(3) 格式相关发现 C3 证据不足但占篇幅过大（W4）。如果 W1–W3 得到充分修订（特别是增加 model ranking stability 分析和 scope 限定），本文可达到 Conference 水平。当前版本是 strong Findings candidate。\n",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 审稿意见 — Round 11 (新颖性 + 完整性 + 写作质量)\n\n## Summary\n\n本文将 Generalizability theory (G-theory) 应用于 LLM 评测方差分解，在 8 个 7–9B 指令微调模型和 5 个 benchmark 上交叉 7 个设计因子（共 2.3M 二值记录），发现 model×item 交互是主导非残差方差源（MC 30–36%，FF 15–17%），多因子设计可将所需 item 数从 500+ 降至 ~100（G ≥ 0.80），MC/FF 格式呈现不同的方差结构。论文提供开源 G-theory 流水线和 D-study 计算器。方法论扎实、鲁棒性验证全面，但在关键 framing 和 scope 声明上存在需要修正的问题。\n\n---\n\n## Strengths\n\n**S1: 实验规模与系统性**\n7 facets × 8 models × 5 benchmarks 的全交叉设计是对 Messing (2026)（5 facets × 1 benchmark）的实质性扩展。2.3M 二值记录为方差分解提供了高置信度估计。\n\n**S2: D-study 预算 — 最具实用价值的贡献**\n将方差分解转化为可操作的 item 预算建议（Table 7, 8, 9），特别是推荐的 3-prompt × 3-seed 设计（178 items, §4.5）给出了平衡成本和可靠性的具体方案。IRT+G-theory 正交互补性（Table 7: IRT 116 items 在 single-condition 下 G=0.457，multi-facet 下 G=0.895）是一个新颖且有说服力的结果。\n\n**S3: 鲁棒性分析堪称典范**\nAppendix A 覆盖了 GLMM complement (ρ=1.0)、accuracy-range stability、Henderson vs REML (<0.5pp)、probit simulation、LOMO (Table 4, CV ≤ 1.25%)、inter-model κ (0.33–0.46)、scoring metric sensitivity 等 9 项检验。这种系统性验证在 NLP 论文中不多见。\n\n**S4: 方法论透明度**\nHenderson Method I 选择的合理性（balanced designs + binary data, §3.5）、notation 清晰（footnote 5）、设计矩阵完整（Table 2）、代码公开。quasi-random facet 处理（§3.6）的 fixed vs. random 对比（G 增加 0.077–0.113）增加了透明度。\n\n**S5: IRT 互补性揭示了一个被忽视的维度**\nTable 7 中 IRT baseline 一行（G=0.457 → 0.895）是全文最有说服力的单一结果，说明 item selection 和 protocol optimization 是独立的优化维度。这对 benchmark 开发者有直接的方法论启示。\n\n---\n\n## Weaknesses\n\n### Must-Fix（影响接收决定）\n\n**W1 [critical]: \"10× fewer items\" framing 隐藏了 total evaluations 的剧增**\n- Abstract: \"reducing item requirements from over 1,000 to roughly 100\" — 仅描述 item 维度的缩减\n- 实际情况：full multi-facet (1,296 conditions) 下 item 从 552→55（10×），但 total evaluations 从 552→71,280（**129× 增长**）\n- 推荐的 3×3 设计虽然在 §4.5 披露了 \"2.9× total-evaluation increase for a 3.1× item reduction\"，但 abstract 和 Figure 1 overview 都只呈现了 item 维度\n- Title 用 \"Reproducibility Budgets\" 暗示效率提升，但对多数用户而言总计算量才是关键成本\n- **建议**: Abstract 中应同时报告 item reduction 和 total evaluation overhead（至少对推荐的 3×3 设计）\n\n**W2 [critical]: Binary scoring scope 未在 title/abstract 中充分限定**\n- Title: \"Reproducibility Budgets for Open-Weight LLM Evaluation\" — 暗示适用于一般 LLM 评测\n- 但所有发现严格受限于 binary correctness scoring（§3.5）\n- Text-exact-match: G 从 0.936 崩溃到 0.007（§4.1）— 方差结构完全改变\n- Partial-credit (GSM8K): G 从 0.86 降至 0.77（§3.5）— 显著退化\n- 对于实际评测场景（code generation、open-ended QA、rubric-based evaluation），binary scoring 是例外而非常态\n- **建议**: Title 添加限定语（如 \"under Binary Correctness Scoring\"），或 abstract 明确声明 scope\n\n**W3 [critical]: G_item 与 model ranking reliability 之间的概念鸿沟**\n- 论文以 items (p) 为 object of measurement（§3.1），计算 G_item 衡量 item-level 跨条件泛化能力\n- 但 benchmark 用户关心的是 model ranking reliability: \"用 178 items 排出的模型顺序是否可重复？\"\n- G_item ≥ 0.80 保证 item scores 在不同 prompt/seed 下一致，但不直接等同于 model ranking 稳定\n  - 如果所有 model 的 item profile 高度相似但绝对分数接近，高 G_item 仍可能对应不稳定的排名\n- 论文提供了间接证据（LOMO Table 4, κ=0.33–0.46），但未直接计算 rank-order stability 或 G_model\n- **建议**: 增加 model ranking stability 分析（如 Kendall's W 或 bootstrap 排名一致性），或至少讨论 G_item 向 model ranking reliability 的映射条件\n\n### Should-Fix（影响评分但不一票否决）\n\n**W4 [warning]: §4.3 format-associated patterns 占比失衡**\n- 探索性发现（n=5, permutation p=0.10, benchmark-level CI spans zero）在 8 页正文中占约 1 页（文本 + Table 6 + Figure 7 + Figure 8）\n- 贡献 C3 在 Introduction 中与 C1、C2 并列，但证据强度远不如前两者\n- **建议**: 压缩 §4.3 为一段描述，将 Figure 7 和 Figure 8 移入 appendix；或降低 C3 在 Introduction 中的权重（如标注 \"preliminary\" 或移入 Discussion）\n\n**W5 [warning]: Table 6 caption 中 MC vs FF 不同量的标注易造成混淆**\n- \"prompt†\" 行对 MC 报告 prompt×item interaction，对 FF 报告 prompt main effect\n- 同一行代表不同统计量，读者自然期望同一行表示相同概念\n- Caption 用 † 标注但解释较复杂：\"For MC, reports prompt×item interaction (prompt main effect <1%); for FF, reports prompt main effect (item-conditional interactions absorbed into residual)\"\n- **建议**: 分开两行（prompt_main, prompt×item），或用不同符号/颜色区分\n\n**W6 [warning]: Conclusion (§5) 过于简短，缺乏 practical implications 和 adoption pathway**\n- 全文仅 4 句话，实质是 findings summary 的压缩版\n- 缺失内容：\n  - 对 benchmark 开发者的具体采纳建议（如 \"在 lm-eval-harness 中集成 G-theory pipeline 需要哪些步骤\"）\n  - 对 leaderboard 维护者的实际影响\n  - Future work（larger models、partial-credit scoring、temporal stability）\n  - 与 IRT pipeline 的集成路径\n- 对于一篇提出可操作 \"reproducibility budgets\" 的论文，缺乏 adoption 讨论是显著不足\n\n**W7 [warning]: Partial-credit transferability 仅在 GSM8K 单一 benchmark 上验证**\n- §3.5 声称 partial-credit 下 G 从 0.86 降至 0.77 (ΔG = −0.135)\n- 但仅 GSM8K 一个 benchmark，且使用特定的 step-level partial credit 方案\n- Code evaluation、open-ended generation、rubric-based scoring 可能呈现完全不同的模式\n- **建议**: 明确声明 \"在 GSM8K 的 step-level partial credit 下初步观察到\"，而非泛化为 \"limited transferability to finer-grained rubrics\"\n\n**W8 [warning]: 遗漏重要相关文献**\n- **MMLU-Redux** (Gema et al., 2024): 识别 MMLU 中错误标注和歧义 items，直接影响本文基于 200 MMLU items 的方差分解解释\n- **MMLU-Pro** (Wang et al., 2024): 扩展版 MMLU，10 选项设计降低了 guessing variance\n- **Contamination 文献**: Limitations 提到 contamination 但未引用任何检测/测量论文（如 Shi et al. 2023, Golchin & Surdeanu 2024）\n- 遗漏 MMLU-Redux 影响论文可信度：如果部分 MMLU items 本身有标注错误，item difficulty 的方差分解可能混入了数据质量伪影\n\n### Minor（不影响接收）\n\n**W9 [minor]: Abstract 约 201 词，略超 EMNLP 2026 的 200 词限制**\n- 通过 LaTeX 命令去除后统计为 201 词。需微调删减 1–5 词。\n\n**W10 [minor]: Abstract 数值密度过高（20+ 数值），影响可读性**\n- 包含 \"30–36%\"、\"15–17%\"、\"2.3M\"、\"76 percentage points\"、\"7–9B\"、\"1,000\"、\"100\"、\"seven facets\"、\"eight models\"、\"five benchmarks\" 等\n- 建议保留最核心的 2–3 个数值（model×item 占比、item reduction ratio），其余用定性描述\n\n**W11 [minor]: main.tex line 43 使用 `\\enlargethispage{1\\baselineskip}` 微调页面容量**\n- 虽然仅增加一行，但可能引起格式审查关注\n\n**W12 [minor]: Table 1 (Positioning) 与 Messing (2026) 的对比需注明 facet 差异**\n- Messing 的最大方差源是 judge identity (43.8%)，属于 LLM-as-judge 评测范式\n- 本文使用 generation-based scoring，替换了 judge identity 为 infrastructure facets\n- 两者研究的评测范式不同，简单的 facet 数量对比（5 vs 7）可能高估增量贡献\n\n---\n\n## Questions\n\n**Q1**: 为什么选择 items 而非 models 作为 object of measurement？如果目标是判断哪个模型最好，G_model 是否更直接？G_item ≥ 0.80 在什么条件下能保证 model ranking stability？\n\n**Q2**: 推荐的 3×3 设计（3 prompts × 3 seeds = 9 conditions × 178 items = 1,602 evaluations）在单 GPU 上的实际墙钟时间是多少？对需要评估大量模型的 benchmark leaderboard 是否可行？\n\n**Q3**: 200 items 通过 stratified sampling 选取。方差分解对特定 item 样本的敏感度如何？不同的 200-item 样本是否会产生类似的 G_item？（Appendix A 中的 bootstrap CI 是 item-level resampling，但不等同于完全独立的 item sample。）\n\n**Q4**: Table 1 中与 Messing (2026) 的对比是否公平？Messing 研究的是 LLM-as-judge 场景（judge identity 43.8%），本文研究的是 generation-based scoring。两者的 facet 集合和评测范式不同，仅用 facet 数量和 benchmark 数量对比是否过于简化？\n\n**Q5**: 对于 model facet 的 quasi-random 处理（§3.6），8 个模型是 deliberate selection 而非 random sampling from a population。这一处理的合理性在什么条件下成立？如果模型更新换代（如 2026 年新一代模型），G-study 结果是否仍然适用？\n\n---\n\n## Missing References\n\n1. **MMLU-Redux** (Gema et al., 2024) — 识别 MMLU 错误标注，直接影响 item-level 方差分解解读\n2. **MMLU-Pro** (Wang et al., 2024) — 10 选项 MMLU 变体，降低 guessing variance\n3. **Contamination 检测文献** (如 Shi et al. 2023, Golchin & Surdeanu 2024) — Limitations 提到 contamination 但未引用相关工作\n4. **Evaluation harness 标准化的持续努力** — 论文引用了 lm-eval-harness 但未讨论标准化 harness 如何与本文的 protocol optimization 建议对接\n\n---\n\n## Overall Assessment\n\n### 官方维度打分（ACL ARR Review Form）\n\n| 维度 | 分数 | 理由摘要 |\n|------|------|----------|\n| **Soundness** | 3.5/5 | 实验方法论扎实，鲁棒性验证全面（S3），但 G_item→model ranking gap（W3）和 binary scope 未充分限定（W2）削弱了实际推论的可靠性 |\n| **Excitement** | 3.0/5 | 对 Messing (2026) 的扩展有价值但主要是 incremental（更多 facets、更多 benchmarks、D-study）；D-study 预算和 IRT 互补性（S2, S5）是最引人注目的贡献 |\n| **Reproducibility** | 4/5 | 匿名代码仓库、详尽的实验设置、Henderson Method I 充分文档化、binary data validation 完善 |\n| **Datasets** | 4/5 | 2.3M 记录的 factorial 数据集对 evaluation methodology 研究社区有价值 |\n| **Software** | 4/5 | 开源 G-theory pipeline 和 D-study calculator 可被复用 |\n| **Reviewer Confidence** | 4/5 | 熟悉 G-theory、psychometrics in NLP、LLM evaluation 文献。仔细阅读了全文和所有 appendix |\n| **Author Identity** | 1/5 | 无法判断作者身份 |\n\n### Overall: **3.5** (Borderline Conference)\n\n**一句话总结**: 方法论扎实、实验规模可观的增量贡献——D-study 预算和 IRT 互补性是最具价值的新发现，但 binary scoring 的 scope 限制、\"10× fewer items\" 的 framing 误导、以及 G_item 与 model ranking reliability 之间的概念鸿沟需要在修订中解决。\n\n**详细理由**: 本文在 Messing (2026) 基础上做了三个方向的扩展（infrastructure facets、cross-benchmark、D-study budgets），其中 D-study 预算是最具实用价值的贡献（S2），IRT 互补性发现（S5）对 benchmark 开发有直接启示。鲁棒性分析（S3）达到了高标准。然而：(1) G_item 与 model ranking reliability 之间缺乏直接桥接（W3），使得 \"reproducibility budgets\" 的实际含义不够清晰；(2) abstract 和 title 的 framing 在 scope（W2: binary scoring only）和效率（W1: total evaluations 增长）两个维度上产生误导；(3) 格式相关发现 C3 证据不足但占篇幅过大（W4）。如果 W1–W3 得到充分修订（特别是增加 model ranking stability 分析和 scope 限定），本文可达到 Conference 水平。当前版本是 strong Findings candidate。\n",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 875 · 2026-05-25T21:27:14.672968+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3513
}
```

</details>

---


### Tool call

_source line 876 · 2026-05-25T21:27:21.335890+00:00_

called mcp__agent-ml-research__cleanup_pdf_images

<details open><summary>🔧 Tool call — mcp__agent-ml-research__cleanup_pdf_images</summary>

```json
{
  "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "tool_args": {
    "output_dir": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/artifacts/review_round_10/_pdf_images"
  }
}
```

</details>

---


### Tool result

_source line 877 · 2026-05-25T21:27:21.386407+00:00_

{"result":"{\"success\": true, \"data\": {\"message\": \"目录不存在，无需清理\", \"deleted\": 0}, \"error\": null, \"metadata\": {}}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__cleanup_pdf_images",
  "elapsed_ms": 50
}
```

</details>

---


### Assistant

_source line 878 · 2026-05-25T21:27:32.269422+00:00_

审稿完成，已提交给 Review Director。

**核心判断**: Overall 3.5 (Borderline Conference)

三个 Must-Fix 问题：
1. **"10× fewer items" framing 隐藏计算量增长** — abstract 仅报告 item reduction，未提 total evaluations 从 552→71,280 (129×)
2. **Binary scoring scope 未在 title/abstract 限定** — title 暗示通用 LLM 评测，但 text-exact-match 下 G 从 0.936 崩溃到 0.007
3. **G_item vs model ranking reliability 概念鸿沟** — 以 items 为测量对象计算可靠性，但用户关心的是模型排名稳定性

主要优势在 D-study 预算实用性（S2）、IRT+G-theory 互补性（S5）和鲁棒性分析质量（S3）。修订后可达 Conference 水平。

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---


## Round 22

## Round 22

10 recorded events


### User

_source line 879 · 2026-05-25T21:29:18.279286+00:00_

[Round 11 审稿请求]:
以下是 Reviewer 1 的完整审稿意见。请逐条回应：对每个 Weakness 和 Question 标注 [AGREE] 同意并说明理由，或 [REBUT] 反驳并提供证据（cite 具体 Section/Table/Figure）。

---

# Reviewer 1 审稿意见 — 方法严谨性 + 实验设计

## Summary

本文将教育测量领域的概化理论（G-theory）引入LLM评估，通过Henderson Method I对8个7-9B开源模型在5个基准上约230万条二值记录进行方差分量分解，发现model×item交互是主要的非残差方差来源（MC 30-36%, FF 15-17%），并据此通过D-study投影给出可复现性预算建议（3-prompt × 3-seed设计将MMLU所需题目从552降至178）。这是G-theory在NLP评估领域的首次完整应用（含D-study投影），方法论框架扎实，实验规模大，且附有9项稳健性检验。主要关切集中在：格式关联模式的统计功效不足但在结论中被过度声称、Bootstrap CI仅捕获item层不确定性、以及二值评分限定下的实用范围偏窄。

## Strengths

**S1** [方法新颖性] 首次将G-theory的完整工作流（G-study方差分解 + D-study预算投影）系统应用于LLM评估，填补了已有工作（Bouthillier et al., 2021; Messing, 2026）在D-study投影和跨格式比较方面的空白。

**S2** [实验规模与设计] 7 facet × 8 model × 5 benchmark的全因子/准全因子设计是该领域迄今最大规模的多面交叉方差分析。

**S3** [稳健性检验充分] Appendix A提供9项独立稳健性分析，系统覆盖了估计方法、数据分布、样本稳定性等多个角度。

**S4** [核心发现的洞察力] model×item交互主导是一个非直觉但重要的发现：模型主要在"哪些题目难"上分歧，而非在整体能力上分歧。MMLU学科粒度分析进一步验证了这一机制。

**S5** [实用产出] 开源G-theory pipeline和D-study calculator具有直接实用价值。IRT与G-theory正交互补的论证也有启发性。

**S6** [Binary data处理的透明度] Section 3.5明确标注了binary scoring假设，probit simulation量化了binarization的代价。

## Weaknesses

### Must-Fix

**W1** [critical] 格式关联模式在结论中被过度声称
- Section 4.3明确标记为"exploratory"和"descriptive observation"（permutation p=0.10, n=5, benchmark-level CI spans zero）
- 但Section 5 Conclusion写"The variance structure is format-dependent...motivating per-format budget calibration"，完全去掉了"exploratory"限定词
- Table 9的预算按MC/FF分开给出，实际上将这一探索性发现当作已建立的结论用于实践推荐
- 建议：Conclusion保留"exploratory"限定词；Table 9加注"based on n=5 benchmarks; format-specific calibration requires replication"

**W2** [critical] Bootstrap CI仅捕获item-level不确定性，D-study预算的置信区间被低估
- Table 9的95% CI仅反映item-level resampling
- LOMO分析显示max|ΔG|=0.030，对应~23%的预算变化，但这一model-level不确定性从未与item-level CI联合量化
- 建议：Table 9标注CI仅反映item-level sampling variability；提供联合item+model uncertainty估计

### Should-Fix

**W3** [warning] Model作为quasi-random facet的辩护链不完整
- 8个purposively selected模型被当作random facet，Meredith (1993)和Putnick (2016)是关于measurement invariance的，非关于justifying random-facet treatment
- LOMO和four-model subset是within-sample stability checks，不等于out-of-sample generalization
- FF的7.3% error（MATH, Table 11）意味着非trivial偏差

**W4** [warning] D-study投影的时间不变性假设未被充分讨论
- LLM模型架构、训练数据变化极快，方差分量temporal stability无证据
- 建议：讨论哪些方差分量最可能随模型代际变化

**W5** [warning] Partial-credit scoring的影响被低估
- GSM8K partial-credit G从0.86降至0.77（ΔG=-0.135），降幅显著
- D-study预算完全基于binary scoring，但现实中越来越多LLM评估采用partial-credit或连续评分

**W6** [warning] Object of measurement的选择及其对实用性的影响未被讨论
- 论文选择items作为object of measurement，但用户关心的是model-level reliability
- 建议：至少解释为什么选择items而非models，以及两种选择下G-coefficient的关系

### Minor

**M1** exp-002 reduced crossing validation仅基于MMLU
**M2** Abstract第一句"up to 79 percentage points"来自prior literature，需clarify
**M3** "quasi-random facet"不是G-theory标准术语
**M4** Benchmark contamination机制未讨论

## Questions

**Q1** 如果用户仅评估1个模型，D-study预算应如何调整？
**Q2** Probit simulation的ρ=0.732是否足够精确以支持quantitative claims？
**Q3** Scale validation仅覆盖Qwen和Llama家族，是否有MoE架构证据？
**Q4** Ordering facet在非MMLU benchmarks上σ²=0——是因为无效果还是未应用？

## Missing References
- Cronbach et al. (1972) — G-theory奠基文献
- Webb, Shavelson, & Haertel (2006) — G-theory在non-standard data上的应用

## Overall Assessment
**3.5** (Borderline Conference) | Confidence: 4/5

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "source": "review_reviewer_2"
}
```

</details>

---


### Tool call

_source line 880 · 2026-05-25T21:29:57.954453+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/conclusion.tex"
  }
}
```

</details>

---


### Tool result

_source line 881 · 2026-05-25T21:29:58.406450+00:00_

1	\section{Conclusion}
2	\label{sec:conclusion}
3	
4	The dominant non-residual variance source in LLM evaluation is the model$\times$item interaction (30--36\% in MC, 15--17\% in FF), revealing that models disagree on which items are difficult rather than differing uniformly in overall ability. Multi-facet evaluation designs absorb this interaction: a 3-prompt $\times$ 3-seed protocol achieves $G \geq 0.80$ with 178 MMLU items versus 552 under single-condition, with cross-benchmark budgets of 93--128 items. The variance structure is format-dependent: MC benchmarks concentrate 68--72\% in item-related components while FF benchmarks disperse to 31--41\%, motivating per-format budget calibration. We recommend three practices: adopt multi-facet designs for published results, report item-level accuracy to expose model$\times$item interaction, and calibrate item budgets per benchmark format.
5	

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 451
}
```

</details>

---


### Tool call

_source line 882 · 2026-05-25T21:29:58.406777+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/appendix.tex"
  }
}
```

</details>

---


### Tool result

_source line 883 · 2026-05-25T21:29:58.959488+00:00_

1	\appendix
2	
3	\section{Additional Robustness Analyses}
4	\label{app:robustness}
5	
6	We report nine robustness analyses that verify the stability of the variance decomposition under alternative analytical choices.
7	
8	\paragraph{GLMM complement.} A generalized linear mixed model (GLMM) with marginal logit link produces variance component rankings that perfectly preserve all seven grouped component orderings ($\rho = 1.0$) relative to Henderson Method~I \cite{jiang2018bayesian, tuerlinckx2006glmm}. This confirms that the linear variance decomposition is robust to the binary outcome distribution.
9	
10	\paragraph{Accuracy-range stability.} The \texttt{item\_id} variance share remains stable across subsets with mean accuracy from 0.62 to 0.72 ($r = -0.048$). This rules out distortion from binary floor or ceiling effects at observed accuracy levels.
11	
12	\paragraph{Estimator robustness.} We compare Henderson Method~I with restricted maximum likelihood (REML-EM, 500 iterations, practical convergence $\Delta < 0.003$ percentage points). All variance components differ by $<$0.5 percentage points between estimators. The largest discrepancy occurs on the residual component (0.47pp); all substantive components (item, model$\times$item, model) differ by $<$0.3pp. Henderson Method~I is preferred for our balanced designs because it produces unbiased estimates without distributional assumptions \cite[Ch.~12]{brennan2001generalizability}.
13	
14	\paragraph{Probit simulation.} A probit simulation matched to our 1,296-condition design confirms that Henderson Method~I recovers variance component rankings from dichotomized data (Spearman $\rho = 0.732$ between binary and continuous rankings, excluding residual; \texttt{item\_id} dominant in all 100 replications; top-5 ordering correct in 79\% of replications). Bias analysis by difficulty stratum shows $|\text{bias}| = 0.28$--$0.37$ for items with $p \in [0.5, 0.8]$, where the Bernoulli variance ceiling $p(1{-}p)$ is largest. Thi
…[truncated 21784 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 552
}
```

</details>

---


### Tool call

_source line 884 · 2026-05-25T21:29:59.160795+00:00_

called Read

<details open><summary>🔧 Tool call — Read</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex",
  "limit": "50",
  "offset": "80"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "tool_args": {
    "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0519/projects/nlp_variance_gtheory/docs/paper/experiments.tex",
    "limit": "50",
    "offset": "80"
  }
}
```

</details>

---


### Tool result

_source line 885 · 2026-05-25T21:29:59.211461+00:00_

80	\subsection{Exploratory: Format-Associated Variance Patterns}
81	\label{sec:format_conditional}
82	
83	Table~\ref{tab:cross_benchmark} reveals a format-associated pattern: MC benchmarks concentrate item-related variance (item + model$\times$item) at 68--72\%, while FF benchmarks disperse to 31--41\% ($n = 5$; permutation $p = 0.10$; item-level $d = 1.73$, benchmark-level CI spans zero); we report this as a descriptive observation. This does not extend to item budgets: HellaSwag (MC, 118 items) exceeds ARC (98) and MATH (101), showing format alone does not predict cost (Figure~\ref{fig:cross_benchmark}). Figure~\ref{fig:difficulty_scatter} shows item difficulty heterogeneity ($\text{std}(p_i)$) predicts item variance share ($\rho = 0.82$; Appendix~\ref{app:difficulty_scatter}). Within MMLU, this mechanism is visible at subject granularity: knowledge-intensive subjects (e.g., international law, $G = 0.930$) show high item variance, while reasoning-heavy subjects (e.g., high school mathematics, $G = 0.614$) show model$\times$item exceeding item difficulty, mirroring the MC--FF contrast (Table~\ref{tab:subject_gstudy}). Per-benchmark details are in Appendix~\ref{app:format_details}. All findings are conditional on binary scoring (\S\ref{sec:binary}).
84	
85	\begin{table}[t]
86	\centering
87	\caption{Format-associated variance structure across five benchmarks (exp-002, 8 models). Variance components (\%) per benchmark; MC = multiple-choice, FF = free-form. Bold = dominant non-residual component. $^\dagger$For MC, reports prompt$\times$item interaction (prompt main effect $<$1\%); for FF, reports prompt main effect (item-conditional interactions absorbed into residual).}
88	\label{tab:cross_benchmark}
89	\scriptsize
90	\begin{tabular}{l rrr rr}
91	\toprule
92	 & \multicolumn{3}{c}{MC} & \multicolumn{2}{c}{FF} \\
93	\cmidrule(lr){2-4} \cmidrule(lr){5-6}
94	 & MMLU & ARC & Hella. & GSM & MATH \\
95	\midrule
96	\textbf{item} & \textbf{37.9} & \textbf{37.9} & 34.3 & 16.9 &
…[truncated 1985 chars]

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "Read",
  "elapsed_ms": 50
}
```

</details>

---


### Tool call

_source line 886 · 2026-05-25T21:32:33.452183+00:00_

called mcp__agent-ml-research__review_reviewer_post_to_director

<details open><summary>🔧 Tool call — mcp__agent-ml-research__review_reviewer_post_to_director</summary>

```json
{
  "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### W1 [critical]: 格式关联模式在结论中被过度声称\n\n**[AGREE] R1-W1**: 完全同意。我在自己的审稿中也将此标记为 W4 (should-fix)。\n\n核实原文：§4.3 明确写 \"we report this as a descriptive observation\"（experiments.tex L83），permutation p=0.10，benchmark-level CI spans zero。但 §5 Conclusion 写 \"The variance structure is format-dependent...motivating per-format budget calibration\"（conclusion.tex L4），完全去掉了 exploratory/descriptive 限定词。\n\n更关键的是，Table 9 按 MC/FF 分开报告 D-study 预算，实际上将这一 p=0.10 的探索性观察当作已确立的结论用于实践推荐。这是一个 framing consistency 问题。\n\nR1 的修改建议具体可操作（Conclusion 保留 \"exploratory\"；Table 9 加注）。我补充建议：Introduction 的贡献 C3 也应降级，明确标注 \"preliminary/exploratory\"，目前与 C1、C2 并列的呈现方式暗示了同等证据强度。\n\n---\n\n### W2 [critical]: Bootstrap CI 仅捕获 item-level 不确定性\n\n**[AGREE] R1-W2**: 同意这是一个重要的统计方法论问题。\n\n论文在 Appendix A \"CI method comparison\" 段落中实际上已经承认了这一点：\"Bootstrap CIs capture item-sampling variability **conditional on these 8 specific models**; model-level stability is assessed separately via LOMO (below).\"（appendix.tex L16）。问题是这两个不确定性来源**从未被联合量化**。\n\n具体地：\n- Table 9 的 95% CI（如 MMLU: [76, 116]）仅反映 item-level resampling\n- LOMO 的 max|ΔG|=0.030（Table 4）对应 ~23% 的预算变化（Appendix B, Figure 9）\n- 如果联合考虑，Table 9 的 CI 可能显著加宽\n\n但我要补充一个 nuance：R1 说 \"D-study 预算的置信区间被低估\" 需要定量验证。LOMO 的 max|ΔG|=0.030 来自 leave-one-out（移除最有影响力的单个模型），不是对模型群体的抽样不确定性。真正的联合 CI 需要对 items 和 models 同时 bootstrap，这在 n_model=8 的情况下统计功效很低。\n\n**总结**：同意 R1 的诊断（CI source 标注不透明）和建议（Table 9 标注 CI 仅反映 item-level variability），但对 \"联合 item+model uncertainty 估计\" 的可行性持保留意见——8 个模型做 model-level bootstrap 可能产生方差极大的估计。更实用的做法可能是报告 sensitivity band（Appendix B 已有 Figure 9 的 ±23% 框架）。\n\n---\n\n### W3 [warning]: Quasi-random facet 辩护链不完整\n\n**[AGREE] R1-W3**: 同意引用选择有问题。\n\nMeredith (1993) 和 Putnick (2016) 是关于 measurement invariance（跨群体测量等价性），而非关于 G-theory 中 random-facet treatment 的合理性条件。正确的引用应为 Brennan (2001, Ch. 4) 关于 fixed vs. random facets 的讨论，或 Shavelson & Webb (1991) 关于 facet universe definition。\n\n但在实质分析层面，论文确实提供了支持 quasi-random treatment 的证据链：\n- Fixed vs. random 对比（Table 10, Appendix A）：ΔG = 0.077–0.113，random 更保守\n- LOMO（Table 4）：CV ≤ 1.25%，max|ΔG| = 0.030\n- Four-model subset check（Table 11）：MC |ΔG| ≤ 0.029\n\n问题是 R1 正确指出的：这些是 **within-sample stability checks**，不等于 out-of-sample generalization。如果加入 2026 年的新模型（如 Llama-4、Gemma-3），方差分量可能不同。FF 的 7.3% error（Table 11, MATH）也说明预测误差不是 trivial 的。\n\n---\n\n### W4 [warning]: D-study 投影的时间不变性假设\n\n**[AGREE] R1-W4**: 同意。\n\n论文在 §4.5 最后一句提到 \"All projections assume the 2024–2025 model generation; §4.6 provides preliminary support\"（experiments.tex L195），但 §4.6 的 scale validation 仅检验了参数规模泛化（3B→72B），未检验时间维度。\n\n考虑到 LLM 训练数据和架构变化速度，model×item interaction 的主导地位可能随模型代际变化。例如，如果未来模型在训练中更均匀地覆盖不同 item 类型，model×item 可能下降，item 主效应可能上升。\n\nR1 建议 \"讨论哪些方差分量最可能随模型代际变化\" 是可操作且不增加实验成本的改进。\n\n---\n\n### W5 [warning]: Partial-credit scoring 影响被低估\n\n**[AGREE] R1-W5**: 同意，与我自己的 W7 一致。\n\n补充 R1 的论点：\n- GSM8K partial-credit 下 G 从 0.86 降至 0.77（Appendix A, L26），但 ΔG 的范围极大（−0.025 to −0.309），受模型准确率调节\n- 更重要的是，48.1% 的错误回答有正确的中间推理步骤（appendix.tex L26），这意味着 binary scoring 系统性地丢失了 item 区分信息\n- 现实中 code generation（pass@k with partial tests）、open-ended QA（rubric scoring）、LLM-as-judge（likert scale）都使用非 binary 评分\n\nD-study 预算声称直接依赖于方差分量估计，而 partial-credit 下方差结构显著不同（residual 从 39.9% 升至 64.9%）。论文应更明确地限定预算适用范围。\n\n---\n\n### W6 [warning]: Object of measurement 选择未被讨论\n\n**[AGREE] R1-W6**: 强烈同意——这与我自己的 W3 (critical) 完全一致。\n\n论文选择 items 作为 object of measurement（§3.1: \"test items (p) serve as the object of measurement\"），G_item 衡量的是 item-level scores 在不同方法论条件下的泛化能力。但 benchmark 用户的核心问题是 \"用这 N 个 items 排出的模型顺序是否可重复\"——这需要以 models 为 object of measurement 计算 G_model，或至少需要桥接分析（如 bootstrap 排名一致性、Kendall's W）。\n\n论文的间接证据（LOMO Table 4, κ=0.33–0.46, four-model subset Table 11）支持了方差结构的 within-sample stability，但**没有直接回答 model ranking reliability 的问题**。\n\n我认为这应该从 R1 的 should-fix 提升为 **must-fix**（或至少接近 must-fix），因为它关乎论文核心实用价值的解释框架。\"Reproducibility Budgets\" 这一概念在读者心中自然对应的是 \"我需要多少 items 才能得到稳定的模型排名\"，而非 \"我需要多少 items 才能稳定地刻画 item difficulty profile\"。\n\n---\n\n### Minor Issues 回应\n\n**[AGREE] R1-M1**: exp-002 reduced crossing validation 仅基于 MMLU。Appendix A \"Reduced crossing validation\" 段落确认 ΔG=0.0008 但仅在 MMLU 上验证（appendix.tex L52）。对其他 4 个 benchmarks 没有交叉验证。虽然 MMLU 的方差结构与 ARC 相似，但 GSM8K/MATH 差异较大，应至少对一个 FF benchmark 验证。\n\n**[REBUT] R1-M2**: R1 写 \"Abstract第一句 'up to 79 percentage points'\"——实际论文 abstract 写的是 \"up to 76 percentage points\"（abstract.tex L1），对应 Sclar et al. (2024) 和 BrittleBench (2026) 的引用。R1 可能误读了数字。不过，R1 的实质关切（该数字来自 prior literature 需 clarify）在 abstract 中通过 \"Growing evidence challenges this assumption:\" 的引导已隐含表明是文献综述，且 introduction 中明确引用了来源。这不构成实质问题。\n\n**[AGREE] R1-M3**: \"quasi-random facet\" 确实不是 G-theory 的标准术语。Brennan (2001) 使用 \"random\" 和 \"fixed\" 二分法，有时讨论 \"partially random\" 设计。论文应使用标准术语并解释为什么将 purposively selected models 按 random 处理（保守估计，upper-bound budgets）。\n\n**[AGREE] R1-M4**: 同意，与我自己的 W8 一致。Limitations 提到 contamination 但未引用任何检测文献。\n\n---\n\n## Questions 回应\n\n**[REBUT] R1-Q1**: 论文实际上已回答了这个问题。\n\n§4.1 Single-Model Baseline（experiments.tex L5–19）给出了单模型 D-study 预算：Llama-3.1-8B 在 MMLU 上，full multi-facet 下 55 items 即达 G ≥ 0.80，G_item(200) = 0.936。单模型方差分量（item 58.4%，residual 23.1%，无 model×item 交互）与多模型方差分量（Table 5）不同，因此预算不同（55 vs. 93 items multi-facet）。\n\n但 R1 的问题可能暗示一个更深层的关切：Table 9 的 cross-model 预算（93–128 items）是否适用于\"仅评估 1 个新模型\"的场景？答案是否——因为 model×item 交互进入了 cross-model G 的 σ²_rel，但在单模型评估中不存在。论文可以更明确地区分这两个使用场景。\n\n---\n\n**[AGREE] R1-Q2**: ρ=0.732 确实是中等水平，但需 nuanced 解读。\n\nAppendix A（appendix.tex L14）报告 probit simulation ρ=0.732（排除 residual），top-5 ordering 正确率 79%，item_id 在全部 100 次重复中均为 dominant。这支持**ranking recovery**（哪个分量最大），但不支持**精确的定量估计**（分量的绝对大小）。\n\n论文的 D-study 预算依赖定量的方差分量值（Eq. 2），而非仅依赖排序。如果 binarization 使方差分量的绝对值产生 ~27% 的 bias（|bias| = 0.28–0.37 for p ∈ [0.5, 0.8]），D-study 预算可能偏离真实值。\n\n但论文在 probit simulation 段落最后论证了 binary data 产生的预算是 **conservative**（binarization 增加 36% 的预算），这意味着误差方向是安全的（过多而非过少的 items）。因此 ρ=0.732 不会导致实践上的危险建议，但定量精度存疑。\n\n---\n\n**[AGREE] R1-Q3**: 论文仅测试了 dense architecture（Table 3 全部为 RMS-Norm dense models）。\n\nMoE 架构（如 Mixtral、DeepSeek-MoE）的 routing 机制可能引入额外的 model×item 交互方差（不同 experts 对不同 item types 的 specialization），改变方差分量结构。这是 §3.6 \"results may not generalize to API-based, base, or >9B models\" 的一个具体实例，但 MoE 值得单独提及。\n\n---\n\n**[REBUT] R1-Q4**: 这是 by design，论文已明确说明。\n\n§3.3（method.tex L66）明确写道：\"Ordering operates only on MMLU (σ²_ordering = 0 for other benchmarks, retained for design balance).\" 此处 ordering 指 few-shot demonstration permutations（Table 2: \"Demo permutations\"），非 answer option ordering。\n\n对于 FF benchmarks (GSM8K, MATH)，few-shot demo ordering 不适用（few-shot 是独立的数学问题序列，顺序效应预期很小）。但对于 ARC 和 HellaSwag（MC），R1 的关切有一定道理：few-shot demo 的顺序可能影响 model 的 in-context learning，而论文在这两个 benchmark 上没有变异 ordering。这是一个实验设计的 scope limitation，不影响已报告结果的有效性，但意味着 ARC/HellaSwag 的方差分解可能低估了 ordering-related 交互。\n\n---\n\n## Missing References 回应\n\n**[AGREE] Cronbach et al. (1972)**: G-theory 奠基文献，应该引用。论文引用了 Shavelson & Webb (1991) 和 Brennan (2001) 作为 G-theory 主要参考，但 Cronbach et al. (1972) 是更早的开创性工作，方法论论文理应引用。\n\n**[REBUT] Webb, Shavelson, & Haertel (2006)**: 这篇关于 non-standard data 的 G-theory 应用确实相关，但论文已经引用了 Mushquash & O'Connor (2006) 和 Jiang & Skorupski (2018) 作为 binary/non-standard data 的 G-theory 参考（related_work.tex L18）。如果要加，可以加，但不算 critical omission。\n\n---\n\n## 总结\n\nR1 的审稿意见整体专业且切中要害。在 6 个 Weaknesses 中：\n- **5 个 AGREE**（W1, W2, W3, W4, W5）+ 1 个 **强烈 AGREE 并建议提升严重度**（W6→should-fix 提升为 near-critical）\n- W1（format overclaim in conclusion）和 W6（object of measurement）与我自己的独立发现高度一致\n- W2（CI 仅捕获 item-level uncertainty）是我未独立标记但认可其重要性的统计方法论问题\n\n在 4 个 Questions 中：1 个 REBUT（Q1 已回答）、2 个 AGREE（Q2 nuanced agree, Q3 agree）、1 个 REBUT with nuance（Q4 by design）。\n\nR1 给出 3.5 (Borderline Conference)，与我的评分一致。两位 reviewer 的独立评估在核心问题（format overclaim、object of measurement、binary scope、partial-credit limitation）上高度趋同，增强了对这些问题严重性的判断置信度。\n",
  "reviewer_id": "2",
  "project": "nlp_variance_gtheory"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "tool_args": {
    "text": "\n# Reviewer 2 对 Reviewer 1 审稿意见的逐条回应\n\n---\n\n## Weaknesses 回应\n\n### W1 [critical]: 格式关联模式在结论中被过度声称\n\n**[AGREE] R1-W1**: 完全同意。我在自己的审稿中也将此标记为 W4 (should-fix)。\n\n核实原文：§4.3 明确写 \"we report this as a descriptive observation\"（experiments.tex L83），permutation p=0.10，benchmark-level CI spans zero。但 §5 Conclusion 写 \"The variance structure is format-dependent...motivating per-format budget calibration\"（conclusion.tex L4），完全去掉了 exploratory/descriptive 限定词。\n\n更关键的是，Table 9 按 MC/FF 分开报告 D-study 预算，实际上将这一 p=0.10 的探索性观察当作已确立的结论用于实践推荐。这是一个 framing consistency 问题。\n\nR1 的修改建议具体可操作（Conclusion 保留 \"exploratory\"；Table 9 加注）。我补充建议：Introduction 的贡献 C3 也应降级，明确标注 \"preliminary/exploratory\"，目前与 C1、C2 并列的呈现方式暗示了同等证据强度。\n\n---\n\n### W2 [critical]: Bootstrap CI 仅捕获 item-level 不确定性\n\n**[AGREE] R1-W2**: 同意这是一个重要的统计方法论问题。\n\n论文在 Appendix A \"CI method comparison\" 段落中实际上已经承认了这一点：\"Bootstrap CIs capture item-sampling variability **conditional on these 8 specific models**; model-level stability is assessed separately via LOMO (below).\"（appendix.tex L16）。问题是这两个不确定性来源**从未被联合量化**。\n\n具体地：\n- Table 9 的 95% CI（如 MMLU: [76, 116]）仅反映 item-level resampling\n- LOMO 的 max|ΔG|=0.030（Table 4）对应 ~23% 的预算变化（Appendix B, Figure 9）\n- 如果联合考虑，Table 9 的 CI 可能显著加宽\n\n但我要补充一个 nuance：R1 说 \"D-study 预算的置信区间被低估\" 需要定量验证。LOMO 的 max|ΔG|=0.030 来自 leave-one-out（移除最有影响力的单个模型），不是对模型群体的抽样不确定性。真正的联合 CI 需要对 items 和 models 同时 bootstrap，这在 n_model=8 的情况下统计功效很低。\n\n**总结**：同意 R1 的诊断（CI source 标注不透明）和建议（Table 9 标注 CI 仅反映 item-level variability），但对 \"联合 item+model uncertainty 估计\" 的可行性持保留意见——8 个模型做 model-level bootstrap 可能产生方差极大的估计。更实用的做法可能是报告 sensitivity band（Appendix B 已有 Figure 9 的 ±23% 框架）。\n\n---\n\n### W3 [warning]: Quasi-random facet 辩护链不完整\n\n**[AGREE] R1-W3**: 同意引用选择有问题。\n\nMeredith (1993) 和 Putnick (2016) 是关于 measurement invariance（跨群体测量等价性），而非关于 G-theory 中 random-facet treatment 的合理性条件。正确的引用应为 Brennan (2001, Ch. 4) 关于 fixed vs. random facets 的讨论，或 Shavelson & Webb (1991) 关于 facet universe definition。\n\n但在实质分析层面，论文确实提供了支持 quasi-random treatment 的证据链：\n- Fixed vs. random 对比（Table 10, Appendix A）：ΔG = 0.077–0.113，random 更保守\n- LOMO（Table 4）：CV ≤ 1.25%，max|ΔG| = 0.030\n- Four-model subset check（Table 11）：MC |ΔG| ≤ 0.029\n\n问题是 R1 正确指出的：这些是 **within-sample stability checks**，不等于 out-of-sample generalization。如果加入 2026 年的新模型（如 Llama-4、Gemma-3），方差分量可能不同。FF 的 7.3% error（Table 11, MATH）也说明预测误差不是 trivial 的。\n\n---\n\n### W4 [warning]: D-study 投影的时间不变性假设\n\n**[AGREE] R1-W4**: 同意。\n\n论文在 §4.5 最后一句提到 \"All projections assume the 2024–2025 model generation; §4.6 provides preliminary support\"（experiments.tex L195），但 §4.6 的 scale validation 仅检验了参数规模泛化（3B→72B），未检验时间维度。\n\n考虑到 LLM 训练数据和架构变化速度，model×item interaction 的主导地位可能随模型代际变化。例如，如果未来模型在训练中更均匀地覆盖不同 item 类型，model×item 可能下降，item 主效应可能上升。\n\nR1 建议 \"讨论哪些方差分量最可能随模型代际变化\" 是可操作且不增加实验成本的改进。\n\n---\n\n### W5 [warning]: Partial-credit scoring 影响被低估\n\n**[AGREE] R1-W5**: 同意，与我自己的 W7 一致。\n\n补充 R1 的论点：\n- GSM8K partial-credit 下 G 从 0.86 降至 0.77（Appendix A, L26），但 ΔG 的范围极大（−0.025 to −0.309），受模型准确率调节\n- 更重要的是，48.1% 的错误回答有正确的中间推理步骤（appendix.tex L26），这意味着 binary scoring 系统性地丢失了 item 区分信息\n- 现实中 code generation（pass@k with partial tests）、open-ended QA（rubric scoring）、LLM-as-judge（likert scale）都使用非 binary 评分\n\nD-study 预算声称直接依赖于方差分量估计，而 partial-credit 下方差结构显著不同（residual 从 39.9% 升至 64.9%）。论文应更明确地限定预算适用范围。\n\n---\n\n### W6 [warning]: Object of measurement 选择未被讨论\n\n**[AGREE] R1-W6**: 强烈同意——这与我自己的 W3 (critical) 完全一致。\n\n论文选择 items 作为 object of measurement（§3.1: \"test items (p) serve as the object of measurement\"），G_item 衡量的是 item-level scores 在不同方法论条件下的泛化能力。但 benchmark 用户的核心问题是 \"用这 N 个 items 排出的模型顺序是否可重复\"——这需要以 models 为 object of measurement 计算 G_model，或至少需要桥接分析（如 bootstrap 排名一致性、Kendall's W）。\n\n论文的间接证据（LOMO Table 4, κ=0.33–0.46, four-model subset Table 11）支持了方差结构的 within-sample stability，但**没有直接回答 model ranking reliability 的问题**。\n\n我认为这应该从 R1 的 should-fix 提升为 **must-fix**（或至少接近 must-fix），因为它关乎论文核心实用价值的解释框架。\"Reproducibility Budgets\" 这一概念在读者心中自然对应的是 \"我需要多少 items 才能得到稳定的模型排名\"，而非 \"我需要多少 items 才能稳定地刻画 item difficulty profile\"。\n\n---\n\n### Minor Issues 回应\n\n**[AGREE] R1-M1**: exp-002 reduced crossing validation 仅基于 MMLU。Appendix A \"Reduced crossing validation\" 段落确认 ΔG=0.0008 但仅在 MMLU 上验证（appendix.tex L52）。对其他 4 个 benchmarks 没有交叉验证。虽然 MMLU 的方差结构与 ARC 相似，但 GSM8K/MATH 差异较大，应至少对一个 FF benchmark 验证。\n\n**[REBUT] R1-M2**: R1 写 \"Abstract第一句 'up to 79 percentage points'\"——实际论文 abstract 写的是 \"up to 76 percentage points\"（abstract.tex L1），对应 Sclar et al. (2024) 和 BrittleBench (2026) 的引用。R1 可能误读了数字。不过，R1 的实质关切（该数字来自 prior literature 需 clarify）在 abstract 中通过 \"Growing evidence challenges this assumption:\" 的引导已隐含表明是文献综述，且 introduction 中明确引用了来源。这不构成实质问题。\n\n**[AGREE] R1-M3**: \"quasi-random facet\" 确实不是 G-theory 的标准术语。Brennan (2001) 使用 \"random\" 和 \"fixed\" 二分法，有时讨论 \"partially random\" 设计。论文应使用标准术语并解释为什么将 purposively selected models 按 random 处理（保守估计，upper-bound budgets）。\n\n**[AGREE] R1-M4**: 同意，与我自己的 W8 一致。Limitations 提到 contamination 但未引用任何检测文献。\n\n---\n\n## Questions 回应\n\n**[REBUT] R1-Q1**: 论文实际上已回答了这个问题。\n\n§4.1 Single-Model Baseline（experiments.tex L5–19）给出了单模型 D-study 预算：Llama-3.1-8B 在 MMLU 上，full multi-facet 下 55 items 即达 G ≥ 0.80，G_item(200) = 0.936。单模型方差分量（item 58.4%，residual 23.1%，无 model×item 交互）与多模型方差分量（Table 5）不同，因此预算不同（55 vs. 93 items multi-facet）。\n\n但 R1 的问题可能暗示一个更深层的关切：Table 9 的 cross-model 预算（93–128 items）是否适用于\"仅评估 1 个新模型\"的场景？答案是否——因为 model×item 交互进入了 cross-model G 的 σ²_rel，但在单模型评估中不存在。论文可以更明确地区分这两个使用场景。\n\n---\n\n**[AGREE] R1-Q2**: ρ=0.732 确实是中等水平，但需 nuanced 解读。\n\nAppendix A（appendix.tex L14）报告 probit simulation ρ=0.732（排除 residual），top-5 ordering 正确率 79%，item_id 在全部 100 次重复中均为 dominant。这支持**ranking recovery**（哪个分量最大），但不支持**精确的定量估计**（分量的绝对大小）。\n\n论文的 D-study 预算依赖定量的方差分量值（Eq. 2），而非仅依赖排序。如果 binarization 使方差分量的绝对值产生 ~27% 的 bias（|bias| = 0.28–0.37 for p ∈ [0.5, 0.8]），D-study 预算可能偏离真实值。\n\n但论文在 probit simulation 段落最后论证了 binary data 产生的预算是 **conservative**（binarization 增加 36% 的预算），这意味着误差方向是安全的（过多而非过少的 items）。因此 ρ=0.732 不会导致实践上的危险建议，但定量精度存疑。\n\n---\n\n**[AGREE] R1-Q3**: 论文仅测试了 dense architecture（Table 3 全部为 RMS-Norm dense models）。\n\nMoE 架构（如 Mixtral、DeepSeek-MoE）的 routing 机制可能引入额外的 model×item 交互方差（不同 experts 对不同 item types 的 specialization），改变方差分量结构。这是 §3.6 \"results may not generalize to API-based, base, or >9B models\" 的一个具体实例，但 MoE 值得单独提及。\n\n---\n\n**[REBUT] R1-Q4**: 这是 by design，论文已明确说明。\n\n§3.3（method.tex L66）明确写道：\"Ordering operates only on MMLU (σ²_ordering = 0 for other benchmarks, retained for design balance).\" 此处 ordering 指 few-shot demonstration permutations（Table 2: \"Demo permutations\"），非 answer option ordering。\n\n对于 FF benchmarks (GSM8K, MATH)，few-shot demo ordering 不适用（few-shot 是独立的数学问题序列，顺序效应预期很小）。但对于 ARC 和 HellaSwag（MC），R1 的关切有一定道理：few-shot demo 的顺序可能影响 model 的 in-context learning，而论文在这两个 benchmark 上没有变异 ordering。这是一个实验设计的 scope limitation，不影响已报告结果的有效性，但意味着 ARC/HellaSwag 的方差分解可能低估了 ordering-related 交互。\n\n---\n\n## Missing References 回应\n\n**[AGREE] Cronbach et al. (1972)**: G-theory 奠基文献，应该引用。论文引用了 Shavelson & Webb (1991) 和 Brennan (2001) 作为 G-theory 主要参考，但 Cronbach et al. (1972) 是更早的开创性工作，方法论论文理应引用。\n\n**[REBUT] Webb, Shavelson, & Haertel (2006)**: 这篇关于 non-standard data 的 G-theory 应用确实相关，但论文已经引用了 Mushquash & O'Connor (2006) 和 Jiang & Skorupski (2018) 作为 binary/non-standard data 的 G-theory 参考（related_work.tex L18）。如果要加，可以加，但不算 critical omission。\n\n---\n\n## 总结\n\nR1 的审稿意见整体专业且切中要害。在 6 个 Weaknesses 中：\n- **5 个 AGREE**（W1, W2, W3, W4, W5）+ 1 个 **强烈 AGREE 并建议提升严重度**（W6→should-fix 提升为 near-critical）\n- W1（format overclaim in conclusion）和 W6（object of measurement）与我自己的独立发现高度一致\n- W2（CI 仅捕获 item-level uncertainty）是我未独立标记但认可其重要性的统计方法论问题\n\n在 4 个 Questions 中：1 个 REBUT（Q1 已回答）、2 个 AGREE（Q2 nuanced agree, Q3 agree）、1 个 REBUT with nuance（Q4 by design）。\n\nR1 给出 3.5 (Borderline Conference)，与我的评分一致。两位 reviewer 的独立评估在核心问题（format overclaim、object of measurement、binary scope、partial-credit limitation）上高度趋同，增强了对这些问题严重性的判断置信度。\n",
    "reviewer_id": "2",
    "project": "nlp_variance_gtheory"
  }
}
```

</details>

---


### Tool result

_source line 887 · 2026-05-25T21:32:37.015595+00:00_

{"result":"{\"success\": true, \"data\": {\"review_director_key\": \"feishu:group:oc_265de443abfe4594f91451b075b582ca:director\"}, \"error\": \"\"}"}

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "tool_result",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2",
  "tool": "mcp__agent-ml-research__review_reviewer_post_to_director",
  "elapsed_ms": 3563
}
```

</details>

---


### Assistant

_source line 888 · 2026-05-25T21:32:45.609062+00:00_

交叉回应已提交。总结：

- R1 的 6 个 Weaknesses 中 **5 个 AGREE**，W6 (object of measurement) 建议从 should-fix **提升至 near-critical**，与我自己的 W3 一致
- **1 个 REBUT**：R1-M2 中的 "79 percentage points" 是误读，论文实际写的是 76
- R1 的 4 个 Questions 中：Q1 REBUT（论文 §4.1 已回答单模型预算）、Q4 REBUT with nuance（ordering σ²=0 是设计选择非发现）、Q2/Q3 AGREE
- 两位 Reviewer 独立评估在核心问题上高度趋同（format overclaim、object of measurement、binary scope），均给出 3.5 Borderline Conference

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "session": "feishu:group:oc_265de443abfe4594f91451b075b582ca:reviewer_2"
}
```

</details>

---
