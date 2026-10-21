---
round: 19
overall_score: 3.0
timestamp: 2026-05-18T10:16:17.195534+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 19 审稿报告

**论文**: How Does Schema Complexity Predict Performance in Training-Free LLM Information Extraction?
**目标 Venue**: EMNLP 2026 (ARR May 25 cycle) — Findings
**Reviewer 编排**: 2 人 (R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量)
**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总 (1 轮即收敛)

---

## Summary

本文研究 training-free LLM IE 中 schema 复杂度如何预测性能退化，将退化分解为 count (Dim 1) 和 confusability (Dim 2) 两个维度。通过 SCS/BCS 量化 confusability，在 FewRel、DocRED、Few-NERD、MAVEN 四个数据集和四个模型上实验。核心发现：count 导致 recall 单调下降（主效应），confusability 导致 type substitution（RE 中 BCS 解释 22-53% batch 间 accuracy 方差），但 NER 无 batch 级信号。Schema decomposition (SDGD) 因 merge amplification (NER) 和 routing failure (RE) 而失败。

R18 的 3 个 critical issues（boundary condition 术语、separable dimensions 措辞、Contribution 2 framing）全部修复。R19 的核心争议转向 novelty 和 impact：SCS 形式同 LLM-PEE，概念发现非 surprising，typical-batch effect size modest (2.2pp)，Dimension 2 batch-level 仅限 RE forced-choice format。

---

## Strengths

**S1. R18 critical issues 全部修复。** [R1+R2 共识] boundary condition 精确化为 forced-choice classification format (非 constrained decoding)；全文统一 "largely additive with bounded interaction"；Contribution 2 焦点从 metric innovation 转为 experimental methodology。修复质量到位。

**S2. 实验设计严谨，控制变量充分。** [R1+R2 共识] BCS-controlled stratification（固定 count 变 BCS）在 training-free IE 文献中首次出现。Within-pool analysis 控制 pool composition confound (permutation p=0.60)。FewRel balanced design 消除 type frequency confound。Cross-model validation 覆盖 4 个模型含 proprietary Gemini 2.5 Flash。

**S3. 统计分析全面透明。** [R1 highlight, R2 Soundness 4/5] TOST equivalence 在三个 margin 水平报告 + logit-scale sensitivity check；bootstrap CIs 区分 pair-level 和 batch-level；variance decomposition 量化 batch vs seed 方差；partial correlation 控制 centrality confound。统计透明度在 NLP 实证论文中罕见。

**S4. 负面结果诚实报告。** [R1+R2 共识] SDGD 失败诊断（merge amplification precision collapse 0.563→0.210; routing failure 73.4% instances 收到 3-5 sub-schema positive predictions）；NER batch-level null；MAVEN centrality confound；logit-scale TOST inconclusive；few-shot widening gap。Oracle routing (0.802 vs 0.504) 精确定位瓶颈。

**S5. Limitations 极其全面。** [R1+R2 共识] 10 条 limitations 含 power analysis 自我披露，预先回应了几乎所有潜在批评。

**S6. Robustness checks 充分。** [R1 highlight] 4 种 prompt variants、mean vs max BCS aggregation、name vs name+def embedding、SCS vs 3 baselines (Levenshtein/WordNet/same-parent)、held-out validation、split-origin covariate。

---

## Weaknesses

### Must-Fix (2 项)

**N1 [critical, R2 提出, R1 同意实质但对评分影响有分歧] 核心发现 novelty 有限。**
- "More types = worse" 已被 Li et al. (2023) 和 LLM-PEE (2025) 定性观察
- "Similar types confuse" 在 hierarchical classification (Deng et al. 2010)、label confusion (Guo et al. 2021) 中有先例
- SCS/BCS 与 LLM-PEE 的 embedding similarity partitioning criterion 形式完全相同（Related Work §2 已承认）
- Controlled experimental methodology (stratified sampling + regression) 是标准方法论，技术上非 novel
- **R1 nuance**: 虽然概念不 surprising，但 quantifying count vs confusability 相对贡献、发现 NER batch-level null task asymmetry 在此前文献中缺失，构成 Findings 级别的 empirical contribution
- **R2 立场**: 作为纯 analytical study，知识增量需足够大但效应量 modest (pairwise r²=1.3-1.7%, typical-batch 2.2pp)
- **Director 判断**: Novelty 确实有限，但 controlled isolation + honest negative results 在 Findings track 仍有价值。建议 Introduction 进一步降低 novelty claim，强调 empirical contribution 而非 conceptual breakthrough

**N2 [critical, R1+R2 共识] Confusability 效应量 RE-specific 且 modest，但 title/framing 暗示跨任务普适性。**
- Pairwise r²=1.3-1.7% (Table 2)
- NER batch-level r≈0, n=450 (§4.3, §4.4)
- Typical-batch gap 仅 2.2pp, CI [0.4, 4.0] (§4.3)
- Dimension 2 batch-level 仅在 RE forced-choice classification format 下成立
- Abstract 缺 typical-batch magnitude 数字，叙事偏重 extreme-batch (-31.2pp, -49pp)
- Title "Training-Free LLM Information Extraction" 暗示跨任务发现，但实际 Dim2 batch-level 高度 RE-specific
- **行动**: Abstract 加 typical-batch magnitude (如 "though typical batches yield modest ~2pp gaps")；Introduction 在 contributions 列表后加 scope qualification；或考虑 title 中加 RE-relevant qualifier

### Should-Fix (5 项)

**W1 [warning, R1 提出, R2 同意] TOST margin vs main effect。**
±3pp margin 允许 interaction 达 main effect 136% (3/2.2)。±2pp marginal (p=0.047)，±1pp inconclusive (p=0.278)。Logit-scale TOST inconclusive (p=0.209)。"Largely additive" 在严格统计意义上依据不充分——数据不能排除 interaction 接近 main effect 的可能。Cross-pool slope consistency (permutation p=0.60) 提供间接支持。建议 Abstract 中 "two largely additive dimensions" 加限定词或 hedging。

**W2 [warning, R1+R2 共识] NER batch-level null 削弱框架普适性。**
NER 是比 RE classification 更 mainstream 的 IE task。"Two-dimensional degradation" 框架对 NER 仅在 pairwise level 成立 (r²=1.3%)，batch-level 没有 actionable signal。论文已在多处承认但 title/abstract framing 仍暗示 general decomposition。

**W3 [warning, R1+R2 共识] NER U-shape 的 "dual-task burden" 假说缺乏实验证据。**
Cross-model replication (LLaMA-70B + Qwen3) 增加现象可信度但不解释机制。三种可能解释 (type-membership filtering, prompt length, instruction complexity) 未做控制实验区分。Discussion 中应标注为 speculative hypothesis。

**W4 [warning, R2 提出, R1 partially rebut] 核心 BCS-controlled detailed analysis 集中在 FewRel。**
DocRED 独立复现了 BCS slopes (slope=-0.713, R²=0.525)，Dimension 1 跨四个数据集。但 within-pool analysis、factorial test、aggregation simulation 全部基于 FewRel。DocRED BCS 分析相对简略 (n=35, 无 within-pool 控制)。R1 部分反驳合理——两个 RE 数据集 (80 vs 96 types, sentence vs document level) 的一致性构成有意义的 replication。

**W5 [warning, R18 遗留, R19 确认 partially fixed] Practical implications 仍偏乐观。**
Discussion 末尾 "diagnostic guidelines derived from correlational evidence" 到位，但 Abstract/Introduction 的叙事仍侧重 extreme-batch 数字而非 typical-batch 的 modest effect (2.2pp)。与 N2 重叠。

### Minor (3 项)

**I1 [info, R1+R2 共识] Monte Carlo simulation evidential status。** Discussion 引用 simulation 时括号 caveat 到位但呈现方式仍给人 independent corroboration 印象。建议正文引用时删去具体数字，仅保留 "post-hoc simulation confirms the aggregation pattern is consistent"。

**I2 [info, R1+R2 共识] Few-shot 5-shot low-BCS 回落解释不充分。** High-BCS 降幅 (-6.6pp) 大于 low-BCS (-3.9pp)，可能有 confusability-specific interaction 而非仅 prompt length effect。承认解释是 speculative。

**I3 [info, R1 提出, R2 部分同意] Prompt variant multiple comparison。** Rothman (1990) 针对 independent replications，这里是 same dataset + same batches。但 Minimal variant 即使 Bonferroni 后仍显著 (p=0.009 vs α=0.0125)，不动摇核心结论。

---

## Reviewer Consensus

以下问题两位 Reviewer 在交叉分享后达成共识 [AGREE]：

1. **R18 修复质量**: N1/N2/N3 全部 FIXED，修复到位
2. **Effect size framing** [N2]: Abstract 需加 typical-batch magnitude，叙事需 calibrated
3. **NER batch-level null** [W2]: 削弱框架普适性，title/framing 应更 precise
4. **TOST margin** [W1]: "Largely additive" framing 偏乐观，需加限定
5. **NER U-shape** [W3]: 假说 speculative，缺控制实验
6. **Simulation** [I1]: Presentation issue, not soundness
7. **Few-shot asymmetry** [I2]: 解释不充分但 info 级别
8. **引用充足度**: 70 篇引用覆盖完整，无明显遗漏

## Reviewer Divergence

1. **Overall score**: R1 = 3.0 (Findings), R2 = 2.5 (Borderline Findings)
   - **核心分歧**: methodology contribution 的价值判断
   - **R1 立场**: controlled design + negative findings 在 Findings track 有价值；NER batch-level null 本身是有价值的 negative finding (task format → batch-level predictability)；统计透明度值得鼓励；降低评分会加剧 publication bias
   - **R2 立场**: stratified sampling + regression 是标准方法论移植，知识增量受限于 modest effect sizes + NER null + SDGD 失败后无 actionable alternative；2.5-3.0 区间合理；如调整 framing 可上调
   - **Director 判断**: 采 3.0 (Findings)。理由：(a) R18 的 3 个 critical 全部修复，论文在 18 轮迭代中持续改进；(b) R19 的 critical issues (N1 novelty, N2 RE-specificity) 是 contribution-level 判断而非 soundness flaws；(c) R2 自己承认 2.5-3.0 合理并给出可上调条件

2. **Novelty 严重性**: R2 定两个 critical (N1/N2)；R1 同意实质但认为在 Findings track 仍构成 acceptable contribution。此分歧反映 Findings 录用标准的解读差异。

3. **Single-dataset concern** [W4]: R2 提出 critical 倾向，R1 部分反驳（DocRED 复现 + Dim1 跨四数据集）。最终降为 warning。

---

## Questions (需作者澄清)

**Q1 [R1, 优先级高]**: Table 2 排除 FewRel (理由: "RE's per-instance format precludes direct comparison of confusion rates")，但 §3.2 和 Appendix Table 14 报告了 FewRel pairwise SCS-confusion ρ=0.218/0.187。两处说法是否矛盾？如果 FewRel 可以计算 pairwise confusion，为何 Table 2 排除？

**Q2 [R2]**: FewRel train-origin types 为何反而 accuracy 低 8.8pp (p=0.06)？Limitations item 10 说 "opposite to contamination hypothesis"，但另一种解释是 train-split types 被选入 training set 因为 inherently 更难。论文是否考虑过这个 alternative explanation？

**Q3 [R1+R2 共识]**: TOST ±1pp inconclusive 意味着 interaction 可能达 main effect 91% (2.0/2.2pp)。Cross-pool slope consistency (p=0.60) 是否足以补充 TOST 的 power 不足？如果不够，是否应将 "largely additive" 改为更弱的表述如 "approximately additive under current statistical power"？

**Q4 [R1]**: BCS independence analysis (Appendix §M) shared variance 20.9%。在 BCS-controlled extreme-batch 实验中，extreme-BCS batches 的 mean type difficulty 分布是否与 random batches 不同？如果是，extreme-batch 的 31.2pp gap 可能部分来自 type difficulty confound。

**Q5 [R2]**: 16-rel condition 使用 single extreme batch per BCS level (Appendix Table 8 caption 承认)。作者是否考虑过用 multiple extreme batches 复现？

---

## Missing References

两位 Reviewer 均确认无明显遗漏。R2 建议补充 Zheng et al. (2023) 和 Lyu et al. (2024)，但未提供完整 citation；R1 认为相关性待确认。70 篇引用覆盖面完整。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目 external_review.paperreview_ai.enabled 未设置）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分理由**:

*Soundness (3.75/5)*: R1=3.5, R2=4.0。实验设计在 training-free IE 文献中属高水准：BCS-controlled stratification、TOST equivalence testing、within-pool analysis、cross-model validation (4 models)、partial correlation controlling centrality confound。统计报告全面透明。扣分点：TOST margin 选择与 main effect 的关系论证不足（±3pp margin vs 2.2pp main effect）；logit-scale TOST inconclusive 削弱 "largely additive" claim 的确定性；NER batch-level null 限制了框架的覆盖面。

*Excitement (2.5/5)*: R1=2.5, R2=2.5。两位 Reviewer 一致。研究问题有价值（首次通过 controlled stratification 隔离 count vs confusability），negative results 有诊断意义。但 SCS/BCS 形式同 LLM-PEE，"两维度" 概念非 surprising，typical-batch effect modest (2.2pp, CI [0.4, 4.0])，NER 无 batch-level signal，SDGD 失败后无 actionable mitigation 方案。作为纯 analytical study，knowledge increment 受限。

*Reproducibility (4/5)*: R1=4, R2=4。实验细节充分（decoding params, seed, batch sizes, bootstrap params, prompt templates 完整公开）。Anonymous review materials 链接已提供。Code promised upon acceptance。单 GPU ~72 GPU-hours。

**置信度**: 4/5。两位 Reviewer 均仔细阅读全文及所有 appendix，熟悉 IE、statistical methodology、LLM prompting 文献。交叉分享后关键问题达成共识。

**一句话总结**: R18 的 3 个 critical issues 全部修复，方法论严谨度和统计透明度在 NLP 实证论文中属高水准。主要限制是 novelty 有限（SCS 同 LLM-PEE, 概念非 surprising）和 Dimension 2 batch-level 效应的 RE-specificity + modest typical-batch magnitude (2.2pp)。达到 Findings 水平，但在该水平的低端。

**如需上调至 3.5 (Borderline Conference)**，需：(a) Abstract 加 typical-batch magnitude 数字并调整叙事权重；(b) "largely additive" 加限定词反映 logit-scale inconclusive 和 TOST power 限制；(c) Title 或 Abstract 中更明确标注 Dimension 2 batch-level 的 RE-specific boundary condition；(d) Discussion 中 practical implications 段坦诚 "diagnostic value outweighs engineering value"。

---

## Detailed Comments (逐节)

### Abstract (~156 words)
- R18-W1 修复到位，篇幅合理。
- 缺 typical-batch magnitude：加 "though typical batches yield modest ~2pp gaps" 使 impression 更 calibrated。
- "Confusability is a schema-structural property" 结尾句有效。

### Introduction
- R18-N2 修复到位："largely additive" 统一使用。
- R18-N3 修复到位：Contribution 2 焦点转为 experimental design。
- Contribution 3 (task asymmetry) framing 存在 R18 遗留分歧（R2 认为是 limitation 包装为 contribution），R19 未再升级。
- 建议：contributions 列表后加一句 scope qualification："These findings are strongest for RE under forced-choice classification; NER confusability effects are limited to pairwise analysis."

### Related Work
- SCS novelty 段诚实承认与 LLM-PEE 关系，positioning 准确。
- Chen et al. (2026) 和 Wei et al. (2023) 已补充。
- 引用密度 (70 篇) 符合 ACL 标准。
- 建议考虑补充 Zheng et al. (2023) 和 Lyu et al. (2024)（待确认具体论文）。

### Experimental Setup
- 不同数据集使用不同 embedding (Qwen3 for Few-NERD, MiniLM for others) 损害 SCS 通用性声明。Cross-check 显示 MiniLM 在 Few-NERD 上 r=0.172 > Qwen3 r=0.138（非 overfitting），但不一致性仍是 reviewer concern。

### Results
- §4.3 Practical magnitude 透明报告 2.2pp (CI [0.4, 4.0])。
- §4.4 TOST 三个 margin + logit-scale caveat 在正文报告——改进显著。
- "Largely additive" 的 caveat 可更前置。

### SDGD (§5)
- "Marginal mean BCS reduction (0.559→0.552)" 解释了 +1.4pp 无显著优势。
- Oracle routing (0.802 vs 0.504) 精确定位瓶颈。

### Discussion
- "Forced-choice classification format" 术语精确化完成。
- Practical implications "diagnostic guidelines derived from correlational evidence" 到位但可更显著。
- U-shape "dual-task burden" 应标注为 speculative hypothesis。

### Limitations
- 10 条覆盖全面，R18 遗留问题均已反映。

### Format
- 正文页数无法编译验证，估算 borderline 8-9 页，需作者确认。
- Checklist 填写质量合格。
- 匿名化无问题。