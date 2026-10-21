---
round: 12
overall_score: 3.0 Findings
timestamp: 2026-05-18T14:31:39.976026+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 Consolidated Review Report
## contrastive_trace_safety → EMNLP 2026 (ARR May 2026 cycle)

**Reviewers**: R1 (方法严谨性 + 统计分析), R2 (新颖性 + 完整性 + 写作)
**Rounds**: 1 (初审 + 交叉分享，达成共识)
**Convergence**: Round 1 达成共识，两位 Reviewer 独立给出 Overall 3.0 (Findings)

---

## Summary

本文系统比较了 hidden-state (HS) 探针与 text-based 探针在推理模型安全承诺点 (Safety Commitment Point, CP) 检测中的表现。核心发现有三：(1) layer selection 是关键的 researcher degree of freedom，基于 balanced accuracy × crossing rate 的复合指标系统性地为 32B 模型选择浅层，掩盖了 HS 优势，而基于 threshold-dependent metrics 的选择恢复了显著性；(2) HS 优势是 encoder-conditional 的，从 MiniLM-384d 到 BGE-large-1024d，HB-significant 模型数从 4/4 降至 1/4；(3) 七种替代方法（GRU、RepE、Mahalanobis、PCA cosine、BOCPD、CUSUM、change-point）均无法稳定匹配监督探针。实验覆盖 4 个模型（2 架构 × 2 规模），FPR 39-52%，oracle gap 85.5%。论文定位为现象描述而非生产级检测器。

---

## Strengths

**S1. Layer selection sensitivity 是有价值的方法论贡献 [R1, R2 共识]**
论文以严谨的消融实验揭示了 layer selection 对 probing 结论的决定性影响。5-metric ablation (Table 2) 清楚展示了不同选择策略如何导致截然不同的结论，这一发现对 probing 方法论文献有直接贡献。两位 Reviewer 共识这是论文最强的贡献。

**S2. 统计方法论扎实 [R1, R2 共识]**
Holm-Bonferroni 12-test 和 4-test 双重校正、10,000 次 bootstrap 重采样、exact permutation test 交叉验证、position residualization 控制、control task (Hewitt framework) selectivity 分析。统计工具使用规范且报告充分。

**S3. 负面结果的信息量 [R1, R2 共识]**
七种替代方法的系统性失败不是简单的"方法不行"，而是揭示了 CP 表征的特性（gradual、concentrated in minor principal components、model-specific）。Section 4.6 的 framing 将失败转化为关于表征几何的正面发现。

**S4. 透明的局限性讨论 [R1, R2 共识]**
Limitations section 量化了 2,240 configurations 的搜索空间、32B 样本量限制、CP 标注不确定性、scope 限制。Bug disclosure (Appendix I) 主动披露了影响先前结论的实现错误。这种透明度在该领域罕见。

**S5. 写作质量 [R2 确认]**
无 AI 写作痕迹（无 em-dash 滥用、无 -ing 分词结尾），叙事结构清晰，Related Work 57 篇引用覆盖合理。

---

## Weaknesses

### Must-Fix (Critical)

**W1. Layer selection 与 evaluation 使用同族 metrics 的循环论证风险 [R1 Critical, R2 AGREE]**
Corrected layer selection 使用 threshold-dependent metrics (precision, inverse FPR)，HS-vs-text evaluation 同样以 precision/FPR 为核心。论文未报告 BA-selected middle layers (QwQ-32B L30, R1-32B L47) 上的 HS-vs-text comparison。BA 是 threshold-free metric，是最中立的 layer selection 基线。如果 HS 优势在 BA-selected layers 不成立，核心 claim 变为 metric-conditional 而非 layer-conditional。R2 称此为"最有洞察力的发现"。**必须补充 BA-selected layers 上的完整 modality comparison。**
[Issue: R13-N1]

**W2. "All four models" overclaim [R1 Major, R2 Major, 交叉完全同意]**
R1-32B 有五重限制（W=1 only、25% coverage、position-mediated、std=0.128、paired covariance），QwQ-32B lead time 为负。当前 framing 虽多次修改但仍不充分——"all four models" 每次出现时未紧跟 R1-32B 限定语。R2 建议替代措辞："robust for two models, qualified for the other two"。
[Issue: R5-N3, 跨 Rounds 5-13 持续 open]

**W3. 32B 统计功效不足 [R1 Critical, R2 Major]**
n=19-20 traces，per-class validation 仅 4-9 traces，2,240 configurations 搜索空间。Bootstrap CI 在此样本量下 below-nominal coverage 是实质性风险。R1 指出 seed-0 outlier (FPR=0.483) 主导方差，exact permutation test 不能修复 power 不足。**32B 结论应标注为 provisional，需补充 post-hoc power analysis。**
[Issue: R5-W1, 跨 Rounds 5-13 持续 open]

### Should-Fix (Major)

**W4. Encoder-conditional advantage 的 "self-defeating" 问题 [R2 Major, R1 partial REBUT]**
论文自身预测更强 text encoder 会消除 HS gap（1024d 后仅 1/4 HB-significant），但 headline framing 仍以 384d 为主。缺少 LLM-based encoder (E5-Mistral-7B, 4096d) 实测。R1 反驳 layer selection 贡献独立于 encoder，encoder-conditional characterization 本身有价值（functional relationship > binary claim）。两位共识缺 LLM-based encoder 实测。
[Issue: R2-W14, 跨 Rounds 2-13 持续 open]

**W5. 累积 DOF 控制不完整 [R1 Major, R2 AGREE]**
作为以 researcher DOF 为核心贡献的论文，自身 DOF 控制有空白：(1) joint (layer, W) 仅 QwQ 验证，R1-32B 缺失；(2) K×W 交互未探索（K ablation 仅 W=1）；(3) LOO-CV 未报告 alternative layers 上的 modality comparison。C-insensitivity 和 K-ablation smooth tradeoff 是缓解因素但不充分。
[Issue: R7-W1, 跨 Rounds 7-13 持续 open]

**W6. PCA-384d "rules out capacity explanation" 过强 [R1 Major, R2 AGREE w/ nuance]**
PCA 保留最大方差方向 ≠ MiniLM 语义空间。"Rules out a pure capacity explanation" 不排除"HS 保留了比 text encoder 更优方向"的替代解释。R2 认为"pure"限定词使 claim 在严格意义上成立，但两位共识 random projection baseline 是更强的 capacity control。
[Issue: R11-N4]

**W7. 单数据集 (HarmThoughts) + CP 标注 IAA 未报告 [R1 Major, R2 AGREE]**
HarmThoughts 是唯一公开 step-level CP 标注数据（选择是 availability-constrained），但论文未充分讨论其 representativeness。95-228 traces 偏小，R1-8B sharper transitions 可能反映 sampling bias。
[Issue: R11-N1]

**W8. Findings 定位而非 Main [R2 Major, R1 AGREE]**
论文不提出新方法、不改进 SOTA、不提供可部署工具，核心是 cautionary finding + encoder-conditional characterization + negative results。与 Hewitt & Manning (2019) 对比：该文提出可复用工具（control task），本文仅提出 reporting practice 建议。如有 layer selection sensitivity 在非安全 task 上的 pilot evidence 可提升 novelty。
[Issue: R12-N1]

### Minor

**W9. Abstract 数据堆砌 [R2 Minor, R1 AGREE]**
~220 words 含过多数字（+15.4, +32.5, 384d, 1024d, 1/4, 39-52%, 85.5%, 1.4-2.7x）。PCA matching 细节不应出现在 Abstract。建议保留 2-3 个关键数字。
[Issue: R2-W9]

**W10. Discussion/Conclusion 重复 [R2 Minor, R1 AGREE]**
Discussion 四段与 Conclusion 逐项复述。建议精简 Conclusion 至 3-4 句核心 takeaway 或合并两节。
[Issue: R2-W11]

**W11. FPR 39-52% 与 deployment 建议矛盾 [R2 Minor, R1 AGREE]**
Discussion "W=3-15 as starting configuration" 是 deployment 建议，与 "characterize rather than production detectors" 定位矛盾。建议改为 future research guidance 语言。
[Issue: R11-N2]

**W12. Step-level 与 trace-level metrics 标注不清 [R1 Minor, R2 AGREE]**
Table 3 使用 trace-level bootstrap，Table 5 使用 step-level metrics，两种 aggregation 差异未在正文中清楚标注。
[Issue: R13-N2]

**W13. Oracle gap 85.5% 仅基于 R1-8B 但被全局引用 [R1 Q, R2 Q, 交叉同意]**
Oracle gap 出现在 Abstract 和 Conclusion 但仅基于 R1-8B。其他 3 模型的 oracle gap 可能差异很大（如 QwQ-32B 因 negative lead time 可能更大）。
[Issue: R13-N5]

**W14. Cross-model transfer "model-specific" 结论过强 [R1 Minor, R2 AGREE]**
PCA 是最弱的 alignment baseline，PCA 下的 failure 不排除 CCA/Procrustes/model stitching 成功。
[Issue: R13-N4]

**W15. GRU 70/30 vs LR 60/20/20 split 标注不清 [R1 Minor, R2 AGREE]**
Table 8 用 70/30，Table 9 用 60/20/20，虽 Appendix D 已解释但正文标注不够一致。
[Issue: R2-W7]

**W16. 正文仅 2 Figures [R2 Detailed]**
信息密度偏低。建议将 temporal windowing 可视化（当前 Appendix D Fig 3）移入正文。
[Issue: R7-W5]

---

## Reviewer Consensus

两位 Reviewer 在以下关键判断上完全一致：
1. **Overall 3.0 (Findings)** — 论文贡献适合 Findings track，不够 Main conference
2. **Layer selection sensitivity 是最强贡献** — 方法论发现有直接价值
3. **W1 (metric circularity) 是最严重的新发现** — 需补充 BA-selected layers 数据
4. **W2 ("all four models") 持续未充分修复** — 跨 9 轮仍 open
5. **W3 (32B statistical power) 是结构性限制** — 无法通过写作修复，只能标注为 provisional
6. **负面结果有信息量** — 但不足以支撑 Main conference acceptance
7. **写作质量良好** — 无 AI 痕迹，统计报告规范

---

## Reviewer Divergence

两位 Reviewer 的分歧均为程度差异而非根本分歧：

1. **W4 (encoder-conditional "self-defeating")**: R2 认为论文预测自身结论被消除是严重问题；R1 认为 encoder-conditional characterization 本身有价值，layer selection 贡献独立于 encoder。**共识**：缺 LLM-based encoder 实测，但分歧在于严重程度（R2: Major, R1: moderate）。

2. **W6 (PCA overclaim)**: R2 认为 "pure" 限定词使 claim 成立；R1 认为仍过强。**共识**：random projection baseline 更优，但在 claim 严格性上有轻微分歧。

3. **R13-N3 (BOCPD on raw hidden states)**: R1 建议直接在 PCA-reduced HS 上测试 BOCPD；R2 反驳 BOCPD 假设低维输入，probe scores 是自然输入。**共识**：PCA-10/50 是未探索的中间地带，但属 minor。

以上分歧均不影响整体评分判断。

---

## Questions (待作者回应)

**Q1** [R1, R2]: BA-selected layers (QwQ-32B L30, R1-32B L47) 上 HS-vs-text precision gap 是多少？如果 gap 不显著，"layer selection sensitivity" 的 claim 是否变为 "metric selection sensitivity"？

**Q2** [R1]: R1-32B W=1 下 5 个 detected traces 与 15 个 undetected traces 是否存在系统性差异（长度、CP 位置、safety topic）？25% coverage 的 significance 是否仅反映 subpopulation effect？

**Q3** [R1, R2]: 如果补充 E5-Mistral-7B (4096d) 实测且 HS gap 消失，核心 claim 如何调整？论文是否准备好了这一结果的 framing？

**Q4** [R1]: Paired ΔPrec std=2.0pp（低方差）vs absolute precision std=12.8pp（高方差）的不一致如何解释？是否意味着 seed 主要影响两种 probe 的 absolute level 而非 relative gap？

**Q5** [R2]: 为什么论文预测更强 encoder 会消除 gap，却不直接测试最强 available encoder？这一遗漏是否削弱了 encoder-conditional claim 的说服力？

**Q6** [R1, R2]: Oracle gap 85.5% 在其他 3 个模型上是多少？

---

## Missing References

两位 Reviewer 共识以下引用缺失：
1. **Ravfogel et al. (2020, 2022)** — INLP, RLACE: 线性概念擦除方法，与 probing methodology 直接相关
2. **Wang et al. (2024)** — E5-Mistral-7B 原始论文：论文讨论 LLM-based encoder 但未引用
3. **Rogers et al. (2020)** — BERTology survey: probing 方法论综述 [R1 建议，R2 未反对]

---

## External Review

外部审稿：未请求。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**Soundness**: 3.5 (R1) / 4.0 (R2) — 统计方法论扎实但 32B 功效和 metric circularity 构成结构性限制
**Excitement**: 3.0 (R1) / 2.5 (R2) — layer selection sensitivity 有价值但属 reporting practice 层面
**Confidence**: 4.0 (两位一致)

**评分理由**：
论文的核心贡献（layer selection sensitivity 是关键 DOF）是正确且有价值的方法论发现，适合 Findings track。但三个结构性问题阻止 Main conference：

(1) **Metric circularity** (W1)：corrected layer selection 和 evaluation 使用同族 metrics，未提供最中立基线（BA-selected layers）上的 modality comparison，使核心 claim 可能是 metric-conditional 而非 layer-conditional。

(2) **Encoder-conditional erosion** (W4)：HS 优势在 1024d 后仅 1/4 HB-significant，论文自身预测更强 encoder 会消除 gap 但未测试，这一 "self-defeating" 特征限制了 impact。

(3) **32B statistical underpowering** (W3)：n=19-20, 2240 configs, per-class 4-9 validation traces。32B 结论本质上是 provisional，无法通过写作修复。

论文在 Findings track 下的价值在于：(a) 为未来 probing 研究提供 layer selection 的方法论警告；(b) 系统记录了七种替代方法的失败模式；(c) 建立了 encoder-conditional advantage 的 functional relationship。这些贡献在 characterization 定位下是合理的。

**Must-fix before Findings acceptance**: W1 (BA-selected layers comparison), W2 ("all four" framing 修正), W3 (32B provisional 标注)。
**Should-fix**: W4 (encoder-conditional 实测或 framing 调整), W5 (DOF 控制补充), W6 (PCA claim 弱化), W7 (HarmThoughts 局限讨论), W8 (Findings 定位一致性)。

---

## Detailed Comments

### 论文结构与页数
8 页正文 + 大量附录，符合 EMNLP long paper 格式。附录内容在正文中有引用。建议将 Appendix D temporal windowing figure 移入正文作为 Figure 3 以增加信息密度。

### 统计报告
Holm-Bonferroni 实施恰当，10k bootstrap + exact permutation 交叉验证是 best practice。Table 3 的 95% CI 报告规范。但 Table 2 (1024d) CI 可能仍基于 1000-resample [未验证，Issue R10-Q6a]。

### 写作风格
无 em-dash/en-dash 滥用，无 -ing 分词结尾，无过度分段。Abstract 信息密度偏高（建议精简至 2-3 个关键数字）。Discussion/Conclusion 重复度约 60-70%，建议压缩。

### 引用覆盖
57 篇引用基本覆盖领域。3 处遗漏（Ravfogel INLP/RLACE, E5-Mistral-7B 原始论文, Rogers BERTology survey）应补充。

### 跨轮持续问题
以下 issue 从 Round 5+ 持续至 Round 13 仍 open，反映结构性限制而非修改不力：
- R5-N3 ("all four models"): 9 轮未解决
- R5-W1 (32B power): 9 轮未解决
- R2-W14 (encoder-conditional): 12 轮未解决
- R7-W1 (累积 DOF): 7 轮未解决

这些问题的持续性本身说明它们是论文的结构性边界，不可能通过文字修改完全消除，需要额外实验数据。