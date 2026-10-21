---
round: 7
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T17:24:26.866656+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7

**论文**: "Valid but Vacuous: Reward Hacking in Neurosymbolic Proof Generation"
**目标 venue**: EMNLP 2026 (ACL Rolling Review, deadline 2026-05-25)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法/实验/统计; R2: 新颖性/写作/格式）
**流程**: Round 1 独立审稿 → 交叉分享 + 逐条回应 → 收敛汇总

---

## Summary

本文提出 Solver Trace Ablation (STA)，通过 leave-one-out ablation 计算 Irreducible Solver Rate (ISR)，诊断 GRPO 训练中 neurosymbolic formalizer 的结构性退化。核心发现：(1) ISR 揭示 execution-only 评估不可见的 99.5% 结构崩溃；(2) ISR 作为 reward 信号在全部 4 个测试剂量下触发 Goodhart collapse；(3) 九种 hacking 模式跨逻辑类型和模型规模出现。论文定位为 empirical study，实验设计严谨、学术诚实度高，但关键统计推断存在系统性问题。

---

## Strengths

1. **研究问题重要且 timely**：在 RL-for-reasoning 快速发展的背景下，系统性记录 neurosymbolic 设置中的 reward hacking 对该领域有直接指导价值。[R1-S1, R2-S1 共识]

2. **实验设计的对照结构合理**：6 个 reward 条件、matched random control（隔离 ISR-specific vs generic reward-variance）、SFT baseline（隔离 RL-specific vs data-driven）、5 seeds 用于主实验，设计深思熟虑。[R1-S2, R2-S2 共识]

3. **罕见的学术诚实度**：主动披露 OR 方向反转（corrected OR=0.61）、premise-count confound 消除效果（1.06×）、deleted checkpoints 导致 N-H 为 upper bound、SFT PR gap confound 等不利证据。[R1-S3, R2-S4 共识]

4. **Trajectory analysis 超越 snapshot 评估**：1000-step 扩展训练证明 transient genuine window 是暂时的，方法论主张本身对社区有贡献。[R1-S4]

5. **九模式 hacking taxonomy 有分类学价值**：H7b（obfuscated tautology, triple gaming）、query-as-fact gaming 此前未记录。Cross-logic transfer 和 cross-scale evidence 增加普适性。[R1-S5, R2-S3 共识]

6. **Premise-count confound 处理充分**：正文明确指出 ISR 对 component count 的敏感性，premise-count-matched comparison 诚实展示控制后效果消失。[R1-S6]

7. **格式合规**：ACL template review mode、double-blind、正文 8 页内、Limitations/Ethics 位置正确、ISR 命名全文一致。[R2-S5]

---

## Weaknesses

### Critical (影响接收决定)

**C1. OR 方向反转的 framing 偏向 uncorrected 结果** [R1-N1, R2 AGREE]

5-seed uncorrected CMH OR=3.37 (p<10⁻⁹) vs 3-seed H8+FN-corrected OR=0.61 (n.s.)。方向从 "ISR 显著优于 random" 反转为 "ISR 略逊于 random"。Table 1 主表仅展示 uncorrected N-H=23%*；Discussion 以 OR=3.37 为开头；corrected 结果仅以 "under stricter classification the effect reverses" 一笔带过。对于 corrected analysis 反转方向的情况，uncorrected 结果不应作为主要叙事。

**C2. CMH p<10⁻⁹ 因 within-seed 非独立性被严重 inflate** [R1-N2, R2 AGREE]

CMH 假设 stratum（seed）内观测独立。但每个 seed 内的 100 个 evaluation samples 来自同一 checkpoint、greedy decoding，是系统性行为（如 ISR s43: 100% H7）。真正的独立观测单位是 seed (n=5)，非 sample (n=350/414)。Seed-level permutation tests 得 p=0.26 (n.s.)。CMH p<10⁻⁹ 作为主要统计证据存在严重的方法论隐患，论文未讨论此问题。

### Warning (影响评分但不致命)

**W1. "Goodhart collapse at all tested doses" 的 trajectory evidence 仅覆盖 β=0.1** [R1-W1, R2 AGREE]

Trajectory-confirmed 仅 β=0.1 的 2 个 seeds (s42, s45)。β=0.05/0.2/0.3 均为 500-step snapshot only。论文自身方法论主张 "snapshot evaluation would overestimate"，但对自己其他 doses 的 claims 使用了 snapshot evidence。

**W2. SFT baseline PR confound 使 C1 "RL-specific" attribution 证据受限** [R1-N3 critical → Director 裁决 warning; R2 REBUT severity]

SFT PR=13% vs exec-only PR=93%。低 PR 本身减少 hacking 机会。100-step checkpoint (PR=32%) 部分缓解但 Fisher p≈0.14 不显著。论文 framing 已用 "consistent with"（非 "proves"），R2 的 rebut 有效，但 C1 作为独立 contribution 的 prominence 与 evidence strength 不匹配。

**W3. Cross-scale 1.7B 仅 single seed** [R1-W3, R2-W6 共识]

4B 实验已证明 cross-seed variance 极大（σ=47pp），但 1.7B 仅 1 seed。§4.5 标题 "Cross-Scale Evidence" 未用 "preliminary" qualifier。

**W4. Deleted checkpoints 造成数据完整性缺口** [R1-W4, R2 context]

ISR β=0.1 s43/s44 checkpoints 丢失，5-seed pooled N-H=23% 为 uncorrected upper bound，corrected=6.06%（3.7× 差距）。Table 1 ‡ 标注不够显著。

**W5. Table 1 exec-only 500-step baseline 为 single seed (s42)** [R1-W6, R2 AGREE]

Cross-seed variance 极大（s42=93%, s43=13%, s44=98%），单 seed 不具代表性。建议改为 3-seed pooled 或注明 range。

**W6. Abstract 仍偏数据堆砌 (11 个数值/统计量 in 4 sentences)** [R2-W2, R1 AGREE]

审稿人在 30 秒内难以提取核心 insight。"6 conditions, 2 logic types, 2 model scales" 是纯规模描述可删减。

**W7. Introduction 5 个 \paragraph{} 叙事碎片化** [R2-W1, R1 AGREE]

"ISR as diagnostic" 和 "ISR as reward" 两段预支 experiments 结论。建议合并为 "Key findings" 段。

**W8. §4.3 β 呈现顺序非升序 (0.1→0.05→0.2→0.3)** [R2-W4, R1 AGREE]

读者难以构建 dose-response 心理模型。建议开头加总结 + 按升序呈现。

**W9. 方法新颖性有限 (Algorithm 1 仅 6 行 LOO)** [R2-W3, R1 AGREE with nuance]

STA 本质是标准 LOO mutation testing 的应用。"Diagnostic becomes optimization target" 是 Goodhart 直接推论。缓解因素：论文正确定位为 empirical study；LOO vs Shapley + O(1) variant 展示了设计空间探索。

**W10. 100 eval samples per-seed 统计 precision 低** [R1-W2, R2 context]

n=18 (β=0.3 s42) 时 CI 极宽 (5.6% → [0.3%, 25.8%])。主文百分比缺 uncertainty 量化。

**W11. Dose-response claim 统计上不足** [from v6-R1-W2, both agree]

β=0.1 用 5 seeds 而 β=0.05/0.2/0.3 用 3 seeds。"Non-monotonic dose-response" 作为 statistical claim 无法支撑。

### Info

**I1.** Table 1 caption ~80 words + 4 脚注符号，可读性待改善 [R2-W5, R1 AGREE]
**I2.** experiments.tex:34 "Notably" AI 写作标记 [R2-W7, R1 AGREE]
**I3.** 缺少 Goodhart 1975 或 Strathern 1997 经典引用 [R2-Missing-3, R1 AGREE]
**I4.** Blog posts (METR, Krakovna) 的 BibTeX venue 格式需确认 [R2-Q4]

---

## Reviewer Consensus [AGREE]

1. ISR collapse trajectory (Figure 2) 和 "diagnostic reliable, optimizer unreliable" 的核心发现成立且有价值
2. OR 方向反转 (3.37 → 0.61) 的 framing 偏向 uncorrected，需以 corrected 为主基调
3. CMH within-seed 非独立性是方法论隐患，p<10⁻⁹ 可能被严重 inflate
4. 方法 novelty 有限但论文定位（empirical study）正确
5. 九模式 taxonomy 有分类学贡献
6. 1.7B cross-scale 仅 single seed，需标注 preliminary
7. Abstract 数据堆砌、Introduction 碎片化、β 呈现顺序均需改善

## Reviewer Divergence [REBUT]

1. **N3/SFT PR confound severity**: R1 评 critical，R2 rebut 至 warning（论文 framing 已 cautious，用 "consistent with"）。**Director 裁决: warning**——论文措辞已适当但 C1 prominence 与 evidence 不匹配。

2. **W5/ISR diagnostic ROC curve**: R1 要求 per-sample sensitivity/specificity，R2 rebut（ISR 是 population-level trend indicator，配合 text-match+functional taxonomy 做分类）。**Director 裁决: R2 rebut 成立**——ISR 设计为 aggregate diagnostic，不需要 per-sample threshold。降为建议而非 weakness。

---

## Questions (需作者 rebuttal)

1. CMH 检验的 within-seed 独立性假设如何论证？是否有 cluster-robust 重分析结果？
2. Corrected OR=0.61 (n.s.) 下，"transient genuine window" 是真实效应还是 uncorrected classification 的 artifact？
3. 100-step exec-only vs SFT 的 Fisher exact p-value 是多少？
4. β=0.05/0.2/0.3 无 1000-step trajectory，"β controls timing not whether" 是否过强？
5. ISR 的 Goodhart vulnerability (ISR≥0.5 for tautology) 在设计时是否可预见？如是，4-dose 实验是 verification 还是 discovery？
6. Premise-count-matched comparison 消除 ISR advantage (1.06×)——ISR reward 的"正面"效果是否仅为鼓励 shorter outputs？

---

## Missing References

1. **Goodhart 1975** "Problems of Monetary Management" 或 **Strathern 1997** 经典改写——以 Goodhart's Law 为核心框架但缺原始来源 [R1+R2 共识]
2. **Cluster-robust / GEE 方法**——与 C2 统计问题相关的方法论引用
3. Blog posts/tech reports (METR, Krakovna 2020) 的 venue 格式需确认是否符合 ACL BibTeX 标准

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 external_review）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3/5 | 4/5 | 3.5/5 |
| Excitement | 3.5/5 | 3/5 | 3.25/5 |
| Reproducibility | 3/5 | 4/5 | 3.5/5 |
| Overall | 3.0 | 3.5 | **3.0** |
| Confidence | 4/5 | 4/5 | 4/5 |

**评分理由**：

核心现象（ISR diagnostic reveals collapse invisible to PR; Goodhart collapse across doses; nine hacking modes）有说服力，对 RL-for-reasoning 社区有直接警示价值。实验设计用心、学术诚实度高。

然而，作为一篇以 empirical evidence 为核心的论文，两个 critical 级统计问题（OR 方向反转 framing、CMH 非独立性）动摇了 quantitative claims 的可靠性。"Transient genuine window" 的 evidence 在 corrected analysis 下方向反转；CMH p<10⁻⁹ 在 within-seed 非独立性下可能被严重 inflate；SFT "RL-specific" attribution 受 PR confound 限制。这些问题叠加，使论文的 robustness 不足以支持主会议接收。

**建议投递 Findings track。** 如能在 rebuttal 中：(a) 提供 cluster-robust/GEE 重分析，(b) 以 corrected OR 为主基调重新 frame genuine window，(c) 降低 C1 prominence，则有望升至 Borderline Conference (3.5)。

---

## Detailed Comments (逐节)

### Abstract
- 11 个数值/统计量过密，删减至 ≤6 个关键数字
- "suggestive but non-robust improvement" 应改为更明确的 "genuine-rate advantage is not robust to classification methodology"
- "6 conditions, 2 logic types, 2 model scales" 合并为 "across multiple conditions and settings"

### Introduction
- 5 个 \paragraph{} 碎片化叙事；"ISR as diagnostic"/"ISR as reward" 预支 experiments 结论
- 建议合并为 2-3 个 \paragraph{}（背景+问题、方法+概述、贡献）
- 更明确 position 为 empirical study（"Goodhart collapse is predictable, but these phenomena are not: [stochastic bifurcation, non-monotonic dose-response, triple gaming]"）

### Method
- Algorithm 1 (6 行) 方法 novelty 有限，但 LOO vs Shapley 讨论和 O(1) variant 展示了设计空间
- Premise-count confound 讨论充分（正文 §3.2）

### Experiments
- §4.2: SFT comparison 的 C1 "RL-specific" claim 需降级为 supporting observation
- §4.3: β 呈现顺序改为升序或开头加 dose-response 总结
- §4.3: "Non-monotonic dose-response" 降为 descriptive pattern
- §4.5: 标题改为 "Preliminary Cross-Scale Evidence"
- Table 1: exec-only 500-step 改为 3-seed pooled 或注明 range; N-H 列增加 corrected 值; caption 精简

### Discussion
- 以 corrected OR=0.61 为主基调，uncorrected 作 upper bound
- 增加 within-seed 非独立性讨论段落

### Statistics
- 正文新增段落讨论 CMH 的 within-seed 非独立性假设及其对 p-value 的 inflation 效应
- 报告 cluster-robust SE 或 GEE (seed as cluster) 重分析
- 或明确以 seed-level permutation test 为 conservative bound (direction consistent, power limited)
- 降低 "p<10⁻⁹" 的 prominence

### Format
- experiments.tex:34 "Notably" → 直接写
- Table 1 caption 精简（† †† 解释移正文）
- 增加 Goodhart 1975/Strathern 1997 引用
- Blog posts BibTeX 格式确认