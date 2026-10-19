---
round: 6
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T17:58:46.084653+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 6（Fresh Review）

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026（ACL Rolling Review）
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1 方法严谨性 + R2 新颖性/完整性）
**交叉分享**: 完成，1 轮收敛
**Overall**: 3.5/5（Borderline Conference）

---

## Summary

本文研究 LLM 多类别（K≥3）标注误差如何沿 7 种典型因果 DAG 拓扑传播至下游因果估计。主要贡献：(1) 推导 7 种拓扑下非差异误分类的闭合偏差表达式，揭示二元 "偏向零" 保证在 K≥3 时结构性失效（83.4% exposure 矩阵产生 sign reversal）；(2) 证明 FWL 不变性使矩阵校正对 4 种 A-as-covariate 拓扑无效——被 annotation correction 文献忽略的 negative result；(3) 提出 ASV（Annotation Sensitivity Values）框架，三种互补类型（magnitude/significance/sign-flip）量化拓扑依赖的脆弱性谱。经验验证使用 4 个 LLM × 3 个 NLP 数据集（23 种配置，161 个 bias 场景）。

---

## Strengths

**S1. 真正的理论空白填补** [R1, R2 共识]
现有文献要么处理二元误分类（Brenner 1993），要么仅覆盖单一拓扑（Lee & Wood-Doughty 2024 仅 confounding）。本文首次在统一框架下系统比较 K≥3 误分类在 7 种 DAG 拓扑下的行为。核心发现——topology 而非 annotator quality 决定下游 bias（同一 F₁ 范围内 bias 相差 10×）——非平凡且有实际意义。

**S2. FWL 不变性的独立价值** [R1, R2 共识]
证明线性校正（C⁻¹ premultiplication, MLA, SIMEX）在 confounding/mediation/collider/M-bias 四种拓扑下 exactly 0% bias reduction。证明简洁（column space preservation under FWL projection, Appendix B.2），结论对 practitioners 有非平凡指导意义。

**S3. 透明的理论层级** [R1]
proved → verified → conjectured 三层体系科学诚实。Proposition 1 对 confounding/collider 的解析证明（Cauchy-Schwarz, general K）技术正确。

**S4. 扎实的验证规模** [R1, R2 共识]
100,000 random confusion matrices（每拓扑）+ 4 LLM × 3 真实 NLP 数据集（HumAID K=10, VAST K=3, CivilComments K=2）= 23 configurations, 161 bias scenarios。远超 "toy example" 水平。

**S5. 可操作的 ASV 框架和 Algorithm 1** [R2]
三种 ASV 类型提供从 "多大误差可容忍" 到 "何时符号翻转" 的完整风险图谱。Algorithm 1 给出拓扑→风险→校正方法选择的 actionable pipeline。

**S6. 时效性** [R2]
LLM 标注在 CSS 中的快速采用使标注误差对因果推断的影响成为紧迫问题，论文定位与 EMNLP 受众匹配。

---

## Weaknesses

### Must-Fix（1 项）

**W-MF1. [MUST-FIX] Abstract 与正文数值不一致** [R1-M4, R2-D1; 双方 AGREE]
- Abstract: "Under realistic LLM accuracy (diagonal ≥ 0.7), the sign reversal rate is 1.4%"
- Section 4.2: 在相同条件下报告 "2.1% sign reversal"
- 可能原因：不同的 averaging 方式（per-coefficient vs per-configuration vs per-topology），但 Abstract 未做限定
- **Action**: 统一数字并明确计算基础

### Should-Fix（6 项）

**W-SF1. Theorem 1 对 K≥3 未证明但标记为 "Theorem"** [R1-M1, R2-W2; 双方 AGREE]
- K=2 通过 perspective function + convexity 严格证明——正确且优雅
- K≥3 仅有数值验证（20,000 random triples, worst-case deviation < 0.005），不构成数学证明
- Conjecture 1 正确使用了 "conjecture" 命名，但 Theorem 1 的不一致命名凸显问题
- **Action**: 拆分为 Theorem（K=2）+ Proposition/Empirical Result（K≥3），或在陈述中显式分层

**W-SF2. Abstract 将 "primary coefficient never reverses" 称为 "structural property"，实际仅有经验支撑** [R1-M2; R2 交叉 AGREE]
- Footnote 2 承认是 23 LLM configurations 的经验观察
- Section 3 仅提供 magnitude dominance 启发式解释，无 formal proof 或 sufficient conditions
- "Structural property" 在学术语境中暗示数学保证
- **Action**: 改为 "empirical regularity" 或提供 formal sufficient conditions（diagonal dominance threshold + coefficient magnitude ratio）

**W-SF3. Proportional effects 假设 (f=λg) 讨论不足** [R1-M3; R2 交叉 AGREE with nuance]
- Theorem 1 核心条件，但主文未解释何时此假设合理
- Appendix A.4 有 general case 数值验证（230K matrices, deviation < 0.01），主文未引用
- R2 认为可降为 Should-Fix（非 Must-Fix），因附录有对冲
- **Action**: Section 3.2 增加 1-2 句说明 proportional effects 的现实含义 + 非比例情形的近似程度

**W-SF4. 线性模型假设与 NLP 实践的 scope mismatch** [R2-W1 CRITICAL → R1 REBUT → 共识 MAJOR/Should-Fix]
- 全部 bias 表达式、sign preservation、FWL invariance 建立在线性 SEM 上
- **R1 纠正 R2 事实错误**: Appendix B.6 覆盖全部 7 拓扑的 logistic DGP（非仅 exposure），Table 8 报告完整结果
- R1 论证：线性模型在 CSS 因果推断中仍广泛使用（Angrist & Pischke 2009），经典测量误差文献同样从线性出发
- 共识：真实限制但非致命——论文在线性框架内的贡献是完整的
- **Action**: Introduction/Conclusion 更明确 scope 为线性 SEM；讨论 B.6 非线性结果中哪些定性结论（如拓扑排序）保持

**W-SF5. ASV 与 E-value 的方法论创新边界不清晰** [R1-W4, R2-W3; 双方独立提出并交叉 AGREE]
- 论文声称三个 key differences，但可能仅是应用领域变换 + 自然延伸
- 未充分对比 mediation sensitivity analysis (Imai et al. 2010) 和 QBA framework (Lash et al. 2009)
- **Action**: 增加 ASV vs E-value/QBA 的技术对比（table 或 dedicated paragraph）

**W-SF6. Conjecture 1 与 Theorem 1 覆盖范围关系不清晰** [R1-W3; R2 交叉 AGREE]
- Theorem 1 覆盖 confounding/mediation；Conjecture 1 覆盖 collider/M-bias
- ε-approximate monotonicity 与 strict monotonicity 的关系未说明
- Exposure/front-door/IV 的 monotonicity 状态散落各处
- **Action**: Section 3.3 末尾加汇总句，明确每个拓扑的 monotonicity 状态和证明级别

### Minor（5 项）

**W-M1.** 缺失 3-4 篇引用：Shu & Yi (2019) 两篇（误分类×因果推断，最关键）、Cadei et al. (2025) PPI 因果推断扩展、Neuhaus (1999) [R2-W4; R1 部分 AGREE，降为 MINOR]

**W-M2.** Non-differential stress test (Appendix B.5) 仅覆盖 exposure 拓扑，应扩展到 confounding/mediation [R2-W5; R1 AGREE]

**W-M3.** Table 1 "Amplif." 列含义在 caption 中未解释 [R2-D3; R1 AGREE]

**W-M4.** Algorithm 1 未显式排除 PPI++ 对 M-bias 的使用（Section 4.5 报告 -88% 有害）[R2-D5; R1 AGREE]

**W-M5.** Figure 2 子图过小，6 个分布细节难辨 [R2-D2; R1 AGREE]

---

## Reviewer Consensus

**[AGREE] 的关键共识**（两位 Reviewer 一致）：
1. Theorem 1 K≥3 命名不严谨——应拆分或显式分层
2. Abstract "structural property" 措辞过度——应降为 "empirical regularity"
3. 1.4% vs 2.1% 数值不一致——必须修正
4. ASV vs E-value 差异化不足——需要明确技术对比
5. 论文在线性框架内的贡献是扎实和完整的
6. FWL 不变性是独立有价值的 negative result
7. Algorithm 1 需加入 PPI++ M-bias guard

## Reviewer Divergence

**R2-W1 严重程度**：R2 定为 CRITICAL（线性假设根本性限制 NLP 适用性），R1 REBUT 降为 MAJOR。

- R1 纠正了 R2 的事实性错误（Appendix B.6 覆盖全部 7 拓扑，非仅 exposure）
- R1 论证线性模型在 CSS 因果推断中是标准方法，且经典测量误差文献同样线性起步
- **Director 判断**: 采纳 R1 的 MAJOR 定级。R2 的核心关切（scope mismatch）成立，但论文已在 B.6 提供非线性 robustness check，且 Limitations 已承认此限制。CRITICAL 意味着不可修补，而此问题可通过更诚实的 scoping 解决。

**R2-W4 严重程度**：R2 定为 MAJOR（遗漏 5 篇引用），R1 部分 REBUT 降为 MINOR。

- R1 同意 3-4 篇应引，但指出 Dawid & Skene (1979) 非必要（本文不涉及 multi-annotator）
- 核心 Related Work 覆盖已较完整
- **Director 判断**: 采纳 R1 的 MINOR 定级。引用补充是直接修复，不构成 structural concern。

**R2-W6（信息密度）**：R2 认为 Section 3.2 密度过高，R1 REBUT。

- **Director 判断**: 采纳 R1 的判断。8 页限制下 7 拓扑的系统覆盖是论文核心贡献，统一结构（bias expression → sign behavior → insight）使扫描可行。

---

## Questions for Authors

**Q1.** [R1-Q1] 是否存在 formal sufficient conditions 保证 primary coefficient 不反转（如 diagonal dominance threshold + |β₁|/|β₂| ratio）？
**Q2.** [R1-Q2] Proportional effects 假设 f=λg 对应什么具体的 DGP 场景？何时不成立？
**Q3.** [R1-Q3] Abstract 中 1.4% 的精确定义和计算基础？与 Section 4.2 的 2.1% 是什么关系？
**Q4.** [R1-Q4, R2-Q4] ASV 相对 E-value 在方法论上的独立技术贡献是什么？
**Q5.** [R2-Q1] 非线性 DGP 下完整拓扑比较数据是否可用？拓扑排序是否与线性一致？
**Q6.** [R2-Q2] C₀ 估计基于小 validation set (<100 gold labels) 时，ASV 可靠性如何？
**Q7.** [R1-Q5] 对 FWL invariance 使校正失效的 4 种拓扑，除 PPI++ 外还有什么 gold-free 策略？

---

## Missing References

1. **Shu, D. & Yi, G.Y. (2019).** Weighted causal inference methods with mismeasured covariates and misclassified outcomes. *Statistics in Medicine*, 38(10), 1835-1854. [最关键——直接处理误分类×因果推断]
2. **Shu, D. & Yi, G.Y. (2019).** Causal inference with measurement error in outcomes. *Statistical Methods in Medical Research*, 28(7), 2049-2068.
3. **Cadei, R. et al. (2025).** Prediction-Powered Causal Inferences. *arXiv:2502.06343*. [PPI→因果推断扩展，与 Section 4.5 直接相关]
4. **Neuhaus, J.M. (1999).** Bias and efficiency loss due to misclassified responses in binary regression. *Biometrika*, 86(4), 843-855.

---

## External Review

**状态**: 未请求（项目配置未启用外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: error — 视觉审查 Agent 因 API 限额异常退出（"You've hit your limit · resets 4pm (UTC)"），未完成页面级排版检查。用户可在限额重置后重新触发 `dispatch_visual_check`。

从 PDF 目视检查（非 Agent 系统化检查）：
- 正文 8 页，Limitations + References 从第 9 页起，符合 EMNLP 8 页限制
- Figure 1（DAG taxonomy）清晰可辨，但 Figure 2（bias distributions）6 个子图在半栏宽下细节较难分辨
- Table 1 结构清晰，但 "Amplif." 列缺 caption 解释
- 匿名性完整（"Anonymous ACL submission"，无 de-anonymizing 信息）

---

## Overall Assessment

**Overall Score: 3.5/5 — Borderline Conference**

| 维度 | R1 | R2 | 综合 |
|------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.5 | 3.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | **3.5** |

**置信度**: 4/5（两位 Reviewer 独立收敛到相同评分，交叉回应后核心判断一致）

**核心判断**：

论文在线性 SEM + 非差异误分类框架内填补了 multi-class × multi-topology 的真正理论空白。FWL 不变性是有独立价值的 negative result，ASV 框架对 practitioners 可操作。验证规模（100K matrices + 23 真实 LLM 配置）远超同类工作。

**阻碍更高评分的关键因素**：
1. **证明完备性**：Theorem 1 对 K≥3 的命名不严谨，"primary coefficient never reverses" 被过度声称为 "structural property"
2. **Scope 限制**：线性 SEM 假设在 NLP 实践中适用范围有限，多项结果限于 K=3
3. **Novelty 定位**：ASV 相对 E-value 的方法论增量需更清晰 delineation

所有问题均可在 ARR revision 中修补。主要修改量集中在措辞调整（Theorem 命名、Abstract 表述、数值统一）和少量补充讨论（proportional effects、ASV 对比、缺失引用），不涉及实验重做或理论推翻。

**建议投递方向**：如果能在 ARR submission deadline (2026-05-25) 前完成 Must-Fix（数值统一）和关键 Should-Fix（Theorem 命名、Abstract 措辞），论文有望在 ARR review 中获得 3.5-4.0 分（Borderline Conference 到 Conference），进入 EMNLP 2026 Main 或 Findings。

---

## Detailed Comments（逐节）

### Abstract
- 1.4% vs 2.1% 数值不一致 [W-MF1]
- "structural property" → "empirical regularity" [W-SF2]
- R2-D1：未明确 sign reversal 仅限 exposure/IV 拓扑，可能误导

### Section 1 (Introduction)
- Framing 总体清晰，三个 contribution 明确
- 数字密度在前 2 轮修改后已改善
- 可更明确地 scope 为 linear SEM

### Section 2 (Related Work)
- 核心覆盖完整（Carroll, Gustafson, Pearl, VanderWeele & Ding, Edwards et al.）
- 补充 Shu & Yi (2019), Cadei et al. (2025), Neuhaus (1999) [W-M1]

### Section 3 (Method)
- 3.1 Setup: non-differential 定义清晰；"text as common cause" 讨论充分
- 3.2 Bias expressions: 7 拓扑按统一结构呈现，系统完整
  - Theorem 1 命名需修正 [W-SF1]
  - Proportional effects 讨论不足 [W-SF3]
  - Conjecture 1 与 Theorem 1 关系不清 [W-SF6]
- 3.3 ASV: 框架设计合理
  - vs E-value 差异化不足 [W-SF5]

### Section 4 (Experiments)
- 4.1 Setup: Monte Carlo 设计充分
- 4.2 Taxonomy: 验证扎实，Table 1 "Amplif." 需解释 [W-M3]
- 4.3 ASV validation: envelope monotonicity 验证充分
- 4.4 Empirical: 23 configs 提供真实 grounding
- 4.5 Correction: FWL 证明干净；Algorithm 1 缺 PPI++ M-bias guard [W-M4]

### Section 5 (Conclusion) + Limitations
- 结论准确反映贡献
- Limitations 覆盖关键限制（non-differential, linear, K 范围, single annotator）
- 可扩展：ASV 在大 K 时的计算成本

### Figures and Tables
- Figure 1: 清晰可辨
- Figure 2: 子图过小 [W-M5]
- Figure 3 (F₁ vs bias): 有效传达核心信息
- Table 1: 结构清晰，caption 需完善 [W-M3]
