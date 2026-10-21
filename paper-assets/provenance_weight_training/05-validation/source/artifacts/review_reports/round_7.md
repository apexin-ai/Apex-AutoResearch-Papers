---
round: 7
review_mode: fresh
overall_score: 2.5-3.0 (Borderline Findings to Findings)
timestamp: 2026-05-21T11:41:38.942087+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 1

**论文**: "When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining"
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量）

---

## Summary

本文研究 detect-and-reweight 范式在含合成数据污染的 continued LM pretraining 中的有效性。三个贡献：(1) 识别 epoch confound——D&R 的 PPL 优势 96% 归因于多 epoch 曝光，epoch-matched 后优势从 0.384 缩至 0.017；(2) 提出 dual-constraint 自适应 b* 框架（α_eff quality floor + ESS stability ceiling），在 Qwen3-0.6B / 132M tokens / 40% self-contamination 下取得 Δ=−0.020 PPL（~0.11%）改进，但下游任务无可测量变化；(3) 分析 detector 的 calibration + discrimination 要求。

---

## Strengths

**S1. Epoch confound 分析有实质纠偏价值。** [R1, R2 共识] Table 1 的 epoch-matched 实验严谨地将 D&R 的 0.384 PPL gap 分解为 epoch 效应（96%）和 filtering 效应（4%），揭示了 prior work (Drayson et al. 2025) 中被忽视的混淆变量。这对社区理解 D&R 的实际机制有意义。

**S2. 框架形式化清晰。** [R1, R2 共识] Dual-constraint 数学表述简洁（§3.2），Proposition 1–2 证明正确（Appendix A），Algorithm 1 可直接复现。三种 regime（clean / α_eff-binding / ESS-binding）划分直观。

**S3. 消融实验覆盖面广。** [R1, R2 共识] Grid search 全空间、threshold 敏感性、contamination level (ρ=0.2/0.4/0.6)、scale (0.6B/1.7B)、constraint regime 分解、detector 家族（3种）均有系统消融。Appendix 13 个 display item 支持可复现性。

**S4. Detector 对比分析有实用价值。** [R1, R2 共识] Table 10 展示 TF-IDF+LR (AUC=0.94, ECE=0.048) 成功、GPT-2 (AUC=0.91, ECE=0.131) 和 N-gram (AUC=0.73, ECE=0.069) 失败，isolate calibration 和 discrimination 的独立作用。

**S5. 诚实的 Limitations。** [R1, R2 共识] §8 覆盖 self-contamination、scale、ρ range、detector coverage、evaluation、effect size 六个方面，坦诚承认核心局限。

**S6. 格式完全合规，引用均真实。** [R2 确认] ACL 两栏 ✅ | 匿名 ✅ | 8 页限制 ✅ | Limitations ✅ | Checklist ✅ | 46 条引用无伪造。

---

## Weaknesses

### Critical（两位 Reviewer 共识）

**W1. 效果大小不足以支撑方法论贡献。** [R1-W1, R2-N1 共识]
- Adaptive b* 的 PPL 改进 Δ=−0.020（0.11%），接近 noise margin（std ±0.006–0.007）
- 下游任务 |Δ|≤0.01（§H："no meaningful downstream impact"）
- ρ=0.6 改进更大（Δ=−0.032, p=0.004）但仍为 0.18%
- 论文在 analysis paper 和 method paper 之间定位模糊；作为 method paper，evidence 不足

**W2. B=4 下 dual-constraint 框架实质退化。** [R1-W2, R2 AGREE]
- α_eff 仅有 5 个离散值 {0, 0.25, 0.5, 0.75, 1.0}
- R1 认为 α_eff-binding 实际占比极低，方法退化为"ESS-only + clean batch 不干预"
- R2 注意论文 §3.3 报告 38.2% α_eff-binding，与 R1 的 ~0.2% 存在数量级差异，需作者澄清
- 无论具体数字，B=4 下离散化削弱了框架的理论优雅性，需 B≥16 验证

**W3. Epoch-matched 比较引入 LR schedule confound。** [R1-W3 critical, R2-W1 major → 交叉后 R1 升级、R2 AGREE]
- D&R epoch-matched 在 2,533/6,103 步时 cosine LR 仍处中段（~64% 峰值），非训练终态
- 论文以"if anything, favors D&R"论证，但 warmer LR 影响方向不确定
- Epoch confound 是论文最强贡献，其核心实验有 confound 直接动摇 foundation
- 需补充独立设计 2,533 步 cosine schedule 的对照实验

**W4. 新颖性不足以支撑 main conference。** [R2-N1, R1 AGREE]
- Epoch confound 是 ablation-level 发现，缺乏机制解释（为什么多 epoch 能替代 reweighting？）
- Adaptive b* 基于成熟统计工具（ESS, Kish 1965; calibration, Guo 2017）的 straightforward 组合
- Detector requirements（需要 calibration + discrimination）接近 expected
- 三个贡献叠加仍偏 incremental

**W5. 实验规模严重不足。** [R2-N2, R1 AGREE]
- 主要实验：Qwen3-0.6B, batch size 4, 132M tokens
- 1.7B 实验 OOD gains 消失（Wiki Δ=+0.013 方向不一致）
- Llama-3.2-3B cross-model transfer 结果 mixed/negative，且省略 PPL 比较
- τ=0.7 是否 scale-invariant 无证据
- 标题暗示一般性结论但 evidence 仅来自 0.6B

### Major

**W6. N=3 统计功效不足。** [R1-W4, R2 AGREE]
- df=2 下 p=0.025 可靠性有限
- Δ=−0.020 的微小效应需更多 seeds 或 bootstrap CI

**W7. Self-contamination 生态效度受限。** [R1-W5, R2-W2 共识]
- Generator = trainee 使 AUC=0.94 人为偏高
- Appendix N 的 cross-model 实验（单 seed、无 PPL）不足以证明泛化
- §8 有声明但不免除对 claim 可信度的影响

**W8. ρ=0.2 失败 + 1.7B 效果减弱限制实用范围。** [R1-W7, R2 AGREE]
- 方法仅在高污染率 (≥0.4) + 小模型 (≤0.6B 有效) + 高 AUC calibrated detector 交集下有效
- 实际 web 污染场景可能不在此交集内

**W9. Abstract/Introduction overclaim。** [R2-W3, R1 AGREE]
- "consistent improvements" 描述 0.11% PPL 过于乐观
- §7 "zero-tuning baseline that improves" 技术正确但 framing misleading
- 将单一实验设置的发现推广为 D&R 的普遍问题，缺范围限定

**W10. Grid search baseline 公平性。** [R1-W6, R2 PARTIALLY AGREE]
- 完整 9 点 grid 仅在 seed 42 做，b=0.3 是 seed 42 特定的
- R2 认为比较设计合理但 effect size 才是核心问题

**W11. Wang et al. (2026) 理论假设不匹配。** [R1-W8, R2 PARTIALLY AGREE]
- 该理论假设已知 α，本文用 α_eff（r=0.70, bias≈−0.03）近似
- R2 认为 loose motivation 在 empirical 论文中可接受；R1 认为不能直接迁移理论保证

### Minor

**W12.** Related Work 遗漏 Mindermann et al. (2022) "Prioritized Training"。[R2-W4, R1 AGREE]
**W13.** 术语不统一（"sharpening exponent" vs "exponent" vs "b"）。[R2-W5, R1 AGREE]
**W14.** "Minimum intervention" 缺乏与其他 b 选择策略的消融对比。[R1-W9, R2 AGREE]
**W15.** §3.3 constraint regime 占比数字与 Figure 2 视觉不完全一致。[R1-W10, R2 AGREE]
**W16.** Figure 1 shaded region 边界与文字描述不一致。[R1-W11, R2 AGREE]
**W17.** vehtari2024psis 年份需确认（OpenAlex 记录 2015 vs bib 2024）。[R2 引用审计]

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成共识 [AGREE]：

1. **Adaptive b* 的方法论贡献因 tiny effect size (Δ=−0.020) 和 B=4 退化而不成立**——论文的主要价值不在方法，而在分析
2. **实验规模过小（0.6B, 132M tokens, B=4）严重限制泛化性**——标题暗示一般性结论但 evidence base 狭窄
3. **LR schedule confound 是 epoch confound 分析的关键漏洞**——论文最强贡献的核心实验有未解决的 confound
4. **论文应重新定位为分析论文**——epoch confound observation 有独立价值，但方法贡献薄弱

---

## Reviewer Divergence

**评分差异 (R1: 2.5 vs R2: 3.0)：**
- R2 认为 epoch confound 发现有独立的 analytical 价值，足以支撑 Findings 接收
- R1 认为 LR confound 未解决（W3 为 critical）、B=4 退化是 soundness 问题，应降低 Soundness 评分
- R2 条件性维持 3.0：如果 rebuttal 中 LR confound 未被解决，会考虑下调至 2.5

**W2 具体数字分歧：**
- R1 声称 α_eff-binding 实际占比 ~0.2%
- R2 指出论文 §3.3 报告 38.2%，两者存在数量级差异
- 核心论点（B=4 下框架退化）双方一致，但需作者澄清具体数字

---

## Questions

Q1. [R1, R2] B≥16 下 α_eff-binding regime 占比是多少？dual-constraint 两个约束是否都有实质作用？
Q2. [R1, R2] 为 D&R epoch-matched 独立设计 2,533 步 cosine schedule 后，Δ=0.017 是否改变？
Q3. [R2] Epoch confound 的机制是什么？多 epoch 曝光为什么能替代 reweighting？
Q4. [R1] Seed 123/456 各自的 grid-best b 是多少？
Q5. [R1] Detector AUC 与方法有效性的定量关系？
Q6. [R2] Llama cross-model transfer 失败是否说明需要 per-model tuning，从而否定 "zero-tuning" 定位？

---

## Missing References

- **Mindermann et al. (2022)** "Prioritized Training on Points that are Learnable, Worth Learning, and Not Yet Learnt" — instance-level online data selection，与 provenance-based reweighting 形成有意义对比。[R2 提出, R1 AGREE]
- **vehtari2024psis** 年份需确认：OpenAlex 记录 2015，bib 写 2024（可能是 JMLR 正式发表年份 vs 原始 arXiv 年份）。[R2 引用审计]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目未启用 paperreview.ai）。

---

## Visual Layout Check（非评分项）

**状态**: ✅ 已完成

**Findings (3 warning, 4 info):**

| 严重度 | 位置 | 问题 |
|--------|------|------|
| ⚠️ warning | p1-6 | 前 6 页无任何 figure/table 视觉锚点，审稿人需读完 6 页纯文本才能看到第一个实验结果。建议在第 1-2 页加入概念图或核心结果摘要图 |
| ⚠️ warning | p7 | Table 1、Table 2、Figure 1 三个 display item 全部堆叠在同一页，视觉节奏严重不均。建议将部分 display item 前移至第 5-6 页 |
| ⚠️ warning | p1-8 | 8 页正文仅 4 个 display item（含 Algorithm 1），对实证论文偏少。Appendix 有 13 个 display item，部分关键结果（Figure 2 constraint regime、Figure 4 data retention curve）可提升到正文 |
| ℹ️ info | p7 | Figure 1 图内文字偏小（约正文 60-65%），可考虑改为 figure* 全宽 |
| ℹ️ info | p5 | Algorithm 1 是前 6 页唯一非文本元素，视觉断节作用有限 |
| ℹ️ info | p8 | Discussion + Conclusion + Limitations 起始段同页，密度高但排版合理 |
| ℹ️ info | p13-16 | Appendix 图表密度充足，格式规范 |

---

## Overall Assessment

**综合评分: 2.5–3.0 (Borderline Findings to Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 2/5 | 2.5/5 | 2/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 2.5 | 3.0 | **2.5–3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合判断：** 论文的核心价值在 epoch confound observation——揭示 D&R 的 96% PPL 优势来自多 epoch 曝光。这一发现有纠偏意义，但受 LR schedule confound 削弱（W3）。Adaptive b* 方法的效果过小（0.11% PPL, 下游为零），在 B=4 下框架退化，实验规模（0.6B）过小，三个贡献均偏 incremental。

**定位建议：** 重新定位为分析论文（以 epoch confound 为核心贡献），或补充 (a) 独立 LR schedule 的 epoch-matched 对照，(b) ≥3B 模型的规模验证，(c) B≥16 下 dual-constraint 的有效性验证。

**当前水平：** Borderline Findings — 如果 LR confound 在 rebuttal 中被充分解决，可支撑 Findings；否则 Borderline Findings。

---

## Detailed Comments

### §1 Introduction
- "consistent improvements" 需加范围限定（仅在 ρ≥0.4, ≤0.6B, calibrated detector 下验证）
- 标题 "When Does D&R Work?" 暗示一般性结论，但 evidence 仅覆盖一个模型家族、self-contamination

### §3 Method
- Dual-constraint 形式化清晰，但 B=4 下离散化问题需在正文讨论（而非仅在 Appendix 提及 r≈0.70）
- "minimum intervention" 设计选择缺乏与 "maximum intervention" (ESS-only) 之外的其他策略对比
- Wang et al. (2026) 理论引用应明确注明假设差异

### §4 Experiments
- Self-contamination 设计的局限应在实验部分而非仅在 Limitations 中讨论
- TF-IDF+LR detector 的选择理由（为什么不用更强的 neural detector）应更充分论证

### §5 Results
- Table 1 epoch-matched 比较需补充独立 LR schedule 对照
- Downstream 结果（无影响）应在正文（非仅 Appendix）明确讨论，避免读者形成过度乐观印象
- ρ=0.6 三 seed 结果更有说服力（p=0.004），建议强调此设置而非 ρ=0.4

### §6 Discussion
- "Practical guidance" 节需加更明确的使用条件限定
- Epoch confound 的机制解释缺失——为什么多 epoch 曝光能替代 reweighting？这是一个值得展开的分析方向

### §8 Limitations
- 充分但偏保守，可更直接地讨论 B=4 离散化和下游无效果

### 排版
- 正文 display item 过少（4 个 / 8 页），前 6 页无图表，审稿人体验差
- 建议将 Appendix 中的 Figure 2 (constraint regime) 和 Figure 4 (D&R dual curve) 提至正文