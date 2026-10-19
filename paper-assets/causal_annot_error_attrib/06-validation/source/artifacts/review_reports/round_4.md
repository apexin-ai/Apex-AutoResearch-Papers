---
round: 4
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-22T15:08:40.340635+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (via ARR), Long Paper
**ARR Deadline**: 2026-05-25
**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性与完整性）
**圆桌轮次**: 1 轮（Round 1 + 交叉分享后收敛）

---

## Summary

本文推导了七种 DAG 拓扑下 K 类非差异误分类对因果估计的偏差表达式，证明 exposure 和 IV 拓扑可产生符号反转（K≥3 时结构性可能，K=2 时不可能），其余五种拓扑保持符号。提出 Annotation Sensitivity Values (ASV) 框架量化各拓扑的脆弱程度，揭示 FWL 不变性导致矩阵修正方法对四种 covariate 拓扑无效。经 23 个真实 LLM 配置 × 7 拓扑 = 161 场景验证，理论预测与 Monte Carlo 模拟一致（grand MAPE 2.0%）。

---

## Strengths

**S1. 系统性填补明确文献空白（R1, R2 共识）。** 现有工作限于 binary misclassification（Teblunthuis 2024，4 DAGs）或单拓扑 categorical 扩展（Lee & Wood-Doughty 2024，仅 confounding）。本文首次在 K≥3 条件下系统覆盖七种拓扑——"first to characterize across seven topologies" 经核查成立。

**S2. FWL 不变性是干净优雅的 negative result（R1, R2 共识）。** 证明当 A 作为 covariate 进入回归时，任何对 dummy matrix D* 的线性变换不改变 treatment coefficient。这直接否定了四种拓扑下矩阵修正方法的有效性，有实际指导意义。Table 4 中 Naive/MLA 均为 0.0% 数值验证了这一结论。

**S3. Exposure 符号翻转结果是核心亮点（R1）。** Proposition 6（Appendix A.8）显式构造反例证明 K≥3 即使 C_kk > 0.5 也可翻转；Dirichlet(1,1,1) 下 83.4% 翻转率，realistic diagonal ≥ 0.7 时 2.1%。K=2 control 严格为 0%，确认结构性断裂。

**S4. 实证验证规模充足（R1, R2 共识）。** 23 个真实 LLM confusion matrix（4 模型 × 3 数据集 × 多 prompting）× 7 拓扑 = 161 bias scenarios。Figure 3 直观展示 F₁ 不预测因果风险。

**S5. 附录质量高（R2）。** 23 页中 15 页附录，含完整证明、反例构造、robustness checks（非线性 DGP、cross-K、bootstrap ASV），大幅增强可信度。

**S6. 实用工作流（R1）。** Algorithm 1 提供从 DAG 识别→校正方法选择的完整决策指南。

---

## Weaknesses

### Must-Fix

**W1 [CRITICAL — R1 首发, R2 AGREE] Theorem 1（envelope monotonicity）证明对一般 K 不完整。**
Theorem 1 声称 proportional effects 下 |B(C(δ))| 单调非递减。证明引用 DPI（data processing inequality），但 C(δ) = (1-δ)I + δC₀ 线性插值族不满足 stochastic degradation 条件（C(δ₂) = M·C(δ₁) for stochastic M）。论文在 Appendix 中承认 "the exact degradation factorization... is non-trivial"。标为 Theorem 的结果解析证明仅对 K=2 对称情形完成。Appendix A.4 存在不依赖 DPI 的直接证明路径（V_W(δ) 单调性），但未升级为完整证明。**必须补全证明或降格为 Conjecture/Proposition。**

**W2 [CRITICAL — R2 首发, R1 AGREE] Abstract/Introduction 对 83.4% 符号反转率的 framing 具有误导性。**
83.4% 来自 uniform Dirichlet(1,1,1) 先验（含大量 realistic 中不可能出现的近置换矩阵）。Realistic accuracy（diagonal ≥ 0.7）下仅 2.1%。更关键：Section 4.3 显示 primary coefficient never reverses，符号反转仅发生在 secondary coefficients with small |β|。但 Abstract 以 alarm tone 将 83.4% 置于最突出位置。R1 指出 83.4% 作为 K≥3 vs K=2 结构断裂量化有理论价值不应移除。**共识：两个数字应同等突出，明确区分 primary/secondary coefficient 风险。**

### Should-Fix

**W3 [MAJOR — R1 首发, R2 AGREE] Eq. (3) 中 λ(C) ∈ [0,1] 未被证明。**
Section 3.2 Mediation 段声明 λ(C) ∈ [0,1]，但 Appendix A.5 中的推导仅数值验证。如果 λ(C) 可超出 [0,1]，mediation bias 的解释将根本改变。应至少提供 sketch proof 或标注为 assumption。

**W4 [MAJOR — R1 首发, R2 强烈 AGREE] "Empirical Finding 1" 术语误导。**
"Empirical Finding" 通常指真实数据发现，而非 Monte Carlo 数值验证。这模糊了已证明结果（Proposition 1: confounding, collider）和未证明结果（mediation, M-bias, front-door）的严格区分。应改为 "Numerical Finding 1" 或升级为 Conjecture/Proposition。全文应建立 Proved → Numerically verified → Conjectured 的清晰三级层次。

**W5 [MAJOR — R1 首发, R2 AGREE] Non-differential misclassification 假设讨论不足。**
LLM 处理的文本可能同时含 A 和 Y 信息。R2 补充两个具体违反场景：(1) outcome-conditional prompting；(2) few-shot ICL 中 demonstration examples 引入的 systematic error。Stress test（Appendix B.5）仅 ε ≤ 0.10 小偏离且限于 exposure topology。应在 Limitations 中明确列举可能违反的 NLP 场景。

**W6 [MAJOR — R2 首发, R1 REBUT] ASV 方法论创新有限——E-value 的直接移植？**
R2 认为 ASV 核心思路是 E-value 框架的移植（将 unmeasured confounding strength 替换为 misclassification severity δ）。R1 反驳：技术差异实质性——(1) E-value 参数化标量 Γ 天然单调，ASV 将 K×K matrix 映射到 1D 路径需额外证明 monotonicity；(2) 三种 ASV 类型 vs E-value 单类型；(3) topology-dependent ranking 是核心贡献。**分歧未完全解决，但 R1 的技术区分有 merit。建议作者更明确定位 ASV 的贡献边界。**

**W7 [MAJOR — R2 首发, R1 REBUT] 论文广度有余深度不足。**
R2 认为同时覆盖 bias taxonomy + ASV + correction + empirical validation 导致每个方向偏浅。R1 反驳：系统性比较是核心贡献，sign-flip 二分法、FWL 不变性、ASV vulnerability ranking 均需跨拓扑才能发现。**分歧未完全解决——这是论文定位问题而非技术错误。**

**W8 [MAJOR — R1 首发, R2 REBUT（降级为 Limitation）] DAG 拓扑必须先验已知。**
Algorithm 1 依赖正确拓扑输入。R2 认为这是因果推断通用 limitation（E-values 和 robustness values 同样需要），但同意应在 Limitations 中提及。共识：在 Limitations 添加一句 "our framework assumes the causal DAG is correctly specified"。

### Minor

**W9 [MINOR — R1 首发, R2 AGREE] Conjecture 1 的 ε < 0.06 bound 可能依赖 DGP 参数。** 当 τ 很小时 6% 相对偏差可能影响推断。建议报告 ε 在多组 DGP 参数下的 sensitivity。

**W10 [MINOR — R1 首发, R2 AGREE] PPI++ 对 M-bias 有害 (-88%) 缺乏机制解释。** R2 给出了推论链（PPI++ 纠正误分类 → 恢复精确调整 → 恢复 M-bias spurious path → bias 增大），论文应 connect the dots。

**W11 [MINOR — R2] Abstract 信息过载——8+ 具体数字让读者难以抓住核心 message。**

**W12 [MINOR — R2] 引用格式：lee_wood_doughty2024 为 workshop paper 未标注；baumann2025/messing2026 为 arXiv preprints 状态未确认。**

---

## Reviewer Consensus

以下问题双方独立达成一致（标注 [AGREE]）：

1. **83.4% framing 的 overclaim 问题**是本文最大的 presentation 缺陷（R1-Q3 = R2-W1 CRITICAL）
2. **Theorem 1 DPI 论证不完整**（R1-W1 CRITICAL = R2 AGREE）
3. **三拓扑符号保持无解析证明 + Empirical Finding 术语误导**（R1-W2/W3 = R2-W2）
4. **λ(C) ∈ [0,1] 未证明**（R1-W2 = R2 AGREE）
5. **Non-differential assumption 讨论不足**（R1-W4 = R2-W5）
6. **FWL 不变性和 Exposure 符号翻转是 genuine contributions**（R1-S2/S3 = R2-S1/S2）
7. **实证验证规模充足，附录质量高**（R1-S5 = R2-S3/S5）
8. **Overall 3.5 Borderline Conference**

---

## Reviewer Divergence

| 问题 | R1 | R2 | 评估 |
|------|-----|-----|------|
| ASV 创新度 | REBUT: 技术差异实质性 | E-value 直接移植 | R1 论据更强——K×K→1D mapping + topology-dependent ranking 有实质区别 |
| 广度 vs 深度 | REBUT: 系统性是核心贡献 | Technical report 感 | 论文定位问题，非技术错误 |
| 拓扑先验假设 | MAJOR weakness | 通用 limitation，非本文特有 | R2 论据更强——但 Limitations 应提及 |
| SIMEX FWL 严格性 | 不够严格 | 结构性推论，无需额外形式化 | R2 论据更强——FWL 对 SIMEX 的推论是直接的 |

---

## Questions（需要作者澄清）

**Q1.** Abstract 中 83.4% 与 Section 4.3 "primary coefficient never reverses" 如何调和？是否考虑区分 primary/secondary coefficient 风险？

**Q2.** Theorem 1 的 V_B(δ) 单调性：C(δ) 线性插值族是否满足 stochastic degradation 条件？如果不满足，是否有不依赖 DPI 的替代证明路径？

**Q3.** 是否存在使 λ(C) ∉ [0,1] 的 confusion matrix？如果不存在，能否提供 sketch proof？

**Q4.** Empirical Finding 1 是否做过 adversarial search（而非仅 random sampling）寻找违反案例？

**Q5.** Non-differential misclassification 在哪些常见 NLP 标注任务中可能被违反？Stress test 是否覆盖了 structured（非 random）differential misclassification？

**Q6.** ASV linear interpolation C(δ) 在实际非线性错误退化模式下的鲁棒性？

**Q7.** DSL 对 M-bias 的 -267% RMSE 和 PPI++ 的 -88%——能否解释 protective topology 下"纠正 = 恢复 spurious bias"的机制？

**Q8.** Multi-LLM ensemble 标注时框架如何扩展？Kim et al. (2025) 发现的 60% 跨模型错误相关性如何影响 non-differential 假设？

---

## Missing References

以下引用由 R1/R2 共同或独立建议：

1. **Imai, Keele & Yamamoto (2010)** "Identification, Inference and Sensitivity Analysis for Causal Mediation Effects" — mediation 敏感性分析，与 ASV mediation 直接可比（R1 + R2）
2. **Buonaccorsi (2010)** "Measurement Error: Models, Methods, and Applications" — measurement error 标准教材（R1 + R2）
3. **Blackwell, Honaker & King (2017)** "A Unified Approach to Measurement Error and Missing Data" — 社会科学 measurement error 框架（R2）
4. **Valeri & VanderWeele (2012)** "Mediation Analysis Allowing for Exposure-Mediator Interactions" — mediator misclassification（R2）
5. **Pangakis, Wolken & Fasching (2023)** "Automated Annotation with Generative AI Requires Validation" — LLM 标注验证（R2）

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 本项目未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态：error。** 视觉审查 Agent 因 rate limit 错误退出（"You've hit your limit · resets May 23, 4pm UTC"），未能完成 PDF 渲染检查。用户可在限额重置后重新触发。

---

## Overall Assessment

**Overall: 3.5（Borderline Conference）**
**置信度: 4/5**

| ACL ARR 维度 | R1 | R2 | 综合 |
|-------------|-----|-----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Presentation | — | 3.5 | 3.5 |
| **Overall** | **3.5** | **3.5** | **3.5** |

**支持接收的理由：**
- 填补了 K≥3 标注误差 × 多因果拓扑的真实文献空白
- FWL 不变性和 exposure 符号翻转是 genuine novel contributions
- 实证验证规模充足（161 scenarios），theory-MC 一致性强
- 附录质量高，再现性好

**阻碍接收的理由：**
- Theorem 1 证明不完整——核心理论贡献的 soundness 受损
- 83.4% framing 与 "primary coefficient never reverses" 之间的 tension 是 integrity concern
- 三拓扑符号保持无解析证明，论文中 proved/verified/conjectured 层次不够清晰
- ASV 方法论新颖性有争议——系统性扩展 vs 方法论突破

**接收路径（→ 4.0 Conference）：**
1. 补全 Theorem 1 证明（直接路径，不依赖 DPI）或降格为 Conjecture
2. 修正 Abstract/Introduction framing：realistic 2.1% 与 83.4% 同等突出，明确区分 primary/secondary coefficient
3. 建立 Proved → Numerically verified → Conjectured 三级层次
4. 扩充 non-differential assumption 的 NLP 场景讨论
5. 补充 5 篇遗漏引用

**当前版本判断：** 介于 Conference 和 Findings 之间。如果 Theorem 1 证明问题和 framing 问题在 camera-ready 中解决，可达 Conference 水平。当前更偏向 Findings track。

---

## Detailed Comments（逐节）

### Abstract
- 信息过载：8+ 具体数字。建议保留 3-5 个核心数字。
- 83.4% 与 2.1% 的顺序和权重需调整——realistic regime 应先行。
- "prove sign preservation for confounding and collider, and verify it numerically for mediation, M-bias, and front-door" 的表述是准确的（已区分 prove/verify），但需确保 Introduction 保持同样清晰。

### Introduction
- Motivation → gap → contribution 逻辑链基本通顺。
- 第 2 段 "83.4% of K=3 confusion matrices cause sign reversal" 出现太早且太突出——读者尚无上下文判断 Dirichlet(1,1,1) 的实际意义。
- Contribution 3（correction guidance）的篇幅分配与其在主文中的深度不匹配。

### Related Work
- 覆盖面良好，三段结构清晰。
- 缺 5 篇引用（见 Missing References）。
- lee_wood_doughty2024 应标注为 workshop paper。

### Method (Section 3)
- Bias expressions 推导结构清晰。
- Proposition 1 条件 (a)(b) 的充分条件表述需更仔细——collider 条件 |τ| > √(Var(g)Var(h))/E[Var(T|A)] 在实践中是否常满足？
- "Empirical Finding 1" → 改为 "Numerical Finding 1"。
- ASV 的 C(δ) 参数化合理，δ_max 约束正确。但 linear interpolation 的局限性讨论可更深入。

### Experiments (Section 4)
- Theory-MC agreement（MAPE 2.0%）令人满意。IV 的 5.5% 需解释（论文已提及 Wald estimator variance amplification）。
- Table 1 和 Figure 2 是论文最有力的展示。
- Section 4.3 empirical validation 结构良好——"primary coefficient never reverses" 是重要发现但在 Abstract 中未体现。
- Correction guidance（Section 4.4）偏浅——5 种方法一段半，缺乏失败机制的深入解释。

### Conclusion & Limitations
- Limitations 覆盖了主要 concern（non-differential assumption, linear SEM, single annotator, K=3 derivations）。
- 应增加：拓扑误指定、outcome misclassification（已有但可强化）、开源 LLM only。
- 承诺代码公开——好。

### Appendix
- 质量高。证明基本完整（除 Theorem 1 的 DPI gap）。
- 反例构造（Proposition 6）严格。
- Bootstrap ASV、logistic DGP、cross-K robustness 增强可信度。
