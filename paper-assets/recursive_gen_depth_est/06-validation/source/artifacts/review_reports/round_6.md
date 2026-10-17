---
round: 6
overall_score: borderline
timestamp: 2026-05-16T20:26:04.815175+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7

**论文**: "How Deep Is Your Data? Estimating Recursive Generation Depth via Statistical Fingerprints"
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**审稿日期**: 2026-05-16
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验设计+统计分析; R2: 新颖性+完整性+Related Work+格式）

---

## Summary

本文将递归生成深度估计形式化为 ordinal classification，构建了 180K 样本的 3×3 Depth Degradation Atlas（3 model families × 3 decoding strategies × 4 depths），提取 19 个统计特征（以 perplexity tail statistics 为主）并用 Random Forest 分类，达到 70-85% 四类准确率。提出 Effective Discriminable Depth (EDD) metric 量化可区分深度边界，报告 EDD₀.₇₅=4（Pythia nucleus, p=0.001）。

---

## Strengths

1. **问题定义原创且重要**：递归生成深度估计是文献空白，填补 binary detection 和 model collapse 理论之间的 gap。形式化为 ordinal classification 是自然且此前未被探索的方向。（两位 Reviewer 一致认可）

2. **系统性实验设计**：3×3 atlas 覆盖全面，控制变量清晰，180K 样本规模充足。特征分析用三种 importance measures（SHAP + Gini + permutation, Kendall W=0.90）交叉验证，结论 robust。

3. **透明的局限性讨论**：d0 inflation、cross-strategy boundary inversion、domain-dependent FPR、BOS-seeded generation caveat 等问题在 Limitations 中坦诚披露。

4. **EDD metric 有独立参考价值**：作为刻画"可区分深度边界"的 operational metric，对后续研究有参考意义。Classifier convergence (≤0.4pp) 间接支持 EDD 的 approximate classifier-independence。

5. **Surface-text ablation 设计巧妙**：Zero-shot LLMs (30-36%) vs RF (78%) 的 42pp gap 明确证实深度信号在分布统计中而非表面文本。正确定位为 ablation 而非 baseline comparison。

6. **Cross-model recursive chain + reverse control** (84.75% / 85.75%) 是 well-designed experiment，部分解决 architecture confound。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [R1-N1 + R2 AGREE] **EDD₀.₇₅=4 的 abstract claim 仍过度概括**

Abstract 写 "EDD₀.₇₅=4 for the best-characterized model family (Pythia, p=0.001; consistent direction across all three families with graded statistical support; §4.4)"。问题：
- "consistent direction" 语义模糊——GPT-2 XL bootstrap p=0.505（不显著），读者易误解为三个模型都支持 EDD=4
- EDD=4 来自 depth extension experiment（仅 nucleus sampling），而主 benchmark (d0-d3) 在 T=0.75 时 2/9 cell 连 EDD≥3 都不满足
- Abstract 含 "§4.4" 内部引用（不规范）

→ 需将 "Pythia" 改为 "Pythia nucleus"，将 "consistent direction" 改为 "directionally consistent but with graded statistical strength (p: 0.001–0.505)"，删除 §4.4 引用。

**MF-2** [R1-N2 + R2 AGREE] **核心结果表（Table 2/4/5）缺乏不确定性度量**

Table 2（9-cell atlas accuracy）、Table 4（cross-model transfer）、Table 5（cross-strategy transfer）均无 std/CI/bootstrap interval。Figure 4 有 CI shaded bands 说明有能力计算但未推广。对于 5-fold CV，至少应报告 fold std；对于 headline accuracy，bootstrap 95% CI 是 ACL ARR 的 soundness 标配。

→ 所有准确率表格增加 mean ± std 或 bootstrap 95% CI。

**MF-3** [R2-N1 + R1 AGREE] **Related Work 遗漏 Schaeffer et al. 2025 "Position: Model Collapse Does Not Mean What You Think" (ICML 2025)**

论文 benchmark 采用 100% synthetic replacement（每代完全用上一代合成数据 fine-tune），而 Schaeffer et al. 明确批评这是不现实假设。Introduction L4-6 将问题框定为与 wild web-crawled corpora 相关——这与论文实际 benchmark 设定之间存在 framing gap。

→ (1) Related Work 引用并讨论 Schaeffer 2025; (2) 补充 ordinal classification 经典文献 (McCullagh 1980, Rennie & Srebro 2005); (3) Discussion 加 1-2 句论证 depth estimation 独立于 collapse 假设的价值。

**MF-4** [R2-N3 + R1 AGREE (downgraded to should-fix by R1)] **Curation PoC 无法支撑 practical utility claim**

Discussion §6 声称 "depth estimation enables depth-graduated data curation"，但 Appendix D.7 PoC 显示 rf_soft vs unfiltered 仅 +0.043 PPL (p=0.407, 不显著)。已从 contribution list 删除但 Discussion 正文仍以应用方向口吻提及。

→ Discussion 中 curation 表述必须加 "preliminary and inconclusive (Appendix D.7)" qualifier。

### Should-Fix（影响评分但不一票否决）

**SF-1** [R1-W1 + R2 AGREE] **LoRA rank 缺乏 sensitivity analysis**：rank=16 直接影响递归 collapse 速度。至少测试 rank ∈ {4, 16, 64} 验证 depth signal 对 fine-tuning capacity 的敏感度。

**SF-2** [R1-W4 + R2-W1 + 双方 AGREE] **EDD classifier-dependence 未被明确声明**：Definition 1 中 AUC 来自 RF classifier，EDD 是 feature+classifier 联合属性而非 distribution-intrinsic。需加 caveat sentence 并引用 Table 3 convergence 作为 empirical bound。同时需对比 EDD 与 Dohmatob (2024) scaling law 的增量信息。

**SF-3** [R1-W2 + R2-W2 + 共识] **Cross-strategy transfer 讨论篇幅不足**：d1-d3 balanced accuracy 仅 45.9% (chance=33%)，§6 仅一句提及。需整段讨论 deployment implications 和策略未知场景下的 performance lower bound。

**SF-4** [R1-N4 + R2 REBUT → 降级] **Reference model circularity ablation 不充分**：所有特征基于 Pythia-1.4B 计算，OLMo-1B 替换仅 Δ=4.0pp 且同 scale/architecture type。R2 REBUT 指出 Pythia self-model 非最高 accuracy (78.2% < GPT-2 XL 85.4%)，cross-scale 隐含验证 robustness。共识：不 invalidate 结论但建议增加 architecturally distinct reference ablation。

**SF-5** [R3-M1 recurring, 两位 Reviewer 确认] **引用完整性问题**：alemohammad2024_mad 作者不一致，knowledge_collapse2025 和 falahati2026_curated 在 OpenAlex 未找到，he2021_deberta_v3 年份标注不一致。Citation integrity 是 Must-Fix 级别。

**SF-6** [R5-W1] **Single-LoRA-instance per depth 的样本非独立性**：每个 depth 的 5000 样本来自同一 generator instance。Limitations 需加 1-2 句 caveat。

---

## Reviewer Consensus

| 问题 | R1 严重性 | R2 严重性 | 共识 |
|------|-----------|-----------|------|
| EDD₀.₇₅=4 scope 需收窄 | critical | AGREE | **Must-Fix** |
| Table 2/4/5 缺 CI | critical | AGREE | **Must-Fix** |
| 遗漏 Schaeffer 2025 | AGREE | critical | **Must-Fix** |
| Curation PoC 不显著 | should-fix | critical | **Must-Fix (conservative)** |
| d0 inflation qualify | critical | warning | **Should-Fix (共识偏高)** |
| LoRA rank ablation | warning | AGREE | **Should-Fix** |
| EDD classifier-dependence | warning | AGREE | **Should-Fix** |
| Cross-strategy 讨论不足 | warning | warning | **Should-Fix** |
| Reference model circularity | major | REBUT → should-fix | **Should-Fix** |
| Citation integrity | warning | warning | **Should-Fix (升级为 Must-Fix for ethics)** |

## Reviewer Divergence

| 问题 | R1 | R2 | 分歧本质 |
|------|----|----|----------|
| 方法论新颖性不足 | REBUT: empirical contribution 足够, EMNLP 不要求 new architecture | critical: 标准特征+RF 无方法贡献 | **严重性分歧**。R1 认为 task formalization + atlas + EDD 本身构成 contribution，classifier invariance 是 strength；R2 认为缺 learned representation 限制 excitement。共识：不 blocking 但降低 excitement，影响 overall score。|
| Seed-group confound 透明度 | W3 (warning) | REBUT: Appendix D.6 已充分 | R2 提供 Appendix 证据，R1 未反驳。采纳 R2 rebuttal — Resolved。|

---

## Questions to Authors

1. EDD₀.₇₅=4 是否在所有 9 个 atlas cell（d3-vs-d4 depth extension）中都有 bootstrap 显著性支撑？请逐 cell 报告 p-value。
2. 如果训练数据中只有 10-50% 来自上一代合成输出（accumulation 而非 replacement），depth fingerprint 是否仍可检测？
3. 如果直接用 p90_ppl 单特征做 threshold-based depth filtering，curation 效果是否等价于 RF pipeline？
4. Cross-model recursive chain 的 signal 是否可与 text quality degradation 完全解耦？即：深度不同但质量相当的样本对，classifier 能否正确判断深度？
5. 有无考虑用 distribution-free 方法（如 MMD/permutation test）作为 EDD 的 complementary measure？

---

## Missing References

1. **Schaeffer, Kazdan, Arulandu, Koyejo (2025). "Position: Model Collapse Does Not Mean What You Think." ICML 2025.** [Must-cite — 直接挑战 benchmark ecological validity]
2. **McCullagh (1980). "Regression Models for Ordinal Data."** [Ordinal classification 开创性工作]
3. **Rennie & Srebro (2005). "Loss functions for preference levels: Regression with discrete ordered labels."** [All-thresholds ordinal method]
4. **Wenzek et al. (2020). "CCNet: Extracting High Quality Monolingual Datasets from Web Crawl Data."** [Perplexity-based filtering — 与 p90_ppl top feature 直接相关]
5. **Podolskiy et al. (2021). "Revisiting the Calibration of Modern Neural Networks."** [Calibration 相关，ordinal classification 场景适用]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用（项目配置 `external_review.paperreview_ai.enabled` 未设置）。

---

## Overall Assessment

**Score: Borderline (weak accept / Findings track)**

**置信度: 4/5**（两位 Reviewer 均熟悉 model collapse 和 AI text detection 领域）

**评估理由**：

- **正面**：问题定义新颖且 well-motivated，atlas 构建系统，特征分析 robust，实验覆盖面广（7 generalization axes），透明的局限性讨论。
- **负面**：(1) 方法层面无创新（标准特征+标准分类器），excitement 受限；(2) 核心 headline 数字被 d0 inflation 拉高且缺 CI；(3) EDD₀.₇₅=4 claim 在统计支撑上不均匀；(4) 遗漏直接批评 benchmark 假设的 Schaeffer 2025；(5) downstream utility（curation）无显著证据支撑。
- **建议**：修正上述 Must-Fix 后，论文适合 EMNLP Findings track 或强 workshop paper。如要冲 main conference，需要至少一项额外贡献：(a) 方法层面改进（如 cross-strategy 自适应）；(b) partial mixing 场景实验证明 ecological validity；或 (c) 更大规模 curation PoC 达到统计显著。

---

## Detailed Comments

### §1 Introduction
- "universal and scale-variant" 内在矛盾——建议改为 "consistent in direction but scale-dependent in magnitude"
- Contribution bullet 3 过度压缩（7 axes + 6 数字），建议拆分

### §3 Method
- §3.2: LoRA rank=16 无选择依据，应加引用或 ablation
- §3.4: Definition 1 后应加 "EDD is an operational measure conditioned on feature+classifier; Table 3 demonstrates approximate classifier-independence"
- §3.4: 应对比 EDD 与 Dohmatob (2024) scaling law 的关系

### §4 Atlas
- Table 2 需加 ± std 或 CI
- §4.1 应增加一段讨论 d2 作为最困难类的原因和 implications

### §5 Generalization
- Table 4/5 需加 CI
- generalization.tex line 110 残留 "signal universality"，应改为 "signal consistency"
- End-to-end PLM negative result (Appendix A.7-A.8, 58-65% vs RF 70-85%) 应提升到主文作为支撑 "why simple features suffice" 的论据

### §6 Discussion
- Cross-strategy bottleneck 需整段讨论
- Curation 表述加 "inconclusive" qualifier
- 应论证 depth estimation 独立于 collapse 假设的价值

### Limitations
- 加 single-LoRA-instance per depth caveat
- 加 partial mixing (accumulation) 场景作为 key open question

### References
- 逐条核实 alemohammad2024_mad, knowledge_collapse2025, falahati2026_curated, he2021_deberta_v3
