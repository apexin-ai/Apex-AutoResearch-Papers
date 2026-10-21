---
round: 1
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T03:40:20.957709+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: True
---

# Round 1 审稿报告

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿日期**: 2026-05-22
**Reviewers**: R1 (方法/理论严谨性 + 实验设计), R2 (新颖性 + 完整性 + 相关工作 + 格式合规)

---

## Summary

本文研究 LLM 标注产生的 K-class confusion matrix 结构如何与 7 种 DAG 拓扑交互，影响因果估计的偏差方向和幅度。三个贡献：(1) 7 种拓扑下的 multi-class bias taxonomy，证明 5 种拓扑维持 sign preservation 而 exposure 和 IV 可产生 sign reversal；(2) Annotation Sensitivity Values (ASVs) 框架提供三种灵敏度度量；(3) 5 种 correction 方法的 topology-aware 评估，揭示 FWL invariance 使 matrix-based 方法对 4 种拓扑无效。

---

## Strengths

1. **问题定义新颖且重要**。将多类标注误差与 DAG 拓扑的交互作为研究对象是全新角度。K=2→K>=3 揭示了结构性质变——sign-flip guarantee 的崩溃——这在 binary 框架中原理上不可能发现。[R1+R2 共识]
2. **部分拓扑证明严谨**。Confounding（Cauchy-Schwarz 界）、Collider（Berkson's bias 反向结构）、Exposure 反例构造清晰可验证。[R1]
3. **FWL invariance 负结果有实践价值**。证明 matrix-based correction 对 4/7 拓扑的 T 系数 bias reduction 恰好为 0%。[R1+R2 共识]
4. **Binarization collapse 分析**揭示 K-class→binary 的额外代价（154x 跨拓扑变化）。[R1]
5. **实证验证扎实**。3 数据集、4 LLM、98+ 场景，MAPE 2.0%。[R2]
6. **写作密度高、结构紧凑、格式完全合规**。[R2]

---

## Weaknesses

### Must-Fix（5 项，影响接收决定）

**W1. Theorem 1 (Envelope Monotonicity) 无解析证明** [R1+R2 共识]
- 仅 500 场景数值验证。ASV 有效性依赖单调性。建议：confounding case 补解析证明，其余降级为 Conjecture。

**W2. Proposition 1 中 mediation/M-bias sign preservation 缺乏 proof** [R1+R2 共识]
- Mediation 仅数值验证（论文承认 proof remains open），M-bias 仅 structural argument，front-door 继承 mediation 缺口。建议拆分 Proposition。

**W3. ASV 参数化 C(δ) 定义域错误** [R1+R2 共识]
- δ∈[0,∞) 不正确。Sign-flip ASV=6.7 可能超出有效域（δ_max≈1.67 if min diagonal≈0.4）。

**W4. 83.4% headline framing 误导** [R1+R2 共识]
- 基于 Dirichlet(1,1,1)，diagonal≥0.7 时降至 2.1%，98 实证场景 zero sign reversals。Abstract 应同时报告 realistic regime 数字。

**W5. 关键相关工作未引用** [R1+R2 共识]
- Audinet de Pieuchon et al. (EMNLP 2025), Zrnic & Candes (PNAS 2024) Cross-PPI, Gligoric et al. (NAACL 2025), Keith et al. (ACL 2020)。

### Should-Fix（6 项）

**W6.** Sign preservation 条件的循环性未在主文讨论 [R1+R2 共识]
**W7.** 线性模型假设局限未在 Limitations 提及 [R1+R2 共识]
**W8.** 实证验证模型不对称（HumAID frontier vs VAST/CC 7B）[R1, R2 部分同意]
**W9.** ASV 对 C₀ 估计不确定性的敏感性未讨论 [R1+R2 共识]
**W10.** MC MAPE 报告不充分（掩盖 per-topology 差异）[R1+R2 共识]
**W11.** "first systematic framework" 过度声明 [R2 提出, R1 部分同意建议弱化措辞]

---

## Reviewer Consensus

完全一致 [AGREE]：W1-W5（所有 must-fix）、W6-W7、W9-W10、所有 minor issues。

## Reviewer Divergence

**Novelty 评估**：R2 认为增量式扩展（Excitement 2.5/5），R1 反驳认为 K>=3 sign-flip breakdown 是结构性质变（Excitement 4.0/5）。Director 判断：R1 反驳有技术依据，但 R2 关于 ASV 和 FWL 创新有限的批评也成立。降级为 should-fix。

---

## Questions

1. Confounding case 能否对 Theorem 1 给出解析证明？
2. Sign-flip ASV 1.1-6.7 是否都在有效 δ 范围内？
3. 是否存在绕过 FWL invariance 的 correction 方法（如 EM imputation）？
4. Proposition 1 条件如何在实际中近似验证？
5. 6 种 error structures 的具体参数？
6. .bib 中有但未 \cite 的高度相关论文——原因？

---

## Missing References

1. Audinet de Pieuchon et al. (EMNLP 2025) — benchmark DSL/PPI debiasing
2. Zrnic & Candes (PNAS 2024) — Cross-PPI (gold-free)
3. Gligoric et al. (NAACL 2025) — Confidence-driven inference
4. Keith et al. (ACL 2020) — Text + causal inference survey

---

## External Review

未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

已完成（3 warnings, 7 info, 0 critical）。主要发现：
- 前 4 页纯文本无 display item，Figure 3 (DAG taxonomy, 当前 p.16) 应移至正文 Method 开头
- 正文仅 3 display items / 8 页，密度偏低
- p.17 四张 figure 挤在单页，字号 ≤6pt 低于可读性阈值

---

## Overall Assessment

**Overall Score: 3.5 / 5 (Borderline Conference)**
**Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 4.0 | 3.5 |
| Excitement | 4.0 | 2.5 | 3.0 |
| Reproducibility | 4.0 | 3.5 | 3.5 |
| Overall | 3.5 | 3.5 | **3.5** |

**修改路径（达到 4.0 Conference 的条件）**：
1. Theorem 1 confounding case 补解析证明，其余降级
2. 拆分 Proposition 1，未证明拓扑降级为 Empirical Finding
3. 修正 ASV 定义域，验证报告值有效性
4. Abstract 同时报告 realistic regime 数字
5. 补充 4 篇关键引用并讨论区别
6. Limitations 补充线性模型假设、sign preservation 条件可验证性、ASV 对 C₀ 敏感性