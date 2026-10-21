---
round: 1
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T20:57:45.233137+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — "Not All Policy Ambiguity Is Equal: Differential Vulnerability Profiles Across LLM Agent Families"

**Venue**: EMNLP 2026 (via ARR August commitment)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: R1 (方法严谨性) + R2 (新颖性与完整性)
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文通过 matched-pair 实验设计，在 τ²-bench 上系统研究 6 种 policy ambiguity 类型对 5 个 LLM agent family 安全违规率的因果效应（2,997 episodes）。主要发现：(1) 歧义整体增加 34.0 pp 违规率（C1, OR=15.1）；(2) 三层类型层级 incompleteness > mid-cluster > coreferential（C2）；(3) 显著的 model×type 交互效应（C4）。实验方法论在 agent safety 领域属上乘（matched-pair + perturbation control + ICC=0.919），但多个方法学问题制约核心结论的稳健性，且核心新颖性存在争议。

---

## Strengths

**S1 [consensus]. 精心设计的因果推断框架。** Matched-pair minimal-edit 设计（每类型 50 对 clause pairs，共 300 对），配合 perturbation control（Δ_perturb=3.33pp vs Δ_ambig=34.0pp）和 ICC 复现验证（0.919 [0.892, 0.940]），构成了在 agent safety 领域罕见的因果推断链。（§4.2, §4.4, §5.5）

**S2 [consensus]. 统计分析全面且规范。** McNemar's test（配对二元数据）、χ² + Cramér's V（omnibus）、Fisher's exact test（小样本）、TOST 等价检验、bootstrap CI（10,000 resamples）、logistic regression、Holm-Bonferroni 校正——覆盖从效应确认到效应量估计的完整链条。（§4.6）

**S3 [consensus]. Failure signature 分析提供机制解释。** 245 traces 的 failure mode taxonomy 揭示 "misparse-and-apply"（linguistic-layer）vs "guess-and-act"（specification-layer）的机制区别，超越纯 aggregate 统计，对工程实践有直接指导意义。（§6.1-6.2）

**S4 [consensus]. ICC 复现分析增强可信度。** Per-type ICC 揭示 linguistic-layer (0.976-0.989) vs specification-layer (0.807-0.857) 的可靠性差异，与理论预期一致。（§5.5）

**S5 [consensus]. 坦诚的 Limitations section。** Cross-judge asymmetry、incompleteness confound、failure mode analysis 覆盖范围限制等均被明确讨论。C3 在 within-judge subgroup 不显著的事实在正文报告。（§Limitations）

**S6 [consensus]. 与 concurrent work 的定位清晰。** Table 1 系统对比 DRIP-R、PolicyBank、MANTRA、PhantomPolicy 等 2026 年 concurrent work。（Table 1）

---

## Weaknesses

### Must-Fix 问题（4 项共识 + 1 项分歧）

**N1 [critical, consensus]. Cross-judge confound 对 C3 和部分 C4 构成威胁。**
GPT-5.4 由 GPT-4.1 评判，其余模型由 GPT-5.4 评判——judge identity 与 model identity 完全混淆。C3（layer effect）在两个 within-judge subgroup 中均不显著（GPT-4.1-judged: p=0.059; GPT-5.4-judged: p=0.157），pooled p=0.017 可能是 judge-level variance 的产物。C4 中涉及 GPT-5.4 的跨 judge 比较（如 GPT-5.4 authorization scope 64% vs Claude 12%）无法排除 judge bias。正文多处直接比较五个模型的绝对违规率而未加 caveat。
→ **要求**: (1) 限定 C3 为 inconclusive; (2) C4 严格区分 within-judge vs between-judge 比较，后者系统性弱化; (3) 考虑第三 judge 交叉验证或人类评估标定。

**N2 [critical, consensus]. TOST equivalence margin 缺乏依据。**
C2 三层类型层级的核心证据依赖 TOST 等价检验，使用 ±15pp 和 ±10pp margin 但未给出任何理论或经验依据。Margin 直接决定 tier boundaries：缩小到 ±8pp 可能分裂 mid-cluster，扩大到 ±20pp 可能坍缩为两层。
→ **要求**: (1) 论证 margin 选择; (2) 报告 ±8/10/12/15/18/20pp 的 sensitivity analysis; (3) 或改用 effect size + CI overlap 的无 margin 方法。

**N3 [critical, consensus]. Incompleteness confound — 信息添加 vs 歧义消解。**
5 种歧义类型的 unambiguous variant 通过改写措辞消除歧义（information content 不变），但 incompleteness 的 unambiguous variant 必然添加新的 policy 规定（因其定义就是 "missing information"）。49.2pp 的效应量混淆了 (a) 歧义导致的违规和 (b) 信息缺失导致的违规。Incompleteness 是三层层级的 top tier 核心成员，如果效应被信息添加 inflate，整个层级结构的解读将改变。R2 称这是"两份审稿中最有洞察力的发现"。
→ **要求**: (1) 报告去除 incompleteness 后剩余 5 类型的 hierarchy 分析; (2) 设计 information-addition control; (3) 正文标注 incompleteness Δpp 的上界性质。

**N4 [critical, consensus]. 正文超过 8 页限制。**
Conclusion (§8) 从 page 8 底部开始，延续到 page 9 约 10-15 行后才进入 Limitations section。EMNLP 2026 规定 long paper 正文严格 8 页（Limitations 不计），违反此 hard constraint 可能导致 desk reject。
→ **要求**: 压缩 §7 Discussion 或 §8 Conclusion（disambiguation channel framework 细节可移入 Appendix）。

**N5 [critical, divergence]. 核心新颖性有限 — "Differential Nocuity" 是否为理论突破。**
R2 认为"不同模型对不同歧义类型反应不同"从先验角度几乎 trivially true，DRIP-R 已有类似 high-level observation，论文缺少 WHY 的理论解释。R1 反驳：high-level not surprising ≠ specific patterns trivially expected——incompleteness 的 universal danger vs authorization scope 的 model-differentiating 特性先验不显然；Systematic Nocuity（41.3% convergent-but-wrong）是真正新颖的概念；canary type 有操作化价值。双方同意 WHY 层面的 mechanistic explanation 需要加深。
→ **要求**: (1) 弱化 "governing principle" 为 "empirical regularity"; (2) 补充 type×model 交互的 mechanistic explanation; (3) 更清晰阐述与 DRIP-R 的增量贡献。

### Should-Fix 问题（10 项）

**W1 [consensus]. Perturbation control 检验力不足。** n=120, MDE≥15pp, CI 上界 13.33pp。5-14pp 范围内的 prompt sensitivity confound 无法排除。建议 n≥300 或在讨论中承认此限制。

**W2 [consensus]. Error analysis ICR 指标选择。** 仅报告 Gwet's AC1=0.78，未报告 Cohen's κ。AC1 在 marginal distribution 极度倾斜时给出比 κ 更高的值（prevalence paradox）。建议同时报告两个指标并说明选择理由。

**W3 [consensus]. 4-tier severity 二值化缺乏 sensitivity analysis。** 主分析将 none/minor/moderate/critical 二值化为 violation vs no-violation。未报告 moderate+critical 阈值下的结论是否一致。

**W4 [consensus]. ICC 复现分析子集代表性不明。** 30 pairs × 2 models × 3 replicates 的选择标准未说明。建议报告选择方法和 per-type ICC。

**W5 [consensus]. Clause pair 构造的 inter-annotator agreement 缺失。** 300 对经两名 NLP annotator 审查，但初始一致率、分歧解决机制、修改比例均未报告。

**W6 [consensus]. 多重比较校正范围不明确。** "Holm-Bonferroni where multiple comparisons are made" 过于模糊。C3 的 p=0.017 在全 family 校正后是否仍显著？

**W7 [partial consensus]. Ambiguity Blindness 操作化定义方法论细节不足。** Coding 是自动还是人工未说明，coding ICR 缺失。R2 认为 surface adoption 可能是 pragmatically appropriate，R1 反驳在客服场景中 escalation 才是 appropriate。建议披露 coding methodology 并讨论此区分。

**W8 [consensus]. 引用错误。** τ²-bench 作者 Victor Barres 写成 Sebastien，其余作者用 "Others" 占位。Lassiter & Goodman 年份需核实（2015 vs 2017）。ferrari_defects 第一作者应为 Rosadini 非 Ferrari。

**W9 [partial divergence]. Taxonomy 衍生性。** R2 认为是 curation 非 creation。R1 认为 principled selection + two-layer integration 有方法学价值。建议弱化作为独立 contribution 的权重。

**W10 [divergence]. EMNLP venue fit。** R2 认为主要贡献偏 AI safety，CL 语言学深度不足。R1 认为 EMNLP scope 足够宽广（同类 agent safety 工作已被接收），但同意加强 linguistic mechanism 分析会增强 venue fit。Director 将此归为 warning 而非 critical——论文有 CL 连接（taxonomy、scope misapplication、good-enough processing），但可以更深入。

---

## Reviewer Consensus

以下问题双方达成一致 [AGREE]：

1. **方法论是核心优势**: Matched-pair + perturbation control + ICC 的组合在 agent safety 领域罕见且有效
2. **C1 (binary effect) 稳健**: OR=15.1, 34.0pp, 所有模型和类型均显著
3. **Cross-judge confound 是最大方法学弱点**: 影响 C3 和部分 C4 的可靠性
4. **TOST margin 需要论证**: C2 的稳健性未经 sensitivity analysis 验证
5. **Incompleteness confound 影响 C2**: 设计层面的问题，需要补充分析
6. **页数超限必须修复**: desk reject 风险
7. **引用错误必须修正**: τ²-bench 作者信息不正确
8. **WHY 的理论解释需要加深**: 两位 Reviewer 均认同
9. **Failure signature 分析有价值**: misparse-and-apply vs guess-and-act 的机制区分超越了纯统计结果
10. **Limitations section 坦诚**: 比同领域大多数论文更透明

## Reviewer Divergence

1. **Overall score**: R1: 3.5 (Borderline Conference) vs R2: 3.0 (Findings)
   - 核心分歧: R1 更重视方法论质量和 specific pattern 的 empirical value; R2 更重视理论突破性和 venue fit
   - R1: "如果 N1-N3 得到充分回应，有望达到 Conference"（conditional 3.5→4.0）
   - R2: "N1-N3 中至少 3 个需要新实验，当前 submission 无法充分回应"（firm 3.0）
   
2. **新颖性**: R1 认为 specific patterns + Systematic Nocuity 超过 Findings 标准; R2 认为 high-level claim 是 trivially expected，specific patterns 是 "useful quantification" 非 "discovery"

3. **Venue fit**: R1 认为 EMNLP scope 覆盖 agent safety（有先例）; R2 认为缺乏 linguistic mechanism 的深入分析

4. **"Confirming causation" 措辞**: R1 认为过强（suggest "supporting"）; R2 认为在 matched-pair 设计下 defensible

---

## Questions（需要作者澄清）

1. TOST margin ±8/10/12/15/18/20pp 下 C2 三层层级是否稳健？
2. 去除 incompleteness 后，剩余 5 个类型的 type hierarchy 是否仍显著？是否仍为多层结构？
3. 为什么 incompleteness 是 universally dangerous 而 authorization scope 是 model-differentiating？能否提供 mechanistic explanation？
4. ICC 30 pairs × 2 models 如何选择？per-type replication 结果？
5. Cohen's κ 是多少？Prevalence index 和 bias index？
6. Severity threshold 改为 moderate+critical 后 C1-C4 如何变化？
7. 模型 API 的确切调用时间和版本？
8. 使用原始 τ²-bench 还是 τ²-Bench-Verified 版本？
9. Ambiguity Blindness coding 是自动还是人工？ICR？
10. 与 DRIP-R 的 type×model 交互分析相比，本文能得出哪些 DRIP-R 无法得出的具体结论？

---

## Missing References

两位 Reviewer 共推荐 7 篇遗漏文献：

1. **Koenig et al. (2024)** "How Well Do LLMs Handle Ambiguity?" — 直接测量 LLM 歧义处理能力
2. **Liu et al. (2023)** "We're Afraid Language Models Aren't Modeling Ambiguity" — LLM 单一解读倾向，与 Ambiguity Blindness 直接呼应
3. **Lakens (2017)** "Equivalence Tests: A Practical Primer" — TOST 方法学标准参考
4. **AgentSpec (Poskitt et al., ICSE 2026)** — Agent policy enforcement，Related Work 应讨论
5. **Hu et al. (2023)** Pragmatic reasoning in LLMs — Ambiguity Blindness 的 pragmatic failure 角度
6. **Pan et al. (2025)** Specification gaming — 与 policy ambiguity exploitation 相关
7. **Pavlick & Kwiatkowski (2019)** Underspecification in NLI — 与 policy ambiguity 的 multiple valid interpretations 本质相关

---

## External Review (Stanford Agentic Reviewer)

**状态：pending**。外部审稿请求已于 2026-05-20T20:39 发送，8 小时后自动提醒。截至报告投递时未返回。

---

## Visual Layout Check（非评分项）

**状态：done**（3 warnings, 7 info）

关键发现：
- **[warning] Page 7-8**: 连续 2 页纯文本（Error Analysis + Discussion），无 figure/table 穿插。Error Analysis 的 failure mode 分析适合用汇总表或分类图打破文字墙。
- **[warning] Page 8-9**: Conclusion (§8) 起始于 Page 8 右栏约 3/4 处，正文延伸到 Page 9。与 R2-N3 (N4 in report) 一致——超过 8 页限制。
- **[warning] Page 6**: Figure 3 热力图单元格数字字号偏小（~6pt），打印版可能难辨。建议考虑 sequential 色板（如 viridis）。
- **[info]**: Figure 1 全宽流程图清晰；Table 1/2 booktabs 风格规范；Figure 2 标签偏小；References 无未解析引用。

---

## Overall Assessment

**Overall: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | **3.5** |
| Excitement | 3.5 | 2.5 | **3.0** |
| Reproducibility | 3.0 | 4.0 | **3.5** |
| Overall | 3.5 | 3.0 | **3.0** |

**Confidence: 4/5** — 两位 Reviewer 均表示 4/5 confidence。

**综合判断理由**：

C1（binary ambiguity effect, +34.0pp）是坚实的实证贡献，实验方法论在 agent safety 领域属上乘。然而：

1. **C2（type hierarchy）受三重威胁**：TOST margin 无依据（N2）+ incompleteness confound（N3）+ 去除 incompleteness 后层级是否成立未验证。C2 是论文最具差异化的 finding，其稳健性直接决定 "Differential Nocuity" 框架的经验基础。
2. **C3（layer effect）实质上 inconclusive**：within-judge subgroup 均不显著（p=0.059, p=0.157），pooled 显著性可能是 judge variance artifact。
3. **C4（model×type interaction）部分可靠**：within-judge comparisons（Claude vs Qwen3 vs DeepSeek）可靠，但涉及 GPT-5.4 的跨 judge 比较不可靠——而 GPT-5.4 恰恰是 interaction 最极端的模型。
4. **N2-N3 需要新实验或新分析**：incompleteness confound 是设计层面问题，information-addition control 需要新数据。TOST sensitivity analysis 可用现有数据完成但尚未报告。
5. **正文超页**（N4）是 desk reject 风险，虽可修复但当前版本违规。
6. **新颖性**：R2 的 "measurement contribution" 定位与 R1 的 "specific patterns have empirical value" 形成分歧。综合来看，C1 的方向性结果（ambiguous > unambiguous）从定义层面 expected，真正的价值在于 magnitude 量化和 type-specific patterns——但后者（C2/C4）的稳健性正是受到方法学问题制约的部分。

**Findings track 定位**：论文的实验设计严谨性和 failure mode taxonomy 的实用价值足以支撑 Findings 接收。达到主会议水平需要：(1) 解决 N2/N3 对 C2 的威胁，(2) 加深 mechanistic explanation，(3) 修复格式问题。如果作者能在 rebuttal 中提供 TOST sensitivity analysis 和去除 incompleteness 后的分析，且结果支持多层结构的稳健性，评分可上调至 3.5。

---

## Detailed Comments

### Abstract
- 准确反映论文内容。"Perturbation control confirming ambiguity-specific causation" 中的 "confirming" 存在分歧（R1 认为过强，R2 认为 defensible）。建议改为 "supporting"。

### §1 Introduction
- Opening example 生动有效。Contribution 2 "significant three-tier type hierarchy" 应区分统计显著与实质显著。

### §2 Related Work
- 覆盖面合理，Table 1 定位有效。但缺少 7 篇重要文献（见 Missing References）。特别是 Liu et al. (2023) 和 Koenig et al. (2024) 与 Ambiguity Blindness 直接相关。

### §3 Taxonomy
- 二层框架有理论基础。但 taxonomy 作为 contribution 的权重应弱化——是 principled curation 而非 creation。Linguistic vs specification 的边界在 conditional precedence (36.8%) vs scopal (39.4%) 处模糊。

### §4 Method
- Matched-pair 设计是核心优势。Cross-judge 设计（§4.4）是最大弱点。TOST margin（§4.6）需要论证。Clause pair 构造（§4.2）的 IAA 缺失。

### §5 Results
- C1 坚实（OR=15.1, 所有模型/类型均显著）。C2 受 TOST margin 和 incompleteness confound 制约。C3 应降级为 inconclusive。C4 的 within-judge 部分有价值，between-judge 部分需弱化。

### §6 Error Analysis
- Failure mode taxonomy（§6.1-6.2）是亮点。Ambiguity Blindness（§6.3）需要更多方法论细节。Systematic Nocuity（§6.4）是新颖概念但需要更多阐释。ICR 指标选择（AC1 vs κ）需要论证。

### §7 Discussion
- "Governing principle" 措辞过强，建议改为 "empirical regularity"。Disambiguation channel framework 较 speculative，论文也承认了。Canary type 概念有趣但仅基于 5 个模型且 GPT-5.4 数据受 judge confound 影响。部分内容可移入 Appendix 以解决页数问题。

### §8 Conclusion
- 忠实于结果。但物理位置超出 page 8，必须压缩。

### Limitations
- 覆盖全面、坦诚。建议增加 TOST margin 选择和多重比较校正范围的讨论。