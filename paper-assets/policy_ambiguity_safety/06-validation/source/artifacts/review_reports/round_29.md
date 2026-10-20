---
round: 29
review_mode: fresh
overall_score: 3.5 — Borderline Conference
timestamp: 2026-05-24T09:46:33.509048+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 29 Consolidated Review Report

**Paper**: "Policy Ambiguity Is Nocuous: Clause-Level Causal Effects on Customer-Service Agent Safety"
**Venue**: EMNLP 2026 (ARR May cycle)
**Reviewers**: R1, R2
**Cross-Response Convergence**: High (both 3.5, consensus on core issues, one factual correction)

---

## Summary

The paper investigates how policy ambiguity at the clause level causally affects LLM agent safety in customer-service scenarios. It contributes a 6-type ambiguity taxonomy, a 300 matched-pair benchmark (τ²-bench), and three empirical claims: (C1) ambiguous clauses cause significantly more safety violations than disambiguated counterparts (+31.2pp), (C2) the effect is robust across 5 frontier models and transfers to real-world SOPs (+12.7pp, 3/5 significant), and (C3) ambiguity type predicts failure mechanism (V=0.45) but not violation rate (V=0.14). The work positions itself as the first causal study of policy ambiguity effects on LLM agents.

## Strengths

**S1. Rigorous causal design.** The matched-pair paradigm with minimal-edit perturbation (Δ_perturb ≈ −0.67pp) provides strong causal evidence, distinguishing this work from prior correlational studies (e.g., DRIP-R). The McNemar test (OR = 15.1, p < 0.001) and multi-model replication strengthen internal validity.

**S2. Comprehensive taxonomy grounded in requirements engineering.** The 6-type ambiguity taxonomy bridges NLP and RE literature, with clear operational definitions and illustrative examples. The distinction between linguistic (4 types) and specification (2 types) layers is well-motivated.

**S3. Practical relevance.** The prevalence audit (87% of real-world policies contain ambiguous clauses) and SOPBench transfer experiments connect the controlled findings to deployment scenarios. The "convergent nocuity" concept (cross-model Jaccard = 0.46) highlights a systemic risk beyond individual model performance.

**S4. Thorough appendix.** The 25-page appendix provides judge prompts, annotator protocols, full clause templates, per-model breakdowns, temperature pilot data, and bootstrap CIs, supporting reproducibility.

**S5. Strong effect size on primary claim.** Pooled Δ = +31.2pp with 95% CI [28.4, 34.0] is a large, practically significant effect with narrow confidence intervals.

## Weaknesses

### Must-Fix

**MF1. 正文疑似超出 EMNLP 2026 严格 8 页限制** [R1-W6, R2-N1; 共识]

§1–§7（不含 Limitations）目视估计约 8.5–8.7 页，超出约 0.5–0.7 页。Limitations 和 Ethics Statement 不计入页数（EMNLP 2026 规则），但 "Data and Code Availability" 通常计入。这是硬格式约束，必须修正。

**MF2. Human κ = 0.41 不足以支撑 C3 type-mechanism dissociation 定位** [R1-N1, R2-N2(c); 强共识]

Re-annotation（A1 vs. A3, collapsed taxonomy）yields κ = 0.41，低于 Krippendorff (2004) α ≥ 0.667 阈值。虽从 R28 的 LLM coder κ = 0.15 显著改善，但 0.41 仍处于 "tentative conclusions only" 区间（0.40–0.667）。§6 的 "diagnostic instrument" 定位和摘要的 claim 在此可靠性水平下不充分。

**事实性澄清**：R2 初始审稿将 Table 16 中 "Type × violation rate" 行的 V = 0.137 误认为 type-mechanism V 值。R1 交叉回应中纠正：V = 0.137 测量类型是否预测违规率（"WHETHER they fail"），而非类型→机制关联。正确的 type-mechanism V = 0.446（3-way）/ 0.363（5-way），均达 Cohen medium effect size。摘要 "V = 0.45 vs. 0.14" 对比的是这两个维度，论述正确。

C3 的真正弱点在于：(a) NMI = 0.23 仅 moderate；(b) 人工 κ = 0.41 不足。

### Should-Fix

**SF1. "Ambiguity" umbrella term 概念张力** [R2-W1; R1 部分同意]

Incompleteness 行为显著不同于其他类型（violation rate 55.6% vs. 31.6–43.6%；Δ = +49.2pp vs. coreferential +18.7pp），且其 "消歧" 本质是 information addition 而非 disambiguation。操作层面的 pragmatic justification（§3: "LLM agents process all six types identically"）合理，但概念张力应在 §3 中显式讨论。RE 文献有先例（Berry et al., 2004; Dalpiaz et al., 2018），但需要论文主动承认 trade-off。

**SF2. SOPBench 效应衰减（+31.2pp → +12.7pp）解释不充分** [R1-W2, R2-W2; 共识]

从 τ²-bench 到 SOPBench 的效应量下降显著但 underexplained。Clause density、inter-clause interactions、system prompt buffering 被提及但未测试。建设性建议：τ²-bench 的 constraint-level（而非 clause-level）重聚合分析可作为中间粒度验证——如果效应在此水平已衰减，则 measurement-granularity 解释成立。

**SF3. Temperature=0 greedy decoding 可能人为放大 convergent nocuity** [R2-W3, R1-W4; 共识，R2 论证更尖锐]

Greedy decoding 下每个模型产生确定性单一输出。如果模型最可能行为是违规，则 100% 违规。Cross-model convergence 可能部分反映确定性 decoding 下高置信度 token 的系统性重叠，而非独立共享的深层脆弱性。

温度 pilot（Appendix AH）显示 t=0.7 时 97% clause-condition pairs 仍 unanimous，但：(1) 仅基于 50 pairs（underpowered）；(2) 不报告 per-clause Jaccard。建议：扩展至 300 pairs 并在 convergent nocuity 讨论中明确承认 greedy decoding 作为 potential confound。

**SF4. Prevalence audit 样本选择偏差** [R2-W4, R1-M5; 共识]

87% 来自公开消费者政策文档，可能低估内部操作手册（更技术化、更多 incompleteness/conditional precedence）或高估法律审核后的企业政策的 ambiguity。这限制了泛化性。建议在讨论中明确样本来源和局限。

**SF5. Cross-family vs. within-family Jaccard 证据不够有力** [R2-W5, R1-W5; 共识]

Within-family (GPT-5.4/GPT-4.1) Jaccard = 0.54，cross-family mean = 0.46，差异仅 0.08。Qwen3/DeepSeek (0.55) 甚至超过 within-family pair。无 bootstrap CI 或 permutation test 验证差异显著性。Jaccard 在 sparse binary vectors 上的 floor effect 削弱区分力。Convergent nocuity 的 "beyond training data overlap" 论证需要统计支持。

### Minor Issues

**M1.** Abstract "(1.3)" 指代不明——应删除或解释。[R2; R1 agrees]
**M2.** Figure 3 y 轴标签可更精确。[R2; R1 agrees]
**M3.** Table 2 脚注信息密度过高，可部分移入正文或 appendix。[R2; R1 agrees]
**M4.** Figure 1 文字偏小。[R2; R1 agrees]
**M5.** 引用格式小问题。[R2; R1 agrees]
**M6.** "Disambiguation neglect" 术语合理（R1 rebuts R2 的 "ambiguity blindness" 建议——neglect 强调行为选择，blindness 暗示认知能力，当前用语更精准）。无需修改。

## Questions for Authors

**Q1.** t > 0 是否显著降低 cross-model Jaccard？当前 pilot 不报告 per-clause Jaccard——全 300 pairs 的 t=0.7 Jaccard 数据将直接检验 convergent nocuity 是否部分为 greedy decoding artifact。[R2-Q1; R1 agrees]

**Q2.** AMI（Adjusted Mutual Information）是否会给出与 NMI=0.23 materially different 的 type-mechanism 关联评估？AMI 校正 chance-level agreement，是聚类评估中更标准的度量。[R2-Q2, R1-Q4; 共识]

**Q3.** τ²-bench 的 constraint-level（而非 clause-level）重聚合后效应量如何？这一中间粒度可诊断 SOPBench 衰减的原因。[R2 constructive suggestion]

**Q4.** Prevalence audit 的 raw inter-annotator κ（consensus 前）是多少？96% initial agreement 在 87% prevalence 下的 κ 会受 base rate 影响。[R1-related]

**Q5.** 对 DRIP-R 的 "correlational design" 定性是否得到原作者认可？R1 认为这是标准的方法论区分（correlational vs. experimental），但建议作者确认 DRIP-R 团队的看法。[R2-Q4; R1 defends but suggests confirmation]

## Missing References

1. **Bommasani et al. (2022) "On the Opportunities and Risks of Foundation Models"** — Convergent nocuity (§6.3) 与 "monoculture risk" / homogenization thesis 直接相关。不同架构模型在 ambiguous clauses 上收敛于相同违规，可能反映训练数据或 RLHF 的同质化。引用此文可加强理论锚定。[R2 提出; R1 strongly agrees]

2. **Cemri et al. MAST failure taxonomy** — 如果存在，其 failure mode 分类与 §6 type-mechanism mapping 直接对比。请作者验证并酌情引用。[R2 提出; R1 agrees]

3. **Wang & Feng (2026) vs. Weng et al. (2026)** — R2 建议补充 "Wang & Feng (2026) Policy Invariance"，R1 指出论文已引用 "Weng et al. (2026)"，可能为同一工作。请作者确认。[R2 提出; R1 partially rebuts]

## External Review

外部审稿未请求。

## Visual Layout Check（非评分项）

**状态**: ✅ 完成 (2026-05-24 09:22–09:25)
**统计**: 0 critical / 2 warning / 6 info

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ Warning | pp.1–2 | 前两页纯文本（Abstract + Intro + Related Work），无 display item。Figure 1 直到 p.3 才出现，审稿人前 2 分钟无视觉锚点 |
| ⚠️ Warning | p.8 | 三个 display items（Table 2 + Fig 4 + Fig 5）堆积，Fig 4/5 尺寸偏小，Fig 5 Jaccard heatmap 单元格文字打印尺寸下可能难辨 |
| ℹ️ Info | p.8 | Fig 4 heatmap 数字字号约正文 60-65%，建议增大或用 figure* 全宽展示 |
| ℹ️ Info | p.3 | Fig 1 红/橙/黄/绿色阶对红绿色盲用户区分度有限（文字标签部分弥补） |
| ℹ️ Info | pp.1-9 | 跨 figure 颜色方案不完全一致，但服务于不同可视化目的，可接受 |
| ℹ️ Info | p.14 | Appendix 表格密集（Tables 4-7 集中一页），作为附录可接受 |
| ℹ️ Info | pp.10-11 | 参考文献格式统一，无 [?] 未解析引用 |
| ℹ️ Info | p.5 | Method 部分纯文本页，作为实验设计描述属正常范畴 |

## Overall Assessment

**评分: 3.5 — Borderline Conference**

两位 Reviewer 评分一致 (3.5/3.5)，交叉回应后共识度高。

本文在研究设计上具有明确的因果推断优势——matched-pair paradigm 是对该领域先前 correlational work 的实质性方法论推进。C1（ambiguity causes violations, +31.2pp）和 C2（cross-model robustness + SOPBench transfer）有充分的统计支持。

**阻碍升至 4.0 (Conference) 的关键问题：**

1. **C3 人工验证不足** (MF2)：κ = 0.41 低于可接受阈值，削弱了 type-mechanism dissociation 这一独立贡献的可信度。如果 C3 被视为 tentative 而非 established，论文的贡献从三个 claims 缩减为两个（C1 + C2），novelty 边际降低。

2. **格式合规性** (MF1)：正文疑似超出 8 页限制——EMNLP 2026 硬约束。

3. **Convergent nocuity 证据链不完整** (SF3 + SF5)：greedy decoding confound 未被排除 + Jaccard within/cross gap 缺乏统计检验。概念有启发性但论证不够严密。

**升分路径：**
- (1) 扩大人工标注至 κ ≥ 0.60，或明确将 C3 降级为 exploratory finding + 调整 abstract/introduction claims
- (2) 修正页面超限
- (3) 扩展温度 pilot（300 pairs, per-clause Jaccard）并在讨论中承认 greedy decoding confound

如果 (1) 和 (2) 在 revision 中解决，评分可提升至 3.5–4.0 区间。当前评分反映：C1+C2 quality 值得 Conference，但 C3 不可靠 + 格式问题将其拉回 Borderline。

---

## Appendix: 交叉回应关键分歧裁定

| 议题 | R1 | R2 | 裁定 |
|------|----|----|------|
| V = 0.137 解读 | REBUT：V=0.137 是 type→violation rate，正确 type-mech V=0.446 | 引用 V=0.137 作为 type-mechanism 证据 | **R1 正确** — R2 误读 Table 16 |
| "Disambiguation neglect" vs "ambiguity blindness" | REBUT：neglect 强调行为选择，更准确 | 建议 "ambiguity blindness" | **R1 正确** — 概念区别合理 |
| DRIP-R characterization | REBUT：correlational vs experimental 是标准区分 | 质疑公平性 | **R1 正确** — 方法论区分合理 |
| Annotator bias (87%) | REBUT：96% agreement ≠ bias；87% 与 RE 文献一致 | 质疑 annotator bias | **R1 更有理** — 更大 concern 是样本选择偏差 |
| Wang & Feng vs Weng | REBUT：可能为同一引用 | 建议补充 | **需作者确认** |