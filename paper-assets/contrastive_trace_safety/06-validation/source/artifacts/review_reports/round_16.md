---
round: 16
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-19T09:15:03.128409+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 16 (Fresh Review)

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性; R2: 新颖性与完整性）
**轮次**: Round 1 独立初审 → 交叉分享 → 共识达成（1轮收敛）

---

## Summary

本文系统研究了隐藏状态(HS)安全探针在推理模型上的层选择敏感性问题。通过4个推理模型（R1-8B, OT-7B, QwQ-32B, R1-32B）、5种选层指标和7种替代方法的实验，论文发现：(1) biased composite metric（balanced accuracy × crossing rate）在32B模型上选择浅层导致HS优势消失；(2) 校正后的threshold-dependent metrics选择深层恢复HS精度优势（+15.4至+21.9pp, Holm-Bonferroni corrected）；(3) 该优势是encoder-conditional且在R1-32B上position-mediated。论文提出五步审计协议并报告了7种替代方法的失败。

---

## Strengths

**S1. 重要的方法论警示（共识）**：层选择作为"关键研究者自由度"(researcher degree of freedom)的系统化识别对hidden-state probing文献具有广泛影响。Table 2的5-metric ablation清楚展示了biased vs corrected层选择如何逆转结论。

**S2. 统计方法论严谨（共识）**：Holm-Bonferroni校正（12-test + 4-test双框架）、BCa bootstrap (10,000 resamples)、exact sign-flip permutation test三种互补方法在NLP安全探针文献中不常见，树立了良好标准。

**S3. 科学诚信典范（共识）**：Section N的Bug Disclosure主动报告QwQ-32B文本探针pipeline bug并详述影响范围和修正，在同行评审论文中难得一见。

**S4. 负面结果报告价值（共识）**：Section 4.6 + Table 19系统报告7种替代方法失败原因，为后续研究划定方法边界。

**S5. 全面的消融覆盖（共识）**：附录A-Z涵盖层扫描(B)、表征压缩(C)、HB逐步检验(D)、窗口消融(E)、注释扰动(J)、多种子稳定性(X)、post-hoc power analysis(Z)等，实验深度充分。

**S6. Control task selectivity验证（共识）**：Section H正确使用Hewitt & Liang (2019)框架验证探针学到安全相关结构，方法论加分。

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical, 共识] Abstract precision gain声明掩盖了R1-32B的position mediation问题**
Abstract声称"+15.4 to +21.9pp, Holm-Bonferroni corrected"涵盖4个模型，但R1-32B的+21.9pp几乎完全由position mediation解释：Section V residualized gap仅+1.9pp，Section Z MDE为9.5pp（远高于实际效应）。读者自然认为4个模型都有robust HS优势，但R1-32B的non-positional证据实际上是统计不可检测的。正文Section 4.2将R1-32B归为"qualified"，但Abstract未反映这一nuance。
- **R1**: Critical (W1)
- **R2**: 隐含同意（W4中narrative tension）

**W2 [Critical, 共识] 32B模型联合超参数搜索空间相对验证集严重失衡**
2,240 configurations (64 layers × 7 W × 5 K)在QwQ-32B约3-4个per-class验证样本上搜索。LOO-CV(Table 25)显示BA-optimal layer跨fold跨度24层(R1-32B)；multi-seed stability(Table 26)显示R1-32B precision std=12.8pp。三项缓解分析（convergence、LOO-CV、multi-seed）均在同一数据上，不构成独立验证。论文未提供nested CV或validation-test gap量化。
- **R1**: Critical (W2)
- **R2**: 隐含同意

**W3 [Critical, R1] K=5 pre-selection缺乏任何justification**
论文声称K=5是事前设定（Section L），但未提供任何理由：无先验工作依据、无理论动机、无pilot study。Table 17显示K对coverage和safe FPR影响显著（K=1时safe FPR≈1.0，K=7时coverage仅51%），说明K的选择实质性影响结论。如为事后选择伪装事前，统计检验有效性受根本质疑。
- **R1**: Critical (W3)
- **R2**: 未单独标记，但在cross-response中未反对

**W4 [Critical, R2] 单一数据集严重限制可推广性**
全部实验仅使用HarmThoughts一个数据集。层选择敏感性这一核心发现可能是特定标注方案的产物。不同安全标注粒度、有害内容类型分布、标注团队都可能产生不同的层选择模式。对于声称揭示"方法论confound"的论文，单数据集验证的普遍性不充分。
- **R2**: Critical (N1)
- **R1**: Major (W7)

**W5 [Critical, R2] 五步审计协议作为贡献缺乏充分论证**
论文将五步审计协议列为贡献之一，但：(a) 无形式化定义（仅Discussion一段文字描述）；(b) 无协议自身的评估（遵循/不遵循协议的false discovery rate？）；(c) 步骤选择无理论依据（为什么≥5 metrics？为什么report 2nd/3rd?）。作为三条贡献之一，仅停留在"建议"层面而无验证。
- **R2**: Critical (N2)
- **R1**: Major (W6，关于5 metrics选择可能post-hoc）

### Should-Fix（显著影响论文质量）

**W6 [Major, 共识] Position baseline对HS advantage core claim的冲击未充分处理**
QwQ-32B position baseline BA(74%)高于HS probes(~68%)（Table 4）。R1-32B residualized probing p=0.914（Section V），HS advantage完全被position解释。2/4模型上position特征与HS probes表现相当或更好，核心claim"hidden states提供文本探针无法捕获的安全信息"被动摇。
- **R1**: Critical→降为Major（考虑论文已在正文讨论）
- **R2**: 隐含同意

**W7 [Major, R2] 新颖性定位不够清晰——层选择对探针的影响是已知现象**
探针性能对层选择敏感是probing文献中广泛讨论的现象（Tenney et al., 2019; Jawahar et al., 2019; Belinkov & Glass, 2019均在bib中但未在正文引用）。应用到安全领域的增量需更清楚地与已有知识区分。Related Work中probing methodology段过于简短。
- **R2**: Major (W1)
- **R1**: 未单独标记但交叉中未反对

**W8 [Major, R2] 与Boxo et al. (2025)差异化不充分**
Boxo et al.直接研究linear probes依赖textual evidence，与本文发现的浅层探针利用text feature leakage高度相关。论文仅一句话提及，未解释增量。
- **R2**: Major (W2)

**W9 [Major, R2] 模型多样性不足——3/4共享Qwen基座**
R1-32B、OT-7B、QwQ-32B均基于Qwen，仅R1-8B基于Llama。"spanning two architectures"准确但跨架构结论强度被削弱。
- **R2**: Major (W3)

**W10 [Major, R1] BCa bootstrap在n=17(QwQ-32B)上的可靠性存疑**
BCa依赖jackknife加速度估计，n=16时估计噪声大，CI覆盖性可能偏离95%。未报告加速度参数值或CI稳定性诊断。Permutation test是好的补充但Table 3主要推断仍基于BCa CI。
- **R1**: Major (W4)

**W11 [Major, R1] LOO-CV双重解读矛盾**
Section B称层选择robust（65-68%一致率），Section V又说instability is the finding。35%不一致在32B上意味着对数据敏感。两个陈述逻辑矛盾。
- **R1**: Major (W5)

**W12 [Major, R1] 5种层选择指标选择可能post-hoc——biased vs corrected分类有循环论证风险**
未解释为何选这5个而非F1/AUROC/MCC，也未说明biased vs corrected分类是先验还是观察结果后。如先看到浅层被选再倒推crossing rate是bias来源，则整个论述循环论证。
- **R1**: Major (W6)

**W13 [Major, R2] Abstract/Introduction框架与实际结论存在叙事张力**
以"should a monitoring system read HS or text?"开头暗示二选一实用问题，但实际结论是方法论层面的("it depends on layer selection")。读者期望与交付不匹配。
- **R2**: Major (W4)

### Minor

**M1 [Minor]** Encoder-conditional advantage（1/4 HB at BGE-large 1024d）应在正文更早讨论，目前仅附录和Discussion一句。（R1-M1）

**M2 [Minor]** Selectivity 11.1-16.8pp缺文献benchmark参照值，读者无法判断高低。（R1-M2）

**M3 [Minor]** 5个orphan bib entries（jawahar2019bert, liu2019linguistic, meng2022rome, tenney2019bert, zhang2025probing_selfverify）。其中Tenney和Jawahar应引入正文。（R1-M3, R2-M1共识）

**M4 [Minor]** 表格小数精度不完全统一（Table 2 vs Table 3）。（R2-M2）

**M5 [Minor]** CP定义在Abstract过于简略，精确定义到Section 1才出现。（R2-M4）

**M6 [Minor]** GRU与LR使用不同数据划分(70/30 vs 60/20/20)，影响有限但正文应更明确说明canonical比较。（R1-W8, R2隐含）

**M7 [Minor]** BOCPD/CUSUM作为alternative methods失败是可预见的——短推理链上变点检测功效本身不足，不能有力证明supervised probing必要性。（R1-W9）

**M8 [Minor]** Section 5 deployment operating points内容与方法论主线关系不大，建议移至附录。（R2-M6）

---

## Reviewer Consensus [AGREE]

1. **Overall Score: 3.0 (Findings)** — 两位Reviewer完全一致
2. **核心价值**: 层选择敏感性是真实且重要的方法论发现
3. **32B证据不足**: 统计功效不足(MDE >> observed effects)使32B结论不可靠
4. **Position mediation**: R1-32B HS advantage几乎完全由position解释
5. **单一数据集**: 限制了方法论confound claim的普遍性
6. **审计协议**: 缺乏形式化和验证，不足以作为主要贡献
7. **统计报告**: Bug disclosure和negative results报告是论文亮点
8. **写作质量**: 无AI痕迹，结构清晰，格式合规（8页正文、行号、匿名化完整）
9. **Findings定位**: 层选择敏感性发现有实用价值但novelty不足以达Main conference

## Reviewer Divergence [REBUT]

无实质性分歧。两位Reviewer从不同角度（R1: 统计方法论; R2: novelty/framing）得出相同结论。

差异仅在severity细节：
- R1将K=5 pre-selection列为Critical，R2未单独标记（但未反对）
- R2将单一数据集列为Critical，R1列为Major（但未反对）
- R1关注BCa reliability和LOO-CV interpretation（R2未深入但认同）
- R2关注novelty positioning和Boxo et al.差异化（R1未深入但认同）

这些差异互补而非矛盾。

---

## Questions（需作者澄清）

**Q1** [共识]: K=5何时确定？是否有事前文档（实验计划、代码提交记录）证明非事后选择？

**Q2** [R1]: QwQ-32B (n=17) BCa bootstrap的加速度参数值是多少？改变random seed后CI宽度变化是否超过10%？

**Q3** [R1]: 如果用nested 5-fold CV在32B上选(layer, K)组合，HS vs text结论是否成立？

**Q4** [R1]: 是否尝试了其他层选择指标（F1, AUROC, MCC）？5个指标的选择时序如何？

**Q5** [R1]: R1-32B residualized gap (+1.9pp) 远低于MDE (9.5pp)。作者认为R1-32B确实有non-positional HS advantage（样本不足）还是position artifact？

**Q6** [R2]: HarmThoughts标注者间一致性(IAA)是多少？单一标注者如何影响结果？

**Q7** [R2]: 除QwQ-32B外其他三模型是否做了类似pipeline完整性验证？

**Q8** [R2]: 审计协议第4步为什么是top-3而非top-5或所有通过阈值的层？

---

## Missing References

1. **Tenney et al. (2019)** "BERT Rediscovers the Classical NLP Pipeline" — 层级信息分布经典论文，已在bib中但未在正文引用，对层选择敏感性论证是必引。（R1+R2共识）
2. **Jawahar et al. (2019)** "What Does BERT Look At?" — 同上。（R1+R2共识）
3. **Belinkov (2022)** "Probing Classifiers: Promises, Shortcomings, and Advances" — probing方法论综述，已引用但正文讨论不足，与本文统计陷阱发现高度相关。（R1）
4. **Vig et al. (2020)** "Causal Mediation Analysis for Interpreting Neural NLP Models" — position mediation分析与causal mediation关系应明确。（R1）
5. **Marks & Tegmark (2024)** 已引用但可在representation geometry讨论中更深入使用。（R2）
6. **Gurnee & Tegmark (2024)** "Language Models Represent Space and Time" — 不同层编码不同信息的空间模式，支撑层选择敏感性一般性。（R2建议性）

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**ARR评分对照**: 3 = Findings（可被Findings接收）

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Confidence | 4/5 | 4/5 | 4/5 |

**置信度**: 4/5（两位Reviewer均为probing方法论和安全检测领域专家，认真审查了全文和附录）

**一句话评语**: 论文识别了hidden-state安全探针中层选择敏感性这一真实且重要的方法论问题，统计分析严谨、负面结果报告诚实、pipeline bug披露透明；但32B模型统计功效不足使"across four models"的claim实际只有7-8B可靠，position baseline在2/4模型上挑战HS advantage核心claim，单一数据集限制方法论confound发现的普遍性，五步审计协议缺乏形式化验证不足以作为主要贡献。总体适合EMNLP Findings接收。

**升分路径**（3.0 → 3.5 Borderline Conference）:
1. Abstract/Introduction准确限定R1-32B结论（position-mediated, below MDE）
2. 提供K=5事前justification或nested CV结果
3. 增加至少一个独立数据集验证层选择敏感性复现
4. 明确5个指标选择时序，消除循环论证嫌疑
5. 从Contributions列表中移除审计协议或形式化验证

---

## Detailed Comments

### Abstract
- 180 words，格式合规
- "+15.4 to +21.9pp"范围包含R1-32B position-mediated值，应排除或加限定
- CP定义应更精确（当前过于简略）
- "the empirical HS advantage is conditional"措辞准确但可能让审稿人觉得核心贡献不够strong

### Section 1 Introduction
- 叙事结构基本完整（背景→痛点→现有不足→贡献）
- 以"should read HS or text?"开头的框架与实际方法论审计结论存在张力，建议调整
- Contributions列表清晰，三条均有section支撑，但五步审计作为隐含第四条出现在Discussion中，叙事不一致
- 应更早提及position baseline的挑战

### Section 2 Related Work
- 六个方向分类组织合理，无堆砌模式
- Probing Methodology段过于简短，未充分讨论层选择在probing文献中的已有认知
- 与Boxo et al.和Kadali & Papalexakis差异化不充分
- Tenney et al.和Jawahar et al.在bib中但未在正文引用，是重要遗漏

### Section 3 Problem Setup
- CP定义清晰（Section 3.1）
- 5个指标选择理由和"biased vs corrected"分类的时序需澄清
- K=5 pre-selection需提供justification

### Section 4 Experiments
- Section 4.2（Layer Selection Sensitivity）是论文最强部分
- Section 4.3（HS vs Text）的position baseline结果应更醒目标记
- Section 4.4（32B Analysis）应明确标为exploratory（given power limitations）
- Section 4.6（Negative Results）具有独立价值

### Section 5 Discussion
- "Layer selection as researcher degree of freedom"框架恰当
- 五步审计过于简略，缺形式化定义和验证
- Deployment operating points与方法论主线关系较弱

### Section 6 Conclusion
- 简洁有效，但应增加"larger 32B datasets"作为next step

### Section 7 Limitations
- 覆盖四个方面，但statistical power讨论不够具体（应引用Table 32 MDE数字）
- 单数据集讨论过于轻描淡写

### 附录
- Section D (HB Correction): 严谨全面
- Section N (Bug Disclosure): 学术诚信典范
- Section V (Position-Residualized): R1-32B p=0.914极为重要，应在正文讨论
- Section Z (Power Analysis): 论文自身最有力的limitation证据，应在正文引用

### 格式合规
- 正文8页，合规
- 匿名化完整："Anonymous ACL submission"
- 行号已开启
- 引用格式一致（natbib）
- 表格小数精度有轻微不一致
- 图中字体≥7pt，可读性良好
- Limitations section存在且充实
- Responsible NLP Checklist完整