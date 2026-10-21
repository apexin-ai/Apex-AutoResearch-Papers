---
round: 3
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T14:04:11.083970+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 3 合并审稿报告

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (via ARR), Long Paper
**Reviewers**: R1（方法严谨性）, R2（新颖性+完整性+写作+格式）
**审稿模式**: Fresh（重新审稿）

---

## Summary

本文系统研究了 K 类（K≥3）非差异误分类在七种典型因果 DAG 拓扑下的偏差传播。核心发现：(1) K=2 时二分类变量的 attenuation-toward-null 保证在 K≥3 时结构性崩塌——exposure 和 IV 拓扑可产生符号反转；(2) 其余五种拓扑维持符号保持（confounding 和 collider 有解析证明，mediation/M-bias/front-door 有数值验证）；(3) 提出 Annotation Sensitivity Values (ASV) 框架量化各拓扑的脆弱性光谱；(4) 证明 Frisch-Waugh-Lovell 不变性导致矩阵校正方法对 4/7 拓扑无效；(5) 通过真实 LLM confusion matrix 的经验验证确认理论预测。

---

## Strengths

**S1** [共识] **重要且及时的问题**。LLM 标注在计算社会科学中快速普及，标注误差对因果推断的影响是紧迫问题。本文提供了首个系统性框架。

**S2** [共识] **K≥3 代数断点的刻画**。证明 K=2 的符号保持保证在 K≥3 时因混淆矩阵高维自由度而结构性崩塌，这是一个非平凡的定性结果，对实践者有直接指导意义。

**S3** [共识] **FWL 不变性的实用洞察**。揭示矩阵校正方法（naive plug-in, MLA）对 4/7 拓扑 provably 无效，文献中长期被忽视，对实践者直接可操作。

**S4** [共识] **ASV 框架的可操作性**。提供参数化的敏感性分析工具，类比 E-values 但针对标注误差，包含三种互补度量（magnitude/significance/sign-flip），实用价值明确。

**S5** [共识] **系统覆盖面**。7 DAG 拓扑 × 5 校正方法 × 多种验证方式（100,000 随机矩阵 + 4 LLM × 3 数据集 + logistic DGP + case study），覆盖面全面。

**S6** [共识] **附录质量高**。12 页附录包含详细 Lemma-Proposition 证明链、stress test、bootstrap ASV 分析、case study，质量高于多数投稿。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [共识, critical] **正文超出 8 页限制约 0.5 页**
Section 5 (Conclusion) 在第 9 页开始，正文约 8.3 页。EMNLP 2026 Long Paper 严格限制 8 页正文（不含 References 和 Limitations）。main.tex 已使用 `\enlargethispage` 和压缩 `\floatsep` 等手段但仍超限。这是 ARR desk rejection 条件之一。
- *建议*：压缩 Section 4（Cross-K robustness 段和 ASV diagnostic results 段可移至附录）；Figure 1+2 占满整页，考虑缩小或合并；精简 Section 2 Related Work。

**N2** [共识, critical] **Sign reversal 严重性被过度声称**
Abstract 和 Introduction 以 Dirichlet(1,1,1) 全参数空间的 83.4% sign reversal 为主导叙事，辅以 "catastrophic" 等极端措辞。但：(1) Dirichlet(1,1,1) 包含大量不现实的非对角占优矩阵（平均准确率 1/K）；(2) 在实际 LLM 分类器精度下（diagonal ≥ 0.7），sign reversal 降至 2.1%；(3) 论文 Section 4.4 自身明确写道 "The primary coefficient (β₁, largest magnitude) never reverses across any empirical configuration; sign flips occur exclusively in secondary coefficients corresponding to rare categories with small |β|"。Section 4.2 的 "catastrophic sign reversal" 小标题与 Section 4.4 的实证结果自相矛盾。
- R1 补充：理论上任何系数 CAN reverse 的结论本身有价值，建议调整为 "sign reversal is theoretically possible for K≥3, practically rare for primary coefficients under realistic classifiers, but non-negligible for secondary coefficients"
- *建议*：(1) Abstract 先报告 realistic regime (diagonal ≥ 0.7, 2.1% sign reversal)，再提 Dirichlet 83.4% 作为理论上界；(2) 明确说明 empirical sign reversal 限于 secondary coefficients；(3) 用 "structurally possible" 替代 "catastrophic"

**N3** [R1 critical, R2 should-fix, 分歧] **Theorem 1 适用范围过窄，Conjecture 1 未证明**
Theorem 1 仅覆盖 confounding + proportional effects（f = λg）。其余 6 个非 IV 拓扑的 ASV 单调性依赖 Conjecture 1，而 Table 9 显示 60-97% 的随机矩阵违反严格单调性（虽然违反幅度 < 0.06）。如果单调性不成立，ASV 的 "临界 δ 阈值" 语义变得模糊。
- R1 立场：ASV 是论文核心实用贡献，其理论基础不应仅依赖 numerical verification → must-fix
- R2 立场：ASV 核心价值在于 topology ranking，ranking 在所有实验中成立，不完全依赖严格单调性；ε < 0.06 足够小 → should-fix
- *建议*：(1) 至少证明 mediation 的单调性（Eq.3 结构较简单）；(2) 给出 ε 关于 K 和 DGP 参数的 formal bound；(3) 明确讨论 Conjecture 失败时 ASV interpretation 如何 degrade

### Should-Fix（影响评分但不一票否决）

**W1** [共识] **3/5 sign preservation 拓扑 "establish" 措辞过度**
Abstract 用 "establish that five topologies show no sign reversal"，但 mediation/M-bias/front-door 仅有 100,000 随机矩阵的数值验证（Empirical Finding 1），附录明确写 "analytic proofs for general K remain open"。"Establish" 暗示证明而非验证。
- *建议*：改为 "prove for confounding and collider, and verify numerically for mediation, M-bias, and front-door"

**W2** [R1 critical, R2 should-fix, 分歧] **FWL invariance 结论缺乏 precise statement**
论文声称 "matrix-based corrections achieve exactly 0% bias reduction" 对 4 个 FWL 拓扑成立，但：(a) "matrix-based correction" 无精确定义；(b) SIMEX 的 0% reduction 与其理论上应能外推的预期矛盾，需解释；(c) 与 Carroll et al. (2006) 已知 residual confounding 结果的关系未澄清。
- R1 立场：缺 formal proof，无法区分深刻洞察 vs 实验 artifact → must-fix
- R2 立场：FWL invariance 是 FWL 定理的 direct corollary（C⁻¹ 不改变 column space → projection matrix 不变 → T 系数不变），3 行推导即可，是 writing clarity 问题 → should-fix
- *建议*：添加 precise definition + 3-4 行 FWL 推导 + SIMEX 解释 + Carroll (2006) 关系讨论

**W3** [共识] **Non-differential misclassification 假设讨论不足**
LLM 处理包含 Y 和 Z 信息的文本，P(A*|A,Y,Z) = P(A*|A) 在许多场景中不成立。Appendix B.4 的 extended stress test 覆盖 96 configurations（4 topologies × 2K × 3 CM × 4ε），但正文 Method 部分未讨论何时 LLM 满足此假设（如 LLM 未见 outcome 文本时）。
- *建议*：(1) 正文讨论具体 NLP 场景（sentiment vs. stance detection）；(2) stress test 进一步覆盖 confounding 拓扑

**W4** [共识] **线性 SEM 假设限制实用性**
所有结果基于线性结构方程。论文自身承认 "FWL invariance result does not hold for logistic regression"——Algorithm 1 的 FWL 分流建议在非线性设定下可能失效，但 Algorithm 1 未标注此 caveat。Appendix B.6 的 logistic DGP robustness check 仅覆盖 3/7 拓扑。
- *建议*：(1) Algorithm 1 标注 "linear models only"；(2) 扩展 Appendix B.6 至全部 7 拓扑

**W5** [共识] **缺少 outcome misclassification 讨论**
许多 NLP 因果研究中 Y 也由 LLM 标注。至少在 Limitations 中讨论 outcome misclassification 的影响和扩展方向。

**W6** [共识] **Abstract 信息过载**
Abstract 包含 15+ 个具体数字（83.4%, 52.6%, 13.7%, 2.1%, 47.0% 等），影响可读性。
- *建议*：保留 3-5 个最关键数字，其余移入正文

**W7** [共识] **未承诺代码/数据公开**
方法论论文含大量仿真实验，代码公开是 ARR 标准预期。ASV 计算工具作为 package 发布可大幅提升实用价值。

**W8** [R1 warning, R2 partially agrees] **新颖性定位不清**
K≥3 sign reversal 已被 Dosemeci (1990) 和 Veierød & Laake (2001) 指出；residual confounding 在 Greenland (2003) 和 Ogburn & VanderWeele (2012) 中已分析。论文应明确界定 "已知结果在 LLM 语境的应用" vs "真正新贡献"。R2 认为这是 framing 改进而非 novelty 不足。

**W9** [R1 warning, R2 partially agrees] **经验验证使用模拟 DGP 而非真实因果数据**
"Empirical validation" 用真实 LLM confusion matrices 但应用于模拟 DGP（线性 SEM），验证的是推导正确性而非实践指导价值。R2 认为这是方法论论文标准做法，但同意完整 real-world case study 会增强说服力。

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成共识：
1. **[AGREE]** 正文超 8 页限制 — 双方 critical
2. **[AGREE]** Sign reversal 83.4% framing overclaiming — 双方同意需调整叙事（R2 critical, R1 upgraded after cross-sharing）
3. **[AGREE]** Non-differential 假设讨论不足 — 双方 warning
4. **[AGREE]** 线性 SEM 限制 + Algorithm 1 缺 caveat — 双方 warning
5. **[AGREE]** Abstract 信息过载 — 双方 warning
6. **[AGREE]** 代码公开 — 双方 warning
7. **[AGREE]** 3/5 拓扑 "establish" 措辞过度 — 双方 warning
8. **[AGREE]** Outcome misclassification 缺讨论 — 双方 warning
9. **[AGREE]** 所有 6 条优势 — 双方一致
10. **[AGREE]** 新颖性评估：相对 Teblunthuis (2024) 和 Lee & Wood-Doughty (2024) 增量充分；ASV 创新中等；FWL invariance 实用价值高；topology-dependent 视角足够
11. **[AGREE]** 缺少 Cinelli & Hazlett (2020)、Gilardi et al. (2023)、Ziems et al. (2024) 等引用

---

## Reviewer Divergence

| 问题 | R1 | R2 | 分歧性质 |
|------|----|----|----------|
| Conjecture 1 严重性 | N1 must-fix | W2 should-fix | 严重性分歧：R1 认为 ASV 理论基础需保障，R2 认为 ranking 结论不受影响 |
| FWL invariance 证明 | N3 must-fix | Should-fix (writing) | 定性分歧：R1 要求 formal proof，R2 认为是 FWL 的 direct corollary 仅需改善表述 |
| 模拟 DGP 验证 | W5 warning | Partially agrees | R1 要求 semi-synthetic 实验，R2 认为方法论论文标准做法 |
| C(δ) 参数化唯一性 | — | Q4 (question) | R1 rebut：线性路径是自然选择但应讨论替代方案（唯一 REBUT 点） |

---

## Questions（需要作者澄清）

1. 在 realistic regime（diagonal ≥ 0.7）下 sign reversal rate 仅 2.1%，为何 abstract 选择以 83.4% 作为主要数字？
2. Empirical Finding 1（mediation, M-bias, front-door 的 sign preservation）是否有解析证明进展？如果这 3 个拓扑的保证只是 conjectural，论文核心 claim "five topologies maintain structural guarantee" 的可信度如何评估？
3. 论文是否计划公开代码和 ASV 计算工具？
4. Algorithm 1 在非线性模型（如 logistic regression）下是否仍然有效？FWL 分流分支的适用范围应如何界定？
5. C(δ) = (1-δ)I + δC₀ 线性参数化的选择理由是什么？如果实际退化路径不在此线上，ASV 的意义如何？

---

## Missing References

1. **Cinelli & Hazlett (2020)** "Making Sense of Sensitivity: Extending Omitted Variable Bias" — 与 ASV 框架有直接可比性（robustness value vs ASV），应在 Section 2 或 3.3 中讨论对比 [双方 AGREE]
2. **Gilardi et al. (2023)** "ChatGPT Outperforms Crowd-Workers for Text-Annotation Tasks" — LLM 标注的标志性论文 [双方 AGREE]
3. **Ziems et al. (2024)** "Can Large Language Models Transform Computational Social Science?" — 综合 survey，与论文 motivation 直接相关 [双方 AGREE]
4. **Bound, Brown & Mathiowetz (2001)** — Survey data 中 measurement error 经典综述 [双方 AGREE]
5. **Bayesian measurement error models 具体引用**（如 Richardson & Gilks 1993, Gustafson 2004 具体章节）— Section 4.5 提及但未引用具体工作 [双方 AGREE]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 因配额限制（rate limit）执行失败，未产出排版审查结果。建议用户可手动触发重试。

---

## Overall Assessment

**Overall Score: 3.5 — Borderline Conference**

**Soundness: 3.5/5** — 核心 bias 表达式和已有证明（Theorem 1, Propositions for confounding/collider）正确；但 Conjecture 1 未证明、3/5 sign preservation 仅有数值验证、FWL invariance 表述不够 precise。

**Excitement: 3.25/5** — Topology-dependent 视角是足够的概念创新，ASV 框架可操作，FWL invariance 被忽视但重要；但理论深度中等（Conjecture 而非 Theorem），ASV 是 E-value 的自然类比，K≥3 break 本身已被 Dosemeci (1990) 指出。

**Reproducibility: 4/5** — 数学公式清晰，DGP 参数详细，附录证明完整；但未承诺代码公开。

**Confidence: 4/5** — 两位 Reviewer 均熟悉测量误差理论和因果推断文献，逐页仔细阅读含附录。

**总体判断**：这是一篇重要且及时的方法论工作，系统性 taxonomy 和 ASV 框架有明确的实用价值。主要不足在于：(1) 格式问题（超页，desk rejection 风险）；(2) framing 过度声称（83.4% vs 2.1%，"catastrophic" vs secondary coefficients only）；(3) 理论完备性中等（Conjecture 未证明，部分 sign preservation 仅数值验证）。如果格式和 framing 问题能在修订中解决，论文有潜力达到 Conference (4.0) 水平；如果 Conjecture 1 能至少部分证明，理论贡献将显著增强。当前版本处于 Borderline Conference / Findings 交界。

---

## Detailed Comments

### Section 1 (Introduction)
- "catastrophic" 措辞与 Section 4.4 实证结果不符——primary coefficient 从未反转
- 建议添加 1-2 句 novelty delineation："The possibility of polytomous sign reversal was noted by Dosemeci et al. (1990); our contribution is the first systematic characterization across multiple DAG topologies and the ASV framework for quantifying this vulnerability."

### Section 2 (Related Work)
- 缺少 Cinelli & Hazlett (2020) 与 ASV 的对比讨论
- 缺少 Gilardi et al. (2023) 和 Ziems et al. (2024) 作为 LLM annotation 动机引用
- 可精简以节省页面空间

### Section 3.2 (Bias Expressions)
- Proposition 1 中 "establish" 措辞对 mediation/M-bias/front-door 过度——应区分 "proven" vs "numerically verified"
- Empirical Finding 1 的条件涉及未知 DGP 参数，实践中难以事前验证——论文已提 ASV 作为替代，但可进一步讨论

### Section 3.3 (ASV Framework)
- Theorem 1 限于 proportional effects——应讨论此假设何时成立/失败
- Conjecture 1：60-97% 矩阵违反严格单调性但幅度 < 0.06——应更诚实地讨论
- C(δ) 线性参数化的选择应讨论替代方案（matrix exponential, Dirichlet-based）

### Section 4 (Experiments)
- Section 4.2 "catastrophic sign reversal" 小标题与 Section 4.4 结果矛盾
- Cross-K robustness 和 ASV diagnostic 段可移至附录以节省空间
- "grand MAPE of 2.0% across 126 scenarios (18 LLM configurations × 7 topologies)" 的 126 = 18×7 推导出现在 Monte Carlo 验证段，容易与 empirical validation 混淆

### Section 4.5 (Correction Guidance)
- "matrix-based correction" 需 precise definition
- FWL invariance 需 3-4 行推导而非仅引用实验结果
- SIMEX 对 FWL 拓扑的 0% reduction 需解释为何不矛盾
- Algorithm 1 需标注 "linear models only" caveat
- Bayesian ME models 作为 FWL bypass 方案需引用具体工作

### Section 5 (Conclusion)
- 溢出到第 9 页——压缩或部分合入 Limitations

### Limitations
- 应增加 outcome misclassification 讨论
- Non-differential 假设的适用场景应更具体

### 附录
- 符号表（Table 8）存在但正文 τ/β_T 仍不一致
- Proposition 编号在正文与附录间缺乏交叉引用
- Figure 2 y 轴标签偏小，影响打印可读性

### 跨轮次 Issue 追踪
本轮为 Round 3 fresh 审稿。以下先前 issue 已确认修复：
- R1-N3 (ASV δ 定义域) — Section 3.3 引入 δ_max 约束 ✓
- R2-N2 ('first systematic framework' overclaim) — Abstract 已改为 'a systematic framework' ✓
- R2-N3 (4 篇缺失引用) — Related Work 已恢复 ✓
- R2-W2 (zero reversals vs narrative tension) — Triple verification narrative 已改善 ✓
- R2-W3 (ASV bootstrap uncertainty) — Appendix B.5 已包含 B=1,000 bootstrap 分析 ✓
- NEW-2 (Feder et al. 2022, Cheng et al. 2024) — Related Work 已引用 ✓
- NEW-3 (Conjecture 1 验证规模) — Appendix C 已扩展至 210,000 matrices ✓

以下 issue 持续存在或新增：
- R1-N1 (Theorem 1/Conjecture 1) — 持续 open（Round 1-3）
- R1-N2 (3/5 拓扑 "establish" 措辞) — 持续 open（Round 1-3）
- R2-N1 (83.4% framing) — 持续 open 且新增 secondary coefficient 维度（Round 1-3）
- R3-NEW-1 ~ R3-NEW-8 — 本轮新增 8 个 issue

完整 issue tracker 见 `artifacts/review_issues.yaml`。
