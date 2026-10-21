---
round: 31
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-22T01:19:08.201548+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Characterizing the Capability Ceiling of Self-Consistency: How Entity-Level Verification Fails in NER

**Venue**: EMNLP 2026 (via ACL Rolling Review)
**投稿类别**: Long Paper
**审稿模式**: Fresh（全新初审）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验+统计；R2: 新颖性+相关工作+写作）
**轮次**: Round 1 + 交叉分享，1 轮收敛

---

## Summary

本文研究 self-consistency（SC）在命名实体识别（NER）上的失败模式，定义了"correlation-selection gap"——质量估计信号与 oracle F1 存在相关性（Spearman ρ up to 0.47, AUROC up to 0.82），但无法用于选择更好的样本。作者提出四阶段诊断级联（degeneracy → agreement fidelity → LP compression → construction），在 4 个 NER 数据集（SciERC, Few-NERD, CoNLL-2003, WNUT-17）、两个模型族（Qwen3-8B, LLaMA-3.1-8B）上系统评估了 9 类方法，发现均无法可靠改善 sample selection。正面结果通过 LP-weighted entity construction（+0.3–1.4pp）和 LP selection（+1.39pp on Few-NERD）在 entity 粒度绕过了 sample-level selection 的瓶颈。

---

## Strengths

**S1. 问题定位精准，填补研究空白。** SC 文献几乎完全聚焦于分类/推理任务，NER 作为 set-valued 结构化输出的代表性任务缺乏系统性 SC 失败分析。本文填补了这一空白。[R1, R2 共识]

**S2. 诊断框架结构清晰、可复用。** 四阶段级联（§2–§4）将复杂问题分解为可独立检验的子问题，每一步有对应实验支撑，逻辑链条完整。该框架可迁移至其他 set-valued 任务。[R1, R2 共识]

**S3. 实验规模和统计严谨性远超领域平均。** 报告了 bootstrap 95% CI、Holm 校正置换检验、permutation p-values、split-half reliability、Bonferroni 校正。300+ 实验覆盖 4 数据集 × 多模型 × 多 seed。[R1, R2 共识]

**S4. 诚实呈现负面结果。** 论文未夸大正面发现，系统展示了 9 类方法的失败并提供了清晰的诊断解释。这在 ML 论文中难得。[R1]

**S5. 引用验证通过。** 57 条 bib entry 全部有引用、无 orphan，52/57 通过在线验证，无伪造引用。[R2]

**S6. Constrained decoding confound 处理得当。** 论文包含 free-form vs constrained decoding 对比（Appendix q），排除了 degeneracy 是 constrained decoding artifact 的可能。[R1]

---

## Weaknesses

### Critical

**C1. N=8 采样不足以支撑 "capability ceiling" 声明** [R1-N2, R2 AGREE]
- N=8 时 degeneracy 12%–62%，部分是小 N 的直接后果。N=16 分析（Appendix）显示 degeneracy 下降、SJ ρ 改善 +0.091、LP 增益出现。Oracle F1 随 N 单调递增（Figure 10）。
- 标题 "Capability Ceiling" 暗示固有结构性上界，但论文未提供 selection gap 随 N 收敛的证据。"Ceiling" 意味着渐近上界，当前数据仅支持 "在 N≤16 上存在显著 gap" 这一更弱结论。
- **修改建议**: 至少在 1 个数据集测试 N=32/64 并展示 selection gap 的 N-dependence 趋势；或将 "ceiling" 修改为 "limitations"（如 "Characterizing the Limitations of Self-Consistency for NER"）。

### Major

**M1. Proposition 1 的 entity-wise independence 假设不现实** [R1-N1 Critical → R2 降为 Major]
- §6.1 Proposition 1 的 MBR 分解依赖 entity-wise independence，但 NER 中实体有 span 重叠约束、句内数量约束、自回归条件依赖。论文仅用一句话承认假设是近似的，未量化偏差。
- R2 认为 Proposition 1 是 motivating analysis 而非核心定理，Table 5 的实证效果独立于理论证明，因此 severity 降为 Major。
- **修改建议**: 将 Proposition 1 重定位为 "motivating analysis under simplifying assumptions"；补充 entity 间 mutual information 的经验量化。

**M2. 核心叙事 framing 偏向负面** [R2-N1 Critical → R1 REBUT → 降为 Major]
- R2 指出 Abstract "no signal outperforms greedy" 与 LP +1.39pp 矛盾。R1 反驳：(1) Abstract 限定于 SciERC，(2) LP 是 model-internal signal 非 entity-level agreement signal（Table 1 caption 明确标注），"entity-level verification fails" 指的是 SJ/VC/EM/FK。
- R1 的反驳成立——"直接矛盾" 指控不成立。但双方均认为整体 framing 偏向负面叙事，应更好地平衡 diagnostic 和 prescriptive 两条线索。
- **修改建议**: Abstract 和 Introduction 中明确区分 agreement signals（确实失败）vs model-internal LP（有条件成功）；重组 claim hierarchy。

**M3. 与 Yao et al. (2026) 的增量区分不充分** [R2-N2 Critical → R1 REBUT → 降为 Major]
- R2 认为本文可能只是 Yao et al. consistency-accuracy correlation 的 NER 特例。R1 反驳：Yao 证明 correlation 存在，本文追问为何不能 operationalize 为 selection gain，提供了四阶段诊断级联，是递进关系而非特例。
- R1 的反驳合理但双方均同意 §8 一句话处理不充分。
- **修改建议**: 在 §1 或 §8 用一段专门对比 Yao et al.，说明 diagnostic cascade + construction 方法的具体增量。

**M4. RE/SQL exploratory extensions 过于薄弱** [R1-W1, R2 AGREE]
- RE 仅 SciERC 1 个模型 397 有效样本（55.5% zero-F1 受 upstream NER 错误污染），SQL 仅 Spider subset n=196 with 87.2% degeneracy。不足以支撑 Introduction 中 "broader set-valued generation problem" 的泛化声明。
- **修改建议**: 明确定位为 preliminary evidence 并在 Limitations 注明；或从 claim 中移除 "broader" 定位。

**M5. 正文/附录比例 8:37 严重失衡** [R2-W1, R1 AGREE]
- 关键信息被推入 Appendix：9 类方法完整结果（Appendix b.4）、N-scaling 分析（Appendix b.6）、hidden-state probes（Appendix h-i）、cross-dataset transfer。审稿人需读 ~47 页才能评估完整性。
- **修改建议**: 将 N-scaling 核心发现和 cross-dataset 结果移入正文。可合并 §9 Discussion + §10 Conclusion 腾出空间。

**M6. 因果性语言超出相关性证据** [R1-W3, R2 AGREE]
- "degeneracy is the binding constraint"（§4）等表述超出证据。Non-degenerate subset 上 selection gap 仍存在，说明 degeneracy 不是唯一约束。论文 §2 声明 "observational" 但后续 section 有因果性措辞残留。
- 注意：历史 R1-W2（Round 1-21）曾修复全文因果语言（15 处 + 4 处残留），本轮发现仍有残留。
- **修改建议**: 全文检查因果性语言，降级为 "a major contributing factor" / "associated with"。

**M7. SciERC (n=529) 和 cross-dataset (n=23) 统计效力不足** [R1-W4, R2 AGREE]
- 论文自身 power analysis（Appendix）确认 80% power requires n≈85 for ρ=0.3，cross-dataset n=23 远低于要求。但这些 caveat 仅在 Appendix 讨论。
- **修改建议**: 在主文相关结论处注明 statistical power 限制。

**M8. 缺少 token-level 不确定性方法的系统比较** [R1-W5, R2 AGREE]
- LP（mean token log-prob）是唯一的 token-level 信号聚合方式，也是唯一展示正面结果的 model-internal signal。未与 sequence entropy、per-token entropy max/variance、predictive entropy（Kuhn et al. 2023）等做比较。
- **修改建议**: 至少补充 sequence entropy 作为 ablation。

### Minor / Info

**m1.** 正面结果 practical significance 有限（+1.4pp at 8x inference cost）——但论文定位为 diagnostic study 而非 method paper，双方认为可接受。建议正文明确定位。[R2-W4, R1 nuanced AGREE]

**m2.** Table 1/Table 3 significance 标注不一致（†/‡ vs bold）。[R1]

**m3.** Figure 1 箭头暗示因果方向与 "diagnostic sequence" 标注不符。建议改为虚线。[R1, R2 AGREE]

**m4.** "Capability ceiling" 未形式化定义。[R1]

**m5.** 10 个 section 在 8 页内过于拥挤，§9 Discussion 和 §10 Conclusion 各不到半页。建议合并。[R2]

**m6.** Table 2 在正文仅展示 Few-NERD 单数据集结果。应至少展示 2 个数据集。[R2]

**m7.** Proposition 1 条件过强（balanced set-overlap utility + entity independence），未讨论对 α 值的敏感性。[R2]

---

## Reviewer Consensus [AGREE]

1. **N=8/"ceiling" 过强** — 论文的泛化 claim 超出实验证据支撑范围。标题暗示固有结构限制，但未提供收敛证据。[C1]
2. **因果语言残留** — 论文声明 observational 但后续有因果性措辞。[M6]
3. **RE/SQL 不足以泛化** — 覆盖度太低，应降级为 preliminary evidence。[M4]
4. **统计效力问题** — SciERC n=529 和 cross-dataset n=23 应在主文注明。[M7]
5. **附录比例失衡** — 关键结果不应仅在 Appendix。[M5]
6. **缺少 token-level 信号比较** — LP 是唯一的 model-internal signal 比较对象。[M8]

## Reviewer Divergence [REBUT]

1. **叙事矛盾 severity** — R2 定为 Critical（"直接矛盾"），R1 以文本证据反驳（LP ≠ entity-level agreement，Abstract 限定于 SciERC）。**Director 判断**: R1 的反驳成立，降为 Major（framing bias 而非 factual contradiction）。[M2]

2. **与 Yao et al. 关系** — R2 认为是 Yao 的特例，R1 认为是递进关系（从 correlation 存在到 why selection fails）。**Director 判断**: R1 论据更充分（四阶段 cascade + construction 是增量），但 §8 一句话确实不够，降为 Major。[M3]

3. **模型覆盖** — R2 称"仅两个同规模模型"，R1 指出论文含 5 个变体（4B/7B/8B/14B/72B），R2 遗漏了 Appendix t 的 72B 数据。**Director 判断**: R2 的事实认定有误，但 72B 仅在 Appendix 且为 zero-shot，缺乏 fine-tuned 大模型验证仍是合理关切。

4. **vs Yun et al. diversity collapse** — R2 认为 degeneracy 是 diversity collapse 的 NER 特例；R1 引用 Appendix q 证据（free-form decoding 下 degeneracy 同样存在）区分两者。**Director 判断**: R1 的区分合理（定义不同、scope 不同、free-form 证据排除了 constrained decoding artifact），但论文正文应更清晰地呈现这一区分。

5. **Holm-Bonferroni 保守性** — R1 认为 k=57 过度保守；R2 反驳对负面结果论文保守校正增强可信度。**Director 判断**: 双方有理。补充 BH-FDR sensitivity check 即可（Info 级别）。

6. **Proposition 1 severity** — R1 定 Critical，R2 降为 Major（motivating analysis 非核心定理）。**Director 判断**: 采用 R2 的 Major 定级——Proposition 1 的实证效果（Table 5）独立于理论证明。

---

## Questions（需要作者回应）

**Q1.** "Entity-level agreement signal" 的精确范围是什么？LP selection 的成功是否意味着 model-internal signals 可以部分绕过 correlation-selection gap？论文应在 §2 中给出明确分类。

**Q2.** N=32/64 时 degeneracy rate 和 selection gap 的趋势如何？是否有证据表明 gap 随 N 收敛到某个 asymptote？

**Q3.** CoNLL 上 48%–87% instances 产生 identical outputs——这是否因为模型在 well-studied benchmark 上 overfit/memorize？在 fully OOD 数据上 degeneracy 是否会降低？

**Q4.** LP-weighted MBR（§6.1）与 model-based MBR（Jinnai et al. 2024）有何实质区别？

**Q5.** Entity-wise independence 假设在实验数据上的近似程度如何？可否通过 entity 对的 mutual information 量化？

**Q6.** 为何未比较 sequence entropy 等其他 token-level 信号聚合方式？LP 的 mean log-prob 聚合是否有特殊优势？

---

## Missing References

以下引用经两位 Reviewer 交叉确认应补充：
1. **Fisch et al. (2021)** "Few-Shot Conformal Prediction with Auxiliary Tasks" — conformal prediction for structured NLP [R2, R1 AGREE]
2. **Chen et al. (2021)** "Evaluating Large Language Models Trained on Code" — pass@k 原始来源 [R2, R1 AGREE]
3. **Varshney et al. (2022)** "Investigating Selective Prediction Approaches..." — selective prediction survey [R2, R1 AGREE]
4. **Malinin & Gales (2021)** — 结构化预测中的不确定性估计 [R1, R2 AGREE]
5. He et al. (2024) on token-level uncertainty decomposition [R2, R1 认为相关但非必须]
6. Test-time scaling survey (2025) [R2, R1 认为相关但非必须]

---

## External Review (Stanford Agentic Reviewer)

未请求（项目未配置外部审稿）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（耗时 ~5 分钟）。发现 1 critical + 6 warnings + 18 info：

**[Critical]** Page 7 单页塞入 4 个 display items（Tables 3, 4, 5 + Figure 3），严重过挤。表格字号极小，Figure 3 散点图标注在 150dpi 下难以辨认。建议移 Table 4 或 5 至 Appendix 或合并。

**[Warning]**
- Pages 1-2 连续纯文本无 display item，首个视觉锚点（Figure 1）在第 3 页——建议提前
- Figure 1 使用红/绿对比色，对色盲用户不友好（~8% 男性）——建议改用 blue/orange 或 Okabe-Ito 色板
- Page 6 全页纯文本（含 Proposition 1），节奏偏紧
- Page 8 Discussion/Related Work/Conclusion 全纯文本
- Appendix p.25 Table 13（57 行汇总表）字号极小
- Appendix p.26 单页 7 个小表格，排版极度拥挤

**整体**: 全文 booktabs 风格一致、公式渲染正确、无 overfull hbox、无 section heading 孤悬、主文在第 8 页结束符合页数限制。

---

## Overall Assessment

### 评分: 3.0 — Findings

**R1 评分**: 3.5 (Borderline Conference) | **R2 评分**: 3.0 (Findings)

### 综合评分理由

本文对 SC 在 NER 上的失败模式提供了系统性的实证分析——四阶段诊断级联有概念价值和复用性，300+ 实验的统计严谨性远超领域平均。然而以下因素限制了评分：

1. **核心 claim 过强** [Critical]: "Capability Ceiling" 暗示固有结构限制，但 N=8 时未提供 selection gap 随 N 收敛的证据。标题和 claim 需要降级。

2. **Framing 失衡** [Major consensus]: 论文在 diagnostic（负面发现）和 prescriptive（正面结果 +0.3–1.4pp）之间的叙事张力未被充分调和。Agreement signals 的失败是清楚的，但 LP 的有条件成功被 framing 淡化。

3. **泛化支撑不足** [Major consensus]: RE/SQL 扩展过于初步；缺少 token-level 信号对比；关键结果在 Appendix 而非正文。

4. **理论贡献有限** [Major]: Proposition 1 依赖不现实的 independence 假设，需重定位为 motivating analysis。

5. **增量新颖性** [Major]: 与 Yao et al. (2026) 和 Yun et al. (2025) 的增量区分需更充分论证。

**Findings 适配理由**: 论文的核心贡献——correlation-selection gap 概念和四阶段诊断级联——有学术价值，适合 Findings 发表。但 "ceiling" 的过强 claim、正面结果的有限 practical significance（+1.4pp at 8× cost）、以及多个泛化性问题，使其不足以进入主会议。

### 置信度: 4/5

两位 Reviewer（confidence 均为 4/5）在核心问题上达成高度共识。分歧点均有充分论据支撑且已 resolve（Director 判断均有据可循）。论文已被仔细通读（含关键 Appendix 章节）。

---

## Detailed Comments

### 按优先级排列的修改建议

**Priority 1 (Must-fix for resubmission)**:
1. 修改标题——将 "Capability Ceiling" 替换为 "Limitations" 或类似审慎措辞；或补充 N=32/64 收敛证据
2. 平衡 diagnostic/prescriptive 叙事——Abstract 和 Introduction 明确区分 agreement signals vs LP
3. 扩展 Yao et al. (2026) 对比——从一句话扩展为一段专门讨论

**Priority 2 (Should-fix)**:
4. 将 Proposition 1 重定位为 motivating analysis，补充 entity 间 dependency 量化
5. 全文检查因果性语言残留
6. 将 N-scaling 和 cross-dataset 核心发现从 Appendix 移入正文
7. 补充 sequence entropy 等 token-level 信号比较
8. 主文标注 SciERC / cross-dataset 的 statistical power caveat
9. RE/SQL 降级为 preliminary evidence

**Priority 3 (Nice-to-have)**:
10. 合并 §9+§10 腾出空间
11. Table 2 扩展至 2+ 数据集
12. Figure 1 改用色盲友好色板
13. 统一 Table 显著性标注格式
14. 补充缺失引用（Fisch 2021, Chen 2021, Varshney 2022, Malinin & Gales 2021）
15. Page 7 display items 过挤——移 Table 至 Appendix 或合并
