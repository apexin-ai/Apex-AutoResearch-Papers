---
round: 8
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T01:44:51.221790+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 8 (Fresh Review)

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 Long Paper (ARR)
**Reviewers**: R1（方法严谨性）, R2（新颖性/完整性）
**审稿模式**: Fresh（无前轮记忆）

---

## Summary

本文系统刻画了 K≥3 多分类标注误差在七种典型因果 DAG 拓扑下的传播机制。在线性 SEM 下推导了各拓扑的偏差表达式，证明了 confounding 和 collider 的 sign preservation（Proposition 1），引入 Annotation Sensitivity Values（ASV）框架并证明了 K=2 下的 envelope monotonicity（Theorem 1），报告了 FWL 不变性这一负面结果（matrix-based correction 对四种拓扑完全无效）。论文诚实地建立了 Proved/Verified/Conjectured 三级认识论层次。所有声称 proved 的结果经 R1 逐步验证均正确。

---

## Strengths

**S1. 系统性跨拓扑分析——填补真实空白。** [R1-S1, R2-S1, 共识] 此前工作限于 binary treatment（Brenner 1993; Teblunthuis 2024）或单一拓扑（Lee & Wood-Doughty 2024 仅 confounding）。本文首次在统一框架下比较 7 种 DAG 拓扑 × K≥3 类别的 bias 行为，揭示同一 confusion matrix 在不同因果结构中产生定性不同偏差。经两位 Reviewer 独立核查相关文献，"首次跨拓扑系统比较"的声称基本成立。

**S2. K=2→K≥3 的 structural transition 是真正的理论贡献。** [R1-S1, R2-S2, 共识] Binary case 的 "toward-null" 保证在 K≥3 下结构性失效（exposure 83.4% sign reversal, IV 52.6%）。Binarization collapse 发现（跨拓扑 bias 差异达 154×）对 NLP 实践有直接指导意义。

**S3. 三级认识论层次在 ML/NLP 论文中罕见且值得推广。** [R1-S2, R2 cross-share 特别赞同] 明确区分 Proved（Proposition 1, Theorem 1）、Verified（Observation 1, numerical checks）、Conjectured（Conjecture 1），这种诚实和精确是优秀的学术实践。

**S4. FWL 不变性是优雅且实用的负面结果。** [R1-S3, R2-S4, 共识] 对于 A 作为协变量的四种拓扑，任何线性变换（包括 C⁻¹ 校正）无法改变 treatment coefficient。贡献在于：(1) 识别所有主流 correction 方法均落入此类；(2) 转化为实用路由规则（Algorithm 1 Step 3）。

**S5. 实验验证广度令人印象深刻。** [R1-S4, R2-S3, 共识] 7 topologies × 23 LLM configs × cross-K(3,5,7) × logistic DGP robustness × 100,000 Dirichlet matrices。理论-实验双重验证（MAPE 1.6% across 161 scenarios）增强可信度。所有 proved 证明经 R1 逐步验证均正确。

**S6. 相关工作覆盖优秀，实用产出有价值。** [R2-S5, R2-S6] 跨流行病学、NLP、因果推断三个子领域的引用覆盖充分。Algorithm 1 提供可操作的 topology→correction 映射流程。

---

## Weaknesses

### Critical

**C1. Theorem 1 scope (K=2 + proportional effects) 与论文 K≥3 定位的核心张力。** [R1-N1 + R2-W4, 共识 CRITICAL]
- Theorem 1（envelope monotonicity）仅对 K=2 + proportional effects (f=λg) + (C₀)ⱼⱼ ≥ 1/2 成立。论文核心创新是 K≥3 场景，但 K≥3 依赖 Observation 1（worst-case deviation < 0.005）和 Conjecture 1（ε < 0.06），无形式化保证。
- ASV 框架的 well-definedness 隐含依赖 monotonicity——若局部违反，min{δ: |bias|>threshold} 可能不唯一，δ* 定义有歧义。当 δ* 较小时（如 IV topology δ*≈0.05），ε=0.06 的 monotonicity 偏差可完全淹没 ASV 信号。
- 建议：(1) Section 3.3 显式讨论 K≥3 下 ASV 的理论地位；(2) 定量分析 ε-approximate monotonicity 对 δ* precision 的影响；(3) 明确 ASV 对 IV 拓扑本质不可靠。

**C2. Proportional effects (f=λg) 在 NLP 场景中几乎不可验证，general case 有 15-17% sign preservation 失败率。** [R1-N2, R2 cross-share AGREE, 共识 CRITICAL]
- f=λg 要求 A 的各类别对 Y 和 T 的效应完全共线——在 NLP 因果推断中几乎不成立。例如 sentiment analysis 中 "neutral" 类别可能对 treatment 影响弱但对 outcome 有独立 baseline 效应。
- General case 下 Proposition 4 显示 λ(C) 有 15-17% 概率超出 [0,1]，sign preservation 可失败，但正文未报告此统计。
- 建议：(1) 正文报告 general case 失败率；(2) 给出 NLP 中 f=λg 成立/不成立的具体例子；(3) 考虑弱化条件或讨论 robustness。

### Major

**M1. Non-differential misclassification 假设在 LLM 场景中的合理性——主文讨论严重不足。** [R1-W2 + R2-W2, 强共识]
- LLM pretraining data 包含 A-Y 统计关联，即使无显式 Y access 也可产生 differential misclassification（如政治立场分类中，强情感文本与 outcome 相关，LLM 对其误分类率更低）。
- Appendix B.5 stress test（Table 7）显示 ε≥0.10 时 sign-flip rate 显著上升，但主文仅在 Limitations 一句话带过，未讨论 realistic ε 范围，也未提供估计 ε 的方法。
- 建议：Section 3.1 增加段落讨论何时非差异性合理、违反时 bias 如何定性改变、引导 Appendix B.5。

**M2. "Primary coefficient never reverses" 认识论定位模糊。** [R1-W1, R2 cross-share AGREE]
- 纯经验观察（23 LLM configs + 100K matrices）被 Abstract 赋予过高 prominence。论文自身在 Section 3.2 承认 "empirical regularity...rather than an algebraic guarantee"，但 Abstract 措辞未充分反映此限定。
- 对 K≥4，精心构造的 C 可能打破此规律。
- 建议：降低 Abstract 表述强度，讨论反例可能性或 magnitude dominance 的形式化条件。

**M3. ASV 框架与 E-values/partial R² 的方法论差异界定不足。** [R2-W1, R1 AGREE with nuance]
- ASV 三个子指标在结构上与 E-values 高度同构，差异主要在参数化对象而非方法论。K²→1D 降维需要 Theorem 1（非平凡步骤），但此证明仅 K=2 完成。
- 共识定位：应为 "systematic application with non-trivial reduction theorem" 而非 "novel framework"。
- 建议：明确列出 ASV 相对于 E-value/partial R² 的结构性差异，或调整 novelty 声称力度。

**M4. δ* uncertainty bound 过宽（IV/exposure 拓扑）。** [R1-W3, R2 PARTIALLY AGREE]
- δ* uncertainty < 0.6 在 δ* ∈ [0.1, 0.5] 时 relative uncertainty > 100%。IV topology bootstrap 95% CI [0.44, 1.29] 跨越 δ=1。
- R2 补充：uncertainty 问题主要集中在 IV/exposure（δ* 较小），confounding/M-bias 上可控。
- 共识：分 topology 讨论 δ* precision，推荐 Bootstrap CI，避免跨 topology 统一 bound。

### Minor

**m1. Table 1 Collider "Amplification" 数据可能存在排版错误。** [R1-W4, R2 REBUT 认为正文推导支持 Collider attenuation]
- Section 3.2 和 4.2 明确将 Collider 标记为 "protective"（attenuation），但 R1 报告 Table 1 Amplification=100%。如确为排版错误，需修正。

**m2. Conjecture 1 "approximately monotonic" 表述模糊。** [R1-W5, R2 AGREE]
- 建议用精确表述替代（如 "monotonic up to ε=0.06 deviations across all tested configurations"）。

**m3. Figure 2 色盲可及性。** [R2-W7]
- Sign reversal 仅用红色标记，未考虑色觉障碍读者。

---

## Reviewer Consensus

两位 Reviewer 在以下问题上达成完全共识（均 [AGREE]）：

1. **Non-differential misclassification 假设讨论不足** — 核心框架假设的 LLM 场景适用性需在主文正面讨论（非仅 Limitations 一句话）
2. **K≥3 理论保证不足** — Theorem 1 仅 K=2，ASV 在 K≥3 理论基础为 conjectural，需显式承认并讨论影响
3. **Proportional effects 假设过强** — 正文需报告 general case 失败率，给出 NLP 场景例子
4. **Primary coefficient claim 定位过高** — Abstract 应降低表述强度
5. **所有 proved claims 正确** — R1 逐步验证 Proposition 1(a)(b)(c)、Theorem 1 全 6 步、Lemma 1 均正确
6. **三级认识论层次是优秀实践** — 在 ML/NLP 论文中罕见
7. **FWL 不变性有实用价值** — 对 NLP 校正实践有直接指导意义

---

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | 权衡 |
|------|---------|---------|------|
| 实证验证范围 | REBUT：161 scenarios + real LLM matrices 已充分 | MAJOR：仅 3 NLP tasks 偏窄，Dirichlet 先验与真实 error structure 有差异 | R1 的 REBUT 有力——论文确实有 cross-K、logistic DGP、real matrices 验证。但 R2 关于 structured confusion matrix 的建议有价值。降为 MINOR 建议。 |
| Abstract 数字密度 | REBUT：分析性论文需要精确数字 | MINOR：>20 个数字过多 | 风格偏好分歧，不影响实质质量。 |
| FWL novelty | REBUT：novelty 在识别和应用，非证明技巧 | MINOR：对熟悉 FWL 读者是直接推论 | R1 的分析更有说服力——贡献在于将代数事实转化为 correction method routing。 |

---

## Questions（需要作者澄清）

1. Theorem 1 推广到 K=3 的具体数学障碍是什么？K=2 的代数结构在哪一步不可推广？
2. Primary coefficient preservation 能否形式化为 magnitude dominance 条件（如 Gershgorin-type bound）？
3. ASV 能否提供 E-values 无法给出的可操作指导？请给出具体决策示例。
4. C₀ 的选择如何影响跨 topology 的 δ* 可比性？
5. FWL invariance 在更强非线性模型（如高维交互项）下 breakdown 幅度是否随 N 或 K scaling？
6. 真实 LLM 的 differential misclassification departure ε 通常是多大？能否引用现有文献估计？

---

## Missing References

- **Ding & VanderWeele (2016)** "Sensitivity analysis without assumptions on unmeasured confounding" — E-value 的前驱理论工作，与 ASV 方法论对比直接相关。[R2 提出, R1 AGREE]
- **Rosenbaum (2002)** "Observational Studies" — sensitivity analysis 领域经典奠基。[R2 提出, R1 认为合理但非必需]

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目配置未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态：错误。** 视觉审查 Agent 因 API 限额耗尽退出（"You've hit your limit · resets 4pm (UTC)"）。用户可在限额重置后重新触发。

---

## Overall Assessment

**Overall Score: 3.5 / 5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 4/5 | 4/5 | **4/5** |
| Excitement | 3.5/5 | 3/5 | **3/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |
| Confidence | 4/5 | 4/5 | **4/5** |

**一句话总结**：理论框架严谨（所有 proved claims 正确）、系统性好（7 topologies × K≥3 是真正的空白填补）、认识论诚实（三级层次罕见），但存在两个结构性问题——(1) Theorem 1 的 K=2 scope 与论文 K≥3 定位之间的落差使 ASV 在最关键的 regime 缺乏理论保证，(2) proportional effects 和 non-differential misclassification 两个核心假设在 NLP 场景中的合理性讨论严重不足。ASV 的方法论增量有限（sensitivity analysis 标准模板的新参数化），实质创新集中在 bias taxonomy 和 FWL 不变性。

**Findings 推荐**：论文填补了多类标注误差 × 因果推断交叉领域的系统性空白，bias taxonomy 和 FWL 不变性对 NLP 实践者有切实价值。如果作者能在 camera-ready 中充分讨论两个核心假设的适用性（non-differential + proportional effects），并在 ASV 的 K≥3 理论地位上做出诚实标注，本文具备 Findings 接收的水平。Main conference 需要更强的方法论创新或更充分的 K≥3 形式化保证。

---

## Detailed Comments

### Abstract
- "the primary coefficient does not reverse...an empirical regularity consistent with magnitude dominance rather than an algebraic guarantee" — 措辞已部分改善，但 Abstract 仍将此作为核心卖点之一。建议进一步降低 prominence 或添加 "in all tested configurations" 限定。
- 数字密度高（>15 个具体数字），两位 Reviewer 意见分歧。建议保留最关键的 5-7 个。

### Section 3.1 (Setup)
- Definition 1（非差异性误分类）定义清晰。但需在此处或 Method 结尾增加讨论：何时假设在 LLM 场景中合理、违反时 bias 如何定性改变。当前仅 Limitations 一句话，不足以应对审稿人质疑。

### Section 3.2 (Bias Expressions)
- Proposition 1 的三部分条件和证明均正确（R1 逐步验证）。
- Numerical Verification 2（primary coefficient preservation）定位需改善——当前 "Numerical Verification" 标签合适，但 Abstract 引用时应保持同等谨慎。
- Collider/M-bias/front-door 小节过于简略。建议添加一句指向 Appendix 完整推导的声明。

### Section 3.3 (ASV)
- Theorem 1 证明完整正确（K=2 confounding + proportional effects，R1 验证全 6 步）。
- K≥3 的 ASV 理论基础为 conjectural——需显式标注此限制及对 δ* precision 的影响。
- ASV 与 E-value 的差异化论述需加强：(1) K²→1D 降维非平凡性；(2) topology-dependent threshold behavior；(3) 三类指标的分层语义。或者降低 "framework" 声称的力度。
- Conjecture 1 措辞建议改为 "monotonic up to ε=0.06 deviations" 替代模糊的 "approximately monotonic"。

### Section 4 (Experiments)
- Theory-MC agreement (MAPE 1.6%) 令人信服。
- Table 1：确认 Collider 行的 Amplification 数值是否正确（正文推导支持 attenuation，但 R1 报告 Table 显示 100%）。Caption 需明确 "Violation" 和 "Amplification" 的精确定义。
- Section 4.3 ASV validation：分 topology 讨论 δ* precision，IV/exposure 上 uncertainty 过大需显式承认。
- Section 4.4 FWL：建议增加一句说明此结果在 measurement error 文献中的 novelty 状态。

### Conclusion & Limitations
- Limitations 覆盖面合理但需深化 non-differential 假设讨论。
- 代码公开承诺合理。

### Appendix
- 证明完整、可独立验证（R1 确认）。
- B.5 Non-Differential Stress Test 是关键补充，应在主文增加引导。
- Algorithm 1 有实用价值。

---

## Issue Tracker 同步

已更新 `review_issues.yaml`。本轮新增/升级 issues：
- R8-C1 [CRITICAL]: Theorem 1 scope vs K≥3 定位（升级自 R6-W4）
- R8-C2 [CRITICAL]: Proportional effects 假设过强（升级自 R6-M3）
- R8-W1 [MAJOR]: ASV vs E-value novelty 差异不足（升级自 R4-W6/R6-W2）
- R8-W2 [MAJOR]: Non-differential 假设讨论不足（复发自 NEW-1）
- R8-W3 [MAJOR]: δ* uncertainty 过宽（升级自 R7-SF5）
- R8-MR1 [MINOR]: 缺失 Ding & VanderWeele (2016)
