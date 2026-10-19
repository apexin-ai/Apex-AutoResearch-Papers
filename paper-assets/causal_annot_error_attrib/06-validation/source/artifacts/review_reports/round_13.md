---
round: 13
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-23T09:45:59.025433+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Multi-Class Annotation Errors in Causal Inference

**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿轮次**: Round 13 (Fresh Review)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验验证; R2: 新颖性+完整性+表达）

---

## Summary

本文系统分析了 K 类 LLM 标注错误在线性 SEM 下沿七种经典 DAG 拓扑（confounding, exposure, mediation, collider, M-bias, front-door, IV）传播至因果效应估计的机制。主要贡献包括：(1) 七种拓扑的闭式偏差表达式，证明 K≥3 引入结构性符号反转可能（二分类不会出现）；(2) Annotation Sensitivity Values (ASVs) 敏感性框架，揭示从 IV（最脆弱）到 M-bias（免疫）的拓扑脆弱性谱；(3) 五种校正方法的拓扑感知评估，证明 FWL 不变性使矩阵校正对四种协变量拓扑无效。经验验证覆盖 23 个 LLM 配置、3 个 NLP 数据集、161 个场景。

## Strengths

**S1. 七种 DAG 拓扑的统一分析框架具有真正的新颖性（R1-S1, R2-S1 共识）。** 先前工作要么覆盖单一拓扑（Brenner 1993 多类混杂；Lee & Wood-Doughty 2024 LLM+confounding），要么限于二元错分类（Teblunthuis 2024，四种 DAG）。本文首次跨七种拓扑进行统一分析，揭示了跨拓扑模式（符号保持层级、ASV 谱），这在单拓扑研究中不可见。"first unified analysis across seven topologies" 的声称经两位 Reviewer 独立确认有事实支撑。

**S2. 诚实的三级理论层级体系（R1-S2）。** 将理论贡献明确区分为"解析证明"（Proposition 1: confounding/collider sign preservation, Theorem 1: K=2 monotonicity）、"数值验证"（Observation 1: 20,000 triples/topology）和"ε-近似猜想"（Conjecture 1），避免了过度宣称。这一透明度是方法论美德。

**S3. K≥3 符号反转发现（R2-S2, R1-S6）。** 通过 Proposition 1(c) 的构造性反例和 100,000 Dirichlet 矩阵验证，清晰展示了多类误分类与二类误分类的本质差异。对使用多类 LLM 分类器的 NLP 因果推断实践者有直接相关性。

**S4. FWL 不变性洞见（R1-S3）。** 证明矩阵校正方法对四种协变量拓扑无效是一个有实践价值的负面结果。R2 认为这是 FWL 定理的"直接推论"，R1 强力反驳：识别 FWL 在误分类校正语境下的含义需要结合列空间性质，并非 trivially obvious。Director 采纳 R1 观点——该洞见具有独立贡献价值。

**S5. 实验验证规模充分且透明（R1-S4, R2-S3）。** 100,000 Dirichlet 矩阵 × 7 拓扑，MAPE 1.6%（161 scenarios）。跨 K 稳健性检验覆盖 K=3,5,7,10。Algorithm 1 和 ASV 框架提供可操作的实践指导（R1-S5, R2-S4）。

**S6. 附录极为详尽（R2-S5）。** 22 页附录覆盖完整证明和 10+ 项鲁棒性检验，展现高度学术严谨性。

## Weaknesses

### Must-Fix

**M1. [must-fix] EMNLP 受众的可达性障碍（R2-W1, R1 AGREE）。**
论文大量使用计量经济学/流行病学术语而面向 NLP 读者的解释不足：
- "plim" 从 Section 3.2 起贯穿全文，仅在 p4 脚注中一句话定义——这是改善但仍不充分（R12 已添加脚注，但 R13 两位 Reviewer 均认为需要更深入的直觉解释）
- FWL 定理是贡献 3 的核心，但分解全在 Appendix A.2；正文首次出现时缺乏直觉解释
- Equation (1) 的残差化概念对不熟悉 OLS 投影的读者不透明
- Notation Table (Table 18, p30) 应更早交叉引用
- **建议**：Section 3.1 开头加 1-2 段直觉性文字，解释 plim、FWL 分解、残差化的含义和动机；Table 18 前置或引用

R1 建议降为 should-fix（认为是写作改进而非方法论问题）。Director 维持 must-fix：EMNLP 是 NLP 会议，读者可达性直接影响论文的 venue fit 和 impact。

**M2. [must-fix] IV sign reversal 表述在论文内部存在 factual 不一致（R1-W3, R2 AGREE 并升级）。**
三处关键表述相互矛盾：
1. **Abstract (p1)**: "no sign reversal occurs for all other topologies including IV"
2. **Section 4.2 (p7)**: "diagonal dominance C₀ > 0.8 reduces but does not eliminate sign reversal risk"
3. **Appendix B.4 (p23)**: "diagonal dominance prevents this crossing"

(2) 说 "does not eliminate"，(3) 说 "prevents"——直接矛盾。Abstract 与 Section 4.2 也矛盾。数值事实本身可能是一致的（真实 LLM 矩阵下 138 个非 exposure 场景中 0 次 sign reversal），但措辞必须统一。需明确区分 "violation（偏差存在）" 和 "sign reversal（符号反转）"，并定义 "realistic accuracy" 的操作边界。

### Should-Fix

**S1. [should-fix] Conjecture 1（K≥3 包络单调性）未被证明，Abstract 呈现不够突出（R1-W1, R2-W2 共识）。**
核心拓扑排序在 K≥3 下依赖 Conjecture 1（ε < 0.06 近似单调性），仅有 210,000 矩阵的数值验证（Appendix B.12）。K=2 证明使用 perspective function 凸性，K≥3 因 V₀(δ) 从标量变为矩阵值函数而无法推广（Appendix A.4 已解释）。

R2 评 must-fix，R1 REBUT：核心贡献是偏差表达式（Eq.1-2, 解析推导）和 sign preservation（Propositions 1-6, 一般 K 的解析证明），非 Conjecture 1。Director 采纳 R1——Conjecture 1 仅支撑 ASV monotonicity 排序，不构成论文核心理论基础。经验证据（Table 3, 161 scenarios）独立验证了拓扑排序。

**建议**：(1) Abstract 明确区分 "K=2 formal guarantees" 和 "K≥3 numerical evidence"；(2) 降低 "vulnerability spectrum" 的声称强度为 "approximate ranking supported by extensive numerical evidence"。

**S2. [should-fix] ASV 与 E-value/partial R² 的形式化比较不足（R2-W3, R1 AGREE）。**
Section 3.3 的 ASV-vs-E-value 对比已有改善（R12 修复），但仍缺乏形式化深度：
- Magnitude ASV 与 E-value 结构高度相似（均提供"结论翻转所需最小扰动阈值"），未展示数学差异
- Sign-flip ASV "has no E-value counterpart" 未解释结构性原因（R1 补充：E-value 度量连续标量的混杂强度，Sign-flip ASV 度量离散矩阵到符号反转边界的距离——数学结构不同）
- 与 Cinelli & Hazlett (2020) partial R² 框架无形式化对比
- **建议**：添加对比表，形式化展示 ASV/E-value/robustness value 在参数空间、敏感性路径、适用场景上的异同

**S3. [should-fix] Proportional effects 假设失败率（15-17%）在正文中讨论不足（R1-W2, R2 AGREE）。**
Appendix B.17 Table 16 报告 proportional effects 在真实 LLM 矩阵下违反率 15-17%（Sparse DGP 高达 24.2%）。当 f≠λg 时，论文退回 Proposition 3（一般情形），其条件 |τ| > B 在实践中通常不可知。R2 补充建议：给出综合 "coverage analysis"——在多少比例的现实 LLM 配置中，至少有一组理论保证成立。
- **建议**：正文中更直接地讨论失败率的实践含义和退化路径

**S4. [should-fix] Section 4.5 FWL invariance 的适用范围限定不够精确（R1-W4 经 R2 修正后）。**
R1 引用 Appendix B.14 Table 13 称 exposure 在 logistic 下有 22-78% 偏差缩减，暗示 FWL invariance 不成立。R2 正确指出：FWL invariance 仅 claim 协变量拓扑（confounding, mediation, collider, M-bias），exposure 不在 claim 范围内（A 是 treatment 而非 covariate）。Table 13 对协变量拓扑的 logistic bias reduction 均为 ~0.003%——确实 negligible。

但正文 Section 4.5 的表述（"FWL invariance holds under linear OLS and approximately under logistic regression"）可能误导读者以为 FWL invariance 覆盖所有拓扑。
- **建议**：明确添加 "FWL invariance applies to covariate topologies only; exposure is excluded because A enters as treatment, not covariate"

### Minor

**m1. [minor] Abstract 信息密度（R2-W4, R1 REBUT）。** R2 认为 7+ 个独立数字造成认知超载，R1 反驳精确定量是好的实践。分歧保留——属风格偏好。

**m2. [minor] 部分拓扑缺少 NLP 场景示例（R2-W5, R1 部分 AGREE）。** M-bias、front-door、IV 未给出 NLP 应用实例。R1 指出这是通用因果推断框架，不限于 NLP。建议为 M-bias/front-door 各加 1-2 句 NLP 场景描述。

**m3. [minor] 商业 LLM 验证缺失（R1-W5, R2 REBUT）。** R2 成功论证：理论结论仅依赖混淆矩阵数学性质（column-stochastic, diagonal dominance），不依赖 LLM 架构。23 个配置已覆盖 7B-235B 参数范围。Limitations 已承认此局限。

**m4. [minor] Non-differential 假设讨论（R2-W7, R1 AGREE minor）。** Section 3.1 已识别成立条件和 stress test（Appendix B.6）。历轮改善显著。

**m5. [minor] DAG 未知时的讨论（R2-W8, R1 AGREE minor）。** 标准因果推断假设，建议 1-2 句讨论应对策略即可。

**m6. [minor] PPI++ 在 M-bias 下有害 (-88%) 缺乏机制解释（R2-Q4, R1 AGREE）。** 可能原因：M-bias 误分类是保护性的，PPI++ 移除保护性衰减，放大偏差。应在正文说明。

**m7. [minor] Conjecture 1 高维覆盖不足（R1-W6, R2 部分 AGREE）。** K=7 每拓扑仅 10,000 样本，42 自由参数空间稀疏。建议增加采样量或做 power analysis。

**m8. [minor] 各项 minor issues（R1-MI1-4, R2-MI1-6）。** Table 1 caption 说明不足、Footnote 1 计算基准不清晰、"Numerical Verification 1/2" 未正式定义、"annotation error" 与 "misclassification" 交替使用未声明同义、Figure 3 y 轴标签不精确。

## Reviewer Consensus

两位 Reviewer 在以下关键判断上达成共识：

1. **[AGREE] 七拓扑统一分析的新颖性成立**（R1-S1, R2-S1）。
2. **[AGREE] 三级理论层级体系（proved/verified/conjectured）是透明的方法论美德**（R1-S2, R2 交叉确认）。
3. **[AGREE] IV sign reversal 表述存在必须修复的 factual 不一致**（R1-W3, R2 升级为 must-fix）。
4. **[AGREE] EMNLP 可达性需要改善**（R2-W1, R1 AGREE 实质但建议降级）。
5. **[AGREE] ASV vs E-value 形式化对比不足**（R2-W3, R1 AGREE）。
6. **[AGREE] Proportional effects 15-17% 失败率需更充分讨论**（R1-W2, R2 AGREE）。
7. **[AGREE] K≥3 理论限制应在 Abstract 更突出呈现**（R1-W1, R2-W2）。

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | Director 裁决 |
|------|---------|---------|--------------|
| Conjecture 1 严重性 | should-fix（偏差表达式才是核心） | must-fix（核心排序依赖猜想） | **R1**——核心贡献是 bias expressions + sign preservation，Conjecture 1 仅支撑 ASV monotonicity |
| Abstract 信息密度 | REBUT（精确定量是好实践） | should-fix（认知超载） | **保留分歧**——属风格偏好 |
| FWL 贡献定位 | REBUT（非平凡洞见） | should-fix（直接推论） | **R1**——识别 FWL 在误分类校正中的含义需结合列空间性质 |
| 商业 LLM | should-fix | REBUT（理论不依赖架构） | **R2**——降为 minor |
| Logistic regression + FWL | should-fix（exposure 结果远非 negligible） | REBUT（FWL 不 claim 覆盖 exposure） | **R2 纠正了逻辑错位**，但 R1 对 Section 4.5 措辞模糊的关切有效 → should-fix 限于措辞精确化 |

## Questions

**Q1.** IV sign reversal 三处表述（Abstract/Section 4.2/Appendix B.4）中哪个是正确的？"realistic accuracy" 的操作定义是什么？（R1-Q2, R2 AGREE — must address）

**Q2.** Proportional effects 15-17% 失败率是否与特定模型类型或 K 值相关？失败时偏差的实际幅度是什么量级？（R1-Q1, R2 AGREE）

**Q3.** M-bias 的 Sign-flip ASV = ∞ 是否可被解析证明？目前仅有数值验证。（R2-Q3, R1 AGREE — 加强论文的方向）

**Q4.** Algorithm 1 的 δ* 阈值选择敏感性如何？不同阈值是否改变拓扑排序？（R1-Q4, R2 AGREE）

**Q5.** Logistic 回归下 Algorithm 1 对 exposure 的推荐是否仍有效？（R1-Q3, R2 重新框定）

**Q6.** PPI++ 在 M-bias 下 RMSE 增大 88% 的机制是什么？（R2-Q4, R1 AGREE）

**Q7.** F1-bias null result (ρ=-0.10, p=0.45, n=56) 的统计功效？R1 部分 REBUT：Fig 3 的论点不是 ρ=0 而是"F1 不是 reliable proxy"，图的定性模式（同 F1 不同拓扑偏差差 10×）已足够支撑。但报告 CI 或 power 是合理改进。

## Missing References

**共识缺失（R2 提出, R1 AGREE）**:
- Imai, Keele & Tingley (2010), "A General Approach to Causal Mediation Analysis" — mediation 分析基础框架
- Roberts, Stewart & Tingley (2020) 或 Pryzant et al. (2021) — text-based causal inference

**分歧**:
- Veitch, Wang & Blei (2020) — R2 提出, R1 REBUT（研究问题不同：text-as-treatment/confounder vs. 标注误差传播）。Director 不强制引用。

R1 未发现显著遗漏，认为文献覆盖在测量误差理论、LLM 标注、PPI、敏感性分析方面均较充分。

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目配置未启用外部审稿。

## Visual Layout Check（非评分项）

**状态：错误。** 视觉审查 Agent 因限额问题退出（"You've hit your limit · resets 4pm (UTC)"）。未产生排版审查结果。用户可在限额重置后重新触发。

**手动页面检查**（Director 基于 PDF 阅读）：
- Section 5 (Conclusion) 在 page 8 内结束 ✓
- Limitations 从 page 9 顶部开始，不计入页数 ✓
- References 从 page 9 开始 ✓
- 正文符合 EMNLP 2026 的 8 页限制 ✓
- 匿名：作者署名为 "Anonymous" ✓
- 模板：`\usepackage[review]{acl}` ✓

## Overall Assessment

**Score: 3.5 (Borderline Conference)**

**Confidence: High**（两位 Reviewer 独立评分一致，交叉分享后核心判断收敛）

**官方维度打分综合：**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 3.0 | 3.25 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

**总评**：论文在测量误差×因果推断的交叉领域做出了系统性贡献：七拓扑统一分析的新颖性经两位 Reviewer 确认成立；K≥3 符号反转发现有理论和实践价值；FWL 不变性洞见具有独立贡献（R1 成功论证其非平凡性）；实验验证规模充分。

但存在两个 must-fix：(1) EMNLP 受众的术语可达性不足——plim/FWL 的直觉解释仍需深化；(2) IV sign reversal 在 Abstract/Section 4.2/Appendix B.4 之间的 factual 不一致必须修复。此外，ASV vs E-value 形式化对比不足、proportional effects 失败率正文讨论不充分、K≥3 理论限制在 Abstract 中呈现不够突出，均为 should-fix。

论文处于主会议接收的边界线上。如修订能解决上述 must-fix 并改善 should-fix 项，可上调至 Conference (4.0)。当前版本更适合 Findings。

## Detailed Comments

### Section 1 (Introduction)
- 叙事结构清晰，三个贡献准确反映论文内容。
- "first unified analysis across seven topologies, building on prior single-topology analyses" 的措辞准确有事实支撑（R1 交叉回应确认）。
- 建议：明确区分 K=2 formal guarantees 和 K≥3 numerical evidence 的理论层级。

### Section 2 (Related Work)
- 覆盖面广泛（测量误差、LLM 标注、敏感性分析、校正方法），两位 Reviewer 均认为较充分。
- 建议补充：Imai et al. (2010) 因果中介分析基础框架；1-2 篇 text-based causal inference 文献。

### Section 3 (Method)
- **3.1**: plim 脚注已添加（R12 修复），但需进一步加直觉段落（1-2 段解释 plim/FWL/残差化的含义和动机）。Table 18 应在此处交叉引用。
- **3.2**: Bias expressions (Eq.1-2) 推导正确，R1 未发现错误。Exposure 的 w_{jk} 权重机制解释清晰（R1-S6）。但 Section 4.2 中 IV sign reversal 的措辞与 Appendix B.4 矛盾，必须修复。
- **3.3**: ASV 框架定义清晰。Theorem 1 (K=2 monotonicity) 证明严谨。ASV-vs-E-value 对比已有改善（R12 添加），但需更深入的形式化展示。

### Section 4 (Experiments)
- **4.1-4.2**: Monte Carlo 验证设计合理，MAPE 1.6% 可接受。Table 1 和 Figure 2 有效支撑 bias taxonomy。IV sign reversal 表述需统一。
- **4.3**: ASV 验证充分。Bootstrap CI 方法合理。
- **4.4**: 经验验证覆盖 23 配置 × 3 数据集。Fig 3 (F1 vs bias) 有效支撑核心论点。建议补充 CI for ρ。
- **4.5**: FWL invariance 措辞需精确限定为 covariate topologies only。K=3/5/10 校正方法对比是 R12 后的显著改善。PPI++ 对 M-bias 有害的机制需解释。

### Section 5 (Conclusion)
- 简洁准确，符合页面限制。

### Limitations
- 覆盖了主要限制（non-differential、线性 SEM、LLM 覆盖）。可进一步加 DAG 未知时的应对策略（1-2 句）。

### Appendix
- 极为详尽（22 页），完整证明和 10+ 鲁棒性检验。两位 Reviewer 均赞扬学术严谨性。
