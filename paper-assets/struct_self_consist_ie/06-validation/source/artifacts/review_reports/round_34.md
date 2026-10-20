---
round: 34
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T09:06:04.882696+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 34

**论文**: "Characterizing the Capability Ceiling of Self-Consistency: A Diagnostic Framework for Test-Time Aggregation in NER"
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**截止日期**: 2026-05-25
**审稿模式**: Fresh（重新审稿）
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作）

---

## Summary

本文研究 self-consistency（SC）在 NER 上的失效机制。通过四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression），系统性分析了为什么 quality estimation 信号能预测输出质量（Spearman ρ 最高 0.45, AUROC 0.82）但无法在 instance 级别选出更好的候选——即 "correlation-selection gap"。实验覆盖 4 个 NER 数据集、2 个模型族（Qwen3-8B, LLaMA-3.1-8B）、9 类方法。探索性的 entity-level construction 在低 degeneracy 条件下（Few-NERD）获得 +1.4 pp 增益，但效果不一致。degeneracy 阈值 θ_crit=0.70 预测 SC 增益何时消失。

---

## Strengths

**S1. 统计实践堪称模范。** [共识] 全面使用 bootstrap 95% CI、permutation test、TOST 等价检验、Holm-Bonferroni 多重比较校正（Table 12, k=57）、post-hoc power analysis。Table 12 的 57 项检验透明报告了全局校正下核心 claim 不达显著（p_HB=0.055），这种统计诚实在 NLP 论文中罕见。

**S2. 实验覆盖和附录深度。** [共识] 4 个 NER 数据集 × 2 模型族 × 9 方法类别 × 16+ 配置，39 页 Appendix 覆盖几乎所有可能的消融角度（温度、sample size、free-form decoding、cross-family、14B scale、epoch confound 等），几乎穷尽了 reviewer 可能提出的消融需求。

**S3. Correlation-selection gap 是有价值的诊断概念。** [共识] 将 quality estimation 与 selection 之间的脱节命名并系统量化，Figure 2 有效可视化了这一 gap。四阶段 cascade 的诊断逻辑清晰，每个阶段有可计算指标。

**S4. 清晰的 observational 定位和实用的负面结论。** [共识] Section 2 开头声明不做因果声明；Section 9 的 diagnostic cascade 提供了可操作的预部署决策树。

**S5. MBR 形式化连接。** Proposition 2 建立了 entity-level construction 与 balanced set-overlap utility 下 MBR 最优性的理论桥梁。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. 全局 Holm-Bonferroni (k=57) 下核心 NER claim 不显著，主文未充分讨论。** [R1 提出, R2 AGREE]
Table 12 显示全局校正下 p_HB=0.055，"no core NER claim survives"。正文使用 family-wise corrected p-values（较小的 k=10, 21, 9），但未在正文中明确告知读者全局校正结果——Appendix e 第 18 页报告了此事实，但作为影响核心结论可信度的关键信息，应在 Discussion 或 Limitations 中显著讨论。此外应为 family-wise 分组提供先验理由（基于研究问题独立性），并报告 BH FDR 作为补充。

**C2. 模型覆盖面不足以支撑跨规模/跨家族泛化声明。** [R1 提出, R2 AGREE]
主实验仅依赖 2 个 8B fine-tuned 模型（Qwen3-8B, LLaMA-3.1-8B）。GPT-5.5 仅 200 instances zero-shot；14B 仅 SciERC；72B 仅 zero-shot AWQ。Abstract/Introduction 声称 "treating NER as a representative instance of set-valued generation"、"the gap persists across scales and families"，但实际模型规模基本锁定在 7-8B，且 zero-shot vs fine-tuned 对比不对等。应限定 claim 范围为 "7-14B fine-tuned + selected zero-shot frontier models"。

**C3. Prescriptive 阶段薄弱，三阶段叙事不完整。** [双方 AGREE]
Introduction 承诺 "Discover → Diagnose → Prescribe" 叙事，但 Prescribe 阶段核心产物——entity-level construction——效果不一致（Few-NERD +1.4pp, CoNLL 负面, SciERC +0.2pp non-significant）。Abstract/Discussion 以 prescriptive 口吻呈现，Section 7.5 标记 "exploratory"——叙事矛盾。Discussion 结论本质是 "what NOT to do" 而非 "what to do"。应统一定位为 "exploratory with promising but inconsistent initial results"。

### Should-Fix（影响评分但不一票否决）

**W1. "Diagnostic Framework" 定位与实际贡献之间存在张力。** [R2 Must-Fix, R1 REBUT — 分歧未解决]
R2 认为 "framework" 需要跨任务通用性和预测能力，实际是 empirical study，建议改标题。R1 反驳称 Appendix ac 的 3-step protocol 使其超越典型 empirical study，"diagnostic framework" 基本成立。Director 判断：论文的 framework 定位有一定基础（诊断 protocol 可操作），但正文叙事偶尔超出诊断范畴，应更审慎。

**W2. 相对于 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的增量贡献界定不清。** [R2 Must-Fix, R1 REBUT — 分歧未解决]
R2 认为增量不够清晰。R1 提供了详细对比表（instance-level vs task-level, quantitative cascade vs qualitative failure modes, LP-weighted vs majority voting, agreement-quality alignment vs diversity）认为增量显著。Director 判断：增量存在但论文 Section 8 表述分散，缺少集中的 "What's new" 段落。

**W3. Free-form decoding 消融仅覆盖 SciERC，CoNLL/WNUT-17 缺失。** [R1 提出, R2 AGREE]
Constrained decoding 可能是 CoNLL 89% degeneracy 的重要驱动因素。如果 CoNLL free-form decoding 的 degeneracy 大幅下降，cascade 对 CoNLL 的诊断结论需修正为 "constrained decoding is the bottleneck" 而非 "SC intrinsically fails"。

**W4. 与 Yun et al. (2025) diversity collapse 关系讨论不充分。** [双方 AGREE]
Degeneracy 与 diversity collapse 的概念关系未深入讨论。Constrained decoding 可能同时驱动 diversity collapse 和 LP compression，但论文仅用一句话区分。需在 Discussion 增加 2-3 句讨论 constrained decoding 作为 confound。

**W5. θ_crit=0.70 缺少充分验证。** [R1 Must-Fix, R2 建议降级 — 分歧]
R1 认为 16 个配置点既拟合又验证，post-hoc fitting 风险。R2 认为 θ_crit 更像描述性发现，不需要 ML 级 held-out 验证，建议降级。Director 判断：降级为 Should-Fix，但需明确定位（descriptive vs normative）并报告 sensitivity sweep 或 LOO-CV。

**W6. 信息密度过高，首次阅读认知负荷极大。** [R2 提出, R1 AGREE]
几乎每个句子 2-3 个统计量，缩写过多（LP, SJ, FK, VC, EM, MV, QE, AUROC 等）。建议主文聚焦 top-level patterns，详细数字移入 Appendix。

**W7. Related Work 覆盖不足。** [双方 AGREE]
Snell et al. (2025) "Scaling LLM Test-Time Compute Optimally" 与 dataset-dependent optimal strategy 直接相关但未引用。Eikema et al. (2025) structure-conditional MBR 与 Proposition 2 的连接可深化。LLM calibration 文献（Kadavath et al. 2022, Tian et al. 2023）讨论不足。

**W8. RE/SQL 扩展太薄，"structured IE" 泛化措辞超出证据。** [双方 AGREE]
RE 仅 SciERC（397 instances, 40% zero F1），且 cascade 行为与 NER 显著不同。SQL 仅一句话提及（87.2% degeneracy）。标题准确限定为 NER，但 Abstract/Discussion 的 "structured IE/prediction" 措辞超出。

**W9. 2-seed vs 3-seed 不对称未说明。** [双方 AGREE]
Table 1 中 selection signals 使用 2-seed mean，baselines 使用 3-seed，正文未解释原因。

### Minor Issues

- **M1**: Figure 1 "diagnostic; not causal chain" 注释好，但箭头视觉暗示因果链，建议用虚线。[双方 AGREE]
- **M2**: 缩写表（Table 5, Appendix）建议以简化版放入主文。
- **M3**: Table 2 "Full coverage in Appendix h.4" 引用——主文缺少 9 类方法的数据集覆盖概览。
- **M4**: Table 65 cost-benefit analysis（p45）很有价值，建议在正文提及核心数字。
- **M5**: 引用括号格式一致性检查（Section 1 有混用）。
- **M6**: 匿名性无问题。Ethics Statement 和 Checklist 覆盖恰当。
- **M7**: 正文可能略微溢出 8 页——确认 camera-ready 严格控制。
- **M8**: Proposition 1/2 的 entity-wise independence 假设应在正文中更明确标注为 simplifying assumption。
- **M9**: Limitations 应补充 prompt sensitivity 未测试。

---

## Reviewer Consensus

以下问题双方达成共识 [AGREE]：

1. **统计实践是核心优势**——bootstrap CI、Holm-Bonferroni、permutation test 的组合使用是标杆级别
2. **Prescriptive 阶段薄弱**——entity-level construction 效果不一致，叙事应降级为 exploratory
3. **模型覆盖面不足**——泛化声明应限定为 7-14B fine-tuned regime
4. **全局统计校正透明度不足**——主文需讨论 k=57 结果
5. **Free-form decoding 消融缺失 CoNLL**——constrained decoding 可能放大 degeneracy
6. **Related Work 覆盖不足**——需补 Snell et al.、Eikema et al.、calibration 文献
7. **与 Yun et al. diversity collapse 关系需深化**
8. **2-seed/3-seed 差异需说明**

---

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | Director 判断 |
|------|---------|---------|---------------|
| Overall 评分 | 3.5 (Borderline Conference) | 3.0 (Findings) | 3.0 (Findings) |
| Framework 定位 | 基本成立（Appendix ac 3-step protocol）| 过高（应为 empirical study）| 有基础但叙事需审慎收敛 |
| 新颖性增量 | 显著（详细对比表）| 不够清晰 | 增量存在但论文表述分散 |
| θ_crit 严重性 | Must-Fix（post-hoc fitting）| Should-Fix（描述性发现）| Should-Fix + 需定位澄清 |
| CoNLL 高 degeneracy tautology | 非 tautological（cascade 排除了其他假设）| 部分 tautological | R1 论证更有说服力 |
| Cross-dataset power | Should-Fix | 领域固有限制 | Info 级，提及即可 |

---

## Questions for Authors

1. **CoNLL free-form decoding ablation**: 在 CoNLL 上进行 free-form decoding，degeneracy 率是否显著下降？如果下降，cascade 的 CoNLL 诊断结论是否需修正？
2. **全局 vs family-wise Holm-Bonferroni**: 按 BH FDR 校正，多少核心 NER claims 能在 FDR<0.05 下成立？
3. **θ_crit=0.70 LOO-CV**: 每个 fold 的 θ_crit 估计值变异范围是多少？
4. **GPT-5.5 sampling strategy**: 200-instance 的选择策略（random? stratified?）及完整结果分解？
5. **Degeneracy filtering + entity construction**: 仅对非 degenerate instances 做 construction，收益是否更大且更一致？

---

## Missing References

1. **Snell et al. (2025)** "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters" (ICLR 2025)——compute-optimal test-time scaling 策略，与 dataset-dependent optimal strategy 发现直接相关。[双方 AGREE 应引用]
2. **Eikema et al. (2025)** structure-conditional MBR——已引用但讨论不足，与 Proposition 2 的连接应深化。[双方 AGREE]

---

## External Review (Stanford Agentic Reviewer)

**状态**：pending（已于 2026-05-22T08:47 发送请求，尚未返回）。如用户收到外部审稿结果，将作为补充材料追加。

---

## Visual Layout Check（非评分项）

**状态**：Agent 超时（300s timeout）。未产出排版检查结果。用户可选择重新触发视觉审查。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**置信度**: 4/5

**评分理由**:

本文在 self-consistency 对 NER 的失效机制上提供了迄今最系统、最严谨的诊断分析，统计实践堪称模范，47 页的分析深度令人印象深刻。Correlation-selection gap 是有用的概念，四阶段 cascade 的诊断逻辑清晰。

评 Findings 而非 Conference 的核心原因：
1. **统计脆弱性**：核心 NER claim 在全局 Holm-Bonferroni (k=57) 下 p_HB=0.055，未达显著——family-wise 分组虽可辩护但主文透明度不足。
2. **Prescriptive arm 不完整**：entity-level construction 仅在 Few-NERD 有显著且一致的增益，三阶段叙事的 Prescribe 阶段无法支撑。
3. **泛化证据有限**：模型覆盖主要锁定在 8B fine-tuned，跨规模声明缺乏 ≥30B fine-tuned 证据；RE/SQL 扩展过于初步。
4. **定位-内容张力**："Diagnostic Framework" 定位有一定基础但超出了当前验证范围（跨任务通用性不足、formal 决策边界不完整）。

**提升路径**（如果 rebuttal/修改能回应以下问题，可升至 3.5 Borderline Conference）：
- 主文透明报告全局 Holm-Bonferroni + BH FDR 结果
- 统一 Prescriptive 叙事为 exploratory
- 限定 claim 范围（模型规模、任务泛化）
- Section 8 增加集中的增量贡献阐述
- CoNLL free-form ablation 或充分讨论 constrained decoding confound

---

## Detailed Comments

### Section 1 (Introduction)
- "Discover → Diagnose → Prescribe" 三阶段叙事中 Prescribe 阶段的承诺过高。建议调整为 "Discover → Diagnose → Explore bypasses"。
- 与 Yao et al. (2026)、Chen et al. (2024)、Xie et al. (2023)、Yun et al. (2025) 的差异化定位应前移到 Introduction，而非留到 Section 8。

### Section 2 (Diagnostic Framework)
- "Capability ceiling" 的 N≤16 定义较窄。R1 论证该概念不依赖固定 N（gap 随 N 增大而扩大），但正文定义与后续 N=32/64 实验存在张力。
- Experimental setup 概览应在此处或之后增加 1-2 段，帮助读者在遇到 Section 3-6 的实验数据时有上下文。

### Sections 3-4 (Mechanistic + Selection Gap)
- Introspection boundary 发现（ESJ AUROC 0.51 vs hidden-state probe 0.63-0.88）有趣但机制解释较浅。
- Table 1 的 2-seed/3-seed 差异需说明。
- Selection alignment α→0 是核心发现但叙事上被 degeneracy 讨论淹没——建议在 Section 4 更突出 α 的 binding constraint 角色。

### Section 5 (Adaptive Methods)
- Table 2（9 method categories）信息密集但缺少主文中的数据集覆盖概览。
- Cross-model ensemble（+0.42pp）仅在 Few-NERD 单数据集测试。

### Section 6 (Theory/Scaling)
- Proposition 1 应更明确标注为 descriptive formalization。Proposition 2 的 MBR 连接是更实质性的理论贡献。
- Inverse scaling under adaptive thresholds 的发现（40/58 transitions 变差）重要但讨论偏技术，实践含义可更直接。

### Section 7 (Experiments)
- 实验设置在 Section 7.1 出现较晚——读者已在 Sections 3-6 消化了大量结果。
- Few-NERD 3 epochs vs others 5 epochs 的混淆需更显著讨论（不仅在 Appendix ab）。

### Section 8 (Related Work)
- 缺少与 Snell et al. (2025) compute-optimal scaling 的对比。
- 与 Yun et al. (2025) 的关系需从 1 句扩展到 1 段——特别是 constrained decoding 作为共同 confound。
- 建议增加集中的 "What's new" 对比段落。

### Section 9 (Discussion and Conclusion)
- 结论本质是 diagnostic（"when not to use SC"）而非 prescriptive。建议与 Introduction 的叙事对齐。
- Practical implications 段落有价值，可考虑增加 cost-benefit 数字（Table 65）。

### Limitations
- 覆盖较好但遗漏：(a) prompt sensitivity 未测试；(b) 仅 8B fine-tuned 主实验，larger model fine-tuned 行为未知。
- 全局 Holm-Bonferroni 下核心 claim 脆弱性应在此处或 Discussion 讨论。

### Appendix
- 极其详尽，几乎所有主文 claim 有对应消融。Appendix ac 的 3-step evaluation protocol 有实用价值。
- Table 65 cost-benefit analysis 建议提升到正文。