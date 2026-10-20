---
round: 19
overall_score: borderline
timestamp: 2026-05-18T06:16:23.673882+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿报告 — Round 1

**论文**: Strong Predictors, Weak Selectors: Why Confidence Signals Fail to Scale Structured Information Extraction
**Venue**: EMNLP 2026 Main Conference (ACL Rolling Review)
**审稿人**: Reviewer 1 (方法严谨性 + 实验设计), Reviewer 2 (新颖性 + 完整性)
**轮次**: Round 1（1 轮独立审稿 + 1 轮交叉分享，达成收敛）

---

## Summary

本文评估五种置信度信号（四种 instance-level：SJ/VC/FK/EM，一种 per-sample：LP）在 LLM-based NER 中的质量估计（QE）和样本选择（selection）效果。核心发现是 "correlation-selection gap"：所有信号均实现可靠 QE（ρ up to 0.45, AUROC up to 0.82），但几乎无法超越 greedy decoding 进行选择。LP 仅在 Few-NERD 上实现显著选择增益（+1.36pp），需两个条件同时满足（低 degeneracy + 足够 LP-quality alignment）。论文诊断了两个阻断机制：instance degeneracy 和 weak LP-quality alignment。

---

## Strengths

**S1 [共识]. QE 与 selection 的系统性分离。** 先前工作常将"信号与质量相关"等同于"信号可用于选择"，本文严格证明这一等价关系不成立。这是有价值的方法论贡献。

**S2 [共识]. 统计方法论远超同类工作。** Bootstrap CIs、TOST equivalence testing、MDE 计算、Bonferroni correction、Fisher combined p-values、external equivalence margins 构成罕见的完整统计分析框架。

**S3 [共识]. 极高的实验透明度。** 几乎每一个有争议的设计选择都被主动标注并讨论：epoch confound、thinking token confound、ε post-hoc 性质、per-entity-type non-independence、LoRA-rank capacity confound。

**S4 [共识]. 附录深度令人印象深刻。** 14+ appendix sections 覆盖了几乎所有可预见的 reviewer 质疑，1353 行 appendix 体现了负责任的学术写作。

**S5 [共识]. 写作质量优秀，AI 痕迹极少。** 无 em-dash/en-dash 解释性使用，无黑名单用词，无 Furthermore/Moreover 堆砌。

**S6 [共识]. 引用完整。** 60 条 bib entry 全部被引用，0 orphan、0 missing（少数缺失见 Missing References 部分）。

**S7 [R1]. 多层次证据三角验证。** Temperature ablation、LoRA-rank ablation、cross-dataset gradient、per-entity-type analysis、epoch curve 构成 converging evidence。

**S8 [R1]. Few-NERD 的正面结果 well-powered。** n=32,565, CI [+1.18, +1.53]，是 convincing evidence that LP selection CAN work under specific conditions。

---

## Weaknesses

### Critical（影响接收决定）

**C1 [共识: R1-W1 + R2-W3]. Epoch confound 污染核心 cross-dataset comparison。**
Few-NERD 使用 3 epochs（其他数据集 5 epochs），是论文中唯一正面结果的来源。Table 4 的 cross-dataset gradient 是 training duration 和 dataset property 的混淆效应。Appendix N 显示 Few-NERD 5-epoch LP gains 从 +1.37pp 降至 +0.62pp。SciERC 3-epoch（degeneracy 6.4%, LP Δ=-1.18pp）与"low degeneracy → LP works"的简单叙事矛盾。主文叙事未充分调整。
→ **要求**: 在 Table 4 旁标注 training epochs 差异；加入 matched-epoch 对比行或在主文明确承认 confound 影响并降低 claim 强度。

**C2 [共识: R1-W2 + R2-W1]. "Two jointly necessary conditions" 因果 claim 过强。**
"Jointly necessary" 是强因果声明，但证据是 observational。Temperature ablation 只操纵了 degeneracy，alignment 是被动观察的。SciERC 3-epoch（ρ=0.317 > 建议 threshold ρ≳0.3, degeneracy 6.4% < 15%, 但 LP 仍为负）是潜在反例。"Two necessary conditions" 框架在实用层面等价于"在标注数据上跑一次看看"，缺乏 a priori 预测力。
→ **要求**: 改为 "jointly associated with" 或 "both appear required in the regimes we tested"；在主文讨论 SciERC 3-epoch 边界情况；ρ≳0.3 标注为 approximate data-driven threshold。

**C3 [共识: R2-N1, R1 AGREE]. Contribution 1 中 "methodological premise" 是定义推论，非实验发现。**
Instance-level signal 无法区分 per-sample candidates 是信号定义的直接推论。将此列为 Contribution 1 的一部分 inflates 贡献清单。该观察在论文中被重复四次（Abstract, §1, §2.1, §4.3），加重 inflation 感。
→ **要求**: 降级为 §2.1 的 framing remark，从 Contribution 列表移除。

**C4 [R2-N2, R1 部分 REBUT]. "Correlation-selection gap" 与 MBR 文献的差异化定位不足。**
Eikema et al. (2025) 诊断 utility misalignment，本文诊断 degeneracy。R1 指出论文在 Related Work 已有区分（"our diagnosis is complementary: degeneracy, not utility misalignment, is the primary bottleneck"），且 non-degenerate instances 上 MBR utility 与 F1 的 median ρ=0.524 提供了实质证据。但该区分在 Introduction 中不够醒目。
→ **要求**: 在 Introduction 中显著写出与 Eikema et al. 的区别（utility misalignment vs degeneracy），而非仅留在 Related Work。

**C5 [R2-N2, R2-N3]. 任务和模型覆盖面不足。**
Title 使用 "Structured Information Extraction" 但实验仅覆盖 flat NER + single-dataset exploratory RE。模型规模限于 3B-8B，70B+ 行为未知。
→ **要求**: 缩窄 title 和 claims 为 "Named Entity Recognition" 或 "Entity-level IE"；或增加非 NER 任务的完整实验。模型规模 limitation 应更显著讨论。

### Warning（影响评分但非一票否决）

**W1 [R1-W3]. 2-seed 实验设计统计效力不足。**
Table 3 使用 2-seed 平均，无法估计 cross-seed variance。建议至少对 primary selection comparison 补充 3-seed 数据。

**W2 [共识: R1-W4 + R2-Q4]. Per-entity-type 分析 non-independence 未量化。**
8 entity types 共享模型/tokenizer/temperature，effective df 可能远低于 6，p=0.004 可能不可靠。建议报告 ICC 估计 effective df 并考虑 permutation test。

**W3 [共识: R1-W5 + R2-Q3]. "Supervised verifier baseline" framing 误导。**
实际只是对 5 个 unsupervised signals 的 supervised combination，非 Cobbe et al. 意义上的 verifier。建议改名为 "supervised signal combination"。

**W4 [共识: R2-W2 + R1 AGREE]. Actionable contribution 偏薄。**
对不满足条件的场景 actionable advice 等于 "use greedy decoding"。Discussion 中 "Closing the gap" 讨论过于泛泛。建议增加 forward-looking analysis（hidden state verifiers 可行性、inference cost 分析等）。

**W5 [R2-W2-baseline]. 缺少重要 baseline signals。**
未测试 P(True)、Self-Certainty 作为 per-sample selection signal；hidden-state-based signals 仅标为 future work。建议至少增加 Self-Certainty。

**W6 [共识: R1-交叉补充 + R2-W4]. RE extension 定位模糊。**
RE 仅单 benchmark + 单 model，标为 "preliminary"，但正文多处引用 RE 结果支撑 general claims。建议将 RE 引用严格限制在 appendix 或增加更多 benchmarks。

### Info（小问题）

**I1 [共识]. Abstract 数字过载（8+ 定量值），建议精简至 ≤3 个关键数字。**

**I2 [共识]. 核心发现数字在 Abstract/Intro/Experiments/Discussion/Conclusion 中几乎逐字重复，浪费空间。**

**I3 [共识]. Discussion 7 个独立段落过于碎片化，建议合并相关主题为 subsections。**

**I4 [R1-W6]. Degeneracy 操作性定义需在主文区分 output degeneracy vs F1 degeneracy（Table 8: "Identical outputs"=11% vs "Constant F1"=17.8%）。**

**I5 [共识: R1-W7 + R2-minor]. SciERC greedy F1 跨 table 数值不一致（0.645/0.644/0.640），建议统一或声明 canonical protocol。**

**I6 [R2-minor]. Table 3 caption 中 split footnote 不优雅。**

**I7 [R2-minor]. Conclusion 最后两句结构松散，与 Limitations 重复。**

**I8 [R1-M3]. Table 3 的 EM/VC 没有报告 p-values（标注为 "---"），应标注为 "< greedy" 或给出实际值。**

**I9 [R1-M4]. Kendall's W=1.0 基于 m=3 raters，statistical precision limited，应更显著标注。**

---

## Reviewer Consensus

以下问题两位 Reviewer 达成完全一致：
1. Epoch confound 是真实问题，需在主文处理 [C1]
2. "Jointly necessary" 因果 claim 过强 [C2]
3. Contribution 1 的 definitional observation 不应列为贡献 [C3]
4. "Supervised verifier" 命名误导 [W3]
5. Actionable contribution 偏薄 [W4]
6. Abstract 数字过载 + 核心数字重复过多 [I1, I2]
7. Discussion 碎片化 [I3]
8. QE vs selection 分离是有价值的方法论贡献 [S1]
9. 统计方法论和附录深度远超同类工作 [S2, S4]

---

## Reviewer Divergence

**分歧 1: Overall 评分 (R1: 3.5/5 vs R2: 2.5/5)**
- R1 从方法论严谨性视角出发，认为实验深度和统计质量本身构成重要贡献，修复 claim 强度和 epoch confound 后可达 main conference 水平。
- R2 从 novelty 视角出发，认为核心发现（instance-level signals 无法 rank candidates）可从第一性原理推导，LP compression 虽有诊断价值但被包装在浅层 "gap" 框架中。
- **Director 判断**: 分歧反映了不同评审标准（experimental rigor vs conceptual novelty）的权衡，两种立场均合理。论文的实验执行确实远超平均水平，但 novelty concern 也是实质性的。

**分歧 2: Excitement (R1: 3.5/5 vs R2: 2/5)**
- R1 认为 QE vs selection 分离对 test-time scaling 社区有直接启示。
- R2 认为 surprise factor 有限，正面发现过小且 dataset-specific。
- **Director 判断**: R2 的 excitement 评分偏低。QE-selection 分离虽非 revolutionary，但对该领域的隐含假设（"correlation implies selection utility"）提供了系统性 falsification，价值高于 R2 评估。但 R2 关于任务覆盖面和正面发现偏弱的关切也是实质性的。

**分歧 3: Novelty 与 MBR 文献的关系**
- R1 [REBUT]: 论文诊断的是 degeneracy（candidate pool 缺乏方差），而非 utility misalignment（Eikema et al.），有实质区别。Non-degenerate instances 上 ρ=0.524 提供了证据。
- R2: 核心概念仍是已知结论的 domain-specific 重述。
- **Director 判断**: R1 的反驳有证据支撑。degeneracy vs utility misalignment 是不同的失败模式。但论文在 Introduction 中对此区分的表达确实不够锐利。

**分歧 4: 任务/模型覆盖面 (仅 R2 提出)**
- R2 将 N2（任务覆盖）和 N3（模型规模）列为 critical。
- R1 未提出这些问题。
- **Director 判断**: N2（title overclaim）是合理的——"Structured Information Extraction" 确实超出了仅 NER 的实验覆盖。N3（模型规模）是合理的 limitation，但将其列为 critical 过严——4B-8B fine-tuned models 是当前 production NER 的主流部署方式之一。建议将 N2 作为 must-address（缩窄 title），N3 作为 should-discuss（在 Limitations 中更显著讨论）。

---

## Questions

**Q1 [R1].** SciERC 3-epoch 的 within-instance alignment ρ=0.317 略高于建议 threshold ρ≳0.3，但 LP Δ=-1.18pp。Threshold 是否应该更高？还是 SciERC 存在 dataset-specific factors？

**Q2 [R1].** Few-NERD INTRA coarse setting（8 types）。Fine-grained types 下 LP selection 是否仍然有效？

**Q3 [R1].** Greedy decoding (T=0) 作为 selection baseline 是否太弱？Beam search 或 top-k sampling 对比如何？

**Q4 [R1].** Entity-token LP 的高 variance + 低性能是否说明 fine-tuned models 在 representation level 上 near-deterministic？对 learned verifier 可行性意味着什么？

**Q5 [R1].** Table 12 N-scaling: N=8→32 LP Δ 从 +0.39pp→+0.95pp (p=0.091)。外推到 N=64/128 是否可能达显著？LP selection 在 SciERC 上是 underpowered 还是 fundamentally limited？

**Q6 [R2].** 是否分析过 SciERC 的 per-entity-type LP selection heterogeneity？

**Q7 [R1].** Free-form ablation 对 NER 无效但对 RE 恢复了 selection (+1.8pp)，NER/RE 分歧的原因是什么？

---

## Missing References

**两位 Reviewer 共同推荐（应引用）：**
- Geifman & El-Yaniv (2017). "Selective Classification for Deep Neural Networks." NeurIPS. — selective prediction 直接相关。
- XGrammar — 论文实际使用的 constrained decoding engine，应被引用。

**R1 推荐（建议引用）：**
- Lin et al. (2024). "Generating Confidence from LLMs." ACL 2024.
- Lafferty, McCallum, & Pereira (2001). CRFs.

**R2 推荐（建议引用）：**
- Varshney et al. (2022). "Investigating Selective Prediction Approaches." — selective prediction across tasks.
- Cheng & Vlachos (2023). "Faster Minimum Bayes Risk Decoding with Confidence-based Pruning."

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。项目配置中未启用外部审稿。

---

## Overall Assessment

### 综合评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
| Excitement | 3.5/5 | 2/5 | **2.75/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Confidence | 4/5 | 4/5 | **4/5** |
| **Overall** | **3.5/5** | **2.5/5** | **3/5** |

### Overall: 3/5 — Borderline (Findings 可接收, Main Conference 需修改)

**一句话总结**: 实验执行和统计方法论远超平均水平（top 10% thoroughness），QE vs selection 的系统性分离是有价值的方法论贡献，但核心因果 claim 过强于证据（epoch confound + observational evidence）、Contribution 1 包含定义推论 inflation、任务覆盖不足以支撑 title、actionable contribution 偏薄。

### 路径建议

**通往 Main Conference (需全部满足):**
1. 修复 epoch confound 处理：主文承认 + matched-epoch 数据或降低 claim 强度
2. 弱化因果 claim："jointly necessary" → "jointly associated"
3. 缩窄 title："Structured IE" → "NER" 或 "Entity-level IE"
4. 锐化与 Eikema et al. 的差异化定位（Introduction 中醒目展示）
5. 降级 Contribution 1 的 definitional observation
6. 增加 forward-looking analysis（超越 "use greedy decoding"）
7. 精简重复内容，释放空间用于更深入的 Discussion

**当前状态**: Findings track 可接收。若能完成上述 1-5 项修改，有望达到 Main Conference borderline accept。

---

## Detailed Comments

### Abstract
- 8+ 定量值过多，建议精简至 ≤3 个关键数字
- "jointly necessary" 应弱化为 "jointly associated"
- "A methodological premise underlies both" 是定义推论，在 Abstract 中不应给予 contribution 级别的 emphasis

### Introduction (§1)
- Contribution 1 的 "definitional observation" 应降级
- 与 Yao et al. (2026) 的对比缺少 hard-prompted vs fine-tuned 的差异说明
- 与 Eikema et al. (2025) 的差异化定位需更锐利
- "Structured Information Extraction" overclaims 实验覆盖

### Method (§3)
- §3.1 需明确区分 output degeneracy vs F1 degeneracy
- Fleiss' κ adaptation 到 entity sets 缺少 validity 论证（独立性假设违反）

### Experiments (§4)
- Table 4 需标注 training epochs 差异
- 2-seed design 的 cross-seed uncertainty 未量化
- Per-entity-type analysis: 报告 ICC, 考虑 permutation test
- Table 3 EM/VC 缺 p-values
- SciERC greedy F1 跨 table 不一致

### Discussion (§5)
- 7 个独立段落过于碎片化，建议合并
- "Practical guidelines" 与 "Implications for practitioners" 重叠
- "Supervised verifier baseline" 应改名
- Forward-looking analysis 需要更具体（hidden state verifiers 可行性、inference cost）
- Free-form ablation NER/RE 分歧未解释

### Conclusion (§7)
- 最后两句与 Limitations 重复
- 核心数字不必逐字重复

### References
- 缺 XGrammar, Geifman & El-Yaniv (2017)
- 3 entries (hobelsberger2025systematic, lightman2024verify, venktesh2025trust) 需验证准确性
