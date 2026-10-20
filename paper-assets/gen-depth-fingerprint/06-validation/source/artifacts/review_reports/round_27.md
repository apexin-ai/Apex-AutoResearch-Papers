---
round: 27
review_mode: fresh
overall_score: 3.0 Findings
timestamp: 2026-05-19T11:16:02.227540+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 27 审稿报告 — Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains

**Venue**: EMNLP 2026 via ARR May Cycle (Long Paper)
**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 论文完整性 + 写作质量）
**审稿模式**: Fresh（初审）
**轮次**: Round 27（1 轮独立审稿 + 1 轮交叉分享，关键问题达成共识）

---

## Summary

本文提出 generation depth classification 任务（gen-0/gen-1/gen-2+ 三分类），在 8 个 base model（5 families, 0.6B-8B）生成链上识别出 differential depth response (DDR) 三分区结构（drifting/intermediate/near-stationary），并用 7 特征集在 LOGO 评估下达到 leak-free binary F1=0.694。论文统计分析极其严谨，控制实验全面，Limitations 坦诚覆盖几乎所有可预见限制。贡献以经验性分析为主，但 base-model-only 限制、中等分类精度和 DDR 可能是 sampling theory 可预测结果，共同约束了影响力。

---

## Strengths

**S1. 任务定义清晰且有意义 [R1-S1, R2-S1]。** 从 binary detection 推进到 ordinal depth classification，与 model collapse 文献和 data provenance 需求自然衔接。37,058 text evaluation suite 覆盖 5 families，为后续研究提供 benchmark。

**S2. 统计分析极其严谨 [R1-S2, R2-S2]。** DDR 分区通过多指标交叉验证（Spearman ρ, Cohen's d, Glass's Δ, Cliff's δ, KS, Levene, TOST, holdout split）。Bonferroni 校正覆盖两个 test family。统计严谨度在 NLP 经验论文中属上乘。

**S3. 控制实验全面且坦诚 [R1-S3, R2-S3]。** Independent-seed (F1=0.680), length-matched subsampling (F1=0.724), seed-level demeaning (F1=0.701), TOST 等价检验，holdout generator split。逐一排除潜在混淆。

**S4. Cross-generator transfer 有说服力 [R1-S4]。** 8×7 transfer matrix 56 个 off-diagonal pairs 全部高于 chance，mean binary F1=0.810。这是论文最强的 generalization evidence。

**S5. 与 concurrent work positioning 准确 [R2-S4]。** Related Work §2.2 对三篇 concurrent work（Broken Telephone, Markovian Chains, Attractor Cycles）的区分清晰。72 篇引用质量良好，无明显遗漏。

**S6. 写作质量高，无 AI 写作标志 [R2-S5]。** 全文无解释性 em-dash，无过渡词堆积，-ing 分词极少。Limitations 异常全面（~34 行），在同类论文中罕见。

---

## Weaknesses

### Must-Fix（影响 acceptance 判断）

**W1 [Critical → Major after cross-sharing] 3/1/3 分区的 data-driven 声称被高估 + entropy min 分类不一致 [R1-W1, R2-agree]。**
- k=2 silhouette=0.632 vs k=3 silhouette=0.499。k=3 时 entropy min 自成一类而非归入 near-stationary。
- Entropy min 的 Cliff's δ=0.354 (medium) 与 Cohen's d=0.016 (near-zero) 严重不一致。用位置度量（Cohen's d）判定 near-stationarity 在 ordinal classification 论文中是 asymmetric methodological choice。
- Holdout split 产生 3/2/2 而非 3/1/3，需 binary-task d 额外 criterion 才恢复。
- **建议**: §4.2 明确讨论 Cliff's δ 不一致；Contribution 2 framing 调整为 "primary 2-partition with domain-informed refinement"（Introduction 已有此表述但 §4.2 容易误导读者认为 3/1/3 是 data-driven）。

**W2 [Major] Base-model-only 限制与 data provenance motivation 的 disconnect [R2-N1, R1-agree]。**
- Introduction 以 data provenance/training corpora contamination 作核心动机，但 web 文本主要由 instruct model 生成。
- Instruct DDR 退化至 silhouette 0.338，cross-condition transfer 接近 chance。
- QLoRA on instruct 达 0.888-0.907 但仅在 Appendix + Discussion 一句话提及。
- **建议**: 在正文 Discussion 或 Results 中更显著讨论 QLoRA instruct 结果（证明 depth signal 存活但需 end-to-end 方法），缓解 applicability gap。

**W3 [Major] DDR 新颖性需更精确 calibration [R2-N2, R1-agree]。**
- Location shift + shape stability 在 temperature-controlled sampling 下可能是可预期的结果。Discussion §5 承认仅为 informal conjecture。
- DDR 更准确的定位：已知 distributional drift 的 feature-level structured decomposition 和 empirical verification，而非发现新现象。
- R1 补充：跨 8 gen × 5 families 的一致性仍有价值，但这是 Findings 级贡献。
- **建议**: 如可能将 informal conjecture 形式化为可检验假设（哪怕定性层面）。

### Should-Fix（改善论文质量）

**W4 [Major] Generator subset 不一致影响跨实验可比性 [R1-W2, R2-W2, 交叉 agree]。**
- QLoRA "+11.6 pp" 是 6-gen LOGO vs 8-gen 3-class F1 跨子集对比，§4.1 未标明。
- Temperature ablation 混合 6-gen/8-gen LOGO。
- Instruct 实验用 within-model CV 而非 LOGO。
- **建议**: §4.1 QLoRA 增量明确标注 6-gen 对比；考虑 camera-ready 时统一或在 Method 添加 subset 对照表。

**W5 [Major] Cross-model chain confound 未完全排除 [R1-W4, R2-Q3, 交叉 agree]。**
- Transfer analysis (train-A/test-B) 是 single-generator 设计，不能排除 mixed-chain 中 generator identity 与 depth position 的潜在关联。
- §4.1 "rules out this confound" 表述过强。
- **建议**: 改为 "provides indirect/supporting evidence against" 或类似弱化措辞。

**W6 [Major] Baseline 对比 framing 需更坦诚 [R1-W5, R2-agree]。**
- Table 2: 4-det+surface binary F1=0.708 > 7-feature 0.705；4-detector ensemble 0.700 ≈ 7-feature。
- DDR 增量在 interpretability（理解 which features drift）而非 classification performance。
- **建议**: §4.3 更明确地将 7-feature 价值定位为 interpretability 而非性能优势。

**W7 [Major] Temperature 消融覆盖不足 [R1-W3, R2-agree]。**
- 仅 3 温度点 × 4 generator，可靠范围 [0.5, 0.7] 对实际部署过窄。
- t=1.0 在主消融中缺失。Cross-temp transfer 仅替换 1 个 generator。
- **建议**: 如有 GPU 资源补充 t=0.8/1.0 消融；否则在 Discussion 更直接讨论温度范围限制。

### Minor

**W8 [Minor] Independent-seed 控制仅覆盖 2/8 generator [R1-W6, R2-agree]。** 特别缺少 Mistral-7B（LOGO F1 最低）的验证。

**W9 [Minor] Table 1 vs Table 2 聚合方式不同 [R1-W8, R2-agree]。** Per-gen macro avg (0.694) vs pooled (0.705)，差 1.1pp。Caption 有注释但易混淆。

**W10 [Minor] anonymous_supplement.tgz 文件缺失 [R2-W4, R1-agree]。** 提交材料清单声明有但文件不存在。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：
1. **Overall Assessment**: 3.0 (Findings)，Excitement 2.5/5
2. **DDR 定位**: empirical characterization，非新现象发现；Findings 级贡献
3. **Base-model limitation**: 论文最核心的 practical limitation；QLoRA instruct 应更显著
4. **Generator subset**: 跨实验不一致需更透明处理
5. **Cross-model confound**: "rules out" 表述过强
6. **统计严谨度**: 本文最大优势，在 NLP 经验论文中属上乘
7. **写作质量**: 无 AI 痕迹，Limitations 异常坦诚
8. **引用**: 72 篇，覆盖完整，无明显遗漏

---

## Reviewer Divergence [REBUT]

三处 minor 分歧，不影响 overall：

1. **R1-W1 严重程度**: R1 标 Critical，R2 认为 Major。理由：3/1/3 的 post-hoc 成分明确，但 Introduction 已区分 data-driven primary partition 和 domain-informed refinement，且 primary 2-partition (k=2, silhouette=0.632) 是 robust 的。**Director 判断**: 降级为 Major——问题真实但论文已有部分 mitigation。

2. **R1-W7 downstream pilot 措辞**: R1 认为 §5 表述过强，R2 反驳 triple-hedged 已足够审慎。**Director 判断**: R2 的反驳有说服力——原文包含 "preliminary pilot" + "does not detect" + "sample size insufficient"，措辞已够审慎。

3. **R2-W3 Abstract 结尾**: R2 认为以 limitation 结尾弱化 pitch，R1 反驳诚实框定是优点。**Director 判断**: 同意 R1——在 Abstract 层面预先框定 scope 是好的学术实践，无需修改。

---

## Questions（需要作者回答）

**Q1.** Entropy min 的 Cliff's δ=0.354 (medium) 与 Cohen's d=0.016 (near-zero) 的巨大差异意味什么？如果 near-stationary 标签基于 Cohen's d 但 Cliff's δ 显示 medium effect，这是否意味着 entropy min 经历了非位置性的 rank-order 重排？这对 DDR 的 location/shape 叙事有何影响？[R1-Q3, R2-agree]

**Q2.** QLoRA on instruct (3-class F1 0.888-0.907) 为什么不在正文更突出讨论？它是缓解 base-model limitation 最有力的证据。[R2-Q2, R1-agree]

**Q3.** Cross-model chains 使用 sample-level 5-fold CV。由于不同 generator 可能贡献 chain 中不同深度的文本，classifier 是否可能学到 generator-specific features？能否提供 per-chain split 结果？[R1-Q1]

**Q4.** gen-0/gen-1/gen-2+ 的实际 class distribution 是什么？gen-2+ 合并 depth 2-4 导致约 3:1 的 gen-2+ vs gen-1 imbalance。建议在 Appendix A 明确报告。[R1-Q2]

**Q5.** DDR 的 location/shape decomposition 是否可从 temperature-controlled sampling 理论直接推导？如果是，DDR 的新颖性在于 empirical verification 还是有超出理论预测的发现？[R2-Q1]

**Q6.** Cross-domain t=0.7 Academic F1=0.628 是否说明 DDR 在方法 "可靠工作范围" 内 domain generalization 较弱？[R1-Q4]

---

## Missing References

两位 Reviewer 均未发现明显遗漏。72 篇引用覆盖 detection、model collapse、iterative generation、stylometry、data provenance 各方面。三篇 concurrent work（Broken Telephone, Markovian Chains, Attractor Cycles）已引用。

---

## External Review (Stanford Agentic Reviewer)

项目未配置 paperreview.ai 外部审稿。跳过。

---

## Overall Assessment

**Overall: 3.0 (Findings)**
**Soundness: 3.5/5 | Excitement: 2.5/5 | Reproducibility: 4.0/5**
**Confidence: 4/5**（两位 Reviewer 均为 4/5）

这是一篇统计分析严谨、评估设计周全的经验论文。任务定义（generation depth classification）有价值，DDR feature-level decomposition 在 8 gen × 5 families 上的一致性有分析意义。写作质量高，Limitations 坦诚度远超一般 NLP 论文。

三个因素使其稳定在 Findings 而非 Conference：
1. **Applicability gap**: data provenance motivation 与 base-model-only applicability 之间的断裂（instruct DDR 退化至 silhouette 0.338）
2. **Novelty ceiling**: DDR location/shape 分离可能是 temperature-controlled sampling 的可预测结果；贡献是 empirical verification 而非新发现
3. **Moderate performance**: binary F1=0.694（~30% error rate）；detection ensemble 已达到或超过此精度

**Rebuttal 可改善的点**（可能推至 3.5 Borderline Conference）：
- 将 QLoRA on instruct 结果更显著地纳入正文叙事
- §4.2 讨论 entropy min 的 Cliff's δ 不一致，调整 3/1/3 framing
- §4.1 弱化 cross-model confound 的 "rules out" 表述
- §4.3 更坦诚地将 DDR 价值定位为 interpretability

---

## Detailed Comments（逐节）

### Abstract
- ~153 words，回答了四个必答问题。NLL 已展开定义。
- R2 认为以 limitation 结尾弱化 pitch，R1 反驳认为是诚实框定。Director 判断：无需修改。

### Introduction (§1)
- 叙事线完整：recursive chains → binary detection 不足 → depth classification → DDR → contributions
- 三条 contribution 均有实验支撑
- Contribution 2 "data-driven analysis" 表述与 §4.2 的 domain-informed 实际操作之间有轻微张力

### Method (§3)
- 任务形式化简洁明确（§3.1）
- Generation chain construction 细节充分（§3.2）
- Feature extraction 动机清晰（§3.3），reference-model + surface 两组设计有理论依据
- Evaluation protocol (§3.4) 的 LOGO + LOFO 双重评估设计周全
- Generator subset 说明（§3.4 第一段）存在但不够结构化

### Results (§4)
- §4.1: LOGO F1=0.694 报告清晰；cross-model F1=0.764 的 confound caveat 在位但 "rules out" 过强
- §4.2: DDR 分区统计全面；entropy min 的处理是主要方法论争议点
- §4.3: Baseline 比较合理但 framing 可更坦诚

### Discussion (§5)
- Location/shape conjecture 明确标为 informal 和 post-hoc
- Instruct analysis 有实质内容（ρ 反转、silhouette 退化）
- QLoRA instruct 结果仅一句话提及，篇幅不足

### Limitations
- 覆盖极其全面：base-model、scale、temperature、prompt-type、domain、language、tokenizer
- 论文在 limitations 上的坦诚度是其最大竞争优势之一

### Format
- 8 页正文（Conclusion 在 p8）✅
- ACL 模板 + `[review]` 选项 ✅
- Double-blind, Anonymous author ✅
- 行号开启 ✅
- Limitations section ✅
- Ethics statement ✅
- anonymous_supplement.tgz 缺失 ⚠️