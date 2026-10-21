---
round: 18
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-19T13:08:57.769802+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 18 (Fresh Review)

**论文**: "Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models"
**目标 Venue**: EMNLP 2026 via ARR May 2026
**Reviewer 编排**: 2 人（R1: 方法严谨性/统计/实验设计; R2: 新颖性/完整性/写作/Related Work）
**审稿模式**: Fresh（重新审稿）
**轮次**: 1 轮（Round 1 初审 + 交叉分享后达成共识，无需 Round 2）

---

## Summary

本文研究推理模型自我越狱（self-jailbreak）场景下，hidden-state (HS) 安全探针的层选择敏感性问题。使用 HarmThoughts 数据集上的四个推理 LLM（2 架构 × 2 规模），作者发现层选择指标的选择可以逆转 HS 探针是否优于文本探针的结论。Crossing-rate composite 指标系统性选择浅层（32B 模型 HS 优势消失），threshold-based 指标选择深层（3/4 模型显示显著 HS 精度优势，+19.2 至 +21.9pp，Holm-Bonferroni 校正）。该优势是 encoder-conditional 的（384d 编码器 4/4 HB，1024d 编码器仅 1/4 HB），且 32B 模型有模型特定 caveats。

---

## Strengths

**[S1] 层选择敏感性是真实且可推广的方法论发现。** 五指标消融 + random-CP control（100% 随机标签选浅层）+ cosine compression 分析（浅层 1.4–2.7× 距离压缩）提供了三条独立验证链。该发现不仅适用于安全探针，可推广至任何使用 threshold-based 检测的探针研究。[R1-S1, R2-S1, 完全共识]

**[S2] 统计框架超越 NLP 论文平均水平。** BCa bootstrap + exact sign-flip permutation test（枚举全部 2^n 排列）+ Holm-Bonferroni 两级校正 + nested CV + multi-seed stability + post-hoc power analysis。在 NLP 安全领域罕见的严谨程度。证据梯度框架（confirmed/significant/exploratory）是有用的分级方式。[R1-S3, R2-S2, 完全共识]

**[S3] 诚实透明的自评。** R1-32B position mediation (+1.9pp, p=0.914)、encoder-conditional 结果、32B 样本量限制、11–50% FPR、bug disclosure (App K) 均被清晰陈述而非掩盖。这在安全相关论文中尤为重要。[R1-S2, R2-S3, 完全共识]

**[S4] 负面结果信息密度高。** 7 种替代方法（BOCPD、CUSUM、Mahalanobis、RepE、MLP、CCS、cross-model transfer）的系统性失败定义了 CP 检测的四项要求（方向性、渐进性、模型特异性、线性可分性），为后续研究提供了排除清单和路标。[R1-S4, R2-S4, 完全共识]

**[S5] Capacity control 证据链完整。** PCA 384d（79–92% 方差保留）+ random projection 384d + 三编码器梯度（MiniLM 4/4 → E5 2/4 → BGE 1/4）构成收敛证据，部分排除纯容量解释。[R1-S5, R2-S5, 完全共识]

---

## Weaknesses

### Must-Fix（Critical + Major，须在修订中解决）

**[W1] (Critical) 32B 超参搜索空间与验证样本严重不匹配，缺 nested CV。** [R1-W1 Critical, R2-W8+交叉 AGREE Critical]

搜索空间高达 2,240 配置（64 层 × 7 W × 5 K × threshold），但 32B 验证集仅 n=4–10 per class。7–8B 模型有 nested 5-fold CV（缩减 13–25%），32B 明确承认 infeasible。Threshold-based 三指标收敛 L63 是有力的间接证据，但来自同一数据集的单次观察。如果 32B 也有 13–25% 缩减，部分 32B 结论可能不再显著。† 标记在快速阅读中容易被忽视，读者可能将 "all four models pass HB†" 理解为 robust 而非 exploratory。

**建议**: (a) 对缩减搜索空间（threshold-based 层 + W ∈ {1,3,5}）执行 nested CV，或 (b) 将 32B 推断统计结论弱化为 descriptive reporting（effect sizes without confidence claims），正文仅保留层选择和 divergence 描述。

**[W2] (Major) 核心贡献是观察性的，缺乏建设性方法论。** [R2-W1 Critical, R1 交叉 AGREE]

论文的中心发现是"层选择指标可逆转结论"——有用的方法论警示，但缺乏经验证的解决方案。Discussion 中的五步审计工作流仅以非正式 bullet points 呈现，未在任何 held-out 数据集或模型上前瞻性验证。作为方法论审计（类似 Hewitt & Liang 2019 control task），诊断本身有价值；但作为安全检测方法的进展，缺乏可部署的 takeaway。

**建议**: 至少在一个 held-out 设置（新模型或新数据集）中前瞻性验证五步工作流，或降低其定位从 "contribution" 到 "discussion"。

**[W3] (Major) HS 优势严重依赖弱基线，Abstract framing 不对称。** [R1-W4 Major, R2-W4 Major + W5 Minor, 强共识]

Against 384d MiniLM: 4/4 HB; against 1024d BGE-large: 1/4 HB（仅 OT-7B）; against E5-Mistral: 2/4 HB。三编码器梯度单调递减，暗示 HS 优势主要反映编码器弱点而非 HS 固有优势——论文 Discussion 自身承认 "represents information not yet captured by current sentence encoders rather than a fundamental modality difference"。但 Abstract 前置 "+19.2 to +21.9pp"（384d），"encoder-conditional" 延后至最后一句，权重严重不对称。此外，+19.2–21.9pp 范围排除了 R1-32B 的 +15.4pp（position-mediated）但包含 QwQ-32B 的 +19.2pp（position-competitive, 负 lead time），三个数字证据强度不均。

**建议**: Abstract 中在引用 precision 数字后立即注明 "against a 384-dimensional sentence encoder; the advantage narrows to 1/4 models against a 1024-dimensional encoder"。

**[W4] (Major) R1-32B 在 count-based claims 中膨胀表观泛化性。** [R1-W5 Major, R2 交叉 AGREE]

R1-32B 通过 HB (precision +15.4pp)，但 residualized gap +1.9pp (p=0.914)、residualized selectivity 3.0pp（低于 Hewitt & Liang 5pp 阈值）、coverage 25%、仅 W=1 显著、1024d CI 包含 0。论文自身判定为 "exploratory" 且 "largely positional"。但 "all four models pass HB†" 和 "three of four models" 等 count-based claims 将 R1-32B 与证据更强的模型并列。

**建议**: 在涉及模型计数的 claim 中使用 "two of four models (confirmed), one additional (significant but position-competitive), and one (exploratory)" 或类似分级措辞，而非笼统的 "three/four"。

**[W5] (Major) CR-composite vs. threshold-based 分类的 post-hoc 性。** [R1-W3 Major, R2 交叉 AGREE (部分保留)]

发现指标分歧 → 分类为两组 → 用同一数据报告——garden-of-forking-paths 风险。论文承认 "this classification is an empirical observation"，并提供三条独立验证（random-CP control、cosine compression、heatmap 系统性），比纯 post-hoc 更有说服力。底层现象（浅层压缩导致 crossing rate 膨胀）是可独立复现的物理事实。但具体分组方式可能是 dataset-specific 的。

**建议**: 增加 garden-of-forking-paths 讨论段；明确 random-CP 和 cosine compression 是独立验证而非原始发现的一部分。

**[W6] (Major) 单一数据集（HarmThoughts）且无 IAA 报告。** [R2-W3 Major, R1 交叉 AGREE]

所有实验使用 HarmThoughts 的 step-level CP 标注，未计算 inter-annotator agreement。CP 标注模糊性可能系统性偏移层选择结论。CP perturbation 分析（±2 步 <2.5pp 变化）部分缓解 random noise 但无法排除 systematic bias。

**建议**: 报告 HarmThoughts 的 harmful category 分布和 CP 位置特征；讨论 IAA 缺失对层选择结论的影响；如可能，在第二数据集上验证 Contribution 1。

**[W7] (Major) K=5 "pre-selection" 声明与正文描述矛盾。** [R1-W2 Major, R2 交叉 AGREE]

Section 3.5 "selected on the R1-8B validation set" 与 Appendix "pre-selected" 直接矛盾。K ablation (K=3,5,7 方向一致) 缓解实质担忧，但措辞不精确损害可信度。

**建议**: 统一为 "K=5 selected on R1-8B validation and held fixed across all models"，删除 "pre-selection"。

**[W8] (Major) 模型多样性不足——3/4 共享 Qwen 基座。** [R2-W2 Major, R1 交叉 AGREE]

仅 R1-8B 提供跨架构（Llama）证据。Section 5 声称浅层压缩是 "architecture-general" 但仅覆盖 2 个架构。对 Contribution 1（层选择敏感性）损害小于 Contribution 2（HS 优势），但泛化性声明缺乏充分支撑。

**建议**: Introduction/Abstract 使用更精确措辞如 "four reasoning models based on two architectures, with Qwen as the dominant base (3/4 models)"。

### Should-Fix（Minor，建议修订但非必须）

**[W9] (Minor) Introduction framing 暗示模态比较研究，实际贡献是方法论审计。** [R2-W6, R1 交叉 AGREE] 标题比 Introduction 更准确反映贡献。

**[W10] (Minor) 正文约 8.1–8.2 页，技术性超过 EMNLP 2026 的 8 页限制。** [R1-W8, R2-W7, 共识] Conclusion 开始于第 9 页上部。需进一步压缩。

**[W11] (Minor) GRU 实验使用不同数据划分（70/30 vs 60/20/20）。** [R1-W6, R2 交叉 AGREE] App E 提供 60/20/20 对照，但并非所有模型。

**[W12] (Minor) Selectivity 与 position contribution "正交" 声明缺形式化论证。** [R1-W7, R2 交叉 AGREE] 建议改为 "complementary"，正文引用 App F residualized selectivity 数据。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致（[AGREE]）：

| 编号 | 问题 | 严重性 | 一致性 |
|------|------|--------|--------|
| W1 | 32B nested CV 缺失 | Critical | 强共识 |
| W3 | HS 优势依赖弱基线 + Abstract 不对称 | Major | 强共识 |
| W4 | R1-32B 膨胀 count-based claims | Major | 强共识 |
| W6 | 单数据集无 IAA | Major | 强共识 |
| W7 | K=5 措辞矛盾 | Major | 强共识 |
| W8 | 模型多样性 3/4 Qwen | Major | 强共识 |
| W10 | 页数轻微超限 | Minor | 共识 |
| — | 定位 Findings | — | 强共识 |

## Reviewer Divergence

**唯一显著分歧：32B 结果篇幅分配（R2-W8）**

- **R2**: 32B 结果统计功效不足但占比偏高，挤占了可用于更强贡献（如验证审计工作流）的篇幅。建议减少。
- **R1**: [REBUT] 32B 是层选择敏感性最强证据来源（Table 2 中 QwQ L2 vs L63 是最引人注目的数据点；两个 32B 模型的 divergence 是独立有价值的发现）。不应删减内容，但应将推断统计弱化为 descriptive reporting。
- **Director 判断**: R1 的反驳成立——32B 结果对 Contribution 1 不可或缺。采纳 R1 建议：保留 32B 描述性内容，弱化推断统计。

**R2-W1 (Critical) 观察性贡献 vs R1 (部分 AGREE) 的 severity 差异**:
- R2 判定 Critical（缺建设性方案限制影响力）
- R1 同意实质但认为方法论审计类似 Hewitt & Liang (2019)，有独立价值
- **Director 判断**: 升级至报告级 Major。论文确实是诊断性而非处方性的，但诊断本身有价值。影响的是 venue 定位（Findings vs Main），而非论文的根本有效性。

---

## Questions

1. 为什么不在缩减搜索空间下对 32B 模型执行 nested CV？固定 W=1 + ~10 层候选，5-fold nested CV 完全可行。[R1-Q1, R2 交叉 AGREE]
2. AUROC 被排除的理由（threshold-free 无法诊断层选择偏差）逻辑成立，但 Appendix 中 AUROC 支持论文结论（△+12.1 to +15.1pp, all p<0.01）。不报告支持自己的指标反而留下 cherry-picking 印象。建议正文提及。[R1-Q5, R2 交叉 AGREE]
3. 给定三编码器梯度单调递减，未来更强文本编码器是否会完全消除 HS 优势？论文未提出不可约 HS 优势的理论论证。[R2-Q3]
4. CP "永久性" 假设是否总成立？是否存在 commitment 后短暂回到安全思考的 traces？如果存在 oscillating patterns，binary classification 框架需修改。[R2-Q4]
5. L2 正则化 C=1.0 是 sklearn 默认值还是选定的？C ∈ [0.01, 100] 扫描是 robustness check 还是 selection？论文应明确声明。[R1-Q2]
6. Trace-level bootstrap 能否充分捕捉 step-level variability？长 trace 对聚合指标贡献权重不成比例，但论文未讨论。[R1-Q3, R2 交叉 AGREE]

---

## Missing References

1. **Azaria & Mitchell (2023)**, "The Internal State of an LLM Knows When It's Lying" — 使用内部状态检测 LLM 不真实生成的基础工作，HS probing for safety 的直接先驱。Related Work Hidden-State Safety Detection 段应引用。[R2 提出, R1 交叉 AGREE]

2. **Turpin et al. (2023)**, "Language Models Don't Always Say What They Think" — 不忠实 CoT 的早期关键工作。与已引用的 chen2025unfaithful 互补。Related Work unfaithful reasoning 句中建议补充。[R2 提出, R1 认为非必须但合理]

---

## External Review

未配置外部审稿（项目配置中 `external_review.paperreview_ai.enabled` 未设置）。

---

## Visual Layout Check（非评分项）

视觉审查未执行（PDF 路径解析失败）。

基于 Reviewer 文本审查的格式观察：
- **正文页数**: ~8.1–8.2 页，Conclusion 开始于第 9 页上部。技术性超过 EMNLP 2026 的 8 页限制。[R1-W8, R2-W7]
- **模板**: `\usepackage[review]{acl}` ✓
- **匿名**: "Anonymous ARR Submission" ✓
- **Limitations section**: 存在且不计入页数 ✓
- **Responsible NLP Checklist**: Appendix A ✓
- **引用**: 61 bib entries, 97 citations, 0 orphan, 0 missing（R2 验证）
- **表格**: 小数精度基本一致

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3/5 | **3/5** |
| Excitement | 3/5 | 2/5 | **2.5/5** |
| Confidence | 4/5 | 4/5 | **4/5** |
| Overall Score | 3.5 | 3.0 | **3.0** |

### Overall Score: 3.0 (Findings)

**评分理由**:

论文识别了一个真实的方法论问题（层选择指标可逆转 HS vs. text 结论），实验设计和统计分析处于探针文献的高水准。五指标消融 + random-CP control + cosine compression 分析构成了有说服力的证据链。

三个因素将其定位在 Findings 而非 Main：

1. **观察性贡献缺乏建设性方案**: 论文诊断了问题但未提供经验证的解决方案。五步审计工作流仅以非正式 bullet points 呈现，未前瞻性验证。方法论审计有独立价值（类似 Hewitt & Liang 2019），但 scope 偏窄。

2. **HS 优势高度条件化**: 仅对弱编码器有效（1024d 下 1/4 HB），R1-32B 完全 position-mediated，QwQ-32B 负 lead time，所有模型 11–50% FPR。论文自身的最终定位 "characterize rather than production detectors" 是准确的，但也意味着实证贡献的可操作性有限。

3. **泛化性受限**: 单一数据集（HarmThoughts）无 IAA，3/4 模型共享 Qwen 基座，32B 验证集过小（2,240 configs vs n=4–10 per class 无 nested CV）。

论文的诚实和透明是其美德，统计严谨性值得肯定。在 Findings track 下，这些 limitations 可以接受；层选择敏感性的发现对安全探针社区有方法论价值。

---

## Detailed Comments

### Section 1 (Introduction)
- Introduction 第二段 ("whether a monitoring system should read the model's hidden states or its generated text") 建立了模态比较预期，但核心贡献是方法论审计——建议调整 framing 使预期对齐。标题比 Introduction 更准确。

### Section 2 (Related Work)
- 覆盖充分（61 bib entries, 2025–2026 最新工作）。
- 建议补充 Azaria & Mitchell (2023) 到 Hidden-State Safety Detection 段。
- Boxo et al. (2025) 仅一句话提及——鉴于其 "textual evidence leakage" 发现与本文层选择问题高度相关，建议 Discussion 中增加对比讨论。

### Section 3 (Method)
- K=5 措辞需统一（Section 3.5 vs Appendix 矛盾）。
- Section 3.3 "This classification is an empirical observation" 是正确的，但应增加 garden-of-forking-paths 的显式讨论。
- 建议说明 F1/AUROC/MCC 排除原因（AUROC 在 Appendix 中实际支持结论，不报告反留 cherry-picking 印象）。

### Section 4 (Experiments)
- Table 3 count-based claims ("all four models pass HB†") 应改为分级措辞。
- 32B 的推断统计（p 值、HB 通过）建议弱化为 descriptive reporting 或移入附录，正文保留 effect sizes 和层选择/divergence 描述。
- Section 4.2 "selectivity measures label structure [...] orthogonal to position contribution" — "正交" 应改为 "complementary"，并引用 App F residualized selectivity。

### Section 5 (Discussion)
- "shallow-layer compression is architecture-general" — 仅 2 个架构证据（1 Llama + 3 Qwen），应限定措辞。
- 五步审计工作流应从 "recommend" 降为 "propose"（已部分完成），并标注 "prospective validation needed"。

### Section 6 (Conclusion)
- 需落在第 8 页以内——压缩 Discussion 或 Related Work。

### Section 7 (Limitations)
- 单数据集应保持为首要限制。
- 建议增加 IAA 缺失对层选择结论的具体影响讨论。

### Abstract
- **最关键的修订**: 应同时报告 384d 和 1024d 结果（"+19.2 to +21.9pp precision against a 384d encoder (HB corrected); against a 1024d encoder, only 1/4 models survives correction"）。
- 应区分 7–8B（robust）和 32B（exploratory/position-mediated）。
- "+19.2 to +21.9pp" 范围排除 R1-32B 但包含 QwQ（position-competitive, 负 lead time）——证据强度不均应体现。