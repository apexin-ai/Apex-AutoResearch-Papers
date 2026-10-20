---
round: 24
review_mode: fresh
overall_score: 3.5 - Borderline Conference
timestamp: 2026-05-20T13:24:41.065902+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 25 审稿报告

**论文**: "Strong Predictors, Weak Selectors: Addressing the Correlation-Selection Gap in Self-Consistency for Named Entity Recognition"
**Venue**: EMNLP 2026 Long Paper (ARR May 2026)
**Reviewers**: R1（方法严谨性 + 实验设计 + 统计分析）, R2（新颖性 + 完整性 + 写作质量）
**日期**: 2026-05-20

---

## Summary

本文研究自一致性（self-consistency）在 NER 中的失效机制。作者构建包含五种置信度信号（SJ, VC, FK, EM, LP）的诊断框架，在四个 NER 基准上系统评估质量估计与样本选择两个维度，发现所有信号均能可靠估计生成质量（ρ up to 0.45, AUROC up to 0.82）但无法有效执行样本选择——即"correlation-selection gap"。论文识别三种结构性故障模式（instance degeneracy、isolated headroom、LP compression），提出 entity-level construction（形式化为 MBR decoding）部分弥合该差距（Few-NERD +1.40pp, SciERC +1.02pp），并给出退化分解上界。

## Strengths

**S1. QE vs. selection 的正交分解是最有概念价值的贡献。** 将 test-time scaling 分解为"能否判断好坏"和"能否据此选出好的"两个可独立评估的维度，结构清晰可操作。五种信号跨四个 NER 基准的全面评估提供了比现有文献更细粒度的理解。（两位 Reviewer 共识）

**S2. 统计处理水准在 NLP 论文中属上乘。** Bootstrap CI（Table 13）、Holm-Bonferroni 多重检验校正（k=57）、TOST 等价性检验（Table 16, Appendix F）、permutation tests（Table 9），不显著结果如实报告（SciERC p_adj=0.20）。（两位 Reviewer 共识，特别认可）

**S3. Entity construction 与 MBR 的形式化联系。** Proposition 1（§6.1）将 entity-level majority vote 推导为 MBR decoding with balanced set-overlaps，提供清晰的决策论基础。

**S4. 极其详尽的补充材料。** 28 页 appendix 覆盖 N-scaling、temperature、seed stability、per-entity-type analysis、free-form decoding ablation、cross-dataset OOD 等。在 NLP 论文中罕见的 thoroughness。

**S5. 实用的诊断协议。** §Z 的三步协议为从业者提供可直接使用的工作流。

## Weaknesses

### 两位 Reviewer 共识的 Must-Fix 问题

**[CONSENSUS CRITICAL] W1. Correlation-selection gap 的 by-construction 成分未区分**
- R1-N1 + R2-N1。4/5 信号（SJ, VC, FK, EM）是 instance-level 的，§3.1 已明确定义其对 N 个候选打相同分数——selection 失效是定义推论而非经验发现。论文将五种信号的 gap 统一呈现为需要"diagnose"的"surprising finding"，夸大了经验性成分。唯一具备 per-sample discrimination 的 LP 确实展现了部分 selection 能力但被 compression 限制。
- **交叉共识**: R2 认为这是 tautology 层面的过度宣传；R1 认为 LP 分析和 governing factors 的 empirical 贡献被 R2 略微低估。两位均同意需明确区分 definitional gap 和 empirical gap。
- **历史**: 此问题自 Round 23 持续存在（R23-N2, in_progress），本轮两位 Reviewer 再次独立提出。
- **建议**: §4 首段明确区分 definitional gap（instance-level signals by design cannot select）和 empirical gap（LP has per-sample discriminability but compression limits effectiveness）。重新校准 Abstract/Intro 叙事，移除对 instance-level signals 的 "surprising"/"diagnose" 框定。

**[CONSENSUS CRITICAL] W2. Cross-dataset 分析（n=23, ρ=0.052, p=0.81）严重 underpowered**
- R1-N2 (critical) + R2 交叉 AGREE。23 个 configurations 的 statistical power 极低：检测 ρ=0.3 at α=0.05, 80% power 需要 n≈85；当前 power 仅约 50%（for ρ=0.4）。"Degeneracy does not predict LP gain" 的 null 结论不可靠。
- R2 补充：decomposition 的数学有效性不依赖此 null finding，但 degeneracy 的 interpretive status（diagnostic indicator vs. predictive variable）受影响。
- **建议**: (1) 报告 post-hoc power analysis，明确可检测的最小 ρ；(2) 将结论从"does not predict"改为"we did not find evidence for prediction, but the analysis is underpowered (n=23)"；(3) 如有可能增加 configurations。

**[CONSENSUS CRITICAL] W3. §5.1/§5.3 包含未完成工作**
- R2-N2 (critical) + R1 AGREE。§5.1 Cross-Model SC 标注"preliminary"（仅 SciERC 一个数据集初步结果 +0.12pp）；§5.3 SCD 标注"ongoing"且完全无实验结果。ARR 提交 incomplete work 会被 AC 视为 premature。
- R1 纠正 R2 的节号：实际为 §5.3（非 §5.2），§5.2 Trained Verifiers 有完整实验（AUC=0.923±0.002）可保留。
- **建议**: 删除 §5.3 全部内容，§5.1 要么补完（多数据集多模型组合）要么降级为 Discussion/Future Work。

### 存在分歧的问题

**[DIVERGENCE] W4. Entity construction 贡献度**
- **R2 判 critical** (N3): entity construction = Florian et al. (2003) entity voting + LP weighting，增量仅 +1.0-1.4pp vs greedy，LP-weighted vs uniform 差异 0.15-0.35pp，新颖性有限，作为独立贡献过弱。
- **R1 REBUT**: 参照基准应为 greedy 而非 uniform weighting；Few-NERD 恢复 ~34% oracle gap（非 R2 估的 25%）；MBR 形式化（Proposition 1）有独立理论贡献；无需训练的 unsupervised 方法在 selection 大面积失败的背景下有方法论价值。
- **Director 判断**: 作为独立方法贡献确实增量性较强，但作为诊断框架的 proof-of-concept 合理。R24 已将其从"principled resolution"降级为"diagnostic-motivated mitigation"，这一定位正确，不应再作为核心卖点。

### 两位 Reviewer 共识的 Should-Fix 问题

**[CONSENSUS WARNING] W5. SciERC entity construction p_adj=0.20 不显著；仅 1/4 数据集显著**
- R1-W1 + R2 AGREE 并加强。Few-NERD +1.40pp 显著，但 SciERC +1.02pp 校正后 p_adj=0.20 不显著；CoNLL 增益为负（−0.29pp）。4 个数据集中仅 Few-NERD 显著。
- **建议**: 正文更醒目标注 SciERC p_adj=0.20，讨论仅 1/4 显著的适用范围含义。

**[CONSENSUS WARNING] W6. k=57 Holm-Bonferroni family 定义不透明**
- R1-W2 + R2 AGREE。57 个检验的构成从未说明。Family 定义直接影响校正严格程度。
- **建议**: Appendix 列出构成规则或完整明细。

**[CONSENSUS WARNING] W7. 72B zero-shot vs 8B fine-tuned 三因素混淆**
- R1-W3 + R2 AGREE。同时变化 scale + training regime + quantization，但 §6.2 从中得出 scaling 结论。Limitations 已坦承但正文未 hedge。
- **建议**: §6.2 结论明确标注 confounded comparison。

**[CONSENSUS WARNING] W8. Seed 数量偏少（SciERC 2-seed, 主要结果 3 seeds）**
- R1-W4 + R2 PARTIAL AGREE。SciERC n=529 高方差任务 2-3 seeds 效力有限。R2 认为 Appendix H 的 signal ranking stability 部分回应此 concern。
- **建议**: 对 SciERC entity construction 核心结果增加到 5 seeds。

**[CONSENSUS WARNING] W9. Proposition 1 entity-wise independence 假设未验证**
- R1-W5 + R2 AGREE。NER 中 entities 间有强依赖（嵌套实体、句法约束、竞争标注）。R2 补充 degenerate subsets 上 entity construction 失效可能正是 independence violation 导致。
- **建议**: 提供经验验证或讨论违反程度。

**[CONSENSUS WARNING] W10. Degeneracy bound 极度松弛（实际恢复率 3-12%）**
- R1-W6 + R2 PARTIAL AGREE。R1 认为预测能力极弱；R2 认为 diagnostic 价值仍在（识别 α 为 bottleneck）。两者同意需明确定位。
- **建议**: 明确 bound 为 diagnostic（识别 bottleneck）而非 predictive，讨论 tightening 方向。

**[CONSENSUS WARNING] W11. 缺 API 模型和 Self-Certainty/P(True) per-sample signals**
- R2-W1 + R2-W2, R1 均 AGREE。scope 限于 open-weight models（LP 在 API 场景不可用）；Self-Certainty/P(True) 未测试但理论上可绕过 selection gap。
- **建议**: Limitations 明确声明 scope 限于 open-weight；Related Work/Discussion 实质性讨论 per-sample confidence 方法。

**[R2 UNIQUE] W12. NER-only 实验无法支撑 "structured prediction" framing**
- R2-N1。Abstract/Intro 叙事推广到 structured prediction，但仅有 NER 实验。Appendix M RE 结果显示 structural signals 在 RE 上接近零——直接挑战框架的通用性。
- **建议**: 严格限定叙事为 NER，或将 RE 结果提升到正文讨论局限性。

**[R2 UNIQUE] W13. 引用质量问题**
- R2-W4。4 条引用未通过 OpenAlex 验证（hobelsberger2025, lightman2024, venktesh2025, aggarwal2023），3 条实质性元数据不匹配，17 条 orphan bib entries。

**[CONSENSUS WARNING] W14. 与 Yao et al. (2026) 差异化不足**
- R2-W3, R1 AGREE with nuance。两篇论文 high-level finding 重叠，需 head-to-head 对比段落。

### 其他 Should-Fix (R2 独有)
- **W15. LP compression 缺与 LLM 校准文献的机制性对接**（R2-W1）
- **W16. 三种故障模式呈 cascade 而非正交关系**（R2-W2）——应重构为 diagnostic cascade
- **W17. Related work 缺 process reward models / self-refinement / diverse beam search 讨论**（R2-W3）
- **W18. N-scaling 分析未与 degeneracy decomposition 联系（D(N), bound(N)）**（R2-W5）

### 小问题（不影响接收）
- Table 2 "n/a" / "†" 标记分散（R1）
- Figure 1 面板注释 6-7pt 偏小（R1, 视觉审查）
- §3.2 Eq.1 Soft Jaccard 分母 max vs union 选择理由（R1, R2）
- Appendix Z 缺 degeneracy > 70% fallback（R1, R2）
- F1 变体和术语命名不一致（R2-W4, R1 AGREE）
- Figure 2 灰度打印可读性弱（R2）
- §6.3 decomposition 正文缺 intuitive explanation（R2）
- Limitations section 偏长（R2）

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成共识：
1. ✅ By-construction gap 需分层叙事（R1-N1 + R2-N1: AGREE）
2. ✅ §5.1/§5.3 未完成工作不应在 ARR 提交（R2-N2: R1 AGREE）
3. ✅ Cross-dataset null 结论 underpowered（R1-N2: R2 AGREE）
4. ✅ SciERC p_adj=0.20 不显著限制 generalizability（R1-W1: R2 AGREE 并加强）
5. ✅ k=57 family 需透明化（R1-W2: R2 AGREE）
6. ✅ 72B comparison confounded（R1-W3: R2 AGREE）
7. ✅ Entity-wise independence 需验证（R1-W5: R2 AGREE）
8. ✅ 缺 Self-Certainty/P(True) 实质性讨论（R2-W2: R1 AGREE）
9. ✅ Yao et al. 差异化不足（R2-W3: R1 AGREE）
10. ✅ 术语不一致（R2-W4: R1 AGREE）

## Reviewer Divergence

1. **Entity construction 贡献度**: R2 判 critical（增量过小，MBR 直接应用），R1 REBUT（34% oracle gap, MBR 理论贡献独立）。Director 判断：作为诊断副产品合理，不应作为核心卖点。
2. **附录长度**: R2 认为 30 页暗示 scope 过大，R1 REBUT（诊断性论文附录长正常，问题在于引用未完成内容）。
3. **Degeneracy bound 价值**: R1 认为预测能力极弱，R2 认为 diagnostic 价值仍在。两者对 bound 实用性期望不同，但都同意需明确定位。

## Questions for Authors

1. 能否量化 correlation-selection gap 中 definitional（instance-level by design）vs empirical（LP compression）的比例？
2. Cross-dataset analysis (n=23) 的 post-hoc power 是多少？80% power 下可检测的最小 ρ？
3. Holm-Bonferroni k=57 的 57 个检验具体构成？
4. Entity-wise independence（Proposition 1）在嵌套实体和 fine-grained types 上的近似程度？
5. §5.1/§5.3 完整实验何时完成？若来不及，是否移至 Future Work？
6. Appendix M 的 RE 结果是否意味着框架是 NER-specific 的？
7. Self-Certainty 在 constrained decoding 下是否可用？与 entity construction 的优势对比？
8. LP compression 的机制成因？是否尝试过 per-entity LP？
9. Free-form decoding 下 LP selection 更有效（Appendix O）——为何不在正文 highlight？
10. Trained verifier AUROC=0.987 但 selection 增益仅 +4.23pp——这是否是最有冲击力的 finding？

## Missing References

两位 Reviewer 共同建议：
- Malinin and Gales (2021) — structured prediction 中 predictive uncertainty
- Xiong et al. (2024) — uncertainty quantification survey

R1 额外建议：
- Gleave and Irving (2022) — reward model overoptimization

R2 额外建议：
- EL4NER (arXiv:2505.23038) — multi-LLM ensemble for NER
- Structure-Conditional MBR (EMNLP 2025) — MBR for structured outputs
- Self-Certainty for Best-of-N (arXiv:2502.18581) — per-sample signal
- G2: Guided Generation for Diversity (arXiv:2511.00432)

R2 引用审计：4 条未通过在线验证，3 条元数据不匹配，17 条 orphan bib entries（详见 W13）。

## External Review

外部审稿：未启用（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-20 12:47–12:50）。发现 1 critical + 4 warning + 9 info：

**Critical:**
- **Page 31**: Figure 10 是文字占位符（"[Figure placeholder: Oracle F1 (N) scaling curves]..."），未渲染实际图表。审稿人会立即判断论文未完成。

**Warning:**
- **Page 1-2**: 连续 2 页纯文本（Abstract + Introduction + Background），首个 display item（Figure 1）直到第 3 页才出现。前 25% 无视觉支撑。
- **Page 5**: 又一个纯文本页（§5 + §6），与 p1-2 形成不均匀节奏。
- **Page 7**: Tables 3, 4, 5 + Figure 3 同页过度拥挤，Figure 3 被挤压。
- **Page 7**: Figure 3 尺寸过小，坐标轴标签接近可读性下限。

**Info:** Figure 1 面板注释 6-7pt; Figure 2 颜色区分度好; Table 1 booktabs 规范; 主体 9 个 display items 密度合理; 附录 25 页 thoroughness 好; 参考文献格式统一无未解析引用; Figure 6 热力图色阶对色盲不友好; Figure 7 偏小但附录可接受。

## Overall Assessment

### 综合评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | **3.5/5** |
| Excitement | 3/5 | 3/5 | **3/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5 | 3.5 | **3.5 (Borderline Conference)** |
| Confidence | 4/5 | 4/5 | 4/5 |

### Overall Assessment: 3.5 — Borderline Conference

这是一篇执行质量很高的诊断性论文。QE vs. selection 的正交分解是有价值的概念贡献，统计处理在 NLP 论文中属上乘，28 页 appendix 展现了极强的 due diligence。

**三个必须解决的核心问题：**

1. **叙事诚信**: Correlation-selection gap 的 4/5 是 definitional 而非 empirical finding，论文 framing 制造了虚假 surprise。需明确分层：definitional gap → empirical gap（LP compression, governing factors）。

2. **统计效力不足**: Cross-dataset null 结论基于 n=23 underpowered 分析；SciERC 核心结果 p_adj=0.20 未过多重检验；4 个数据集中仅 1 个 entity construction 增益显著。

3. **未完成内容**: §5.1 "preliminary" + §5.3 "ongoing" 在 ARR 提交中不可接受；Appendix Figure 10 是文字占位符。

**Rebuttal 关键路径：**
- (a) 重构叙事分离 definitional vs. empirical gap
- (b) 删除 §5.3，§5.1 补完或移至 Future Work
- (c) 补充 power analysis，软化 null 结论措辞
- (d) 替换 Figure 10 占位符
- (e) 增加 SciERC seeds 或坦承 entity construction 仅在 Few-NERD 显著

若 (a)-(d) 在 rebuttal 期间完成，论文有望升至 4.0 (Conference)。

## Detailed Comments

### §1 Introduction
- 收紧 structured prediction/structured IE 叙事为 NER-specific（R2-N1）
- 将 "surprising finding" 框定改为 "systematic characterization"（R1-N1, R2-N1）

### §2 Related Work
- 增加与 Yao et al. (2026) 的 head-to-head 段落（R2-W3, R1 AGREE）
- 讨论 process reward models、self-refinement、diverse beam search（R2-W3）
- Self-Certainty/P(True) 概念性讨论（R2-W2, R1 AGREE）

### §3 Methodology
- Eq.1 Soft Jaccard 分母 max vs union 选择理由（R1, R2）
- 术语统一：F1 变体、signal 缩写（R2-W4, R1 AGREE）

### §4 Diagnostic Framework
- 首段明确区分 definitional gap 和 empirical gap（R1-N1, R2-N1 核心修改点）
- LP compression 与 LLM 校准文献对接（R2-W1）

### §5 Adaptive Methods
- 删除 §5.3 SCD（R2-N2, R1 AGREE）
- §5.1 补完或降级（R2-N2, R1 AGREE）
- §5.2 Trained Verifiers 保留

### §6 Theory
- Proposition 1 entity-wise independence 需验证或讨论（R1-W5, R2 AGREE）
- §6.2 scaling 结论 hedge confounded comparison（R1-W3, R2 AGREE）
- §6.3 bound 明确为 diagnostic 而非 predictive（R1-W6, R2 PARTIAL AGREE）
- 三因素改为 cascade 叙事（R2-W2）

### §7 Experiments
- §7.3 cross-dataset null 结论加 power analysis 和 hedging（R1-N2, R2 AGREE）
- §7.5 SciERC p_adj=0.20 更醒目标注（R1-W1, R2 AGREE）
- k=57 family 明细（R1-W2, R2 AGREE）
- 考虑提升 trained verifier gap-persists finding 到正文（R2 Q4）

### Appendix
- Figure 10 占位符必须替换（视觉审查 critical）
- N-scaling 与 D(N)/bound(N) 联系（R2-W5）
- §Z 增加 degeneracy > 70% fallback（R1, R2）
- 清理 orphan bib + 核实引用问题（R2-W4）