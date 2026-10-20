---
round: 30
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T17:17:03.954265+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 30 (Fresh Review)

**论文**: "Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER"
**Venue**: EMNLP 2026 (Long Paper, ARR)
**截止日期**: 2026-05-25
**Reviewer 编排**: 2 人（R1: 方法严谨性/实验设计/统计分析; R2: 新颖性/framing/完整性/Related Work）
**审稿模式**: Fresh（无历史上下文）

---

## Summary

本文系统研究 NER 中 entity-level self-consistency signals 的能力边界。核心发现：agreement-based signals 能估计输出质量（Spearman ρ up to 0.47, AUROC up to 0.82）但无法用于 sample selection（所有 signal 均不优于 greedy decoding），称为 "correlation-selection gap"。论文提出四阶段诊断 cascade（QE → degeneracy → agreement fidelity → LP compression）定位失败原因，建立 MBR decoding 理论联系（Proposition 1），并给出三条绕过路径（LP selection +1.39pp, entity construction +1.02-1.40pp, cross-model ensemble +0.42pp）。实验覆盖 4 个 NER 数据集、2 个 model family（4B-72B + GPT-5.5）、9 类方法，附 57 项统计检验的 Holm-Bonferroni 校正。

---

## Strengths

**S1. 实验覆盖度和系统性极为出色。** 4 NER benchmarks（SciERC/Few-NERD/CoNLL/WNUT-17）跨域、跨难度梯度；模型从 4B 到 72B 再到 GPT-5.5；9 类方法覆盖 selection/construction/ensemble/supervised。60+ 张表格的 33 页 appendix 提供罕见级别的实验细节。[R1-S1, R2-S1, 共识]

**S2. 诊断框架设计精巧且可复用。** 四阶段 cascade 逐步排除失败原因，每个阶段有明确 pass/fail 判据。对未来 structured generation 的 test-time compute 研究有方法论贡献。[R1-S2, R2-S2, 共识]

**S3. 统计方法论严谨。** 全局 Holm-Bonferroni（k=57）、bootstrap 95% CI、TOST 等价性检验、instance-level permutation test。对以负面结果为核心的论文，这种统计审慎度是必要的且做到了。[R1-S3, R2-S1, 共识]

**S4. 负面结果的建设性处理。** 不止报告"SC 失败"，而是诊断 WHY + 理论联系（MBR）+ 三条可操作绕过路径。从 "negative finding" 升级为 "diagnostic + prescriptive"。[R1-S4, 共识]

**S5. MBR 理论联系有启发性。** 将 entity construction 形式化为 structured MBR decoding，嵌入更广泛的 decoding 理论。[R1-S5, R2-S3, 共识]

**S6. Hidden-state probe 提供独立 introspection evidence。** AUROC 0.63-0.88 证明信息在模型内部存在但 agreement signals 无法有效提取。[R2-S5, 共识]

---

## Weaknesses

### Must-Fix (共识 Critical)

**W1. SciERC 单 seed 削弱 25%+ NER 证据基础。** SciERC 仅用 1 个 seed（seed=42），而 Few-NERD/CoNLL 用 3 seeds。SciERC 承载 disproportionate 的正面证据（construction gain 最大 +1.02pp, zero-shot +1.53pp; hidden-state probe AUROC 0.882; medium-difficulty primary test bed）。单 seed 的 bootstrap CI 仅反映 instance-level 变异，无法量化 seed-level 不确定性。[R1-W1 critical, R2 强烈 AGREE]
→ **建议**: 补充 SciERC 3-seed 实验；或在正文显著标注 single-seed caveat（当前仅 Appendix j 简要提及）。

**W2. Cross-task validation (RE/SQL) 过于单薄，不支撑 "beyond NER" 的泛化。** RE 仅 SciERC 单数据集单模型（n=207 non-zero），55.5% zero-F1 来自 span error confound，信号排序与 NER 反转。SQL 仅 n=196 + 87.2% degeneracy（ceiling effect），无系统分析。Cross-model 仅 1 dataset × 1 model pair。Abstract/Intro 的 "validate on RE and SQL" 宣传力度超出证据。[R1-W3 warning, R2-W2 critical, 共识——R2 认为应为 critical]
→ **建议**: 降低 RE/SQL 宣传为 "preliminary extension"；Limitations 补充 cross-task 证据局限。

### Should-Fix (共识 Warning)

**W3. Proposition 1 (Entity Selection Bound) 过松，理论贡献需重定位。** Bound (1−D)·G_nd·α 仅捕获 3-12% 实际 gain（Table 30），几乎无排除力。论文自述 "loose" 但列为核心贡献之一。Empirical cascade 与 theoretical decomposition 存在两套平行框架但缺映射说明。[R1-W2 critical, R2 AGREE]
→ **建议**: 重定位为 "diagnostic decomposition" 而非 "performance bound"；讨论哪个因子（α）最保守及为什么。

**W4. Degeneracy 可能是更简洁的核心解释，四阶段 cascade 可能 over-engineered。** 高 degeneracy 下 selection 失败是 trivial（样本全同）。非 degenerate instances 上 α→0（signal alignment 极低，0.000-0.161）才是核心洞察。更精确的 framing 应为 "near-zero selection alignment despite moderate quality correlation"，不需要整个 cascade。Cascade 有方法论复用价值但作为 narrative 过重。[R1-W6 warning, R2-W4 warning, 共识]
→ **建议**: 主文中更突出 non-degenerate failure（α→0）作为核心发现；cascade 定位为可复用诊断协议。

**W5. 训练配方差异构成跨数据集比较混淆。** Few-NERD 3 epochs vs 其他 5 epochs。SciERC 消融显示 degeneracy 随 epoch 单调递增（43.5%→60.3%）。Few-NERD 低 degeneracy（13%）可能部分由更少 epochs 解释，但 Few-NERD 未做 5-epoch 对照。[R1-W4 warning, R2 AGREE]
→ **建议**: 补充 Few-NERD 5-epoch 消融或明确解释选择依据。

**W6. Abstract 信息密度过高。** ~180 词含 12+ 数字、多个首次出现的缩写、4 项 contributions。ρ/AUROC 来自不同信号但写法可能误导。[R2-W6, R1 AGREE]
→ **建议**: 精简至核心 3-4 个数字；明确标注 ρ 和 AUROC 来源信号。

**W7. Limitations 覆盖不全。** 缺失：(a) RE/SQL 证据单薄性，(b) cross-model 仅 1 dataset × 1 pair，(c) hidden-state probe per-dataset training 可能 overfit，(d) entity construction gain 幅度（+1pp at N× cost）。[R2-W7, R1 AGREE]
→ **建议**: 补充上述 4 点。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识（[AGREE]）：

1. **Cross-task 证据不足以支撑泛化声明** — RE/SQL 应明确降级为 preliminary extension [R1-W3 + R2-W2]
2. **SciERC 单 seed 是显著弱点** — 承载 disproportionate 正面证据但无 seed-level 方差 [R1-W1 + R2]
3. **Degeneracy 是更简洁的核心解释** — α→0 是洞察核心，cascade 作为 narrative 过重 [R1-W6 + R2-W4]
4. **理论 bound 需重定位** — 3-12% 捕获率不足以称为 "bound"，应改为 diagnostic decomposition [R1-W2 + R2]
5. **训练配方差异需控制** — Few-NERD 缺 5-epoch 对照 [R1-W4 + R2]
6. **Abstract 过密 + Limitations 不全** — 需精简数字并补充关键局限 [R2-W6/W7 + R1]
7. **Cross-dataset correlation power 问题** — n=23 power 不足，但核心结论依赖 per-dataset 检验（power 充足），措辞需 hedge [R1-W5, R2 部分 REBUT]

---

## Reviewer Divergence

| 问题 | R1 立场 | R2 立场 | Director 判断 |
|------|---------|---------|---------------|
| **标题 "Capability Ceiling" framing** | "Characterizing" 已是防御性 hedge，因果措辞修改属 minor revision (warning) | 标题暗示 impossibility result，应改标题 (critical) | **R2 更合理**：标题整体是防御性的，但正文因果措辞（"governs"/"determines"/"explaining where and why"）与 observational design 确有矛盾，需系统性替换。标题本身可保留但正文需修。定为 **Should-Fix**。 |
| **Entity construction 新颖性** | 诊断对比价值 + MBR 形式化被低估 | 实质是 threshold MBR 特殊情况，新颖性有限 (warning) | **R1 更合理**：construction 本身不新，但其与 selection 的系统对比揭示了失败的粒度边界（sample-level vs entity-level），这是诊断贡献的一部分。定为 **info 级**。 |
| **MBR 文献区分** | NER-specific 机制与 MT MBR 有质的区别，需将讨论从 Appendix 移入 main text | 区分不充分，读者可能视为 re-instantiation (warning) | **折中**：内容上 R1 正确（LP compression under constrained decoding 是 NER-specific），但呈现上 R2 正确（关键对比在 Appendix 不够）。定为 **Should-Fix**（移入 main text）。 |

---

## Questions

**Q1.** SciERC 为何仅用 1 个 seed？是资源限制还是方法论考虑？[R1-Q1, 共识]
**Q2.** Hidden-state probe 是否做过 LODO CV？论文已有 LODO 结果（§3: AUROC drops to 0.559-0.671）但主文讨论不足——如 probe 不能 transfer，"introspection boundary" 证据价值减弱。[R2-Q2, R1 AGREE]
**Q3.** Entity construction "bypasses entity-level self-verification" 但仍依赖 entity-level agreement——更准确表述应为 "bypasses sample-level selection by operating at entity granularity"。[R2-Q3, R1 AGREE]
**Q4.** Cross-model 为何未在 Few-NERD（degeneracy 最低）上测试？这是逻辑上最应做的实验。[R2-Q4, R1 AGREE]
**Q5.** Proposition 1 entity-wise independence 假设 violation 程度？Table 30 Ratio (3-12%) 间接反映但未直接量化 entity-pair correlation。[R2-Q5, R1 部分 AGREE]
**Q6.** LP compression threshold ε=0.05 选择依据？不同 ε 是否改变 LP ranking？[R1-Q2]
**Q7.** TOST equivalence margin δ 的选择是否 data-driven（循环推理风险）？[R1-Q3]
**Q8.** Zero-shot instruction-tuned 模型下 gap 幅度是否有实质变化？[R1-Q4]

---

## Missing References

- R1: 未发现重要缺失。可选补充 Malinin & Gales (2021) "Uncertainty Estimation in Autoregressive Structured Prediction"
- R2: 建议补充 Varshney et al. (2022) ACL Findings (selective prediction), Xin et al. (2021), Malinin & Gales (2021) ICLR (structured uncertainty)
- 需核实：ma2024selfimproving 第一作者（bib "Ma" vs OpenAlex "Xie"）
- 引用验证：57 bib, 0 orphan, 0 missing, 2 not found (OpenAlex 覆盖 gaps), 4 minor encoding mismatches
- 引用质量总评：**良好**，无虚假引用

---

## External Review (Stanford Agentic Reviewer)

未配置，不适用。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时约 4 分钟）

| Severity | 发现 |
|----------|------|
| warning | Pages 1-2 连续纯文字墙（Abstract + Intro + Diagnostic Framework 开头），无 figure/table/equation 穿插。建议将 Figure 1 提前至第 2 页。 |
| warning | Page 7 极度拥挤——Table 4 + Table 5(a/b) + Figure 3 全部堆叠，表格间距极小，Figure 3 被压缩至可读性下限（约正文字号 60-65%）。建议移 1-2 个 table 到 appendix。 |
| info | Figure 1（p3）三阶段诊断级联 + 关键数值，颜色编码清晰，caption 自含。 |
| info | 所有正文表格统一 booktabs 风格，最优值加粗，精度一致——排版规范。 |
| info | p17 Figure 6 热力图使用红-黄-绿渐变，建议改用 viridis 或 Blue-Orange 色标（红绿色盲友好）。 |
| info | Appendix 多页大面积空白（p41/46/47 >50% 空白），可合并减少。 |
| info | 需验证正文页数：Conclusion 结束位置约 p9 上部，Limitations 紧随。若 Conclusion 超 p8 底部需压缩。 |

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
| Excitement | 3.5/5 | 3.0/5 | **3.0/5** |
| Reproducibility | 4.0/5 | 4.0/5 | **4.0/5** |
| **Overall** | **3.5** | **3.0** | **3.0 (Findings)** |
| Confidence | 4/5 | 4/5 | **4/5** |

### 评分理由

**给 3.0 (Findings) 而非 3.5 的原因：**
1. **Cross-task overclaiming**：标题已限定 NER，但 Abstract/Intro 仍宣传 "validate on RE and SQL"，证据基础远不支撑（RE 单数据集+span error confound，SQL 仅 n=196 的 ceiling effect）
2. **因果 framing 与 observational 设计的系统性矛盾**：虽然标题 "Characterizing" 是防御性的，但正文因果措辞（"governs"/"determines"/"explaining where and why"）仍普遍存在
3. **SciERC 单 seed 在承载核心正面证据的数据集上是显著缺陷**
4. **理论 bound 捕获率仅 3-12%**，作为 "contribution" 的实际约束力有限

**给 3.0 而非更低的原因：**
1. NER 范围内的诊断框架是实质性贡献（四阶段 cascade + 可复用协议）
2. 统计严谨性在 NLP 实证论文中属上乘（k=57 Holm, TOST, bootstrap CI）
3. 9 方法 × 4 数据集的系统性负面结果在该领域尚无先例
4. Prescriptive escape routes 虽增量有限（+1-1.4pp）但方向正确
5. 所有 critical 问题均可在 revision 中修复

### 升级至 3.5 (Borderline Conference) 的条件
- [ ] SciERC 补充至少 2 个额外 seed（或充分论证 single-seed 不影响核心结论）
- [ ] RE/SQL 在 Abstract/Intro 中明确降级为 preliminary exploration
- [ ] Proposition 1 重定位为 diagnostic decomposition（非 performance bound）
- [ ] 正文因果措辞系统性替换（"governs"→"is associated with" 等）
- [ ] MBR 文献对比从 Appendix 移入 main text §8

---

## Detailed Comments

### Section 1 (Introduction)
- "explaining where and why" 暗示因果但证据为相关性 → 改为 "characterizing where and how"
- "validate on RE and SQL" → "extend exploratorily to RE and SQL"
- Contributions list #4 "prescriptive escape routes" 的 cost-effectiveness 应在主文讨论（N× cost for ~1pp），当前仅 Appendix Table 61

### Section 2 (Diagnostic Framework)
- Signal 定义清晰（5 signals 无歧义），instance-level vs per-sample 区分贯穿全文——这是优点
- Entity matching（exact span + type）描述充分
- Eq. 1 (SJ) 引用 Hungarian matching 缺引用 → 补 Kuhn (1955)

### Section 3 (How Self-Verification Fails)
- ESJ/MRSC/LSC 三个独立 probe 一致失败是有力证据
- Hidden-state probe LODO 结果（AUROC drops to 0.559-0.671）已在文中但讨论不足 → 补充解释 CoNLL vs SciERC AUROC 差异原因（task difficulty → error outlier separability）
- "introspection boundary" 术语需考虑 probe 的 dataset-specific 性质

### Section 4 (Where Single-Signal Selection Fails)
- Table 1 (selection) 清晰展示核心 negative result
- "definitional vs empirical" 二分法（§4 首段）是论文最精妙的区分之一 → 建议在 Abstract/Intro 更突出
- Cross-dataset ρ=0.052 (n=23, p=0.81) 的 power 问题已承认但措辞需 hedge

### Section 5 (Adaptive Methods)
- Table 2 (method summary) 是优秀的概览
- Cross-model (+0.42pp) 仅 Few-NERD × 1 pair → 在正文中标注 "single-dataset result"
- LightGBM verifier cross-dataset transfer 为负（-0.76 to -1.02pp）→ 强化了 dataset-specific 的论点

### Section 6 (Threshold Regime Analysis)
- MBR 连接严谨但 Proposition 1 bound 过松 → 见 W3
- Inverse scaling 发现（40/58 transitions 下 construction F1 下降）是重要实践发现
- θ_crit=0.70 作为 necessary condition（非 sufficient）有实际价值

### Section 7 (Experiments)
- Few-NERD 3 epochs vs others 5 epochs → 需控制 [W5]
- Table 4 (entity construction) multi-seed mean±σ 是好的做法
- Holm 分 family（selection k=21, construction k=10, signal k=9）vs global k=57 → 需解释分 family 的依据和全局结果

### Section 8 (Related Work)
- Ma et al. (2024) 已引用 → 验证第一作者
- MBR 文献对比需从 Appendix 移入此处 [Divergence #3]
- Yun et al. (2025) diversity collapse 差异化（Table 62）在 Appendix，核心对比建议在 main text 简述

### Section 9 (Discussion)
- 因果措辞集中区 → 系统替换 "governs"/"determines" [W1 divergent]
- Cost-effectiveness 讨论（"N× cost for ≈1pp"）已存在但需更 explicit

### Section 10 (Conclusion)
- 2 句过于精简；建议加 1 句关于 non-degenerate failure（α→0）作为核心洞察的总结

### Limitations
- 覆盖良好但缺 4 点 [W7]
- 已有 frontier model degeneracy 差异讨论（Claude 74% vs DeepSeek 5.5%）→ 有进步

### Format Compliance
- ✅ 正文 ≤8 页（需视觉审查确认 Conclusion 结束位置）
- ✅ Double-blind（"Anonymous ACL submission"，"[anonymized URL]"）
- ✅ ACL LaTeX 模板 + [review] option
- ✅ References 不限页数
- ✅ Limitations + Ethics Statement 存在
- ⚠️ p7 极度拥挤（视觉审查 warning）