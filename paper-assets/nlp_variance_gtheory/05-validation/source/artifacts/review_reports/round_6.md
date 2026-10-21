---
round: 6
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T14:48:15.193448+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# Round 7 审稿报告 — nlp_variance_gtheory

**论文**: "Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis"
**Venue**: EMNLP 2026 via ARR May 2026 cycle（deadline: 2026-05-25）
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人参与本轮审稿（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）。Reviewer 3 为前轮 roster 遗留，本轮未分配任务、无审稿意见提交。
**日期**: 2026-05-22

---

## Summary

本文将 Generalizability Theory (G-theory) 系统应用于 LLM 评估的方差分解，设计了最多 7 facet 的 fully crossed factorial 实验，覆盖 8 个 7-9B 开源指令微调模型和 5 个 benchmarks，约 230 万条评估记录。主要发现：(1) 多 facet 设计比单条件设计需要少 10× 的 items 达到 G ≥ 0.80（55 vs 552）；(2) BF16/FP16 在 binary scoring 下功能可互换（<0.1% 交互）；(3) model×item 交互占总方差高达 36%，指示 differential item functioning。论文提供 D-study budget calculator 作为实践工具。

---

## Strengths

**S1. 首个系统性多 facet G-theory 分析 LLM 评估方差** [R1-S1, R2-S1, 共识]
同时交叉 infrastructure facets（precision, seed, temperature）和 methodology facets（prompt, ordering）与 item/model 的联合分解，在维度覆盖和交互效应分离上显著超过 Messing (2026) 的单 benchmark 5-facet 设计和 Madaan et al. (2024) 的逐因素分析。

**S2. Robustness 分析深度罕见** [R1-S2, R2-S2, 共识]
8 项独立 robustness 检查：GLMM complement（ρ = 1.0）、accuracy-range stability、Henderson I vs REML（Δ < 0.003）、probit simulation null calibration（ratio = 1.0008）、CI method comparison（bootstrap vs jackknife, ratio 0.96-1.04）、LOMO（CV ≤ 1.25%）、scoring metric sensitivity、facet specification sensitivity。在同类 NLP 论文中属最高水平。

**S3. 可操作的实践贡献** [R1-S4, R2-S3, 共识]
D-study budget projections 将方差分量转化为具体设计建议（Table 4, 7, 9），3 prompts × 3 seeds 作为最小充分设计。承诺开源 pipeline 和 calculator。

**S4. Precision separability 有即时实用价值** [R1-S3, R2-S5, 共识]
BF16/FP16 功能等价的定量确认（<0.1% 交互），直接简化评估实践中的精度选择。

**S5. 写作质量高** [R1-S6, R2 implicit, 共识]
逻辑链清晰（single-model → cross-model → cross-benchmark → D-study），G-theory 背景介绍对 NLP 读者友好。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. [Critical] Model exchangeability 论证不充分，D-study budgets 泛化边界不清** [R1-N1 + R2-W2, 强共识]

8 个 purposively 选取的 7-9B instruction-tuned 模型作为 quasi-random facet，但论文提供的验证均为 within-sample：
- LOMO（Table 5, CV ≤ 1.25%）证明内部一致性，非外部代表性
- Forward prediction（4→8, |ΔG| = 0.035）是 within-sample interpolation，非 out-of-sample generalization
- Section 3.5 的 conservatism argument（random G < fixed G, ΔG = 0.077-0.113）表明 budgets 在方向上是 conservative，但不保证对 unseen models 的可迁移性

Model 主效应仅 2.5%（Table 2），反映 7-9B instruct 模型内的窄能力范围。标题 "Open-Weight LLM Evaluation" 和 Section 5 的通用建议超出实验支撑范围。Abstract 已加 "instruction-tuned" qualifier，但 Conclusion 和标题未限定。

**建议**：(a) 提供 out-of-sample model validation 或更充分的 sensitivity analysis; (b) Conclusion 加 scope qualifier; (c) 考虑标题是否需要限定。

**N2. [Critical] "10× fewer items" framing 隐藏总评估量 129× 增长** [R2-W1, R1 交叉 AGREE, 强共识]

Abstract 的 "55 versus 552 items" 比较中，55 items 对应 1,296 conditions/item（总评估量 71,280/model），而 single-condition 仅 552/model。Abstract 提及推荐 3×3=9 conditions 设计，但 55 items 是 full 1,296-condition 下的数字。**推荐设计（9 conditions）下达到 G ≥ 0.80 需要多少 items 这一关键数字未报告。**

LLM 评估主要成本是推理计算量，item count 为中心的 framing 与实践者核心关切错位。此问题与 N1（exchangeability）叠加——如果 D-study budgets 的可靠性本身因模型 exchangeability 存疑而打折，而实际计算成本又被低估，核心实践建议可信度进一步下降。

**建议**：(a) §4.5 增加 total evaluation budget 对比表（items × conditions = total evals）; (b) Abstract 报告推荐设计下的 item budget; (c) 使用 "total evaluation budget" 框定效率增益。

**N3. [Critical → Warning, 部分改善] Format-associated pattern 呈现层级仍与证据强度不匹配** [R1-N2, R2 交叉 AGREE, 共识]

n = 5 benchmarks 的 exhaustive permutation test resolution floor 为 p = 0.10（C(5,2) = 10 种划分），benchmark-level CI spans zero ([-1.7, 5.1], df = 3)。

**改善点**：相比前几轮，format pattern 已从 Contributions 列表中移除，Abstract 措辞已弱化。
**残余问题**：§4.3 仍占完整 section + Table 3 + Figure 3，与经严格验证的 §4.4（precision separability）获得同等呈现空间。Abstract 仍提及 "observe a format-associated pattern"。

因已不在 Contributions 中，从 critical 降级为 warning，但建议进一步调整：§4.3 标题加 "Exploratory"，Abstract 使用更谨慎措辞。

### Should-Fix（影响评分但不一票否决）

**W1. Binary scoring limitation 影响被低估** [R1-W1 + R2-W4, 共识]

GSM8K partial-credit pilot 显示方差结构根本性改变：prompt 从 25.5% → 1.2%，G 从 0.770 → 0.553，item difficulty ranking ρ = 0.26。但 pilot 仅 1 个模型（Llama），无法估计 model-related 方差分量（binary 下 ~30%）。Conclusion 的 D-study budgets 未限定适用范围为 binary scoring——Section 3.5 末尾有此 caveat，但 Abstract/Conclusion 缺失。

**建议**：Conclusion 加 "under binary correctness scoring" 和 scope qualifier; Limitations 重点强调 metric-conditional budgets。

**W2. D-study projection invariance 假设讨论不充分** [R1-W2, R2 交叉 AGREE, 共识]

三个 invariance 威胁未充分展开：(1) item pool expansion（其他 47 个 MMLU subjects）; (2) model universe expansion（加入 1B/70B 模型）; (3) temporal drift（模型代际更替）。"Order-of-magnitude guides" 缺乏量化含义。

**建议**：§4.5 扩展 Projection assumptions 段落，量化 "order-of-magnitude" 含义（如 bootstrap CI 范围 ≈ ×1.5-3×），建议定期重估方差分量。

**W3. 200-item stratified sample 代表性验证不完整** [R1-W3, R2 交叉 AGREE（降低 severity）, 共识]

10/57 MMLU subjects，CV = 3.1% 验证 sampling variance 非 representativeness。分层抽样覆盖 4 学科领域，"order-of-magnitude" 定位部分缓解。

**建议**：报告 10 subjects vs full 57 subjects 在 accuracy/difficulty variance 上的比较。

**W4. exp-002 跨基准设计不对称性** [R1-W4, R2 交叉 AGREE, 共识]

Ordering 仅在 MMLU 操控，prompt 在 MC/FF 间语义不同（MC: 选项格式; FF: CoT elicitation strategy）。MC vs FF 方差结构差异可能部分源于设计结构差异。

**建议**：§4.3 明确讨论设计不对称性作为 confound。

**W5. 跨 benchmark 分析缺乏解释性深度** [R2-W5, R1 partially agree, 部分共识]

MC vs FF 差异仅描述性报告，未分析 item 特征如何驱动 model×item 交互。R1 认为属 future work 但同意 §4.3 应增加机制讨论。

**建议**：§4.3 增加 1-2 段关于 FF 方差分散可能机制的讨论。

---

## Reviewer Consensus [AGREE]

1. **Model exchangeability / narrow target universe**：LOMO + forward prediction 均为 within-sample，不足以保证 D-study budgets 的 out-of-sample 可迁移性。Abstract/Conclusion 需加 scope qualifier。
2. **Cost framing**："10× fewer items" 隐藏了总评估量的大幅增长，推荐设计的实际 item budget 是读者最需要的数字但未报告。
3. **Binary scoring limitation**：partial-credit pilot 显示方差结构根本性改变，budgets 的 metric-conditional 性质需在 Conclusion 中明确声明。
4. **Format pattern 呈现**：已从 Contributions 移除（改善），但 §4.3 的呈现空间仍与证据强度不匹配。
5. **Design asymmetry**：exp-002 跨 benchmark 的 facet 不对称性可能混淆 format effect。

## Reviewer Divergence [REBUT]

1. **新颖性 vs Messing (2026)**：
   - R2（W3, warning）：增量主要是"更多 facet + 更多 benchmark"，概念上是标准 G-theory 的直接扩展，新颖性有限。
   - R1（REBUT）：交叉 infrastructure + methodology 的联合分析不是 trivial extension——只有同时交叉才能发现 precision 可忽略、seed/temperature 的 item-conditional 效应。D-study calculator 作为 resource 有独立价值。对 EMNLP 这样以应用为导向的 venue，构成充分贡献。
   - **Director 判断**：R1 的反驳有理。论文的价值不在方法论创新而在首次系统应用+可操作工具。但 R2 的关切也合理——如果定位为"应用+工具"论文而非"方法创新"论文，framing 应相应调整。

---

## Questions（需作者澄清）

1. **推荐 3×3 设计在 G ≥ 0.80 时需多少 items？** 这是解决 cost framing 问题的关键数字。[R2-Q1, R1 交叉 AGREE]
2. **|ΔG| = 0.035 对应的 D-study budget 变化是多少？** 如 55 items → ? items。[R1-Q3]
3. **模型视为 fixed facet 时 G 和 budget 如何变化？** Table 6 的 ΔG = 0.077-0.113 确认 random 假设产生 conservative budgets，但需讨论绝对影响。[R1-Q2]
4. **GLMM vs Henderson I 方差分量的绝对值差异？** Appendix A 报告 <0.3pp，但对小分量（如 model = 2.5%）相对误差可达 12%。[R1-Q1]
5. **Section 4.6 G_obs = 0.71 (sub-family) 是否意味着 budgets 仅对跨架构比较有效？** [R2-Q6]

---

## Missing References

- **Gao et al. (2024)** lm-evaluation-harness — 作为 de facto 评估工具，实践建议应讨论与其默认协议的关系 [R2, R1 交叉 AGREE]
- **Cardinet, Johnson & Pini (2010)** "Applying Generalizability Theory using EduG" — G-theory 应用方法论参考 [R1 建议, 非必需]
- **Kunievsky and Evans (2025)** — 引用准确性需作者确认 [R2]

---

## External Review

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

**状态**: done（2026-05-22 14:23 → 14:26, ~3 min）

| 严重性 | 位置 | 发现 |
|--------|------|------|
| Warning | Page 2 | Figure 1 axis labels/legend/tick labels 字号偏小（≤6pt），作为论文第一个视觉锚点可读性重要 |
| Warning | Page 3-4 | 连续两页纯文本（Related Work → Method 3.1），无 display item。建议将 Figure 2 从 page 5 前移 |
| Info | Page 5 | Figure 2 面积较小，仅占左栏 ~1/3 高度，可适当放大 |
| Info | Page 7 | Figure 3 堆叠柱状图建议确认灰度打印时仍可辨别（hatching pattern） |
| Info | Page 7 | Table 3 Bold 标记规范，所有表格 booktabs 风格，专业 |
| Info | Page 5-8 | Float 位置合理，无漂移 |
| Info | Page 1-14 | 未发现 margin 溢出、公式渲染错误、未解析引用 |
| Info | Page 9-10 | 参考文献格式统一 |

**总结**: 无 critical 排版问题。2 个 warning（Figure 1 字号、纯文本节奏）为可选改进。

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

**EMNLP 2026 评分标准**: 3.5 = Borderline Conference（介于可被主会议接收和 Findings 之间）

**置信度**: 4/5（两位 Reviewer 均 4/5，方法论和 venue 匹配度高）

**核心判断**:

论文在实验执行层面表现出色——7 facet fully crossed design 的规模（230 万记录）、8 项 robustness 检查的深度、D-study budget calculator 的实用价值在同类工作中均属领先。G-theory 框架对 LLM 评估方差的系统性分析填补了该领域的空白。

制约评分的三个核心问题：

1. **泛化边界不清晰**（N1）：D-study budgets 是论文最核心的实践贡献，但其可靠性取决于方差分量对 unseen models 的可迁移性——当前验证均为 within-sample，target universe 限于 7-9B instruct models 但 framing 更宽泛。

2. **Cost framing 误导**（N2）：headline claim "10× fewer items" 隐藏了总评估量的 129× 增长，推荐设计（3×3）下的实际 item budget 未报告，使读者无法评估实际成本。

3. **Format pattern 证据不足**（N3, 已部分改善）：虽已从 Contributions 移除，但 §4.3 的呈现空间仍与 n=5 的统计基础不匹配。

**修改后预期**：如果作者 (a) 补报推荐设计下的 total evaluation budget, (b) 在 Abstract/Conclusion/标题中限定 target universe, (c) 提供 out-of-sample model 的 sensitivity analysis 或更充分的泛化论证，论文可达 4.0 (Conference) 水平。当前版本推荐 Findings。

---

## Detailed Comments（逐节）

### Abstract
- "55 versus 552 items" 数字绑定 1,296 conditions，需报告推荐设计（9 conditions）下的对应数字
- "open-weight" 无限定词，建议改为 "open-weight 7-9B instruction-tuned"
- "observe a format-associated pattern" 可进一步弱化为 "observe suggestive but statistically underpowered differences"

### Section 1 (Introduction)
- Contributions 列表已改善（format pattern 不再列为独立贡献）
- Contribution 1 "10.0× fewer items" 需 cost context

### Section 2 (Related Work)
- Positioning 段落 vs Messing (2026) 的对比基本充分，但可更明确将 Messing 定位为 direct precursor
- 缺少 lm-evaluation-harness (Gao et al., 2024) 引用

### Section 3 (Method)
- §3.1 G-theory 背景介绍清晰，σ²_τ/σ²_δ 建议用独立公式编号 [R2-P1]
- §3.2 seed 42 选择建议简要说明为任意选取 [R1-M1]
- §3.5 target universe 定义已改善（"7-9B instruction-tuned"），random vs fixed model 对比有价值

### Section 4 (Experiments)
- §4.1 single-model baseline 清晰完整
- §4.2 "(1.1 c.u., 1.0)" 含义不明，需定义 [R2-P4]；Table 2 "all others: 0.0" 改为 "<0.1%" [R1-M2, R2-P2]
- §4.3 建议标题加 "Exploratory"；增加设计不对称性讨论和 FF 方差分散机制
- §4.5 需增加推荐设计的 total evaluation budget 对比表；Projection assumptions 段落需扩展
- §4.6 "Preliminary Scale Validation" 定位合理，G_obs = 0.71 的含义需更突出讨论

### Section 5 (Conclusion)
- D-study budgets 建议需加 "under binary correctness scoring" 和 "for 7-9B instruction-tuned models" scope qualifiers
- "10× fewer items" 需附带 total evaluation cost context

### Section 6 (Limitations)
- 覆盖面合理（model scope, binary scoring, benchmark sample, temporal correlation）
- 建议增加：D-study budgets 的 metric-conditional 性质；推荐设计的 total computation cost

### References
- Anonymous (2025) arXiv:2601.00822 存在潜在匿名性风险 [R2-P5]

### Appendix
- Appendix A robustness 分析全面
- Appendix E prompt templates 建议标注设计理由 [R1-M4]
- 建议在 Appendix 中增加全 5 benchmark D-study 曲线图 [R2-P3]