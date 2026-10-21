---
round: 9
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T17:16:42.513984+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 10 (Fresh Review)

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**Venue**: EMNLP 2026 Long Paper (ARR)
**Reviewers**: R1 (方法严谨性/实验/统计) + R2 (新颖性/定位/完整性/写作)
**交叉分享**: 完成，1 轮收敛

---

## Summary

本文研究 detect-and-reweight (D&R) 范式在含合成数据污染的 continued LM pretraining 中的有效性条件。通过 Qwen3-0.6B 上的受控实验（132M FineWeb tokens, ρ=0.4, 3 seeds），报告三个发现：(1) D&R 相对于 adaptive reweighting 的 PPL 优势中 >95% 来自 multi-epoch exposure confound；(2) 有效 reweighting 需要检测器同时具备足够 discrimination (AUC) 和良好 calibration (ECE)；(3) dual-constraint adaptive b*（α_eff ≥ τ + ESS ≥ n_min）通过 minimum intervention 原则自动选择 b，消除 grid search。

---

## Strengths

**S1. Epoch confound 发现有真实修正价值 [R1, R2 共识]**
Table 1 中 D&R full (~2.4 epochs) PPL=17.278 vs. epoch-matched D&R (~1.0 epoch) PPL=17.657，差值占 D&R 优势的 ~96.7%。独立 LR schedule 复现（17.651 vs. 17.657, Δ=0.006）排除 LR 混淆。这纠正了 Drayson et al. (2025) 中的重要效果误归因，对 D&R 社区有即时实用价值。

**S2. 实验设计严谨 [R1, R2 共识]**
系统化受控实验：逐因素消融（epoch matching → detector quality → contamination level → scale），3 seeds 提供统计基础，paired t-tests 报告显著性。Random weights 对照确认检测器信号的必要性；ESS-only 消融隔离 minimum intervention 的价值。

**S3. 诚实的 Discussion [R1, R2 共识]**
§6 不回避负面发现：downstream 零改善 (Table 3)、α_eff proxy 局限 (r=0.70)、效应量极小 (Δ=-0.020)、ρ=0.2 失败。这种透明度在分析论文中增强了结论可信度。

**S4. 数学框架简洁正确 [R1]**
Proposition 1-2 证明（Appendix A）利用协方差符号和加权集中性标准结论，推导正确。

**S5. 附录丰富 (A-Q)，可复现性好 [R1, R2 共识]**
实验细节充分（§4），Algorithm 1 伪代码清晰，17 个附录覆盖证明、消融、proxy 验证、practitioner guide。

---

## Weaknesses

### Critical / Must-Fix

**C1. Seed 42 checkpoint resume artifact 使主表核心比较可信度严重存疑 [R1-W1, R2 AGREE]**
Appendix P 揭示 seed 42 的 adaptive 模型使用 checkpoint-resumed run（前 ~1,000 步超参不同），in-distribution Δ 被膨胀约 8 倍（−0.041 resume vs. −0.005 from-scratch）。R2 定量推算：替换后 3-seed mean Δ 从 −0.014 缩小到 ~−0.002，基本消失。paired t=−6.2, p=0.025 的可信度严重存疑。**必须以 from-scratch seed 42 重跑主表**，否则 adaptive b* 的方法贡献无法成立。

**C2. 多重比较未校正 [R1-W2 critical, R2 降为 major]**
6 种方法的多组比较（≥5 个检验），所有 p 值均 uncorrected。Bonferroni 校正后 α=0.01，p=0.025 不再显著。R2 认为 epoch confound 作为 effect size decomposition 不受影响，但对 adaptive b* method claim 的统计支撑确实不足。**需报告校正后 p 值或 bootstrap CI**。

**C3. 方法新颖性不足以支撑独立贡献 [R2-N1, R1 AGREE]**
加权公式 w=(1-q)^b 完全沿用 Drayson et al. (2025)；ESS (Kish 1965) 和 α_eff 均为已有概念；dual constraint 组合是直接应用而非根本性创新。论文真正价值在分析发现，但 §1 四条 contribution 混合观察型和方法型，§3 Method 仍占 ~1.5 页，与 analysis paper 定位不匹配。**应明确定位为 analysis paper，adaptive b* 降级为 practical corollary**。

**C4. Downstream task 零改善削弱实际意义 [R2-N2, R1-W5 共识]**
Table 3 显示所有 downstream benchmarks |Δ| ≤ 0.01，方向不一致。§6 解释（"PPL improvements operate in a regime that standard benchmarks cannot resolve"）存在循环论证风险。R1 指出讨论仅 ~4 行，应扩展 PPL→downstream 阈值效应分析。**需 7B+ 验证或更细粒度评估**。

### Major / Should-Fix

**M1. 实验规模和场景过于狭窄 [R2-W1, R1-W6 共识]**
仅 0.6B/1.7B 模型，self-contamination，单一数据集 (FineWeb)，单一污染类型 (continuation)。ρ=0.3 关键中间点完全缺失。1.7B 效果减弱且 OOD 方向不稳定（holdout Δ=-0.013, Wiki Δ=+0.013）。Abstract/Introduction 的 claim 范围（"web corpora at scale"）远超实际验证范围（ρ∈{0.4, 0.6}, ≤1.7B, self-contamination）。

**M2. 论文定位仍存在模糊性 [R2-W2, R1 AGREE]**
Abstract 第一句强调 analysis（"we analyze when, why, and how"），随后介绍 method（"we introduce a dual-constrained formulation"）。§3 Method ~1.5 页对 analysis paper 偏重。建议进一步压缩 §3 至 ~0.5 页（详细推导移至附录），释放空间给更深入的分析讨论。

**M3. α_eff proxy 质量偏弱（r=0.70, R²=0.49）[R1-W3, R2 交叉后升级至 major]**
α_eff 是 dual-constraint 的理论基石（bisection 目标函数），但仅解释 49% 方差。负回归偏差（β≈-0.031）导致系统性低估。§6 已有 'Limitations of α_eff' 段落，但未分析 51% 未解释方差来源（检测器噪声 vs batch sampling variance vs 二值化 r_i 信息丢失）。R2 指出 soft label 版 α_eff（用 q_i 替代二值化 r_i）可能同时改善 proxy 质量和 granularity。

**M4. Self-contamination 生态效度有限 [R1-W4, R2 AGREE]**
实际场景合成数据来自更强模型（GPT-4 等），分布差异大。Appendix O cross-model transfer（Llama-3.2-3B）结果 mixed（MMLU+1.57pp, HellaSwag-0.60pp），PPL 比较被省略，使该实验几乎无法验证方法跨模型有效性。

### Minor

**m1. Per-batch B=4 下 dual constraint 统计可靠性存疑 [R1-W7, R2 AGREE]**
B=4 时 α_eff(0) 仅 {0, 0.25, 0.5, 0.75, 1.0} 五值，b* batch 间分布未报告。在 gradient accumulation 级别（B=16）计算可改善 granularity。

**m2. 关键证据仅在附录 [R1-W8, R2 AGREE]**
Proxy validation (r=0.70, Appendix K)、seed 42 artifact (Appendix P)、ρ=0.2 失效 (Appendix N) 影响核心 claims 可信度，应在正文中告知读者。

**m3. Responsible NLP Checklist 出现在 PDF 中 [R2-W5, R1 AGREE]**
EMNLP 2026/ARR 规定 checklist 应在 OpenReview 表单中填写，不在论文 PDF 中。移除可释放 ~1 页空间。

**m4. 效应量极小需更充分的 cost-benefit 论证 [R2-W4]**
Adaptive vs. uniform Δ=-0.020 PPL (~0.11% relative)。应增加 cost-benefit 分析：引入检测器训练/推理/calibration 开销 vs. 获得的改善。

**m5. 小格式问题 [R2]**
ρ 的 token-level vs. document-level 区分在 §3.1 定义时就应澄清；Figure 2 灰度打印可读性不足（缺 marker shape/line style）；Table 2 "4σ" 含义不明确。

---

## Reviewer Consensus [AGREE]

1. **Overall 3.0 (Findings)**: 两位 Reviewer 独立给出相同评分，交叉后维持。
2. **主要价值在分析而非方法**: Epoch confound 发现有修正价值，三条件系统化有实用性；adaptive b* 是增量工程贡献。
3. **Downstream null 是最大实践弱点**: PPL 改善未转化为任何可测量的 downstream 改善。
4. **Seed 42 artifact 必须修复**: 核心比较的统计可信度依赖于此。
5. **规模/场景过窄**: 验证范围远不足以支撑 claim 范围。
6. **定位应偏向 analysis paper**: §3 Method 篇幅与 analysis 定位不匹配。

## Reviewer Divergence [REBUT]

1. **α_eff proxy 严重性**: R1 标 major，R2 初始标 minor。交叉后 R2 倾向同意升级至 major——α_eff 是 dual-constraint 理论基石，49% 未解释方差不是 minor 精度问题。**最终共识：major**。

2. **多重比较校正严重性**: R1 标 critical，R2 交叉后认为应降为 major——理由是 epoch confound 作为 effect size decomposition 不依赖 hypothesis test。**最终判定：对 epoch confound 分析不影响（major），但对 adaptive b* method claim 为 critical**。

3. **1.7B 措辞**: R1 称"效果反转"，R2 修正为"diminished and inconsistent"（holdout 仍有 Δ=-0.013，OOD 方向不稳定）。**采纳 R2 措辞**。

---

## Questions for Authors

Q1. 能否提供排除/替换 seed 42 (from-scratch) 后的主表结果？这是决定方法贡献是否成立的关键实验。

Q2. ρ=0.3 表现如何？这是方法有效与否的临界区间，缺失不可接受。

Q3. 在 7B+ 规模上，(a) epoch confound 发现是否仍成立？(b) PPL 改善是否能传递到 downstream？

Q4. Cross-model contamination（如 GPT-4 生成）下检测器 AUC/ECE 如何变化？dual constraint 是否仍有效？

Q5. 简单固定 b=0.6 是否足够？如果是，dual-constraint 框架的 added value 是什么？

Q6. 是否考虑 soft label 版 α_eff（用 q_i 替代二值化 r_i），以改善 proxy 质量？

Q7. Appendix Q (Table 13) 的 practitioner decision summary 非常实用，为什么不放主文？

---

## Missing References

1. **Tay et al. (2022)** — PPL 与 downstream performance 的非线性关系。鉴于 Table 3 的 downstream null result，此引用几乎必需，可 contextualize §6 的发现。**最重要遗漏**。
2. **Pruthi et al. (2020)** — Influence function-based data valuation。作为 instance-level data valuation 的另一范式，有助于定位本文方法。
3. **Llama 3 technical report (Meta, 2024)** — 大规模 pretraining 中的数据 curation pipeline，可在 §2 中作为 motivation 引用。
4. Sagawa et al. (2020) DRO 已引用（references.bib 中存在），无需补充。

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。项目未配置外部审稿。

---

## Visual Layout Check（非评分项）

**状态**: 已完成（2 warnings, 6 info）

### Warnings
- **Page 5-6**: Display items 分布不均——Page 5 大段讨论 Table 1/2 和 Figure 2 的结果，但三个 display items 全部堆叠在 Page 6。建议将 Table 1（较小）提前到 Page 5 底部。
- **Page 7**: 整页纯文本（§5.3 + §6 开头），无 figure/table/equation 穿插。多处引用 Appendix 表格，读者无法即时验证。考虑将关键 sensitivity 分析图移入主文。

### Info
- Figure 1 彩色方框在灰度打印下可能难以区分（橄榄色 vs 绿色）
- Figure 2 双线仅靠颜色区分，缺 marker shape/line style
- Table 2 数值精度一致，格式规范
- Table 3 标题暗示效果不显著，审稿人可能据此质疑实验价值
- Algorithm 1 排版整洁
- Appendix 末页底部 ~1/3 空白

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 (交叉后从 3.5 下调) | 3.0 |
| Excitement | 3.0 | 2.5 | 2.5 |
| Reproducibility | — | 4.0 | 4.0 |
| Confidence | 4 | 4 | 4 |

**一句话总结**: 扎实的分析工作——epoch confound 发现纠正了文献中的重要误归因，三个有效性条件有实用价值——但方法新颖性有限（同一公式 w=(1-q)^b 的工程改进）、seed 42 artifact 使核心统计推断存疑、downstream 零改善削弱实际影响力、实验规模偏小（0.6B/1.7B, self-contamination）。达到 Findings 水准，但 novelty、statistical rigor 和 impact 不足以进入主会议。

**提升路径**:
- **→ 3.5 (Borderline Conference)**: 修复 seed 42 重跑主表 + 补充 corrected p-values + 补 ρ=0.3 实验 + 明确 analysis paper 定位（压缩 §3）
- **→ 4.0 (Conference)**: 以上 + 7B+ 规模验证 + cross-model contamination 实验 + downstream 改善（或转为负面结果论文的强定位）

---

## Detailed Comments

### §1 Introduction
- 四条 contribution 的排序和权重需调整：分析发现（1-3）应更突出，adaptive b*（4）应明确为 practical corollary
- Figure 1 概览图有效但橄榄色/绿色区分度不足

### §3 Method
- 当前 ~1.5 页对 analysis paper 仍偏重；建议压缩至 ~0.5-0.75 页，Algorithm box 和详细推导已在 Appendix
- §3.2 中 α_eff 的 proxy 质量局限（r=0.70）应在定义处即时提示，而非仅在附录和 Discussion 中讨论
- 二值化 r_i = 1[q_i ≤ 0.5] 丢失连续信息，soft label 替代方案值得讨论

### §4 Experimental Setup
- ρ 的 token-level vs. document-level 区分（footnote 9）应在 §3.1 定义 ρ 时即澄清
- Self-contamination 的生态效度局限应在 Setup 结尾即预告（而非等到 §8 Limitations）

### §5 Results
- Table 1 中必须标注 seed 42 使用了 checkpoint-resumed model（当前仅在 Appendix P）
- Display items 分布不均（全在 Page 6），建议重新布局
- §5.3 sensitivity analysis 是好内容但 Page 7 全文字无图表，视觉节奏断裂

### §6 Discussion
- 最大改进：Discussion 已从 11 行扩展到 50+ 行，覆盖 5 个主题，质量显著提升
- Downstream null result 讨论仍偏短（~4 行），应引用 Tay et al. (2022) contextualize PPL-downstream gap
- Cost-benefit 分析缺失：检测器训练/推理/calibration 开销 vs. Δ=-0.020 PPL 改善
- Practitioner decision summary (Appendix Q Table 13) 应移入主文

### §7 Conclusion
- 与 findings 匹配，前瞻性讨论已改善

### §8 Limitations
- 覆盖全面：scale、ρ range、detector coverage、N=3 seeds、self-contamination
- 建议增加一句关于 PPL-downstream gap 的 limitation

### Format
- Responsible NLP Checklist 应从 PDF 移除（在 OpenReview 表单填写）
- 移除后释放 ~1 页空间可用于加强 Discussion 或引入 Appendix Q 的 decision summary