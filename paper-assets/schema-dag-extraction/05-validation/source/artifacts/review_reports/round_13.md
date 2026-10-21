---
round: 13
overall_score: 3.0
timestamp: 2026-05-18T03:14:43.948679+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 13 Consolidated Review Report

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 via ACL ARR May 2026 cycle
**审稿模式**: 2 Reviewers × 1 Round + 交叉回应
**Reviewer 分工**: R1 (方法严谨性 + 实验设计) / R2 (新颖性 + 写作完整性 + 格式合规)

---

## Summary

本文对 training-free LLM IE 中 schema 复杂度如何预测性能退化进行了系统性的 controlled study。将退化分解为两个维度（type count 和 type confusability），提出 SCS/BCS 指标量化 confusability，在四个数据集（Few-NERD, FewRel, DocRED, MAVEN）和四个模型（Qwen3-32B, Llama-3.1-8B/70B, Gemini 2.5 Flash）上验证。论文同时报告了 schema decomposition (SDGD) 的负面结果及其失败诊断。这是一篇实验设计极为严谨的 analysis paper，方法论示范价值突出，但核心贡献受限于 SCS 与 LLM-PEE 指标形式相同、confusability 效应量小（typical 2.2pp）、且 batch-level 信号仅对 RE 有效。

---

## Strengths

**S1. [共识] BCS-controlled quasi-experimental design 是本文最强的方法论贡献。** 固定 count 变化 BCS 的设计在 NLP 实证研究中罕见。FewRel balanced design 消除 type frequency 混淆；within-pool 分析控制 pool composition；TOST equivalence testing 形式化检验 bounded association。两位 Reviewer 一致认为该设计具有方法论示范价值。

**S2. [共识] Robustness checks 的广度和深度在该领域论文中属于上乘水平。** 跨模型 (8B/32B/70B/Gemini)、跨 prompt variant (4 种)、跨数据集 (4 个)、BCS 聚合方式 (mean vs max)、SCS embedding ablation、cross-seed variance decomposition、logit-scale sensitivity。两位 Reviewer 均高度评价。

**S3. [共识] 负面结果的诚实报告和系统诊断。** SDGD 失败不仅被报告，还被系统诊断：NER merge amplification（precision 0.563→0.210）、RE routing failure（73.4% 实例在 3-5 个 sub-schema 同时产生 positive prediction）。Oracle routing +29.8pp 证明理论上限存在，问题在 merge/routing 实现。

**S4. [共识] Limitations section 极为详尽。** 8 项具体限制 + multiple comparisons 声明，覆盖 model coverage、effect size、factorial tests、metric scope、causal mechanism、data contamination。两位 Reviewer 均评价为同领域最佳之一。

**S5. [共识] MAVEN centrality confound 的识别。** 发现 per-type BCS 在同源 schema 上与 centrality 混淆（raw positive correlation 控制 log frequency + degree centrality 后消失），提出 pairwise SCS 作为替代。这是一个有独立价值的方法论贡献，对后续使用 embedding similarity 做 schema 分析的工作有警示价值。

**S6. [共识] 跨模型验证覆盖度好。** Dimension 1 在所有模型上复现（RE 斜率 -30.1pp vs -30.7pp，几乎一致），包括私有 API 模型 Gemini 2.5 Flash。

---

## Weaknesses

### Must-Fix 问题（影响接收决定）

**[共识] W1. SCS 增量贡献有限 + "We introduce" 措辞有误导性**
- Severity: R1 标 major, R2 标 critical; 交叉后 R1 上调至 major
- 论文承认 SCS = LLM-PEE 的 partitioning criterion（§2 SCS novelty 段），但 §3.2 仍以 "We introduce the Schema Confusability Score" 开头，给读者造成指标新颖性的错误印象
- 贡献实质是 analysis framework + 实验发现，而非新指标
- 核心问题：如果 practitioner takeaway 仅为 "RE schema 设计时检查 BCS，预期改善 3-5pp"，这更接近 "系统验证直觉" 而非 "发现新机制"
- R1 补充：centrality confound 发现、few-shot 不缓解 confusability gap (+4.3pp widening)、merge amplification 诊断是 non-obvious 贡献，部分缓解新颖性不足
- **修改要求**：§3.2 改 "We introduce" → "We operationalize" 或 "We adopt"；更好地 frame 哪些发现是 counter-intuitive

**[共识] W2. Dimension 2 效应量小，叙事过度强调 extreme-batch gap**
- Severity: R1 major, R2 critical; 交叉后共识为 major
- Typical-batch BCS gap 仅 2.2pp（95% CI: [0.4, 4.0]），pairwise r² = 1.3-1.7%。CI 下界 0.4pp 接近于零
- 叙事频繁强调 extreme-batch gap（25-31pp），但这些来自人工构造的极端 batch
- Abstract 层面的 framing 是诚实的（"≈2.2pp in typical batches"），但 Introduction/Results 的叙事节奏偏向极端值
- BCS > 0.59 阈值缺乏 formal derivation（无 ROC/threshold sensitivity/precision-recall）
- **修改要求**：(1) Introduction/Results 叙事中 extreme-batch 数字仅作对比锚点，typical gap 前置；(2) 补充 BCS threshold ROC/precision-recall 分析或删除具体阈值推荐

**[共识] W3. NER batch-level null result 限制泛化性**
- Severity: R1 major, R2 critical; 交叉后共识为 major
- Batch-level BCS-F1 correlation 在 NER 为零（r = 0.004, p = 0.94, n = 450），使得 BCS 作为 pre-hoc screening tool 仅适用于 RE
- 论文 Title/Abstract 包含 "Information Extraction"（跨任务），但 Dimension 2 batch-level 发现仅限 RE
- Abstract 已诚实报告（"but not in NER, where the signal is absent despite significant pairwise effects"），但 Title 无 qualifier
- MAVEN batch-level BCS 分析未报告（可能因 centrality confound 而回避，但应明确说明）
- **修改要求**：(1) MAVEN batch-level 分析要么报告要么明确说明为何省略；(2) 考虑 Title 是否需要限定

**[共识] W4. Logit-scale TOST 不一致，削弱 "bounded association" 核心 claim**
- Severity: R1 major; R2 在交叉中 AGREE
- Linear-scale TOST p = 0.003 通过，但 logit-scale（对 ~50% accuracy 更合适）交互项 marginally significant (p = 0.047)，TOST inconclusive (p = 0.209)
- 论文将 logit-scale 结果放在 Appendix，选择 linear-scale 为 primary specification，可被视为 outcome-driven
- Back-transformation argument（2.53-2.78pp 仍在 ±3pp margin 内）提供部分辩护
- 两位 Reviewer 共识：不足以推翻核心 claim（back-transformed magnitude 仍远小于 count 主效应），但正文需更显著报告不一致
- **修改要求**：§4.4 正文显著报告 logit-scale 结果；claim 弱化为 "evidence for bounded association under primary linear specification; logit-scale inconclusive due to limited power"

---

### Should-Fix 问题（影响评分但不一票否决）

**[共识] W5. Gemini 2.5 Flash 引用错误**
- bib 条目 `gemini-team-2024` 指向 "Gemini 1.5"（arXiv:2403.05530），但论文实际使用 Gemini 2.5 Flash
- 事实性错误，两位 Reviewer 一致确认
- **修改要求**：替换为正确引用或标注 "Gemini 2.5 Flash (Google, 2025)"

**[共识] W6. Conclusion 过短，缺 future work**
- Severity: R2 major, R1 minor; 共识至少 should-fix
- Conclusion 约 120-130 words，基本重复 Abstract 内容，缺 future work/broader implications/training-based IE 对比
- §5 末尾有三个 future directions，但不够系统
- **修改要求**：扩展至 2-3 段，含 future work + broader implications + training-based IE 对比

**[共识] W7. Abstract 偏短，缺 motivation**
- Severity: R2 major, R1 minor; 共识 should-fix
- 实际约 115-140 words，低于 ARR 通常期望的 150-250 words
- 缺少问题重要性 framing 和 cross-model generalization 提及
- **修改要求**：补充 1-2 句 motivation + cross-model evidence，扩至 ~200 words

**[共识] W8. Contribution 3 NER null result framing**
- R2 标 critical (packaging null result), R1 REBUT (task-dependent diagnosis has value)
- 交叉后部分共识：保留独立 contribution 但改措辞更 transparent
- R1 建议措辞："We demonstrate that batch-level confusability prediction is task-dependent: effective for RE but absent in NER, and diagnose this asymmetry"
- **修改要求**：Contribution 3 改写，强调诊断性发现而非包装 null result

**[共识] W9. Findings-contributions 映射不清**
- Introduction 4 findings vs 4 contributions 映射关系非 1:1（Finding 3 "cross-scale consistency" 无对应 contribution）
- **修改要求**：统一数量或在 contribution list 中标注对应 findings (§X)

**[共识] W10. -ing participial phrases 残留**
- 约 10-15 处 AI 写作痕迹（"indicating...", "confirming...", "highlighting..."）
- **修改要求**：改写为独立句子

---

### Minor 问题（不影响接收）

- MAVEN validation set 是否用于 hyperparameter 选择未声明
- FewRel closed-set classification + constrained decoding 格式特殊性，泛化性不确定
- 多重比较：prompt variant 8 tests 的 directional consistency 应显式报告 sign test p-value
- Appendix N/P 残余因果语言 ("count-driven", "BCS-driven") 与 Limitations "correlational evidence" 不一致
- DocRED count curve 在正文引用但 Appendix 未呈现

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：

1. SCS 与 LLM-PEE 形式相同，"We introduce" 措辞有误导性
2. Dimension 2 效应量小 (2.2pp typical)，叙事过度强调 extreme-batch gap
3. NER batch-level null result 限制 "跨 IE 任务" 泛化性声称
4. Gemini 2.5 Flash 引用错误（事实性问题）
5. BCS > 0.59 阈值无 formal derivation
6. Conclusion 过短，缺 future work
7. Abstract 偏短，缺 motivation
8. Findings-contributions 映射不清
9. -ing phrases AI 写作痕迹残留
10. 实验设计严谨度在该领域属上乘（最强共识点）
11. Robustness checks 广度和深度堪称典范
12. 负面结果诚实报告有社区价值
13. MAVEN centrality confound 发现有方法论贡献

---

## Reviewer Divergence

**分歧 1：Contribution 3 NER null result 的定性**
- R2 [critical]：将 "BCS 在 NER 上不 work" 包装为 contribution，建议合并到 Contribution 2
- R1 [REBUT]：task-dependent diagnosis（missed entity dominance + centrality confound 机制分析）超出简单 null result，值得独立 contribution，但同意措辞需更 transparent
- 结果：部分收敛——保留独立 contribution 但改 framing

**分歧 2：FewRel contamination 风险严重度**
- R1 [major]：train-origin p=0.06 仅 suggestive，non-uniform contamination 未排除，DocRED 每 count 仅 5 batches
- R2 [REBUT → minor]：反向差异 + covariate control ($\Delta R^2 = 0.005$) + DocRED replication ($R^2 = 0.53$) 已充分
- 结果：未收敛——记录分歧。Director 评估：论文的 contamination 分析在当前 NLP 标准下属充分，但确实无法 100% 排除 non-uniform contamination

**分歧 3：Overall score**
- R1: 3.5 (Borderline Conference)
- R2: 3.0 (Findings)
- 差异来源：Excitement (R1: 3/5, R2: 2.5/5)——R1 认为方法论示范价值 + centrality confound + few-shot widening gap 值 0.5 分区分

---

## Questions for Authors

**Q1. [R1, AGREE by R2]** 能否报告 mixed-effects logistic regression 结果（accuracy as binomial outcome, count + BCS as fixed effects, batch as random effect）？这可解决 scale-dependence concern。

**Q2. [R1]** Count 80（full FewRel schema）时 natural BCS variation 太小 (IQR = 0.033)，confusability 效应不可检测。这是否意味着 confusability 只在 schema 被人工 partition 时 matter？

**Q3. [R2, AGREE by R1]** NER U-shape 能否通过 full-schema false positive 检查直接验证 "type-filtering overhead" 假设？

**Q4. [R2]** Pairwise NER signal 存在 (r = 0.112) 但 batch-level 完全消失 (r ≈ 0)——是否存在 cancellation effect（confusable types 同时增加 IntraSub 和减少 missed rate）？Table 8 NER missed rates 的 non-monotonic pattern 部分支持此假设。

**Q5. [R1, AGREE by R2]** Dimension 2 为何未在 Gemini 2.5 Flash 上测试？这将显著加强 cross-model generalization claim。

**Q6. [R2]** BCS > 0.59 阈值如何推导？跨数据集 (FewRel vs DocRED) 是否一致？

---

## Missing References

1. **[共识] Gemini 2.5 Flash 正确技术报告**（当前 `gemini-team-2024` 指向 Gemini 1.5）
2. **[R1]** Structured prediction calibration 文献（与 constrained decoding + routing failure 分析相关）
3. **[R2]** Embedding similarity for label confusion 文献（如 Prototypical Networks 的 confusion-with-distance 分析）
4. **[R1]** Müller et al. 2019 ("When Does Label Smoothing Help?")、Peterson et al. 2019 ("Human Uncertainty Makes Classification More Human")

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目配置未启用 `external_review.paperreview_ai.enabled`）。

---

## Overall Assessment

### 官方维度评分

| 维度 | R1 | R2 | 加权评估 |
|------|----|----|----------|
| Soundness | 3.5/5 | 4.0/5 | 3.5/5 — 实验设计扎实但 logit-scale TOST inconsistency 是真实的方法论问题 |
| Excitement | 3.0/5 | 2.5/5 | 2.5/5 — 核心发现 incremental (count > confusability 是 intuitive 的; SCS = LLM-PEE); 方法论示范价值存在但不足以弥补 |
| Reproducibility | 4.0/5 | 4.5/5 | 4.0/5 — 代码承诺 release; 实验参数和 prompt templates 完整公开 |

### Overall Score: **3.0 (Findings)**

**一句话判断**: 一篇实验设计严谨、统计分析全面的 analysis paper，方法论示范价值突出（quasi-experimental BCS control + centrality confound 发现 + SDGD failure diagnosis），但 Dimension 2 confusability 效应量小（typical 2.2pp, CI 含 0.4pp）、SCS 指标非新颖（= LLM-PEE）、batch-level 信号仅对 RE 有效（NER 为 null），加上 logit-scale separability 不一致，整体贡献力度和泛化性更适合 Findings 而非主会议。

**上调路径（3.0 → 3.5+ 可能的修改）：**
1. 解决 logit-scale TOST concern（通过 mixed-effects logistic regression 或正文 prominently 报告 + claim 弱化）
2. 提供 BCS threshold 的 formal analysis（ROC 或 precision-recall）
3. 改善 SCS framing（"We operationalize" 而非 "We introduce"）
4. Conclusion 扩展 + Abstract 扩充
5. 修正 Gemini 引用
6. 更好地 frame non-obvious findings（centrality confound, few-shot gap widening, merge amplification diagnosis）为核心贡献

**Confidence: 4/5** — 基于两位 Reviewer 的仔细阅读（含所有 Appendix 和 references.bib），交叉回应中的共识和分歧分析。