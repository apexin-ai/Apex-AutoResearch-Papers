---
round: 9
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-19T03:13:18.141213+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 12 (Fresh Review)

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**Venue**: EMNLP 2026 Main Conference (ARR May cycle)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 完整性 + 写作质量)
**审稿模式**: Fresh (重新审稿)

---

## Summary

本文将递归生成深度估计形式化为序数分类任务，构建了一个 180K 样本基准（3 模型族 × 3 解码策略 × 4 深度），用 Random Forest 在 19 个统计特征上实现 69-86% 四分类准确率（chance=25%）。论文定义了 Effective Discriminable Depth (EDD) 度量，构建了 Depth Degradation Atlas，并在 8 个泛化维度上进行系统评估。这是一项问题定义新颖、实验执行严谨、报告透明诚实的实证研究，但在生态效度、跨策略部署和规模可扩展性方面存在结构性限制。

---

## Strengths

**S1. 任务定义的原创性 [R1, R2 一致]。** 递归生成深度估计是一个真正未被研究过的问题，填补了 model collapse 理论（假设深度已知）和二分类检测（忽略深度信息）之间的空白。EDD 度量的形式化（Definition 1, Eq. 1）数学自洽且有概念价值。

**S2. 系统性实验设计 [R1, R2 一致]。** 3×3 model-strategy grid × 4 depths = 180K 样本，加上 8 个泛化轴（cross-model, cross-strategy, cross-scale, cross-domain, cross-model chains, prompted generation, seed replication, depth extension），构成了非常全面的实验矩阵。基线覆盖四类方法且对比公平。

**S3. 统计实践透明 [R1 主导, R2 认同]。** Bootstrap 95% CI 贯穿主要结果；domain bias 分析的三子实验设计严谨；初始 bug 透明报告并修复；RF seed robustness 验证（std=0.06pp）。

**S4. 诚实的局限性讨论 [R1, R2 一致]。** d0 膨胀、cross-strategy 失败、14B EDD=0、5 个 cross-scale 混杂因素、单 LoRA 种子不确定性、curation PoC 非显著——均被如实报告。Limitations 覆盖 12+ 个具体限制。

**S5. 理论-实证对应 [R1 主导]。** tail erosion 理论预测与 9/9 cells 的 p90_ppl top-2 ranking 对应；temperature d1 median p90_ppl (92.2) 与 nucleus d2 median (92.3) 的精确匹配验证了 strategy-dependent convergence 理论。

**S6. 特征重要性三重验证 [R1 主导]。** Gini/SHAP/permutation 三种方法的一致性（Kendall's W=0.90, p<0.005）增强了核心发现的可信度。

**S7. Related Work 覆盖充分 [R2 主导]。** 67 条引用覆盖 model collapse、AI text detection、membership inference、ordinal classification、decoding strategies 五个维度，达到 EMNLP 标准。

---

## Weaknesses

### Must-Fix (2 项)

**W1. 生态效度差距过大，需更清晰的 scope 声明 [R1-W1, R2-W2; AGREE]。**
基准使用 Wikipedia 种子 + LoRA fine-tune 的 full-replacement recursive chain（每步完全替换训练数据）。真实世界的递归污染涉及 accumulation（混合真实+合成数据）、全量微调、混合语料、未知比例。论文 Limitations 有承认但 framing 不够突出。
- **要求**: Abstract/Introduction 明确声明 full-replacement chain 的 scope 限制；Discussion 增加 accumulation setting 讨论。

**W2. Cross-strategy transfer 在部署场景下近乎失败 [R1-W2; R2 交叉升级认同]。**
d1-d3 balanced accuracy 仅 45.9%（chance=33%），出现 d1/d2 boundary inversion（d1v2 AUC < 0.5）。在实际部署中解码策略几乎总是未知的。Two-stage pipeline 恢复 11.5pp 但仍有大幅差距。论文标题以 "estimating recursive generation depth" 为核心 claim，但在最常见场景下该 claim 实质不成立。
- **要求**: Abstract 补充 d1-d3 balanced accuracy 到同等显著位置；将 cross-strategy bottleneck 从 limitation 提升为独立贡献/发现。

### Should-Fix (7 项)

**W3. d0 膨胀导致 headline metrics 误导 [R1-W3, R2-W6; AGREE]。**
d0 recall >97% 使 4-class accuracy 和 cross-model transfer 66.4% 被系统性抬升。d1-d3 balanced accuracy（within-distribution 71.6%, cross-model 55.4%, cross-strategy 45.9%）才是评估实际能力的关键数字。
- **要求**: 所有 headline 数字旁系统性并列 d1-d3 balanced accuracy。

**W4. Cross-scale 证据不足 [R1-W4 Should-Fix, R2-W1 Must-Fix; Director 裁定 Should-Fix]。**
仅 3 个 7-14B 模型，5 个混杂因素同时存在（QLoRA、样本量、仅 nucleus、vocabulary mismatch、14B 自参考）。两个 7-8B 模型 AUC 轨迹完全不同（Llama monotonic vs Qwen U-shaped），无法确定主流 pattern。14B 的 EDD=0 因自参考混杂不可直接与 1-1.5B 比较。
- **Director 裁定理由**: R2 将 14B EDD=0 视为 "致命瓶颈" 并推断 70B+ 必然失效，但 R1 正确指出 14B 自参考混杂使该数据点不可靠，scale effect 和 reference model effect 未被分离。在混杂未分离前，两种推断均缺乏充分依据。论文已标记为 "Preliminary"，应进一步降调。
- **要求**: Abstract/Contributions 降调 cross-scale claim；声明 "cross-scale results are confounded and should be interpreted as existence proofs"；若可能用 Pythia-1.4B 作为 14B reference 补充实验。

**W5. Curation PoC 主比较不显著 [R1-W5, R2-W7; AGREE]。**
RF vs unfiltered p=0.407, d_z=0.41。RF vs random 的 3 个比较未做多重校正（Bonferroni 后 borderline non-significant）。
- **要求**: 标记为 inconclusive；应用 Bonferroni 校正；Discussion 中不以 "feasible" 描述 depth-graduated filtering。

**W6. Abstract 信息过载 [R1-Detailed, R2-W4; AGREE]。**
约 200 词塞入 20+ 数字和多层嵌套括号。
- **要求**: 重写 Abstract，保留 2-3 个关键数字，分为 problem-method-result 三层叙事。

**W7. Discussion 实质缺失 [R1-Detailed, R2-W5; AGREE]。**
Section 7 仅一段约 80 词，核心讨论被放逐到 Appendix Extended Discussion。
- **要求**: 扩展至 3-4 段，涵盖 accumulation setting、model collapse mitigation 交互、部署 roadmap。

**W8. 多重共线性下 feature importance framing 不当 [R1-W6; R2 partially agree]。**
VIF>10 的 14-16/19 features 使 individual Gini importance 不可靠，但正文以 "p90_ppl ranks top-2 in 9/9 cells" 为核心叙事。三重验证（Kendall's W=0.90）缓解了 validity 问题，但 framing 应以 feature group 而非 individual feature 为分析单位。

**W9. 算法贡献定位需强化 [R2-W3 Must-Fix; R1 REBUT; Director 裁定 Should-Fix]。**
RF/XGBoost/LightGBM 在 0.4pp 内收敛，说明分类器选择不构成贡献。
- **Director 裁定理由**: R1 的反驳有理——论文明确自我定位为 "empirical study and problem formalization"，*ACL 有 benchmark/analysis paper 先例（RAID, M4-SemEval）。Classifier convergence 恰恰证明核心贡献在 feature design + task formalization。这是 positioning 问题而非缺陷，不应列为 Must-Fix。
- **要求**: Introduction 强化 empirical study + problem formalization 定位。

---

## Reviewer Consensus [AGREE]

1. **生态效度差距是最核心的结构性问题**（R1-W1 ≡ R2-W2）
2. **d0 通胀系统性抬升 headline metrics**（R1-W3 ≡ R2-W6）
3. **Cross-strategy 在 d1-d3 近乎失败（45.9%）是部署的根本障碍**
4. **Curation PoC 统计不显著（p>0.4）**（R1-W5 ≡ R2-W7）
5. **Abstract 过载 + Discussion 缺失是写作层面最大问题**
6. **Prompted generation 验证仅 1/9 cells 不足**
7. **Overall 3.0 (Findings) — 两位 Reviewer 评分完全一致**

## Reviewer Divergence [REBUT]

1. **算法贡献是否构成 Must-Fix**: R2 认为 Must-Fix（"方法论贡献几乎为零"），R1 REBUT（benchmark paper 有先例，classifier convergence 证明 feature value）。**Director 采纳 R1 立场**——降级为 Should-Fix (W9)。

2. **14B scale 瓶颈的严重程度**: R2 列 Must-Fix（"致命"，推断 70B+ 必然失效），R1 列 Should-Fix（自参考混杂使数据不可靠）。**Director 采纳折中立场**——Should-Fix (W4)，14B 数据因混杂不可直接推断。

3. **AI 写作痕迹 (R2-W8)**: R1 REBUT（无具体例子，作者已声明使用 AI 辅助）。**Director 采纳 R1 立场**——不列入 weakness，但建议作者自查 dash 和 -ing phrases。

---

## Questions (需要作者澄清)

**Q1 [R1].** Accumulation setting（混合真实+合成数据训练）下深度信号预期如何变化？

**Q2 [R1].** Cross-model chain 的 84.75% 中有多少来自 depth signal vs architecture shift？能否通过与 single-model chain 对比做定量分解？

**Q3 [R1].** 为什么 d3 recall 一致高于 d2？是否因为 d3 有更多独特退化信号？

**Q4 [R1].** Feature extraction "requires no GPU" 的声明是否准确？Pythia-1.4B forward pass for 5000×512 tokens 在 CPU 上是否真的只需 2 分钟？

**Q5 [R1].** 不同深度数据间的间接统计依赖关系对 CV 独立性假设有何影响？

**Q6 [R2].** 14B 的 higher-order moments 成为 top features 是否暗示了 feature adaptation 策略？

**Q7 [R2].** τ=1.1 时 depth signal 消失——高 temperature 能否有效规避 depth estimation？代价是什么？

---

## Missing References

1. **Muennighoff et al. (2024)** "Scaling Data-Constrained Language Models" — data mixing 与 scale-dependent attenuation 相关 [R2]
2. **Ilyas et al. (2022)** "Datamodels" — data attribution 与 provenance toolkit 相关 [R2]
3. **孤立 bib entry**: c2pa2024 在 bib 中但未在正文引用 [R1, R2 一致]
4. **5 条引用 mismatch**: alemohammad2024_mad, garces_arias2025_decoding_decoded, he2021_deberta_v3 (year mismatch), llama3, guo2024_biscope [R1]

---

## External Review (Stanford Agentic Reviewer)

外部审稿未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**
**Confidence: 4/5**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.5/5 | 3.5/5 | 3.5/5 |
| Excitement | 3.0/5 | 2.5/5 | 2.75/5 |
| Overall | 3.0 | 3.0 | **3.0** |

**综合评价**: 问题定义新颖且 timely，实验执行严谨，统计实践透明，局限性报告诚实——这些是论文的核心优势。但两个结构性限制压制了评分：(1) 生态效度差距（controlled full-replacement chain vs real-world accumulation）使方法的实际适用性存疑；(2) 跨策略迁移在 d1-d3 仅 45.9%，在最常见的部署场景（策略未知）下深度估计接近随机。方法上无算法创新（标准 RF + 标准特征），核心贡献在 task formalization + systematic empirical analysis 层面。适合 Findings 发表，距 Main Conference 需要：(a) 缩小生态效度差距（accumulation setting 实验），或 (b) 解决 cross-strategy 瓶颈（robust strategy-invariant features），或 (c) 提出有算法新颖性的 depth estimation 方法。

---

## Detailed Comments (逐 Section)

### Abstract
- 信息密度过高，20+ 数字塞入约 200 词。建议重构为 3 层叙事（problem → method → key findings），保留 2-3 个关键数字。
- "69-86% four-class accuracy" 应伴随 d1-d3 balanced accuracy 作为等权修正。
- "cross-model transfer reaches 66.4% (2.7× chance)" 中 d1-d3 (55.4%) 应提升到同等位置。

### Introduction (§1)
- 叙事线清晰：递归循环 → 工具空白 → fingerprint 发现 → 贡献。
- "empirical study and problem formalization rather than an algorithmic contribution" 的自我定位恰当且诚实。
- Contribution 列表第 3 点过于冗长，数字细节应移至正文。

### Related Work (§2)
- 覆盖全面（67 references），positioning 准确。
- 补充引用 Muennighoff et al. (2024) 和 Ilyas et al. (2022)。

### Method (§2)
- Problem definition 形式化清晰。建议增加 full-replacement vs accumulation 区分。
- EDD 定义数学自洽。T=0.70 选择应添加独立依据讨论。
- 19 features 的 effective dimensionality ~4-5 是重要发现，应更突出。

### Theory (§3.1)
- Temperature d1 ≈ nucleus d2 (92.2 vs 92.3) 的验证有力但为 cherry-picked 单一比较。

### Atlas (§4)
- Strategy effect (9.3pp) > model effect (7.2pp) 是有趣发现。
- Feature importance 应以 group 而非 individual 为核心叙事。
- Feature trajectory 图应从 Appendix 移回正文。

### Generalization (§5)
- Baseline comparison 全面公平。Classifier convergence 证明 feature-determined ceiling。
- Cross-model d2 recall (26.8-52.6%) 是最大弱点。
- Cross-strategy failure 是论文最重要的负面结果，framing 应更突出。
- Cross-scale 标记 "Preliminary" 恰当，应进一步降调。

### Discussion (§7)
- 仅一段约 80 词，远不够。需扩展至 3-4 段。

### Limitations
- 覆盖广泛且诚实，特别是 domain-dependent FPR 和 adversarial robustness 的承认。
- 建议增加 full-replacement vs accumulation 作为 top-level limitation。

### Appendix
- 信息量极大。Temperature robustness 中 "memorization as prerequisite" (τ=1.1) 是重要机制洞察。
- Domain bias analysis 是亮点。
- Feature extraction GPU/CPU 声明需核实。

### 格式合规
- ACL review template ✓, double-blind ✓, Anonymous ✓
- 清理孤立 bib entry c2pa2024；核实 5 条引用 mismatch。
