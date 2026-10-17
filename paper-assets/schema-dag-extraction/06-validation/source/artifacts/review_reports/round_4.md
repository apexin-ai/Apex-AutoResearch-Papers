---
round: 4
overall_score: weak reject
timestamp: 2026-05-16T09:22:25.402052+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 4 审稿报告 — schema-dag-extraction

**论文**: Does Type Confusability Drive Schema-Induced Degradation in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 Main Conference (ARR May cycle, deadline 2026-05-25)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计+统计; R2: 新颖性+完整性+写作+格式）
**轮次**: Round 1 独立审稿 + 交叉分享，1 轮收敛

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能下降的机制。提出 Schema Confusability Score (SCS)，通过 count curves（变 schema size）和 BCS-controlled 实验（固定 size 变 confusability）在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上隔离出两个退化通道：count-driven recall decline 和 confusability-driven type confusion。发现 pairwise SCS 可预测 type confusion（r=0.112-0.129），但 effect size 极低（r²=1.3-1.7%）。Schema decomposition 在 NER 上因 merge amplification 失败，在 RE 上 +1.4pp 不显著（p≈0.19）。

---

## Strengths

1. **实验设计精巧**: Count curves + BCS-controlled 两种范式互补，是隔离 schema degradation 机制的有效方法论贡献。[R1, R2 共识]
2. **多任务多数据集覆盖**: 4 个数据集涵盖 NER/RE(句)/RE(篇)/ED，schema 规模 66-168 types，cross-domain 和 same-domain。[R2]
3. **高度透明**: 对负面结果的坦诚报告（SDGD 失败、modest r²、MAVEN 反转、v2 prompt n=5 不显著）值得肯定。[R1, R2 共识]
4. **Centrality confound 发现**: 对 MAVEN 正向 correlation 的 centrality 解释有独立方法论价值，提醒社区 per-type embedding aggregation 在 homogeneous schema 上的陷阱。[R1, R2 共识]
5. **统计严谨性**: Bootstrap CIs、permutation tests、within-pool controls、BCS aggregation sensitivity analysis 等多层检验。[R2]
6. **Reproducibility 良好**: 完整 prompt 模板（Appendix D）、decoding 参数、数据集描述。[R1]

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1** [R1-N1 + R2 AGREE] **因果语言超出 correlational evidence 支撑**
- Title "Drive"、§4.3 "quasi-experimental evidence" 暗示因果推断，但 BCS-controlled 实验未控制：(a) type frequency in pretraining corpus, (b) type definition quality/length, (c) prompt position effects
- Limitations #6 承认 "correlational evidence" 与正文 "quasi-experimental" framing **直接矛盾**
- MAVEN 已做 partial correlation（Appendix C），但 Few-NERD/FewRel 缺失
- **Action**: 明确列出控制了什么（count）和未控制什么；消除内部矛盾；对 FewRel 做 type frequency partial correlation

**C2** [R1-N2 + R2-N2 强共识] **Pairwise effect size 极低（r²=1.3-1.7%），framing hierarchy 倒置**
- SCS 解释 type confusion variance 仅 1.3-1.7%，剩余 ~98% 来自其他因素
- Typical-batch gap 仅 2.2pp (CI: [0.4, 4.0])，约为 extreme gap 31.2pp 的 7%
- 但 abstract/Table 3/Conclusion 均以 31.2pp 为 headline，2.2pp 被埋在 §4.3 中段
- 缺乏从 pairwise r²→batch-level gap 的数学推导（至少需 back-of-envelope estimation）
- **Action**: Abstract/Intro 以 typical-batch magnitude 为 primary headline；提供聚合放大的数学解释

**C3** [R1-N3 + R2 部分同意] **Full 80-rel 自然条件回归不显著 (p=0.762) 但极端构造结果作为核心 evidence——cherry-picking 风险**
- Table 5 第三行: full 80-rel, n=25, slope=+0.221, p=0.762，在自然采样条件下 BCS 无可检测预测力
- 论文注释 BCS range insufficient (IQR=0.033)，但此 null result 仅在 table footnote 出现
- Within-pool 16-sub (n=100, p=0.027) 显著，但选择性报告有利 setting 的印象明显
- **R2 保留意见**: BCS range compression 是设计特性非 BCS 无效的证据，但同意需并列讨论
- **Action**: 正文中 80-rel null result 与 extreme-batch result 并列讨论；明确 "detectable with sufficient BCS range" ≠ "practically important"

**C4** [R2-N1 + R1-W3 强共识] **RE batch composition +1.4pp 是 null result 却被写入 contributions 和 abstract**
- p≈0.19, n=1 treatment, BCS margin 0.006, 在 15 random seeds 中排第 13
- Abstract "succeeds for RE" + "demonstrating a directionally consistent application" + contributions #4 均构成 overclaim
- RQ3 的实质回答是 "No for NER, not significantly for RE"
- **Action**: 从 contributions list 移除或改为 negative/inconclusive；Abstract 直接说 "does not yield statistically significant gains"

### Reviewer Consensus [AGREE]

以下问题两位 Reviewer **完全一致**：
- C1 (因果语言): 正文超出 correlational evidence 支撑 [R1 critical + R2 AGREE]
- C2 (effect size framing): typical 2.2pp 应为 primary headline [R1+R2 mutual AGREE]
- C4 (+1.4pp overclaim): null result 不应作为 contribution [R1+R2 mutual AGREE]
- Embedding 不一致: 应在所有 dataset 报告两种 embedding [R1-W2 + R2 AGREE]
- Abstract 过长: 精简至 ~200 words [R1+R2]
- §5 SDGD 过短: merge amplification 分析应入正文 [R1+R2]
- 正文仅 1 Figure: error taxonomy 图应入正文 [R1+R2]
- DocRED R² 解释矛盾: "wider confusability range" 与 Table 1 数据相反 [R1-W5 + R2 AGREE]

### Reviewer Divergence [REBUT]

**MAVEN 反转的严重程度**:
- R2 = critical (N3): 限制 two-channel model 普适性，在最大 schema 上部分失效
- R1 = warning: pairwise SCS-confusion 在 MAVEN 仍高度显著 (r=0.129, p<10⁻⁴²)，失效的是 per-type aggregation 而非 underlying relationship；已有 centrality confound 诊断
- **Director 判断**: 降为 **warning with scope qualification**。R1 的论据更有说服力——pairwise signal 完好，问题在 aggregation 方法论而非 fundamental relationship failure。但 abstract/intro 必须明确标注 "cross-domain schemas" 作为适用条件。

**Prompt robustness**:
- R2: n=5 初始失败说明 prompt sensitivity 比 claimed 更大
- R1: n=25 结果 definitive (p<0.0001, r=-0.919)，n=5 是 underpowered 正确诊断
- **Director 判断**: 同意 R1。n=25 结果 definitive。但 abstract "robust across prompt designs" 仍需改为 "directionally consistent with attenuated magnitude"。

### Should-Fix（影响评分）

**S1** MAVEN 反转适用范围需明确标注 [R2-N3 降级 + R1 REBUT → warning]
- Abstract/Intro 需明确 two-channel model 适用于 cross-domain schemas
- Discussion 需扩展 same-domain vs cross-domain 本质区别

**S2** Embedding 选择不一致且缺乏 first-principles justification [R1-W2 + R2 共识]
- Qwen3 for Few-NERD vs MiniLM for FewRel/DocRED/MAVEN
- 需在所有 dataset 报告两种 embedding 对比

**S3** Abstract 过长 (~280 words) [R1 + R2 共识]
- 精简至 ~200 words，核心发现各一句概括，数字留给正文

**S4** §5 SDGD 正文过短 (~0.5 页) [4 轮均被指出]
- Merge amplification 是最重要的实践发现，应从 Appendix 移入正文

**S5** 正文仅一幅 Figure [4 轮均被指出]
- Error taxonomy 图应入正文 §4.4

**S6** Discussion + Conclusion 过短 (~0.5 页) [R2-W4]
- 缺理论机制讨论（cosine sim 为何预测 LLM confusion）、实用指导（BCS threshold 设置）、scaling 讨论
- Future work 需具体实验设计

**S7** Cross-model claim 过度 [R1-W4 + R2 AGREE]
- Abstract "Both channels replicate on Llama-3.1-8B" 省略了 NER Channel 2 在 8B 上未复制

**S8** DocRED R² 解释矛盾 [R1-W5 + R2 AGREE]
- §4.3 归因 "wider confusability range" 但 Table 1 显示 DocRED BCS range < FewRel

**S9** SCS 基于 type name 但 prompt 包含 definitions [R1 + R2]
- §3.2 称 "reflect information available at inference time" 但 prompt 实际包含 definitions
- 需讨论 mismatch 或测试 definition-inclusive SCS

**S10** §4.4 "100% of confusion errors are intra-batch" 是 RE closed-set classification 的 tautology [R1 + R2 AGREE]
- Constrained decoding 限定 enum 为 batch types + "none"，非 "none" 错误必然 intra-batch
- 不应作为 Channel 2 evidence

**S11** Related Work 覆盖缺口 + orphan bib [R1 + R2]
- 4+ 篇在 bib 但未 cite (RelationPrompt, Li 2023, Wadhwa 2023, DEE)
- 11 个 orphan bib 条目需清理
- 缺 DST schema complexity 和 non-LLM type confusion 文献

**S12** "robust across prompt designs" 需降调 [R2-W6, R1 部分同意]
- 改为 "directionally consistent across prompt designs, with attenuated magnitude"

---

## Questions（需作者澄清）

1. 能否提供从 pairwise r²≈1.5% 到 extreme-batch 31.2pp gap 的数学推导？pair-wise effects 的相关结构如何影响 batch-level 聚合？
2. 为什么 FewRel 用 MiniLM 而 Few-NERD 用 Qwen3 embedding？有无在所有 dataset 用统一 embedding 的结果？
3. BCS-controlled 实验中，high-BCS vs low-BCS batches 的平均 type frequency 是否有系统差异？
4. Table 5 full 80-rel 回归不显著——如果增加到 n=100 random batches，是否能检测到效应？
5. SDGD merge amplification 是否使所有 decompose-then-merge 策略对 span-level tasks 无效？是否探索过 non-union merge（majority voting, calibrated confidence）？
6. 如果 SCS 仅解释 ~1.5% 方差，剩余因素（entity frequency, prompt position, definition quality）中哪个是主导？有初步数据吗？

---

## Missing References

1. **Chia et al. (2022)** RelationPrompt — zero-shot RE prompt-based approach [在 bib 未 cite]
2. **Li et al. (2023)** Evaluating ChatGPT's Information Extraction Capabilities [在 bib 未 cite]
3. **Wadhwa et al. (2023)** Revisiting Relation Extraction in the era of LLMs [在 bib 未 cite]
4. **Shiri et al. (2024)** DEE — schema-aware event extraction decomposition [在 bib 未 cite]
5. **Rastogi et al. (2020)** SGD — dialogue state tracking schema complexity（建议新增）
6. Traditional supervised NER/RE 中 fine-grained type confusion 的 embedding similarity 文献（建议新增）

---

## External Review (Stanford Agentic Reviewer)

项目配置 `external_review.paperreview_ai.enabled: false`。未请求外部审稿。

---

## Overall Assessment

**评分: Weak Reject (偏向 Findings)**
**置信度: 4/5**

两位 Reviewer 独立给出 3.0/5 (Findings) 并在交叉分享中高度收敛。

**核心判断**：论文的方法论贡献有价值（BCS-controlled 设计、centrality confound 诊断），但三个结构性问题限制了 Main Conference 接收：

1. **Effect size 过小 + framing 过度乐观**：pairwise r²=1.3-1.7%，typical-batch gap 仅 2.2pp，但论文以 extreme-batch 31.2pp 和因果语言 ("drive") 作为 headline。证据支撑的是 "confusability is a statistically detectable but practically modest factor"，而非 "confusability drives degradation"。

2. **应用层面无显著改善**：RQ3 的两个尝试均为 negative/inconclusive（NER SDGD 失败，RE +1.4pp p≈0.19），但被包装为正面贡献。

3. **Full 80-rel 自然条件回归不显著**：在不构造极端条件时，BCS 对 accuracy 无可检测预测力，削弱 practical significance。

**推荐路径**：
- **Findings 接收条件**：修正因果 framing、反转 headline hierarchy (typical > extreme)、将 +1.4pp 坦率承认为 inconclusive、标注 cross-domain 适用范围
- **Main Conference 接收额外需要**：补充 cross-embedding sensitivity、数学推导放大机制、更多模型验证、扩展 Discussion

---

## Detailed Comments

### Abstract
- 过长（~280 words），需精简至 ~200
- 31.2pp extreme gap 不应作为 primary headline，改用 typical 2.2pp 或 quartile -5.3pp
- "succeeds for RE" overclaim，改为 null/inconclusive
- "Both channels replicate on Llama-3.1-8B" 缺 NER Channel 2 失败的 qualification
- "robust across prompt designs" → "directionally consistent with attenuated magnitude"
- MAVEN 反转用 "generally" 不够，需显式标注 cross-domain 适用范围
- "cleanly separable in RE" 需附加 "(a closed-set classification task)"

### §1 Introduction
- RQ1 的 "Drive" 语气与 correlational evidence 不匹配
- Contributions #4 (+1.4pp) 应移除或改为 negative result

### §2 Related Work
- 4 篇在 bib 未引用（RelationPrompt, Li 2023, Wadhwa 2023, DEE）
- 缺 DST schema complexity 和 non-LLM type confusion 文献

### §3 Experimental Setup
- §3.2 SCS 基于 type name only 但 prompt 包含 definitions：mismatch 需讨论
- Embedding 选择不一致缺 first-principles justification
- DocRED 采样细节不足

### §4 Results
- §4.2: cluster bootstrap 应并列报告或替代 pair-level bootstrap 作为 primary
- §4.3: 80-rel null (p=0.762) 需与 extreme-batch 并列讨论而非仅 footnote
- §4.3: DocRED R² explanation 与 Table 1 BCS range 矛盾
- §4.3: "quasi-experimental" framing 与 Limitations #6 矛盾
- §4.4: "100% intra-batch confusion" 是 RE tautology，非 evidence

### §5 Schema Decomposition
- 正文过短 (~0.5 页)，merge amplification 分析应从 Appendix 移入
- +1.4pp 需坦率承认为 null result

### §6-7 Discussion & Conclusion
- 合计仅 ~0.5 页，需扩展至 ≥1 页
- 缺理论机制讨论、practitioner guidance、scaling 讨论
- Future work 过泛

### Format
- 仅 1 Figure：error taxonomy 图应入正文
- 11 orphan bib 条目需清理
- p-value 格式不一致
- vLLM v0.20.2 版本号需核实
