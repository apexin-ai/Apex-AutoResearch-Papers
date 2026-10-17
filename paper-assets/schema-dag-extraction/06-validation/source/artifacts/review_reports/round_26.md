---
round: 26
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-21T19:08:52.398976+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 24 (Fresh Review)

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 (ARR May 2026 cycle), Long Paper
**Reviewers**: R1 (方法严谨性, 3.5 Borderline Conference), R2 (新颖性与完整性, 3.0 Findings)
**审稿模式**: Fresh (无上轮记忆)

---

## Summary

本文研究 schema 复杂度（type count + inter-type confusability）如何预测 training-free LLM 信息抽取的性能退化。作者提出 Schema Confusability Score (SCS) 及其 batch 聚合 Batch Confusability Score (BCS)，通过 count curves 和 BCS-controlled extreme batch 实验，在 4 个数据集（Few-NERD/FewRel/DocRED/MAVEN）上验证了两个退化维度：count-related recall decline 和 confusability-related type substitution。核心发现：BCS 解释 22–58% 的跨 batch RE 准确率方差（但 58% 受 centrality 严重混淆），NER batch-level BCS 信号为 null，schema 分解（SDGD）因 merge amplification 失败。跨模型验证覆盖 4 个模型家族（Qwen3-32B, LLaMA-8B/70B, Gemini 2.5 Flash）。

---

## Strengths

1. **研究问题重要且定义清晰**：首个在 training-free LLM IE 中系统隔离 type confusability 与 type count 效应的控制研究，填补了现有工作仅讨论 schema 规模但忽略 inter-type confusability 的空白。[R1, R2 共识]

2. **实验设计精细**：Count curves + BCS-controlled extreme batches 的双重设计互相补充。FewRel 的 balanced design (700 instances/type) 有效控制了 type frequency 混淆。[R1, R2 共识]

3. **统计方法学透明度罕见**：报告了 VIF、ecological correlation caveat (Robinson 1950)、TOST 等价检验、功效分析、variance decomposition。这种自我批判风格在 NLP 论文中少见。[R1]

4. **诚实报告负面结果**：NER batch-level BCS null（3 个模型确认）、SDGD decomposition failure（merge amplification）——这些负面结果本身是有价值的社区贡献。[R1, R2 共识]

5. **14 页深度 Appendix**：覆盖 factorial analysis、centrality confound control、power analysis、batch aggregation simulation、split-origin analysis、prompt sensitivity、variance decomposition 等，展现严谨的 robustness checking。[R1, R2 共识]

6. **跨模型验证方向一致**：Count decline 在 4 个模型家族上均呈单调下降，BCS 效应方向在 FewRel 上跨 5 个模型一致。[R1]

7. **格式完全合规**：ACL template [review]、8 页正文、Limitations 合规、匿名化完整、Checklist 正确放在 OpenReview form。[R2]

8. **引用无虚假**：72 条 bib entries，59/72 在线验证通过，无 fabricated citations。[R2]

---

## Weaknesses

### Must-Fix (5 items, 全部为 R1+R2 共识)

**C1. DocRED R²=58% 受 centrality 严重混淆，不应作为核心 claim** [R1-N1, R2 AGREE]

Table 11 显示 DocRED 上 BCS 与 degree centrality 的 VIF=50.9，两变量 r=0.99。偏相关虽然显著，但无法归因于 confusability 而非 centrality。Abstract 和 Section 4.3 突出报道 "22–58%"，读者自然将 58% 视为 confusability 解释力——这是误导性的。FewRel R²=22% (VIF=1.16) 是唯一可靠的效应量估计。

→ **要求**：Abstract/正文将 DocRED R² 标注为 confounded by centrality，以 FewRel R²=22% 为主要 claim；或做 centrality-residualized BCS 回归报告残差 R²。

**C2. Gemini 跨模型验证受单一 leverage point 驱动** [R1-N2, R2 AGREE]

Gemini count-16 的 BCS-accuracy 相关受一个 high-BCS outlier 驱动。Leave-one-out 删除该点后，r 从 −0.480 降至 −0.18 (p=0.64)，相关完全不显著。但 Section 4.3 正文声称 Gemini 结果 "replicates on a proprietary architecture"，未披露此 leverage point。论文的 "4 model families" 跨模型验证是关键 selling point，Gemini 验证的 fragility 显著削弱普适性声明。R2 补充：count dimension 方向一致性不受影响，仅 BCS dimension 受影响。

→ **要求**：正文 §4.3 披露 Gemini leverage point，描述为 "directionally consistent but statistically fragile"。

**C3. Ecological correlation caveat 需要更显著的 framing** [R1-N3, R2-W3 独立重合]

Pair-level r² ≈ 1.3–5.2% 但 batch-level R² = 22–58%，~10–40× 放大是 ecological aggregation 的数学必然（Appendix N simulation 已证实）。然而 Abstract 和 Conclusion 使用 "BCS explains 22–58%" 而未注明 ecological 属性。NLP 社区多数读者不了解 ecological correlation，会将 R² 误读为个体级强效应。

→ **要求**：Abstract 加注 "at the ecological (batch-aggregate) level"；Section 4.3 添加专门讨论段，引用 Appendix N simulation 说明 pair-level 如何通过聚合产生 batch-level R²。

**C4. SCS/BCS 指标新颖性不足，贡献定位模糊** [R2-N1, R1 AGREE]

SCS 本质是 `cos(embed(name_i), embed(name_j))`，是标准 embedding cosine similarity，继承自 LLM-PEE (Liu et al., 2025)。Appendix M 显示 name-only 与 name+definition SCS 无差异，进一步说明 SCS 仅捕获表面名称重叠而非深层概念混淆。论文真正贡献在实验方法论（BCS-controlled batch design），但 Abstract 和 Contributions 的措辞将 SCS 包装为独立贡献。

→ **要求**：重写 Contributions 明确区分 methodology contribution (BCS-controlled experimental framework) vs. metric (SCS inherits LLM-PEE)；Abstract 降低 SCS 独立贡献暗示。

**C5. NER null 叙述内部张力** [R2-N2, R1 AGREE]

论文同时给出两种不兼容解释：(1) "structural barrier" — NER 错误分散于 miss/boundary/type (IntraSub 56–93%)，BCS 根本无法预测，暗示 genuine null；(2) "insufficient power" — BCS SD=0.027，65% power，暗示 possible false negative。两种解释不可同时成立。Abstract "NER batch-level confusability signal remains nonexistent" 中 "nonexistent" 传达确定性，但 Appendix E.2 承认功效不足。

→ **要求**：明确采取一种立场，或将两种作为 competing hypotheses 呈现并讨论如何区分；Abstract 避免暗示确定性结论。

### Should-Fix (7 items)

**W1. DocRED 每 count level 仅 5 batches，R² 估计存在小样本正偏** [R1-W1, R2 AGREE]
N=5 + VIF=50.9 组合使 DocRED 偏相关分析几乎无统计效力。建议增加 batches 或降低 DocRED R² 强调。

**W2. 多项核心分析缺乏跨模型验证** [R1-W3, R2-W4 独立重合]
DocRED R²=58%、error taxonomy、SDGD failure、TOST factorial 均仅 Qwen3-32B。Conclusion 中 "replicated across four models" 掩盖了实际验证范围。至少对 LLaMA-70B 复现 DocRED BCS-controlled。

**W3. BCS-controlled batch 的 greedy 构建引入语义域系统偏差** [R1-W4, R2 AGREE]
High-BCS batches 类型来自同一语义域（Tables 26-27），语义域覆盖更窄。窄域 batch 可能因 domain-specific 特征而更难，非纯 embedding confusion。论文未讨论。建议分析语义域覆盖差异或增加域内 BCS-controlled 实验。

**W4. 单种子 + FP8 non-determinism** [R1-W5, R2 AGREE]
Residual SD=0.88pp 占 BCS effect size 18–44%。DocRED (N=5) 下单次运行有不可忽略随机波动。建议对 key results 运行 3 seeds。

**W5. Abstract 信息过载** [R2-W1, R1 AGREE]
Abstract 数字密度过高（r², R², pp decline 等），影响首次阅读理解。建议精简保留 headline numbers。

**W6. Sections 5-6 过度压缩** [R2-W2, R1 AGREE]
Schema Decomposition (Section 5) 是三大贡献之一却仅半 column。建议压缩 §2 Related Work（当前约 1.3 页，部分与 Intro 重复）腾出空间扩展。

**W7. BCS clean validation 实际仅限 FewRel 1 个数据集** [R1 交叉升级 R2-W5，分歧保留]
FewRel R²=22% (VIF=1.16) 是唯一 clean verification。DocRED: VIF=50.9；MAVEN: centrality confound；NER: null。R2 原评估 2 个 RE 数据集，R1 认为仅 1 个。可靠结论应收紧至 "FewRel R²≈22%, ecological level, open-weight models"。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上完全一致：

1. **DocRED R²=58% 不可信**：VIF=50.9 使 BCS vs centrality 不可分离，论文最引人注目的定量 claim 需要大幅降调 [C1]
2. **Gemini 验证 fragile**：BCS dimension 依赖单一 leverage point，"4 model families" 验证实际在 BCS dimension 上只有 3 个开源家族可靠 [C2]
3. **Ecological amplification 需显著 caveat**：pair-level r²≈1-5% → batch R²=22% 是聚合的数学必然，非 confusability 的强预测力 [C3]
4. **SCS 非独立贡献**：继承自 LLM-PEE，论文真正贡献在实验方法论 [C4]
5. **NER null 叙述自相矛盾**：structural barrier vs insufficient power 不兼容 [C5]
6. **跨模型验证深度不均**：核心量化分析均为 Qwen3-32B 单模型 [W2]
7. **实验设计精细**：BCS-controlled batch design 是有价值的方法论贡献 [Strength]
8. **负面结果有价值**：NER null + SDGD failure 对社区有启发性 [Strength]
9. **格式完全合规**：无违规 [Strength]

## Reviewer Divergence [REBUT]

1. **TOST 量表敏感性** — R1 认为 Should-Fix（logit-scale 对 bounded data 更合适），R2 认为 accuracy 0.70-0.92 远离边界，linear defensible，且核心 claim 不依赖 TOST。**Director 判断**：保留分歧，列为 divergent warning (R24-D1)。

2. **BCS 可靠验证数据集数量** — R1 认为仅 FewRel 1 个 clean（DocRED confounded），R2 认为 RE 2 个数据集。**Director 判断**：R1 论证更有力（VIF=50.9 确实使 DocRED 不可信），但 DocRED 的方向一致性仍有参考价值，不宜完全否定。

3. **Excitement 维度** — R1 给 3.5（实验方法论 + 负面结果有社区价值），R2 给 2.5（SCS metric 缺乏新意限制 excitement）。**Director 判断**：R1 观点更合理——简单 metric + 精细实验设计 本身是有效贡献模式。Excitement 综合 3.0。

---

## Questions

1. **DocRED centrality-residualized BCS**：能否先对 centrality 回归取 BCS 残差，再报告残差 R²？这能更清楚隔离 confusability 独立贡献。[R1]
2. **Gemini batches 扩展**：能否增加 Gemini count-16 BCS-controlled batches（25→50），检验 leverage point 是否采样偏差？[R1]
3. **TOST 量表选择文献**：是否有方法学文献支持 accuracy ∈ [0,1] 上使用 linear-scale TOST？[R1]
4. **NER null 机制**：NER 是 span-level 任务（局部特征更重要），RE 是 sentence/document-level 任务（全局 schema 推理更重要）——这是否是 task asymmetry 的根本原因？[R1]
5. **域内 BCS-controlled**：是否测试过同一语义域内构建 high/low BCS batches 以排除 domain bias？[R1]

---

## Missing References

两位 Reviewer 均未发现严重遗漏。Related work 覆盖充分。

可选补充：
- Aly et al. (2019) "Hierarchical Multi-Task Learning for Fine-Grained Entity Typing"
- Onoe & Durrett (2020) "Fine-Grained Entity Typing for Domain Independent Entity Linking"
- R23 遗留可选：Ren et al. (2016) AFET, Choi et al. (2018) Ultra-Fine Entity Typing, Min et al. (2022) Rethinking Demonstrations

---

## External Review (Stanford Agentic Reviewer)

**状态**：pending（已请求，尚未返回）。请求时间：2026-05-21T18:49:05Z，将在 8 小时后自动提醒用户。

内部审稿不等待外部结果。如外部审稿返回后发现与内部审稿的重大差异，Research Director 可酌情追加评估。

---

## Visual Layout Check（非评分项）

**状态**：done（2026-05-21T18:49:04 → 18:52:37，耗时约 3.5 分钟）

### Warnings (3)

1. **Pages 1-3 连续纯文本**：Title/Abstract/Intro/Related Work 共 3 页无任何 display item。审稿人需翻过 3 页才看到第一个视觉锚点（Table 1, p4）。建议在 p1 或 p2 加入概览图（如 SCS 概念示意 / 核心发现预览图）。

2. **正文 display items 偏少**：8 页正文仅 4 个 display items（Table 1-2, Figure 1-2），对实证论文偏少（通常 5-8 个）。核心定量结果分散在文字中，缺少汇总 main results 表。

3. **Pages 8-9 连续纯文本**：Section 5 + Section 6 + Limitations 连续 2 页无 display item。Section 5 的 decomposition failure 适合用一张小表或示意图辅助。

### Info (13) — 摘要
- Table 1-2, Figure 1-2 排版整洁，booktabs 风格，配色色盲友好
- Figure 1 左面板两条线在高 count 端区分度低
- Figure 2 panel (a) legend 与数据线有轻微重叠
- Appendix 14 页含 27 张表但 0 张 figure
- Prompt templates 排版清晰
- SCS 公式渲染正确
- 匿名标记正确

---

## Overall Assessment

**综合评分：3.0 (Findings)**
**置信度：4/5**

### 评分理由

**可接收为 Findings 的理由：**
- 研究问题重要且实验设计精细（BCS-controlled batch design 是有价值的方法论范式）
- FewRel 上 BCS R²=22%（ecological level, VIF=1.16）是可信的效应量
- 负面结果（NER null, SDGD failure）对社区有明确的警示价值
- 14 页 Appendix 展现了罕见的统计透明度
- 格式完全合规，引用无虚假

**不足以进入 Conference (4.0) 的理由：**
- **核心定量 claim 过度宣称**：最引人注目的 R²=58% 本质上不可解释（centrality vs. confusability）；跨模型验证在 Gemini 上由单一 leverage point 支撑
- **SCS/BCS 指标新颖性有限**：继承自 LLM-PEE 的标准 embedding cosine similarity，Appendix M 证实 definitions 无额外贡献
- **可靠结论范围窄于呈现**：严格而言仅 FewRel 1 个数据集提供 clean BCS validation，且为 ecological level R²=22%
- **NER null 叙述自相矛盾**：structural barrier vs insufficient power 两种解释不兼容
- **核心分析缺乏跨模型验证**：DocRED R², error taxonomy, SDGD, TOST factorial 均为 Qwen3-32B 单模型

### 达到 Conference (3.5-4.0) 的路径

如果作者在 revision 中：
1. 将 DocRED R² 标注为 confounded，以 FewRel R²=22% 为主要 claim
2. 正文披露 Gemini leverage point
3. 加强 ecological correlation caveat（Abstract + 正文专门讨论段）
4. 重新 frame SCS 贡献为 methodology vs metric
5. 统一 NER null 叙述
6. 至少对 LLaMA-70B 复现一项核心分析

则有望达到 3.5 (Borderline Conference)。进一步达到 4.0 需要新增实验数据（centrality-residualized R², 更多 Gemini batches, 域内 BCS-controlled）。

---

## Detailed Comments

### Section 1 (Introduction)
- RQ1-RQ3 定义清晰，但 "first controlled study" claim 需要更精确的 scoping（LLM-PEE 已做 schema partitioning，本文的控制研究是 analytical 而非 engineering）
- Contributions 第 1 条将 SCS/BCS 与实验方法混为一谈，建议拆分

### Section 2 (Related Work)
- 覆盖充分，约 1.3 页
- "SCS novelty" 段 (lines 220-233) 已尝试区分与 LLM-PEE，但措辞仍模糊——"our contribution is the controlled experimental methodology" 应提升到更显著位置
- 可适当压缩以为 Section 5 腾空间

### Section 3 (Experimental Setup)
- BCS-controlled batch 的 greedy 构建方法（Section 3.3）未讨论语义域偏差
- Table 1 数据集统计清晰
- SCS 定义（Section 3.2）技术上正确但应更明确承认与 LLM-PEE 的关系

### Section 4 (Results)
- §4.1 Count curves：方向性发现稳健，跨模型一致
- §4.2 Pairwise SCS：效应量极小 (r²≈1-5%)，已适当报告
- §4.3 BCS-Controlled：核心结果章节。DocRED R²=58% 的 centrality confound 讨论不足（仅在 footnote 4 中一笔带过）；ecological amplification caveat 不够显著；Gemini leverage point 未在正文披露
- §4.4 Multi-Dimensional Degradation：error taxonomy 分析有洞察力（IntraSub vs ExtraSub 分布差异），但仅 Qwen3-32B
- §4.5 Centrality Confound：诚实的分析，MAVEN 的 centrality 问题处理得当

### Section 5 (Schema Decomposition)
- 三大贡献之一，空间严重不足（半 column）
- NER merge amplification 和 RE routing failure 的双重失败机制是有价值的发现
- 建议用 Table 或 Figure 辅助叙述

### Section 6 (Discussion and Conclusion)
- "BCS enables pre-hoc diagnostics" 是合理的实用价值定位
- "replicated across four models" 措辞过强，应精确化为 "count direction replicated on four models; BCS effect replicated on three open-weight families"

### Limitations
- 6 点覆盖全面（model coverage, effect size, task scope, causal mechanism, contamination, domain scope）
- Across-batch correlation 和 Multiple comparisons 两段补充得当
- NER null 的 power=65% 应在此更明确讨论其与正文 structural barrier 解释的张力

### Appendix
- 14 页 27 表，robustness 极其充分
- Appendix N (ecological simulation) 是关键证据，应在正文更显著地引用
- Appendix R (variance decomposition) 量化了 FP8 non-determinism，有价值但未在正文充分讨论影响