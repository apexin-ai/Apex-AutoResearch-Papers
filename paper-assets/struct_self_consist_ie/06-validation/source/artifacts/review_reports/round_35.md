---
round: 35
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T10:30:31.440156+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 35 (Fresh Review)

**论文**: When Does Test-Time Scaling Fail? Boundary Conditions for Structured Prediction
**Venue**: EMNLP 2026 via ARR May 2026 (Deadline: 2026-05-25)
**审稿模式**: Fresh（全新初审）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮达成）

---

## Summary

论文研究 test-time compute scaling（self-consistency、best-of-N）在结构化预测上的失败条件，以 NER（4 个数据集）和 RE（exploratory）为案例。核心发现 **correlation-selection gap**：质量估计信号能有效预测输出质量（AUROC 最高 0.82），但 instance-level selection 始终无法超越 greedy decoding（gain < 1pp，N=64）。诊断 cascade 将失败定位到两个 boundary conditions：output convergence（degeneracy 12-68%）和 signal alignment collapse（α→0）。Exploratory entity-level construction 在低 degeneracy 条件下部分绕过瓶颈（+1.40pp on Few-NERD）。

---

## Strengths

**S1** [R1+R2 共识] **统计方法论显著超越 NLP 论文平均水平**。Holm-Bonferroni 全局校正（k=57）、MDE 分析、TOST equivalence testing、bootstrap CI、permutation tests 的组合使用在 NLP 经验性论文中极为罕见，为实证分析设立了高标准。

**S2** [R1+R2 共识] **Correlation-selection gap 是一个真正有价值的经验贡献**。将 "QE 信号有效" 与 "selection 成功" 解耦，命名并系统量化了此前文献中未被清晰表述的现象。Figure 1 的可视化清晰传达了核心 insight。

**S3** [R1+R2 共识] **Diagnostic cascade 概念清晰且实用**。四阶段诊断（degeneracy → oracle headroom → LP compression → signal alignment）逻辑自洽，每个阶段有可操作的度量。Appendix ae 的三步评估协议对社区有直接实用价值。

**S4** [R1+R2 共识] **异常详尽的消融和 robustness 分析**（47 页附录）。覆盖 temperature、sample size scaling、epoch、LoRA rank、cross-model transfer、OOD、free-form decoding、thinking tokens、entity-level LP decomposition、construction threshold sensitivity 等。

**S5** [R1+R2 共识] **诚实报告负面和有限结果**。MDE 分析坦承 "absence of evidence, not evidence of absence"；bypass 策略效果如实呈现（cross-model +0.42pp, entity construction +1.4pp），未过度渲染。

**S6** [R1] **Failure mode gallery**（Appendix ag）提供 9 个具体失败案例的质性分析，直观展示三类典型错误模式，有教学价值。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [R1+R2 共识, Critical] **Scope overclaim：标题声称 "Structured Prediction" 但证据主要是 NER。**
标题 "Boundary Conditions for Structured Prediction" 设定了远超实验覆盖的验证门槛。充分实验仅 NER（4 数据集 × 2 模型家族）。RE 仅 SciERC 单数据集 exploratory 扩展（Appendix o, 397 实例, 1 模型），SQL 仅一句话提及 87.2% degeneracy。NER entity-set（无序集合）与 dependency parsing（树结构）、SRL（predicate-argument）、event extraction（嵌套结构）的输出空间结构差异巨大——degeneracy 和 alignment collapse 的表现形式可能完全不同。Discussion (p.8) 自承 "generalization to other structured tasks requires further investigation"，与标题的强 claim 形成内在矛盾。
→ **建议**：(a) 限缩标题为 NER/IE（如 "Boundary Conditions for Entity Recognition"）；或 (b) 补充至少一个完整的非 NER 结构化预测任务的 cascade 分析。

**N2** [R1 Critical, R2 Should-Fix, 分歧] **SciERC 仅 1 个 training seed，统计可靠性不足。**
SciERC 是论文中分析最详尽的数据集（Figure 2 LP compression、entity-level probe、calibration analysis、free-form ablation 都以 SciERC 为 primary showcase），但仅用 1 个 training seed（seed=42），测试集仅 529 实例。论文自承 σ=0.48pp。Few-NERD 和 CoNLL 使用 3 seeds，SciERC 为何只用 1 seed 未解释。R1 认为 critical（核心发现可能不稳定），R2 认为 should-fix（核心结论由 3-seed Few-NERD/CoNLL 支撑，SciERC 更多是补充验证）。
→ **建议**：补充 SciERC 2 个额外 training seeds（1861 train sentences，训练成本可控）；若不可行，在主文明确标记 SciERC 相关结论为 tentative。

### Should-Fix（影响评分但不一票否决）

**W1** [R2 提出, R1 确认] **正文可能超出 8 页限制。** Section 9 (Discussion and Conclusion) 结论段落溢出到 Page 9 顶部。EMNLP 2026 规则：正文 8 页，Limitations/Ethics 不计入。需压缩 Related Work 或 Discussion。

**W2** [R1+R2 共识] **Capability-diversity tension 作为 central finding 缺乏形式化。** 论文将此呈现为 central finding（Section 9），但缺乏可操作定义。Figure 3 仅展示 3 个数据集的 MV ΔF1 趋势，且 CoNLL N=64 时 MV gain 为正（+0.6pp），与 tension 叙事部分矛盾。R1 认为 structured output 上的量化分析是新的，但同意形式化不足。R2 认为文献已有隐含讨论（Snell et al. 2025, Brown et al. 2024）。
→ **建议**：给出可测量定义（如 degeneracy vs base F1 的函数关系），或降级为 observed pattern。

**W3** [R1+R2 共识] **与 Yun & Price (2025) 差异化论述不充分。** "Signal alignment collapse" 与 "format diversity collapse" 语义高度重叠。Section 8 仅一句话带过差异。需 1-2 段明确对比两个概念的定义级区别及诊断 cascade 的增量信息。

**W4** [R2 提出, R1 部分同意] **相关工作缺少重要领域。** 缺失：conformal prediction for NLP structured outputs、token-level uncertainty decomposition（Xiao et al. 2020）、MBR with entity-level F1 utility function（概念上即 entity construction 的 principled 版本）。R1 同意 conformal prediction 和 token-level 相关，认为 active learning 关联较弱。

**W5** [R1+R2 共识] **Proposition 1 entity independence 假设与数据不符。** Split-half r=0.578-0.644 违反 independence 假设。Table 31 bound ratio 0.13-0.63 证实 bound 过松。R1 认为定性方向仍成立（高 degeneracy → MV 无法改善），R2 建议降格为 illustrative bound。
→ **建议**：提供 correlated entity（3-12% correlation）下 bound 偏移的数值分析，或明确降格。

**W6** [R1+R2 共识] **Free-form decoding ablation 覆盖不全。** 仅 SciERC + CoNLL。Few-NERD（degeneracy 最低 12%）是最应验证的数据集——若 free-form 下 degeneracy 不变，强化 "model-intrinsic" 论点；若显著下降，cascade 结论需重新解读。

**W7** [R2 提出, R1 同意] **诊断 cascade 阈值的 task-specificity 未讨论。** Degeneracy >30%、α<0.05 等阈值在不同 task 上是否稳定？已观察到 task 差异大（SciERC 12% vs WNUT-17 67.9% degeneracy），需明确说明。

---

## Reviewer Consensus [AGREE]

1. **Scope overclaim 是最严重的问题**：两位 Reviewer 独立提出且交叉确认，NER 证据不能支撑 "structured prediction" 的标题
2. **Correlation-selection gap 是最有价值的贡献**：命名并量化了此前未被清晰表述的现象
3. **统计方法论达到高标准**：Holm-Bonferroni k=57、MDE、TOST 组合使用远超同行
4. **Entity independence 假设需要更透明的讨论**：bound 过松但定性方向成立
5. **Capability-diversity tension 形式化不足**：需要可操作定义或降级 framing
6. **Free-form ablation 需要覆盖 Few-NERD**
7. **正文页数超限需修复**（格式合规）

## Reviewer Divergence [REBUT]

1. **SciERC 单 seed 严重程度**：R1 认为 Critical Must-Fix（核心发现可能不稳定），R2 认为 Should-Fix（核心结论由 3-seed Few-NERD/CoNLL 支撑）。**Director 判断**：列为 Must-Fix 但允许 camera-ready 补充，不一票否决。

2. **方法对比公平性**（R1-W2）：R2 反驳——论文论点是 "所有方法 gain 都小"，不是 iso-compute 竞赛。**Director 判断**：R2 论点更强，降级为小问题（建议 Table 2 caption 标注 compute cost）。

3. **Greedy baseline 选择**（R1-W3）：R2 反驳——greedy 是 test-time scaling 文献标准 baseline（Snell et al. 2025, Wang et al. 2023, Brown et al. 2024）。**Director 判断**：R2 论点成立，不构成问题。

4. **Capability-diversity tension 新颖性**：R1 认为 structured output 量化是新的，R2 认为增量有限。**Director 判断**：作为经验观察有价值，但不应 framed 为 central finding——Should-Fix。

---

## Questions

**Q1** [R2] Correlation-selection gap 是否在任何非 NER 结构化预测任务中被验证过？

**Q2** [R2] 为何没有直接实验 entity-level F1 作为 MBR utility function 的方案？概念上比 majority vote 更 principled。

**Q3** [R2] Proposition 1 bound ratio 仅 0.13-0.63——是否考虑过基于 partial degeneracy 的连续 bound？

**Q4** [R2] Figure 3 中 Few-NERD N=64 仍有正向增益，SciERC 几乎平坦——是否主要由 base model quality 驱动？更弱模型（3B/1B）是否会有更大 scaling gains？

**Q5** [R1] SciERC 为何只用 1 个 training seed？是资源限制还是其他原因？

---

## Missing References

- Conformal prediction for NLP structured outputs（近年多项工作将 conformal prediction 应用于 NER/序列标注的 uncertainty quantification）
- Token-level uncertainty decomposition（如 Xiao et al. 2020 epistemic/aleatoric 分解）
- Snell et al. (2025, ICLR) compute-optimal scaling 中关于 diminishing returns 的讨论
- Entity-level F1 作为 MBR utility function 的 principled 版本（vs 当前的 majority vote）

---

## External Review (Stanford Agentic Reviewer)

未启用。项目配置中 `external_review.paperreview_ai.enabled` 未设置为 true。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时约 4 分钟）

| 严重度 | 位置 | 发现 |
|--------|------|------|
| warning | p.24 | 附录页面约 2/3 空白（Appendix n 结尾），建议调整 float/section break |
| warning | p.17 | Figure 7 热力图使用红→绿色阶，对红绿色盲不友好，建议改 viridis 或 Blue→Orange |
| warning | p.16 | Figure 6 校准图同样存在色盲友好性问题 |
| warning | p.7 | 主文单页密度极高（Table 3 + Table 4 + Figure 4 + 两段文字），视觉上略拥挤 |
| info | p.1 | 首页无视觉锚点，Figure 1 在 p.2，延迟可控 |
| info | p.3 | 唯一纯文本页（信号定义），建议加小型 signal summary 表 |
| info | p.14-47 | 附录 34 页极为详尽，关键附录建议主文显式指引 |
| info | p.5 | Table 2 信息密度高但格式正确 |
| info | p.6 | Figure 3 色彩区分度良好且色盲友好 |
| info | p.47 | 末页空间利用合理（~85%） |

无 critical 排版问题。色盲友好性（Figure 6, 7）建议修复。

---

## Overall Assessment

**评分**: **3.5 — Borderline Conference**
**置信度**: 4/5（两位 Reviewer 均熟悉 self-consistency 和 NER 领域文献）

### 评分理由

**支持 Conference (4.0) 的因素**：
- Correlation-selection gap 是社区有价值的经验发现，命名并量化了此前模糊的现象
- 诊断 cascade 有独立方法论价值，附带可复用的三步评估协议
- 统计方法论（Holm-Bonferroni k=57、MDE、TOST）在 NLP 经验性论文中属上乘
- 47 页附录体现极致的 thoroughness，几乎覆盖所有可预见的 reviewer 质疑
- 诚实报告负面结果和方法局限性

**限制 Conference 的因素**：
- **[Critical]** 标题/Abstract 声称 "structured prediction" 但证据主要是 NER——scope-evidence gap 是最大问题
- SciERC（最核心数据集）仅 1 training seed，统计可靠性不足
- Capability-diversity tension 作为 central finding 形式化不足，且文献中已有隐含讨论
- 核心贡献是诊断性的（"what fails"）而非建设性的（"how to fix"），prescriptive guidance 有限
- Proposition 1 的理论贡献偏薄（independence 假设不成立，bound 过松）

### 改进路径（Conference 4.0 所需）

若作者能在 camera-ready 中完成以下修改，论文可达 Conference 水平：
1. **[必须]** 限缩标题和 Abstract scope 为 NER/Information Extraction
2. **[必须]** 补充 SciERC 多 seed 实验（或标记为 tentative）
3. **[必须]** 修复页数溢出（压缩至 8 页正文）
4. **[强烈建议]** 加强与 Yun & Price (2025) 的差异化论述
5. **[建议]** 降级 capability-diversity tension 的 framing 或给出可操作定义

当前版本适合 **Findings (3.0-3.5)**；scope 修正后为 **Borderline Conference (3.5-4.0)**。

---

## Detailed Comments

### Section-by-Section

**Abstract**: 第一句 "structured prediction remains uncharacterized" 过强，实际只 characterize 了 NER（和初步 RE）。建议改为 "entity-level information extraction" 或 "set-valued NER outputs"。"Exploratory entity-level construction partially bypasses" 中 "partially" 用词准确。

**Section 1 (Introduction)**: Discover → Diagnose → Explore bypasses 三阶段叙事清晰。但 "using NER...and RE as case studies" 中 RE 的篇幅远不能称为 case study（Appendix 2 段 vs NER 的完整 pipeline）。

**Section 2 (Diagnostic Framework)**: 五种信号的定义清晰。SJ 引用 Fleiss 1971 可能有误（Fleiss 是 inter-rater reliability，非 Soft Jaccard 来源）。Table 5 术语不一致（"Soft Jaccard" vs "structural similarity"）。建议 p.3 加小型 signal summary 表改善可浏览性。

**Section 3 (How Self-Verification Fails)**: Introspection boundary 是有趣概念但后续很少复用——考虑去掉以减少 cognitive load，或在 Discussion 中回顾。

**Section 4 (Where Single-Signal Selection Fails)**: 核心 section。Figure 2 双量纲共轴（AUROC vs ρ）初看混淆，建议分双轴。Table 1 caption "paired bootstrap" 但内容是 Spearman ρ，可能有误。

**Section 5 (Adaptive Methods)**: Table 2 信息密度高。建议添加 compute cost 列（各方法相对于 greedy 的倍数），避免误导为等预算比较。

**Section 6 (Threshold Regime Analysis)**: Proposition 1 的 "entity selection diagnostic" 方向性有用，但应在正文中明确标记为 illustrative upper bound（当前表述可能让读者误以为是 tight bound）。θ_crit=0.70 的 task-specificity 应讨论。

**Section 7 (Experiments)**: 详尽。Few-NERD LP selection +1.39pp (p<0.001) 是论文最强的正面结果。Table 4 的 "2-seed" vs Section 7.1 "3-seed" 不一致应修复。

**Section 8 (Related Work)**: 需扩展：补充 conformal prediction、token-level uncertainty、MBR with structural utility。与 Yun & Price (2025) 的差异化需从一句话扩展为 1-2 段。

**Section 9 (Discussion and Conclusion)**: "Central finding is a capability-diversity tension" 需更强支撑或降级。Conclusion 段落溢出到 p.9——必须压缩。

**Limitations**: 覆盖面广（correlational vs interventional、scope、seed、prompt template）。建议明确提及为何 SciERC 只用 1 seed。

**Ethics Statement**: 基本合规。论文脚注已注明 "No new human data was collected"。