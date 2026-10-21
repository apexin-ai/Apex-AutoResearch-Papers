---
round: 17
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-23T14:05:26.227104+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 17 审稿报告

**论文**: Multi-Class Annotation Errors in Causal Inference: Topology-Dependent Bias, Sensitivity, and Correction
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿轮次**: Round 17 (Fresh Mode)
**Reviewer 编排**: 2 人（R1: 方法严谨性 / R2: 新颖性与完整性）
**交叉审阅**: 完成（1 轮交叉后收敛）

---

## Summary

本文系统分析了 LLM 生成的 K-class（K≥3）标注误差在七种典型因果 DAG 拓扑下对因果估计的偏差传播。在线性 SEM 框架下推导了各拓扑的解析 bias 表达式，证明了 K≥3 混淆矩阵可以产生 sign reversal（K=2 时因代数约束不可能），提出 Annotation Sensitivity Values (ASV) 进行 topology-aware 敏感性分析，并证明 FWL 不变性使矩阵校正方法在四种 covariate 拓扑下可证明无效。验证覆盖 161 个场景（23 LLM 配置 × 7 拓扑），MAPE 1.6%。

---

## Strengths

1. **系统性贡献填补重要空白**：首次统一分析 multi-class annotation error 在 7 种 DAG 拓扑下的传播——先前工作仅覆盖 1-2 种拓扑且多限于 K=2。"First unified analysis" 声明经核查在当前文献范围内成立。[R1, R2 共识]

2. **K≥3 sign reversal 是非平凡理论发现**：证明了 K=2 的 toward-null 保证因代数约束在 K≥3 时被打破——83.4% Dirichlet(1,1,1) 矩阵在 exposure 下产生 sign reversal，但 primary coefficient 在所有测试配置中均未反转。这是论文最强的理论贡献。[R1, R2 共识]

3. **K=2 理论严谨**：Theorem 1 使用 perspective function convexity 证明 envelope monotonicity，手法巧妙且正确。Proposition 系列的拓扑特定 sign preservation 证明详尽。[R1]

4. **多层次验证充分**：(a) Theory-MC agreement 1.6% MAPE across 161 scenarios；(b) 100,000 Dirichlet 矩阵的 sign preservation 分析；(c) 23 empirical LLM confusion matrices（HumAID K=10, VAST K=3, CivilComments K=2）验证定性模式。[R1, R2 共识]

5. **ASV 三维分解有实用诊断价值**：magnitude / significance / sign-flip 三种 ASV 提供直观的 topology-dependent 风险评估，vulnerability ranking（IV 最脆弱 → M-bias 免疫）为研究设计提供可操作指导。[R1, R2 共识]

6. **FWL 不变性负面结果有重要价值**：代数证明四种 covariate 拓扑下矩阵校正方法在线性回归中可证明无效，引导实践者避免无效校正策略。[R1 证实 FWL 证明为 structural foundation，非纯经验发现]

7. **附录材料详尽（22页）**：完整证明、扩展实验、robustness checks、bootstrap CI 分析，reproducibility 表现优秀。[R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [format] Abstract 超过 EMNLP 2026 的 200 words 限制（约 245 words）
- R2 初审发现，R1 交叉审阅后从 minor 升级为 must-fix
- 超出 22.5%，构成实质性 desk reject 风险
- 当前 abstract 试图覆盖全部七种拓扑结果和多项数值发现，建议精简到 3-4 核心信息点
- **两位共识 must-fix**

**MF-2** [soundness] K≥3 理论缺口：Conjecture 1 的 ε-近似单调性是论文最大理论弱点
- Theorem 1 仅证明 K=2 envelope monotonicity
- Table 10 显示 **60-97% 的随机矩阵违反严格单调性**（confounding 90%, collider 97%, mediation 83%），worst-case deviation ≤0.013
- K=7 的 42 维参数空间中 10,000 采样覆盖率极低
- 仅在 default DGP 参数下验证，β/σ² 偏离后 conjecture 是否成立未知
- ASV vulnerability ranking 的可靠性直接依赖此单调性
- R1 列为 critical (must-fix)；R2 初审列为 should-fix，交叉后升级为 borderline must-fix
- **Director 采纳 must-fix**：论文标题聚焦 Multi-Class 但 K≥3 核心结论仅为 conjecture

### Should-Fix（影响评分但不一票否决）

**SF-1** [presentation] Correction Guidance 深度与"三大贡献"定位不匹配
- Section 4.5 仅约半页正文，Algorithm 1 仅在 Appendix p.30
- 五种方法选择标准、计算成本对比均缺失
- R2 列为 must-fix；R1 交叉 REBUT 降为 should-fix（实质内容存在于 Table 4 和 Appendix B.15/B.19）
- **Director 采纳 should-fix（高优先级）**：同意 R1——内容存在，问题在 presentation；但与端到端验证缺失联合看削弱第三贡献

**SF-2** [experiments] 缺乏端到端实证验证 pipeline
- 论文从未展示完整链条：C estimation → ASV diagnosis → Algorithm 1 routing → correction → improved estimates vs gold-label
- ClinicalBERT 案例仅覆盖 confounding 单一拓扑
- R1 列为 must-fix；R2 交叉 PARTIALLY AGREE 降为 should-fix——本文定位为 theoretical contribution，MC 验证是标准验证方式，ground-truth causal effects 在观察性数据中几乎不可获取
- **Director 采纳 should-fix（高优先级）**：理论贡献无需完整 pipeline，但建议至少展示一个拓扑的路由效果或降低 correction guidance 贡献定位

**SF-3** [novelty] ASV 相对于 E-values 的方法论创新论证不充分
- 核心数学操作（沿 C(δ) 计算 tipping point）是标准 sensitivity analysis 方法
- Remark 1 的三点区分主要是应用域差异和参数化差异，非方法论结构创新
- 拓扑分层能力（同一 C 在不同 DAG 下产生不同 ASV）是 E-value 框架无法自然实现的实质贡献——但论文未通过 worked example 展示
- **两位共识 should-fix**

**SF-4** [presentation] EMNLP 受众可达性偏低——计量经济学术语壁垒
- plim、FWL theorem、Wald estimator、column-stochastic、Birkhoff polytope、Dirichlet prior 对 NLP 读者壁垒过高
- 首次出现时缺乏 parenthetical 直觉解释
- Section 3.1 缺少 Intuition 段落用 NLP 例子建立直觉
- **两位共识 should-fix（高优先级）**

**SF-5** [scope] 线性 SEM 假设对 EMNLP 受众的适用性讨论不足
- NLP 因果推断最常用 logistic regression，bias 表达式在非线性模型下有效性未在主文检验
- 附录已有部分验证（Appendix B.2 FWL under logistic, B.7 robustness-to-nonlinear-DGP），但主文几乎未提及
- R1 列为 must-fix；R2 交叉降为 should-fix（验证材料已存在，问题在 presentation）
- **Director 采纳 should-fix**：已有验证材料，需在主文 Section 4 增加 3-4 句总结

**SF-6** [soundness] Proportional effects 假设 (f=λg) 的可验证性和适用范围
- Theorem 1 核心条件在实践中不可直接验证
- 论文未讨论 NLP 场景下何时合理、研究者如何判断
- Appendix B.13 检查了 OOB 随 departure from proportionality 的变化，但主文未提及
- **两位共识 should-fix**

**SF-7** [soundness] Non-differential misclassification 假设的 stress test 局限性
- NLP 文本中 Y 经常嵌入 A 的文本，LLM 可能隐性依赖 Y 信号
- Stress test 仅 5 个 VAST topics（≤29 per-topic samples），只检查 uniform perturbation
- 缺少 structured Y-dependent violation 的检验
- **两位共识 should-fix**

**SF-8** [soundness] Collider sign preservation 仅有经验验证
- Table 2 中 collider 标记为 "Empirical"，而 confounding 有代数证明
- Proposition 5 仅证明 proportional case，general case（Proposition 6）只给出 magnitude bound
- 削弱 Proposition 1 统一框架的严谨性
- R1 首提，R2 交叉 AGREE（初审遗漏）
- **两位共识 should-fix**

**SF-9** [presentation] "Sign reversal" 的 primary vs secondary coefficient 区分不清晰
- Abstract "secondary coefficients" 首次出现时未定义
- "Primary coefficient never reverses" 这一关键信息未出现在 abstract 中
- Section 4.2 中 "2.1% sign reversal" 易被误解为 primary treatment effect reversal
- **两位共识 should-fix**

### Minor Issues

1. Figure 2：7 子图在半页内拥挤，灰度打印下 red=sign reversal 难区分，建议使用 hatching pattern [R1, R2]
2. Table 1 "Cond." 列和 "Sign Flip" 列含义在 caption 中解释不够，应增加脚注 [R1, R2]
3. Algorithm 1 Step 2 "RMSE red. < 0.02" 阈值来源未说明 [R1]
4. 23 LLM 配置代表性有限（缺 GPT-4/Claude 等商业模型），但作为理论验证而非 benchmark 可接受 [R1, R2 near-consensus]
5. Bib 含 2 条未引用条目（dawid1979, rosenbaum2002），应引用或移除 [R2, R1 AGREE]
6. Appendix 22 页 vs 正文 8 页比例悬殊——虽不违规，但 Algorithm 1 和 Table 4 arguably 属于正文内容 [R2]

---

## Reviewer Consensus [AGREE]

1. **Abstract 超字数为格式硬伤**，需精简至 ≤200 words [MF-1]
2. **K≥3 Conjecture 1 是论文最大理论缺口**——ASV ranking 可靠性依赖于此 [MF-2]
3. **ASV 的拓扑分层能力是对 E-value 框架的实质扩展**，但论文未充分论证 [SF-3]
4. **术语密度对 EMNLP 读者壁垒过高**，需增加直觉解释 [SF-4]
5. **Proportional effects 和 non-differential 假设需更多讨论** [SF-6, SF-7]
6. **K≥3 sign reversal 是论文最强理论贡献** [Strengths]
7. **MC 验证 1.6% MAPE 充分可信** [Strengths]

---

## Reviewer Divergence [REBUT]

| 问题 | R1 | R2 | Director 裁定 |
|------|----|----|-------------|
| Correction Guidance | should-fix | must-fix | **should-fix（高优先级）**——内容存在，presentation 问题 |
| 端到端验证 | must-fix | should-fix | **should-fix（高优先级）**——理论贡献不要求完整 pipeline |
| 线性 SEM 讨论 | must-fix | should-fix | **should-fix**——附录已有验证，主文需引用 |
| Conjecture 1 严重性 | must-fix | borderline must-fix | **must-fix**——标题聚焦 Multi-Class 但 K≥3 仅为 conjecture |

---

## Questions（需作者澄清）

1. Conjecture 1 在非 default DGP 参数下（|β|>5 或接近 0）是否仍成立？是否有反例？
2. 如果将 linear SEM 替换为 logistic regression，bias 表达式的解析推导是否可能？还是只能依赖 MC？
3. Algorithm 1 要求研究者已知正确 DAG——对 NLP 新手是否构成使用门槛？
4. Gold labels 不可用时（LLM 标注的主要使用动机），框架推荐什么校正方法？MC-SIMEX 是否在所有拓扑下足够好？
5. Sign reversal 是否仅限于 secondary coefficients？Primary treatment coefficient 在 exposure 下是否永远安全？

---

## Missing References

**两位 Reviewer 建议补充：**
- Jurek et al. (2005) "Proper interpretation of non-differential misclassification effects" [R2, R1 AGREE]——与 "beyond toward-null" 核心主题直接相关
- Valeri & VanderWeele (2014) mediation measurement error [R2]——与 mediation topology 相关
- Stefanski & Carroll (1985) logistic regression measurement error [R1]——支撑 linear assumption 边界讨论
- Oster (2019) coefficient stability [R1]——与 ASV sensitivity 思路可比
- Tan et al. (2024) LLM annotation survey [R1]——补充 related work 覆盖度

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未启用**（项目配置 `external_review.paperreview_ai.enabled: false`）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已派发但异常退出（rate limit error）。未产生有效 findings。用户可选择重新触发。

---

## Overall Assessment

**Overall Score: 3.5 / 5 (Borderline Conference)**

**置信度: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 (交叉后从4降至3.5) | 3.5 |
| Excitement | 3 | 3 | 3 |
| Reproducibility | 4 | — | 4 |
| Overall | 3.5 | 3.5 | **3.5** |

**理由**：论文填补了 multi-class annotation error × 因果推断的系统性分析空白，K=2 理论严谨，K≥3 sign reversal 是非平凡发现，MC 验证充分。但存在两个关键弱点：(1) K≥3 核心结论仅为数值 conjecture，与论文标题和定位的理论严谨性预期不符；(2) 一个硬性格式违规（abstract 超字数）需在提交前修复。ASV 框架有实用价值但方法论创新边界需更清晰论证。Correction guidance 作为三大贡献之一深度不足（正文仅半页 + 缺端到端验证），需要调整贡献定位或补充内容。EMNLP 受众可达性需通过增加直觉解释来改善。

**修复后前景**：
- Abstract 超字数是低成本必修项
- K≥3 理论缺口是结构性问题，短期内无法通过简单修改解决——建议在正文中更诚实地标注为 open problem，明确 ASV ranking 在 ε≤0.013 近似下的稳定性
- Correction guidance 可通过 (a) 移入 Algorithm 1 + 扩充讨论或 (b) 降级贡献定位来解决
- 术语可达性和 logistic regression 讨论是低成本高回报修改

若 MF-1（abstract）和关键 SF 问题（SF-1, SF-4, SF-5）得到处理，论文有望从 3.5 提升至 4.0（Conference-level）。MF-2（K≥3 理论缺口）是结构性限制，需要管理预期而非消除。

---

## Detailed Comments

### Section 1 (Introduction)
- "first unified analysis of LLM-generated multi-class annotation error propagation across seven canonical DAG topologies in linear SEMs" 声明经核查成立，但 "unified" 主要指系统覆盖而非统一理论——各拓扑 bias expression 仍逐一推导 [R2]
- 三大贡献中 correction guidance 的深度需与实际内容匹配 [R1, R2]

### Section 3.1 (Setup and Notation)
- plim/FWL/Wald 首次出现时需 parenthetical 直觉解释 [R1, R2]
- "Notation conventions" 段落是有益的但不够——需为 NLP 读者增加 Intuition 小段落 [R2]
- Non-differential misclassification (Definition 1)："LLM 分类时不观察 Y" 辩护在 Y 嵌入文本时可能不成立 [R1]

### Section 3.2 (Bias Expressions)
- Proposition 1 将 confounding（proved）和 collider（empirical）并列，可能给读者造成同等严谨性印象——应明确区分 [R1, R2]
- "Numerical Verification 2: Primary coefficient preservation" 是重要发现但仅为经验事实，abstract 中的表述应一致 [R2]

### Section 3.3 (ASV)
- Theorem 1 (K=2) 证明严谨 [R1]
- Conjecture 1 (K≥3)：10,000 矩阵在高维空间覆盖率极低；建议弱化为 "Empirical Observation" 或至少明确标注 DGP 依赖性 [R1]
- Remark 1 的 ASV vs E-value 区分需增加 worked example 展示拓扑分层的实质差异 [R1, R2]

### Section 4 (Experiments)
- Theory-MC agreement 1.6% MAPE 充分 [R1, R2]
- Section 4.2 sign reversal 结果中 primary vs secondary coefficient 区分需更清晰 [R1, R2]
- Section 4.4 empirical validation 使用真实 LLM CM 有说服力，F1-bias 无相关性（ρ=-0.10, p=0.45）是有力结果 [R2]
- Section 4.5 需扩充或降级贡献定位 [R1, R2]
- 建议增加 3-4 句总结 Appendix B.2/B.7 的 logistic regression 验证结果 [R2]

### Limitations
- 当前覆盖范围合适（non-differential assumption, linear SEMs, C known/estimable, end-to-end as future work）
- 建议增加 proportional effects 假设的讨论 [R1]