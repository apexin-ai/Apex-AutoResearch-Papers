---
round: 43
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-23T08:51:15.857185+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

## Round 43 审稿报告

**论文**: Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**审稿模式**: Fresh（全新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验/统计; R2: 新颖性/相关工作/写作）
**轮次**: 1 轮（交叉回应后达成共识，无需 Round 2）

---

### Summary

论文研究 test-time compute scaling（self-consistency, best-of-N）在 NER 任务上的表现，核心发现是 "correlation-selection gap"：质量估计信号可预测输出质量（AUROC 达 0.82）但无法转化为 instance-level selection gains（≤1pp）。通过 degeneracy 和 signal alignment collapse 两个维度建立诊断框架，并在 entity-level construction 上报告了有条件的正向结果（+1.40pp on Few-NERD, 3-epoch）。实验覆盖 4 个 NER 数据集、2 个模型族、4B-72B scale range，附带 RE 和 SQL 初步探索。

---

### Strengths

**S1. Correlation-selection gap 是真实且有价值的发现。** 质量估计信号与输出质量的高相关性（ρ 达 0.45, AUROC 0.82）为何无法转化为选择增益（≤1pp），这一现象此前未被系统识别。对 NER 实践者有直接价值——避免在无效的重复采样上浪费推理预算。[R1-S1, R2-S1 共识]

**S2. 实证覆盖面和系统性极高。** 4 个 NER 数据集 + RE + SQL，5 个信号族，2 个模型族 + 3 个 scale + GPT-5.5 frontier，57 项统计检验，46 页 appendix 包含 robustness checks、calibration 分析、mechanistic probes。[R1-S2, R2-S2 共识]

**S3. 统计报告透明。** 同时报告 global Holm (k=57) 和 per-family Holm (k=10)，明确 p_adj=0.055 的边界情况，附 post-hoc power analysis、bootstrap CI、permutation tests。[R1-S3, R2-S4 共识]

**S4. 与 concurrent work 的坦诚对比。** Table 1 和 §2 对 Landesberg et al. (2026) 的定位诚实，承认 concurrent discovery validates the gap as cross-domain。[R2-S3]

**S5. Degeneracy 概念框架清晰。** 将 gap 分解为结构性层（信号赋予所有候选相同分数）和诊断性层（LP 压缩），概念清晰。[R1-S4]

---

### Weaknesses

#### Must-Fix（两位 Reviewer 共识）

**[MUST-FIX] W1. 2-3 seeds 统计推断力严重不足 [R43-N1]**
核心 negative claim（"selection yields <1pp"）依赖 2-3 seeds，但 bootstrap CI 跨越零点（LP Δ 95% CI [-0.41, +2.54]）。无法区分"真无效应"和"检测力不足"。§7.4 报告的 signal ranking 稳定性（ordinal）不等同于效应量显著性（cardinal）。
- R1 Must-Fix, R2 AGREE
- 建议：negative claims 改为 "we find no evidence of selection gains within our statistical power"；正文附 CI；报告 MDE（最小可检测效应量）

**[MUST-FIX] W2. Degeneracy decomposition bound 过松，贡献定位不一致 [R43-N2]**
Bound 仅恢复 3-12% oracle gap（Figure bound），§6.3 自述 "intentionally loose necessary condition"，但 §1 将其列为四大贡献之一（Explore [§5, §6]），framing 不一致。Bound 更接近存在性定理而非精确诊断工具。
- R1 Must-Fix, R2 AGREE
- 建议：§1 将 bound 降级为 existence result；正文报告恢复率；降低论述调性

**[MUST-FIX] W3. 观察性设计下因果措辞系统性过强 [R43-N3]**
论文自述 observational (§3)，但多处使用因果语言：§1 "jointly determine"、§4 "eliminates the variation"、§4 标题 "Where Single-Signal Selection Fails"（暗示因果）、§6.2 "inverse scaling"、§8 "localizing failure"。Figure 1 的 "(diagnostic sequence, not causal chain)" 免责仅在 caption 中。Few-NERD 3v5 epoch 同时改变 degeneracy 和 alignment——混淆变量的直接证据。
- R1 Must-Fix, R2 strongly AGREE
- 建议：系统性替换因果措辞为关联性描述；§3 首段增加 observational design 声明；增加混淆变量讨论

**[MUST-FIX] W4. 处方性结果统计基础不足 [R43-N4]**
Entity-level construction 的全局 Holm p_adj=0.055 不显著；per-family p_adj=0.006 依赖未预注册的 family 划分。Abstract 中 per-family 值先于 global 值，引导读者优先注意更显著值。Prescriptive claim 是论文区别于 "pure negative results" 的关键差异点——如果站不住，novelty 进一步下降。
- R2 Must-Fix, R1 AGREE
- 建议：prescriptive 结果降级为 exploratory observation；或增加额外实验增强 power

#### Should-Fix（影响评分）

**[SHOULD-FIX] W5. 标题-内容不匹配 [R43-N5]**
"Why Self-Consistency Fails for NER" 与 §7.5 conditional gains (+1.40pp)、§5.1 cross-model positive results、§8 conditional recommendation 不一致。
- R2 Must-Fix, R1 REBUT（标题描述默认配置主导现象，ACL 标准范式）
- Director 判定：降为 Should-Fix，但强烈建议修改为条件性表述

**[SHOULD-FIX] W6. Table 1 novelty comparison 维度偏向本文 [R43-N6]**
Failure decomp. 和 Diagnostics 重叠计分；Prescriptive 标 "Conditional" 但全局不显著；缺少对竞争工作有利维度。
- R2 Must-Fix, R1 REBUT（两维度是不同层次）
- Director 判定：降为 Should-Fix，建议合并重叠维度并标注 p 值

**[SHOULD-FIX] W7. Few-NERD epoch 混淆无法分离 [R43-W1]**
3-epoch undertrained model 不仅 degeneracy 低，还可能有更弱的 greedy baseline。实践者部署 fully converged model，prescriptive recommendation 的泛化性存疑。
- R1 Should-Fix, R2 AGREE

**[SHOULD-FIX] W8. RE/SQL 扩展过于初步 [R43-W2]**
RE (n=397, 单数据集) 和 SQL (n=196) 规模不足以支撑 "cross-task exploration" 宣传。
- R1-W5, R2-W2 独立提出

**[SHOULD-FIX] W9. 数字密度过高 [R43-W3]**
Abstract ~15 个数值，§7 每句 2-3 个数字，影响可读性。
- R2-W1, R1 AGREE
- 建议：Abstract 保留 4-5 个关键数字

**[SHOULD-FIX] W10. 模型多样性有限 [R43-W5]**
仅 Qwen + LLaMA 两个开源家族。Frontier model degeneracy profile 差异大（5.5-74%），论文基于 12-68% 开源模型的结论普适性存疑。
- R1-W4, R2 AGREE

**[SHOULD-FIX] W11. "Primarily diagnostic" 定位削弱实用价值 [R43-W6]**
框架无法事前预测哪些实例受益于 scaling。Pilot N=8 diagnostic 有实用场景但 §7.5 未展开为 practitioner workflow。
- R2-W3, R1 部分 REBUT

**[SHOULD-FIX] W12. 相关工作可能遗漏 [R43-W8]**
Malinin & Gales (2021) 关于自回归结构化预测不确定性估计、Reflexion (self-verification for structured outputs) 应讨论。
- R2-W4, R1 部分 AGREE

---

### Reviewer Consensus [AGREE]

以下问题两位 Reviewer 完全达成共识：

1. **Seeds 不足是论文最大统计瓶颈** — 核心 negative claims 和 positive claims 的 CI 均过宽
2. **Bound 过松与贡献定位不一致** — §1 的宣传与 §6.3 的实际效果脱节
3. **因果措辞需系统性降级** — 全文需替换为关联性描述
4. **Per-family Holm 未预注册** — prescriptive claim 的统计基础不牢
5. **RE/SQL 过于初步** — 与 cross-task 宣传不匹配
6. **数字密度过高** — Abstract 和 §7 需精简
7. **核心判断：论文的分析质量高于其 claim 的可靠性** — 框架设计合理、实验覆盖广，但统计推断力不足以支撑正文中的 claim 强度

---

### Reviewer Divergence [REBUT]

1. **标题是否需要修改** — R2 Must-Fix（过度简化），R1 REBUT（ACL 标准范式，降为 should-fix）。Director 判定：降为 Should-Fix，建议添加条件性修饰。
2. **Table 1 维度是否 cherry-picking** — R2 Must-Fix，R1 REBUT（两维度是不同层次）。Director 判定：降为 Should-Fix。
3. **新颖性判断** — R1 认为 correlation-selection gap 是 genuinely surprising（AUROC 0.82 却 ≤1pp 选择增益，直觉无法预见）；R2 认为 SC 在结构化输出上效果差是可预期的直觉，论文的贡献在于量化而非发现。Director 判定：发现本身有价值，但 "量化已知方向的现象" 的 excitement 确实低于 "反直觉发现"。

---

### Questions

Q1: Bound 的 3-12% 恢复率是否已是该分析框架下的阶最优？如果不是，为何不追求更紧 bound？

Q2: Free-form decoding 一致性反转 RE LP selection——correlation-selection gap 是否 decoding-strategy-dependent？结论适用范围需怎样限定？

Q3: Entity construction θ 依赖 held-out data 选择（0.15-0.35 跨数据集），这是否削弱了 pre-deployment diagnostic 的实用性？

Q4: 69% inverse scaling 的 N-transitions 中，高/低 degeneracy 子群的比例是否显著不同？如果是，这支持诊断框架；如果否，框架预测价值存疑。

---

### Missing References

1. **Malinin & Gales (2021)** — "Uncertainty Estimation in Autoregressive Structured Prediction"：直接相关于自回归结构化预测的不确定性估计
2. **Shinn et al. (2023, Reflexion)** — 迭代自我验证方法在结构化任务上的应用
3. 传统 NER ensemble 方法（CRF ensemble, BiLSTM-CRF bagging）与 LLM self-consistency 面临类似挑战的历史联系（R1 认为关联较弱）

---

### External Review (Stanford Agentic Reviewer)

未配置外部审稿，跳过。

---

### Visual Layout Check（非评分项）

视觉审查 Agent 超时（300s timeout）。未产生有效 findings。用户可手动重新触发。

---

### Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Overall | 3.5 | 3.0 | 3.0 |
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3.5/5 | 2.5/5 | 3/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**判定理由**：

论文揭示了一个真实且有价值的现象（correlation-selection gap），实证覆盖面和统计透明度值得肯定。但四个共识性 Must-Fix 问题限制了论文的可靠性：

1. **统计推断力不足**（seeds 太少）使核心 claims——无论 negative 还是 positive——的 CI 过宽
2. **Bound 过松**与贡献定位不一致，理论贡献被高估
3. **因果措辞过强**与自述 observational 设计矛盾
4. **Prescriptive claim 统计基础不牢**——论文区别于 "pure negative results" 的关键差异点站不住

核心判断：**论文的分析质量高于其 claim 的可靠性**。如果将 claims 系统性降级（因果措辞→关联性、bound→existence result、prescriptive→exploratory），论文作为 Findings 级别的实证分析是合格的。修改 W1-W4 后有望达到 3.5（Borderline Conference），但当前状态更适合 Findings。

---

### Detailed Comments

**§1 Introduction**: 四阶段路线图的 "Explore" 将 bound 列为主要贡献，与 §6.3 的 "intentionally loose" 不一致。Mechanistic evidence 在 Appendix 中却列为贡献点。

**§2 Related Work**: Table 1 的 7 维度应合并 "Failure decomp." 和 "Diagnostics"，并在 "Prescriptive" 一栏标注 p_adj。缺少 Malinin & Gales (2021) 和 Reflexion 的讨论。

**§3 Diagnostic Framework**: 首段应增加 observational design 声明，明确后续分析为关联性而非因果性。

**§4 Single-Signal Selection**: 标题 "Where Single-Signal Selection Fails" 暗示因果，建议改为 "Single-Signal Selection Results" 或类似中性表述。

**§6.3 Degeneracy Decomposition**: 正文应报告 3-12% 恢复率（当前仅 Appendix），将 bound 降级为 existence result / screening test。

**§7.5 Prescriptive Results**: Abstract 中 per-family p_adj 应后置于 global p_adj。正文应明确声明全局校正下不显著并讨论含义。3-epoch condition 需增加 greedy baseline 控制讨论。

**Abstract**: ~15 个数值过多，建议保留 4-5 个关键数字。RE/SQL 提及应进一步缩减。

**Limitations**: 当前内容充分。可增加 "decoding-strategy-dependent" 的讨论。