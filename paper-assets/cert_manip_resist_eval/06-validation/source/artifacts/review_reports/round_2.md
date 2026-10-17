---
round: 2
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T12:02:14.059533+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告：Round 3（Fresh Review）

**论文**："The Shifting Bottleneck: How Panel Size Modulates Adversarial Vulnerability in LLM Judge Panels"
**Venue**：EMNLP 2026（ARR May 2026 cycle, Long Paper）
**Reviewers**：R1（方法严谨性）+ R2（新颖性/完整性）
**审稿模式**：Fresh（重新审稿，无上轮记忆）

---

## Summary

本文研究 LLM 多模型评审 panel 在对抗攻击下的脆弱性，将 panel 级漏洞分解为个体法官弱点（η_max，最弱环节）和结构多样性（K_eff，有效独立通道数）。在 15 个模型（6 families, 3 capability tiers）、6 种攻击、2 个 MCQ 基准（MMLU, ARC）、K∈{3,5,7}（455–6,435 panels）上进行穷举实验，发现 panel-size-dependent vulnerability regime transition：K=3 时 η_max 主导（wild cluster bootstrap 5/12 显著），K≥5 时 K_eff 成为主要预测因子（7/12 显著）。聚合层面的 K_eff 正向关联掩盖了 attack-mechanism-dependent 结构（targeted attacks 6:6 split shared-bias attacks），Bayesian calibration 可反转 diversity channel。

---

## Strengths

**S1. 明确且有价值的研究问题。** 将 panel 脆弱性分解为 η_max 和 K_eff 两个维度，直接回应 Al Masoud et al. (2026) 将 diversity 和 individual robustness 混为一谈的问题。分解框架对 LLM evaluation 社区有实际指导价值。[R1+R2 共识]

**S2. 穷举式实验设计。** 15 模型 × C(15,K) 面板 × 6 攻击 × 2 基准 × 4 聚合规则，所有组合实际运行而非采样，消除面板选择偏差。实验规模远超同类工作。[R1]

**S3. 罕见的统计诚实度。** 4 种独立修正方法逐层剥离 inflated significance（OLS 8/12 → Clustered SE 0/12 → Mixed Effects 3/12 → Bootstrap 1/12, Table 3），展示 K_eff 信号坍塌过程。坦诚报告 Cinelli-Hazlett 78% 条件不 robust、API-only 不复现等不利结果。这种 transparency 在 NLP 论文中非常罕见。[R1+R2 共识]

**S4. Attack-mechanism-dependent 结构有洞见。** GAM 分析揭示的 6:6 targeted/shared-bias split（§5.4, Figure 3）在 K=5 时保持 11/12 一致性，提供了超越聚合统计的机制理解。[R1+R2 共识]

**S5. 高质量附录。** Appendix A-K（proof, robustness checks, Cinelli-Hazlett sensitivity, cross-benchmark prediction, attacked K_eff stability 等）系统覆盖潜在质疑，在同类研究中非常罕见。[R1+R2 共识]

**S6. 实用的部署建议。** K=3 筛选个体鲁棒性 + K≥5 管理相关鲁棒性 profile + Bayesian calibration 逆转 diversity channel，直接可操作。[R1+R2 共识]

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [critical, R1+R2 consensus] K_eff 独立预测能力被 Cinelli-Hazlett 实质性削弱，正文 framing 过于乐观**

Cinelli-Hazlett 分析显示 28/36（78%）条件下，已知的 η_max confound 超过 K_eff 的 RV（Table 9, Appendix I），意味着 K_eff 的表观效应可能完全由能力差异解释。即使在 K_eff"最强"的 K=7，仍有 8/12 条件不 robust。§6 报告 28/36 后立即转向"Robustness increases with K"的正面叙述，未明确陈述核心含义：**在绝大多数条件下，多样性信号无法与能力差异区分**。

Capability-matched Pool A（r=0.50, K_eff 9/12, Appendix F Table 7）是论文最有力的证据，但被埋在附录中，且未在 Pool A 上运行 Cinelli-Hazlett——如果 RV 改善，将大幅加强论证。

**行动项**：(1) §6/§7 明确 qualification；(2) Pool A 关键数字提升至正文；(3) 在 Pool A 上运行 Cinelli-Hazlett；(4) 重新 frame 为 descriptive regime transition。

**W2 [critical, R2+R1+Visual Agent consensus] 正文 Conclusion 溢出至第 9 页，格式违规**

Section 7 最后 1-2 行（"the transition threshold K*...remain open."）溢出到第 9 页顶部，在 Limitations 之前。EMNLP 2026 long paper 正文严格 8 页。视觉审查 Agent 独立确认溢出约 1.5 行。可能导致 desk rejection。

**行动项**：压缩 Analysis(§6) 或 Conclusion(§7) 文本。

**W3 [critical→warning, R2 critical, R1 partial rebut] Regime transition 新颖性争议**

R2 认为 regime transition 的定性方向可从 majority vote 机制直接推导（K=3 翻转 1 judge 即改变结果，η_max 主导是数学必然），将"discovery"包装 overstates 新颖性。R1 反驳：attack-mechanism-dependent structure（6:6 split）、Bayesian calibration reversal、定量精度均不可从 CJT 推导，构成实质贡献。

**综合判定**：降级为 warning。定性方向确实有一定可预期性，但 attack-type taxonomy、aggregation modulation 和定量刻画提供了超越 CJT 的实质贡献。"We discover"措辞应调整。

**行动项**：(1) Abstract "We discover"→"We empirically characterize and quantify"；(2) §2 CJT 段落承认定性方向可预期，突出超越 CJT 的具体贡献。

### Should-Fix（影响评分但不一票否决）

**W4 [warning, R1 critical→R2 rebut→降级] ε=10⁻⁶ 敏感性分析不充分**

log(ASR+ε) 中 ε 选择可能创造高杠杆点。R1 标为 critical，R2 反驳：§5.1 已报告 FDR stable across ε∈{10⁻³,10⁻⁶,10⁻⁹}，fractional logit 93.1% directional agreement 实质替代了 ε 敏感性。综合判定降为 warning。

**行动项**：报告零 ASR 面板占比和不同 ε 下的 coefficient estimates。

**W5 [warning, R1+R2 consensus] Clean K_eff 对 position bias 和 prompt injection 无效但纳入汇总**

Table 8 (Appendix H) 显示 position bias ARC ρ=0.08、prompt injection ρ≈0.60。"X/12 significant"汇总包含这些无效条件。

**行动项**：分开报告 K_eff-stable (ρ≥0.90) 和 K_eff-unstable 条件的显著性。

**W6 [warning, R1+R2 consensus] 13 clusters 低于 Cameron et al. (2008) 的 20-cluster 下限**

未探索 Webb 6-point weights 等 few-cluster 改进方法。缺引 MacKinnon & Webb (2018)。

**W7 [warning, R1+R2 consensus] API-only 子集不复现 regime transition**

API-only (r=0.85, VIF=4.4) K_eff 仅 3/12。替代解释（K_eff 捕获 AWQ INT4 能力方差而非多样性信号）需在 §6 明确讨论。

**W8 [warning, R1+R2 consensus] 仅 3 个离散 K 值，K=4 缺失**

K∈{3,5,7} 仅给出 K*∈(3,5)。C(15,4)=1365 计算量可控。

**W9 [warning, R2 raised, R1 agrees] K_eff 未与已有 diversity measures 对比**

引用了 Kuncheva & Whitaker (2003) 但未做实证对比（Q-statistic、disagreement measure）。

**W10 [warning, R2 raised, R1 partial agree] Attack taxonomy 中 position bias 分类有争议**

Position bias (ρ=0.08 on ARC) 的 K_eff 稳定性行为更接近 shared-bias 而非 targeted。"taxonomy"用词过强，建议改为"empirical categorization"。

**W11 [warning, R1+R2 consensus] Abstract 数字密度过高**

大量具体数字（1/12, 7/12, 6435 等）淹没核心 message。

**W12 [warning, R2 raised, R1 confirms] Shi et al. (2024) bib 条目标题错误**

shi2024judgerobust 标题与 zheng2023judging 重复，arXiv:2402.14016 的真实标题不同。

**W13 [warning, R1 raised, R2 partial rebut] 功效分析仅限 K=3**

K=5/K=7 的 MDE 未报告。R2 部分反驳（η_max 5/12→0/12 排除纯功效解释），但补充 MDE 有价值。

**W14 [warning, R1+R2 consensus] MCQ-only 局限性讨论不足**

MMLU 和 ARC 均为 MCQ，与 LLM judge 实际部署场景（open-ended evaluation）差异大。Limitations 已提及但不够突出。

### Minor（不影响接收）

**M1** [R1+R2 consensus] §6/§7 偶有不当因果语言（"reverses", "eliminating"）
**M2** [R1+R2 consensus] Theorem 1 stochastic dominance 仅覆盖 58% pairs，42% 的分布特征未讨论
**M3** [R1 raised, R2 partial agree] Fractional logit (Table 7) 是否使用 wild cluster bootstrap 未明确

---

## Reviewer Consensus

以下问题 R1+R2 完全一致 [AGREE]：
1. K_eff-η_max 共线性是论文的根本性限制，正文 framing 需更审慎
2. 页数超限需修复
3. Pool A 是论文最有力证据，应提升至正文
4. Clean K_eff 对 2/6 攻击类型无效，汇总统计应区分
5. 13 clusters 不足，需讨论改进方法
6. API-only 不复现需更充分的替代解释讨论
7. MCQ-only 局限性讨论需加强
8. Abstract 数字过载
9. Shi 2024 bib 错误
10. 因果语言需降级为 associational

## Reviewer Divergence

**分歧 1：新颖性评估**
- R2：regime transition 定性方向可从 CJT/majority vote 推导，新颖性有限（critical）
- R1：attack-mechanism-dependent structure、Bayesian reversal 不可预测，定量精度有独立价值（partial rebut）
- **综合判定**：降级为 warning。"We discover"措辞需调整，但论文超越 CJT 的贡献实质存在。

**分歧 2：ε 敏感性严重性**
- R1：critical——零 ASR 占比和系数变化未报告，可能影响核心结论
- R2：should-fix——fractional logit 交叉验证 + 3 个数量级 ε 稳定性已提供充分保障
- **综合判定**：降级为 warning。补充零 ASR 统计和 coefficient estimates 即可。

---

## Questions for Authors

1. 各条件下 ASR=0 的面板占比？[R1-Q1]
2. K_eff 的实际分布范围（均值、SD、min、max）？[R1-Q2]
3. Capability-matched Pool A 上的 Cinelli-Hazlett RV 是否优于全池？[R1-Q3, R2-Q1, 关键实验]
4. Theorem 1 不满足 stochastic dominance 的 42% pairs 是否集中在同一 capability tier？[R1-Q4]
5. Fractional logit (Table 7) 使用的推断方法？[R1-Q5]
6. Position bias 归类为 targeted attack 的先验理由？[R2-Q2]
7. K=7 时 K_eff 从 7/12 降至 5/12——是 power loss 还是 effect attenuation？[R2-Q4]

---

## Missing References

- **MacKinnon & Webb (2018)** "The wild bootstrap for few (treated) clusters" — few-cluster bootstrap [R1+R2 consensus]
- **Austen-Smith & Banks (1996)** "Information Aggregation, Rationality, and the Condorcet Jury Theorem" — CJT 战略投票扩展 [R2, R1 agree]
- **Stureborg et al. (2024)** "Large Language Models are Inconsistent and Biased Evaluators" — LLM evaluator 不一致性 [R2, R1 agree]
- **Ye et al. (2024)** "Justice or Prejudice? Quantifying Biases in LLM-as-a-Judge" — LLM judge bias 量化 [R2]
- Shi et al. (2024) bib 条目标题需核实更正 [R2, R1 confirm]

---

## External Review (Stanford Agentic Reviewer)

**状态**：pending（已发送请求，尚未返回）。外部审稿结果到达后将作为补充信息发送至 Group C。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成。**0 critical, 4 warnings, 10 info**。

关键发现：
- **[warning] Page 9**：Conclusion 溢出约 1.5 行至第 9 页（与 R2-N2 一致）
- **[warning] Page 5**：整页纯文本（§4.3–§4.6），无 display item。建议前移 Table 2/3
- **[warning] Page 8**：§6 Analysis + §7 Conclusion 全页无 display item，建议添加 summary figure
- **[warning] Page 17**：末页约 40% 空白，附录排版可压缩
- **[info]** Figure 1 位置优秀（page 2 顶部全宽）；Figure 2/3 色彩方案色盲友好；所有 Table 使用 booktabs 规范；无未解析引用或 LaTeX 错误
- **[info]** 部分 figure 标签字号偏小（Figure 1 约 60% 正文字号，Figure 3 x 轴标签、Figure 7 等高线标注）

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3.25/5 |
| Excitement | 3.5/5 | 3/5 | 3.25/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4/5 | 4/5 | 4/5 |

**一句话总结**：扎实的实证工作以罕见的统计诚实度填补了 LLM judge panel diversity vs. robustness 的研究空白，但 K_eff 的独立效应在 78% 条件下不能排除 capability confound，限制了核心 claim 的因果解释。

**推荐接收的理由**：研究问题有明确实际价值，attack-mechanism-dependent structure 有洞见，穷举实验和 9 个附录的稳健性分析在同类工作中非常罕见，部署建议可操作。

**推荐拒绝的理由**：(1) K_eff-η_max 共线性使核心 claim 因果解释不可靠；(2) 正文超 8 页格式违规；(3) regime transition 的定性方向有一定可预期性。

**升级路径**：修复格式违规（W2, W12）+ 在 Pool A 上运行 Cinelli-Hazlett 证明 K_eff 独立性（W1）+ 重新 frame 贡献（W3）→ 有望升至 **4.0 (Conference)**。

---

## Detailed Comments

### Section 1 (Introduction)
- "We discover" 措辞偏强，建议 "We empirically characterize and quantify"
- Contribution 1 需在 CJT 背景下定位——承认定性方向可预期，强调定量精度和 attack-type/aggregation 交互的贡献

### Section 2 (Related Work)
- CJT 段落应补充 Austen-Smith & Banks (1996) 和 Ladha (1992) 已引但缺少对 correlated voting 下 panel size 效应的预测
- 缺 Stureborg et al. (2024) 和 Ye et al. (2024) 关于 LLM judge bias/inconsistency 的引用

### Section 3 (Threat Model)
- Theorem 1：58% 覆盖率限制实用价值，建议讨论 42% 不满足 pairs 的分布特征（是否集中在同 tier 内）
- Definition 1 (Adaptive Adversary) 的 oracle 假设在实际场景中过强——Limitations 已提及但讨论可更深入

### Section 4 (Methodology)
- §4.5 Eq.2：报告零 ASR 面板占比，明确 ε=10⁻⁶ 的影响程度
- §4.6：讨论 Webb 6-point weights 或 subcluster bootstrap 的适用性，引用 MacKinnon & Webb (2018)
- K_eff (§4.3)：应在附录中与 Q-statistic、disagreement measure 做实证对比
- Fractional logit (§4.6 末尾引用) 需明确使用的推断方法

### Section 5 (Results)
- §5.1/§5.2："X/12 significant"汇总应区分 K_eff-stable 和 K_eff-unstable 条件
- §5.2：Pool A (r=0.50, 9/12) 关键数字应在此处呈现
- §5.2：报告 K=5/K=7 的 MDE
- §5.4：position bias 分类争议——建议单独讨论或基于 Appendix H 重新分类；"taxonomy"改为"empirical categorization"

### Section 6 (Analysis)
- "Diversity–Capability Confound"段：28/36 之后应明确陈述"K_eff 独立效应在大多数条件下不能排除 η_max confound"
- 明确讨论 K_eff 作为 capability variance proxy 的替代解释
- 因果语言检查："reverses"→"is associated with a sign change"
- 如果添加 Pool A Cinelli-Hazlett 结果，此处是最佳位置

### Section 7 (Conclusion)
- 需压缩至第 8 页内
- "eliminating panel composition's predictive power entirely"→ associational 表述
- 对 K_eff 独立性 claim 给出明确 qualification

### Limitations
- MCQ vs open-ended failure mode 差异需更突出讨论
- K=4 缺失应提及

### References
- 修正 shi2024judgerobust 标题
- 补充 MacKinnon & Webb (2018), Austen-Smith & Banks (1996), Stureborg et al. (2024), Ye et al. (2024)