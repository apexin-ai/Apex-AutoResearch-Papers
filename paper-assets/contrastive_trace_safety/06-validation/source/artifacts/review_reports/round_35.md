---
round: 35
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T21:49:14.872383+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: True
---

# 审稿报告 — Round 35 (Fresh Review) [修正版]

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR Long Paper, 8-page main text + unlimited refs)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**审稿模式**: Fresh（重新审稿，无历史轮次记忆）
**收敛**: Round 1 完成。5 项 AGREE + 2 项 REBUT（novelty 定位 + 32B framing）。分歧属学术判断，非事实争议，不需追加轮次。

---

## Summary

本文研究推理模型中 hidden-state safety probe 的 layer selection 敏感性问题。作者在 4 个推理 LLM（R1-8B/Llama-3, OT-7B/Qwen2.5-7B, QwQ-32B/Qwen2.5-32B, R1-32B/Qwen2.5-32B）上发现：layer selection metric 的选择（crossing-rate composite vs. threshold-based）导致 14-61 层的系统性分歧，并定性反转 hidden states 是否优于 text 的结论——浅层两者等效（p=0.83），深层 HS 优势显著（+20-22pp precision, p<0.005, cross-validated at 7-8B）。论文将此偏差归因于 cosine compression 机制，提供 AdvBench 跨数据集复制和 Gemma-2 跨架构几何验证，报告 7 种替代检测方法均不及监督探针。

---

## Strengths

**S1. 核心发现具有实践价值且统计可靠。** 同一数据上 p=0.83 vs. p<0.005 的定性逆转（Table 2）是 striking 的实证发现。Metric 选择作为被忽视的 specification choice 影响安全结论，对 safety probing 社区有直接方法论指导价值。AdvBench 跨数据集复制增强 C1 的可信度。R1 特别强调：14-61 层的分歧 + 结论的正负逆转，在 safety-critical 领域具有独立的论文级价值。[R1, R2 共识]

**S2. 统计框架远超同类论文水平。** Nested 5-fold LOO-CV（7-8B）, exact permutation tests（32B, n≤20）, BCa bootstrap CIs（10,000 resamples, trace-level clustering）, Holm-Bonferroni step-down correction（12 final tests）, 后验 power analysis（MDE 报告）, Cohen's d, 三级 evidence gradient（confirmed/significant†/exploratory†）。[R1, R2 共识]

**S3. 证据分级透明诚实。** 7-8B（cross-validated confirmed）、QwQ-32B（significant†）、R1-32B（exploratory†）三级划分全文一致。Bug disclosure（Section M）高度透明。[R1, R2 共识]

**S4. 几何机制提供可检验假设。** Table 8 定量展示浅层 inter-step cosine distances 比深层小 1.4-2.7×。Random-label controls（Tables 6-7）证实浅层选择是 label-independent geometric artifact。虽因果证据不足（见 W3），但提供了明确的后续实验方向。[R1, R2 共识]

**S5. 附录极为详尽（~20 页, 24 节）。** 覆盖 random-label decomposition、cosine volatility、selectivity、multi-seed stability、position residualization、power analysis、hyperparameter robustness 等。[R1, R2 共识]

**S6. 负面结果系统报告。** Section 4.6 + Appendix P 系统报告 BOCPD/CUSUM/RepE/CCS/MLP 等 7 种方法的失败。[R1, R2 共识]

---

## Weaknesses

### Must-Fix (Critical)

**W1 [critical, R1-N1 + R2-N2, 共识 AGREE] 架构覆盖失衡——"cross-architecture" 过度声称 + 缺乏非 reasoning 模型控制。**
Table 1 中 4 个模型实际为 **1 Llama-3 + 3 Qwen2.5**。完整 metric→layer→conclusion cascade 的 cross-architecture 验证仅有 R1-8B 一个非 Qwen 模型。Gemma-2（Section B.3）仅验证 geometric precondition。R1 在交叉回应中补充了重要新维度：**全部 4 个模型均为 reasoning model，无非 reasoning 控制**。论文标题暗示 reasoning-model 特异性，但实验无法区分 layer selection sensitivity 是 reasoning model 特有还是 safety probing 的通用属性。Llama-3.1-8B-Instruct（非 reasoning, 同架构）是低成本的控制实验——如果偏置在非 reasoning 模型上同样存在，论文影响力反而更大。

**W2 [critical, R1-N2, 共识 AGREE] 位置混淆在 32B 上吸收 HS 优势，且显著性与统计功效混淆。**
Quadratic residualization 在 2/4 模型中吸收 HS advantage——恰好是 32B 模型。保留显著性的 R1-8B（n=43）远大于其余模型。Linear vs. quadratic 差异（Table S2: linear 3/4 vs quadratic 2/4）暗示位置效应可能是非线性的，但论文未讨论此差异的含义。

**W3 [critical, R1-N3 + R2-W1, 共识 AGREE] Cosine compression 因果链缺直接干预证据。**
Abstract "**The mechanism is cosine compression**" 是论文中最强的未验证因果声称。R1 提出具体验证实验：**对每层 hidden states 做 L2 归一化后重新计算 crossing rate**——如果 CR-composite 不再偏好浅层则因果链成立，否则说明非 compression 因素在驱动。R2 补充替代解释：浅层 lower-rank structure、proximity to input embedding。R1 将此保持为 must-fix：因果机制是 Discussion 的核心叙事支柱，仅有相关性则 Discussion 解释力显著降低。**两位 Reviewer 一致认为这是本文最关键的方法论缺陷。**

### Should-Fix (Warning)

**W4 [warning, R1-W1, 共识 AGREE] AdvBench 仅验证 C1 未验证 C2。**
AdvBench 复现 metric-induced layer selection bias (C1) 但未验证 HS vs. text 优势（C2）。C1 和 C2 是独立 claim，后者外部验证更弱。

**W5 [warning, R1-W2, 共识 AGREE] 两阶段设计的探索自由度。**
Layer 和 window 选择基于 validation set，最终评估在同分布 test set 上。未采用 nested CV。Table 34 的 13-25% shrinkage 定量反映此 optimism。

**W6 [warning, R1-W3 + R2-W3, 共识 AGREE] 32B n=19-20 统计推断受限。**
LOO-CV fold stability: R1-32B/QwQ-32B dominant layer 仅 65-68% folds 被选中（vs R1-8B 100%）。

**W7 [warning, R1-W4 + R2-W4, 共识 AGREE] Ensemble holdout 选择偏置 + Ens-Best 不显著。**
R1 补充关键发现：Table 3 Ens-Best 差异 **p>0.22（不显著）**——无统计学证据表明 ensemble 优于 best single metric。Ensemble 的 robustness 论证（"不需选对指标"）有部分支持（4 模型 best single metric 不完全一致），但缺乏外部验证。Level 3 recommendation 应弱化为 "potential improvement pending further validation"。

**W8 [warning, R1 AGREE R2-W2] 负面结果 (C3) 主文归因不足。**
R1 补充两个深层假设：(1) CCS 失败暗示 safety signal 与 contrast-consistent directions 不对齐；(2) Cross-model transfer 失败暗示 safety encoding 是模型特异的，与 "architecture-general" 声明存在张力。主文 Section 4.6 过于简略，应指向 Appendix J/P 的 detailed failure analysis。

---

## Reviewer Consensus

| ID | 问题 | R1 | R2 | 交叉结果 |
|----|------|----|----|----------|
| W1 | 架构 + 非 reasoning 控制 | N1 Must-Fix | N2 Must-Fix | **AGREE** (R1 补充非 reasoning 控制维度) |
| W2 | 位置混淆 + power | N2 Must-Fix | W3 → 升级 | **AGREE** |
| W3 | Cosine compression 因果 | N3 Must-Fix | W1 → 升级 | **AGREE** |
| W4 | AdvBench C1 only | W1 Should-Fix | 补充证据 | **AGREE** |
| W5 | 两阶段探索自由度 | W2 Should-Fix | 补充证据 | **AGREE** |
| W6 | 32B 统计推断 | W3 Should-Fix | W3 Should-Fix | **AGREE** |
| W7 | Ensemble 偏置 | W4 Should-Fix | W4 Should-Fix | **AGREE** (R1 补充 p>0.22) |
| W8 | C3 主文归因 | AGREE R2-W2 | W2 Should-Fix | **AGREE** |

## Reviewer Divergence

**分歧 1 — 新颖性定位 [R2-N1]（评分分歧的核心驱动）**

- **R2 立场**: C1（metric→layer→conclusion cascade）本质是 Belinkov (2022) 已知 probing sensitivity 在 safety domain 的 instantiation。概念层面增量有限。
- **R1 REBUT**: (1) 14-61 层分歧的**定量规模**远超一般 probing sensitivity 文献（Tenney et al. 2019 报告渐变关联，非对立选择 + 结论逆转）；(2) 结论正负逆转在 safety-critical 领域的**实践后果**具有独立论文级价值；(3) cosine compression 与 crossing-rate 行为的具体联系是**新观察**，非文献重述。R1 建议降级为 Should-Fix。
- **R1 让步**: 论文确实应在 Related Work 中更系统地对比 probing methodology 文献，量化 safety probing 中 sensitivity 的*程度*是否异常。
- **Director 评估**: R1 的三点论证部分有说服力——quantitative scale + conclusion reversal 确实超越简单 domain replication。但 R2 的 conceptual incrementality 担忧在 *ACL 审稿标准下是合理的。此分歧是 legitimate academic disagreement，deferred to AC。在报告中如实记录双方立场。

**分歧 2 — 32B framing [R2-W3]（次要分歧）**

- **R2 立场**: Table 2 的 R1-32B p<0.001 与 Section 8 的 boundary condition 之间存在 "张力"。
- **R1 REBUT**: Table 2 p<0.001 是关于**层选择分歧**（C1），Section 8 boundary condition 是关于 **HS 优势**（C2），这是两个不同的研究问题，不存在真正张力。
- **R1 让步**: Abstract 中 7-8B 与 32B 结果的并列呈现可能让快速阅读者忽略 32B 的弱结果。
- **Director 评估**: R1 的技术 REBUT 正确——R2 混淆了 C1 和 C2 两个声明。但 R2 关于 Abstract 清晰度的底层担忧合理。已在 Detailed Comments 中保留 Abstract 改进建议。

---

## Questions

**Q1.** BGE-large (1024d) + quadratic position residualization 叠加条件下，HS advantage 是否在所有 4 个模型上消失？Table 27 和 Table 30-31 分别报告但未交叉。

**Q2.** Linear residualization 3/4 保留显著性 vs. quadratic 2/4——是 quadratic model 过拟合还是真实非线性 confound？请提供 R² 或 AIC/BIC 对比。

**Q3.** 对浅层表征做 L2-normalization 后重新计算 crossing-rate，layer selection 分歧是否缩小？（cosine compression 因果链最小验证）

**Q4.** Human-human inter-annotator agreement（非 LLM-human）计划何时补充？

**Q5.** 在 Llama-3.1-8B-Instruct（非 reasoning 同架构模型）上运行同实验，layer selection bias 是否同样存在？

---

## Missing References

### 必须补充（R1 "最不应该缺失的引用"）

1. **Ethayarajh (2019)** — "How Contextual are Contextualized Word Representations?" — **直接研究 contextual representations 的 anisotropy**（即论文所说的 "cosine compression"），是 representation geometry 领域的开创性工作。论文 Section B（Appendix）详细讨论 shallow layer cosine compression 但完全未引用该领域的基础文献。R1 指出：此遗漏使论文看起来对 representation geometry 文献不够熟悉，可能被 reviewer 视为学术不严谨。**必须补充。**

### 建议补充

2. **Tenney et al. (2019)** — "BERT Rediscovers the Classical NLP Pipeline" — layer-wise probing 开创性工作
3. **Ravichander et al. (2021)** — "Probing the Probing Paradigm" — probing methodology 批判
4. **Voita & Titov (2020)** — MDL probing — 与本文 "不同指标产生不同层选择" 核心关切一致
5. **Pimentel et al. (2020)** — Information-theoretic probing — 理论框架
6. **Elazar et al. (2021)** — Amnesic probing — "移除信息后观察效果" 范式与 position residualization 在精神上相似

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成（2026-05-25 21:15-21:20 UTC）

| 严重性 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | p5 | 单页承载 Figure 3 + Table 2 + Table 3，视觉密度高 |
| ⚠️ warning | p7 | Figure 5 + Table 4 + Table 5 最密集页，留白极少 |
| ⚠️ warning | pp11-23 | Appendix 前 13 页仅 1 figure，视觉单调 |
| ℹ️ info | 全文 | Figure 3 heatmap 红-绿色阶不利于色盲；Figure 4 hollow/filled dots 灰度区分度有限 |
| ℹ️ info | pp1-8 | 11 display items in 8pp (~1.4/p)，密度合理 |
| ℹ️ info | 全文 | 无 LaTeX 错误，双栏对齐良好 |

**总评**: 0 critical, 3 warning, 15 info。8-page 限制下的正常 tradeoff。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**置信度: High (4/5)**
**R1: 3.5 (Borderline Conference) | R2: 3.0 (Findings)**

**评分分歧说明:**
R1 与 R2 的 0.5 分差异完全由新颖性评估驱动（见 Divergence 分歧 1）。R1 认为 14-61 层分歧的定量规模和结论逆转的实践后果构成超越 domain replication 的独立贡献（3.5）；R2 认为概念层面增量有限（3.0）。在所有方法论问题上双方完全一致。

**Director 评估 → 3.0 (Findings):**

核心方法论发现（C1: metric-induced layer selection bias 导致 14-61 层分歧和结论定性逆转）solid 且 reproducible。统计框架远超同类论文。证据分级诚实透明。

但三个 Must-Fix 结构性问题共同限制论文达到 Main Conference 标准：

1. **架构覆盖**（1 Llama + 3 Qwen, 无非 reasoning 控制）使 "cross-architecture" 和 "for Reasoning Models" 两个核心声称均缺乏充分验证。
2. **Cosine compression 因果主张**仅有 correlational evidence，Abstract "The mechanism is cosine compression" 未获验证。
3. **32B position confound + 统计功效**问题使 C2（HS advantage）的 generality 大打折扣。

C2 在 7-8B 上 cross-validated 且 solid，但在 stronger controls 下系统性削弱（384d 4/4 → 1024d 1/4 → quadratic 2/4），暗示 HS advantage 可能部分源于 text encoder ceiling。关键叠加实验未报告。Ethayarajh (2019) 这一 representation geometry 基础文献的缺失使论文的学术定位显得不够完整。

论文作为 **Findings** 有价值：well-documented 方法论警示 + 可检验几何假设 + 3-tier defense 实用建议。R1 关于定量规模和实践后果的论点有一定说服力，但在结构性限制（单一数据集、架构同质性、缺失因果验证）未解决的情况下，Director 倾向 R2 的 3.0 评估。

**EMNLP 2026 ARR**: 3.0 = Findings（可被 Findings 接收）

---

## Detailed Comments

### Abstract (p1)
- **"The mechanism is cosine compression"** → 改为 "A candidate mechanism is cosine compression" 或 "cosine compression correlates with the bias"
- **"two architectures"** → 改为 "(one Llama-based, three Qwen-based, at two scales)" 明确分布
- **"the geometric precondition extends to a fifth architecture (Gemma-2)"** → 标注仅验证 precondition 而非完整 cascade
- 187 words — 符合 200-word 限制

### Related Work
- **必须**增加 Ethayarajh (2019) anisotropy 文献——与论文核心讨论的 cosine compression 直接对应
- 建议扩展 probing methodology 对比（Belinkov, Voita, Hewitt, Pimentel），特别量化 safety probing 中 sensitivity 程度是否异常

### Section 4.3 — Position Residualization
- 建议将 32B 详细分析移至 Appendix，释放空间
- 应讨论 linear vs. quadratic 差异的含义

### Section 4.6 — Negative Results
- R1 补充：CCS 失败暗示 safety signal 与 contrast-consistent directions 不对齐；transfer 失败暗示 model-specific encoding。应指向 Appendix J/P

### Section 5 — Discussion
- 缺乏：C1 impact on existing literature、encoder ceiling interpretation、ensemble caveats（p>0.22 non-significant）、linear vs. quadratic 理论解读

### Limitations
- 缺少：human-human IAA、cosine compression correlational status 明确承认、ensemble selection bias、非 reasoning 模型控制限制