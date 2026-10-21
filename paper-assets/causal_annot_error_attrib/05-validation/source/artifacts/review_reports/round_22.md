---
round: 22
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-24T01:47:23.104055+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 22 (Fresh Review)

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 via ACL Rolling Review (Long Paper)
**审稿模式**: Fresh（重新审稿，无历史记忆）
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+理论/实验验证; R2: 新颖性+完整性+相关工作）
**轮次**: 1 轮（关键问题达成共识，无需第 2 轮）

---

## Summary

论文研究 LLM 多类标注误差（K≥3 non-differential misclassification）在因果推断中沿 7 种 DAG 拓扑的传播行为。三个核心贡献：(1) 多类偏差分类法，证明 5 种拓扑保持符号、exposure 和 IV 可反转；(2) Annotation Sensitivity Values (ASV)，提供拓扑依赖的脆弱性排序；(3) 拓扑感知校正路由，证明 FWL 不变性使 4 种拓扑的矩阵校正无效。工作量大、技术正确、验证充分，但核心理论贡献仅覆盖 K=2 和 K=3 对称情形，一般 K≥3 依赖未证明的猜想，且三个强假设（非差异误分类、线性 SEM、proportional effects）的联合约束限制了 NLP 场景下的实际适用性。

---

## Strengths

**S1** [强共识] **问题定义精准且时效性强。** LLM 标注在 NLP 因果推断中快速增长（Gilardi et al. 2023, Ziems et al. 2024），但标注误差的因果后果缺乏系统研究。论文填补了这一空白。

**S2** [强共识] **拓扑分类法（Table 1）是原创且高价值的贡献。** 将 7 种 DAG 拓扑的偏差行为系统分类，揭示 topology-dependent vulnerability 全景图。这是超越 Hernán & Cole (2009) 二分类框架的有意义扩展。实践者可根据自己的 DAG 快速判断误分类风险等级。

**S3** [强共识] **FWL 不变性是论文最有实践冲击力的发现。** 证明 matrix-based corrections（MLA, DSL, MC-SIMEX）对 4 个 covariate 拓扑无效——直接挑战了"有混淆矩阵就能修正"的朴素直觉。这是一个反直觉且重要的负面结果，对实践者有明确行动指导价值。

**S4** [强共识] **数值验证规模令人印象深刻。** 100,000 Dirichlet 矩阵、545,945 adversarial 矩阵、23 empirical LLM 配置、bootstrap convergence、cross-K robustness——验证的广度和深度在同类论文中少见。

**S5** [强共识] **K=2 证明严格完整。** Theorem 1 + Propositions 1-6 覆盖全部 7 拓扑在 K=2 下的符号保持条件，附录证明逻辑清晰、步骤完整。

**S6** [共识] **Appendix 组织和完整性。** 27 页附录覆盖从完整证明到 DGP 敏感性、非线性模型验证、stress test 等，显示对潜在质疑的预判和回应能力。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [强共识, critical] **K≥3 一般情形仅有猜想，ASV 核心性质未证明。**

Theorem 1（envelope monotonicity）仅对 K=2 成立；Theorem 2 要求对称混淆矩阵，但论文自身的 Remark 4 承认 VAST 实际混淆矩阵的 Frobenius distance d_rel = 0.30–0.38，远非对称；一般 K≥3 的 envelope monotonicity 仅有 Conjecture 1（100,000 矩阵数值验证，最大违反 ε < 0.017）。对于以 "Multi-Class" 为核心卖点的论文，K=2 已有成熟文献（Brenner 1993, Hernán & Cole 2009），真正的增量贡献在 K≥3，但该部分停留在猜想阶段。

补充：(1) adversarial testing 的 4 种结构族是否覆盖 worst case 不清楚；(2) ε=0.017 在因果推断中的实际含义未讨论——如果真实效应量很小（τ ≈ 0.05），0.017 的违反可能影响 ASV ranking。

*注：R2 在交叉回应中澄清了一个重要区分——sign preservation（Proposition 1）已被证明覆盖一般 K（under proportional effects），未证明的是 envelope monotonicity。论文正文对这一区分不够清晰。*

**MF-2** [强共识, critical] **非差异误分类假设在 NLP 场景中过强且脆弱。**

Definition 1 假设 P(A*|A) 不依赖 Y 和 Z，但 LLM 注释器的错误模式高度上下文依赖（情感分类器对中性文本误判率更高；stance detection 对模糊立场质量更差；in-context learning 使误差与 prompt 示例相关）。论文自身的 Appendix B.6 stress test 确认了假设的脆弱性（sign-flip 率在 ε=0.20 时达 13.9%）。Appendix B.26 的 Y-stratified 检验仅拒绝 1/12 配置，但未报告统计功效——低功效下"不拒绝"不等于"假设成立"。

如果非差异假设不成立，5 个拓扑的符号保持保证不再适用，论文的核心实践价值大幅下降。论文目前不提供差异误分类下的退化保证。

**MF-3** [共识, critical] **相对于测量误差文献的增量创新有限。**

误分类效应因 DAG 拓扑而异的基本洞察在 Carroll et al. (2006)、Brenner (1993)、Buonaccorsi (2010) 中已有充分讨论。技术手段（混淆矩阵乘积、FWL 分解）是标准工具。论文声称的 "first systematic analysis" 在 "K≥2 × 7 topologies × linear SEM" 这个特定组合上成立，但更多是覆盖度贡献而非方法论创新。R1 补充：FWL invariance 结果和 ASV 定量化是非平凡增量，但不足以构成 EMNLP 主会要求的 "exciting" 贡献。

当前形态适合 Findings 接收，进主会需要更强的 K≥3 质变论证或 Conjecture 1 被证明。

### Should-Fix（影响评分但不一票否决）

**SF-1** [强共识] **Proportional effects 假设的 NLP 适用性讨论严重缺失。** Theorem 1 对 confounding 拓扑要求 proportional effects。Non-proportional sparse DGP 的符号保持违反率达 24.2%（Appendix B.17），但正文对此数据的呈现不足。论文未讨论在实际 NLP 因果研究中 proportional effects 何时合理。（注：R2 澄清 in-assumption verification 不构成"循环论证"，但实践相关性讨论确实缺失。）

**SF-2** [强共识] **端到端验证不够真实。** Section 4.4 使用真实混淆矩阵但合成 DGP（semi-synthetic）。缺少从头到尾使用真实数据（真实注释、真实因果问题、真实 outcome）的验证。（R2 承认获取此类数据很困难，建议作为 limitation 明确说明。）

**SF-3** [共识] **线性 SEM 假设限制实际适用性。** NLP 因果推断越来越多使用非参数方法（matching, doubly-robust estimators）。偏差公式在这些模型下是否成立是开放问题。Appendix B.14 仅验证了 logistic 下的 FWL 不变性，未验证偏差公式本身。

**SF-4** [共识] **ASV 的 gold-label "鸡生蛋" 问题。** ASV 和 PPI++ 都需要 gold labels 估计 C₀。Bootstrap 收敛分析（Appendix B.8）需 ~500 gold labels，但极少 gold labels（50-100 samples）时 ASV 估计的可靠性未讨论。

**SF-5** [共识] **Algorithm 1 阈值缺乏形式化依据。** 决策阈值从 Monte Carlo 经验选取，未讨论对 DGP 参数变化的敏感度和泛化性。

**SF-6** [共识] **"provably" 在 abstract/正文中使用隐含三个强假设。** 建议附注条件或改为 "under [assumptions], we prove that..."。

**SF-7** [共识] **K=2 sign reversal 叙事过于简化。** "Absent in the binary case" 未限定到 confounding/mediation，exposure topology 在对角元素 <0.5 时也可 sign reversal。建议修改为限定表述。

### Minor（不影响接收）

- Figure 2 各拓扑 y 轴量级差异大，建议统一 scale 或加 median 标线
- C/C₀/C(δ) 三者区分首次引入时不够清晰，建议 notation table
- Remark 4（VAST d_rel=0.30-0.38）与正文脱节，应在正文提及 Theorem 2 对称假设的实证局限
- Abstract 数字密度高（10+ 具体数字），核心信息被稀释（R1 部分反驳：具体数字符合 *ACL 规范）
- Section 3.3 列了三个 sensitivity analysis 参照物但只详细比较了 E-values
- "LLM" 术语范围：ClinicalBERT 等 task-specific classifiers 非严格 LLM
- Section 4.4 semi-real case study 描述过于简略

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成强共识 [AGREE]：

1. **Conjecture 1 未证明是核心理论缺口**——削弱 ASV 作为诊断工具的可靠性
2. **非差异误分类假设在 NLP 中过强**——论文自身的 stress test 确认了假设脆弱性
3. **端到端验证不够真实**——缺少使用真实因果数据的完整验证
4. **总体评分 3.5 (Borderline Conference)**——适合 Findings 但进主会需更强论证
5. **Table 1 taxonomy 和 FWL invariance 是论文最有价值的贡献**
6. **K=2 证明严格完整**，数值验证规模令人印象深刻

---

## Reviewer Divergence

1. **PPI++ 贡献度**: R2 认为仅是 Angelopoulos et al. (2023) 的应用，不应作为独立 contribution；R1 反驳——FWL 负面结果 + topology-aware decision procedure 超越单纯应用。**Director 判断**: R1 论据更有说服力，FWL futility 是独立贡献。

2. **Venue 适配度**: R2 认为偏统计/计量论文在 EMNLP 受众有限，类似论文通常发 TACL；R1 反驳——NLP 动机核心，先例充分（Keith et al. 2020 ACL, Feder et al. 2022 TACL），Findings 明确接受。**Director 判断**: 不构成拒稿理由。

3. **Abstract 数字密度**: R2 认为堆砌稀释主信息；R1 认为具体数字使 claims 可验证，符合 *ACL 规范。**Director 判断**: 可精简但非关键问题。

---

## Questions

1. Conjecture 1 最大违反值 0.017——在因果推断中（尤其效应量小时），这对 ASV ranking 决策的实际影响有多大？能否给出"可接受违反阈值"的理论或实践论证？
2. 非差异误分类假设不成立时，论文框架是否提供任何退化保证（degradation guarantee）？或者完全失效？
3. Non-proportional sparse DGP 的 24.2% 符号保持违反率——在实际 NLP 因果研究中（如 sentiment → policy outcome），treatment effects 更可能是 proportional 还是 non-proportional？
4. Gold-label budget 极少时（50-100 samples），ASV 估计的方差和偏差如何？Appendix B.8 的起步 N*=6,000 是否反映了实际需求？
5. Algorithm 1 中将 PPI++ 替换为 MC-SIMEX（不需要 gold labels），correction performance 退化幅度和拓扑差异如何？

---

## Missing References

**确认缺失（双方共识）：**
- Mahajan (2006) "Identification and estimation of regression models with misclassification" — 多值误分类非参数识别
- Hu (2008) "Identification and estimation of nonlinear models with misclassification" — 非线性模型误分类
- Cornfield et al. (1959) — sensitivity analysis 奠基性工作
- Törnberg (2024) "ChatGPT-4 Outperforms Experts..." — LLM 注释质量实证

**R1 提出但已引用（R2 核实确认）：**
- Kuroki & Pearl (2014) — 已引用 p10
- Shu & Yi (2019a) — 已引用 p11
- Lash et al. (2009) — 已引用 p10
- Gustafson (2003/2004) — 已引用 p10

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已派发但执行超时（300s）。未产出有效 findings。用户可选择重新触发。

---

## Overall Assessment

**评分: 3.5 / 5 — Borderline Conference**
**置信度: 4/5**

**评分理由：**

论文解决了一个重要且时效性强的问题（LLM 多类标注误差在因果推断中的传播），提供了有价值的实用工具（Table 1 taxonomy, ASV diagnostics, FWL futility result）。技术执行扎实，K=2 证明严格完整，数值验证规模令人印象深刻。

然而，三个结构性问题限制了论文的评分：(1) 核心理论贡献仅覆盖 K=2 和 K=3 对称，一般 K≥3 依赖未证明的 Conjecture 1——对于以 "Multi-Class" 为卖点的论文，这是重要的理论缺口；(2) 非差异误分类假设在 NLP 场景中几乎必然被违反，论文不提供退化保证；(3) 相对于测量误差文献的方法论创新有限，更多是"系统性覆盖+实用工具"型贡献。

**定位判断：** 当前形态适合 **Findings 接收**（3.0-3.5 区间），贡献清晰但进主会需要更强的理论支撑或实践验证。如果作者能 (a) 证明 Conjecture 1 或提供更紧的理论界，(b) 提供差异误分类下的退化分析，(c) 更充分论证 K≥3 相对于 K=2 的质变性质，则有望提升至 4.0（Conference 接收）。

---

## Detailed Comments

### Section 1 (Introduction)
- "first systematic analysis that jointly addresses" (p2) — 在 "K≥2 × 7 topologies × linear SEM" 组合上成立，但应更谨慎定位相对于 Carroll et al. (2006), Buonaccorsi (2010) 的增量
- Contribution 3 的措辞建议从 "PPI++ correction" 调整为 "topology-aware correction guidance including FWL futility result"
- "absent in the binary case" 应限定为 "for confounding and mediation topologies where K=2 guarantees attenuation"

### Section 3.1 (Non-differential Misclassification)
- Definition 1 后应在正文充分讨论该假设在 NLP 中何时合理、何时不合理（给出具体 NLP 任务例子）
- 应引用 Appendix B.6 stress test 的关键结果（至少一段摘要）
- Y-stratified 检验（B.26）应报告统计功效

### Section 3.2 (Bias Expressions)
- 应明确区分 "sign preservation (proved for general K under proportional effects, Proposition 1)" 和 "envelope monotonicity (proved for K=2 Theorem 1, K=3 symmetric Theorem 2, conjectured for general K≥3)"
- Non-proportional sparse DGP 的 24.2% 违反率应在正文呈现或至少提及

### Section 3.3 (ASV)
- "analogous to E-values" 的措辞削弱新颖性，建议更明确地论证 ASV 的差异化（topology-specific, multi-class specific）
- 应讨论 Conjecture 1 的 0.017 违反在因果推断实践中的含义（与效应量的相对大小）
- Gold-label budget 约束应在此处讨论

### Section 4 (Experiments)
- Section 4.4 semi-real case study 需更多细节（baseline RMSE、improvement 的绝对值）
- 建议增加一个真正使用真实因果数据的端到端验证（或在 Limitations 中明确说明缺失原因）

### Limitations
- Proportional effects 何时在 NLP 中合理的讨论应更具体
- 应明确线性 SEM 在非参数方法下的局限

### Format Compliance
| 项目 | 状态 |
|------|------|
| 正文 ≤8 页 | ✅ |
| Abstract ≤200 words | ✅ (~170 words) |
| Double-blind 匿名 | ✅ |
| Limitations section | ✅ |
| ACL style template | ✅ |
| AI 使用披露 | ✅ (Appendix D) |