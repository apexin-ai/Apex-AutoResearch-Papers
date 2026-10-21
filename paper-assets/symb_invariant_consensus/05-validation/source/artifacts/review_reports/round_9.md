---
round: 9
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T01:20:27.502522+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 12 审稿报告

## Summary

本文提出 SICA（Symbolic Invariant Consensus Aggregation），通过从 LLM 推理 trace 中自提取逻辑约束并用 MAX-SAT 聚合来扩展 Self-Consistency。核心发现是负面结果：自提取约束继承模型偏差（"symbolic confirmation bias"，BR=4.97×），27 种修复策略全部失败。跨架构 NLI 验证提供逃逸路径（ProofWriter +6.67pp），DRC 自适应路由方法恢复 83-90% 增益。实验规模令人印象深刻（11 模型、3 数据集、27 策略），oracle 控制设计精妙（+29.90pp），但核心新颖性不足、统计功效偏低、标题 overclaiming 制约了论文水平。

## Strengths

1. **实验规模和系统性出色**：6 个开源模型 + 5 个 frontier 模型、3 个逻辑推理数据集、27 种修复策略（12 principled + 15 参数变体）、4-seed replication、TOST equivalence tests——对负面结果论文来说覆盖面突出。[R1/R2 共识]

2. **Oracle 控制设计精妙**：用 FOLIO/ProofWriter 的 gold FOL annotations 替换自提取约束，展示 +29.90pp/+17.17pp 增益，精确定位瓶颈在 extraction 而非 MAX-SAT/Z3 mechanism。自提取仅捕获 ~12% 的 oracle ceiling。这是论文最有说服力的部分。[R1/R2 共识]

3. **CJT 框架提供清晰理论语言**：Condorcet Jury Theorem 的 independence assumption 解释了 SC plateau 和 SICA 失败，比纯经验描述更有洞察力。K_eff 作为 ordinal diagnostic 的定位恰当。[R2 首提，R1 同意]

4. **诊断框架有实用价值**：C₀ < 5% 意味 SICA 退化为 SC、三类 failure mode（Type A/B/C）、process-level independence 分析——对后续研究有参考价值。[R1]

5. **诚实的局限性披露**：论文在 Limitations 中详细讨论了统计功效、单 seed、capability-gap 分析弱点、计算成本等。学术诚信值得肯定。[R1/R2 共识]

6. **BH 多重比较校正和 TOST 等价性检验**使用恰当，sensitivity 分析（±1/±2/±3pp margins, relative TOST）是良好的统计实践。[R1]

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical, 共识]** **标题 "Do Not Improve...from 7B to Frontier Scale" overclaiming**
- Frontier 模型（gpt-4o, gpt-4.1, gpt-5.5, o3, Gemini-2.5-Pro）使用 Mistral-7B 做跨模型提取，不是 self-extraction。标题中 "Self-Extracted" 与 frontier 实验设计不匹配。
- 开源模型中 QwQ-32B 仅在退化条件（AIME n=22, GSM8K n=30, C₀<5%）上测试。有效实验范围集中在 7B-14B。
- **建议**：修改标题去掉 "to Frontier Scale" 或加限定词（如 "from 7B to 14B, with Cross-Model Evidence at Frontier Scale"）；Abstract/Introduction 明确区分 self-extraction 和 cross-model extraction。
- [R2 首提 N2, R1 AGREE]

**W2 [critical, 共识]** **SCB 核心新颖性不足——self-correction failure 在 FOL 载体上的实例化**
- Huang et al. (2024) 已证明 LLMs cannot self-correct without external feedback；Stechly et al. (2025) 证明 self-verification 不可靠；Wan et al. (2025) / Jhaveri et al. (2026) 研究了 CoT confirmation bias。SCB 是同一机制在不同载体（FOL 约束 vs 自然语言）上的实例化，非概念突破。
- Z3 验证通道的 provable soundness 是有趣切入点（证明瓶颈在提取而非验证），但更接近实验发现而非概念突破。99% 约束通过 Z3 语法检查却仍无用——这一点比 SCB 本身更有趣，应在 framing 中更突出。
- **建议**：(1) 降低 Contribution 1 的 novelty claim 调门；(2) 重新定位贡献重心为量化诊断体系（BR=4.97×, K_eff, C₀）和实验规模（27 策略系统排除）；(3) 突出 formal channel 下 SCB 的 non-obvious 之处。
- [R2 首提 N1, R1 AGREE with nuance: 量化贡献不应低估]

**W3 [critical, 共识]** **统计功效 <21% 无法支撑"无效果"核心结论**
- McNemar 在 n=200-600 条件下检测 |Δ|=2pp 效应的功效 <21%。16 个非退化条件中 10 个 TOST "underpowered"。最大研究（n=804）MDE=1.86pp，但观测 Δ=+0.25pp。
- 标题 "Do Not Improve" 将"检测不到效果"等同于"没有效果"，不被 power<21% 支撑。
- R2 补充 nuance：Abstract 正文措辞（"no evidence of improvement...ten conditions remaining underpowered"）实际较审慎；aggregate pattern（16/16 无显著正面）仍有信息量，可补充 meta-analytic sign test。
- **建议**：(1) 标题和 Contribution framing 使用更审慎措辞；(2) 报告各条件可排除的效应大小范围；(3) 补充 aggregate sign test。
- [R1 首提 N1, R2 AGREE]

**W4 [critical, 共识]** **单 seed 复制严重不足**
- 唯一 4-seed 复制（Mistral-7B FOLIO）Δ 范围 +3.43 到 -0.49pp（~4pp 跨度），超过 TOST ±2pp 边界。温度敏感性也显示 T=0.7 是"孤立峰"。其他单 seed 条件可靠性存疑。
- R2 补充：aggregate pattern（16/16 无正面）在 seed variance 下仍有信息量——如果 SICA 真有 2-3pp 正效果，16 条件全无显著正面不太可能。建议补充 meta-analytic 分析。
- **建议**：至少对 3-4 个关键条件做多 seed 复制，或明确降低单 seed 结论强度。
- [R1 首提 N2, R2 AGREE]

**W5 [critical, 共识]** **Capability-gap 分析证据过于薄弱**
- Spearman ρ=1.0, p=0.003, 但 n=6 且 4/6 共享 DeBERTa verifier。Verifier-collapsed 分析（n=3 独立 verifier）p=0.167，不显著。Process-κ gradient 也只有 n=5。
- Introduction/Conclusion 以 p=0.003 呈现，但 Limitations 承认 p=0.167——framing 不一致。
- **建议**：(1) 增加更多独立 NLI verifier 架构（≥5 独立 verifier）；(2) 正文中引用 p=0.003 时同步报告 collapsed p=0.167 作为 robustness check；(3) 使用 "consistent empirical pattern rather than statistically confirmed law" 的措辞（论文 Limitations 已有，需一致化到正文）。
- [R1 首提 N3, R2 AGREE = R2-W3]

**W6 [critical, 共识]** **DRC 作为 Contribution 4 不够充分**
- DRC 本质是基于 trace agreement 阈值 τ 的 confidence-based routing，标准 cascade 设计。τ=0.7 仅在 2 个数据集验证（ProofWriter 选择, FOLIO held-out），τ 敏感性分析缺失。
- full-combo gain 本身仅在 Mistral-7B（最弱模型）上显著；对更强模型 full-combo 就不显著，DRC 无从发挥。
- **建议**：将 DRC 降级为 §6 的 practical observation，不作为独立 Contribution 编号；或增加 routing 策略对比和 τ 敏感性分析。
- [R2 首提 N3, R1 AGREE]

### Should-Fix（影响评分但不一票否决）

**S1 [warning, 共识]** **BR 可能存在循环论证**
- 56.4% 约束零变量重叠，约束几乎按定义"支持"source trace 的答案。BR=4.97× 中多少是提取设计产物 vs 模型级 bias 未被区分。
- **建议**：做控制实验——随机 shuffle 约束-trace 映射后计算 BR，量化 "design artifact" 成分比例。
- [R1 首提 W1, R2 AGREE: 重要遗漏]

**S2 [warning, 共识]** **CIL 名称和 information-theoretic 声称有误导**
- "Cumulative Information Lift" 实际是 log-odds ratio，非互信息/KL 散度。"Cumulative" 无体现。"unify" 过强（仅经验相关，无数学推导关联 K_eff/BR）。n=8 非独立样本上 ρ=0.881 可能受 outlier 影响。
- **建议**：重命名为 "Conditional Correction Ratio" 或类似；删除 "unify" 措辞；添加 leave-one-out sensitivity。
- [R1 首提 W2, R2 AGREE]

**S3 [warning, 共识]** **Independence-Accuracy Trade-off（Contribution 2）framing 问题**
- K_eff 是 Kish design effect 的直接应用，BR 是条件概率比，C₀ 是 zero-cost filter。各自简单直观，价值在组合应用到 LLM 自提取场景，更像 Contribution 1 的量化工具集。
- **建议**：将 Contribution 2 重新措辞为"量化诊断工具集"，降低 "trade-off" 的发现性措辞。引用 Krogh & Vedelsby (1994) 明确不是新发现。
- [R2 首提 W1, R1 AGREE]

**S4 [warning, 共识]** **Figure 2（27 strategies summary）placement 问题**
- 在 §5.6（page 7）引用但实际出现在 page 25。核心贡献的视觉支撑不应在 appendix。
- **建议**：调整 LaTeX placement 确保 Figure 2 出现在 §5.6 附近。
- [R2 首提 W4, R1 AGREE; 视觉审查也确认]

**S5 [warning, 共识]** **Appendix ~18 页，关键信息分配不合理**
- Table 15（frontier SCB, 9 models）支撑标题级 claim 却在 appendix。主文 8 页仅 3 个 display items（1 figure + 2 tables），密度偏低。
- **建议**：合并 Discussion+Conclusion 省空间；将 Table 15 和 capability-gap scatter plot 移入正文；精简 Case Studies 和 Extraction Error Taxonomy。
- [R2 首提 W5, R1 AGREE; 视觉审查也确认]

**S6 [warning, 分歧]** **27 策略 scope 限定——排除 trained extractor**
- R1 观点：Oracle +29.90pp 显示 trained extractor 最有前途，排除后 "all fail" 有误导。
- R2 反驳：研究问题明确界定为 zero-cost 自提取修复，trained extractor 改变 setup。"all fail" 指 27 种自提取策略，scope 准确。
- **Director 判断**：R2 反驳有理——研究问题的 scope 限定是合理的。但 Abstract 中应明确 scope 限于 training-free interventions，避免读者误解。
- [R1 W4 vs R2 REBUT; 部分共识]

**S7 [warning, 分歧]** **K_eff 用 κ 替代 ICC 验证充分性**
- R1 观点：κ 和 ICC 测量不同东西，r=0.625 只是中等相关，正文多处将 K_eff 作字面有效样本量使用。
- R2 反驳：论文已定位为 ordinal diagnostic，r=0.625 对排序足够，K_eff 不是核心结论。
- **Director 判断**：R2 反驳有理——K_eff 作为 ordinal diagnostic 的定位已足够审慎。但正文中偶有逾越（如 "traces beyond a dozen add negligible independent information"），应统一限定为排序用途。
- [R1 W5 vs R2 REBUT; 部分共识]

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：

1. 标题 overclaiming（frontier 用 cross-model extraction, "Do Not Improve" 过于绝对）
2. SCB 新颖性不足（self-correction failure 的 FOL 实例化，非概念突破）
3. DRC 贡献不足以作为独立 Contribution
4. 统计功效 <21% 制约"无效果"结论的强度
5. 单 seed 复制不足（~4pp 跨 seed 波动）
6. Capability-gap n=6 证据薄弱（collapsed p=0.167）
7. CIL 名称误导（log-odds ratio ≠ information-theoretic quantity）
8. BR 可能存在循环论证（提取设计产物 vs 模型级 bias）
9. Figure 2 和 Table 15 应在正文而非 appendix
10. Oracle 控制设计精妙（论文最有说服力的部分）
11. 实验规模和 Limitations 诚实性值得肯定

## Reviewer Divergence

以下问题存在分歧：

1. **27 策略是否应包含 trained extractor**：R1 认为排除最有前途方向后 "all fail" 有误导（W4）；R2 认为 zero-cost scope 限定合理（REBUT）。**Director 倾向 R2**——研究问题 scope 合理，但 Abstract 应明确限定。

2. **K_eff 验证充分性**：R1 认为 κ→ICC 替代验证不充分（W5）；R2 认为 ordinal diagnostic 定位已足够（REBUT）。**Director 倾向 R2**——但正文应避免将 K_eff 作字面有效样本量使用。

3. **Cross-architecture escape 证据宽度**：R2 认为仅 ProofWriter 显著（W3）；R1 partial REBUT（FOLIO 不显著可能是 power 问题而非方法问题）。**Director 判断**——两者都有道理，原因是混合的（power + task alignment）。

4. **Conclusion 长度**：R1 认为 4 行过短；R2 认为 8 页限制下 Discussion+Conclusion 分离可接受。**Director 倾向 R2**——但合并可省空间给更重要的 display items。

5. **Abstract 信息密度**：R2 认为偏高；R1 REBUT（负面结果论文需完整传达核心信息）。**Director 倾向 R1**——当前密度对快速评估论文价值是必要的。

## Questions（需要作者澄清）

1. **BR 循环论证控制实验**：如果随机打乱约束-trace 映射后 BR 是多少？这能量化 BR 中"提取设计产物"的比例。[R1 Q1, R2 AGREE]

2. **Frontier self-extraction 可行性**：gpt-4o 在 Table 15 标记为 self-extraction ($^a$)，其他 frontier 标记为 cross-model ($^b$)。为什么不对所有支持 structured output 的 frontier 模型做 self-extraction？[R2 Q1]

3. **Trained extractor 是否消除 SCB**：用 oracle annotations 微调小模型作为 extractor，SCB 是否会消失？这是否是本文最重要的 limitation？[R2 Q2, R1 同意]

4. **CIL robustness**：ρ=0.881 (n=8) 的 bootstrap CI？去掉最强 pair（Mistral×DeBERTa-PW）后相关性是否保持？[R2 Q3, R1 AGREE]

5. **DRC τ 敏感性**：τ ∈ {0.5, 0.6, 0.7, 0.8, 0.9} 的 Pareto 曲线？ProofWriter 选择 τ=0.7 在 FOLIO 上的最优 τ 是否相同？[R1 Q4]

6. **Seed 方差 vs Table 1**：4-seed ~4pp 波动是否使 Table 1 单 seed 结果基本不可解释？是否考虑 aggregate sign test 补充 meta-analytic 证据？[R1 Q5, R2 nuance]

7. **FOLIO Unknown 类处理**：FOL 约束如何处理 open-world semantics 的 Unknown？[R1 minor]

8. **非命题约束**：99% 约束是命题级的。引导模型生成真正的一阶逻辑约束是否可能改善结果？[R1 Q2]

## Missing References

R2 在 Round 11 中标记了遗漏引用（Byerly & Khashabi 2026 TACL, arxiv:2604.07650 等），本轮未重新核查引用完整性。论文当前 ~48 citations，Related Work 覆盖面整体较广。[R2 优势 #4]

## External Review (Stanford Agentic Reviewer)

**状态：未请求**。项目配置中外部审稿未启用。

## Visual Layout Check（非评分项）

视觉审查已完成（3 warnings, 13 info, 0 critical）。

**Warnings：**
1. Pages 1-2 连续纯文本无 display item，第一个视觉锚点（Figure 1）在 page 3 顶部。
2. 主文 8 页仅 3 个 display items（1 figure + 2 tables），密度偏低（通常 5-8 个）。Figure 2 被放在 appendix page 25。
3. Page 25 Figure 2 上方 ~1/3 空白。

**Info（摘要）：**
- Table 1 (page 6) 使用 booktabs 风格，行分组清晰。
- Appendix 排版整洁（Algorithm 1-2、prompt templates、多个 tables）。
- References 无未解析引用 [?]。
- Page 26 有 5 个 figures 密集排列，axis labels 偏小。

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 加权共识 |
|------|----|----|----------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | 3.5 | 4.0 | 3.5 |
| Overall | 3.5 | 3.0 | 3.0 |
| Confidence | 4 | 4 | 4 |

**评分理由：**

论文的实验规模和方法论严谨程度值得肯定（Soundness 3.5），oracle 控制设计精妙，Limitations 节诚实全面。但多个关键弱点将论文限制在 Findings 水平：

1. **新颖性不足**（Excitement 2.5）：SCB 是 self-correction failure（Huang 2024）在 FOL 载体上的实例化，可从已有文献合理预期。主要贡献在量化深度（BR=4.97×, 27 策略系统排除）而非新现象发现。DRC 是标准 cascade 设计，不构成方法论创新。

2. **标题和 framing overclaiming**：标题声称 "from 7B to Frontier Scale" 但 frontier 实验非 self-extraction；"Do Not Improve" 绝对否定不被 power<21% 支撑；Contribution 2 是 Kish design effect 的直接应用而非新发现。

3. **统计证据基础偏弱**：(a) 16/16 无显著正面但 power<21%，aggregate pattern 有信息量但未做 meta-analytic 分析；(b) 4-seed 复制仅 1 个条件，~4pp 跨 seed 波动使单 seed 结果不可靠；(c) capability-gap 核心正面贡献的 collapsed p=0.167 不显著。

4. **正面贡献证据偏窄**：Cross-architecture NLI 仅在 ProofWriter (Mistral-7B) 上显著（BH 校正后）；DRC 在 2 个数据集上验证不足。

**接收建议**：建议作为 **Findings paper** 接收，条件是修复标题 overclaiming、降低 SCB novelty claim、将 DRC 降级、统一正文与 Limitations 的 statistical framing。如果完成这些修改并补充 BR 控制实验和 aggregate sign test，有潜力升级为 Borderline Conference。

## Detailed Comments

### Section-by-Section

**Abstract**: 信息密度高但核心信息完整。需要：(1) 修改 "from 7B to Frontier Scale" 措辞；(2) 明确 27 strategies 的 scope 限于 training-free interventions；(3) "we find no evidence of improvement" 虽比标题审慎但应加 underpowered caveat。

**Introduction (§1)**: 叙事结构清晰（SC 瓶颈 → CJT → SICA → 失败 → 诊断 → 逃逸）。需要：(1) 更早建立 formal channel distinction（Z3 provably sound, failure in extraction not verification）；(2) Contribution 2 承认是量化而非新发现；(3) Contribution 4 (DRC) 降级或加深。

**Related Work (§2)**: 覆盖面广，~48 citations，5 个段落。Neuro-symbolic 三分类法（Specification/Program/Trace）是有用的组织框架，但应标注为作者分类而非 established taxonomy。与 Huang 2024 / Stechly 2025 / Wan 2025 的区分需在 Introduction 更早建立。

**Background & Setup (§3)**: SICA pipeline 形式化完整（Eq. 1-5, Algorithm 1-2）。"Empirical Finding 1/2" 的定位恰当（相比此前版本的 Proposition/Bound 已改善）。"Symbolic Mirage Hypothesis" 命名偏 dramatic，建议改为 "Symbolic Bias Inheritance" 或 "Extraction Bias Hypothesis"。CIL 应重命名并降低 "unify" 声称。

**Experiments (§4)**: Table 1 结构清晰，regime 分组有信息量。GSM8K (n=30) 和 AIME (n=22) 作为 degenerate 条件放在主表中可能给读者统计错觉——建议移至 appendix 或脚注。4-seed replication 仅 1 个条件，是最大统计弱点。

**Analysis (§5)**: SCB 分析（BR=4.97×, 83.3% 约束支持错误答案）是论文最有力的分析，但 BR 可能存在循环论证。Process-level independence（cosine 0.69 > κ 0.46）分析有洞察力。27 策略汇总 Figure 应在正文。

**Cross-Architecture (§6)**: ProofWriter +6.67pp (p<0.001) 是实质性结果。Capability-gap 分析有趣但 n=6 + shared verifier 制约结论强度。DRC τ=0.7 缺 sensitivity 分析。

**Discussion (§7)**: 简洁有效。可与 Conclusion 合并省空间。

**Conclusion (§8)**: 4 行过于简短。建议合并到 Discussion 末尾。

**Limitations**: 全面诚实，覆盖 power、single-seed、capability-gap、计算成本等。是论文的优点。

**Appendix**: ~18 页，内容丰富但 Table 15（frontier SCB）和 Figure 2（27 strategies）应在正文。Page 26 的 5 个 figures 偏小偏密。
