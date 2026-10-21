---
round: 3
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-21T11:37:46.656358+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: "The Likert Blindspot: Detecting Hidden Style Bias in LLM Judges via Controlled Style Decomposition"
**Venue**: EMNLP 2026 Main Conference (via ARR)
**审稿编排**: 2 Reviewers — R1 方法严谨性, R2 新颖性/完整性
**交叉回应**: 完成（1 轮收敛）

---

## Summary

论文提出 Controlled Style Decomposition (CSD)，一个检测 LLM judge per-axis style bias 的 black-box 框架。核心发现 "Likert Blindspot"：标准 Likert 打分在七种统计方法下均无法检测到 pairwise comparison 清楚揭示的 style bias（3 judges × 3 benchmarks × 3 axes）。方法包括 NLI-gated style rewriting、position-controlled pairwise comparison、GEE conditional decomposition 分离 style vs originality effects。n=355 scaled replication 显示 Likert d→0 而 BT 稳定在 67.5%，作者将此定义为 measurement attenuation 而非单纯的 power gap。

---

## Strengths

1. **实验设计严谨**: position control (双向 swap)、NLI gate (0.90 threshold + sensitivity analysis across 0.70-0.95)、cross-judge replication (GPT-4o, Qwen3-32B, Claude Sonnet 4 as negative control)、cross-benchmark validation (LLMBar, AlpacaEval, MT-Bench)。在 NLP 实证研究中属较高水平。

2. **七种统计方法的 sensitivity hierarchy (Table 2)** 有说服力——四种 Likert-based 方法全失败 vs 两种 pairwise 方法全成功，排除了特定统计测试的 artifact 解释。Binarized Likert sign test (同样是 forced choice, 仍然 non-significant) 特别有价值。

3. **统计素养突出**: Holm-Bonferroni with explicit 6-test family definition、primary/exploratory/confirmatory trichotomy (§4.1)、Bradley-Terry with pair-level bootstrap CI、GEE with correlation structure robustness check (Appendix C)。

4. **GEE confound decomposition 发现有价值**: verbosity 的 confound-free 纯 style bias (Style OR=13.10/11.34, Orig OR n.s.) vs formality/register 的混合效应，对后续研究有指导意义。两个 judge 之间 verbosity OR 高度一致 (13.10 vs 11.34) 增强可信度。

5. **Negative control 设计加强可信度**: Claude Sonnet 4 在两个 axis 上均未检测到显著 style 偏差 (BT 56.2%/54.1%)，证明 CSD 有 discriminative validity。

6. **Rewriter independence test (Appendix D)** 直接回应最可能的方法论质疑：GPT-4o 作为独立 rewriter，verbosity Style OR 仅下降 22% (13.10→10.17)，formality BT 64.4% vs 66.5% (Δ=−2.1pp)，Blindspot 在独立 rewriter 下持续存在。

7. **Limitations section 充分诚实**: 7 段覆盖 quality-style confounding、evaluator-producer bias、benchmark coverage、human evaluation 缺失、scale granularity、NLI validation methodology 等。

---

## Weaknesses

### Must-Fix（3 个，两位 Reviewer 强共识）

**W-MF1 [critical] NLI Gate 验证存在 evaluator-producer 循环偏差**

NLI gate 本身使用 DeBERTa-v3-large（架构独立），但 gate *验证*（§5.1）使用 Qwen3-32B 作为 annotator——同时也是 rewriter 和 judge 之一。False negative rate 8.4% 可能被低估，因 Qwen3-32B 自然更倾向认为自己的改写保留了语义。GPT-4o spot-check (n=50, 94% 一致率) 部分缓解，但 50 对样本的 Wilson CI 约 [83%, 99%]，置信区间过宽。论文在 Limitations 承认 "human evaluation would provide stronger validation"，但将此放在 Limitations 而非 Discussion 中处理，显得对问题严重性评估不足。

**两位 Reviewer 强共识** (R1 识别, R2 独立确认)。

建议：≥200 对人工标注，或两个架构独立的模型分别验证。

**W-MF2 [critical] Bradley-Terry IIA 假设未检验**

BT 模型假设 Independence of Irrelevant Alternatives (IIA)，即 formal text 相对 casual text 的偏好概率不随 item 基线质量变化。但 GEE decomposition (Table 3) 恰好揭示了 originality (基线质量代理) 对偏好有显著影响 (GPT-4o formality Orig OR=2.32, p=0.006)，直接暗示 style preference 可能随 item 质量变化——violating IIA。如果高质量 item 上 style bias 更弱（或更强），BT 的 pooled 估计可能产生 Simpson's paradox 式的误导。

论文未报告任何 IIA 诊断检验。Appendix C 的 GEE style×originality 交互项检验 (p=0.53/0.32) 不等价于 BT 层面的 IIA 检验，且 n=88 检测交互效应功效极低。

**两位 Reviewer 强共识** (R1 识别, R2 完全同意)。

建议：报告 Hausman-McFadden test 或拟合 Thurstone-Mosteller 模型做稳健性检查。

**W-MF3 [critical] Originality confound 显著，削弱识别策略**

多配置下 Originality OR 显著且与 Style OR 量级相当甚至更大：
- GPT-4o formality: Style OR=2.58 vs Orig OR=2.32
- Qwen3-32B register: Style OR=1.91 vs Orig OR=5.72
- Qwen3-32B formality (n=88): Style OR=4.20 vs Orig OR=4.70

CSD 宣称的 "per-axis style bias isolation" 在 formality 和 register 上只实现了部分分离。Direction asymmetry (78.8% vs 54.5%) 进一步支持 originality confound 的存在。GEE additive specification 的交互项检验 (p=0.53/0.32) 在 n=88 下功效不足以可靠排除交互效应。

重要例外：**verbosity 确实展现了 confound-free 的 clean identification** (Style OR=13.10/11.34, Orig OR n.s.)，是论文最强的实证结果。

**两位 Reviewer 强共识** (R1 识别为 critical, R2 独立确认并指出与 "four gaps" framing 的逻辑矛盾)。

建议：重新界定 claim 为 "style-correlated preference shift" 而非 "style bias isolation"；在 originality 差异最小的子集上重复分析。

### Should-Fix（8 个）

**W-SF1 [warning] "Blindspot" 命名准确性争议**

R2 认为 critical：Table 1 中 3/9 bias-positive cells Likert 也检测到了，这不是 blindspot 而是 efficiency gap。R1 反驳：论文的 severity spectrum framing（moderate bias 区间完全失灵、强效应区部分恢复）合理，3/9 cells 逃逸恰好支持 spectrum 叙事。

**Director 判定**: Should-Fix。Spectrum framing 有一定说服力，但 "Blindspot" 一词暗示结构性不可能检测。更关键的是，n=355 时 Likert d=−0.025 也可解读为 Likert 和 pairwise 测量不同构念（absolute quality difference vs ordinal preference）——论文 §5.2 隐约承认但未整合进 framing。建议在 Discussion 正式讨论构念差异替代假设。

**W-SF2 [warning] Related Work 引用覆盖面不足**

R2 认为 critical (36 篇 vs 40-60 标准，缺 NLG evaluation surveys、counterfactual generation、scale design 等方向)。R1 认为数量非质量标准。

**Director 判定**: Should-Fix。引用数量不是硬标准，但以下特定缺失影响论文定位可信度：GEE 原始论文 (Liang & Zeger 1986)、scale design 文献 (Krosnick 1999, Preston & Colman 2000)、equivalence testing (Lakens 2017)、IIA 检验 (Hausman & McFadden 1984)。

**W-SF3 [warning] "Four critical gaps" 有 cherry-picking 嫌疑**

§1 四个 gap 的合取条件使得只有 CSD 满足所有条件。CASSE/FairJudge 已做 multi-dimensional decomposition（被归入 "correlational" 排除），RATE/Counterfactual Rhetorical 已做 interventional analysis（被归入 "Likert-based"/"persona-level" 排除）。R1 和 R2 均指出此问题。

建议：更诚实地承认各 gap 已有部分解决方案，定位为 integrative framework 而非唯一解。

**W-SF4 [warning] Claude negative control 需等效性检验**

BT 56.2% 的 95% CI [.489, .636] 包含 50% 也包含 ~63%（GPT-4o 效应量），non-significance ≠ evidence of equivalence。Claude 的极端 originality sensitivity (Orig OR=6.66, p<0.0001) 进一步削弱 negative control 解读——Claude 可能有不同类型的偏差（originality-dependent 而非 style-dependent）。Abstract "confirms discriminative validity" 过于肯定。

建议：使用 TOST equivalence testing (Lakens 2017)。

**W-SF5 [warning] Conclusion 仅一句话，严重不足**

8 页长文的结论仅 "CSD reveals the Likert Blindspot...style bias audits should adopt pairwise comparison" 一句。应包括：主要发现总结、方法论贡献的意义、对社区实践的具体影响、未来研究方向。两位 Reviewer 共识。

建议：扩展至 10-15 行。

**W-SF6 [warning] Evaluator-producer bias 处理不够彻底**

Qwen3-32B 同时担任 rewriter + judge 是设计缺陷。Style OR 在独立 rewriter test 中下降 22% (13.10→10.17)，非可忽略。Originality OR 系统性约 2× GPT-4o (formality: 4.99 vs 2.32; register: 5.72 vs 2.21)。Register axis 未做 rewriter independence test——恰好是 evaluator-producer bias 风险最高的配置。两位 Reviewer 共识。

**W-SF7 [warning] 主实验以 LLMBar (n=100) 为中心**

AlpacaEval 和 MT-Bench 仅作 partial replication (Table 1 仅 5 个额外 rows)。核心 Blindspot 论证完全基于 LLMBar 的 n=88 NLI-gated pairs。Scaled replication (n=355) 仅限 Qwen3 formality 一个 cell。LLMBar 是为 instruction-following 设计的 benchmark，其 100 条样本对更广泛 LLM evaluation 场景的代表性值得商榷。两位 Reviewer 共识。

**W-SF8 [warning] Novelty 定位需更诚实**

Likert vs pairwise 灵敏度差异是测量学经典结论 (Thurstone 1927, Kiritchenko 2017, Novikova 2018) 的 LLM 评估领域应用。R2 认为增量 novelty (LLM judge 场景 + 定量 attenuation 测量 + 7 方法比较) 有价值但不应包装为发现级突破。R1 反驳认为 application context + sensitivity hierarchy 构成充分贡献。

**Director 判定**: Should-Fix。应在 Abstract/Introduction 明确标注为 "known measurement theory principle 在 LLM judge evaluation 的首次系统定量验证"。

### Minor（5 个）

- **W-M1**: Table 1 Likert d 负值含义未解释（两位共识）
- **W-M2**: §3.5 "Interventional Design" 标题与 evidence 强度不匹配，建议改为 "Design Rationale" 或 "Quasi-Interventional Design"（两位共识）
- **W-M3**: GEE conditional decomposition 列为独立 contribution 有膨胀之嫌（R2 提出, R1 反驳——Director 判定 minor framing 调整）
- **W-M4**: wu2023style bib 年份不一致 (2023 vs 2025)
- **W-M5**: Figure 4 power curve 使用 observed effect sizes 参数化，功能上接近 post-hoc power analysis（论文有 disclaimer 但不改变实质）

---

## Reviewer Consensus

| # | Issue | R1 | R2 | Status |
|---|-------|----|----|--------|
| 1 | NLI gate 验证循环偏差 | N1 critical | AGREE | **共识 Must-Fix** |
| 2 | BT IIA 未检验 | N2 critical | AGREE | **共识 Must-Fix** |
| 3 | Originality confound | N3 critical | AGREE | **共识 Must-Fix** |
| 4 | Claude negative control 等效性 | W4 warning | AGREE | **共识 Should-Fix** |
| 5 | Conclusion 过短 | AGREE | W2 warning | **共识 Should-Fix** |
| 6 | Rewriter independence 覆盖不全 | W6 warning | AGREE | **共识 Should-Fix** |
| 7 | LLMBar generalizability | AGREE | W5 warning | **共识 Should-Fix** |
| 8 | Evaluator-producer bias | AGREE | W6 warning | **共识 Should-Fix** |

## Reviewer Divergence

| # | Issue | R1 | R2 | Director 判定 |
|---|-------|----|----|---------------|
| 1 | "Blindspot" 命名 | REBUT (spectrum 合理) | N1 critical | **Should-Fix** |
| 2 | 引用数量 | REBUT (数量≠质量) | N2 critical | **Should-Fix** |
| 3 | NLI 阈值 sensitivity | W1 warning | REBUT (§5.1 已有) | **Dropped** |
| 4 | 多重比较框架 | W3 warning | REBUT (§4.1 合理) | **Dropped** |
| 5 | RATE 批评公平性 | REBUT | W4 warning | **Minor** |
| 6 | GEE contribution 定位 | REBUT (应用新颖) | W3 warning | **Minor** |
| 7 | Novelty 定位 | REBUT (应用+hierarchy够) | W1 warning | **Should-Fix** |

---

## Questions（需作者澄清）

1. 如果 Likert 和 pairwise 测量的是不同构念（absolute quality difference vs ordinal preference），那么 Table 2 的 binarized Likert sign test（同样是 forced choice, p=0.296）如何排除这一替代解释？
2. n=355 时 Likert d 从 0.102 缩小到 −0.025——BT 稳定/略升而 Likert→0 的 differential shrinkage 如何解释？是 measurement attenuation 还是 regression to the mean？
3. Direction asymmetry (78.8% vs 54.5%): GEE additive specification 是否足以分离 style 和 originality？n=88 下交互项检验功效是否足够？
4. Claude Sonnet 4 极端 originality sensitivity (Orig OR=6.66, p<0.0001) 如何解释？是否意味着 Claude 有不同类型的偏差（originality-dependent 而非 style-dependent）？
5. 各 benchmark×axis×judge 单元 NLI 过滤后的 effective sample size？

---

## Missing References

**两位 Reviewer 共同推荐**: Liang & Zeger (1986), Krosnick (1999)

**R1 推荐**: Hausman & McFadden (1984), Agresti (2010), Lakens (2017)

**R2 推荐**: van der Lee et al. (2019, 2021), Celikyilmaz et al. (2020), Ross et al. (2021, MICE), Preston & Colman (2000), Liu et al. (2023, G-Eval), Li et al. (2024, Arena-Hard), Keith et al. (2020)

---

## External Review (Stanford Agentic Reviewer)

外部审稿：用户已跳过（skipped at 2026-05-21T11:14:38）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warnings, 6 info）：

**Warnings**:
- Page 1-3: 连续 3 页纯文本无任何 display item，审稿人在 page 4 前无视觉锚点，影响第一印象
- Page 4: Figure 1 (pipeline overview) 图内文字标签字号偏小（约正文 60%），打印时可能难以辨认
- Page 13: 最后一页仅 4 条参考文献（~20% 占比），约 80% 空白

**Info**:
- Figure 2 (DAG) 红/蓝/橙配色色盲友好性一般
- Table 1 p 值格式不完全一致
- Figure 3 菱形标记密集区略有重叠
- Figure 4 曲线在 n>200 区域多条线重合
- Conclusion 排版紧凑，过渡自然
- Limitations 内容充实，篇幅适中

---

## Overall Assessment

**Overall: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 3.5/5 | 4/5 | 3.5/5 |
| Overall | 3.5 | 3.0 | **3.0** |

**评分理由**:
- **方法论** (R1: 3.5): 实验设计和统计处理在同领域工作中突出。3 个 Must-Fix 方法论问题（NLI validation 循环偏差、BT IIA 未检验、originality confound）均为可修复的技术问题，不动摇核心发现方向。
- **新颖性** (R2: 3.0): 核心发现（Likert vs pairwise sensitivity gap）是测量学经典结论（Thurstone 1927）的领域迁移。增量 novelty 在于 LLM judge 场景的首次系统定量验证、七种方法的 sensitivity hierarchy、GEE confound decomposition 的有趣发现。这是结构性限制——修改 framing 可以改善但不能根本改变贡献的新颖性水平。
- **综合判定**: 扎实的实证工作，对 LLM evaluation 社区有实用价值（"style bias audits 应使用 pairwise comparison" 是可执行的建议）。但核心贡献更接近 systematic empirical study 而非 conceptual breakthrough。方法论问题修复 + framing 诚实化后，可达 **Borderline Conference (3.5)**。当前推荐 **Findings 级别接收**。

**Confidence**: 4/5

---

## Detailed Comments（逐节）

**Abstract**: 信息密度过高（7 行含 3 judges × 3 benchmarks × 3 axes + 具体统计数字）。建议精简数字，保留核心 message。"confirms discriminative validity" 措辞过于肯定（需 equivalence testing 支持）。

**Introduction**: 四个 gap 的构造有 cherry-picking 嫌疑。对 RATE 的批评语气偏重（RATE 目标不同于 style bias detection）。Contribution 3 (GEE decomposition) 是标准方法应用，建议降级为 experimental finding。Contribution 4 限定条件 "(n<500)" 是改进，但仍需基于更广泛的 benchmark 验证。

**Related Work**: 组织清晰（三条线索），但缺 GEE 方法学来源 (Liang & Zeger 1986)、scale design 文献 (Krosnick 1999)、equivalence testing (Lakens 2017) 等直接支持论文论点的核心引用。

**Method**: 设计周全。§3.5 "Interventional Design" 标题与 disclaimer 语气不一致，建议改为 "Design Rationale"。DAG (Figure 2) caption 详细但图本身的 NLI gate 与 Rewrite 关系箭头不够直观。Direction-aware NLI 的 tradeoff 讨论充分。

**Experiments**: 统计框架严谨（§4.1 明确定义 primary/exploratory/confirmatory）。Table 1 的 Likert d 负值需解释。Table 2 sensitivity hierarchy 是论文最有价值的结果之一。GEE decomposition (Table 3) 发现有趣但 "conditional decomposition" 而非 "causal decomposition" 的定位需更明确。

**Conclusion**: 严重不足（一句话）。需扩展。

**Limitations**: 充分且诚实，7 段覆盖主要弱点。但 NLI gate 验证的 evaluator-producer 循环问题严重性评估不足——应从 Limitations 提升到 Discussion 正面讨论。