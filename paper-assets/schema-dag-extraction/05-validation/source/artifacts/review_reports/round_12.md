---
round: 12
overall_score: 3.0 - Findings
timestamp: 2026-05-17T14:43:55.385025+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 12 审稿报告 — schema-dag-extraction

**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**审稿人**: Reviewer 1（方法严谨性 + 统计分析）+ Reviewer 2（新颖性 + 写作 + 格式）
**日期**: 2026-05-17
**轮次**: Round 12（经 11 轮修订后的评估）

---

## Summary

本文系统研究 training-free LLM 信息抽取中 schema-induced degradation，通过 BCS-controlled stratification 将 type count 和 type confusability 两个因素隔离分析。在 4 个数据集（Few-NERD, FewRel, DocRED, MAVEN）上发现：count 效应主导（~20× larger），confusability 的 typical-batch gap 仅 2.2pp（CI [0.4, 4.0]）；batch-level BCS 预测力仅在 RE 任务上成立（R²=22-53%），NER 为 null。同时报告了 schema decomposition 的系统性失败（NER merge amplification + RE routing failure）及 MAVEN centrality confound。

经 11 轮修订，论文在 framing accuracy、statistical reporting、format compliance 方面有显著改善。大部分前轮 critical issues 已修复。残留问题主要集中在写作层面和 excitement 不足。

---

## Strengths

1. **实验设计严谨且互补**：Count curves + BCS-controlled stratification 构成合理的准实验策略；within-pool 控制有效隔离 pool composition confound。在 NLP 分析论文中属于上乘水平。[R1, R2 强共识]

2. **统计方法规范透明**：Bootstrap CI、permutation tests、TOST equivalence with sensitivity analysis、cluster-robust CIs、variance decomposition——方法选择与数据结构匹配，超过多数 NLP 论文的统计严谨度。[R1, R2 强共识]

3. **负面结果诚实报告**：NER batch-level null、SDGD failure（merge amplification: precision 0.56→0.21）、2×2 factorial inconclusive、logit-scale TOST inconclusive——不做选择性强调。学术透明度在该领域难得。[R1, R2 强共识]

4. **Centrality confound 分析典范**：MAVEN per-type BCS 正相关被识别为 centrality artifact，从 confound identification 到 partial correlation 到 interpretation 逻辑完整，对后续使用 embedding similarity 做 label analysis 的工作有方法论警示价值。[R1, R2 强共识]

5. **Cross-validation 广度**：4 datasets × 3 tasks × 3 models × 4 prompt variants × 3 seeds，覆盖面远超同类工作。[R1, R2 共识]

6. **Limitations 异常详尽**：8 条具体 limitations 带量化证据 + multiple comparisons paragraph，属高标准 disclosure。[R1, R2 共识]

7. **前轮 Critical Issues 大量修复**：R10/R11 的 7 个 critical issues 中 6 个已 resolved（因果语言、聚合叙事、TOST anchoring、SCS novelty framing、NER overclaiming、Contribution 格式）。仅 practical significance（R11-N2）降级为 should-fix 继续追踪。

---

## Weaknesses

### Must-Fix（影响接收决定）

**无 critical-level must-fix 残留。** 所有前轮 critical issues 已修复或降级。当前最严重的问题为 writing-level should-fix（见下）和 excitement 层面的结构性限制。

### Should-Fix（影响评分）

**S1. Introduction Finding (1) 仍过于密集。** [R2 N1; R1 未反驳]
Introduction L15 的 Finding (1) 是 56 词复合句，含冒号、两个括号插入、分号、and/but 转折。作为最核心的发现，可读性不佳直接影响审稿人第一印象。建议拆为 2-3 句，同时在此处展开 TOST 首次缩写。

**S2. Conclusion 仅 3 句话，缺 future work 和 broader implications。** [R2 N2; R1 交叉 AGREE]
当前 Conclusion 像 TL;DR 而非有洞察的收尾。SDGD future directions 在 §5 而非 Conclusion 中，审稿人在结尾无法看到 forward-looking vision。Training-based IE 对比仅一句话，过于单薄。建议扩展至 5-8 句。

**S3. TOST logit-scale inconclusive (p=0.209) + 2×2 factorial (p=0.56) 未在正文充分讨论。** [R1 N3→should-fix; R2 交叉 AGREE]
三项 robustness check 均未确认 separability，仅 primary regression ±3pp TOST 成功。"Bounded association" 应限定为 "under the primary specification"。R1 经重审 Appendix C 三重 anchoring 后从 critical 下调为 should-fix，但 logit-scale 不一致性仍需正文讨论。

**S4. Practical significance 工程场景锚定不足。** [R1 N2 + R2 W1; 交叉强共识]
Typical gap 2.2pp（CI 下界 0.4pp），top-quartile screening 仅改善 3-5pp。BCS 定位为 "lightweight pre-hoc screen"，但在什么部署条件下 3-5pp 足以改变 schema design 决策？缺乏与现有 schema optimization 方法的定量对比。Cohen (1988) 行为科学标准套用 NLP 场景需更多论证。

**S5. Contribution 3 将 NER null result 包装为正面贡献。** [R2 W4; R1 交叉 AGREE]
"NER shows no batch-level BCS signal despite significant pairwise SCS effects" 是 null result 的正面包装。建议改写为 "We identify task-dependent limitations of batch-level confusability metrics"。

**S6. Introduction 五发现 vs 四贡献不对齐。** [R2 W5; R1 交叉 AGREE]
Finding (4) centrality confound 和 Finding (5) decomposition failure 映射到哪条 contribution 不明。建议统一数量或标注映射。

**S7. TOST 首次出现未展开。** [R2 W1; 继承自 R11-W2 NOT FIXED]
Introduction L15 首次使用 "TOST p=0.003" 未写全称。展开在 §4.4 才出现。

**S8. Appendix N/P 残余因果语言。** [R2 W2]
"count-driven decline"（L502, L508）、"BCS-driven confusability effect"（L513）与 Limitations §7 "correlational evidence" 不一致。替换为 "count-related" / "BCS-associated"。

**S9. Orphan bib entries。** [R1 S1 + R2 W5]
wellek2010testing、perneger-1998、llm-calibration-survey-2024 未被引用。删除或补充引用。

---

## Reviewer Consensus

以下问题两人达成完全共识 [AGREE]：

1. **Practical significance 需要工程场景锚定**（R1-N2 ≈ R2-W1）：2.2pp typical gap 需要明确在什么条件下有 actionable value
2. **TOST margin 三项 robustness check 不支持 separability**（R1-N3; R2 交叉 AGREE）：bounded association 应限定为 primary specification
3. **Contribution 3 包装 null result**（R2-W4; R1 交叉 AGREE）：需更诚实的改写
4. **Conclusion 过短，缺 future work**（R2-N2; R1 交叉 AGREE）
5. **五发现 vs 四贡献不对齐**（R2-W5; R1 交叉 AGREE）
6. **MAVEN 被排除 → batch-level 有效覆盖仅 2/4 数据集**（R2-W3; R1 交叉 AGREE）
7. **Findings 而非 Main**（R1 3.0 + R2 3.0 交叉后一致）
8. **前轮大部分 critical issues 已修复**（R2 Round 12 逐条确认）

## Reviewer Divergence

**D1. NER overclaiming 程度（R2 REBUT R1-N1）**：
- R1 认为 Abstract/Conclusion 将 Dimension 2 作为跨任务通用发现呈现，构成 overclaiming
- R2 反驳：Abstract 已明确 "but not in NER"；Contribution 3 限定 "specific to RE"；Discussion 有专段分析。当前 framing 已充分限定，不构成 overclaiming
- **Director 判断**：R2 的 REBUT 有效。当前 Abstract/Introduction 的表述已精确区分 pairwise (cross-task) vs batch-level (RE-specific)。但 Conclusion 过短（3 句）导致 nuance 被压缩——Conclusion 扩展后此问题完全消除。

**D2. SCS 无新颖性是否为独立 Must-Fix（R1 部分同意 R2-N1，但归入 Excitement）**：
- R2 列为 N1 critical：核心指标无新意，insight 确认直觉
- R1 部分同意但认为：(a) MAVEN centrality confound + decomposition 双重失败模式超出直觉；(b) 新颖性不足是 Excitement 评分问题，不是可通过修改 fix 的缺陷
- **Director 判断**：R1 更准确——novelty 不足无法通过 paper revision 解决。反映在 Excitement 2.5-3/5 和 Findings 推荐中。

**D3. Multiple comparison correction（R2 REBUT R1-W1）**：
- R1 认为 8 个 correlated tests 无 correction 不够严谨
- R2 反驳：Bonferroni 对 correlated tests 不适用（Rothman 1990）；prompt analysis 是 robustness check 非 primary evidence；directional consistency 7/8 充分
- **Director 判断**：R2 的 REBUT 成立。当前论证合理。

**D4. SCS circularity（R2 REBUT R1-W4）**：
- R1 认为 Few-NERD 使用 extraction model 自身 embeddings 有 circularity
- R2 反驳：MiniLM cross-check r=0.172 > Qwen3 r=0.138，如果 circularity 导致 inflation 应 Qwen3 > MiniLM，实际相反；论文已在正文和 Limitations 讨论
- **Director 判断**：R2 的 REBUT 成立。Cross-embedding 证据有效排除 circularity inflation。

**D5. Excitement 分数（R1: 3/5 vs R2: 2.5/5）**：
- R1：controlled experimental framework 有方法论价值；centrality confound + decomposition 失败超出预期
- R2：核心 insight 增量有限，无 mechanistic explanation，无可操作方案
- **Director 判断**：两者差距在于对 "框架本身的贡献价值" 的判断——合理分歧，不影响接收建议（均指向 Findings）。综合 Excitement 2.75/5。

---

## Questions（需作者回答）

1. **Practical significance anchoring**：在什么具体部署场景下（schema 规模、precision/recall 基线、应用领域），2.2pp typical gap 或 3-5pp top-quartile screening 足以改变 schema design 决策？
2. **Training-based IE 对比**：Fine-tuned models 是否也受 schema complexity 影响？如果是，本文发现范围更广；如果不是，training-free 的限制需要更清晰界定。
3. **16-type FewRel val split**：仅使用 16-type validation split 能否复现 pairwise SCS-confusion 相关的方向和显著性？这能缓解 train+val 合并的 contamination 担忧。

---

## Missing References

[两人共识]
1. **Outlines (Willard & Louf, 2023)** — grammar-constrained decoding 基础工作，论文大量使用 vLLM constrained decoding 但未引。对 RE routing failure 分析（§6）尤其重要。[R1 确认最重要]
2. **Cheng et al. (2023) "Batch Prompting"** — count-curve 概念上相关
3. **Lu et al. (2022) "Fantastically Ordered Prompts"** — label ordering sensitivity
4. **Fetahu/Li et al. (COLING 2025)** — universal entity taxonomy

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |
| Reproducibility | 4.0/5 | 4.0/5 | 4.0/5 |
| Clarity | — | 3.5/5 | 3.5/5 |

**Overall Score: 3.0 — Findings**

- R1 初审: 3.5 → 交叉后修正为 3.0（认同 R2 对 novelty 的严格评估）
- R2 初审: 3.0 → 交叉后维持 3.0
- Director 综合: **3.0 — Findings（可被 Findings 接收）**

**核心判断**：

论文经 11 轮修订后，技术严谨性和写作准确性有显著提升。前轮 7 个 critical issues 中 6 个已 resolved。当前版本是一篇 **方法论严谨、结果报告诚实** 的 controlled empirical study。

**接收障碍（结构性，非修改可解）**：
1. **Excitement 不足**（2.75/5）：核心发现（count > confusability 20×, typical gap 2.2pp）有量化价值但符合直觉预期；SCS/BCS 非新指标；框架未产出可操作的解决方案
2. **Batch-level 覆盖有限**：BCS 的核心预测力仅在 RE（2/4 datasets）成立

**可修改的 should-fix（修复后不改变 track 推荐，但提升论文质量）**：
1. Introduction Finding (1) 拆句 + TOST 展开
2. Conclusion 扩展（future work + training-based IE + broader implications）
3. TOST bounded association 限定为 "primary specification"
4. Practical significance 工程场景锚定
5. Contribution 3 诚实改写
6. 五发现/四贡献对齐
7. Appendix 因果语言清理 + orphan bib 清理

**推荐 track**：**Findings**。论文的 Soundness (3.5) 和 Reproducibility (4.0) 达到录用标准，但 Excitement (2.75) 不足以进入主会议。修复上述 should-fix 可确保 Findings 录用。

**置信度**: 4/5（两位 Reviewer 在核心判断上完全一致；分歧限于 novelty bar 的价值判断，已通过交叉分享达成收敛）