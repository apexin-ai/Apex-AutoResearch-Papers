---
round: 15
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T11:53:01.474045+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 15（Fresh Review）

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: 重新审稿（fresh）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验完整性; R2: 新颖性+完整性+表达）
**交叉分享**: 完成（1 轮即收敛）
**日期**: 2026-05-23

---

## Summary

本文研究 K-class LLM 标注误差（非差分误分类）在 7 种典型 DAG 拓扑下对因果估计的偏差传播。主要贡献：(1) 推导 7 种拓扑的闭合形式偏差表达式，证明 K≥3 引入结构性 sign reversal（二元情形不存在）；(2) 提出 Annotation Sensitivity Values (ASV) 框架，给出拓扑依赖的脆弱性排序（IV 最脆弱，M-bias 免疫）；(3) 证明 FWL invariance 使矩阵校正对 4 种协变量拓扑无效，提供拓扑感知的校正指南。K=2 的 ASV 单调性有严格证明（Theorem 1），K≥3 仅有数值验证支撑的 Conjecture 1。实验在合成 DGP + 23 个真实 LLM 混淆矩阵上验证，Theory-MC MAPE 1.6%。

---

## Strengths

**S1** [R1+R2 共识] 首次系统研究 K≥3 多类标注误差在 7 种 DAG 拓扑下的因果偏差传播，对 binary-only 文献（Wood-Doughty 2018/2024, Teblunthuis 2024）是实质性扩展。选题重要且时机恰当——LLM 标注在 CSS 中快速普及。

**S2** [R1+R2 共识] 三级证据层次（proved / numerically verified / conjectured）科学透明，避免常见的过度声明。两位 Reviewer 均赞为方法论美德。

**S3** [R1] 7 种拓扑的闭合形式偏差表达式（Eqs. 1-3 及 Appendix A.3-A.8）为一般 K 推导，理论贡献扎实。

**S4** [R1+R2 共识] FWL invariance 负结果（Section 4.5）——矩阵校正对 4 种协变量拓扑 exactly 0% bias reduction——具有直接实践指导意义，回答了"不应该做什么"。

**S5** [R1] Theory-MC 一致性 MAPE 1.6% across 161 scenarios（23 LLM configs × 7 topologies），验证规模充分、精度高。

**S6** [R1] 23 页附录包含完整证明、15+ 项鲁棒性检查（非线性 DGP、cross-K、bootstrap CI、non-differential stress test 等），学术严谨度出色。

**S7** [R2] K≥3 sign reversal 发现（83.4% under uniform Dirichlet, 2.1% under realistic accuracy）对多类标注场景的 CSS 实践者有直接警示价值。

**S8** [R1+R2 共识] F₁ 与 causal bias 无显著相关（Spearman ρ = −0.10, p = 0.45, Figure 5）——标准分类指标不能替代拓扑感知的因果分析，对 NLP 实践者有重要警示。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W-MF1** [R1-N1 + R2-N1, 共识 critical] **K≥3 ASV 单调性仅为 Conjecture，论文最核心的实用贡献缺乏理论保证**

Theorem 1 仅证明 K=2 在 proportional effects 下的 envelope monotonicity。对于论文标题强调的 "Multi-Class"（K≥3）情形，ASV 的拓扑脆弱性排序和 Algorithm 1 校正指南完全依赖 Conjecture 1（ε-approximate monotonicity, ε < 0.06），该猜想仅有 210,000 随机矩阵的数值支撑。随机采样无法排除特定对抗性矩阵结构导致单调性失效的可能。

**附加事实性问题**（R1 发现，R2 确认）：Observation 1 (p.6) 声称 "worst-case deviations < 0.005"，但 Table 10 (Appendix, p.27) 显示 confounding K=3 worst magnitude = 0.011，front-door = 0.031——构成表面数值矛盾。两处使用不同矩阵数量（30,000 vs 10,000），但更多矩阵应发现更大偏差，无法解释差异。

建议修改方向：(a) 修正 Observation 1 数值或澄清度量定义差异；(b) 补充对抗性搜索（gradient-based optimization over column-stochastic C），而非仅 Dirichlet 随机采样；(c) 量化 violation 的参数空间特征——ε < 0.06 集中在什么类型的矩阵？real LLM 中是否出现过？(d) 讨论 violation 时 ASV ranking 的实际鲁棒性。

### Should-Fix（影响评分但不一票否决）

**W-SF1** [R2-N2 提出 must-fix, R1 AGREE 但降为 should-fix; Director 采纳 should-fix（高优先级）] **对 EMNLP 受众的可及性不足**

计量经济学术语（plim, FWL, Wald estimator, E-value, column-stochastic）解释不充分。plim 在 Abstract/Introduction 隐含使用但正式定义在 p.4 脚注 1；FWL 作为核心概念仅 p.3 一句话解释；E-value 未解释基本思想就与 ASV 对比。Abstract 在约 250 词内覆盖 7 拓扑 × sign reversal × ASV × monotonicity × correction × FWL + 大量具体数字，认知负荷极高。

Director 裁决：降为 should-fix，理由：(a) ACL venue 接受跨学科论文（如 Feder et al. 2022），(b) 8 页限制下增加 Preliminaries 可能压缩核心内容。建议优先：Abstract 精简（保留 1-2 核心发现）+ E-value/FWL 直觉解释（各 1-2 句），空间效率最高。

**W-SF2** [R1-N2 提出 must-fix, R2 REBUT 降为 should-fix; Director 采纳 should-fix] **缺乏真实观测数据的端到端因果分析验证**

所有实验均为合成线性 SEM + 注入真实 LLM 混淆矩阵。Section 4.4 "Empirical Validation" 验证的是 theory-MC 一致性，未在任何真实观测数据上运行完整因果分析流程（LLM 标注 → ASV 诊断 → 校正 → 因果估计评估）。Appendix B.18 政治广告案例仅停留在 ASV 诊断层面。

Director 裁决：降为 should-fix，理由：(a) 核心贡献是理论性的，三层验证已是高标准；(b) 端到端验证需同时有 gold labels 和 known causal effects，结构性困难；(c) ARR H13 不要求额外实验。建议将 B.18 扩展为完整校正流程演示。

**W-SF3** [R1-W1 + R2-W1, 共识 should-fix] **Non-differential misclassification 假设的适用性讨论和验证不够充分**

Table 15 (Appendix B.16) 显示安全阈值极紧——多数数据集要求 ε < 0.02。Stress test (Table 7, Appendix B.6) 仅 exposure 拓扑有完整表格，extended 4-topology test 仅文字摘要无表格。LLM 可能通过上下文间接获取 Y 信号，few-shot 示例可能引入 differential bias。

建议：(a) 将 extended stress test 4 拓扑结果以表格呈现；(b) 讨论 LLM CoT/few-shot 可能引入的 differential patterns；(c) 给出定量指导——超过什么阈值时结论不可靠。

**W-SF4** [R2-W2, R1 AGREE] **与核心 prior work 的增量区分不够清晰**

Remark 1 (p.6) 的 ASV vs E-value 三点对比各仅一句话，不够充分。Correction guidance 的贡献性质（benchmark 式比较 vs 方法创新）定位不清。建议增加结构化对比表。

**W-SF5** [R1-W5, R2 AGREE] **Theorem 1 的 proportional effects 假设限制性强且实践中难以验证**

f ⊥ g 时 OOB 率达 25%（Appendix B.13），NLP-realistic 下 0.07%。但实践者无法先验验证 proportional effects 是否成立。R2 补充：sufficient condition not necessary，Appendix B.13 数值分析全面。共识 should-fix（偏 minor）。

**W-SF6** [R1-W4, R2 AGREE] **Abstract FWL invariance 声明缺少 "under linear OLS" 限定**

Abstract "provably ineffective" 未标注 FWL 严格仅在 linear OLS 下成立。Logistic 下 breaks（|ΔSF| < 0.02, Table 5）。修复成本极低。

**W-SF7** [R2-W5, R1 AGREE] **Algorithm 1 经验阈值缺乏理论依据**

90.6% RMSE reduction、τ_conf > 0.7 等阈值从 Table 4/7 经验提取，未讨论对不同 DGP 参数的敏感性。

**W-SF8** [R1-W2, R2 AGREE] **Table 1 Violation vs Sign Flip 列定义模糊**

Caption 未显式定义两列含义，Violation 和 Sign Flip 的包含关系不直观。

### Minor

**W-MI1** [R1-M3 + R2-W4, 共识] Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难。Figure 3 y 轴标签不够直观。

**W-MI2** [R1-W3, R2 部分 REBUT] ASV 参数化 C(δ) 假设均匀退化。R2 澄清 C₀ 本身捕获非均匀性、δ 是标准做法；但同意应补充 real LLM C₀ 下的 ranking 稳定性检验。

**W-MI3** [R1-M1] 符号密度高（约 20 个符号），可考虑正文增加 notation summary。

**W-MI4** [R1-M2] Algorithm 1 是最具实践价值的输出之一，但被放在 Appendix 最后一页。建议正文 Section 4.5 中放置简化版。

**W-MI5** [R2 minor] Abstract "seven canonical" 的 canonical 选取标准未解释。

**W-MI6** [R2 minor] Figure 1 caption "starred-node" 含义应在 caption 内解释。

**W-MI7** [R2 minor] 匿名审稿阶段建议提供 anonymous repository 链接供 reproducibility 验证。

---

## Reviewer Consensus

以下为两位 Reviewer 通过交叉分享达成的共识：

1. **[AGREE] K≥3 ASV 单调性未证明是论文最大的理论缺口**（R1-N1 = R2-N1）。Observation 1 与 Table 10 的数值不一致进一步削弱可信度。
2. **[AGREE] Non-differential 假设的实践可信度需更充分讨论和验证**（R1-W1 ≈ R2-W1）。Stress test 完整表格仅覆盖 exposure 拓扑。
3. **[AGREE] Abstract 信息密度过高，计量术语解释不充分**（方向一致，severity 分歧见下）。
4. **[AGREE] Figure 可读性有改进空间**（R1-M3 = R2-W4）。
5. **[AGREE] Abstract FWL invariance 应加 "under linear OLS"**（R1-W4, R2 AGREE）。
6. **[AGREE] Algorithm 1 阈值是经验性的**（R2-W5, R1 AGREE）。
7. **[AGREE] Table 1 列定义需明确**（R1-W2, R2 AGREE）。
8. **[AGREE] ASV vs E-value 对比不够充分**（R2-W2, R1 AGREE）。
9. **[AGREE] 三级证据层次是方法论美德**（S2）。
10. **[AGREE] FWL invariance 负结果有独立实践价值**（S4）。

---

## Reviewer Divergence

1. **EMNLP 受众可及性的严重程度**：R2 列为 must-fix（EMNLP 主流读者无法 follow 方法论会限制 impact），R1 降为 should-fix（ACL 接受跨学科论文，8 页限制下增加 Preliminaries 会压缩核心内容）。**Director 裁决：should-fix（高优先级）**。R1 的页面约束论点成立，但 R2 对受众匹配的担忧合理。建议低空间成本的改进：Abstract 精简 + 关键术语直觉解释。

2. **真实数据端到端验证的严重程度**：R1 列为 must-fix（Abstract "topology-aware analysis is necessary" 缺乏真实数据支撑），R2 降为 should-fix（核心贡献是理论性的，端到端验证存在结构性困难）。**Director 裁决：should-fix**。R2 的三个论点（理论贡献的验证标准、ARR H13、ground truth 获取困难）更有说服力。

3. **任务覆盖范围**：R2 建议增加 NER/RE/event detection 任务。R1 REBUT——这些是 span-level 任务，超出 K×K 混淆矩阵框架的适用范围，但同意分类任务内数据集多样性不足。**Director 裁决：采纳 R1 的 REBUT**。NER/RE 确实超出框架范围。但在分类任务内增加数据集多样性（如 topic classification, NLI）是合理的低优先级建议。

---

## Questions

以下为需要作者回应的关键问题（按优先级排序）：

1. **[R1+R2] Observation 1 数值澄清**：Observation 1 "< 0.005"、Conjecture 1 "ε < 0.06"、Table 10 "0.011/0.031" 三者之间的关系？使用的偏差度量是否相同？

2. **[R1+R2] Conjecture 1 violation 分布**：ε < 0.06 的 violations 在 confusion matrix 参数空间中的分布如何？集中在对角占优度极低的区域？这类矩阵在 23 个 LLM 配置中出现过吗？

3. **[R1+R2] Differential misclassification 下 ASV ranking 稳定性**：在 outcome-dependent 分类偏差（ε = 0.03-0.05）下，ASV vulnerability ranking 是否仍稳定？

4. **[R1] 当前主流 LLM 准确率**：GPT-4o/Claude 在同类任务上准确率是否已显著高于 0.45-0.81？如是，框架警示在多大程度上仍适用？

5. **[R2] Logistic FWL 等价性**：Table 5 的 "practically negligible"（< 0.005）判断是否依赖 DGP 参数？是否存在使 deviation 变得 substantial 的参数配置？

---

## Missing References

**R2 提出**：Imai, Keele, and Tingley (2010) "A General Approach to Causal Mediation Analysis"。R1 确认遗漏程度有限（VanderWeele 2015 等已覆盖因果中介）。**查证**：references.bib 已包含 imai_keele_tingley2010 和 imai_keele_yamamoto2010，Related Work p.3 已引用。实际未遗漏。

**R1**：未发现重大引用遗漏。可考虑补充近期 LLM calibration 文献。

**Director 结论**：无关键引用遗漏。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置中未开启 external_review）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 因配额限制未能完成实际页面检查（error: "You've hit your limit · resets 4pm (UTC)"）。格式合规性由两位 Reviewer 人工确认：
- ✅ 正文 8 页（Sections 1-5 + Limitations），符合 EMNLP 2026 Long Paper 限制
- ✅ Limitations section 存在（p.8-9），覆盖 3 个主要局限
- ✅ Double-blind 合规——"Anonymous ACL submission"，无身份信息泄露
- ✅ 引用格式正确，ACL 模板
- ✅ 附录 23 页，包含完整证明和补充实验
- ⚠️ Figure 2 子图过小（7 个子图 single-column），灰度打印颜色区分困难

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

**置信度: 4/5**（两位 Reviewer 均给出 4/5 置信度，交叉分享后在核心问题上达成共识）

**评分理由**：

论文解决了一个重要且未被系统研究的问题——K-class LLM annotation error 在因果推断中的 topology-dependent 传播。工作量巨大（7 拓扑 × K-class × 3 ASV × 5 校正方法 × 23 页附录），三级证据层次和 FWL invariance 负结果均有独立方法论价值。

然而，论文最核心的实用贡献——K≥3 下 ASV 的拓扑脆弱性排序——依赖未证明的 Conjecture 1，且正文（Observation 1）与附录（Table 10）存在数值不一致，削弱可信度。对 EMNLP 受众的可及性不足（计量术语解释不充分、Abstract 过于密集）可能限制实际 impact。

**从 3.5 提升至 4.0 (Conference) 的关键路径**：
1. 修正 Observation 1 与 Table 10 的数值矛盾（factual correction，最低成本）
2. 为 Conjecture 1 补充 failure mode 分析（violation 集中区域、ranking 鲁棒性）或 partial proof
3. Abstract 精简 + 关键术语（plim/FWL/E-value）增加直觉解释
4. Abstract 加 "under linear regression" 限定 FWL 声明

以上 4 项中，第 1 和第 4 项可在 rebuttal/camera-ready 中即时完成，第 3 项可在 camera-ready 中完成，第 2 项需要一定的技术工作但不需要新实验。

---

## Detailed Comments

### Abstract (p.1)
- 约 250 词，覆盖概念过多。建议精简至 3 个核心发现：(1) K≥3 sign reversal, (2) topology-dependent vulnerability ranking, (3) FWL invariance negative result。具体数字（83.4%, 2.1%, 52.6%, 210,000, 1.6% MAPE 等）保留 2-3 个最有冲击力的即可。
- "matrix-based corrections are provably ineffective" 需加 "under linear regression"。

### Section 1 Introduction (pp.1-2)
- 叙事结构清晰（problem → gap → contribution → evidence）。
- Contribution 3（correction guidance）的性质定位不清——是方法创新还是 benchmark 式比较？建议明确区分。

### Section 2 Related Work (pp.2-3)
- 引用覆盖充分，涵盖测量误差、因果推断、NLP 标注质量三条文献线。
- 与 Teblunthuis (2024) 和 Lee et al. (2024) 的技术增量可更具体（如对比表）。

### Section 3 Method (pp.3-6)
- Bias expressions (Eqs. 1-3) 推导清晰，一般 K 下成立。
- Proposition 1 (sign preservation)：confounding 和 collider 的解析证明完整正确。条件 "|τ| > √..." 缺少直觉解释。
- Theorem 1 (K=2 monotonicity)：证明利用 perspective function 凸性，技术上正确。Proportional effects 假设的讨论可更充分（可验证性和退化行为）。
- Observation 1 (K≥3 monotonicity)："< 0.005" 与 Table 10 不一致，需修正。
- Conjecture 1 (ε-approximate)：数值验证规模（210,000 矩阵）充分但缺乏对抗性搜索。"under default DGP parameters" 限定适当。
- Remark 1 (ASV vs E-value)：三点对比每个仅一句话，不够充分。

### Section 4 Experiments (pp.6-8)
- Theory-MC MAPE 1.6% 精度高。
- Table 1 Violation/Sign Flip 列定义需在 caption 中明确。
- Figure 5 (F₁ vs bias)：信息传达有效。
- Section 4.5 correction guidance：FWL invariance 论证清晰。PPI++ M-bias 有害的机制解释（protective attenuation removal）到位。
- Algorithm 1 在 Appendix 最后一页，建议正文放简化版。

### Section 5 Conclusion + Limitations (p.8-9)
- Conclusion 简洁恰当。
- Limitations 覆盖 3 个主要局限（non-differential 假设、线性 SEM、观测范围），长度适当。Gold-label bootstrapping 约束已提及。
- 可补充：Algorithm 1 阈值的 DGP 依赖性。

### Appendix (pp.9-31)
- 完整证明（7 拓扑 sign preservation + Theorem 1 monotonicity），15+ 鲁棒性检查。
- Table 10 与 Observation 1 数值需对齐。
- B.18 政治广告案例可扩展为完整校正流程。