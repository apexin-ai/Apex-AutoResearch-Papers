---
round: 23
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T03:40:22.686020+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — Round 23 (Fresh Review)

**论文**: "Depth Profiling: Classifying Recursive Generation Depth in Base LLM Text Chains"
**Venue**: EMNLP 2026 (ARR Long Paper)
**审稿模式**: Fresh（重新审稿，无上轮记忆）
**Reviewers**: R1（方法严谨性+实验设计+统计分析）, R2（新颖性+写作质量+完整性）

---

## Summary

本文提出 generation depth classification 任务，将文本按递归生成深度分类为 gen-0/gen-1/gen-2+，并识别出 differential depth response (DDR) 三分结构：3 个 drifting 特征（entropy mean, TTR, hapax ratio）、1 个 intermediate（entropy std）、3 个 near-stationary（entropy max, tail decay, entropy min）。在 8 个 base model（5 个 family，0.6B–8B）上用 LOGO 评估，leak-free binary F1 = 0.694。实验控制极为严谨（20+ 个附录覆盖多层消融），写作质量良好，格式合规。核心局限：仅限 base model（instruct 模型下 DDR 结构被颠覆）、gen-0 seed sharing 导致 3-class 评估存在 leakage、下游效用实验统计效力不足。

---

## Strengths

**S1. 任务定义新颖且有意义。** [R1,R2 共识] Generation depth classification 将二元 real-vs-synthetic 检测推进到更细粒度的 provenance 分析。与 model collapse 文献的联系建立得好。

**S2. 实验控制极其严谨。** [R1,R2 共识] LOGO + LOFO + seed-level demeaning + independent-seed + length-matched + random-subsample control 构成多层次 confound control pipeline。R1 评价"很少见到如此完整的 control 链"。

**S3. DDR 三分结构有分析价值。** [R1,R2 共识] 将特征空间分解为 drifting/intermediate/near-stationary 提供了理解 recursive generation dynamics 的有用视角。多指标交叉验证（ρ, d, KS, Levene, TOST, Glass's Δ, Cliff's δ, k-means, holdout split）增强可信度。

**S4. 分析深度突出。** [R1,R2 共识] 20+ 个附录系统覆盖消融、混淆矩阵、特征分布、跨域迁移、跨温度迁移、扰动鲁棒性、下游效用等维度。QLoRA upper bound（3-class F1=0.905）有效定位了 handcrafted features 的价值。

**S5. 写作质量良好。** [R2] 无 AI 写作痕迹，Abstract 信息密度高，引用完整（68 条），格式合规（≤8 页正文，匿名化完整，ACL review 模板）。

**S6. Limitations 讨论诚实透明。** [R1,R2 共识] 对 base-model 限制、instruction tuning 退化、temperature sensitivity、3-class metric inflation 等问题的自我批评到位，没有 overclaim。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. [critical] 仅限 base model 的限制对论文 significance 构成根本性约束。** [R1-N2, R2-N2, 完全共识]
- Appendix K 显示 3 个 instruct 模型家族（OLMo, Qwen, Llama）全部表现灾难性：entropy mean ρ 从 −0.60 翻转至 +0.48，6/7 特征方向反转，OLMo LOGO F1 从 0.763 暴跌至 0.338。DDR 的核心结构在 instruct model 下被根本性颠覆。
- 论文多处措辞暗示超出 base-model 范围的一般性（§1 "how language models transform distributions"、§6 "classifying text by generation depth"），超出实验支撑。
- Title 已含 "Base LLM"，但 Abstract/Introduction/Conclusion 中仍需更显著地限定 scope。
- 建议：(a) 在 Abstract 前几句即明确 base-model scope；(b) 将 instruct 结果从附录提升到正文 Discussion 作为核心发现；(c) 讨论 DDR 特征方向反转的理论含义。

**C2. [critical] Gen-0 seed sharing 使三分类 LOGO 评估存在 leakage。** [R1-N1 critical, R2 agree 但倾向 should-fix]
- LOGO 中 held-out generator 的 gen-0 文本与训练集 gen-0 完全相同（共享 Wikipedia seed passages），构成 data leakage。Confusion matrix 显示 gen-0 recall=99.4%（vs gen-1: 75.0%, gen-2+: 73.7%），不对称性与 leakage 一致。
- Binary F1 = 0.694 作为 primary metric 不受影响（排除 gen-0），但论文的 Contribution 1 和 Abstract 同时呈现 3-class F1 = 0.762，后者受 gen-0 leakage 污染。
- Independent-seed 实验（Appendix T）仅 2 generators（Pythia-2.8B, OLMo），不足以验证 full 3-class LOGO 可靠性。
- 建议：在 full 8-gen LOGO 下进行 independent-seed 实验并报告 3-class F1；或将论文 framing 调整为以 binary 为核心。

**C3. [critical] 下游效用实验统计效力不足，且结果削弱论文价值主张。** [R1-W2 warning, R2-N1 critical, 共识]
- Downstream fine-tuning 实验仅 n=3 seeds，Cohen's d 值 86.0/119.7 为 artificial inflation。TOST 结果虽然 "practically indistinguishable"，但 n=3 的统计效力极低。
- 更根本的问题：depth-aware curation 与 random subsampling 无差异，否定了 depth classification 最直觉的应用场景（数据筛选）。论文试图将此定位为 supporting evidence（DDR 是 diagnostic 而非 prescriptive），但 Discussion 和 Contribution 4 仍将此作为核心结论反复引用。
- 建议：增加 seeds 至 10-20；将 Contribution 4 降级为 preliminary observation；更坚定地 commit 到 "scientific characterization" 方向。

### Should-Fix（影响评分但不一票否决）

**W1. [warning] Tail decay 的 "near-stationary" 分类统计支撑不足。** [R1-W1, R2 agree]
- TOST 等效性检验（ε=0.20）仅 4/8 generators 通过，|d| 范围 0.15–0.22 已接近 intermediate 区间（entropy std d=0.16）。需放松至 ε=0.25 才达 7/8。
- 建议考虑将 tail decay 移至 intermediate 组（3/2/2 结构），或在正文充分讨论其边界地位。

**W2. [warning] Cross-domain 实验使用 t=1.0，与主实验 t=0.7 不一致，domain 和 temperature 效应混淆。** [R1-W5, R2 agree 并强化]
- t=0.7 下 Academic domain binary F1 降至 0.626（vs t=1.0 的 0.739），cross-domain robustness 部分归功于高温度而非真正的 domain 迁移。
- 建议 cross-domain claim 基于 t=0.7 结果。

**W3. [warning] 多个 generator subset (5/6/8-gen) 混用增加 cross-experiment 比较复杂度。** [R1-W4, R2 agree]
- 不同 section/appendix 使用 5/6/8-gen subsets，缺统一对照表。核心 claim 应统一使用 8-gen LOGO。

**W4. [warning] Baseline 对比缺少 n-gram 统计特征 baseline。** [R2-W4, R1 partially agree]
- 缺少 character n-gram profile 等简单统计 baseline。Avg-LogProb 和 QLoRA 已有但可补充。

**W5. [warning] 3 个 drifting features 高度相关（r=0.81-0.97），DDR 的 "3-drifting" 结构可能被维度高估。** [R1-M3, R2 agree]
- TTR-hapax r=0.97，entropy mean-TTR r=0.86。需 PCA/factor analysis 验证是否为单一 latent factor。

**W6. [warning] Introduction 的 model collapse/data provenance 双动机在 Discussion 中发展不均衡。** [R2-M1, R1 agree]
- Provenance 方向在 downstream 实验后基本被放弃，但 Introduction 仍保留此动机。论文应坚定 commit 到 scientific characterization 方向。

---

## Reviewer Consensus [AGREE]

1. **Base-model-only 是全文最根本的约束**（C1）：DDR 在 instruct 模型下完全失效，论文的实际影响力受限。两位 Reviewer 均标记 critical。
2. **Gen-0 seed sharing 需要 full 8-gen independent-seed 3-class F1 来 resolve**（C2）：当前 binary F1 不受影响，但 3-class 叙事缺乏干净支撑。
3. **下游 utility 是最薄弱的 Contribution**（C3）：n=3 统计效力不足 + 结果本身否定数据筛选价值。Contribution 4 需降级或加强。
4. **实验控制极其严谨**：多层 confound control 是论文最大优势。
5. **DDR 的分析价值真实**：即使分类性能一般，drifting/stationary 分解提供了有用的科学视角。
6. **写作质量和格式合规**：无 AI 痕迹，引用充分，满足 ARR 要求。

---

## Reviewer Divergence [REBUT]

**D1. DDR "框架" 是否被过度包装。** [R2-N3 critical, R1 REBUT]
- R2 认为 DDR 本质是按相关系数分组的描述性分析，不构成方法论贡献。
- R1 反驳：DDR 经过 6 层独立验证（k-means clustering, 多指标交叉验证, per-generator TOST, TOST bound sensitivity, holdout generator split, heteroscedasticity robustness），超出简单描述性分析。
- **Director 判断**：R1 的举证更有说服力——DDR 的验证深度确实超过标准 EDA。但 "framework" 措辞可能过强，建议调整为 "empirical decomposition" 或 "empirical finding"。**总体倾向 R1，但建议适度降低包装力度。**

**D2. Baseline "反超" 的严重性。** [R1-W3 warning, R2 REBUT]
- R1 认为 4-detector ensemble binary F1=0.708 > 7-feature 0.705 构成"反超"，削弱 DDR 方法论贡献。
- R2 反驳：binary F1 差异仅 0.001（noise 范围内）；论文已声明定位为 "contextualizing" 而非 "competitive advantage"；DDR 价值在可解释性而非性能。
- **Director 判断**：R2 更准确。Binary F1 差异 0.001 不构成有意义的"反超"。3-class 差异 0.071 值得讨论，但论文定位合理。**不构成独立 weakness。**

**D3. Cohen's d 异方差问题的严重性。** [R1-W6 warning, R2 REBUT]
- R1 认为正文依赖 pooled Cohen's d 而非 heteroscedasticity-robust 指标。
- R2 反驳：论文已在附录报告 Glass's Δ 和 Cliff's δ，DDR partition 在 robust 指标下保持不变。
- **Director 判断**：R2 更准确。这是 presentation issue（正文应提及 robust 指标），不是方法论缺陷。**降级为 minor。**

---

## Questions（需要作者澄清）

**Q1** [R1,R2 共识] 能否在 full 8-gen LOGO 设置下报告 independent-seed 3-class F1？这是验证 gen-0 分类可靠性的关键实验。

**Q2** [R1] 8-gen 设置下 cross-reference spread 是否仍 ≤ 0.013？

**Q3** [R1,R2 共识] 是否考虑 PCA/factor analysis 验证 3 个 drifting features 是否为单一 latent factor？

**Q4** [R2] 如果 depth classification 对数据筛选无帮助，最有价值的应用场景是什么？请给出具体用例。

**Q5** [R2] DDR 三分法阈值（|ρ|=0.60, 0.10）的 sensitivity analysis？（R1 指出论文已有 ±0.10 分析和 TOST bound sensitivity，但 R2 可能遗漏。）

**Q6** [R1] Qwen3-1.7B 在 t=0.5/0.7 下 binary F1 完全相同（0.751），CI 缺失原因？

**Q7** [R1] Table 2 pooled vs per-generator macro average 差异从何而来？

**Q8** [R2] Instruction tuning "reverses feature drift direction" 基于 3 个家族（非 R2 所述的 1 个），但仍需确认：Llama-3.2-3B-Instruct 的 LOGO F1 是多少？

---

## Missing References

**共识推荐**：
- Self-training/self-play 文献（Yuan et al. 2024 "Self-Rewarding LMs"; Chen et al. 2024 "SPIN"）—— 在 §2.2 简要提及作为 training-loop iterative generation 的对比
- Ordinal regression NLP 应用文献 —— 当前主要引用通用 ML 领域

**可选**：
- Bao et al. (2024) "On the Reliability of AI Text Detectors" —— 与 cross-generator 分析相关
- 更多 lexical diversity 方法论文 —— R2 提到 MTLD/MATTR，但 R1 指出论文已在 §2.3 引用

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | 3/5 |
| Excitement | 2.5/5 | 2/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.0 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**：
- 任务定义新颖（generation depth classification vs binary detection），DDR 三分结构是有价值的经验性发现，实验控制极其严谨 —— 这些优势支撑 Findings 级别。
- 但三个 critical 问题共同限制了论文达到 Conference 水平：(1) base-model-only 限制使论文在 instruct 模型主导的真实场景下适用性极低；(2) gen-0 seed sharing 使核心三分类评估不完整；(3) 下游效用实验统计效力不足且结果否定了最直觉的应用场景。
- 方法论贡献（特征工程+XGBoost）在 novelty 维度偏弱（Excitement 2.5/5）。DDR 的价值更多在分析框架而非分类性能，但论文对此的 framing 不够坚定。
- 如果作者能 (a) 补充 instruct 模型的系统实验（即使为负面结果），(b) 提供 full 8-gen independent-seed 3-class F1，(c) 更坚定地定位为 scientific characterization，论文有潜力达到 3.5 (Borderline Conference)。

---

## Detailed Comments（逐节）

### Abstract
- 信息密度高，四问题均有回答。
- "base (pretrained)" 限定在最后一句出现，位置过靠后。建议在前几句即明确。
- 3-class F1 受 gen-0 leakage 影响，应标注或移除。

### Introduction (§1)
- 叙事线基本完整（背景→缺口→洞察→贡献），但 model collapse 和 data provenance 双动机在后文发展不均衡。
- Contribution 4（downstream null result）以 n=3 实验支撑，统计基础薄弱。
- "how language models transform distributions under iterative conditioning" 措辞暗示超出 base-model scope。

### Related Work (§2)
- 组织合理，非 survey 式罗列。
- §2.3 引用密度略低（但 R1 指出实际有 8 篇引用，5 行文本）。
- 缺少 self-training/self-play 文献和 ordinal regression NLP 应用。

### Method (§3)
- 实验设计严谨，LOGO + LOFO 评估协议设计合理。
- 3-class 分组决策有 Appendix D 5-class 实验支撑。
- 参考模型选择（Pythia-410M）有 cross-reference 消融（spread ≤ 0.013），但应在正文更显著地讨论。

### Results (§4)
- Table 1 设计合理（binary F1 在前），但 gen-0 seed sharing 脚注信息过于不显眼。
- §4.2 DDR 分析有价值，多层验证增强可信度。正文应同时报告 Glass's Δ/Cliff's δ 而非仅在附录。
- §4.3 baseline 对比定位合理（"contextualizing" 而非 "competitive"），但缺 n-gram baseline。

### Discussion (§5)
- "gen-1 per-class F1=0.63" 指代不明，应标注来源。
- model collapse/provenance 动机与 diagnostic 定位之间仍有 framing 张力。
- downstream utility 结论引用力度与 n=3 统计基础不匹配。

### Limitations (§8)
- 诚实全面，覆盖 base-model、temperature、scale 等。
- 温度敏感性和 cross-domain 温度混淆可更显著讨论。

### Appendix
- 体量巨大（20+ 个），系统覆盖各潜在质疑。
- Independent-seed 控制（Appendix T）仅 2 generators，需扩展。
- 定性示例（Appendix X）仅 1 条 Pythia 链，建议补充其他模型。

### Format
- 正文 ≤ 8 页，Limitations 在 Conclusion 后 References 前，匿名化完整。
- Figure 1 x 轴标签字体偏小（可能 < 7pt）。
