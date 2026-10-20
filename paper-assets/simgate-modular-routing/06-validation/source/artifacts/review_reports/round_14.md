---
round: 14
overall_score: 3.0 (Findings)
timestamp: 2026-05-17T15:32:48.567783+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 14 (Fresh Review)

**论文**: "Death Avoidance as the Dominant Routing Signal: A Counterfactual Analysis on ScienceWorld"
**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验充分性; R2: 新颖性+完整性+写作质量）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文提出 episode-level counterfactual 框架，用于诊断模块化 LLM agent 路由决策的驱动信号。在 ScienceWorld（11/30 task types, 245 episodes, Qwen2.5-7B-Instruct）上，发现 78.9% 的非平局路由标签来自 death asymmetry（penalty-independent），DAF 在 P=100 时达 90.4%。Router 训练实验表明 episode-level 路由无法超越 always-deterministic baseline。MATH 和 ALFWorld 提供跨环境 boundary condition 对比。

---

## Strengths

**S1. 研究问题重要且切中要害。** "what signal drives routing" 是 routing 研究的先决问题，现有工作几乎未系统回答。framing 为 "should we learn to route, or is it simpler than that?" 清晰有用。[R1-S1, R2 同意]

**S2. 方法论设计干净。** Algorithm 1 的 pure-strategy counterfactual 框架在方法论上 sound：相同初始条件、相同 seed、binary catastrophic outcome indicator。框架原则上可推广至任何具有可控 modality 对比和二元灾难性结果的环境。[R1-S2, R2-S2]

**S3. Penalty-independent finding 是真实的经验贡献。** 78.9% 的 death-asymmetry label fraction 不依赖于惩罚值 P，是经验量化的结果。Death rate differential (42.9% vs 16.3%) 的大小并非先验可知。[R1-S3]

**S4. 罕见的学术诚实。** 论文明确承认 DAF 是数学推导量、r=0.97 是代数后果、cluster bootstrap K=11 不满足推荐门槛、Llama pilot 仅 preliminary。这种自我批判在 ML 论文中少见。[R1-S4, R2-S1]

**S5. 有价值的负面结果。** Router 训练实验 (§3.6) 表明当 death avoidance 主导时，学习型 router 相对 always-deterministic 无优势。Oracle margin 仅 2.89 分 (-6.58 vs -9.47)，routing upside 本质极小。[R1-S5]

**S6. 统计分析严谨。** Bootstrap CI (B=10,000)、LOO robustness (Appendix D)、penalty sensitivity (Appendix G)、data scaling ablation (25%-800%, Appendix F)、anti-cherry-picking 论证 (Appendix C)、labeling quality audit (Appendix B)。[R2-S2]

**S7. 写作质量高。** 无 em-dash/en-dash 滥用，无 AI 写作标志词，过渡词节制，段落结构自然，专有名词首次出现均有定义。[R2-S4]

---

## Weaknesses

### Must-Fix

**W1. 单环境依赖严重限制泛化性。** [R1-W3 + R2-W2, Consensus]
所有核心定量结论基于 ScienceWorld 1 个环境、11/30 task types、1 个 backbone (Qwen2.5-7B-Instruct)。跨环境证据薄弱：
- MATH (N=795) 是 predicted null（p=0.81），设计上就不应有 routing signal，是最弱形式的验证
- ALFWorld (N=135) 的 "deterministic" modality 是提供 admissible actions（information asymmetry），与 ScienceWorld 的 ground-truth observations 本质不同，不构成同一框架的直接 replication
- Llama-3.1-8B pilot (N=70) 样本量过小
- 缺少第二个 catastrophic-failure 环境的 replication（论文自己提到 NetHack/Crafter 但无结果）
标题 "Death Avoidance as the Dominant Routing Signal" 暗示一般性，但证据仅支持 ScienceWorld-specific claim。

**W2. Figure 3 数据不一致。** [R2-W3, R1 AGREE with reservation]
Figure 3 (signal_reversal.pdf) 仅展示 ScienceWorld 和 MATH 两个环境，缺少 ALFWorld（Table 1 包含全部三环境）。更严重的是：Figure 中标注 MATH 为 N=300，但 §3.3 正文和 caption 报告 N=795。这是数据不一致，需立即澄清。

### Should-Fix

**W3. DAF framing 仍给 headline metric 过多权重。** [R1-W1 + R2-W1, Consensus with minor severity divergence]
DAF = δP/(δP + Δ_nd) 随 P 单调递增，90.4% 是 P=100 的代数后果（P=10 时仅 50.4%，P=1 时约 8.5%）。论文已采用 dual-metric 设计（Abstract 中 78.9% 在 DAF 之前），但 DAF 仍获得过多叙事权重。R1 列 Must-Fix，R2 降级为 Should-Fix（认为 dual-metric 已提供足够 qualification）。Director 判断：标题和 Introduction 应进一步以 78.9% 为主导。

**W4. 核心发现存在 obvious-in-hindsight triviality 风险。** [R2-W1, R1 AGREE with qualification, Divergence]
一旦知道 (a) death penalty = -100，(b) internal death rate 是 deterministic 的 2.6 倍，"death avoidance dominates" 是算术必然。R2 认为 78.9% 也近乎 trivial；R1 反驳说 δ=0.265 的大小是经验发现而非先验可知。Director 判断：death rate differential 的量化是真实贡献，但论文应更明确论证先验预期和经验 surprise（为什么 routing signal 来源多元是 prior assumption）。

**W5. Safe RL 引用严重不足。** [R1 partial + R2-W4, Consensus]
Safe RL 仅引 Garcia 2015 (survey) + CRPO 2021，共 2 篇。论文声称 "modality routing already functions as a safety mechanism"，这直接与 Safe RL 文献对话，但引用覆盖严重不足。.bib 中有 5 个 orphan entries (altman1999cmdp, achiam2017cpo, wang2023voyager, chen2023frugalgpt, zhou2024webarena) 未被引用。

**W6. LLM Agent Failure Mode 相关工作缺失。** [R2-W5, R1 AGREE]
Appendix I 分析了 failure modes（state hallucination）但 Related Work 中无 agent failure taxonomy 引用。

**W7. Router negative result 叙事定位不够清晰。** [R2-W6, R1 AGREE]
Router 失败存在两个竞争解释：(a) ground truth ≈ always-det (oracle 仅好 2.89 分)，(b) 27.7% step-level mislabeling。两者不互斥但论文未在正文中同时呈现。建议在 §3.6 强调 oracle margin 极小作为 primary 解释。

**W8. Abstract 数字过多。** [R2-W7, R1 AGREE]
约 190 词中含 12+ 数字（78.9%, 75/95, P=100, 90.4%, δ=0.265, r=0.97, 59.0%, 4B, N=795, p=0.81, N=135, N=70），审稿人难以在 30 秒内提取核心判断。建议精简至 3-4 个关键数字。

**W9. Selection bias from prescreening 11/30 task types。** [R1-W5, R2 AGREE with qualification]
排除的 19/30 task types（63%）可能系统性不同。Appendix C anti-cherry-picking 论证部分缓解（included vs excluded det death rate comparable），但未完全消除。特别是 30-step budget 限制可能过滤掉了需要更长 horizon 的、非 death-dominated 的 routing signal。

**W10. 1.7B non-monotonic dip 未解释。** [R1-W7, R2 AGREE]
1.7B episode-level balanced accuracy (43.1%) 低于 0.6B (50.7%)，跨 seed robust (41.7-44.4%)。论文的 speculation ("overfits to death-prediction correlation") 无实验支撑。

### Minor

**W11. Concurrent work 讨论过于压缩。** [R2-W8, R1 AGREE]
四篇 concurrent work (Zeng, Sun, Zhang, Wu, all 2026) 压缩在一句话中，应展开最相关的 1-2 篇。

**W12. Table 2 caption "Single seed" 需澄清。** [R2-M1, R1 AGREE]

**W13. Limitations section 组织松散。** [R2-M3]

**W14. Appendix F minority-class diversity caveat 应在正文 §3.6 提及。** [R2-M5, R1 AGREE]

**W15. Orphan bibliography entries。** [R1-W9, R2 confirmed]
5 个 .bib entries 未引用。应引用整合到 Related Work 或移除。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：

1. **单环境限制是最关键缺陷** — 无第二个 catastrophic-failure 环境的 replication [R1-W3, R2-W2]
2. **DAF framing 需要修正** — 78.9% 应为 primary metric [R1-W1, R2-W1]
3. **Safe RL + agent failure taxonomy 引用不足** [R1 partial, R2-W4, R2-W5]
4. **写作质量高** — 无 AI 写作痕迹 [R2-S4]
5. **负面结果报告诚实且有价值** [R1-S5, R2-S1]
6. **方法论 sound 但 straightforward** [R1-S2, R2-S2]

## Reviewer Divergence

**核心分歧：triviality 风险的严重程度**

- **R1 立场 (3.0 Findings)**：78.9% label fraction 是 "genuine empirical content"，δ=0.265 的大小并非先验可知。框架本身 (Algorithm 1) 是方法论贡献。论文的 self-awareness 不应被惩罚。
- **R2 立场 (2.5 Borderline Findings)**：即使 78.9% 也近乎 obvious-in-hindsight — 一旦知道 2.6x death rate differential，death-dominated labels 是直接推论。核心 finding 不应是环境设计的直接推论。Excitement 评分 2/5。

**Director 判决**：R1 的论证更有说服力 — death rate differential 的大小和方向是经验发现（ScienceWorld 的环境设计不保证 internal strategy 死亡率更高），且论文通过 find-non-living-thing 的反例（零死亡但仍有 routing signal）展示了 framework 的区分能力。However, R2 的 concern 不应被忽视：论文需要更明确地论证 prior expectation 和 empirical surprise。

---

## Questions

**Q1.** Figure 3 中 MATH 标注 N=300 但正文报 N=795，请澄清：这是论文版本间的数据不一致，还是 Figure 使用了 N=795 的子集？

**Q2.** 如果标题改为 "Death Avoidance as the Dominant Routing Signal in ScienceWorld: ..." 以 downscope generalization claim，是否会更准确反映证据强度？

**Q3.** Oracle margin 仅 2.89 分 (-6.58 vs -9.47)。这意味着即使有完美 router，routing 的理论 upside 极小。这一事实是否应作为 router negative result 的 primary explanation（而非 mislabeling 或 data scarcity）？

**Q4.** 对于 excluded 的 19/30 task types，如果将 step budget 从 30 增加到 50-100，是否有预期会出现 non-death routing signal？

**Q5.** 是否考虑过在 non-death episodes 上单独训练 router，以 disentangle label noise confound from structural limitation？

---

## Missing References

两位 Reviewer 共同建议补充的引用（已交叉确认）：

1. **Safe RL**: 补充 2023-2026 Safe RL 工作（当前仅 Garcia 2015 + CRPO 2021）
2. **Agent failure taxonomy**: Cemri et al. (NeurIPS 2025) "Why Do Multi-Agent LLM Systems Fail?"
3. **LLM routing**: Shnitzer et al. (2023); FrugalGPT (已在 .bib 未引用)
4. **Counterfactual NLP**: Kaushik et al. (2020)
5. **Orphan .bib entries**: altman1999cmdp, achiam2017cpo, wang2023voyager, chen2023frugalgpt, zhou2024webarena — 应引用或移除

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未启用 paperreview.ai）。

---

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分分布**: R1 = 3.0, R2 = 2.5. Director 综合判定 3.0。

**Soundness**: 3.5/5 — 方法论 sound（paired counterfactual comparison, bootstrap CI, 多维度 robustness），但 DAF 的 penalty-dependent 本质和单环境限制降低了结论的外部有效性。

**Novelty**: 2.5/5 — 框架本身 straightforward（paired comparison + decomposition），核心 finding 存在 trivial-in-hindsight 风险。但 death rate differential 的量化和 router negative result 的系统验证有增量价值。

**Significance**: 3.0/5 — 对 agent routing 研究有实际指导意义（在 catastrophic-failure 环境中先检查 death avoidance 再设计复杂 router），但影响范围受限于特定环境类型。

**Clarity**: 4.0/5 — 写作清晰诚实，统计报告完整，无 AI 写作痕迹。

**Confidence**: 4/5

**综合理由**：论文解决了一个重要的诊断性问题，框架设计干净，统计分析严谨，写作诚实。Penalty-independent 的 78.9% label fraction 是真实的经验贡献，router 的系统性负面结果对社区有参考价值。但三个因素阻止了更高评分：(1) 所有核心结论依赖单一环境，缺少第二个 catastrophic-failure 环境 replication；(2) 核心发现的 novelty 受限于 death rate differential 大小的经验观察，后续推导多为数学后果；(3) Figure 3 数据不一致需要立即修复。修正 framing（以 78.9% 为主导、downscope 泛化声明）和修复 Figure 3 后，论文达到 Findings 水平。增加 NetHack/Crafter replication 将显著增强论文至 Borderline Conference (3.5)。

---

## Detailed Comments

### Abstract
- 数字过多（12+），精简至 3-4 个核心数字
- DAF=90.4% 不应作为 headline，78.9% 更具信息量
- r=0.97 可移除（论文自己承认是代数后果）

### Introduction
- Contributions 列表结构完整，每条有 section 支撑
- 但应更明确论证为什么 routing signal 来源多元是 prior assumption（现有文献隐含假设什么？）
- "applicable to any environment" 的 generalization claim 应限定

### Method
- Algorithm 1 清晰可复用
- DAF decomposition 数学正确，但 penalty-dependent 本质需在 §2.4 开头更突出
- SCI 已合理降级到 Appendix

### Experiments
- §3.1 decomposition 结果扎实
- §3.2 Llama pilot 应明确标注为 anecdotal evidence
- §3.3 MATH negative control 清晰但应注明这是 weak validation
- §3.4 ALFWorld 的 modality 定义差异应在 section 开头而非中间讨论
- §3.5 baselines oracle degeneracy 是有力的 supporting evidence
- §3.6 应在正文讨论 oracle margin (2.89 分) 和 mislabeling (27.7%) 的竞争解释
- Figure 3: 修复 N 标注不一致，补充 ALFWorld

### Related Work
- Tool Use 和 Adaptive Computation paragraphs 充分
- Safe RL paragraph 严重不足（仅 2 篇）
- 缺少 agent failure taxonomy 讨论
- Concurrent work 讨论过于压缩

### Discussion
- "Why the router fails" paragraph 有用但可加强
- Scaling predictions 有价值但 speculative
- Framework applicability 应更明确列出限制条件

### Conclusion
- 简洁准确，无 overclaim

### Limitations
- 内容充分（27.7% mislabeling, step budget, backbone, cross-env, episode-level label granularity, distribution shift）
- 建议分段或加 paragraph headers 提高可读性

### Format Compliance
- 8 页正文 ✓
- ACL review 模板 ✓
- Double-blind 匿名 ✓
- Limitations section ✓
- Ethics Statement ✓
- 行号 ✓
- 5 个 orphan .bib entries 需清理