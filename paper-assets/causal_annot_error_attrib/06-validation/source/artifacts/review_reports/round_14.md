---
round: 14
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T10:57:05.157985+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 14 审稿报告

**论文**: "Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction"
**Venue**: EMNLP 2026 (ARR Long Paper)
**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性 + 完整性）
**审稿模式**: Fresh（重新审稿）

---

## Summary

本文研究 K-class LLM 标注误差在 7 种 canonical DAG 拓扑下的因果推断偏差传播。三个贡献：(1) 多分类偏差分类法——推导 7 种拓扑的偏差表达式（Eqs 1–5, 对一般 K），证明 confounding/collider 的符号保持（Propositions 1–6），构造 exposure/IV 的符号反转反例；(2) ASV 灵敏度诊断框架——证明 K=2 envelope monotonicity（Theorem 1），K≥3 数值验证（Conjecture 1, ε<0.06），定义三种互补 ASV 度量；(3) 校正指导——证明 FWL invariance 导致矩阵校正对 4 种协变量拓扑无效（负面结果）。通过 MC 模拟（161 scenarios, 1.6% MAPE）、3 个 NLP 数据集（23 个 LLM 配置）和 ClinicalBERT 案例验证。

---

## Strengths

**S1. 系统性范围覆盖前所未有。** 首个 K-class × 7 topology 的统一标注误差传播分析。Prior work 仅覆盖 1–4 种拓扑（Lee & Wood-Doughty 2024 仅 confounding；TeBlunthuis et al. 2024 限于 K=2, 4 DAGs）。K≥3 揭示定性新现象：exposure 下 83.4% 符号反转，而 K=2 时结构上不可能。[R1 S1, R2 S1 共识]

**S2. 三级证据层次的科学诚实性。** 论文明确区分 proved（Proposition 1, Theorem 1）、numerically verified（Observation 1, Numerical Verifications 1–2）和 conjectured（Conjecture 1）。这种分层在同类论文中不常见，是方法论美德。[R1 S2]

**S3. 符号保持证明技术正确。** R1 逐步验证了核心推导：Confounding 的 Cauchy-Schwarz 论证链、Collider 的 Berkson attenuation、Exposure 的 K=3 反例构造。Propositions 1–6 对一般 K 成立（非仅 K=2）。[R1 S3]

**S4. FWL invariance 负面结果新颖且有实践价值。** 证明矩阵校正对 4 种协变量拓扑无效（列空间保持论证简洁正确），直接帮助实践者避免无效操作。OLS 和 logistic 下均验证（Table 5, Table 13）。[R1 S5, R2 S3 共识]

**S5. 多层次验证流水线完整。** 解析推导 → MC 模拟（161 scenarios, N=10,000）→ 实证 LLM 混淆矩阵（23 配置 × 3 数据集）→ ClinicalBERT 案例（Appendix B.3）。210 种校正配置 × 6 方法。[R1 S4, R2 S4 共识]

**S6. Algorithm 1 具有可操作性。** 三步走决策流程（assess risk → select correction → FWL warning）将理论直接转化为 NLP 从业者工具。[R2 S5]

---

## Weaknesses

### Should-Fix

**W1. ASV 与 E-value 的形式化对比缺失。** [R2-W1, R1 AGREE]
- Section 3.3 将 ASV 定位为 "analogous to E-values"，Appendix B.20 Table 18 提供对比表但过于简略。全文无 proposition 或 theorem 形式化说明：(a) ASV 在何种条件下退化为 E-value；(b) K×K confusion matrix 参数化与 risk-ratio 参数化的数学区别；(c) sign-flip ASV 无法被 E-value 自然扩展的结构性原因。
- **影响**：如果 ASV 仅是 E-value 的 re-parameterization，方法论贡献被显著削弱。
- **建议**：正文增加 Remark 或 Proposition 形式化说明核心区别。
- **跨轮追踪**：R4-W6 → R6-W2 → R8-W1 → R11 → R12 → R13 → R14。连续 8 轮提出，论文虽调整了 ASV 定位（framework → diagnostics）并添加了 Table 18，但形式化对比仍缺失。

**W2. Conjecture 1 未证明但被 Algorithm 1 实质性使用。** [R1-W1, R2-W3, 双方 AGREE]
- Theorem 1（envelope monotonicity）仅在 K=2 + proportional effects 下证明。K≥3 降级为 Conjecture 1（30,000 matrices 数值验证, ε<0.06）。Algorithm 1 的 ASV 阈值判断隐式依赖 envelope monotonicity。
- **重要澄清（R2 成功 REBUT R1 的 critical 评级）**：论文的 "Multi-Class" 标题由偏差表达式（Eqs 1–5, 一般 K）+ 符号保持定理（Propositions 1–6, 一般 K）支撑，非仅由 Theorem 1 支撑。因此此问题影响 ASV 工具的可靠性，但不动摇核心理论贡献。
- **建议**：(a) Algorithm 1 添加显式声明"ASV 阈值有效性依赖 Conjecture 1，失效时误差上界 ε<0.06"；(b) 讨论 K≥3 证明的数学障碍（K=2 依赖 perspective function 凸性 + 单变量参数化；K≥3 参数空间变多维，凸性不再直接适用）；(c) 讨论 ε=0.06 在治疗效应估计中的具体含义。
- **跨轮追踪**：R8-C1 → R9-M1 → R11 → R12 → R13 → R14。

**W3. 比例效应条件 (f=λg) 限制性未充分探讨。** [R1-W2, R2 AGREE with nuance]
- Appendix B.13 报告一般 DGP 下 15–17% failure rate（Sparse DGP 24.2%），但 NLP-realistic DGP 的 sign failure rate 仅 0.07%（R2 补充）。论文未刻画何种结构条件下比例效应成立/失败，实践者无法判断自身 DGP 是否满足。
- **Director 判定**：R1 标记 critical 过重。NLP-realistic 场景 0.07% failure rate 表明该条件在目标应用中通常满足。降级为 should-fix。
- **建议**：(a) 给出比例效应的直觉解释；(b) 讨论实践者如何用观测数据近似评估此条件；(c) 正文提及 NLP-realistic 0.07% vs general 15-17% 的对比。
- **跨轮追踪**：R6-M3 → R8-C2 → R9-C1 → R11 → R12 → R13 → R14。

**W4. 对 EMNLP 读者的可及性不足。** [R2-W2, R1 部分 REBUT]
- Section 3.1–3.2 的 plim、FWL decomposition 等计量经济学术语对 EMNLP 广泛读者不友好。plim 脚注和 FWL 内联定义已添加（R12 修复），但缺少直觉性解释段落。
- **Director 判定**：R1 有理——目标读者（使用 LLM 标注进行因果推断的 NLP 研究者）应具备基本 CI 背景。但 EMNLP 受众广泛，增加 NLP running example 会显著提升可及性。保持 should-fix（低优先级）。
- **建议**：Section 3.1 增加 1 个具体 NLP 场景（如情感分类作为 treatment variable）串联偏差表达式推导。
- **跨轮追踪**：R9-C2 → R11-W2 → R12-W1 → R13 → R14。

**W5. IV 拓扑被标记为 maximally fragile 后缺少替代方案讨论。** [R1-W4, R2 AGREE]
- IV 被排除于 Conjecture 1 和 ASV 单调性分析之外（52.6% sign reversal under Dirichlet prior）。Algorithm 1 仅给消极建议（"不要校正"），未提供积极替代方案。
- **建议**：讨论 IV 设计中应对标注误差的替代策略（bounds approach、robust IV、two-sample IV）。
- **新发现**（R14 首次作为独立 issue 提出）。

### Minor

**W6. Abstract 数字密度过高。** [R2-W5, R1 AGREE] 10+ 个具体数字，信息过载。建议保留 3–4 个最关键数字。跨轮追踪：R3-NEW-4 → R8 → R11 → R12 → R13 → R14。

**W7. Table 1 的 Yes/Yes*/No 标注不够直观。** [R2-W6, R1 AGREE] 需查看脚注理解 Yes* 含义。建议改用 "Conditional" 或在 caption 中直接解释。

**W8. Algorithm 1 阈值过于具体化。** [R2-W7, R1 AGREE] 来自特定 MC 设置的阈值可能不适用于其他 DGP。建议标明为参考值并建议实践者根据场景校准。

**W9. 混淆矩阵 C 的可获得性是 chicken-and-egg 问题。** [R2 新发现] 框架假设 C 已知或可估计，但获取准确 C 需 gold-standard 标签。Limitations 应提及。

**W10. 实证验证仅覆盖 open-weight 模型。** [R1-W5, R2 AGREE] 4 个模型（7B–235B），无商业模型（GPT-4, Claude），无 ordinal 任务。核心贡献是理论性的，不依赖特定模型，但一般性声明应降低力度。跨轮追踪：R1-W3 → R9-S3 → R11 → R12 → R13 → R14。

---

## Reviewer Consensus [AGREE]

1. **Conjecture 1 的未证明状态是 soundness concern**：两位 Reviewer 独立识别此问题（R1-W1, R2-W3），交叉回应中双方确认。Algorithm 1 应显式声明对 Conjecture 1 的依赖。
2. **ASV vs E-value 形式化对比缺失削弱方法论贡献**：连续 8 轮提出，双方持续 AGREE。
3. **FWL invariance 是真正新颖且有实践价值的负面结果**：双方作为 top strength 识别（R1-S5, R2-S3）。
4. **三级证据层次（proved/verified/conjectured）是科学诚实的体现**：双方赞赏（R1-S2, R2 在交叉回应中 AGREE）。
5. **格式合规**：8 页限制 ✅，匿名性 ✅，Limitations 位置 ✅，References 格式 ✅。
6. **相关工作覆盖完整**：无关键遗漏。Imai et al. (2010), Pryzant et al. (2021), Feder et al. (2022) 等均已引用。

## Reviewer Divergence [REBUT]

1. **R1-W1 severity（Theorem 1 K=2 only = critical?）**
   - R1：core claim 在 multi-class 下未证明，标题与证明范围落差是 critical。
   - R2 REBUT：偏差表达式（Eqs 1–5）和符号保持（Props 1–6）均对一般 K 证明。仅 Theorem 1（monotonicity）限于 K=2。"Multi-Class" 标题由前两者支撑。
   - **Director 裁定**：R2 rebuttal 成立。降级为 should-fix。

2. **R1-W3（线性 SEM 下 sign preservation 未在非线性模型验证？）**
   - R1：符号保持在非线性模型下未验证。
   - R2 REBUT：Appendix B.7 Table 8 已验证 logistic 下 |ΔSF_r| < 0.02。R1 混淆了 FWL invariance 失效（校正方法限制）与符号保持（理论结果）。
   - **Director 裁定**：R2 rebuttal 成立。R1 的具体 claim 被事实纠正。线性 SEM 限制降为 minor。

3. **R2-W4（EMNLP venue fit 不足？）**
   - R2：核心贡献是纯因果推断方法论，NLP 连接通过应用域建立。
   - R1 REBUT：问题直接来自 NLP 实践（7 篇引用中 5 篇来自 *ACL），数据/模型均为 NLP，Algorithm 1 直接针对 NLP 研究者。先例：Feder et al. (2022) TACL, Keith et al. (2020) ACL。
   - **Director 裁定**：R1 rebuttal 成立。Venue fit 不构成 weakness。

4. **R2-W2（可及性 = should-fix?）**
   - R2：plim/FWL 对 EMNLP 读者不友好，should-fix。
   - R1 REBUT：目标读者应具备 CI 基础，建议降为 minor。
   - **Director 裁定**：保持 should-fix 但降低优先级。EMNLP 受众广泛，增加 NLP running example 有价值。

---

## Questions

**Q1** [R1-Q2, R2 AGREE]: Proposition 3 worst-case bound B（Eq. 16）依赖 DGP 参数（Var(g(A)), Var(f(A))）。实践者通常不知道真实 DGP 参数——如何从观测数据估计 B 的上界以判断符号保持是否成立？

**Q2** [R1-Q3, R2 AGREE]: Table 5（Appendix B.7）logistic 下矩阵校正产生 ~7% bias reduction。对高风险应用（如医疗因果推断），推荐的 non-matrix-based 替代方案是什么？

**Q3** [R1-Q4, R2 AGREE]: Appendix B.13 的 15–17% 单调性失败率是否集中在特定 confusion matrix 结构（如高度非对角占优）？如果失败集中在特定区间，实践者可提前排除。

**Q4** [R2-Q4, R1 AGREE]: DAG 拓扑未知时 Algorithm 1 如何使用？Limitations 简述 "apply under each candidate topology"，但应更显著地集成到 Algorithm 1 中。

**Q5** [R1-Q5, R2 AGREE]: ClinicalBERT 案例（Appendix B.18）OR=0.89 对混淆矩阵选择的敏感性如何？不同合理混淆矩阵下的 OR 分布（bootstrap/sensitivity analysis）会增强可信度。

---

## Missing References

两位 Reviewer 均确认相关工作覆盖完整。Imai, Keele & Tingley (2010), Pryzant et al. (2021), Feder et al. (2022), Wood-Doughty et al. (2018), VanderWeele & Ding (2017), Keith et al. (2020) 等关键文献均已引用。

R2 提到一篇可能相关的近期工作（arXiv:2602.15730, "Causal Effect Estimation with Latent Textual Treatments"），但聚焦 latent treatment 而非标注误差传播，非关键遗漏。

无关键缺失引用。

---

## External Review (Stanford Agentic Reviewer)

**状态**：未请求。项目配置未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：Agent 错误——rate limit 导致视觉审查 Agent 退出（"You've hit your limit · resets 4pm (UTC)"）。未能完成 PDF 渲染和逐页检查。

**替代检查（Director 手动）**：
- PDF 共 9 页（p1–8 正文 + Limitations，p9 起 References）
- Figure 1（p.3）：7 种 DAG 拓扑，清晰可读
- Figure 2（p.7）：Bias distributions，7 panel，尺寸偏小但可辨
- Figure 3（p.8）：F1 vs bias 散点图，标注清晰
- Table 1（p.7）：排版整洁，与 Figure 2 共享 p.7
- Appendix 23 页，排版规范

**用户可重新触发视觉审查**：本报告不因视觉审查缺失而推迟。

---

## Overall Assessment

### 评分（EMNLP 2026 ARR 标准）

| 维度 | 分数 | 理由 |
|------|------|------|
| **Soundness** | 3.5/5 | 在覆盖范围内（偏差表达式一般 K、符号保持一般 K、Theorem 1 限 K=2）理论严谨。Conjecture 1 的未证明性和比例效应限制是主要 concern，但 NLP-realistic 场景影响有限（0.07% sign failure）。R1 验证了核心证明的技术正确性。 |
| **Excitement** | 3.5/5 | 问题重要且时效性强（LLM 标注替代人工标注用于 CSS 因果推断）。7 拓扑统一分析新颖；FWL invariance 负面结果实用价值高。但线性 SEM + K=2 证明范围限制了即时实践影响。 |
| **Reproducibility** | 4.0/5 | Appendix 23 页提供完整推导、MC 参数、DGP 设置。Algorithm 1 可操作。承诺代码公开。唯一缺失：LLM 标注的 prompt 模板未提供。 |
| **Overall** | **3.5/5 (Borderline Conference)** | 两位 Reviewer 独立评分一致。技术贡献扎实（统一框架 + FWL invariance + 符号保持证明），验证流水线完整。主要 concern：ASV vs E-value 形式化对比缺失（连续 8 轮）、Conjecture 1 未证明但被 Algorithm 1 使用、比例效应限制性需更好论证。若 W1–W3 解决，可达 4.0 (Conference)。 |
| **Confidence** | 4/5 | R1 逐步验证了核心证明（Propositions 1–7, Theorem 1, FWL invariance）。R2 检查了格式合规、引用完整性、novelty 定位。交叉回应纠正了 R1 的两个 factual error（logistic sign preservation 已验证、Multi-Class 标题由偏差表达式 + 符号保持支撑）。 |

### 一句话总结

技术上严谨的因果推断工作（K-class × 7 topology 统一分析 + FWL invariance 负面结果 + 多层次验证），但 ASV 方法论贡献的独立性论证（vs E-value）和 K≥3 ASV 的理论基础（Conjecture 1）是 Borderline Conference 与 Conference 的关键区别因素。

### 距 Conference (4.0) 的差距

1. **ASV vs E-value 形式化对比**（W1）：增加 Remark/Proposition 说明数学结构区别 → 澄清方法论贡献独立性
2. **Algorithm 1 对 Conjecture 1 的依赖声明**（W2）：显式说明 + 讨论失效后果 → 增强用户信任
3. **比例效应的直觉解释和诊断指南**（W3）：正文提及 NLP-realistic 0.07% + 实践者评估指南 → 增强可操作性

---

## Detailed Comments

### Section 1 (Introduction)
- 第 2 段 "The transition at K≥3 is not gradual but structural" 的叙述有力且准确。
- 第 3 段 F₁ vs bias 的论证（Spearman ρ=−0.10, p=0.45）有效地建立了 topology > annotator quality 的核心 insight。但 power=0.57 意味着检测 |ρ|≥0.3 的能力有限——如果真实 ρ 在 0.1–0.2 之间，当前样本量无法区分。

### Section 3 (Method)
- Definition 1 (non-differential misclassification) 清晰，附有 NLP 场景直觉解释（p.4）。
- Section 3.1 "Notation conventions" 段（p.3-4）的 plim 脚注和 FWL 内联定义是 R12 修复的成果，有效但仍偏技术性。
- Conjecture 1（p.6）的 ε=0.06 容差——建议明确说明"这意味着在最坏情况下，ASV 可能低估实际偏差严重程度，但误差不超过 6% 的最大偏差量"。
- M-bias 和 front-door 已添加 NLP 场景示例（annotator expertise/topic difficulty, sentiment → engagement → revenue），有效增强可理解性。

### Section 4 (Experiments)
- Table 1（p.7）呈现 7 种拓扑的关键属性，设计紧凑有效。Yes* 标注需改进（W7）。
- Figure 3（p.8）F₁ vs bias 散点图清晰展示 topology > F₁ 的 insight。
- Section 4.5 FWL invariance 段已包含 "Under linear OLS" 限定和 logistic 下 < 0.065% 的结果——准确。
- Section 4.5 已提及 ClinicalBERT 验证（"Appendix B.3 confirms FWL invariance in clinical NLP"），解决了 R11-W1。
- PPI++ 对 M-bias 有害的机制解释（"misclassification attenuates the spurious M-bias path, and PPI++ removes this protective attenuation"）清晰。

### Section 5 + Limitations (p.8)
- Conclusion 简洁有效（4 句话）。
- Limitations 覆盖 6 点（non-differential, linear SEM, ASV parameterization, DAG uncertainty, FWL under logistic, LLM 配置范围），合理但应增加混淆矩阵 C 的可获得性问题（W9）。
- "Code and data will be released" 承诺 ✅。

### Appendix
- 23 页 appendix 详尽覆盖完整证明链、补充实验、stress tests。关键表格：Table 2（sign conditions summary, p.20）、Table 5（logistic FWL, p.22）、Table 7-8（stress test, p.23-24）、Table 10（envelope violations, p.26）、Table 12（proportional effects, p.28）、Table 18（ASV vs E-value, p.30）。
- Table 18 是 ASV vs E-value 对比表但过于简略——这是 W1 的核心位置。

### 格式
- 正文 8 页 ✅（Section 5 + Limitations 完全在 p.8 内）
- ACL [review] 模板 ✅
- 匿名 "Anonymous ACL submission" ✅
- 无代码链接或 deanonymization 风险 ✅
- References 格式一致 ✅
