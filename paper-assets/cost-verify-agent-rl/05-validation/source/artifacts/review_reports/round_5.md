---
round: 5
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T08:55:10.915372+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 5 审稿报告：Sign Misattribution in Step-Independent Agent RL

**审稿模式**：Fresh（重新审稿）
**Reviewer 配置**：2 人（R1: 方法严谨性/理论-实验对齐 | R2: 新颖性/竞争力/完整性）
**圆桌轮数**：1 轮初审 + 交叉分享（达成收敛，无需第二轮）

---

## Summary

本文诊断了 multi-turn agent RL 中 step-independent windowing 的两个失败机制：(1) M1: Policy information loss——窗口截断上下文导致恒定性能天花板；(2) M2: Advantage sign misattribution——episode 级 reward 投射到窗口级 advantage 导致大量梯度方向错误。通过 ALFWorld 上 2×2 factorial 实验（实际为 3-of-4 partial factorial，Cell C 因 NaN 崩溃缺失）隔离两机制。Episode-level GRPO（完整轨迹作为单一 sample）修复两者，在 1.7B 上实现 17.2% OOD 成功率（vs 6.7% SFT baseline），但 11 seed 中仅 36% 达到统计显著 OOD 泛化。8B 单种子实验和 ScienceWorld 跨环境实验提供初步证据。

---

## Strengths

**S1. 严谨的理论框架（两位共识）**
Proposition 1（locally correct action 的 advantage sign 趋近 base success rate）和 Proposition 2（correct sign gradient 上界 ≤ p/[1-(1-p)^K]）提供 closed-form bounds，Figure 2 理论预测与实验定性吻合。在同期工作中，本文的形式化分析深度独特。

**S2. 精巧的 Factorial 实验设计（两位共识）**
2×2 factorial（step/episode context × step/episode advantage）正交分离 M1 和 M2 的方法论 clean。Cell A vs B 隔离 sign misattribution 的增量效应，Cell B vs D 隔离 information loss。这种 factorial approach 在 agent RL 分析文献中不常见。

**S3. 三种互补的 Sign Misattribution 验证指标（两位共识）**
Sign-episode correlation、credit agreement rate、P(correct|update) 从不同角度验证 M2，增强诊断可信度。Figure 4 在 binary vs penalty reward 下的对比清晰展示 sign-episode 的近乎确定性映射。

**S4. 诚实的结果报告（两位共识）**
论文未隐藏 36% 泛化率和种子不稳定性（Section 4.5, Table 2），在当前 agent RL 文献中值得肯定。Abstract 未 overclaim。

**S5. 全面的 Related Work 覆盖（两位共识）**
Section 5 讨论 15+ 同期方法（IRC/iStar、MC-GRPO、GAGPO、SWEET-RL、HCAPO、Turn-PPO、EDGE-GRPO、RC-GRPO、GiGPO 等），定位为 "diagnostic complement"。DAPO、VAPO、PRIME、Ahmadian et al. 2024 均有引用。

**S6. Figure 1 有效传达核心思想（两位共识）**
Step-independent windowing（M1+M2 叠加）与 episode-level training（M1+M2 修复）的可视化对比清晰直观。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [Critical | R2 提出, R1 同意 Critical] **缺乏与同期方法的任何直接实验对比**
- 论文在 Section 5 讨论 15+ 同期方法但实验中无一复现。唯一对比是 SFT 和 REINFORCE++。
- R1 和 R2 从不同角度达成共识——R2：无法评估 solution 竞争力；R1：无法验证 diagnostic 框架对同期方法的解释力（如 HCAPO 的 step-level credit 是否避免了 sign misattribution）。
- Discussion 中引用 HCAPO/GiGPO 的 ALFWorld 数据属于间接证据，不足以替代受控实验对比。
- **跨轮状态**：连续 4 轮（Round 2-5）未解决。从 Round 2 的 reframe 到 Round 3 的间接引用，始终未实际复现任何同期方法。
- **建议**：至少复现 1-2 个代表性方法（HCAPO 或 Turn-PPO），或用诊断框架对其进行预测性分析并用其公开结果验证。

**N2** [Critical | R1 提出, R2 同意] **理论（binary reward）vs 实验（ternary reward）gap 未充分桥接**
- Propositions 1-2 假设 binary reward r∈{0,1}，实验用 ternary reward r∈{-0.1, 0, 1}。理论预测 19.1% upper bound 与实测 52.07% credit agreement 的 discrepancy 仅有定性解释。
- R2 补充：discrepancy 方向（实测比理论更差）加强主论点，但削弱理论严谨性。
- **跨轮状态**：连续 5 轮（Round 1-5）未完全解决。Round 3 改为 ternary、三指标区分、binary 28% credit agreement 纳入，但缺乏 ternary 下的形式化上界推导。
- **建议**：(a) 推导 ternary reward 下的修正上界；(b) 或补充纯 binary reward 对照实验验证原理论。

**N3** [Critical/Major 分歧 | R1=Critical, R2=Major] **Cell C 缺失使 factorial 不完整**
- Cell C（full context + step-level advantage，隔离 M2 alone）因 NaN 崩溃缺失，打破 2×2 factorial 完整性。
- R1 立场（Critical）：factorial 是全文方法论核心，缺失一个 cell 使正交可加假设无法验证。NaN 本身暗示 M1-M2 可能存在非可加性交互。
- R2 立场（Major）：Cell A vs B 和 B vs D 对比仍有效，定性结论（两机制各自有害）不被摧毁，但应停止称 "factorial design"——实际是 incomplete factorial。
- **跨轮状态**：连续 5 轮（Round 1-5）。Discussion 中已添加非可加性交互段落，但未能实际运行 Cell C。
- **合并判定**：Critical 偏 Major。定性结论可从 A-B-D 三 cell 推断，但量化分解（M1 和 M2 各贡献多少）无法完成。论文应修正 "factorial" 措辞为 "partial factorial"。

**N4** [Critical/Major 分歧 | R2=Critical, R1=Major] **Solution 无新颖性——Episode-level GRPO 就是原版 GRPO**
- 论文承认 episode-level training "reverting to GRPO's original design"（Section 2.4）。"correction" 实质是回退到原始设计。
- R2 立场（Critical）：Long Paper 的 solution 完全无新颖性，贡献只能靠 diagnostic framing 支撑，但诊断框架自身有 N2/N3 的质量问题。
- R1 立场（Major）：diagnostic paper 有先例（"Are Sixteen Heads Really Better than One?" 等），Critical 应保留给方法论错误而非贡献幅度判断。但同意这是论文天花板——当 solution 无新颖性时 diagnostic 质量必须过硬。
- **合并判定**：Major 偏 Critical。此 issue 定义了论文的贡献上限（最高 Findings），但不构成 reject 理由。

### Should-Fix（影响评分但不一票否决）

**W1** [Major | 两位共识] **36% 种子泛化率限制实用价值，缺乏失败种子分析**
- 11 seeds 中仅 4 个 (36%) 达到统计显著 OOD 泛化。Appendix I 的 information diversity 分析样本量仅 n=11（4 vs 7），统计推断受限。
- R1 补充：诚实报告值得肯定，但论文从 36% 中抽取了过强结论。真正问题是 overclaiming 而非样本量。
- **建议**：(a) 增加种子数量；(b) 提供更详细的成功/失败种子结构性差异分析。

**W2** [Major | 两位共识] **Discussion/Conclusion overclaiming**
- Discussion（line 546-551）有 qualifier（"though experimentally verified only on GRPO"），但 Conclusion（line 586-588）写 "This finding applies to any method combining step-level windowing, sparse reward, and group-relative normalization" 无 qualifier。
- **建议**：Conclusion 中 "any method" → "GRPO-style group-relative methods" 或添加实验范围限定。

**W3** [Major | 两位共识] **ScienceWorld 仅验证 failure 未验证 fix**
- ScienceWorld 仅报告 Cell A 崩溃，未报告 Cell D（episode-level GRPO）结果。跨环境验证仅证明 "问题存在" 但不能证明 "fix 有效"。
- **跨轮状态**：Round 4-5 连续两轮。
- **建议**：补充至少 1 seed Cell D ScienceWorld 结果。

**W4** [Major | 两位共识] **Table 1 跨 condition 报告标准不一致**
- Cell A = best seed, Cell B = best checkpoint, Cell D = mean of 2 seeds。三种标准混用降低严谨度。
- **跨轮状态**：连续 5 轮（Round 1-5）。标注修复（caption 逐 condition 标注）不够——需统一底层数据报告标准。
- **建议**：所有 condition 统一为 mean ± std（或至少统一为 best checkpoint across seeds）。

**W5** [Major | 两位共识] **累积散度论证的 "comparable magnitude" 假设仅基于单一训练 snapshot**
- |Â_correct|/|Â_wrong| ≈ 1.32 来自 step 5 的单一快照。
- R2 补充：comparable magnitude 非核心 claim（即使 M2>>M1 factorial 仍有效），但若保留此表述需跨 training steps 验证。
- **跨轮状态**：连续 5 轮。Single-snapshot caveat 已添加但不够。
- **建议**：补充至少 3-5 个不同训练阶段 × 2-3 seeds 的测量，或删除 "comparable magnitude" 表述。

**W6** [Major | 两位共识] **h-sweep 基于 single seed**
- Figure 3(b) window-size sweep 基于单一种子，鉴于论文自身揭示的极端种子敏感性，threshold 发现需多种子验证。
- **跨轮状态**：连续 5 轮。
- **建议**：至少 3 seeds 验证 h=5→full threshold。

**W7** [Major | R1 提出, R2 同意] **Proposition 2 upper bound vs equality 措辞不一致**
- Proposition 2 给出 upper bound (≤) 但正文某些地方作 equality 使用。不改变结论方向但影响理论陈述精确性。

**W8** [Minor | 两位共识] **REINFORCE++ 作为 baseline 代表性不足**
- 仅训练 15 步，作为唯一 non-GRPO baseline 无法支撑 "standard remedies fail" 的 claim。
- **跨轮状态**：连续 5 轮。

### 格式问题

**F1** [Minor | 两位共识] **Conclusion 正文轻微溢出 page 9（约 4 行）**
- Section 7 Conclusion 约 4 行溢出到 page 9 左栏顶部，属 EMNLP 2026 8 页限制的技术性违规。Limitations 紧随其后不计入。
- **建议**：压缩 Related Work 或 Discussion 腾出空间。

---

## Questions to Authors

**Q1** [R2]: 4 个成功种子中 OOD 性能的方差有多大？性能是集中还是分散？

**Q2** [R2]: Table 2 中不同 K 值（5 vs 8）的实验是否支持 Proposition 2 关于 K 增大降低 sign error 的预测？

**Q3** [R2]: 如果改用 dense reward（per-step shaping），M2 是否真的消失？Figure 5 (Appendix D) 显示 dense reward shaping 也 collapse 到 0%，这似乎与理论预测矛盾。

**Q4** [R2]: 是否考虑过中间方案（overlapping/hierarchical windows）缓解 M1 同时修正 M2？

**Q5** [R1]: Cell C 的 NaN 崩溃是否在不同学习率/clip range 下均出现？具体尝试了哪 6 种超参数配置？

**Q6** [R1]: 论文的理论框架能否预测 VinePPO（tree-search credit assignment）的 step-level credit 是否也受 sign misattribution 影响？

---

## Missing References

**已确认引用**（Round 4 提出，Round 5 确认已在 Section 5 中）：
- DAPO (Yu et al., 2025) ✓
- VAPO (Yao et al., 2025) ✓
- PRIME (Cui et al., 2025) ✓
- Ahmadian et al. (2024) ✓

**仍缺失**（Round 5 新发现，两位共识）：
- **ArCHer** (Zhou et al., 2024) — hierarchical RL for multi-turn interaction，与 M1（information loss）替代方案直接相关
- **VinePPO** (Kazemnejad et al., 2024) — tree-search credit assignment，若其 step-level credit 避免 sign misattribution 则说明问题在组归一化而非 step-level 本身
- **Let's Verify Step by Step** (Lightman et al., 2023) — outcome vs process supervision 对比，与本文 episode vs step advantage 讨论直接相关（R1 建议）

---

## External Review

**状态**：未请求。本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：已完成（4 warning, 0 critical, 14 info）

主要发现：
1. [Warning] 前两页无 display item，Figure 1 直到第 3 页才出现，延迟审稿人认知锚定。建议提前至第 2 页。
2. [Warning] Figure 3 面板(a) 红/绿对比对色盲不友好。建议改用 Okabe-Ito 色板或增加 line style/marker 辅助。
3. [Warning] Figure 4 纯绿/纯红柱状图对色盲不友好。建议蓝/橙替代或添加填充纹理。
4. [Warning] Page 16 过度密集（Figure 6 + Figure 7 + Table 6 堆叠），Figure 7 尺寸偏小。建议分页。
5. [Info] 整体排版质量合格：公式渲染正确，无 overfull hbox，无 [?] 未解析引用，匿名合规，booktabs 风格规范。

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | **3/5** |
| Excitement | 3/5 | 2/5 | **2.5/5** |
| Reproducibility | — | 4/5 | **4/5** |
| Confidence | 4/5 | 4/5 | **4/5** |
| **Overall** | **3.0 (Findings)** | **2.5 (Borderline Findings)** | **3.0 (Findings)** |

### 合并评分理由

**Overall 3.0 (Findings)**，但处于 Findings 区间低端，距 2.5 仅一步之遥。

**支持 3.0 的论据**（R1 主导）：
- 双机制理论框架（Propositions 1-2 + factorial decomposition）在同期工作中的形式化深度独特
- Diagnostic paper 有独立学术价值——"知道该怎么做" 和 "理解为什么原来的做法错了" 是不同贡献
- Appendix A.3 的 6-factor meta-analysis（为什么社区默认 step-independent）在同期文献中未见
- 诚实报告（36% 泛化率、种子不稳定性）符合学术规范

**支持 2.5 的论据**（R2 主导）：
- Solution 完全无新颖性——episode-level GRPO = 原版 GRPO 回退
- 核心发现被 15+ 同期工作独立覆盖，增量知识贡献有限
- 缺乏同期方法的任何实验对比，无法评估 diagnostic 框架的实际价值
- 36% 种子泛化率严重限制实用价值

**关键分歧记录**：
- Solution 新颖性严重程度：R1=Major vs R2=Critical
- Cell C 缺失严重程度：R1=Critical vs R2=Major
- Excitement：R1=3/5 vs R2=2/5（核心分歧在于 diagnostic contribution 的权重）

**Rebuttal 可能改变评分的条件**：
- 补充 ternary reward 下的理论结果或纯 binary reward 对照实验 → 化解 N2
- 至少一个同期方法（HCAPO/Turn-PPO）的对比实验或预测性分析 → 化解 N1
- Cumulative divergence magnitude ratio 的多时间点测量 → 化解 W5
- 以上三项若完成，R1 可上调至 3.5，整体可能达 3.0-3.5

**无法通过 rebuttal 解决的问题**：
- Solution 无新颖性（N4）——这是论文定位问题，非修改可解
- Cell C NaN 崩溃（N3）——需额外实验且可能根本无法运行
- 种子泛化率 36%（W1）——需大量额外训练

---

## Reviewer 交叉回应摘要

### R1 对 R2 意见的回应
- [REBUT] N1 (Solution novelty): 降级为 Major。Diagnostic paper 有先例，但同意是论文天花板。
- [AGREE] N2 (No concurrent comparison): 同意 Critical，但理由不同——为验证 diagnostic 框架解释力而非评估 solution 优劣。
- [AGREE] W1 (36% seed rate): 同意。诚实报告值得肯定但 overclaiming 是真正问题。
- [AGREE] W2 (Overclaiming): 同意。"any" → "GRPO-style"。
- [REBUT] W3 (Experimental scale): 部分反驳。论文已有三维度验证，超出同领域多数论文。
- [AGREE] W4 (Page limit): 同意 Minor。约 4 行溢出。
- [AGREE] W5 (REINFORCE++ baseline): 同意。
- [AGREE] Missing refs: ArCHer + VinePPO + Lightman 2023。
- **维持 Overall 3.0, Excitement 3/5。**

### R2 对 R1 意见的回应
- [AGREE] C1 (Binary/ternary gap): 同意。遗漏的重要问题。方向加强主论点但削弱理论严谨性。
- [AGREE] C2 (Comparable magnitude): 同意但倾向 Major 非 Critical。核心 claim 是两机制各自独立存在，非幅度相当。
- [AGREE with nuance] C3 (Cell C NaN): 同意削弱但降级 Major。A-B-D 三 cell 仍支撑定性结论。应停止称 "factorial"。
- [AGREE] M1-M4: 全部同意。
- **维持 Overall 2.5, Excitement 2/5。**

---

## 跨轮持续问题（Round 1→5 仍 open）

以下问题已连续多轮被识别但始终未完全解决：
1. **Binary/ternary reward gap** (W2) — 5 轮
2. **h-sweep single seed** (W5) — 5 轮
3. **Cell C 缺失** (W8) — 5 轮
4. **REINFORCE++ 不公平** (W9) — 5 轮
5. **Comparable magnitude 单点测量** (W11) — 5 轮
6. **Table 1 报告标准不一致** (W12) — 5 轮
7. **缺乏同期方法实验对比** (R2-N1) — 4 轮