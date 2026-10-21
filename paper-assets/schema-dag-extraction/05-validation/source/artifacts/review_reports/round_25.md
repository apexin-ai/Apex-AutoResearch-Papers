---
round: 25
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-21T18:09:17.280655+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 23 (Fresh Review)

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 via ARR May 2026 (Deadline: 2026-05-25)
**类型**: Long Paper (8 pages)
**审稿人**: Reviewer 1（方法严谨性）+ Reviewer 2（新颖性/完整性/格式合规）
**审稿模式**: 圆桌 1 轮 + 交叉分享

---

## Summary

本文研究 training-free LLM IE 中 schema 复杂度对性能的影响，提出 Schema Confusability Score (SCS) 及其 batch-level 聚合 Batch Confusability Score (BCS)，通过 count curves 和 BCS-controlled 两套互补实验范式，在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）、3 个 IE 任务（NER/RE/ED）和 4 个模型（Qwen3-32B/LLaMA-8B/LLaMA-70B/Gemini 2.5 Flash）上系统分析。核心发现：性能退化沿两个维度展开——count-driven recall decline 和 confusability-driven type substitution；BCS 在 RE 上解释 22-58% 的 cross-batch 方差但在 NER 上信号为 null；schema decomposition (SDGD) 因 merge amplification 和 routing failure 而失败。

---

## Strengths

**S1. 研究问题重要且 understudied。** 首个系统隔离 type count 与 type confusability 的控制研究。现有工作（LLM-PEE, CrossAgentIE 等）观察到 schema 变大时性能下降，但未分离出具体因素。confusability-aware 视角填补了重要的认知空白。[R1-S1, R2-S1 共识]

**S2. 控制变量实验设计质量高。** Count curves + BCS-controlled 两套范式交叉设计，BCS-controlled 的 extreme batch 构建（greedy search on SCS graph）是有创意的 quasi-experimental manipulation，远超 LLM-PEE 的 post-hoc correlational analysis。[R1-S2, R2-S1 共识]

**S3. 分析深度在 empirical NLP 论文中罕见。** 28 页含 18 个附录，涵盖 TOST 等价性检验、Monte Carlo simulation、prompt sensitivity（5 种 prompt variant）、format independence（paired constrained/unconstrained）、within-pool analysis、label renaming intervention、relaxed matching 等。[R1-S3, R2-S2 共识]

**S4. 诚实的 null result 和负面结果报告。** NER batch-level BCS null、MAVEN centrality confound、SDGD 全面失败、label renaming 反效果——均未掩饰，配有详细的 power analysis 和机制分析。SDGD oracle routing (72.4% vs 50.4%) 精准定位了 decompose-then-merge 的瓶颈在 routing 而非 decomposition。[R1-S4/S6, R2-S3 共识]

**S5. BCS 的独立预测力有干净验证。** Appendix O joint model 分析（BCS unique R²=0.259 vs composition unique R²=0.299, VIF=1.06）有力支持 BCS 捕获 confusability-specific signal 而非 type difficulty proxy。[R1-S5]

**S6. Limitations 部分坦诚全面。** 覆盖 model coverage、effect size、task scope、causal mechanism、data contamination、domain/language scope、multiple comparisons 共 7 个点。[R2-S5]

---

## Weaknesses

### 高优先级（两位 Reviewer 共识，需优先处理）

**W1 [R1 Must-Fix / R2 Should-Fix] Logit-scale TOST inconclusive 但论文以 linear-scale 为主要结论。**
Appendix C 坦承 logit-scale TOST 在 count×BCS interaction 上 inconclusive（p=0.209），但将 linear-scale 作为 primary analysis（p=0.003 at ±3pp）。对于 bounded [0,1] accuracy data，logit-scale 通常更合适。R2 指出 accuracy 在 0.37-0.86 区间内 logit 优势有限，但双方一致认为正文需同时报告两种 scale 结果，结论至少调整为"linear-scale bounded, logit-scale inconclusive"。
→ **Action**: 正文报告 logit-scale 结果，调整 interaction bounded 的 claim 强度。

**W2 [R1 Must-Fix / R2 Should-Fix] DocRED 偏相关 VIF=50.9 下不可靠。**
DocRED BCS-centrality collinearity 达 VIF=50.9（r=0.99），标准误膨胀 ~7.1×，偏相关 point estimate 极不稳定。论文称"BCS retains predictive value but does not uniquely identify the causal channel"——在 VIF=50.9 下，甚至这一措辞都过强。R2 指出 FewRel BCS-controlled（VIF=1.18）是更干净的核心证据，DocRED 偏相关仅为补充。
→ **Action**: 大幅弱化 DocRED 偏相关结论，承认 BCS 和 centrality 在 DocRED 上 inseparable。

**W3 [R1-W7 + R2-W2 共识] NER null 叙述张力 + Abstract task-dependent 信号不均衡。**
两层问题交织：(1) §5/§6 将 NER 描述为"structural barrier"，但 Appendix E.2 power analysis 显示 power 仅 65%——两者不能同时成立；(2) Abstract 突出 22-58% R² 但 NER null 仅一句带过，造成 framing 不平衡。R1 从 logical consistency 角度、R2 从 framing prominence 角度指出同一问题。
→ **Action**: 统一 NER null 叙述为"inconclusive, likely attenuated"；Abstract 给 NER null 同等 prominence。

**W4 [R1-W9 + R2-W3 共识，交叉后升至 borderline Must-Fix] 跨模型验证不对称。**
所有 core experiments 仅在 Qwen3-32B 上完成。跨模型验证（LLaMA-70B/8B, Gemini）仅覆盖 count curves + BCS-controlled，未涵盖 error taxonomy decomposition、centrality confound analysis、SDGD。最关键的是：DocRED R²=58%（论文最强定量 claim）完全缺乏跨模型支持。R1 指出如果 LLaMA-70B 在 DocRED 上只有 R²=15%，headline claim 需重写。
→ **Action**: 明确标注各 finding 的跨模型支持状况；Limitations 讨论 DocRED R²=58% 的单模型依赖。

### Should-Fix（两位 Reviewer 共识或单方提出且对方认可）

**W5 [R2-W1, R1 AGREE] SCS vs LLM-PEE novelty framing 不清晰。**
SCS 与 LLM-PEE partitioning criterion 形式完全一致（pairwise cosine similarity of type name embeddings）。论文在 Section 2 承认但未上升为显眼的 novelty statement。读者容易得出"SCS = LLM-PEE rebranded"的印象。实际贡献是 controlled experimental framework，需明确点明。
→ **Action**: Section 2 或 3.2 加 explicit novelty statement。

**W6 [R1-W4, R2 AGREE] TOST margin ±3pp 的 argument (1) 循环论证。**
三个 converging arguments 中 argument (1)（IQR-predicted Δ=2.2pp from BCS effect itself）直接引用被检验量的 effect size 确定 margin。
→ **Action**: 删除 argument (1)，仅保留 (2)(3) 两个外部标准。

**W7 [R1-W6, R2 AGREE] Batch-level R²=22-58% 缺少 ecological correlation caveat。**
Pairwise r²≈1.5% 到 batch R²≈22% 的 ~15× 放大本质是 ecological correlation。Appendix N Monte Carlo simulation 证实是 aggregation smoothing（EF≈3.35）而非 compositional effect。正文需显式 caveat + 引用 Robinson (1950)。
→ **Action**: §4.3 加 ecological correlation caveat，将 Robinson (1950) 引用从 Appendix 移到正文。

**W8 [R2-W4, R1 部分同意] Sections 5-6 过度压缩。**
Page 8 承载 centrality confound + SDGD 全部分析 + Discussion and Conclusion，叙事密度过高。R2 建议移 §4.5 到 appendix，R1 反对（boundary condition 应留正文），建议压缩 §4.5 为 1-2 段。
→ **Action**: 压缩 §4.5（per-embedding 细节移入 Appendix），释放空间给 §5-§6 展开 practical guidelines 和 future directions。

**W9 [R1-W3, R2 REBUT 降级] Gemini count-16 BCS-controlled 依赖单个 leverage point。**
Leave-one-out 后相关从 r=-0.80 降至 r=-0.42。R1 标 Must-Fix，R2 rebut 降为 Should-Fix——核心跨模型证据在 LLaMA-70B（decline −30.7pp vs Qwen3 −30.1pp），Gemini 仅补充验证。**此为两位 Reviewer 的主要 severity 分歧。**
→ **Action**: 正文报告 leave-one-out sensitivity；区分"open-weight 一致复现"vs"proprietary 部分支持"。

**W10 [R1-W8, R2 AGREE] DocRED count curves 仅 5 batches/level。**
n=5 per level 偏低（vs Few-NERD 25, FewRel 25），CI 必然很宽。论文已在脚注说明高评估成本原因。
→ **Action**: 报告完整 CIs，正文说明 batch 数限制原因。

**W11 [R1-W5, R2 Partial REBUT] Bootstrap CI 非独立性讨论不足。**
R2 指出 batch-level 分析单位的独立性基本成立（每个 batch 独立采样 type set），但 across-batch 的 shared model/prompt template 可能引入系统性偏差。
→ **Action**: 补充讨论 across-batch correlation 对 bootstrap CI coverage 的潜在影响。

### Minor

**W12 [R2-W6, R1 AGREE] Responsible NLP Checklist 出现在 PDF 中（格式违规）。**
按 EMNLP 2026/ARR 政策，Checklist 应在 OpenReview form 中填写，不在 PDF 中。Pages 9-10 包含完整 Checklist。可能在 desk rejection checklist 中被标记。
→ **Action**: 从 PDF 移除，在 OpenReview form 中填写。

**W13 [R2-W5, R1 AGREE] 正文数字/统计呈现密度过高。**
§4.1-4.3 每段嵌入 10+ 统计值，cognitive overload。
→ **Action**: per-dataset 详细统计值移入 appendix table，正文保留 headline numbers。

**W14 [R1-W10, R2 AGREE] Multiple comparisons 不做 correction 的理由不充分。**
Few-NERD 和 FewRel 共享 Wikidata 来源，"independent replication"假设可讨论。
→ **Action**: 简要讨论 dataset independence 程度。

**W15 [R1-W11, R2 AGREE] 单种子 + greedy decoding 可复现性。**
Residual SD=0.88pp 约占 BCS effect size 的 18-44%。
→ **Action**: 报告 seed variability 或讨论 residual 相对于 effect size 的比例。

**W16 [R2-W7, R1 AGREE] 2 个 orphan bibliography entries。**
`park-2024-grammar-aligned` 和 `zhou-2024-grasping` 未被引用。
→ **Action**: 删除或引用。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上达成一致：

1. **控制变量实验框架是本文真正的贡献**，远超 SCS metric 本身的新颖性。论文需要更清晰地区分这两层。
2. **NER batch-level BCS null 的处理需要改进**：叙述一致性（R1）+ framing prominence（R2）两个角度指向同一修改需求。
3. **跨模型验证是核心薄弱点**：R1 关注 DocRED R²=58% 的单模型依赖，R2 关注 error taxonomy 未跨模型验证——叠加后为仅次于统计方法问题的第二大 concern。
4. **SDGD 负面结果有独立价值**，对 decompose-then-merge 范式的失败分析（merge amplification + routing failure）值得发表。
5. **分析深度出色**：28 页 18 附录，是 empirical NLP 论文的高水准。
6. **整体评分 3.5 Borderline Conference**：两人独立给出相同分数。

## Reviewer Divergence [REBUT]

主要分歧在 **severity 而非 direction**：

| 问题 | R1 判断 | R2 判断 | 分歧本质 |
|------|---------|---------|----------|
| Logit TOST (W1) | Must-Fix | Should-Fix | R2: accuracy 不在极端区间，linear 非完全不当 |
| DocRED VIF (W2) | Must-Fix | Should-Fix | R2: 非核心 claim，弱化措辞即可 |
| Gemini leverage (W9) | Must-Fix | Should-Fix | R2: 核心跨模型证据在 LLaMA-70B，Gemini 仅补充 |
| §4.5 处理 (W8) | 留正文压缩 | 移入 appendix | R1: boundary condition 信息应留正文 |

无方向性对立矛盾。所有分歧均可通过 framing 调整和措辞弱化解决，不需要重新实验。

---

## Questions（需要作者澄清）

**Q1 [R1/R2 共同关注]** Logit-scale TOST inconclusive (p=0.209) 与 linear-scale TOST (p=0.003) 的分歧——作者选择 linear-scale 作为 primary analysis 的统计理由是什么？

**Q2 [R1]** DocRED VIF=50.9 下的偏相关（Table 11）是否在 bootstrapped/permutation 框架下稳定？是否尝试过 ridge regression？

**Q3 [R1]** Gemini count-16 BCS-controlled 的 leave-one-out 后，具体 Pearson r 和 p-value 数值？

**Q4 [R1/R2 共同关注]** NER batch-level BCS null：作者倾向于"structural absence"还是"power insufficient"的解释？两者在论文中的不一致如何解决？

**Q5 [R2]** Pair-to-batch R² 放大（1.5% → 22%）是 aggregation smoothing 还是存在 compositional interaction？Appendix N simulation 支持前者，但论文在 §6 的 practical implications 更像假设后者。

**Q6 [R2]** SCS/BCS 在 homogeneous schemas（如 MAVEN/FrameNet）上不适用——这对 generalizability 有何影响？实践中如何判断一个 schema 是否适合用 BCS 做诊断？

**Q7 [R2]** Label renaming 降低 SCS 后反而损害准确率（Table 29）——这是否意味着"confusability-aware schema design"的实践建议本质上不可行？

---

## Missing References

1. **Robinson, W.S. (1950)** "Ecological Correlations and the Behavior of Individuals" — 已在 Appendix N 引用，需移到正文 §4.3 作为 batch-level R² 的 ecological correlation 警示。[R1 提出, R2 AGREE]
2. **Ren et al. (2016)** "AFET" / **Choi et al. (2018)** "Ultra-Fine Entity Typing" — Hierarchical entity typing 工作，与 type granularity/confusability 主题相关。[R2 建议, 非 critical]
3. **Min et al. (2022)** "Rethinking the Role of Demonstrations in In-Context Learning" — 可为 few-shot confusability 影响提供理论支撑。[R2 建议, 非 critical]

---

## External Review (Stanford Agentic Reviewer)

**状态：已跳过。** 外部审稿请求已发送（2026-05-21T17:47 UTC），但用户选择跳过（2026-05-21T17:51 UTC）。本轮无外部审稿结果。

---

## Visual Layout Check（非评分项）

**状态：已完成。** 3 warnings, 0 critical, 11 info。

**主要发现：**

1. **[Warning] 前 3 页无任何 display item。** Pages 1-3 为连续纯文本（Title/Abstract/Intro/Related Work/Experimental Setup），第一个视觉锚点（Table 1）到第 4 页才出现。审稿人在前 2 分钟仅看到密集文本墙。建议在 page 1-2 加入 motivating figure（如 Figure 1 的简化版）。

2. **[Warning] 主文 8 页仅 4 个 display items（2 figures + 2 tables）。** 对于重实证的控制实验论文偏少（同类论文通常 5-8 个）。大量定量结果仅以文字陈述。建议从附录提升 1-2 个关键表格到主文。

3. **[Warning] Page 8（最后一页正文）为纯文本。** Section 5 + Section 6 无任何 display item，与开头形成"文字夹击"。SDGD decomposition 结果适合配一个小型汇总表。

**正面评价：** Figure 1/2 色盲友好（蓝/橙方案），caption 自包含，Table 排版使用 booktabs 规范。References 无 [?] 未解析引用。Limitations 篇幅适当。

---

## Overall Assessment

**Overall Score: 3.5（Borderline Conference）**
**Confidence: 4/5**

### 评分理由

**研究问题（+）**：重要且 understudied。首个系统隔离 count vs confusability 的控制研究，对 IE schema 设计有直接实践意义。

**实验设计（+）**：控制变量框架（count curves + BCS-controlled batches）质量高，quasi-experimental manipulation 远超先前 correlational work。分析深度（28 页 18 附录）在 empirical NLP 论文中出色。

**负面结果价值（+）**：SDGD 失败的机制分析、label renaming 反效果、few-shot 扩大 gap——这些 non-obvious negative findings 有独立发表价值。

**统计基础裂缝（−）**：logit-scale TOST inconclusive 削弱 interaction bounded claim；DocRED VIF=50.9 使偏相关不可靠；batch-level R² 缺少 ecological correlation caveat。这些问题均可通过 framing 调整解决，但当前状态下部分核心 claim 的统计支撑不够稳固。

**跨模型验证不足（−）**：DocRED R²=58%（最强定量 claim）和 error taxonomy 仅基于 Qwen3-32B。Gemini 验证有 leverage point 问题。

**Novelty 定位（−）**：SCS 与 LLM-PEE 形式重叠，实验范式的 novelty 需要更清晰的 framing。

**NER null 处理（−）**：structural barrier vs power insufficient 的双重叙述需要统一。

### 修订路径

所有高优先级问题均可通过 **framing 调整、措辞弱化和补充讨论** 解决，不需要重新实验。具体修订：
1. 正文同时报告 linear 和 logit-scale TOST 结果
2. 弱化 DocRED 偏相关 claim
3. 统一 NER null 叙述，Abstract 给予同等 prominence
4. 标注各 finding 的跨模型支持状况
5. 加 SCS novelty statement 和 ecological correlation caveat
6. 从 PDF 移除 Responsible NLP Checklist
7. 压缩 §4.5，扩展 §5-§6

修订后论文有望达到 **4.0（Conference）** 水平。当前状态适合 **Findings track**（3.0-3.5）。

---

## Detailed Comments（逐节）

### Abstract
- 22-58% R² claim 需加 NER null qualifier（W3）
- "task-dependent effect structures" 的表述是好的，但需要更突出

### Section 1 (Introduction)
- RQ1-RQ3 设置清晰，但 RQ1 的回答（§4.3）是 task-dependent 的——RE yes, NER inconclusive——这一 nuance 在 Introduction 的 findings 概述中不够明确
- Contribution list 需要更突出 experimental paradigm 而非 metric

### Section 2 (Related Work)
- LLM-PEE 的区分当前是在 "our work differs in three ways" 中处理的，需要在 SCS novelty paragraph 中更直接地承认形式重叠并点明真正的 novelty

### Section 3 (Experimental Setup)
- SCS/BCS 定义清晰，操作化良好
- 数据集选择合理，但 DocRED 5 batches/level 的限制需要在正文中说明（W10）
- 单种子 + greedy decoding 的设计合理但需要在 Limitations 中更定量地讨论 residual variance

### Section 4 (Results)
- §4.1-4.3 统计值密度过高，考虑将 per-dataset 细节移入 appendix table
- §4.3 R²=22-58% 需加 ecological correlation caveat + Robinson (1950)
- §4.4 NER-RE asymmetry 分析是论文亮点之一
- §4.5 centrality confound 留在正文但应压缩

### Section 5 (SDGD)
- 负面结果有价值但分析过度压缩
- Oracle routing 恢复 72.4% 的发现很有启示性，值得更多讨论空间

### Section 6 (Discussion and Conclusion)
- 过短，practical implications 仅一段
- 缺少 future directions（hierarchical extraction, routing-aware decomposition, task-adaptive BCS thresholds）
- Confusability-aware schema design 的建议需要更谨慎（W7 ecological correlation + Q7 renaming 反效果）

### Limitations
- 覆盖面充分（7 个点）
- 需补充：DocRED R²=58% 单模型依赖、跨模型验证的不对称性

### Format
- 正文 ≤ 8 页 ✓
- ACL template with [review] option ✓
- Anonymous ✓
- Limitations section present ✓
- **Checklist 在 PDF 中需移除** ✗
- **`\enlargethispage{3\baselineskip}` 在 sdgd_negative.tex 中**——formatting hack，审稿人可能注意到