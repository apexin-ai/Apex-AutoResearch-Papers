---
round: 8
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-25T22:52:53.836067+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8

**Venue**: EMNLP 2026 (ARR)  |  **Reviewers**: R1 (方法严谨性), R2 (新颖性/完整性)  |  **轮次**: 2 轮（初审 + 交叉回应，收敛）

---

## Summary

本文研究 LLM-as-a-judge 评分面板中 panel 规模（K=3,5,7）对多种证书操纵攻击抵抗力的影响。研究在 MMLU 和 ARC-Challenge 两个多选基准上，系统评估了 12 个 LLM 在 6 种攻击下的攻击成功率（ASR），并引入 K_eff（有效独立通道数）作为多样性度量，探讨多样性与攻击抵抗力之间的关联。实验使用 5 种统计推断方法（OLS、WCB、fractional logit、Bayesian、crossed RE），发现 K_eff 与 ASR 呈正关联（多数条件下），η_max（最大评委权重）的预测力随 K 增大而减弱，但这些关联受 diversity-capability confound 显著影响（69% 条件下 K_eff 效应可被已知混杂变量完全解释）。

## Strengths

1. **实验规模和系统性**：12 模型 × 6 攻击 × 2 基准 × 3 panel 规模 = 36 conditions 的 full-factorial 设计在 LLM judge safety 文献中属大规模系统评估。

2. **多种推断方法交叉验证**：5 种统计方法（OLS、WCB、fractional logit、Bayesian、crossed RE）提供 robustness，β_std 方向在 10/12 conditions 一致（position bias 除外）。

3. **Position bias exception 的理论洞见**：2 个负方向条件与 position bias 攻击的 taxonomy 一致性提供 construct validity，是论文中最具原创性的发现之一。

4. **透明的局限性声明**：Abstract、Introduction、Limitations 反复标注 "all findings are associational"，Cinelli-Hazlett 69% 结果前置，体现实证研究的诚实态度。

5. **敏感性分析框架**：Cinelli-Hazlett sensitivity analysis、ε robustness check、多种 diversity metrics 对比展示严谨的方法论意识。

## Weaknesses

### Must-Fix

**MF1. Diversity-Capability Confound 削弱核心关联的可解释性** [R1 Must-Fix, R2 Should-Fix → Director: Must-Fix (framing)]

Cinelli-Hazlett 分析显示 69%（25/36）条件下 K_eff 的正效应可被已知 confound（diversity 与 capability 的 r=0.70-0.81 相关）完全解释。Introduction 中 "we address this gap by decomposing the roles of diversity and capability" 暗示可以干净分离两个因子，但 multicollinearity 使这种分离在统计上不可靠。

R2 反驳：10/12 方向一致性不太可能完全由 confound 解释（confound 应增加不确定性而非系统性产生一致方向），κ-diversity 12/12 confirmation 和 position bias exception 提供 construct validity。R2 建议降为 Should-Fix。

Director 判断：R2 的缓解论点有说服力，但 69% coverage 仍然是核心 contribution 的根本性限制。至少需要：(1) 删除 "decomposing" 表述，(2) Contribution 1 重述为条件性关联（"diversity and vulnerability show positive association, partially confounded by capability"），(3) 正文 Analysis 部分（非仅 Limitations）讨论 confound 的实质影响。本 issue 跨 6 轮审稿持续被标记。

**MF2. Vote-Counting (X/12) 作为主要汇总方法在统计上不当** [R1-R2 共识]

Abstract 和 Introduction 完全依赖 vote-counting 汇总（"K_eff positive in 10/12 conditions, κ-diversity 12/12"）。Hedges & Olkin (1985) 已证明 vote-counting power 可任意低。I²>87% 的高异质性下，"10/12 显著"可能反映条件间系统差异（如 attack type × benchmark 交互）而非一致效应。

论文在 Section 5.2 已有 DerSimonian-Laird pooled β̂_std（K_eff 0.286-0.353, CI excluding zero），R2 纠正了 R1 的事实错误——DL pooling 在正文 Section 5.2 而非附录。但两位 Reviewer 共识：Abstract/Introduction 应以 pooled β̂_std ± CI 为主要 framing，vote counts 降为补充描述。例如 "K_eff's pooled standardized coefficient is 0.286–0.353 (CI excludes zero)" 比 "10/12 conditions" 更 informative 且方法论更正确。

**MF3. 因果语言持续残留** [R1-R2 共识，第 6 次标记]

标题 "How Panel Size Shifts..." 中 "shifts" 是因果动词，与 "associational" 定位矛盾。Introduction "decomposing" 同样暗示因果分离。此 issue 自 Round 3 起被反复标记，至今未解决。需全文 grep 因果动词并替换为中性表述。

### Should-Fix

**SF1. K_eff "Effective Independent Channels" 名称的理论基础已被 GoF 拒绝** [R1 Must-Fix, R2 REBUT → Director: Should-Fix]

Cramér-von Mises GoF 在 97-100% conditions 下拒绝 Gaussian copula 假设。R1 认为理论解释失效（Must-Fix），R2 反驳：K_eff 在论文中作为 empirical predictor 使用，ranking robustness（Spearman ρ≈0.86-0.87）保证回归系数方向稳定性，GoF 拒绝不影响 empirical role。

Director 采纳 R2 立场：这是 terminology issue 而非 method failure。建议 (1) 改名为更中性术语（如 "pairwise-MI-based diversity index"），(2) 正文声明 K_eff 仅作 empirical predictor，(3) GoF 拒绝率从附录提升到正文。

**SF2. AWQ INT4 量化混淆** [R1-R2 共识]

6 个 local AWQ INT4 模型人为放大 diversity-capability confound。API-only pool 中 K_eff 降到 2-3/12 但 MDE>0.9，无法判断 K_eff 信号来自 genuine diversity 还是 quantization damage。应在正文 Analysis 部分更显著讨论（非仅 Limitations）。

**SF3. Proposition 1 应降级** [R1-R2 强烈共识]

Stochastic dominance 下 ASR monotonicity 近似于定义推论，证明仅 3 行，仅 58% pairs 适用。降级为 Observation 或 §3 自然推论，删除 Contribution 独立条目。此 issue 自 Round 6 起被反复标记。

**SF4. ε=10⁻⁶ 对 log-log 回归的 Sensitivity** [R1-R2 共识]

log(ASR+ε) 中 ε=10⁻⁶ 的选择未经 sensitivity analysis。R2 指出影响预期较小（ASR≈0 的条件 leverage 有限），但应在附录报告 ε=10⁻⁴, 10⁻⁸ 结果，或升级 fractional logit 为 co-primary analysis。

**SF5. 仅 Multiple-Choice 基准** [R1-R2 共识]

MMLU+ARC 的 bounded output space 可能使某些攻击效果被低估。论文标题和 claims 未过度泛化，但标题或 Abstract 应明确 "multiple-choice evaluation" scope。

**SF6. 攻击模板覆盖不足** [R1-R2 共识]

每种攻击仅 1-2 template variants。R2 补充：template 选择可能与 model family vulnerability 有系统性交互，引入 template-specific bias。§4.2 增加 caveat，future work 建议增加 template diversity。

**SF7. API 模型版本无锁定** [R1-R2 共识]

Table 2 注明 "May 2026 snapshots" 但缺具体 version/snapshot ID。Appendix 应列出 OpenRouter 返回的版本信息。

**SF8. Conclusion 过于简略** [跨 4 轮标记]

约 150 words，缺 practical implications、AI safety 连接、future directions。建议扩展至 2-3 段。

**SF9. Novelty 与经典 Ensemble Theory 区分不足** [R2 flag, R1 rebut — 分歧记录]

R2：核心发现（diversity 在低 bias 时有益）是 Brown et al. (2005) 的 LLM instantiation，novelty 有限。R1 反驳：adversarial LLM 场景有本质差异（adaptive attacks vs random faults），K_eff 正系数的反直觉方向是 genuine contribution。论文应在 §2 或 §6 明确讨论——哪些发现是已知理论的 instantiation，哪些是 genuinely novel（如 position bias exception）。

## Questions

1. 如果用 κ-diversity（12/12 正方向）替代 K_eff 作为主要 diversity metric，核心结论是否改变？三种 metric 的 K-trajectory 差异（K_eff 4→7→8, κ 8→7→6, Shannon 4→4→0）如何解读？
2. Pool A (API-only) 能否通过增加 K 取值（K=9,11）提升功效以有效 de-confound？
3. "Effective independent channels" 名称在 GoF 拒绝后是否会误导后续研究的引用和解读？

## Missing References

以下文献应在 Related Work 中实质性讨论：
- **Krogh & Vaidya (1995)** — bias-variance-covariance decomposition，论文发现可能是其 LLM instantiation
- **Brown et al. (2005)** — diversity 仅在低 bias 时有益的理论预测
- **Horváth et al. (2022)** — certified ensemble robustness
- **Lakshminarayanan et al. (2017)** — deep ensembles
- **Kuncheva (2003)** — diversity measures 不一致性（与三种 metric 不同结论吻合）
- **MacKinnon & Webb (2017)** — few-cluster bootstrap

## External Review

外部审稿：未请求。

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 3 warnings, 8 info）：
- ⚠️ **页数疑似溢出**：正文约 8.2-8.3 页，EMNLP 2026 限制 8 页正文。需压缩 Section 6 或 Section 7。
- ⚠️ **附录 Figures 19-21**（Cinelli-Hazlett 等高线图）子图标注约 5-6pt，建议增大字号或减少每页子图数。
- ⚠️ **Page 7 视觉拥挤**：Figure 5 + Table 4 + Figure 6 三个 display items 堆叠。
- ℹ️ 全文表格 booktabs 格式规范，未发现渲染错误、引用缺失或 margin 溢出。

## Overall Assessment

**3.0 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| 整体评分 | 3.0 (Findings) | 3.5 (Borderline Conference) | **3.0 (Findings)** |
| Soundness | 弱 | 中 | 中偏弱 |
| Novelty | 低 | 中偏低 | 低-中 |
| Significance | 中 | 中 | 中 |
| Clarity | 中 | 中偏高 | 中 |

**评分依据**：

论文的实验规模（36 conditions × 5 推断方法）和方法论透明度值得肯定，但两个结构性限制制约其贡献等级：

(1) **Confound 是结构性的**：69% conditions 下核心关联可被 capability confound 解释，API-only pool 功效不足无法 de-confound。这使论文核心 contribution（diversity-vulnerability association）的因果方向无法确认。

(2) **Novelty 受限**：核心发现与 Brown et al. (2005) 理论预测一致。K_eff 正系数方向虽在 adversarial 语境下有解释价值，但论文未充分论证超越经典理论的增量贡献。Position bias exception 是最具原创性的发现但未被提升为主要叙事。

(3) **持续性问题未解决**：因果语言（6 轮标记）、Proposition 1 trivial（3 轮标记）、Conclusion 过简（4 轮标记）等问题跨多轮审稿仍在，反映修订对审稿反馈的响应不充分。

**适合 Findings 理由**：实验设计系统性和统计框架多样性使论文在实证方法论层面有参考价值。Position bias exception、operationalization dependence 等发现对 LLM judge safety 社区有贡献。但 confound 的结构性限制和 novelty 不足使其难以达到主会议接收标准。

**R1-R2 分歧记录**：
- K_eff GoF (R1-N2)：R1 Must-Fix vs R2 Should-Fix → Director 采纳 R2（terminology issue）
- Novelty (R2-N3)：R2 novelty 不足 vs R1 adversarial context genuine contribution → 分歧记录，建议论文明确论证
- Confound 严重程度 (R1-N1)：R1 Must-Fix (critical) vs R2 Should-Fix (framing) → Director Must-Fix (framing 级别)
- 评分差异根源：R1 侧重方法论缺陷的 disqualifying 效应，R2 侧重 5 种推断方法交叉验证的工程质量

## Detailed Comments

### 致作者

1. **优先级最高**：将 Abstract/Introduction framing 从 vote counts (X/12) 改为 pooled β̂_std ± CI。这是最容易修复且回报最大的改动。
2. **K_eff 命名**：GoF 拒绝后 "effective independent channels" 可能误导后续研究。建议改为中性名称并在正文声明 empirical-only usage。
3. **Position bias exception 叙事价值**：2/12 负方向条件与 position bias taxonomy 的一致性是论文最具原创性的发现——考虑在 Contribution 列表中提升其地位，替代 Proposition 1。
4. **页数溢出**：正文约 8.2-8.3 页，超 EMNLP 2026 的 8 页限制。建议压缩 Section 6 Analysis。
5. **因果语言**：第 6 轮被标记。建议全文 `grep -iE "shift|decompos|determin|driv|caus"` 系统清理。