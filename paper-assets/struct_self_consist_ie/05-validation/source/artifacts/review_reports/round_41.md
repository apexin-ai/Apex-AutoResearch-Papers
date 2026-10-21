---
round: 41
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-23T05:30:29.514484+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 41

**论文**: "Why Self-Consistency Fails for NER: Degeneracy, Signal Collapse, and the Correlation-Selection Gap"
**Venue**: EMNLP 2026 (ARR May cycle, Long Paper)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性; R2: 新颖性/完整性）
**审稿轮次**: Round 1, 1 轮收敛（关键问题全部达成共识）

---

## Summary

论文研究 test-time compute scaling（self-consistency、best-of-N）在 NER 上的有效性。通过 4 个 NER 数据集、2 个模型家族（Qwen3-8B, LLaMA-3.1-8B）、N=8–64 的系统实验，发现 quality estimation signals 能预测输出质量（AUROC 0.82）但无法有效指导样本选择（MV gains <1pp），揭示了 "correlation-selection gap"。论文提出一个诊断框架，将失败归因于 degeneracy（12–69% 实例产生相同 entity set）和 signal alignment collapse（α→0）。Entity-level construction 在 Few-NERD 3-epoch 上获得 +1.40pp，但该结果高度依赖训练状态（5-epoch 下降至 +0.09pp）。

---

## Strengths

1. **研究问题重要且定位精准**：SC 在推理任务上成功但在结构化预测上失败的机制分析填补了社区空白。[R1, R2 共识]

2. **实验极其详尽且透明**：4 数据集 × 2 模型家族 × 5 信号 × 9 方法类别，N scaling 到 64，38 页附录覆盖 robustness/ablation/calibration/power analysis。统计检验的两种校正方案均完整报告。TOST equivalence testing 是方法论加分项。[R1, R2 共识]

3. **Degeneracy 概念有实证价值**：12–69% 的 NER 实例产生相同 entity set，这一 NER-specific failure mode 是有洞察力的发现，且 degeneracy rate 作为 pre-deployment check 有实际应用价值。[R1, R2 共识]

4. **MBR decoding 理论连接清晰**：Proposition 1 将 entity construction 形式化为 MBR 特例，为结构化预测中的 SC 提供了理论锚点。[R1, R2 共识]

5. **Negative results 诚实报告**：明确报告 cross-dataset transfer 失败、RE 局限、epoch confound，Appendix ah 预先回应 12 个潜在 objections。[R2]

6. **Reproducibility 高**：承诺开源代码/checkpoint/数据，超参数报告详尽（Table 22, Appendix m），使用公开数据集和开放权重模型。[R1: 4/5, R2: 4/5]

---

## Weaknesses

### Must-Fix（5 项，交叉分享后共识）

**MF1** [R1-N1, R2 AGREE] **分解 bound 仅恢复 3–12% 实际增益，核心形式化贡献实用价值不足**
- 位置：§6.3, Figure 10, Table 33
- Bound E[ΔF1(A)] ≤ (1−D)·G_nd·α 仅捕捉 3–12% actual gains，88–97% 由未建模因素决定（inter-entity 依赖、非线性交互）。
- R2 交叉回应补充：bound 的真正价值在于识别**必要条件**（D→1 时任何聚合方法都无效），而非定量预测。当前 framing 试图呈现为定量诊断工具是 overselling。
- **建议**：重定位为 necessary condition test；弱化 Table 33 ratio 列；§6.3 明确声明 bound intentionally loose。

**MF2** [R1-N2, R2 AGREE] **核心正面 claim 统计显著性取决于多重比较校正方案**
- 位置：Appendix f, §7.5
- 全局 Holm-Bonferroni (k=57): p_adj=0.055（未达阈值）；per-family (k=10): p_adj=0.006。主文使用 per-family 报告但未提供 family 划分的先验理由。
- R2 交叉回应指出：per-family 校正非统计错误，但 **family 划分是研究者自由度**，需先验理由。
- 与 MF5 叠加：唯一正面结果同时面临 under-training artifact + 统计显著性依赖校正方案的双重质疑。
- **建议**：§7.1 提供 family 划分先验理由；主文同时报告全局 p_adj=0.055；坦诚讨论不确定性。

**MF3** [R1-N3, R2 AGREE（略低严重度）] **Mechanistic probes 使用 Qwen2.5-7B 而非主实验 Qwen3-8B**
- 位置：Appendix i, §4
- Hidden-state probes/ESJ/MRSC 全部在 Qwen2.5-7B-Instruct（非 fine-tuned）上执行，但正文 §4/Table 3 直接引用结果支撑主论述，未提及模型不一致。
- R2 交叉回应：probe 结果属于辅助性证据，删除不影响核心结论，但引用时必须标注模型不一致。
- **建议**：正文引用处标注 "obtained on Qwen2.5-7B"；Limitations 列出局限；可选在 Qwen3-8B 上复现至少一组 probe。

**MF4** [R2-N1, R1 AGREE（略低严重度）] **与 Landesberg et al. (2026) 的 correlation-selection gap 概念重叠，differentiation 不足**
- 位置：§1, §2 "Concurrent work", Table 1
- Landesberg et al. 在 reasoning 场景独立发现 correlation-selection gap (global r=0.47, within-prompt r=0.27)。当前 §2 仅一段话处理区分。
- R1 交叉回应：认同需更强 differentiation，但指出论文有实质差异——degeneracy 是 NER-specific，entity construction 是结构化预测特有。
- **建议**：§2 用至少半页系统对比两个框架；明确标注 Landesberg 在 gap 发现上的优先权；强调 failure mechanism 差异（prompt-level effects vs degeneracy+signal collapse）；Table 1 增加 failure mechanism 维度。

**MF5** [R2-N2, R1 交叉后升级为 critical] **Few-NERD epoch confound 严重削弱最显著正面结果**
- 位置：§7.5, Abstract, Appendix ad
- +1.40pp 来自 3-epoch under-converged 模型；5-epoch 下 LP gain 从 +1.39 降至 +0.09pp（94% collapse），entity construction 从 +0.88 降至 +0.20pp（77% reduction）。
- Abstract 中 "+1.40pp" 未加任何条件限定。这是论文中**唯一超过 1pp** 的正面选择结果。
- R1 初审标为 Should-Fix，交叉分享后升级为 critical（与 R2 一致）。
- **建议**：Abstract 限定条件（"under 3-epoch training; collapses at convergence"）；§7.5 完整呈现 3-epoch vs 5-epoch 对比数据而非仅 "should be interpreted cautiously"。

### Should-Fix（6 项）

**SF1** [R1-W5 + R2-W1, 完全共识] **Diagnostic vs prescriptive 叙事定位不一致**
- Abstract/§8 定位 "diagnostic, not predictive"，但 §7.5 使用 "the diagnostic framework correctly predicts this"，§5 提出 adaptive methods，Appendix aj 提供 practical recommendations。
- **建议**：统一定位——承认框架有弱预测能力，或将 §5/§7.5/Appendix aj 语气改为 post-hoc 分析。

**SF2** [R1-W2, R2 AGREE] **2–3 seeds 统计推断力不足**
- Seed-level 方差仅基于 3 个点估计（df=2）。R2 注意到 3-5 seeds 是领域事实标准，但 Table 12 的 bootstrap CI 基于 10,000 permutations 却仅 3 seeds 训练方差，这一矛盾需讨论。
- **建议**：Limitations 声明 "variance estimates from 3 seeds should be interpreted as approximate"。

**SF3** [R1-W3, R2 AGREE] **RE/SQL 扩展过薄，不足以支撑 Abstract 泛化性声称**
- RE 仅 SciERC 单数据集 N=8，SQL 几乎无实质结果。Abstract 并列给读者泛化印象。
- **建议**：Abstract 改为 "our analysis focuses on NER; preliminary observations on RE suggest..."

**SF4** [R2-W3, R1 部分 AGREE] **Related Work 覆盖面不足**
- 遗漏：(a) Eikema et al. (2025) structure-conditional MBR decoding (arXiv:2510.20700)——与 §6.1 MBR 连接高度相关；(b) uncertainty estimation/calibration in NLP；(c) 2025-2026 TTS 新进展。
- **建议**：§2 扩展，特别引用 Eikema et al. (2025)。

**SF5** [R2-W5, R1 AGREE] **Entity-level decomposition 增量贡献需更强论证**
- 需明确展示 entity-level 能发现但 task-level 会遗漏的具体现象。R1 指出：degeneracy 定义（identical entity sets）只有 entity-level 可计算，entity construction 是 entity-level 特有策略。但论文未提供 task-level vs entity-level 分析结论矛盾的具体 case study。
- **建议**：§3 或 §4 增加对比实例。

**SF6** [R1-W4, R2 partial REBUT] **Constrained decoding 对 LP 的 confound 未充分解耦**
- Free-form ablation 仅在 SciERC 上验证（LP std ratio 0.97×，排除了极端假说），但一个数据集不够。R2 部分 rebut：当前证据足以排除 "LP compression 完全是 constrained decoding artifact"，但不足以完全解耦。
- **建议**：至少在 CoNLL 上重复 free-form ablation。

### Reviewer Divergence（2 项，不影响评分）

**DIV1** 标题 "Why SC Fails for NER" 与内容匹配度
- R2 认为 "Why" 暗示因果解释但论文仅提供 what/when → Should-Fix
- R1 REBUT："Why X Fails" 是 NLP 标准标题范式，当前标题在领域惯例内
- **Director 判断**：R1 的 rebut 有理，"Why" 在 NLP 论文中通常指诊断性解释而非严格因果。记录但不列入 action items。

**DIV2** 正文数字密度过高
- R2 认为 Abstract ~15 数值、§4 每段 8+ 数值导致 takeaway 难提取 → Should-Fix
- R1 REBUT：诊断性实证论文数字是内容本身，建议降为 Minor（加 plain-language takeaway 句）
- **Director 判断**：R1 rebut 合理。建议在关键段落首句加无数字的 claim sentence 作为可选优化，不列为 Should-Fix。

---

## Questions（合并去重）

1. 分解 bound 的松弛度（88–97%）主要来自哪个简化假设——entity 间独立性、α 的线性近似、还是乘法结构？是否尝试过更紧的 bound？[R1-Q1]
2. 能否在 Qwen3-8B 上复现至少一组 probe（ESJ 或 hidden-state），验证 mechanistic findings 的跨模型迁移性？[R1-Q2]
3. Few-NERD 5-epoch 下 entity construction 的具体收益数字？Appendix ad 暗示收益消失，请明确报告。[R1-Q3, R2-Q1]
4. Free-form decoding 下 LP 在 CoNLL 和 Few-NERD 上的 selection 表现？如果显著改善，"LP fails for structured prediction" 需 qualified。[R1-Q4]
5. 是否考虑预注册假设层级（primary/secondary/exploratory）处理多重比较？[R1-Q5]
6. Instance-level 分析在哪些 scenario 下产生与 task-level 分析矛盾的结论？即 task-level 显示 SC 应 work 但 instance-level 揭示实际 fails 的 case？[R2-Q4]
7. Degeneracy 定义放宽到 partial match 是否显著降低 D？是否改变框架结论？[R2-Q5]
8. Proposition 1 的 entity independence 假设在 NER 中通常不成立——违反对 MBR 等价性的实际适用性影响？[R2-Q2]

---

## Missing References

1. **Eikema et al. (2025)**: "Structure-conditional minimum Bayes risk decoding" (arXiv:2510.20700) — 直接处理结构化输出的 MBR 问题，与 §6.1 高度相关但未被引用。[R2-W3, R1 AGREE]
2. **Uncertainty estimation/calibration 文献**：Desai & Durrett (2020) on calibration of NLU models; Xiao et al. (2022) on uncertainty in structured prediction — 与 LP signal 分析和 Appendix c 的 calibration analysis 相关。[R2-W3, R1 AGREE]
3. **2025-2026 TTS 新进展**：reward-tail-guided search、short-m@k 等方法 — §2 仅引用 Snell et al. (2025)，对最新进展覆盖不足。[R2-W3]

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿（状态：not_requested）。

---

## Visual Layout Check（非评分项）

状态：**done**（耗时 ~5 分钟）

| 严重度 | 页面 | 发现 |
|--------|------|------|
| ⚠️ warning | p.2 | Figure 1 红绿配色对色盲用户不友好（~8% 男性），建议改用蓝/橙双色或增加纹理辅助 |
| ⚠️ warning | p.2 | Figure 1 内部标注文字偏小（AUROC=0.82 等），打印后可能低于 8pt 可读阈值 |
| ℹ️ info | p.4 | Figure 2 蓝绿柱子色盲区分度略低，但有文字标签辅助 |
| ℹ️ info | p.7 | 单页 3 个 display items，密度偏高但排版整齐 |
| ℹ️ info | p.15 | Figure 7 热力图数值文字较小（~6-7pt），Appendix 中影响有限 |
| ℹ️ info | p.22 | 页面底部较大空白（~40%），Appendix 页面可接受 |
| ℹ️ info | p.46 | 末页仅 ~30% 内容，Appendix 末页可接受 |

0 critical, 2 warning, 5 info。无阻断性排版问题。Figure 1 色盲友好性建议修改。

---

## Overall Assessment

**评分**: 3.5 / 5 (Borderline Conference)
**置信度**: 4 / 5

### 维度分数

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |

### 评分理由

论文在一个重要但未充分研究的问题上提供了系统性的诊断分析——SC 为何在 NER 上失败。实验覆盖面和统计严谨度在 NLP 实证研究中属上乘，degeneracy 概念和 MBR 理论连接有独立价值。

但 5 个 Must-Fix 问题共同削弱了论文的核心贡献支柱：
- **形式化贡献**（bound）仅解释 3–12% 现象（MF1）
- **唯一正面选择结果**（+1.40pp）同时受 epoch confound（MF5，94% collapse at convergence）和统计显著性校正方案依赖（MF2，全局 p_adj=0.055）的双重质疑
- **辅助证据**（mechanistic probes）使用不同模型未经验证（MF3）
- **核心概念**（correlation-selection gap）与 concurrent work 重叠，differentiation 不足（MF4）

论文的**负面发现**（SC 对 NER 基本无效、degeneracy 概念、系统性文档记录）具有独立价值，使 3.0 (Findings) 成为合理的 lower bound。如果 MF1-MF5 得到充分回应——特别是 MF2（统计透明度）、MF4（novelty differentiation）和 MF5（epoch confound 的坦诚处理），论文有望进入 Conference 范围。

当前状态下，论文处于 Borderline Conference / Strong Findings 的位置。

---

## Detailed Comments

### §Abstract
- "+1.40pp" 需加条件限定（"3-epoch; diminishes at convergence"）→ MF5
- "preliminary RE and SQL pilots" 表述可接受，但与正文 RE/SQL 的 thin coverage 存在落差 → SF3
- 数字密度高（~15 数值）但 R1 认为诊断论文可接受 → DIV2

### §1 Introduction
- "correlation-selection gap" 首次使用应加简短定义 → Minor
- Figure 1 是有效的 overview，但色盲友好性需改善 → Visual Check

### §2 Related Work
- Landesberg et al. (2026) 的处理仅一段话，严重不足 → MF4
- 遗漏 Eikema et al. (2025) structure-conditional MBR → SF4
- 遗漏 uncertainty estimation/calibration 文献 → SF4

### §3 Diagnostic Framework
- 框架设计逻辑自洽，5 信号分类（per-sample vs instance-level）清晰
- entity-level vs task-level 的增量贡献需具体 case study 支撑 → SF5

### §4 Where Single-Signal Selection Fails
- LP compression 发现扎实（within-instance LP range 中位数 0.041）
- Mechanistic evidence 引用需标注模型不一致 → MF3
- "diagnostic not predictive" 与后续 §7.5 语言矛盾 → SF1

### §5 Adaptive Methods
- Cross-model SC (+0.42pp Few-NERD) 仅单数据集，已标注 preliminary
- Table 3 的 9 方法类别覆盖全面
- §5 作为整节存在是否与 "diagnostic" 定位冲突？→ SF1

### §6 Threshold Regime Analysis
- MBR 连接（Proposition 1）干净
- Bound 松弛度问题 → MF1
- "scaling law" 基于 6 点应改为 "scaling trend" → Minor
- α 符号与 significance level 冲突 → Minor

### §7 Experiments
- 实验设计和覆盖面优秀
- §7.5 epoch confound 处理过于轻描淡写（"should be interpreted cautiously"）→ MF5
- 统计检验校正方案选择缺先验理由 → MF2
- Free-form ablation 仅 SciERC → SF6

### §8 Discussion/Conclusion
- Practical recommendations 有应用价值
- "diagnostic, not causal" 定位与 §7.5 的预测性语言矛盾 → SF1

### Limitations
- 覆盖了主要局限但未明确列出：(a) mechanistic probes 的模型不一致 → MF3；(b) epoch confound 的深层含义
- 长度适当（1 小段，~3 点）

### Appendix
- 极其详尽（38 页 a-aj），是论文的重要优势
- 缺目录，建议增加 → Minor
- Appendix ah (self-review) 是少见的透明度展示
