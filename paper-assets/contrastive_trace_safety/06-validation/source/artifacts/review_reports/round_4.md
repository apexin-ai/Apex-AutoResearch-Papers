---
round: 4
overall_score: 3.0 - Findings
timestamp: 2026-05-17T18:59:43.882019+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 5

**论文**: "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models"
**目标 Venue**: EMNLP 2026 (Findings track, via ARR)
**截止日期**: 2026-05-25
**审稿编排**: 2 Reviewers (R1: 方法严谨性+实验设计, R2: 新颖性+完整性)
**交叉分享**: 完成，收敛良好

---

## Summary

论文在4个推理模型(R1-8B, OT-7B, QwQ-32B, R1-32B)上系统比较了hidden-state probe与text probe检测safety commitment point的性能。核心方法论发现：layer selection中crossing rate组件引入系统性偏差，选择浅层掩盖了HS优势；corrected deep layers下12/12 Holm-Bonferroni测试通过。7种替代方法的负结果划定了方法边界。

---

## Strengths

1. **层选择敏感性发现具有广泛方法论价值** — crossing rate偏差的机理解释清晰、可验证，对任何使用阈值型检测的probing研究都有警示意义。这一发现本身值得发表。
2. **科学透明度优秀** — Bug disclosure (Appendix F)、compounding errors的完整追溯、biased vs corrected结果的并列呈现，在ML论文中罕见。Limitations section诚实全面。
3. **统计框架严谨** — Holm-Bonferroni correction, null-centered bootstrap, Hewitt control tasks, selectivity metrics，在同类工作中属上乘。
4. **负结果系统性强** — 7种方法×4模型的全面测试，包含完整配置搜索(BOCPD 5 configs, CUSUM 10 configs, PCA 3 dims × 5 pairs)，为后续研究划定清晰边界。
5. **覆盖有意义的变异维度** — 2 architectures × 2 scales × 2 training methods × 5 layer metrics × 7 windows，提供比单模型研究更强的外部效度。
6. **写作质量** — 无AI写作痕迹(零em-dash、零en-dash、无黑名单用词)，叙事连贯，主线统一性较好。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[N1] 文本基线维度不对等使核心modality claim不可信** [共识: R1+R2]
- HS特征4096-5120d vs text encoder all-MiniLM-L6-v2 384d，维度差10-13x。L2正则化LR在高维输入天然拥有更多可利用特征空间。
- 论文Discussion (Section 6 para 2) 自己提出信息论解释("hidden states should dominate text features purely by signal capacity")，等于自证维度差可能驱动全部结果。
- Temporal windowing在W=15时将绝对维度差进一步放大(61440d vs 5760d)。
- Contribution 2 ("Consistent HS precision advantage") 在未控制维度变量的情况下无法成立为modality发现。
- **修复方向**: (a) 增加至少一个768d+文本编码器(如all-mpnet-base-v2或BGE-base)；(b) 或HS PCA降维到384d后对比，isolate modality effect；(c) 或将framing严格限定为"vs. all-MiniLM-L6-v2 baseline"而非泛化的modality结论。

**[N2] "12/12 Holm-Bonferroni"呈现方式误导** [共识: R1提出, R2 agree with nuance]
- 3个指标(balanced accuracy, precision, FPR)在同一混淆矩阵上计算，统计上高度相关。Precision和FPR通过假阳性数学关联。同一模型内3测试几乎必然同时显著或不显著。
- Holm-Bonferroni在任意依赖结构下控制FWER是统计上valid的(R2指出)，但"12/12"的呈现给人12条独立证据线的错觉。真实独立确认数≈4(每模型一个)。
- **修复方向**: 改为"all 4 models show significant HS advantage on all three metrics"，强调4个独立模型而非12个相关测试。

**[N3] QwQ-32B: position baseline > HS probe + lead time负值，但Abstract/Intro叙事未反映** [共识: R1+R2]
- Position baseline bal_acc = 0.746 vs HS probe = 0.740 (Table 4, -0.6pp)。HS lead time负值(-1.2到+1.9步) vs text +3.7到+12.3步。
- Control task中position baseline accuracy(0.705) > HS probe(0.667)。
- Selectivity 14.4pp是vs random labels而非vs position features——主要编码位置信号的probe仍可有高selectivity。
- Abstract "precision gains across all four models" 暗示统一实践优势，但QwQ上HS检测更晚5-10步。
- **修复方向**: Abstract/Intro区分per-step accuracy vs practical detection superiority；对QwQ限定为"higher precision at cost of later detection"；考虑position控制变量回归。

### Should-Fix（影响评分但不一票否决）

**[W1] 32B样本量(n=19-20)统计功效不足** [共识: R1+R2, R2升级为critical]
- R1-32B W=1 coverage仅25%(5/20 traces)，precision/lead基于5个样本。论文未报告效应量95% CI。
- 建议报告bootstrap CI、对5-trace结果显著降级、考虑BCa校正。

**[W2] Negative results "all fail" framing偏差** [共识: R1+R2]
- RepE on QwQ-32B bal_acc 0.756 > supervised LR 0.740，不算"fail"。BOCPD 93%检出率有部署价值。Cross-model transfer仅PCA+direct未尝试CCA/Procrustes。
- 建议改为"produce inconsistent or limited results"；RepE-QwQ单独讨论。

**[W3] Related Work仍缺6-8篇2024-2026高相关论文** [共识: R1+R2]
- 遗漏: multi-dimensional refusal (arXiv:2602.02132 + ICML 2025), CoT monitorability, HS safety probing (ACL 2025), autonomous jailbreak agents, safety alignment depth (ICLR 2025), LEACE, amnesic probing。

**[W4] Discussion/Conclusion逐句对应重复** [共识: R1+R2]
- Conclusion sentences 2-4与Discussion内容逐项对应。约0.3-0.5页浪费。

**[W5] Layer selection泛化claim缺跨任务验证** [部分分歧: R2 raise, R1 partial rebut]
- Discussion声称"any threshold-based study..."但未在其他任务验证。
- 共识：对Findings track novelty足够，但应降级为hypothesis。

**[W6] "四个互补指标收敛"实质独立性≈2** [共识: R1+R2]
- Precision≈inverse FPR(数学相关)，additive composite由前三者派生。
- 建议增加正交指标(AUROC/MCC)或诚实表述为"two independent metric families converge"。

---

## Reviewer Consensus [AGREE]

以下问题两位Reviewer完全达成共识：
1. 文本基线维度混淆变量是论文最严重的问题(N1)
2. QwQ-32B的position baseline竞争力+负lead time削弱了HS claim的普遍性(N3)
3. "12/12"呈现方式需改善(N2)
4. Negative results "all fail" framing过度简化(W2)
5. Related Work引用不足(W3)
6. "四指标收敛"独立性被高估(W6)

## Reviewer Divergence [REBUT]

仅一处实质性分歧：
- **R1-W4 (multi-seed)**: R2反驳——LR是确定性算法，无seed敏感性。R1接受修正，同意真正关切是split sensitivity而非seed sensitivity。**共识结论**：主实验不需multi-seed，但split robustness(如cross-validation)是合理的future improvement。

- **R2-W5 (novelty ceiling)**: R1部分反驳——事后直觉≠事前可预见，quantified impact(5/12→12/12翻转)是实质贡献。但R1同意泛化声称需降级。**共识结论**：Findings track novelty足够，泛化claim应hedge。

---

## Questions

1. 如果将HS特征PCA降维到384d（与text encoder维度匹配），12/12 HB tests中有多少仍然pass？
2. QwQ-32B上如果在LR中加入t/T作为控制变量，HS-text precision差异是否仍然显著？
3. R1-32B W=1 coverage 25%（5/20 traces）——报告这5条trace的precision值及其variance？
4. 论文使用单一数据集(HarmThoughts)，layer selection sensitivity结论对不同CP annotation protocol是否robust？
5. Appendix D提到的OT-7B "layer selection bug" 与Appendix F的M002 bug是同一个还是不同问题？

---

## Missing References（两位Reviewer共同确认）

1. "There Is More to Refusal in Large Language Models than a Single Direction" (2025, arXiv:2602.02132)
2. "The Geometry of Refusal: Concept Cones and Representational Independence" (ICML 2025)
3. "Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety" (2025, arXiv:2507.11473)
4. "Towards Fully Exploiting LLM Internal States to Enhance Safety" (ACL 2025)
5. "Large Reasoning Models Are Autonomous Jailbreak Agents" (Nature Communications 2025/2026)
6. "Safety Alignment Should Be Made More Than Skin-Deep" (ICLR 2025)
7. LEACE: Perfect Linear Concept Erasure (Belrose et al., 2023)
8. Amnesic Probing (Elazar et al., 2021)

---

## External Review (Stanford Agentic Reviewer)

未请求。

---

## Overall Assessment

**评分: 3.0 / 5 (Findings — 可被 Findings 接收)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Overall | 3.0 | 3.0 | 3.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**判断依据**：
- **Contribution 1（layer selection sensitivity）** 是真实的、有价值的方法论发现，足以支撑Findings论文。机制清晰，量化影响明确(5/12→12/12翻转)，对probing社区有警示价值。
- **Contribution 2（HS precision advantage）** 因维度混淆变量(N1)和QwQ position问题(N3)而证据力大幅削弱。修复方向明确（增加更强text encoder或PCA降维消融），但需要额外实验。
- **Contribution 3（negative results）** 有信息量但framing过度("all fail")需修正。
- 论文透明度、统计严谨性和实验覆盖度在同类工作中属上乘。
- 写作质量好，无AI痕迹，结构完整。

**可接收条件**：
- N1必须通过实验或framing调整解决（最低限度：将Contribution 2严格限定为"vs. 384d sentence encoder baseline"）
- N2和N3可通过framing调整解决（不需要新实验）
- W1-W6建议改进但非blocking

---

## Detailed Comments

### Abstract
- ~210 words，长度合理。
- "$n{=}19$--$47$ test traces; $n{=}19$--$20$ at 32B scale" 过细，建议删除内部引号。
- "all 12 Holm-Bonferroni-corrected hypothesis tests confirm significant HS superiority" 应改为 "HS probes significantly outperform text probes on all four models (Holm-Bonferroni corrected)"。
- 缺少对QwQ-32B检测时间劣势的一句限定。

### Introduction
- 5段结构完整，叙事连贯。
- Contribution 2 已含 "(against a 384-dimensional sentence encoder, all-MiniLM-L6-v2, as the text baseline)" qualifier，但在 "all 12 Holm-Bonferroni-corrected hypothesis tests" 部分仍暗示普适性。
- Contribution 3 "Seven alternative approaches ... all fail" 应改为 "produce inconsistent or limited results"。

### Method
- Section 3.3 layer selection sensitivity analysis清晰且有说服力。"complementary"比此前的"independent"准确。
- 仍需承认precision/FPR的数学相关性意味着"four metrics converge"的证据力弱于表面值。

### Experiments
- Table 2 (HS vs text)是核心表格，数据清晰。
- Section 5.4 (32B model-specific analysis)处理得当，但其nuance未充分反映到Abstract/Intro。
- Table 5 (negative results)布局较挤，可读性可改善。
- Section 5.3 caveats中"Fourth"的编号不连贯(前文仅有First, Second, Third标记)。

### Discussion
- Layer selection作为researcher degree of freedom的讨论有insight。
- Cross-model divergence分析是论文亮点之一。
- "Design implications"段正确声明了non-deployment qualifier。
- 泛化声称("any threshold-based study...")应降级为hypothesis。

### Limitations
- 覆盖6个主要局限，诚实全面。
- "Text encoder as baseline"段承认了N1的问题但仅以一段轻描带过，应更prominent。

### Appendix
- Bug disclosure (Appendix F) 值得赞赏。
- GRU details (Appendix D-E) 充分，但split不一致问题需更明确标注。
- BOCPD/CUSUM sweep (Appendix H) 仅R1-8B有详细表格，其他模型0%结果缺表格支持（已有文字说明配置范围）。
