---
round: 7
overall_score: 3.0 - Findings
timestamp: 2026-05-18T12:47:57.971267+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 7 审稿报告（Continue 模式）— Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

**Venue**: EMNLP 2026 Main (ARR May 2026 cycle)
**Deadline**: 2026-05-25
**Reviewers**: R1 (方法严谨性+实验有效性), R2 (新颖性+相关工作+写作+完整性)
**轮次**: Round 7 (Continue from Round 6), 修订评估

---

## Summary of Changes Since Round 6

本轮有 20+ commits 的实质性修改，响应了 Round 6 报告中的绝大多数 issue：

1. **Compensation redundancy 实验**（C1 resolved）：KL+compensation 在 30%（2-seed, PPL 8.97±0.01 vs KL-only 8.96±0.03）和 50%（5 指标完全一致）均无效。新增 Appendix 证明 compensation 网络已收敛（step 700 plateau）。Claim 升级为 "renders compensation redundant at both tested sparsity levels"，有实验支撑。

2. **Multi-seed 大幅扩展**（W2 substantially improved）：Table 2 现有 30% KL global 3-seed（8.96±0.02）、50% KL MMLU 3-seed（28.1±0.2）、BCE 3-seed（28.13±0.20）。但 30% KL uniform PPL（8.82, 推荐配置）仍为单 seed。

3. **14B 跨规模验证**（新增）：Qwen-2.5-14B 数据（Table 8）。KL PPL 优势保持（7.62 vs TEAL 8.73），但 MMLU 低于 TEAL/BCE 8pp（63.7 vs 71.8%）。诚实报告为 "scale-dependent MMLU gap"。

4. **SNR 扩展分析**（W8 resolved）：从 80 步扩展至 300 步（7 checkpoints），加入 95% bootstrap CI。发现 non-monotonic trajectory（BCE mid-training > KL），是有信息量的新发现。

5. **OOD 30%**（W4 resolved）：C4 PPL 16.03±0.01（2-seed），推荐操作点 OOD 验证完成。

6. **Claim 校准**：near-orthogonal → weakly correlated; Iso-compute → Extended Training Analysis; Contribution 1 → "Empirical observation"; coupling 因果 → 相关性; cross-arch "consistent" → "preliminary evidence"。

7. **新增 appendix**：Extended SNR Analysis、Extended Downstream Evaluation（HellaSwag/PIQA/BoolQ）、Compensation Training Convergence。

---

## Round 6 Issue Disposition

### Resolved (10 issues)

| Issue | Round 6 状态 | 修复评估 |
|-------|-------------|---------|
| C1: Compensation claim 缺实验 | Critical | **Resolved**. KL+comp 实验完成, 两个 sparsity 均无效, 附 convergence 证据 |
| W3: Iso-compute 术语 | Warning | **Resolved**. 标题改名 + wall-clock 数据 |
| W4: OOD 仅 50% | Warning | **Resolved**. 30% C4 PPL 16.03±0.01 (2-seed) |
| W5: 三区域采样不足 | Warning | **Resolved**. 措辞弱化为 "qualitative behaviors at sampled levels" + caveat |
| W6: Missing refs | Warning | **Resolved**. SparseInfer + SVD-CSP 已补 (39 refs total) |
| W7: Mistral 缺 downstream | Warning | **Resolved**. Claim 弱化为 "preliminary evidence" |
| W8: SNR 统计 | Warning | **Resolved**. 300 steps + 95% CI + non-monotonic 发现 |
| W9: near-orthogonal | Warning | **Resolved**. weakly correlated ($R^2$=0.038) |
| W10: 28.5% 偏差 | Warning | **Resolved**. TEAL@28.5% 对比, <0.3 PPL 差异 |
| M4: Forward KL 论证分散 | Minor | **Resolved**. 交叉引用已加 |

### Partially Addressed (3 issues, 降级)

| Issue | Round 6 状态 | 本轮评估 | 新状态 |
|-------|-------------|---------|--------|
| C2: 技术新颖性有限 | Critical | Contribution 1 改为 "Empirical observation", MaskLLM 对比充分. 但方法本身（KL+Gumbel+Lagrangian 组合）未变. **定位修正到位, 核心局限不变.** | Warning (降级: framing 已改善) |
| C3: Coupling vs oracle confound | Critical | §4.2 明确承认 confound, Limitations 讨论, 语言改为 "correlates with" 而非 "causes". **但仍无实验分离.** | Warning (降级: 坦诚承认+语言校正) |
| W1: PPL-downstream disconnect | Warning | Abstract 更平衡, 30% 为推荐操作点. 但 14B 数据加剧此问题（KL PPL best 但 MMLU 输 8pp）. | Warning (持续) |

### Insufficient Progress (1 issue)

| Issue | Round 6 状态 | 本轮评估 |
|-------|-------------|---------|
| W2: Multi-seed 不完整 | Warning | 显著改善但推荐配置（30% uniform PPL 8.82）仍为单 seed |

---

## New Issues This Round

**R7-N1. [Warning] 14B MMLU 反转暴露 output-preservation 目标的根本局限**
- Table 8: KL PPL=7.62（best）但 MMLU=63.7% vs TEAL 71.8%（-8.1pp）。Uniform 仅恢复 +0.8pp。
- 这不是简单的 allocation 问题：KL 的 output-preservation 目标在更高 knowledge density 模型上系统性地 underweight task-specific features。
- 论文诚实报告（"gap appears intrinsic to KL's output-preservation objective"），但讨论过于简短。
- 8B 的 PPL-downstream disconnect（W1）在 14B 被放大为 PPL-MMLU 反转，构成对 KL distillation 方法论的根本质疑。
- **要求**：14B 段落应更深入讨论 output-preservation vs task-specific preservation 的 tradeoff。

**R7-W1. [Warning] Conclusion 过短**
- 仅 1 句话（"A <1% predictor with KL distillation halves TEAL's PPL across 7-14B; uniform allocation cuts cross-seed σ 7.5×."），缺 future directions 和 broader implications。
- 对于一篇完整论文，Conclusion 应至少 3-5 句：核心发现总结 + PPL-downstream disconnect 的反思 + 14B 发现的 implications + future work。

**R7-W2. [Info] `\enlargethispage{8\baselineskip}` 格式 hack**
- experiments.tex 第 253 行。8 行的扩展幅度较大。需确认未导致实际超页。

**R7-W3. [Info] Multi-seed 覆盖不一致**
- 推荐配置（30% KL uniform, PPL 8.82）是单 seed，而非推荐配置（30% KL global）反而有 3-seed。统计一致性有瑕疵。

---

## Strengths (本轮新增/强化)

**S1. Compensation redundancy 证据链完整**（本轮新增）
KL+compensation 实验 + convergence 证明 + 两个 sparsity level 交叉验证。这是本轮最重要的贡献：论文从 "未验证的 claim" 变为 "有实验支撑的发现"。

**S2. 14B 跨规模验证的诚实报告**（本轮新增）
多数论文会隐藏 mixed results；本文不仅报告 KL PPL 优势，还坦诚展示 MMLU gap 和 uniform 无法修复的事实。这增加了论文的可信度。

**S3. SNR 扩展分析发现 non-monotonic trajectory**（本轮新增）
BCE mid-training SNR > KL 是一个非 trivial 的发现，提供了新的 mechanistic insight。95% CI 增加了统计可信度。

**S4. 消融设计全面且有信息量**（持续）
Table 3 的 loss isolation 设计（特别是 BCE+Gumbel+Penalty=38.02 > vanilla BCE=27.97）仍然是论文最强的部分。

**S5. 写作质量良好**（持续）
无 AI 写作痕迹（grep 确认无 em-dash/en-dash）。Claims 校准到位（correlates, preliminary evidence, qualitative behaviors）。格式合规（8p main, [review] option, anonymous, Limitations/Ethics/Checklist）。

---

## Weaknesses (综合排序)

### Warning (影响评分但不一票否决)

**W1. 技术新颖性有限（持续 5 轮）**
- 核心方法是 Forward KL (Hinton 2015) + Gumbel-Sigmoid (Jang 2017) + Adaptive Penalty（标准约束优化）的组合。MaskLLM 已使用相同原则。
- 论文已正确重定位为 "empirical analysis / mechanistic understanding"，但 Contribution 1 的 gradient formalization 仍然是对 backpropagation 基本性质的重述。
- 影响：更适合 Findings 而非 Main Conference。

**W2. Coupling vs oracle confound 无实验分离（持续 5 轮）**
- BCE 使用 magnitude oracles，KL 直接优化 output distribution。观察到的差距可能源于 oracle quality 而非 gradient coupling。
- 论文现在坦诚承认（§4.2 + Limitations），语言校正为 "correlates with"。但 7 轮审稿仍未提供 KL-derived masks → BCE 的控制实验。
- 影响：gradient analysis（Contribution 1）的因果解释力被削弱。

**W3. PPL-downstream disconnect + 14B MMLU 反转（持续 5 轮 + 新加剧）**
- 8B: 50% downstream 崩溃；30% MMLU +2pp（温和）。
- 14B: KL PPL 最优但 MMLU 输 TEAL 8pp，uniform 仅 +0.8pp。
- 这不是 presentation 问题（叙事已大幅改善），而是方法论的 fundamental limitation：output-distribution preservation ≠ task-relevant preservation。14B 数据表明此 gap 随规模扩大。
- 影响：削弱 KL distillation 作为通用方法的 claim。

**W4. Multi-seed 覆盖仍不完整（持续 7 轮）**
- 推荐配置（30% KL uniform, PPL 8.82）仍为单 seed。Table 5 的 40% 行全部单 seed。
- 较 Round 6 有显著改善（Table 2 多数关键行已有 3-seed），但统计一致性仍有瑕疵。

**W5. Conclusion 过短**
- 1 句话的 Conclusion 不足以承载 14 页论文的 takeaway。审稿人可能认为草率。

---

## Questions (需作者回应)

**Q1.** 14B MMLU gap（KL 63.7 vs TEAL 71.8）的机制是什么？论文说 "intrinsic to output-preservation objective"，但 output preservation 和 task performance 之间的解耦为何在 14B 比 8B 更严重？是否与 Qwen-2.5-14B 的 knowledge density 或 SwiGLU gate distribution 有关？

**Q2.** 30% KL uniform（推荐配置）的 PPL 8.82 为何缺 multi-seed？如果这是最终推荐配置，单 seed 的可靠性如何保证？

**Q3.** BCE mid-training SNR > KL 的 non-monotonic 现象是否有更深层的解释？论文的 "KL coupling becomes effective after coarse mask learning" 假说是否可以通过 mask entropy trajectory 验证？

---

## Overall Assessment

**评分: 3.0/5 — Findings**
**置信度: High (4/5)**

### 与 Round 6 的评分变化

Round 6: 2.5 (Borderline Findings) → Round 7: 3.0 (Findings)

**提升 0.5 分的原因：**
1. Compensation redundancy 实验补齐了 Round 6 最大的 gap（C1），从 "未验证 claim" 变为 "有实验支撑的发现"
2. 14B 跨规模数据，虽然 mixed，但增加了论文的深度和诚实度
3. Multi-seed 覆盖大幅改善，Table 2 多数关键行有 3-seed
4. SNR 扩展分析（300 steps + 95% CI + non-monotonic 发现）提供了新的 mechanistic insight
5. Claims 校准全面到位，写作质量持续良好

**不升至 3.5 的原因：**
1. 技术新颖性有限——已有组件的直接组合，持续 5 轮未改变
2. Coupling vs oracle confound 无实验分离——7 轮审稿后仍仅有语言修正
3. 14B MMLU 反转加剧了 PPL-downstream disconnect，暗示 output-preservation 目标的 fundamental limitation
4. Multi-seed 覆盖仍有盲区（推荐配置单 seed）

### 定位建议

论文作为 **EMNLP 2026 Findings** 论文是合适的：
- **实验工作高于 Findings 平均水平**：消融设计全面（Table 3）、跨架构验证（LLaMA/Mistral/Qwen）、negative results 诚实报告、三区域分析有实用价值
- **方法论贡献不足 Main Conference**：技术为已有组件组合，理论分析是 backprop 基本性质的形式化
- **最有价值的贡献是 empirical insights**：compensation redundancy、PPL-downstream disconnect 的量化、allocation-dependent operating regions、14B scale-dependent effects

---

## Detailed Comments (逐节)

### Abstract
- 叙事较 Round 6 显著改善：以 30% 推荐操作点开头，14B + MMLU gap 诚实披露
- 仍有 ~6 个数字（139%, 18%, 7.5×, 49%, 7-14B），但每个服务于叙事，可接受
- "rendering post-hoc compensation redundant at both 30% and 50% sparsity" 现在有实验支撑

### Introduction
- Contribution 1 "Empirical observation and quantification" 比之前的 "Identification" 更准确
- Contribution 2 compensation redundancy claim 有实验支撑
- Contribution 3 "allocation-to-downstream interactions at 7-14B" 准确反映了 mixed results

### Method (§3)
- 数学表述正确
- §3.6 Gradient-Based Motivation：SNR 扩展分析（300 steps, non-monotonic trajectory）增加了信息量
- Taxonomy (Table 1) 作为组织框架有价值

### Experiments (§4)
- §4.2 Extended Training Analysis（改名 ✓）：wall-clock 对比 ✓；confound acknowledgment ✓
- §4.3 消融：Compensation Redundancy 段落是本轮最有价值的新增内容
- §4.4 Regime Analysis：措辞弱化到位
- §4.5 SPON：weakly correlated ✓
- §4.6 Cross-arch + 14B：Mistral preliminary evidence ✓；14B 诚实但讨论偏短
- Inference Efficiency + Training Stability 段落被削减/移入 appendix，正文更紧凑

### Conclusion
- 过短（1 句）。需要扩展。

### Limitations
- 全面：PPL as proxy、per-target training、14B MMLU gap、OOD coverage、coupling vs oracle confound、seed variance、no wall-clock speedup。
- 14B limitation 讨论比 §4.6 更深入（"output-preservation objective may underweight task-specific features at higher knowledge densities"），建议将这一讨论也整合到正文。

### Appendix
- 内容扎实且信息密度高
- 新增 SNR Extended、Extended Downstream、Compensation Convergence 三个 appendix，均有价值
- Extended Downstream (HellaSwag/PIQA/BoolQ) 提供了 30% 操作点的正面证据

### Format Compliance
- 14 页 PDF（8p main + appendix + refs + limitations/ethics）
- `[review]` option ✓, anonymous ✓, line numbers expected (需确认)
- `\enlargethispage{8\baselineskip}` 需要检查是否导致实际超页
- 39 references，接近 typical range

---

## Issue Tracker 同步

本轮 resolved 10 个 Round 6 issues，降级 3 个 Critical→Warning，新增 4 个 issues（1 Warning + 1 Warning + 2 Info）。

**跨轮持续未解决的核心问题：**
- 技术新颖性（R3-S1）：持续 5 轮，已从 Critical 降为 Warning
- Coupling vs oracle confound（R3-S2）：持续 5 轮，已从 Critical 降为 Warning
- PPL-downstream disconnect（R3-C2）：持续 5 轮，Warning
- Multi-seed 不完整（R1-W3）：持续 7 轮，in_progress

**新增 issues：**
- R7-N1: 14B MMLU 反转（Warning）
- R7-W1: Conclusion 过短（Warning）
- R7-W2: enlargethispage 格式（Info）
- R7-W3: Multi-seed 覆盖不一致（Info）