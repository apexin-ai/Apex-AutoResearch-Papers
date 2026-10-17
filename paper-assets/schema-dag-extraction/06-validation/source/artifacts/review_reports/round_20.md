---
round: 20
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T04:47:46.410637+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 20 审稿报告（圆桌会议汇总）

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**Venue**: EMNLP 2026 via ARR May 2026 cycle
**审稿日期**: 2026-05-19
**Reviewer 编排**: R1（方法严谨性 + 实验设计 + 统计分析）、R2（新颖性 + Related Work + 写作 + 格式）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮即收敛）

---

## Summary

本文研究 training-free LLM 信息抽取中 schema 复杂度导致性能退化的两个维度：type count（维度1）和 type confusability（维度2）。作者提出 Schema Confusability Score (SCS) 和 Batch Confusability Score (BCS) 来量化类型间语义混淆度，在 Few-NERD (NER)、FewRel (RE)、DocRED (doc-RE)、MAVEN (ED) 上使用 Qwen3-32B 为主模型进行系统实验，辅以 Llama-3.1-8B/70B 和 Gemini 2.5 Flash 的跨模型验证。主要发现：(1) count 下降是主导因素；(2) BCS 在 RE forced-choice 格式下解释 22-53% 的跨 batch 准确率方差，但对 NER 无 batch-level 信号；(3) schema decomposition 因 merge amplification (NER) 和 routing failure (RE) 而失败。

---

## Strengths

1. **实验设计精良**：Count curves + BCS-controlled 双范式有效分离 count 和 confusability。Within-pool 控制（从 80-rel pool 抽 16-rel subsets）排除 pool composition confound。FewRel balanced design 消除 type frequency confound。设计思路清晰，在 NLP 实证研究中属上乘。

2. **统计处理透明度高于 NLP 平均水准**：TOST equivalence testing（含 sensitivity analysis across margins）、permutation tests、bootstrap CIs（percentile + cluster）、cross-seed variance decomposition、split-origin covariate analysis。多数 NLP 论文不做 equivalence testing；本文不仅做了，还报告了 margin 对结论的敏感性。

3. **诚实报告 negative results**：SDGD 失败（merge amplification + routing failure）、label renaming 失败（unfamiliarity > confusability reduction）、NER batch-level BCS null、logit-scale TOST inconclusive、few-shot 加剧混淆。这些 negative results 的信息量可能超过 positive findings。

4. **跨模型验证覆盖广**：Qwen3-32B → Llama-3.1-8B/70B → Gemini 2.5 Flash (API)，跨开源/闭源、8B-70B+。Dimension 1 directional consistency 证据充分（RE slope near-identical across models: -30.7 vs -30.1pp）。

5. **格式完全合规**：`\usepackage[review]{acl}` 正确，匿名化完整，正文 ≤ 8 页，Limitations 位置正确，Responsible NLP Checklist 填写详实，引用格式一致。

6. **引用覆盖度好**：~70 个 unique cited keys，覆盖直接竞争者、基础方法、evaluation/statistical 方法、representation degeneration 文献。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[W-Critical-1] "Largely additive" overclaim：仅在 sentence-level RE linear scale 成立** [R1-N1, R2-N2 | 双方共识]
- Abstract/Conclusion 声称 "two largely additive dimensions"，但实际支撑仅来自 FewRel 69-batch full-range regression on linear scale (TOST p=0.003 at ±3pp)。
- FewRel logit-scale: interaction marginally significant (p=0.047), TOST inconclusive (p=0.209)
- DocRED: interaction +5.7pp, 95% CI [-1.6, 13.0], TOST p=0.77
- NER factorial: p=0.50; FewRel 2×2 factorial: p=0.56
- **修复要求**：Abstract/Conclusion 将 "largely additive" 限定为 sentence-level RE linear specification；明确承认 DocRED 和 logit-scale 不成立。

**[W-Critical-2] "Two-dimensional across NER/RE/ED" framing 超出证据** [R1-N3, R2-N2 | 双方共识]
- Dimension 2 (BCS) batch-level 预测力仅在 RE forced-choice format 有效。NER batch-level r≈0 (n=450)；MAVEN centrality confound 控制后信号消失。
- Abstract "across NER, RE, and event detection" 误导读者认为两个维度在三个任务上都成立。
- 实际上：Dim1 (count) 跨任务一致；Dim2 (BCS) 仅 RE forced-choice batch-level 有效，NER/MAVEN 仅 pairwise level 有信号。
- **修复要求**：Abstract/Introduction 区分 pairwise（跨任务）和 batch-level（RE-specific）证据；将 "across NER, RE, and ED" 改为更精确表述。

**[W-Critical-3] Pairwise r²=1.3-1.7% 效应量解读不够审慎** [R1-N2, R2 AGREE with nuance | 共识]
- SCS 仅解释 type confusion 方差的 1.3-1.7%，>98% 由其他因素决定。
- 引用 Cohen (1988) behavioral research 标准，但 LLM 系统变量可控度远高于行为研究，标准适用性未论证。
- Batch-level R²=22-53% 是更有说服力的证据，但正文叙事将 pairwise 和 batch-level 并列，未以 batch-level 为主线。
- **修复要求**：移除或弱化 Cohen 类比；以 batch-level R² 为主线证据，pairwise 定位为机制解释；讨论 SCS 作为代理指标的局限性。

### Should-Fix（影响评分但不一票否决）

**[W-Warning-1] Title "Predict" 与 correlational evidence 不匹配** [R2-N1 Critical, R1 降为 Should-Fix | 分歧]
- "Predict" 在统计语境可辩护（BCS explains 22-53% variance），但 renaming 实验反驳朴素因果链（降低 SCS 反而降准确率 3-9pp）。Limitations 承认 "correlational evidence"。普通读者可能误解为可操作的因果关系。
- **建议**：考虑改为 "Relate to" / "Shape" / "Affect"。

**[W-Warning-2] TOST ±3pp margin 选择不够保守** [R1-W1, R2-W1 | 双方共识]
- ±2pp 仅 marginally equivalent (p=0.047)；±1pp inconclusive (p=0.278)。
- 90% CI upper bound 2.0pp 接近 main effect 2.2pp（interaction 可能达 main effect 91%）。
- **建议**：正文突出 ±2pp marginal 和 logit-scale inconclusive；弱化为 "bounded interaction at ±3pp level"。

**[W-Warning-3] SCS 新颖性不足** [R2-N3, R1 部分 REBUT | 分歧]
- SCS = LLM-PEE 的 partitioning criterion（论文自己承认）。R1 认为 controlled framework 有独立贡献价值；R2 认为效应量有限（~2pp typical, r²≈1.5%）且无可行缓解方案（SDGD 失败、renaming 反向、few-shot 加剧），excitement 不足。
- **建议**：更深入对比 LLM-PEE merge 策略差异；强化 negative result 的 actionable value；考虑增加至少一个可行缓解实验。

**[W-Warning-4] Renaming 实验与 practical implications 矛盾** [R2-W2, R1 AGREE | 共识]
- Discussion §6 建议 "flag type pairs with SCS>0.85 for definition refinement"，但 renaming 实验显示降低 SCS 反而降低准确率。
- **建议**：Discussion 区分 "SCS 作为诊断指标" vs "降低 SCS 作为干预手段"。

**[W-Warning-5] CrossAgentIE 对比不充分** [R2-W3, R1 AGREE | 共识]
- CrossAgentIE (ACL 2025 Findings) 的 cross-type debate 与 confusability 分析直接相关，但仅在括号中列出。
- **建议**：增加 1-2 句讨论 debate 机制与 confusability-aware batching 的异同。

**[W-Warning-6] DocRED 5 batches/count level 样本量不足** [R1-W3, R2 AGREE | 共识]
- Factorial interaction CI 极宽 [-1.6, 13.0]；count curve 趋势估计不可靠。
- **建议**：增至 15 batches（如资源允许），或明确讨论 power limitation。

**[W-Warning-7] Dimension 2 未在 proprietary model 验证** [R1-W4, R2 AGREE | 共识]
- Gemini count-64 仅 11/25 batches（原因未说明）；Llama-70B BCS 仅 count=16。
- **建议**：解释 Gemini partial data；Limitations 明确标注。

**[W-Warning-8] FewRel split-origin 需在正文说明** [R1-W6, R2-W4 | 双方共识]
- Held-out validation (ρ=0.216, p=0.018) 比 covariate analysis 更有说服力但埋在 Appendix。
- **建议**：正文 §3.1 简要提及。

**[W-Warning-9] Rothman (1990) 引用：within-study 二级分析需加 caveat** [R1-W2, R2 AGREE | 共识]
- Cross-dataset 比较引用 Rothman 合理；but prompt variant 分析 (4×2) 非独立假设。

**[W-Warning-10] SDGD routing failure 与 constrained decoding 交互分析不足** [R1-W5, R2 AGREE | 共识]
- Oracle +29.8pp vs practical all below baseline → 瓶颈在 routing。缺少 unconstrained decoding 下 decomposition 的 ablation。

---

## Reviewer Consensus

以下问题双方达成共识：
1. **[AGREE]** "Largely additive" overclaim 是论文最核心的 framing 问题，必须限定为 sentence-level RE linear scale [W-Critical-1]
2. **[AGREE]** "Two-dimensional across NER/RE/ED" framing 超出证据支撑，BCS batch-level 仅限 RE forced-choice [W-Critical-2]
3. **[AGREE]** 效应量解读应以 batch-level R²=22-53% 为主线，Cohen 标准适用性不足 [W-Critical-3]
4. **[AGREE]** TOST ±3pp margin 不够保守，additivity 结论高度依赖 margin 选择 [W-Warning-2]
5. **[AGREE]** Renaming 实验与 practical implications 存在未充分讨论的张力 [W-Warning-4]
6. **[AGREE]** CrossAgentIE 对比不充分 [W-Warning-5]
7. **[AGREE]** DocRED 样本量不足 [W-Warning-6]
8. **[AGREE]** Dim2 未在 proprietary model 验证 [W-Warning-7]
9. **[AGREE]** FewRel split-origin held-out validation 应提到正文 [W-Warning-8]
10. **[AGREE]** SDGD routing failure 分析应讨论 constrained decoding 交互 [W-Warning-10]
11. **[AGREE]** Missing reference: Dubey et al. (2018) Pairwise Confusion (ECCV)

## Reviewer Divergence

| 议题 | R1 立场 | R2 立场 | 说明 |
|------|---------|---------|------|
| Title "Predict" | Should-Fix（统计语境可辩护） | Critical（暗示因果） | R1 认为"predict"是统计标准用语；R2 认为 renaming 反例+correlational 性质要求更谨慎措辞 |
| SCS 新颖性 | Controlled framework 有独立贡献 | 不够（=LLM-PEE criterion，效应量有限，无缓解方案） | R1 对 "experimental design as contribution" 更宽容；R2 认为缺乏 actionable outcome |
| Venue fit | Empirical study 完全适合 EMNLP | 质疑是否适合 main track | R1 引用 ACL ARR review form "empirical contribution" 条款反驳；R2 未在交叉中回应此反驳 |
| 总评分 | 3.5（Borderline Conference，条件性：framing 修复） | 3.0（Findings） | 核心差异：negative results 贡献价值和 novelty 门槛判断不同 |

---

## Questions（需要作者澄清）

1. 如果 "largely additive" 仅在 sentence-level RE linear scale 成立，论文的核心 framework claim 应如何重新定位？是否应将标题聚焦于 RE？
2. SCS 作为 confusability 的代理指标仅解释 1.3-1.7% pairwise 方差，是否有更精细的代理指标候选（如基于 in-context confusion matrix 的指标）？
3. Renaming 实验的 label unfamiliarity 效应是否可以通过使用模型训练数据中高频出现的 paraphrase 来缓解？
4. Oracle routing +29.8pp vs practical routing all below baseline：如果去掉 enum constraint（允许更自由的 "none" prediction），routing 策略是否改善？
5. Gemini 2.5 Flash count-64 为何仅 11/25 batches 完成？

---

## Missing References

1. **Dubey et al. (2018), "Pairwise Confusion for Fine-Grained Visual Classification" (ECCV 2018)** — pairwise confusion metric 与 SCS 动机高度重叠 [双方 AGREE]
2. **Collier et al. (2021), "Exploiting Class Similarity for ML with Confidence Labels"** — inter-class similarity 对分类的影响 [R2 提出, R1 AGREE 低优先级]
3. **LLM calibration × constrained decoding 文献** — 与 routing failure 和 format dependency 分析相关 [R1 提出, R2 AGREE]

---

## Overall Assessment

**综合评分: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4 | 4 | 4 |
| **Overall** | **3.5** | **3.0** | **3.0** |

**评分理由**：

论文展示了高水准的实验设计和统计方法论（Soundness 3.5，在 NLP 实证研究中属上乘），negative results 的诚实报告有独立贡献价值，跨模型验证覆盖面广，格式完全合规。

但以下因素将论文限定在 Findings 档位：

1. **核心 framing 超出证据**（双方共识）："largely additive" 仅在 sentence-level RE linear scale 成立；"two-dimensional across NER/RE/ED" 中 Dimension 2 batch-level 仅限 RE forced-choice。Abstract/Introduction 的 scope claim 与实际证据之间存在系统性 gap。

2. **Excitement 不足**（R1: 3.0, R2: 2.5）：SCS 形式上 = LLM-PEE 的 partitioning criterion；核心发现（count dominates, similar types confuse more）在直觉层面不意外；实际效应量有限（typical batch ~2pp, pairwise r²≈1.5%）；所有干预方向均失败（SDGD、renaming、few-shot）。

3. **缺乏 actionable outcome**：论文是纯诊断性研究，Discussion 的四个 "actionable directions" 均为 untested suggestions。对于 Borderline Conference 门槛，至少期望一个 direction 有初步验证。

**升级路径**（若目标 Borderline Conference 3.5）：
- (a) 修正 framing：限定 "largely additive" 和 "two-dimensional" 的适用范围至 evidence 实际支撑的边界
- (b) 补充至少一个可行缓解实验（如 contrastive definitions for high-SCS pairs，或 unconstrained decoding routing ablation）
- (c) 以 batch-level R²=22-53% 为主线证据重组叙事，弱化 pairwise r² 和 Cohen 类比
- (d) 更深入对比 LLM-PEE merge 策略差异，说明 SDGD 失败的 task-specific 原因

---

## Detailed Comments

### Abstract
- "two largely additive dimensions" 需限定为 sentence-level RE
- "across NER, RE, and event detection" 应区分 Dim1（跨任务）和 Dim2 batch-level（RE-specific）
- "BCS explains 22-53% of cross-batch RE accuracy variance under RE's forced-choice format" — 已有 format caveat，但紧跟 "largely additive" 后容易让读者泛化

### Introduction
- Finding (1) 末尾有 "but not in document-level RE or NER" 限定，但被 "two largely additive dimensions" 主标签淹没
- Contribution 1 "first controlled study...across NER, RE, and event detection" 需精确化

### Experimental Setup
- §3.1 FewRel: 应提及 train/val split 合并理由和 held-out validation 结果
- §3.3: DocRED 5 batches/count level 的 power limitation 应在此处说明

### Results
- §4.2 pairwise r²=1.3-1.7%: Cohen 引用应弱化或移除
- §4.3 BCS-controlled: batch-level R²=22-53% 应更突出作为主要效应量证据
- §4.4: "largely additive" 应弱化为 "bounded interaction at ±3pp in sentence-level RE"

### SDGD
- §5: routing failure 与 constrained decoding 交互应讨论
- Oracle +29.8pp 的指导意义（routing 是瓶颈）应更强调

### Discussion
- §6 practical implication (1) "flag SCS>0.85 for definition refinement" 与 renaming 实验矛盾，需区分诊断 vs 干预
- §6 (3) "contrastive definitions...untested; future work" — 如能提供初步验证将显著提升论文

### Related Work
- CrossAgentIE cross-type debate 需更深入对比
- 增加 Dubey et al. (2018) pairwise confusion 引用

### Format
- Orphan bib entry (jagannatha2020calibrating) 需清理
- Gemini partial data (11/25 batches) 需解释原因
- 少数 bib entries 的 first author field 需核实

---

## 外部审稿

**外部审稿：未配置**（项目未启用 `external_review.paperreview_ai`）

---

*报告由 Review Director 基于 Reviewer 1 和 Reviewer 2 的独立审稿及交叉分享回应汇总生成。*