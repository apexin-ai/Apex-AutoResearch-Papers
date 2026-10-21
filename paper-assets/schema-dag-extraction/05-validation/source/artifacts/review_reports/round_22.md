---
round: 22
review_mode: fresh
overall_score: 3.0 — Findings
timestamp: 2026-05-19T18:07:37.721227+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 22 (Fresh Review)

**项目**: schema-dag-extraction
**论文**: "How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?"
**目标 Venue**: EMNLP 2026 (ARR May 2026)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人（R1: 方法严谨性, R2: 新颖性/完整性）
**轮次**: 1 轮（交叉后收敛）

---

## Summary

本文研究 training-free LLM information extraction 中 schema complexity 如何预测性能退化，提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 两个度量，在 Few-NERD (NER)、FewRel (RE)、DocRED (DocRE)、MAVEN (ED) 四个数据集上开展受控实验。核心发现：退化沿两个维度运作——type count 驱动 recall 下降（Dim1），type confusability 驱动 type substitution（Dim2）；BCS 解释 22-58% 的跨 batch RE accuracy variance，但 NER 无 batch-level 信号。所有 mitigation 尝试（schema decomposition、label renaming、few-shot）均失败。

---

## Strengths

**S1.** 研究问题重要且填补明确空白——zero-shot LLM IE 中 schema complexity 影响的首次系统受控研究，count-curve + BCS-controlled 双范式互补设计在该领域罕见 [R1, R2 共识]

**S2.** 统计方法论显著优于领域平均水平：TOST equivalence tests、bootstrap CIs (B=10,000)、permutation tests、cross-seed variance decomposition、range-matched robustness checks [R1 Soundness 3.5, R2 Soundness 4]

**S3.** 负面结果的诚实报告具有独立价值：NER batch-level null、MAVEN centrality confound、SDGD 全面失败（merge amplification + routing failure）、renaming 降低准确率、few-shot 扩大 confusability gap [R1, R2 共识]

**S4.** 17 个 Appendix 的深度和透明度罕见，Limitations section 全面诚实 [R1, R2 共识]

**S5.** 跨模型验证（Llama-3.1-8B/70B, Gemini 2.5 Flash API）增强 Dimension 1 结论可信度 [R1, R2 共识]

**S6.** Error taxonomy（Figure 2, Table 3）将 confusability 与具体错误类型（IntraSub）建立因果链，有独立分析价值 [R2]

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [Must-Fix] Title/Abstract scope 与实际发现不匹配** [R2 N1, R1 部分同意]
- Title 声称 "Information Extraction" 但 batch-level confusability（Dim2 核心叙事）仅在 RE (FewRel, DocRED) 上完整成立
- NER batch-level BCS-F1 correlation r ≈ 0（§4.2, n=450）
- MAVEN ED 受 centrality confound（§4.5）
- R1 rebut：pairwise SCS 跨任务成立，batch-level 是聚合局限非维度失败。但 R1 也同意 Abstract framing 需加 task-format qualifier
- **共识**：Abstract 必须区分 pairwise (跨任务) vs batch-level (RE only)；建议 Abstract 加 "task-dependent effect structures" 和 "under RE's forced-choice format" qualifier

**C2. [Must-Fix] SCS/BCS 核心度量的 novelty 论证不充分** [R2 N2, R1 rebut 但下调评分]
- SCS = cosine similarity of type-name embeddings，BCS = mean pairwise SCS——无技术创新
- 论文自承与 LLM-PEE 的 partitioning criterion 一致（§2 最后一段）
- "Controlled experimental framework" 作为主贡献，需更有力地论证与 standard ablation study 的区别
- R1 rebut：方法论创新在实验范式，22-58% R²、renaming 反直觉结果、NER null 无法靠直觉预测。但 R1 交叉后也将评分下调至 3.0-3.5
- **共识**：需更突出 non-obvious findings 和定量发现的价值，或补充 BCS 的实际应用案例

**C3. [Must-Fix] TOST ±3pp margin 循环论证 + logit-scale 分歧** [R1 N2, R2 部分同意]
- ±3pp 首要理由是 "approximates the typical BCS-predicted accuracy gap"——用 BCS 自身预测力校准检验 BCS 效应是否可忽略的阈值
- 灵敏度分析：±2pp 时 FewRel 仅勉强通过（p=0.047）；logit-scale TOST inconclusive（p=0.209）
- R2 补充：logit 变换对 bounded data 更合理，logit inconclusive 削弱等价性结论（从 minor 升级为 should-fix）
- 论文提供了 Cohen's δ 和实践显著性等独立锚点，但正文未充分展示
- **共识**：Cohen's δ 作为首要理由，±2pp 结果入正文，logit-scale 分歧需正文讨论

**C4. [Must-Fix] 页数违规** [R2 W4, R1 交叉 AGREE]
- Section 7 (Conclusion) 起始于第9页，正文超出 EMNLP 2026 的 8 页限制
- **双方确认违规，必须压缩**

### Should-Fix（影响论文质量）

**W1. 无有效 mitigation** [R1, R2 共识]
- SDGD 失败（NER merge amplification, RE routing failure, ED 同）
- Renaming 降低准确率（-3.0pp low-BCS, -8.8pp high-BCS; Table 24）
- Few-shot 扩大 confusability gap (+4.3pp from 0-shot to 5-shot)
- 唯一建议 "flag SCS > 0.85" 为监控非解决方案
- R1 补充：负面结果有独立价值，约束了未来解决方案空间

**W2. 单种子+FP8 噪声→CI 未含模型级方差** [R1 N1→降级, R2 rebut]
- Bootstrap CI 仅捕获 batch composition variance；FP8 residual SD=0.88pp（Appendix Q）
- R2 rebut 有效：greedy decoding 下多种子≈重复测量 FP8 噪声；跨模型验证提供间接鲁棒性
- **Director 判定**：降为 should-fix。建议 FP8 噪声传播进 bootstrap 产生保守 CI

**W3. Dim2 cross-model 验证不足** [R1 W3, R2 AGREE]
- BCS-controlled（Dim2）仅在 Qwen3-32B 上验证，NER 在 8B 模型有 floor effects
- Dim2 (BCS) 未在 proprietary models 验证（Limitations §7 已承认）
- Abstract/Intro 措辞未充分区分两个维度的验证范围

**W4. Unconstrained decoding ablation 结论过强** [R1 W5, R2 AGREE]
- n=25，"eliminates the BCS-accuracy correlation" 措辞过强
- 未做 Fisher z-test 正式比较 constrained vs unconstrained 的 ρ 差异
- 应改为 "insufficient evidence to detect" 并报告 power

**W5. DocRED range-matching power 不足** [R1 W2, R2 AGREE]
- Range-matched CI [-7.13, 7.44]，宽度~14pp，power 严重不足
- Non-significance ≠ absence of interaction
- DocRED 显著交互 (−9.4pp) 与 FewRel TOST 通过之间的张力未充分调和

**W6. Pair-to-batch R² 放大 simulation 独立性假设** [R1 W1, R2 AGREE]
- Simulation 假设 pair-level 效应独立，但同 batch types 共享 prompt context
- R2 补充：核心 batch-level R² 是直接观测值不依赖 simulation
- 需补充非独立性讨论和 ecological inference 文献

**W7. Type definitions 分析应提升至正文** [R2 W3, R1 AGREE]
- "definitions 无帮助"（Table 15, Δr: −0.023 to +0.035）是重要发现，目前仅在 Appendix L

---

## Reviewer Consensus [AGREE]

1. **页数违规必须修复**（C4）
2. **Abstract 需加 task-format qualifier**（C1）——pairwise 跨任务成立，batch-level 仅 RE
3. **TOST margin 需重构 justification**（C3）——Cohen's δ 为首要锚点
4. **无有效 mitigation 是最实质弱点**（W1）——但负面结果有独立价值
5. **Unconstrained ablation 结论需弱化**（W4）
6. **DocRED range-matching 需报告 power**（W5）
7. **Definitions 分析应入正文**（W7）
8. **Missing references 均应补充**（MR1-MR3）
9. **Execution quality 高**（Soundness 3.5-4），统计方法论优于领域平均
10. **负面结果报告值得肯定**

## Reviewer Divergence [REBUT]

1. **单种子 CI 严重性**：R1 认为 must-fix（需多种子）；R2 rebut 降级为 should-fix（greedy decoding 下多种子无新信息，FP8 噪声传播即可）。**Director 采纳 R2 立场**——R2 关于 greedy decoding 的论证有效。

2. **Novelty 是否足够**：R2 认为 SCS/BCS 无技术新意 + core finding 可预期→Excitement 2.5；R1 认为方法论创新在实验范式→Excitement 3.5。**Director 判断**：novelty 确实有限（SCS = cosine sim），但定量发现（22-58% R²）超出直觉，合理区间 3.0。

3. **Title "Predict"**：R1 认为暗示因果需修改；R2 rebut "Predict" 是标准统计用语，BCS-controlled 是准实验设计。**Director 采纳 R2 立场**——Title 无需修改。

4. **Few-shot confounding**：R1 认为高 BCS batch 的 few-shot example 区分度可能更低；R2 rebut 实证数据不支持此担忧（gap 未按 confound 预测方向变化）。**Director 采纳 R2 立场**——添加 disclaimer 即可。

---

## Questions to Authors

1. 能否提供 FP8 噪声传播后的保守 CI（即使仅 FewRel BCS-controlled）？这比多种子实验更有信息量。
2. TOST ±3pp margin 是否有来自先前 LLM IE 工作的 external benchmark？如无，Cohen's δ 应作为首要理由。
3. DocRED 显著交互（−9.4pp）与 FewRel TOST 通过之间的张力如何调和？"bounded interaction" 的适用范围是否应限定为 sentence-level RE？
4. Appendix M 中 EF=3.35 是从 batch 内有效自由度独立计算，还是从 observed R² 反推？如果是后者，simulation 论证为同义反复。
5. NER batch-level null 的根本假设是什么？exact-match 评估将 boundary/type error 混合是唯一解释吗？
6. Abstract 数字（85.7%, 49.5%, 88.0%, 38.7%）的具体来源条件（dataset, count level, prompt version）应标注。

---

## Missing References

以下引用经两位 Reviewer 共识确认应补充：

1. **GLiREL** (Boylan et al., NAACL 2025) — zero-shot RE via shared embedding space，与 SCS 概念一致
2. **Grasping the Essentials** (Wan et al., 2024) — LLMs 对 relation definitions 利用不充分，与 Table 15 发现相关
3. **GLiNER-Relex / ASEE** 等 schema matching + extraction 解耦工作，与 SDGD 动机相关

---

## External Review (Stanford Agentic Reviewer)

**状态：未请求**（项目未启用 `external_review.paperreview_ai`）

---

## Visual Layout Check（非评分项）

**状态：timeout**（elapsed 1068s）。视觉审查 Agent 超时未完成。用户可手动重新触发 `dispatch_visual_check`。本报告不因视觉审查推迟投递。

---

## Overall Assessment

**Overall Score: 3.0 — Findings**
**Confidence: 4/5**

| 维度 | R1 | R2 | Director 综合 |
|------|----|----|--------------|
| Soundness | 3.5 | 4.0 | **3.75** |
| Excitement | 3.5 | 2.5 | **3.0** |
| Reproducibility | 3.5 | 4.0 | **3.75** |
| Overall | 3.0-3.5 | 3.5 | **3.0** |

**评分理由**：

执行质量高的实证分析论文。双范式受控实验设计（count-curve + BCS-controlled）在 LLM IE 领域少见，统计方法论规范，负面结果报告透明。Soundness 接近 4 分水平。

但以下因素制约其达到主会议水平：
1. **Novelty 有限**：SCS/BCS 无技术创新（cosine similarity + mean），与 LLM-PEE 一致；core finding "confusable types hurt performance" 方向可预期
2. **Scope 不匹配**：Title 声称 IE，但 batch-level Dim2 仅 RE 成立（2/4 数据集）
3. **无有效 mitigation**：所有干预尝试失败，实际可操作建议有限
4. **统计敏感性**：TOST 等价性对 margin 选择敏感（±2pp 勉强，logit inconclusive），DocRED interaction 张力未解决
5. **页数违规**：正文超8页

**达到 3.5 (Borderline Conference) 的路径**：修复页数违规 + 重构 TOST margin justification + Abstract 加 task-dependent qualifier + 强化 non-obvious findings 作为 novelty 论证 + 正文纳入 definitions 分析。

**达到 4.0 (Conference) 的路径**：以上全部 + 补充至少一个 promising mitigation 方向（即使初步）+ 多模型 BCS-controlled 验证 + FP8 保守 CI。

---

## Detailed Comments

### §1 Introduction
- "first controlled study" → 建议改为 "to our knowledge, the first controlled study"（论文部分已使用此措辞，但不一致）
- 四个 findings 的 (2) 应更明确区分 pairwise (跨任务) vs batch-level (RE only)

### §3 Experimental Setup
- §3.2 SCS 定义：应在正文（而非仅 Appendix L）提及 name-only vs name+definition 对比结果
- §3.5 Model：FP8 噪声传播对 CI 的影响应在此处或 Limitations 讨论

### §4 Results
- §4.2 BCS-Controlled：practical magnitude（IQR Δ=2.2pp）应更突出——这是典型场景下的预期效应量，极端 batch gap（25-31pp）是设计上放大的
- §4.4 Multi-Dimensional：TOST margin justification 需重构；±2pp 结果和 logit-scale 分歧需入正文
- §4.4 DocRED factorial：range-matched 分析需报告 n 和 power；诚实讨论与 FewRel 的张力

### §5 SDGD
- "eliminates the BCS-accuracy correlation" → "insufficient evidence to detect a significant correlation at n=25"
- 因果语言 "due to" → 加 hedge "largely attributable to"
- MAVEN ED 结果（merge amplification 确认）是有价值的新增，但应说明其对 general IE claim 的支撑有限

### §6 Discussion
- "SCS as a proxy for conceptual overlap" 段落很好，但应与 renaming 的 familiarity confound 更明确关联
- Practical implications 应纳入 definitions 分析（Table 15）和 Rothman multiple comparison 策略的更早讨论

### Appendix
- Appendix M (Simulation): 澄清 EF=3.35 来源（独立估计 vs 反推）；加非独立性讨论
- Appendix C (Factorial): 报告 range-matched n 和 post-hoc power

### 格式
- 压缩正文至8页（Conclusion 必须在第8页内结束）
- 补充 3 篇 missing references