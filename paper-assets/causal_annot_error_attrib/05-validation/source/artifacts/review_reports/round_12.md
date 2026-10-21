---
round: 12
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T06:48:51.867211+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 12 审稿报告

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**类型**: Long Paper (8 页限制)
**Reviewer**: R1（方法严谨性）+ R2（新颖性与完整性）
**轮次**: Round 12 (fresh mode)

---

## Summary

本文研究 K 类（K≥3）LLM 标注误差在因果推断中的拓扑依赖传播机制。作者推导了 7 种 DAG 拓扑下的闭式偏差表达式，证明 K≥3 引入 binary 不存在的符号反转（sign reversal）——exposure 和 IV 拓扑可反转因果效应符号，而 5 种拓扑维持结构性保证。提出 Annotation Sensitivity Values (ASV) 敏感性分析框架，揭示从 IV（最脆弱）到 M-bias（免疫）的脆弱性谱。证明 FWL 不变性使矩阵校正在 4 种协变量拓扑下完全无效（0% bias reduction）。23 个 LLM 配置 × 3 NLP 任务的经验验证与理论预测一致（MAPE 1.6%）。

---

## Strengths

**S1 [共识]: 拓扑依赖框架的系统性填补真实空白。** 将混淆矩阵 C 与 DAG 拓扑的交互效应作为核心分析维度是本文最重要的贡献。Teblunthuis (2024) 仅覆盖 binary×4 DAGs，Lee & Wood-Doughty (2024) 仅覆盖 categorical×1 DAG。本文首次在 K≥3×7 topologies 交叉点提供统一分析框架，发现"同一混淆矩阵在不同拓扑下产生质的不同偏差"（R1-S1, R2-S1 共识）。

**S2 [共识]: 证据层次的诚实标注（Proved/Verified/Conjectured）。** 论文对 K=2 提供完整证明（Theorem 1），对 K≥3 明确区分三级证据层次。Table 2 汇总了各拓扑的充分条件和验证状态。这种自我约束在方法论论文中值得肯定（R1-S2, R2-S4 共识）。

**S3 [共识]: 理论-模拟一致性极强。** MAPE 1.6% across 161 scenarios (23 LLM configs × 7 topologies)，有效排除推导中的代数错误，为闭式表达式提供强数值支撑（R1-S3, R2-S1 共识）。

**S4 [共识]: FWL 不变性是干净且有实践价值的负面结果。** 证明矩阵校正（MLA, DSL）在 confounding/mediation/collider/M-bias 下精确 0% bias reduction，直接驳斥"有混淆矩阵就能校正"的朴素假设。逻辑回归下不变性经验性保持（<0.005, Table 13）（R1-S4, R2-S3 共识）。

**S5 [共识]: ASV 框架实用性。** 三种互补 ASV 指标（magnitude, significance, sign-flip）覆盖不同实践需求。Sign-flip ASV 识别临界 N*（低于此阈值所有 rejection 被阻断）在 E-value 框架中无对应物。Algorithm 1 提供可直接使用的决策流程（R1-S5, R2-S2/S5 共识）。

---

## Weaknesses

### Must-Fix

**W1 [R1 must-fix / R2 should-fix → Director 判定 should-fix]: Theorem 1 仅限 K=2，K≥3 核心单调性停留在 Conjecture。**
- 论文标题承诺 "Multi-Class" 但 Theorem 1 (envelope monotonicity) 仅对 K=2 成立。K≥3 完全依赖 Observation 1（20,000+ 配置数值验证）和 Conjecture 1（ε<0.06 approximate monotonicity）。
- R1 评 must-fix（影响核心 claim 可信度），R2 评 should-fix（数值验证规模充分，ASV 实践价值不完全依赖 monotonicity）。
- **Director 判定 should-fix**：论文已诚实标注三级证据层次，数值验证规模充分（30,000 matrices × K∈{3,5,7}），violation magnitude negligible（≤10⁻¹²）。但论文**应在正文中讨论 Conjecture 1 失效时对 Algorithm 1 实践指导的具体影响**——如果 monotonicity 不严格成立，δ 阈值判定是否仍可靠？

**W2 [R1 must-fix / R2 agree → Director 判定 should-fix]: 非差异性错分假设在 LLM 场景下论证不足。**
- Definition 1 要求 P(A*|A,Y,Z) = P(A*|A)。Appendix B.5 的 stress test 覆盖 ε=0.10-0.50，但未直接从 23 个 LLM 经验矩阵估计实际差异性程度。
- R1 评 must-fix，R2 同意问题存在但补充 ε=0.10 更接近实际。
- **Director 判定 should-fix**：假设在标准 text classification pipeline（LLM 仅看 source text）下合理，stress test 覆盖了有意义的 ε 范围。但论文应从现有 gold label subset 估计实际 differential degree，使参数选择有经验依据。

**W3 [R2 M5, R1 交叉确认 → Director 判定 must-fix]: 正文可能超出 8 页限制。**
- Section 5 (Conclusion) 从 p8 下方 1/3 处延续至 p9 顶部约 4-5 行。EMNLP 2026 的 8 页正文限制是硬约束（Limitations/ethical considerations 不计入）。
- **Director 判定 must-fix**：格式违规是 desk reject 风险。必须压缩结论使正文完全收入 8 页。

### Should-Fix

**W4 [R1 W3, R2 W3 共识]: 计量经济学术语对 EMNLP 受众可及性不足。**
- plim (probability limit) 在 Section 3.2 频繁出现但未定义其直觉含义。FWL (Frisch-Waugh-Lovell) 在 Section 4.5 引用但未陈述定理内容。对 CL/NLP 读者不友好。
- 建议：Section 3.1 加 plim 脚注定义（"大样本下估计量收敛到的值"）；FWL 首次使用加内联解释（"partialling out controls"）。

**W5 [R1 W3, R2 W3 共识]: 线性 SEM 假设的正文讨论不足。**
- Appendix B.6/B.13 的 logistic DGP 验证充分（Table 5, Table 13: sign-flip rate 差异 <0.02, FWL bias reduction <0.005），但正文仅一句 "structural patterns persist under logistic DGP"。
- 建议：Section 4.5 增加 1-2 句总结 logistic 发现 + 显式引用 Appendix B.13。

**W6 [R1 W4, R2 交叉 AGREE]: 校正方法比较仅在 K=3 下进行。**
- Table 4 的 RMSE reduction 仅覆盖 K=3。FWL 不变性与 K 无关（代数性质），但 PPI++ 和 MC-SIMEX 的相对性能可能随 K 变化——PPI++ 在 K>3 需更多 gold labels，MC-SIMEX 外推精度可能下降。
- 建议：至少在附录中补充 K=5/K=10 校正方法排名稳定性验证。

**W7 [R1 W6, R2 W4 共识]: 实证验证规模偏小。**
- 23 个 LLM 配置来自 4 个模型 × 3 任务，缺少商业 API（GPT-4/Claude）、>235B 模型、NER 等结构化标注任务。CivilComments 实际为 K=2，与 K≥3 核心贡献不完全对齐。
- 两位 Reviewer 共识：不影响核心贡献（理论结果与 LLM 无关），但限制泛化性声明。

**W8 [R2 W2, R1 交叉降为 minor]: Abstract 信息密度过高。**
- Abstract 包含至少 9-10 个定量信息点，对不熟悉该领域的 EMNLP 读者构成认知负担。
- 建议：聚焦 2-3 个核心数字（83.4% sign reversal, FWL 0% bias reduction），其余移至 Introduction。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识：

1. **[AGREE] 拓扑依赖框架是真正的新贡献**——K≥3 下 stochastic constraint 打破 binary 结构保证是非平凡理论发现
2. **[AGREE] 三级证据层次（Proved/Verified/Conjectured）标注诚实**——Table 2 清晰区分各结果证明状态
3. **[AGREE] FWL 不变性是干净的负面结果**——矩阵校正对 4 种协变量拓扑精确无效
4. **[AGREE] Conjecture 1 未证明削弱理论完整性**（分歧仅在严重性：must-fix vs should-fix）
5. **[AGREE] 非差异性假设论证不足**——未从实际 LLM 数据估计差异性程度
6. **[AGREE] 正文可能超 8 页限制**——Conclusion 溢出至 p9
7. **[AGREE] EMNLP 受众可及性不足**——plim/FWL 等术语需解释
8. **[AGREE] 线性 SEM 正文讨论不足**——logistic 结果在附录但正文未引用
9. **[AGREE] Algorithm 1 阈值硬编码自 K=3**——适用条件未标注
10. **[AGREE] "First unified analysis" 声明准确**（R1 REBUT R2-W5 成功）
11. **[AGREE] 缺失引用**：VanderWeele (2015) 因果中介标准参考、Schennach (2020) 非线性测量误差综述

## Reviewer Divergence

1. **Conjecture 1 严重性** [分歧保留]
   - R1: must-fix（标题承诺 Multi-Class 但 Theorem 限 K=2，影响核心 claim 可信度）
   - R2: should-fix（数值验证规模充分，ASV 实践价值不完全依赖 monotonicity）
   - Director: 采纳 should-fix（论文已诚实标注，violation magnitude negligible）

2. **ASV bootstrap CI 宽度** [R2 REBUT 成功]
   - R1 W5: should-fix（CI 跨越安全/不安全分界，影响可操作性）
   - R2 REBUT: 排名稳定性比绝对值更重要，CI 宽度反映真实参数不确定性而非框架缺陷
   - Director: 采纳 R2 观点，降为 minor

3. **Stock & Yogo (2005) 引用必要性** [R1 REBUT 成功]
   - R2: 应引用弱 IV 文献
   - R1 REBUT: 论文处理的是 instrument measurement error 而非 instrument relevance，分析目标不同
   - Director: 采纳 R1 观点，可选引用但非必要

---

## Questions

**Q1 [R1, R2 共识]:** K≥3 证明困难的解析直觉是什么？K≥3 的 K²-K 额外自由度允许 off-diagonal 交叉污染（cross-contamination），打破 K=2 的 1-自由度结构约束，使凸性论证不再全局成立。正文应更清晰解释此直觉。

**Q2 [R1]:** 能否从 23 个 LLM 配置的 gold label subset 直接估计实际差异性程度（P(A*|A,Y) vs P(A*|A) 的经验偏离）？这将使 stress test 的 ε 参数选择更有实际依据。

**Q3 [R2]:** ASV 的 diagonal parameterization C(δ) = (1-δ)I + δC₀ 假设所有类别均匀退化。实际中稀有类别退化更快——1D 降维是否遗漏关键信息？建议在 Limitations 讨论多维 ASV 扩展方向。

**Q4 [R2]:** FWL 不变性对非参数/半参数因果推断方法（doubly robust estimators, TMLE）是否仍成立？这关系到 Algorithm 1 对现代因果推断工具箱的适用性。论文应在 Limitations 标注此适用边界。

**Q5 [R2]:** PPI++ 需要 ≥20% gold labels（Table 14）。Algorithm 1 是否需要 cost-aware 版本——讨论 gold label budget 对方法选择的影响？

---

## Missing References

**MR1 [R2 提出, R1 AGREE]:** VanderWeele (2015, "Explanation in Causal Inference")——因果中介分析标准参考。论文 mediation 拓扑分析大量使用中介概念但未引用此标准参考。

**MR2 [R1 提出, R2 AGREE]:** Schennach (2020)——非线性/半参数测量误差综述。论文假设线性 SEM 但声称对 NLP 有指导意义，应讨论非线性扩展的可能性和挑战。

**MR3 [R1 提出, R2 AGREE]:** Si et al. (2023, "Can ChatGPT Replace Traditional Annotation Pipelines?") 或类似 LLM 标注质量系统评估——补充 non-differential 假设的经验支撑。

**MR4 [R2 提出, R1 REBUT → 可选]:** Stock & Yogo (2005, "Testing for weak instruments in linear IV regression")——与 IV 拓扑概念相关但分析目标不同。可作为补充背景。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（1 critical, 4 warnings, 7 info）。

**Critical:**
- 前 6 页连续纯文本无任何 figure/table，审稿人在形成第一印象时完全没有视觉锚点。Figure 1（DAG 拓扑图）是核心概念图，应前移至 Introduction（P1-P2）。

**Warnings:**
- P7 三个 display items（Figure 1 + Figure 2 + Table 1）挤在同一页，每个图表被压缩。Figure 2 直方图细节在当前尺寸下勉强可读。
- 正文 8.5 页仅 4 个 display items（3 figures + 1 table），主要实验结果表格（Table 3-4）全在 Appendix，审稿人在正文中看不到核心定量结果表格。
- Appendix P21 三图挤一页，Figure 5（混淆矩阵热力图）色块文字较难辨认。
- Figure 7（ASV magnitude ranges）使用红绿色板对色盲不友好，建议改用蓝/橙或 Okabe-Ito 色板。

**Info:**
- Figure 2 建议除颜色外增加 marker shape 区分，提高打印和色盲场景可辨识度。
- Figure 3 caption 较简短，建议增加"如何阅读此图"说明。
- References 排版正常，无未解析引用。
- Algorithm 1 伪代码框排版清晰。

---

## Overall Assessment

### 评分汇总

| 维度 | R1 | R2 | Director 综合 |
|------|-----|-----|-------------|
| Soundness | 3.5/5 | 4/5 | **3.5/5** |
| Excitement | 3.5/5 | 3.5/5 | **3.5/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5/5 | 3.5/5 | **3.5/5** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Overall Assessment: 3.5 — Borderline Conference

**推荐：Borderline Conference (3.5)**

论文在一个重要且 timely 的问题上做出了系统性贡献：
- (+) 拓扑依赖的多类错分偏差分析是真正的新视角，将分散的单拓扑/binary 先前工作统一为 7 topology × K≥3 框架
- (+) K≥3 sign reversal 发现（83.4% under Dirichlet, 2.1% under realistic accuracy）具有实践警示价值
- (+) FWL 不变性负面结果干净且有实操指导意义
- (+) 三级证据层次标注体现学术诚实
- (+) Algorithm 1 提供可直接使用的决策流程

但存在以下限制使其处于 Conference 门槛边缘：
- (-) 核心 K≥3 单调性停留在 Conjecture（有充分数值支撑但无解析证明），与标题 "Multi-Class" 承诺存在落差
- (-) 非差异性假设在 LLM 场景下的经验依据不足
- (-) 对 EMNLP 受众的可及性不足（plim/FWL 未解释，logistic 结果未在正文引用）
- (-) 实证验证仅 23 个配置，缺少商业 API 和端到端验证
- (-) 正文可能超 8 页限制（格式风险）

如果 W3（页数）、W4（术语可及性）、W5（logistic 正文讨论）能在 camera-ready 前修复，论文可达到 Conference 水平。如果这些改善无法实现，Findings track 是合理的去向。

### 置信度: 4/5
两位 Reviewer 仔细检查了核心证明、Monte Carlo 验证设计、stress test 方法论和经验验证设计，对因果推断和测量误差文献有足够背景。

---

## Detailed Comments

### Section 1 (Introduction)
- 叙事结构清晰：从 LLM 标注趋势 → K≥3 结构性转变 → F1 不预测因果风险 → 三个贡献
- "first unified analysis...building on prior single-topology analyses" 措辞准确（R1 REBUT R2-W5 确认）
- 建议减少 Abstract 中的定量信息点至 2-3 个

### Section 3 (Method)
- Section 3.1: plim 未定义直觉含义，建议加脚注
- Section 3.2: 7 种拓扑的偏差表达式推导清晰，Proposition 1 的 (a)(b)(c) 条件结构合理
- Section 3.3: ASV 的 K²→1D 降维和三类指标设计合理；Theorem 1 限 K=2 已正确标注；proof obstacle 解释（perspective function convexity 在 K≥3 失效）应更清晰
- **建议增加 ASV-vs-E-value 显式对比**：sign-flip ASV 和 N* 是 E-value 无对应物的新贡献

### Section 4 (Experiments)
- Section 4.2: Table 1 三级符号（✓/✓*/✗）清晰
- Section 4.3: ASV ranking（IV 最脆弱 → M-bias 免疫）跨 DGP 稳定
- Section 4.4: 经验验证（23 configs, 161 scenarios, MAPE 1.6%）充分但规模可更大
- Section 4.5: 校正指导有实践价值，但 K=3 限制应明确标注；FWL 适用边界（仅线性/logistic）应标注

### Section 5 (Conclusion) + Limitations
- Conclusion 溢出至 p9，必须压缩
- Limitations 覆盖了 non-differential 假设、线性 SEM、LLM 覆盖度——内容合理但可补充 ASV diagonal parameterization 假设
- 建议补充：FWL 不变性对非参数方法不适用的显式声明

### Appendix
- 证明完整（A.1-A.8），数值验证详实（B.1-B.17）
- ClinicalBERT 案例（B.3）和 Political Ad Tone 案例（B.17）有实践价值，建议在正文中引用
- 附录材料是论文的重要支撑，Reproducibility 条件充分