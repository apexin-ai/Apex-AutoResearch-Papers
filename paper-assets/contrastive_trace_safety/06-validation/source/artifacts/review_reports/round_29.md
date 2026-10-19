---
round: 29
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-21T17:09:28.181131+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 29 (Fresh Review)

**论文**: Layer Selection Sensitivity in Hidden-State Safety Probes for Reasoning Models
**Venue**: EMNLP 2026 (via ARR)
**审稿模式**: 重新审稿 (fresh)
**Reviewer**: R1 (方法严谨性+统计有效性) + R2 (新颖性+完整性+写作)

---

## Summary

论文定义了 reasoning model 推理链中的 Safety Commitment Point (CP)，系统比较了 hidden-state (HS) 和 text probes 在 4 个 reasoning LLM (3 Qwen + 1 Llama, 7-8B 和 32B) 上的 CP 检测能力。核心发现是方法论性质的：layer selection metric 的选择可以定性地逆转 HS probe 的结论——crossing-rate composite metric 系统性选浅层（所有模型），而 threshold-based metrics 选深层，两者在 32B 模型上产生 p=0.83 vs p<0.005 的逆转。在 threshold-based 层上，HS 对 384d text encoder 有 +15-22pp precision 优势（7-8B cross-validated, 32B exploratory），但此优势随 text encoder 质量提升而缩减（1024d 下仅 1/4 模型显著），且与 temporal position 部分重叠。

---

## Strengths

**S1. 方法论严谨性在同类 probing 论文中罕见。** 5-metric taxonomy、bootstrap 10k resamples + Holm-Bonferroni 12-test 校正、random-label decomposition control、Hewitt & Liang control tasks、nested 5-fold CV (7-8B)、evidence gradient 三级分类——多层防线对抗虚假发现。[R1+R2 consensus]

**S2. Bug disclosure (M002) 是模范级科研透明度。** 完整记录 QwQ-32B text probe pipeline bug 的发现、影响和修正过程。[R1+R2 consensus]

**S3. Negative results 系统且有价值。** 7 种替代方法（BOCPD/CUSUM/MLP/CCS/RepE/Mahalanobis/cross-transfer）的失败及原因分析，对后续研究者有直接参考价值。[R1+R2 consensus]

**S4. Evidence gradient 分类法避免了典型 probing 论文的 overclaim。** cross-validated / significant / exploratory 三级分类，32B 全文标注 exploratory†，统计报告诚实。[R1+R2 consensus]

**S5. Encoder-conditional HS advantage 的 doubly conditional framing 科学准确。** 同时报告 encoder quality gradient (384d→1024d: 4/4→1/4 HB) 和 position overlap (linear 3/4, quadratic 2/4)。[R1+R2 consensus]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [consensus] 主文缺少 conditional inference caveat——HB 校正的 12 tests 是条件于已选层和窗口的推断，而非对 ~2,240 搜索空间的 marginal inference。**
- R1-N1 Critical + R2 AGREE
- 主文 Table 3/Abstract 报告的 p-values 会让读者误以为是 unconditional significance。Appendix W 的 conditional inference 讨论必须出现在主文中。32B validation fold 仅 ~4 traces，selection overfitting 风险高。
- **建议**：主文 Section 3.5 或 4 明确 conditional inference 性质；报告 effective degrees of freedom；考虑 permutation-based marginal coverage 或 post-selection inference (Berk et al., 2013)。
- 关联 issue: R26-N1 (recurring since R26, 至今 4 轮未完全解决)

**MF2. [consensus] E5-Mistral PCA 降维混淆——4096d→384d PCA 人为削弱 text probe，HS 优势可能是维度差异而非模态差异。**
- R1-N2 Critical + R2 AGREE
- Appendix U 将 E5-Mistral-7B (4096d) PCA 降至 384d "to match MiniLM dimensionality"，然后与 HS (4096d) 比较。这同时改变了 encoder quality 和 dimensionality，无法分离两个变量。
- **建议**：补充 4096d E5-Mistral 直接对比；或将 HS 也 PCA 降至 384d 做 capacity-matched 实验。若 HS 优势在维度匹配后消失，需重新表述 Contribution 2。
- 关联 issue: R29-N1 (新发现)

**MF3. [consensus] 模型多样性不足——3/4 Qwen 架构，标题 "four reasoning LLMs" 暗示的多样性高于实际。**
- R2-N2 Critical + R1 AGREE
- 论文自己在 Discussion 指出 crossing-rate shallow-layer bias 是 Qwen-specific (random-label decomposition: Qwen 保留几何偏差, Llama 消除)。仅 1 个 non-Qwen 模型不足以支撑架构通用性 claim。
- **建议**：标题增加架构限定（如 "across reasoning LLMs of two architectures"）；Abstract 明确 3/4 Qwen 这一事实。
- 关联 issue: R23-N2 (recurring since R23, 7 轮未完全解决)

### Should-Fix（影响评分）

**SF1. [consensus] 单数据集 (HarmThoughts) 限制核心 claim 普适性。**
- R2-N1 + R1-W2
- Metric reversal 可能是数据集特有现象。AdvBench 仅验证 geometric precondition (1.67×)，未验证 layer reversal 本身。R1 认为 metric reversal 存在性已在 4 models 上一致证明，将此降级为 Should-Fix。
- **建议**：在 AdvBench 上补充 layer sweep 验证 metric reversal 是否复现；或显著弱化 claim 措辞。
- 关联 issue: R22-W2, R23-N5 (recurring since R22)

**SF2. [consensus] QwQ-32B 在 abstract 中标 "significant" 但 n=19 且无 nested CV。**
- R1-W1 + R2 AGREE
- 与 Table 4 "sample-limited" 标注存在内部张力。建议降级为 "suggestive" 或 "provisionally significant"。
- 关联 issue: R26-N2

**SF3. [consensus] Abstract 信息过载。**
- R2-W2 + R1 AGREE
- 试图覆盖 7+ 独立发现，数字密度过高（"+15 to +22pp at 7-8B"），核心信息被稀释。
- **建议**：重组为 motivation(2句) → core finding(2-3句) → implication(1句)，具体数字移入正文。
- 关联 issue: R23-W4 (recurring since R23)

**SF4. [consensus] Discussion 过度压缩（半 column ~25行）。**
- R1-W3 + R2 AGREE (考虑 8-page 约束)
- 关键讨论（crossing rate 机制、metric reversal 因果方向、部署 implications）被推至附录。
- **建议**：精简 4.4/4.5/4.6 为 Discussion 腾空间。
- 关联 issue: R29-W2 (新发现)

**SF5. [consensus, R2 partial REBUT] Crossing-rate composite 缺理论动机。**
- R1-W4 + R2 partial REBUT
- R2 辩护：作为 foil/contrast case 展示 metric reversal 有合理性。但 R1+R2 均同意需补充 1-2 句设计 rationale（为何合理、在什么假设下应该 work）。
- 关联 issue: R26-W1

**SF6. [consensus] 32B 统计效力不足下的过度解读。**
- R2-W6 + R1 AGREE
- Discussion 对 32B 结果做较强解读（如 "crossing-rate bias is Qwen-specific"），但这可能仅因 sample size 不同。
- **建议**：Discussion 明确区分 7-8B (统计有力) vs 32B (统计效力不足)。
- 关联 issue: R22-W1, R26-N2

**SF7. [R2 raise, R1 partial agree] Evidence gradient 贡献定位模糊。**
- R2-W5 + R1 partial REBUT
- 在 Contributions list 中包装标准统计实践为 "contribution" 可能引起 overclaim 质疑。R1 认为有 corrective 价值但同意降级为 methodological recommendation。
- 关联 issue: R29-W1 (新发现)

**SF8. [consensus] Figure 1 (Layer Heatmap) ACL single-column 下可读性差。**
- R2-W4 + R1 AGREE
- 4×5 heatmap 在 single-column 下每个子图很小，颜色区分困难。Per-column normalization 使跨 metric 比较失效。
- **建议**：改为 full-width 或拆分为两图；axis label 字号加大。
- 关联 issue: R23-VIS (recurring since R23)

---

## Reviewer Consensus

所有关键问题均达成共识：

- **[AGREE]** Conditional inference caveat 必须出现在主文中 (MF1)
- **[AGREE]** E5-Mistral PCA 降维是 capacity confound (MF2)
- **[AGREE]** 3/4 Qwen 架构限制了 generalization claim (MF3)
- **[AGREE]** 单数据集是 structural limitation, Findings 可接受 (SF1)
- **[AGREE]** QwQ-32B "significant" 标签应降级 (SF2)
- **[AGREE]** Abstract 需重组 (SF3)
- **[AGREE]** Discussion 需扩展 (SF4)
- **[AGREE]** 32B 解读需更审慎 (SF6)

---

## Reviewer Divergence

**Excitement 评分分歧**：R1 给 3.5/5, R2 给 2.5/5。
- R1 认为揭示被整个领域忽视的方法论陷阱（可逆转已发表结论）有足够 excitement 达到 Conference threshold。
- R2 认为本质是 sensitivity analysis 而非新方法/新机制发现，impact 局限于 safety probing 子领域。
- **Director 判断**：分歧反映方法论审计类工作的评价标准差异。两者均认为 Findings track 合适。

**Chan & Yong (2025) 区分**：
- R2-W3 认为区分不充分（overlap 显著）
- R1 REBUT 认为 research questions 本质不同（"能否检测" vs "层选择如何影响检测结论"），当前讨论已足够
- **Director 判断**：R1 rebuttal 合理，当前 Related Work 已有约 10 行详细对比，可多用 2-3 句但非必须。

---

## Questions for Authors

**Q1.** [R2] Shallow layer cosine 聚类是否是 trivial artifact（overall variance 小）而非 safety-specific 压缩？是否测量了 shallow vs deep layers 的 overall variance？

**Q2.** [R1] E5-Mistral 为何 PCA 降至 384d 而非使用原始 4096d？这一选择的实验设计理由是什么？

**Q3.** [R1] 是否考虑过 permutation-based 方法估计整个搜索空间的 marginal type-I error rate？

**Q4.** [R2] R1-32B residualized 后 HS advantage 消失（+1.9pp, p=0.914）是否暗示其 HS advantage 完全由 position mediation 驱动？

**Q5.** [R2] 5-metric taxonomy 的选择有无 principled 理由，还是 pilot study 后 empirical 选定？

**Q6.** [R1] 32B 是否可用 LOO-CV 近似 nested validation？

**Q7.** [R1] FPR 11-50% 在实际部署中是否 actionable？Discussion 应更直接回答此问题。

**Q8.** [R2] Bug M002 影响 QwQ-32B text probe。是否对其他 model-modality 组合进行了 pipeline sanity check？

---

## Missing References

以下引用经两位 Reviewer 交叉确认为高相关：

1. **Li et al. (2024)** "Inference-Time Intervention: Eliciting Truthful Answers from a Language Model" — layer-specific probes for inference-time 干预，与本文 layer selection 问题直接相关 [R2 suggest, R1 AGREE]

2. **Levinstein & Herrmann (2024)** "Still No Lie Detector for Language Models" — 对 probing-based detection 的系统性批判，与 metric reversal 发现形成对话 [R2 suggest, R1 AGREE]

以下引用仅由一方提出，需作者自行验证：
- Gurnee et al. (2024) "Language Model Internals Reveal Progress Toward Safety" [R2 suggest, R1 无法确认]
- Nanda et al. (2023) / TransformerLens [R2 suggest, R1 REBUT: 与标准 linear probing 无关]

**引用验证结果**：80 条 bib entries 全部真实。0 orphan entries, 0 missing entries。5 条 minor mismatch（LaTeX 特殊字符编码），15 条近期 arXiv 未被 OpenAlex 索引（已知论文）。R2 报告 belrose2023tunedlens authors 为空实为误报（实际 authors 完整）。

---

## External Review

未配置外部审稿（Stanford Agentic Reviewer），跳过。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（耗时 ~4 分钟）。0 critical, 4 warnings, 11 info。

**Warnings:**
1. **Pages 3-5 text wall**: 连续 3 页纯文本（Related Work + Methods），无 figure/table 穿插。审稿人在前半程缺少视觉锚点。
2. **Display items 后置集中**: 6 个 display items 全部在 pages 6-8，pages 1-5 仅有一个小型 Table 1。
3. **缺方法概览图**: 多组件方法（HS/text probes、temporal windowing、5-metric taxonomy）全靠文字描述，认知负担高。
4. **Figure 1 axis label 偏小**: 约正文 60% 字号，打印或低分辨率下难以辨认。

**Info (highlights):**
- Figure 2 (Forest plot) 清晰，色盲友好
- Table 格式规范 (booktabs)
- 附录结构完整（目录 + 30+ tables + 5 figures）
- References 无未解析引用
- Limitations 简短合规
- 页数合规（正文至 p8，Limitations 在 p9）

---

## Overall Assessment

**评分**: 3.0 (Findings)

**R1**: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.5, Reproducibility 4.5
**R2**: 3.5 (Borderline Conference) — Soundness 4.0, Excitement 2.5, Reproducibility 4.0
**Director 综合**: 3.0 (Findings)

**理由**：

两位 Reviewer 独立给出 3.5，但 Director 基于以下考量降至 3.0：

1. **MF1 (conditional inference) 是跨轮次反复出现的系统性问题**（R22→R25→R26→R29，至今 4 轮未完全解决）——主文至今未明确 p-values 是 conditional on upstream selection 的推断。这对一篇以统计严谨性为卖点的论文是致命的。

2. **MF2 (E5-Mistral PCA confound) 是新发现的实验设计缺陷**——encoder robustness gradient (4/4→2/4→1/4 HB) 是 Contribution 2 的核心论据之一，但 E5-Mistral 数据点存在维度混淆，使 gradient 的第二个数据点不可靠。

3. **MF3 (Qwen 架构主导) 是跨轮次反复出现的结构性限制**（R23→R29，7 轮未解决）——标题和 abstract 仍暗示比实际更高的模型多样性。

4. **单数据集 (SF1) + 中等新颖性 (R2 Excitement 2.5)** 共同限制了 impact。Metric reversal 发现有实践价值但更适合 Findings track。

**修改后评分预期**：
- MF1 (主文加 conditional inference caveat) + MF2 (补 4096d 或 capacity-matched 对比) 处理后 → 3.5
- 若同时处理 MF3 (标题/abstract 架构限定) + SF1-SF4 → 有望冲 3.5-4.0 区间

**置信度**: 4/5

---

## Detailed Comments

### Abstract
- 信息密度过高，核心信息被 7+ findings 稀释。重组为 motivation→core finding→implication 结构。
- "+15 to +22pp" headline 来自 384d MiniLM baseline，应提及 encoder 条件。
- QwQ-32B "significant" 与 Table 4 "sample-limited" 存在张力。

### Introduction
- Contribution 1 (metric reversal) 定位准确，与 Belinkov (2022) 的增量清晰。
- Contribution 2 (boundary conditions) 命名得当。
- Evidence gradient 不应与前两个并列为独立 contribution。
- 缺方法概览图（当前 Table 1 信息价值有限）。

### Related Work
- Chan & Yong (2025) 对比充分（R1 确认 ~10 行详细讨论）。
- Boxo et al. (2025) 定位得当（text leakage complementary mechanism）。
- 缺 Li et al. (2024) ITI 和 Levinstein & Herrmann (2024)。
- Crossing rate 与 early exit consistency metrics 的概念差异需明确。

### Method
- L2 logistic regression 选择合理，C=1.0 robustness 已验证 (<2pp variation)。
- Temporal windowing 设计清晰，per-model validation W 选择合理。
- Section 3.5 必须加 conditional inference caveat。
- Crossing-rate composite 需补设计 rationale。

### Experiments
- Table 2 (layer selection) 是论文最有力的 table，直接展示 metric reversal。
- Table 3 (HS vs text) 结构清晰，dual-encoder 对比有参考价值。
- Section 4.4 (32B analysis) 标注得当（exploratory†, MDE）。
- Section 4.6 (negative results) 简洁有效。
- 建议精简 4.4-4.6 为 Discussion 腾空间。

### Discussion
- 仅半 column，关键机制解释被推至附录。
- 需补入：(1) cosine compression 关键发现摘要；(2) FPR 11-50% 的部署 implications；(3) conditional inference 性质。
- "Multi-metric audit" 建议有实践价值但 three-layer ensemble 作为 solution 需更强 disclaimer。

### Conclusion
- 压缩到 3 行过短。
- QwQ-32B quadratic position absorption 未反映。
- confirmed 7-8B 和 exploratory 32B 的区分已有但不够显著。

### Limitations
- 3 点覆盖合适（dataset scope, statistical power, architecture coverage）。
- 缺 BCa small-sample coverage 讨论。

### Appendix
- 内容极其充分（20+ pages，30+ tables）。
- Bug disclosure (M002) 是模范。
- 但主文应自包含关键论据，不应要求 reviewer 读 20 页附录才能评估核心 claims。

### 格式合规
- 页数合规 ✓（正文 8 页，Limitations/Ethics 在 p9）
- Double-blind ✓（Anonymous ARR Submission）
- ACL template ✓
- Limitations ✓
- Ethics Statement ✓
- 注意：enlargethispage 10+11=21 baselineskip 在 page 8 较激进，可能被个别 reviewer 视为 gaming page limit。
