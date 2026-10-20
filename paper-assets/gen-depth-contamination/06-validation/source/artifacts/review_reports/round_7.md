---
round: 7
overall_score: 3.5 Borderline Conference
timestamp: 2026-05-18T14:51:01.975025+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 圆桌审稿汇总报告 — Round 7-Continue（修订评估）

**项目**: gen-depth-contamination
**论文**: Generational Depth Estimation of Recursive Synthetic Text
**目标 Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**审稿模式**: Continue（基于 Round 8 fresh review 的修订评估）
**Reviewer**: R1（方法/实验侧重）, R2（新颖性/完整性侧重）
**轮次**: Round 7C — 1 轮独立评估 + 1 轮交叉分享，达成收敛
**日期**: 2026-05-18

---

## Summary

本文提出 K*（discrimination boundary），度量递归合成文本中相邻代际保持统计可区分性的最大深度。使用 15 维统计特征 + OBD + LightGBM，在 9 个模型配置、3 个源域、4 种解码策略上系统刻画 K*。核心发现：Web 文本（C4）K*=2，Wikipedia K*=1，arXiv K*=3。下游 filtering 验证显示 binary filtering（与 K*=2 一致）表现与 graduated 方法相当。

本轮为修订评估：论文针对 Round 8 提出的 23 个 open/in_progress issues 进行了修改。两位 Reviewer 独立评估修订效果后交叉分享，1 轮即达成收敛。

---

## Strengths

1. **修订回应率高**：23 个待处理问题中 18 个完全解决（78%），体现对审稿反馈的认真回应
2. **论文定位大幅改善**：明确自我定位为 measurement framework（Discussion line 48: "The method combines established components; the contribution is the measurement framework and the empirical characterization it enables"），filtering 从独立 contribution 降级为 validation（Section 5 标题改为 "Downstream Filtering Validation"）
3. **θ=0.60 论证诚实化**：放弃过度包装的"三重独立证据"，改为 "data-driven operational threshold" + θ sensitivity analysis（Appendix K, Figure 7），K*=2 在 [0.575, 0.625] 稳定
4. **DPI 理论声明恰当软化**："guarantees" → "motivates"，正确定位为直觉动机而非严格证明
5. **关键缺失引用补齐**：Kirchenbauer et al. 2023（watermarking）, Penedo et al. 2024（FineWeb）, Gehrmann et al. 2019（GLTR），引用 34→37，核心缺口已填
6. **Appendix 实质性扩展**：LaTeX markup ablation（L）、power curve analysis（J）、feature group ablation（H）、zero-shot prompt template（I）、θ sensitivity figure（K）显著增强可复现性和实验深度
7. **Abstract 可读性提升**：数字密度降低约 40-50%，核心数字保留完整
8. **叙事一致性改善**：Abstract → Introduction（measurement 为主）→ Method → "Downstream Filtering Validation"（降级）→ Discussion（自我定位）→ Conclusion，主线连贯

---

## Weaknesses

### Must-Fix（1 个）

**W1. [Major] arXiv graduated filtering failure 与 Abstract "K* predicts curation granularity" claim 直接矛盾**
[共识：R2 发现，R1 交叉回应完全 AGREE 并承认自己漏检]

- Abstract (main.tex:39): "domain-appropriate K* correctly predicts optimal curation granularity"
- Discussion (line 30): "On arXiv (K*=3), graduated filtering similarly shows no improvement over unfiltered data"
- 这两个 claim 直接矛盾

核心问题：K*=2 预测 binary 最优是 trivial 的（仅两个可区分层级，graduated 无额外信息可用）。真正有预测力的测试应为 K*=3 → graduated 优于 binary，但实验否定了这一点。"K* predicts curation granularity" 在 non-trivial 条件下被证伪。Discussion 中 "discriminability rather than curation utility" 的 hedge 诚实，但 Abstract 未同步。

**修改方向**：Abstract 删除或弱化 "correctly predicts optimal curation granularity"。可选：(a) 限定为 "K*=2 correctly predicts binary filtering as optimal for web text"，(b) 重构为 "K* characterizes discriminability boundaries that inform but do not directly determine curation strategy"。

### Should-Fix（4 个）

**W2. [Minor] "Generator-independent" 术语残余问题**
[共识：R1 STILL_OPEN, R2 REBUT 具体引用但 AGREE 残余问题存在]

Contribution (c)（line 28）已加 "among continuation-mode generators" 限定，但 Abstract (main.tex:38) "Generator-independent statistical features" 和 Section 4.2 标题仍无 hedge。鉴于 Qwen-cont cross-scorer K* 2→1，未限定的 "generator-independent" 过强。

**修改方向**：Abstract → "largely generator-independent"；Section 4.2 标题加 qualifier。

**W3. [Minor→Moderate] "Structural complexity" / "lexical diversity" 术语混用且未独立测量**
[共识：R1 和 R2 独立发现，交叉分享中合并]

同一论文中 experiments_c1.tex:143 用 "structural complexity"，discussion.tex:40 用 "domain-level lexical diversity"。两个术语均未独立测量。Feature ablation 证明 vocabulary features 对分类器重要 ≠ 测量了域级 lexical diversity。

**修改方向**：(a) 统一术语，(b) Appendix 报告三域 type-token ratio 或 vocabulary entropy 验证排序与 K* 一致，(c) 承认 "correlation suggested by feature ablation, not independently measured"。

**W4. [Minor] Scorer claim 过强**
[共识：R1 发现 N3, R2 AGREE 并补充详细证据]

experiments_c1.tex:80 "K* is governed by the generation process rather than the scorer" 与以下事实矛盾：Qwen-cont K* 2→1，Qwen-7B arXiv K* 3→2（borderline），Wikipedia Qwen K* 2→1。

**修改方向**："K* is largely robust to scorer choice (8/9 configurations preserve K* under cross-scoring)"。

**W5. [Minor] OBD McNemar tests 报告不充分**
[共识：两位 AGREE]

Appendix G 报告 "all p&lt;0.01" 但缺实际 p 值。至少应报告最大 p 值。

### Noted（非阻塞，3 个）

**N1. Drayson et al. practical increment 仍偏薄**（FR7-W2, PARTIALLY RESOLVED）。Filtering 已降级为 validation，不再是 contribution 级问题。但如果 K*=3 graduated filtering 也失败，K* 对 curation 决策的 diagnostic 价值比论文 framing 更弱。

**N2. Mistral-7B K*=1 机制解释仍为投机性**（FR7-W4, STILL_OPEN partial）。Repeat-loop + BPE tokenizer 假说已添加但缺定量验证。可接受为 limitation。

**N3. 低 contamination ratio 下 net-beneficial 效应主文未提及**（FR7C-N3）。Appendix 已承认 10-50% 合成数据 net-beneficial，但主文 framing 侧重 contamination harms。一句话即可解决。

---

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键判断上完全一致：

1. **Overall score**: 3.0 → 3.5（Borderline Conference），评分上调幅度和理由一致
2. **最大改善**：论文定位清晰化（measurement framework, filtering 降级）
3. **最大剩余弱点**：arXiv graduated filtering 叙事矛盾（W1）
4. **θ 修订有效**：data-driven operational threshold 诚实且有充分支撑
5. **DPI 修订有效**："motivates" 正确定位
6. **引用缺口已填**：34→37，watermarking/GLTR/FineWeb 核心缺口补上
7. **Appendix 扩展实质性**：LaTeX ablation, power curve, feature ablation, prompt template, θ sensitivity 均有价值
8. **Excitement 不变（2.5）**：方法新颖性有限；arXiv graduated filtering failure 实际降低了 practical excitement

---

## Reviewer Divergence [REBUT]

**无实质性分歧。** 两处事实性纠正（不影响评估结论）：

1. **R1 声称 "新增 GPT-4o-mini 作为第三个 scorer"（FR7-W7 resolution）**：R2 全文 grep 验证，GPT-4o-mini 不出现在论文任何位置。实际新增为 arXiv cross-scorer with Pythia-1.4B。R1 事实性错误，但 RESOLVED 判定可能基于 arXiv 扩展仍然成立。
2. **R1 引用 "sole prior work addressing iterative contamination" 位于 Discussion line 48（R1-N1）**：R2 验证该文本不存在于论文中。Discussion line 48 为 self-positioning 句。Issue 取消。
3. **R1 引用 "generator-independent K* estimates" 位于 Introduction line 23（FR7-N1）**：R2 验证 line 23 为 "Our contributions:"。R1 的 broader concern（Abstract/Section 标题缺 hedge）有效但具体引用有误。

---

## Questions

1. 是否愿意在 Appendix 报告三个域的 type-token ratio 或 vocabulary entropy？这是一个简单计算，可以将 "lexical diversity governs K*" 从 post-hoc 解释提升为经验性支撑。
2. arXiv graduated filtering 结果本身是一个有趣的发现。与其用 hedge 隐藏，是否可以重构为正面发现："K* measures discriminability, which is necessary but not sufficient for curation benefit"？

---

## Missing References

本轮未发现新的缺失引用。37 篇引用对 empirical paper 可接受，但 camera-ready 建议补充至 40+。

---

## External Review (Stanford Agentic Reviewer)

项目未配置外部审稿。无外部结果。

---

## Overall Assessment

**评分：3.5 — Borderline Conference**（EMNLP 2026 ARR 评分标准）
**置信度：高**（两位 Reviewer 独立给出相同评分，交叉分享后共识度极高）

| 维度 | Round 8 | Round 7C | 理由 |
|------|---------|----------|------|
| Soundness | 3.5 | 4.0 | θ 论证修正 + DPI 软化 + LaTeX ablation + power curve，claims 与 evidence 更匹配 |
| Excitement | 2.5 | 2.5 | 问题新颖性不变；arXiv graduated filtering failure 降低 practical excitement |
| Reproducibility | 4.0 | 4.5 | Zero-shot prompt + feature ablation + power curve + θ sensitivity figure |
| Overall | 3.0 | 3.5 | 从 solid Findings 提升至 Borderline Conference |

**上调理由**：修订体现了对审稿反馈的认真回应。论文核心优势（跨模型/域/解码的 K* 系统性经验刻画）现在以恰当校准的 claims 呈现。诚实的自我定位（"measurement framework with established components"）解决了此前多轮中最顽固的 framing 问题。

**未达 4.0（Conference）的原因**：(1) 方法新颖性有限（现有组件的新组合），(2) practical utility 受限（K*=2→binary; K*=3→graduated 仍无优势），(3) 一个新 major 叙事矛盾（Abstract vs Discussion on curation granularity），(4) Excitement 2.5 反映该发现虽严谨但可能不足以引起主会议级别兴趣。

**建议**：Borderline Conference / strong Findings。若 W1（Abstract 叙事修正）和 W3（lexical diversity 测量）得到解决，论文可以更有信心地站稳 3.5，并有可能在 AC 重视系统性经验工作的情况下达到 4.0。当前状态下，Findings 接收有充分支撑；Conference 接收取决于 AC 对方法新颖性门槛的判断。

---

## Detailed Comments

### Issue Resolution 统计

| 类别 | Round 8 待处理 | Round 7C 已解决 | 仍 Open | 新增 |
|------|--------------|----------------|---------|------|
| Critical | 4 | 4 (100%) | 0 | 0 |
| Major | 6 | 5 (83%) | 1 partial | 1 new |
| Minor | 5 | 5 (100%) | 0 | 2 new |
| 其他 open | 8 | 4 | 4 partial | 0 |
| **合计** | **23** | **18 (78%)** | **5** | **3** |

最终剩余：8 个 issues（1 must-fix, 4 should-fix, 3 noted）

### 各 Section 逐节点评

**Abstract**: 大幅改善（数字精简，可读性好）。Must-fix: "correctly predicts optimal curation granularity" 与 arXiv 证据矛盾。Should-fix: "Generator-independent" 需 qualifier。

**Introduction**: Contribution list 有效重组。DPI "motivates" 正确。Minor: Contribution (c) 可以更清晰地区分 measurement 和 validation。

**Related Work**: 核心缺口已填（watermarking, GLTR, FineWeb）。37 篇引用可接受。Drayson 定位为 "special case when K*=1" 准确。

**Method**: θ 论证诚实且有充分支撑。OBD McNemar 需补充实际 p 值。

**Experiments (C1)**: "Domain as the sole dominant factor" 标题 vs 正文 "primary" 术语不一致。Scorer claim (line 80) 过强。

**Experiments (C3)**: 主文 framing 侧重 contamination harms，可一句话提及低 ratio 下 net-beneficial 效应。

**Discussion**: Self-positioning 优秀。"Discriminability rather than curation utility" insight 诚实但未反映在 Abstract。Lexical diversity 术语与 experiments_c1.tex 不统一。

**Limitations**: 全面（8 点）。Prompt-chain caveat（2/7）、Qwen balance（8）措辞得当。

**Appendix**: 新增内容显著加强论文。LaTeX ablation（L）有效回应 arXiv K*=3 格式退化质疑；power curve（J）支撑样本量合理性；feature ablation（H）增加实验深度。

### R1 事实性错误记录

本轮交叉分享中 R2 识别出 R1 的三处事实性引用错误：
1. GPT-4o-mini 作为 scorer：论文中不存在
2. "sole prior work" 文本：Discussion line 48 不含此表述
3. Introduction line 23 "generator-independent K* estimates"：该行为 "Our contributions:"

这些错误不影响 R1 的核心评估判断，但在引用论文具体内容时 R1 的准确性低于 R2。Director 在汇总时已基于 R2 的事实核查进行校正。