---
round: 11
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T04:12:41.384106+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# Round 11 Consolidated Review Report (修正版)

> **修正说明**：本版修正了先前提交中 Reviewer 1 评分的错误（3.5→4.0），并补充了 R1 完整审稿中新发现的 weaknesses（K 值敏感性、IV 实践指导、结构化违反测试）和 minor issues。

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**投稿类别**: Long Paper (8 页正文限制)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）
**格式合规**: ✓ 正文 ≤ 8 页, ✓ Double-blind, ✓ ACL 引用格式, ✓ Limitations 节

---

## Reviewer 评分总览

| 维度 | Reviewer 1 | Reviewer 2 |
|------|-----------|-----------|
| **Overall** | **4.0 (Conference)** | **3.5 (Borderline Conference)** |
| Soundness | 4/5 | 4/5 |
| Excitement | 3.5/5 | 3/5 |
| Reproducibility | 4/5 | — |
| Confidence | 4/5 | — |

---

## Summary

本文分析 K≥3 多类别标注误差在七种典型 DAG 拓扑下如何传播到因果估计中。核心贡献：(1) 七种拓扑的 bias 闭式表达，证明/验证五种拓扑保持符号方向而 exposure 和 IV 可产生符号反转；(2) ASV 诊断工具揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱；(3) FWL 不变性负面结果证明基于矩阵的校正方法对四种拓扑无效。23 个真实 LLM 配置的 161 场景验证确认理论预测（MAPE 1.6%）。

---

## Strengths

**S1 [共识]**: FWL 不变性是干净且重要的负面结果。对四种协变量拓扑，矩阵校正在线性 OLS 下精确实现 0% bias reduction，logistic 下偏差可忽略（< 0.01%, Table 5）。直接阻止实践者在这四种拓扑上浪费计算资源。

**S2 [共识]**: 三级证据层次（Proved / Numerically Verified / Conjectured）是方法论典范。Theorem 1 → Observation 1 → Conjecture 1 清晰界定证明边界。R1 称"在 NLP 理论工作中罕见且值得推广"，R2 称"应被 AC 特别注意"。

**S3 [共识]**: 首次系统覆盖 K≥3 × 7 种 DAG 拓扑。前作仅覆盖 K=2、4 种 DAG。每种拓扑的 bias 机制都有清晰的因果直觉支撑。

**S4 [共识]**: 实证验证规模充分且全面。161 scenarios MAPE 1.6%，per-topology 从 0.5%（confounding）到 5.7%（IV）。100,000 随机矩阵符号保持验证。

**S5 [共识]**: Proposition 1 的 sign preservation 条件结构清晰。四种拓扑分别用 Cauchy-Schwarz、Berkson attenuation、leakage boundedness 和结构性论证给出充分条件。

**S6 [共识]**: Algorithm 1 + Table 4 校正方法比较覆盖 210 配置（5 方法 × 6 error structures × 7 拓扑），对实践者直接可用。

---

## Weaknesses

### Major (3 项)

**W1 [Major, 分歧]**: ASV 相对于 E-value 的新颖性定位。
- R2: C(δ) 参数化与 E-value "高度同构"，三个 ASV 类型本质是同一 δ 在不同阈值。
- R1 反驳：扰动对象不同（annotation error vs. unmeasured confounding），sign-flip ASV 无 E-value 对应物，拓扑依赖性是独特创新。R1 Excitement 3.5/5 部分因 ASV 贡献来自系统性而非方法论突破。
- **Director 判定**：R1 技术正确，R2 的定位建议有价值。**建议 Section 3.3 增加 1 段显式 ASV-vs-E-value 对比**。

**W2 [Major, 共识]**: K≥3 理论不完整。Theorem 1 仅覆盖 K=2；Conjecture 1 依赖 210,000 次数值验证。两位 Reviewer 均认为诚实处理——R1 Soundness 仍给 4/5。R2 建议补充 K=3 符号计算验证。不构成拒稿理由。

**W3 [Major, 分歧→降级]**: Proportional effects (f=λg) 假设适用性。
- R1 原评为 should-fix（W1）：适用范围未充分论证，未从 23 个 LLM 配置估计 f/g 比值。但也指出 "B.15 non-proportional 下 97.3% 仍成立"这个观察被淹没在附录。
- R2 交叉回应 REBUT severity：Table 15 和 Proposition 4 提供充分 robustness。
- **Director 判定**：维持 should-fix。主文应引用 Table 15 robustness 结果。

### Should-Fix (8 项)

**W4 [Should-Fix, 共识]**: Abstract 信息密度过高（~5 个数字）。建议保留 1-2 核心数字，其余移至 Introduction。

**W5 [Should-Fix, R1 新增]**: Non-differential stress test 仅覆盖随机扰动模型。R1 指出 B.5 用 Uniform[-1,1] 随机 Δ，未测试结构化违反（outcome-conditional prompting、文本难度-outcome 关联、label-specific LLM bias）。建议补充至少一种结构化违反模型，或在 Limitations 中更明确讨论。

**W6 [Should-Fix, 共识]**: Section 3 NLP 可达性不足。plim/FWL 假设计量经济学背景。建议 Section 3.1 增加 "Notation roadmap"（3-4 句）。

**W7 [Should-Fix, 共识]**: LLM 配置多样性有限（四个 7-13B 开源模型，缺 commercial API、>70B、ordinal）。不影响核心贡献。Limitations 应更具体。

**W8 [Should-Fix, R1 新增]**: 校正方法比较（Table 4）固定 K=3，未验证 K 值敏感性。论文强调 K=2→K≥3 质变，但校正是否对此 robust 未验证。建议补充 K∈{2,5,10} 的校正比较（至少 2-3 种关键拓扑）。

**W9 [Should-Fix, 共识]**: ASV Bootstrap CI 过宽（exposure/IV 特异）。Exposure δ*=0.94 [0.60,1.36], IV δ*=0.75 [0.44,1.29] 跨越分界线。其余 5 种拓扑 CI 在同一类别内——拓扑特异问题，非框架缺陷。

**W10 [Should-Fix, 共识]**: 线性 SEM 结论的非线性推广整合不足。Appendix B.6/B.13 有 logistic 验证但主文未充分整合。R1 新增具体问题：logistic 下 bias 量级解释——log-odds ratio vs additive effect 量纲不同，"approximate correctness" 如何解释？

**W11 [Should-Fix, 共识]**: ClinicalBERT case study (Appendix B.3) 应在正文 Section 4.5 提及。展示 FWL 不变性实际意义。

### Minor (2 项)

**W12 [Minor, R1]**: IV 52.6% denominator sign change 缺乏 NLP 实践指导。应在 Section 4.1 增加 2-3 句——如 IV 策略需要的最低 diagonal dominance。

**W13 [Minor, R1]**: 四个文本问题——(M1) Eq.(2) wⱼₖ 的 marginal distribution 来源未 clarify; (M2) Figure 2 y 轴标签不够 informative; (M3) Section 4.4 "predictably" 主观用语; (M4) Limitations "outcome misclassification of A" 措辞歧义。

---

## Reviewer Consensus [AGREE]

1. FWL 不变性是论文最强、最干净的贡献
2. 三级证据层次是值得 AC 特别注意的方法论美德
3. K≥3 gap 是真实局限但诚实处理——不构成拒稿理由
4. Abstract 需减少数字密度；Section 3 需提高 NLP 可达性
5. Non-differential 假设需更好的主文讨论
6. 真实 LLM 验证对理论论文足够但多样性有限
7. 所有主要 weaknesses 可在 camera-ready 阶段解决

## Reviewer Divergence [REBUT]

1. **ASV vs E-value 新颖性**：R2 认为高度同构 → R1 反驳扰动对象不同且拓扑依赖性独特。Director 支持 R1 技术判断。
2. **Proportional effects 严重性**：R1 评 should-fix（evidence buried in appendix），R2 REBUT further downgrade（97.3% robustness）。Director 维持 should-fix。
3. **Overall 评分分歧**：R1 给 4.0 (Conference)，R2 给 3.5 (Borderline Conference)。分歧主要来自 Excitement（R1: 3.5, R2: 3.0）——R2 对 ASV 新颖性更保守。

---

## Questions for Authors

**Q1** [R1]: Theorem 1 中 V₀(δ) convexity 论证——当 f ≈ λg + small perturbation（near-proportional）时，monotonicity 是否以 Lipschitz 方式退化？Appendix B.12 暗示 worst-case deviation 0.01，但缺乏形式化。

**Q2** [R1]: PPI++ 对 M-bias -88% RMSE 的机制——是否与 M-bias collider conditioning 结构导致 gold labels 引入额外 selection bias 有关？

**Q3** [R1]: ASV bootstrap 不确定性仅在 N=1,500 测试。N > 100,000 时 sharp transition 是否更 sharp？N 增大主要影响 δ_sig 还是 δ_mag？

**Q4** [R1]: Logistic 下 bias 表达式的 "approximate correctness" 如何解释？Bias 方向正确但量级不适用，还是两者都近似正确？

**Q5** [R1]: Conjecture 1 的 per-topology ε（confounding 0.006, IV 0.112）——IV 的 11.2% 相对偏差在因果推断中是否可忽略？是否应讨论"可接受 ε 阈值"？

**Q6** [R2]: ASV sharp phase transition 对 N < 1,000 的实践含义？ASV 是渐近量，有限样本行为未刻画。

**Q7** [两位]: 23 个 LLM 配置的 non-differential departure ε 量级是多少？

**Q8** [R1]: PPI++ 在不同 gold label 比例下的性能降解？

**Q9** [R1]: ASV 在 DAG 不确定性下的 robustness？

---

## Missing References

1. **Prediction-Powered Causal Inferences** (2025, arXiv:2502.06343) [共识]
2. **Variance-Aware LLM Annotation** (2025, arXiv:2601.02370) [共识]
3. **Hidden Measurement Error in LLM Pipelines** (2026, arXiv:2604.11581) [共识]
4. **Dawid & Skene (1979)** [共识]
5. **Rosenbaum (2002), Mathur et al. (2018)** [共识]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查仍在进行中（started at 2026-05-23T03:56:05Z）。本报告不等待，完成后会自动补发到 Group C。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**评分拆解**：
- R1: 4.0 (Conference) — 认为核心贡献（FWL 不变性 + 七拓扑 bias taxonomy + 三级证据层次）足以支撑主会议接收，所有 weaknesses 可 camera-ready 解决
- R2: 3.5 (Borderline Conference) — 对 ASV 新颖性更保守（Excitement 3/5），认为 Conjecture 1 未证明和 NLP 可达性是拉低因素
- Director: 3.5，倾向 3.5-4.0 区间上半部

**评分理由**：

论文针对一个重要且时机恰当的问题提供了系统性理论分析。核心贡献清晰：

*支持接收的因素*（R1 4.0 的理由，Director 认可）：
1. 七种拓扑 × K≥3 的完整 bias 分析在文献中确为首次
2. 三级证据层次的方法论诚实度在 NLP 理论工作中罕见且值得推广
3. FWL 不变性比 "method X improves by Y%" 的正面结果更有长期影响
4. 实验验证超过理论论文的通常标准

*阻碍完全接收的因素*（R2 3.5 的理由，Director 部分认可）：
1. K≥3 monotonicity 停留在 conjecture，ASV 框架在主要使用场景下缺乏解析保证
2. ASV 与 E-value 的技术区分可以更鲜明（虽然 R1 已论证两者不同构）
3. 对 EMNLP 主流 NLP 读者门槛偏高
4. 非差异性假设的 stress test 缺少结构化违反模型（R1 新增的重要批评）
5. 校正方法比较缺少 K 值敏感性分析（R1 新增）

论文可发表，增量贡献明确。通过针对性修改（提高可达性、补充结构化 stress test 或在 Limitations 讨论、增加 K 值敏感性、显式 ASV-vs-E-value 对比），可达到 Conference (4.0) 水平。当前状态为强 Findings 候选或 Borderline Conference。

**Confidence: 4/5**

---

## Detailed Comments

### Section 1 (Introduction)
- 更早将 7 种拓扑分为 "sign-preserving"（5）和 "sign-reversing"（2）[R1]
- "first unified analysis" 措辞恰当 [共识]

### Section 3 (Method)
- Section 3.1 开头增加 "Notation roadmap"（3-4 句话）[W6]
- Definition 1 后增加 2-3 句直觉解释 non-differential 假设 [W5]
- Eq.(2) clarify wⱼₖ 的 marginal distribution 来源 [R1 M1]
- Section 3.3 增加 ASV-vs-E-value 显式对比段 [W1]
- 主文引用 Table 15 robustness（97.3% under non-proportional）[W3]

### Section 4 (Experiments)
- 用 1-2 句话提升 logistic DGP 核心结论到主文，clarify bias 量级解释 [W10]
- Section 4.1：IV 52.6% sign change 增加 NLP 实践 guidance [W12]
- Section 4.5：简要提及 ClinicalBERT case study [W11]
- Figure 2 y 轴标签更 informative [R1 M2]
- Section 4.4 "predictably" → "consistently with theoretical predictions" [R1 M3]

### Limitations
- 更具体讨论 LLM 多样性缺口 [W7]
- 增加有限样本 ASV 行为讨论 [Q6]
- 修正 "outcome misclassification of A" 措辞歧义 [R1 M4]
- 更明确讨论哪些 LLM 使用模式违反 non-differential 假设 [W5]

### 事实纠正
- R1 对 Appendix B.13 的描述有误（称"一个数据集"，实为 Monte Carlo 模拟）。已由 R2 纠正。
- R2 称"正文未讨论 PPI++ negative transfer"，但 Section 4.5 已明确提及。已由 R1 纠正。
- R1 交叉回应中引用了错误的表号（Table 13 是 logistic bias，不是 λ(C)）。已由 R2 纠正。