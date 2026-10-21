---
round: 2
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-23T09:16:34.481184+00:00
reviewer_ids: ['1', '2']
cross_response_reviewer_ids: ['1', '2']
force_resubmit: False
---

# 审稿报告 — Round 2 (Fresh Review)

**论文**: Sign Misattribution in Step-Independent Agent RL: Dual Mechanism Diagnosis and Episode-Level Fix
**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性, R2: 新颖性/完整性）+ 视觉审查 Agent

---

## Summary

本文诊断了多轮 agent RL 中 step-independent windowing 的两个结构性失败机制：(1) Policy Information Loss (M1)——截断上下文导致固定性能天花板；(2) Advantage Sign Misattribution (M2)——group normalization 下 advantage 符号反映 episode 结果而非局部动作质量，导致累积退化。在 p=12.5%, K=8 时，理论预测 binary reward 下 80.9% 梯度方向错误；penalty reward 下实测 52% credit agreement（≈随机）。通过 2×2 factorial 分离两个机制（实际为 3/4 cells，Cell C 未实现），展示 episode-level GRPO 解决两者。11-seed 评估显示 73% 避免 collapse 但仅 36% 实现统计显著 OOD 泛化。初步单 seed 8B（90.3% OOD）和 ScienceWorld 跨环境证据。

---

## Strengths

**S1. 问题定位精准且有实际影响**。Step-independent windowing 是 RAGEN 等框架的默认配置，广泛使用但缺乏理论审视。将训练崩溃追溯到信用分配结构缺陷（而非超参数问题）对从业者有直接指导价值。

**S2. 理论分析在假设范围内正确**。Proposition 2 的推导（P(correct|update) = p/[1-(1-p)^K]）逻辑清晰，数值验证一致。Figure 1 直观展示 sign error 随任务难度恶化的趋势。

**S3. 诚实透明的多 seed 报告**。11-seed 评估揭示 collapsed/stagnant/generalized 三类结果分布，未 cherry-pick 最好 seed。Appendix 提供 step-5 统一评估表作为 anti-cherry-picking defense。

**S4. Factorial 设计思路合理**。2×2 分离 observation scope 和 advantage granularity 的想法概念清晰，A→B→D 的 progression 叙事有效。

**S5. 实践指导明确**。Discussion 中 "use largest feasible h (h≥20); h≤10 collapses" 的建议对社区有直接可操作价值。

---

## Weaknesses

### Must-Fix（5 项，影响接收决定）

**MF1 [R1+R2 共识] 理论预测 80.9% vs 实验测量 52% 的差距在主文中处理不当**
- Abstract/Intro 将 80.9%（binary reward 理论值）和 52%（penalty reward 实测值）简单并列，给读者造成两者互相支持的印象，实际两者之间存在 28.9pp 差距。Gap 解释仅在 Appendix A.2（penalty-induced variance），主文无充分讨论。如果 penalty reward（实际系统常用）将 correct-sign rate 从 19.1% 提升到 52%，Proposition 2 的定量预测在实际系统下的指导意义需重新评估。
- **建议**：(a) 在主文 Section 3 或 4.4 显著讨论差异；(b) 推导 penalty reward 修正公式或跑纯 binary 实验验证理论预测；(c) 考虑将标题数字改为实验值。
- **Round 1 状态**：曾被标记并修复（加了并列呈现），但修复不充分，本轮两位 Reviewer 再次提出。

**MF2 [R1 提出, R2 共识] Eq.6 累积发散论证的 "comparable magnitude" 假设过强**
- Eq.6 假设 correct 和 incorrect gradient 量级相当，但 GRPO normalization 下成功 episode 的 advantage 量级系统性大于失败 episode（μ 较小时 r+−μ 远大于 0−μ）。一个大的 correct gradient 可能抵消多个小的 incorrect gradients，使 "monotonic divergence" 结论不成立。这从根本上影响论文的因果解释——sign misattribution 的实际影响可能从 "active divergence" 降级为 "noisy convergence"。
- **建议**：(a) 从实验日志提取 advantage 分布数据分析量级比；(b) 若无法证明量级可比，将 Eq.6 降级为 worst-case analysis。

**MF3 [R1+R2 共识] Factorial 设计不完整：Cell C 缺失 + 种子数不足**
- 2×2 factorial 实际只有 3/4 cells。Cell C（full context + step-level advantage）正是独立隔离 M2 的关键——没有它，M2 的证据来自 A→B 对比（同时改变了 advantage granularity），存在混淆变量。Cell C 的 6 次 KL 崩溃本身说明 step-level advantage 在 full context 下行为可能质性不同。每个 condition 仅 2 seeds，在论文自己发现的高 seed variability（27% collapse, 36% stagnate, 36% generalize）下统计功效严重不足。
- **建议**：(a) 尝试 gradient/advantage clipping 稳定 Cell C；(b) 增加 factorial seeds 至 5+；(c) 更显著讨论 Cell C 缺失对结论的具体影响。
- **Round 1 状态**：曾被标记并修复（加了 Cell C crash record），但核心问题（实验不完整）未解决。

**MF4 [R2 提出] 缺少与同期方法的实验对比**
- Introduction 声称 "GiGPO, GAGPO, Turn-PPO address symptoms but not the structural root cause: the windowing itself"，但无实验支撑。特别是 **HCAPO** (Tan et al., 2026, arXiv:2603.08754) 在 ALFWorld + Qwen2.5-7B 上报告比 GRPO 高 13.8%，使用 step-level credit assignment 但取得良好效果——直接挑战 "windowing itself is the problem" 的核心论点，且未被引用。
- **建议**：(a) 至少在 ALFWorld 上跑 Turn-PPO 或 HCAPO baseline；(b) 若无法实验对比，将强声明改为 hypothesis。
- **新发现**：Round 2 新增。

**MF5 [R2 提出, R1 部分共识] Episode-level "Fix" 的 seed 依赖严重 + 标题 overclaiming**
- 11 seeds 中仅 4 个 (36%) 达到 p<0.01 显著 OOD 泛化——使用论文推荐的 fix 有 64% 概率无法获得有意义改进。Abstract 说 "resolves both mechanisms" 但实际只在少数 seed 上 resolve。Title 中 "Fix" 暗示可靠解决方案，与实际 36% 成功率不匹配。Stagnant vs. generalized seeds 的差异完全没有诊断分析。
- **建议**：(a) Title/Abstract 中将 "Fix" qualify 为 "necessary condition"；(b) 分析 generalized vs stagnant seeds 早期 dynamics 差异；(c) 讨论 seed selection 策略。

### Should-Fix（7 项，影响评分但不一票否决）

**SF1 [R1] Definition 1 操作化存在逻辑循环**。Section 4.4 用 "成功 episode 中所有 valid action windows" 操作化 "locally correct"，恰好犯了论文所批评的错误——用 episode outcome 替代 local quality。建议讨论近似局限性。

**SF2 [R1] Window-size cliff 基于 single seed**。鉴于高 seed variability，"cliff" 措辞过强，建议改为 "preliminary observation" 或增加 3+ seeds 验证。Round 1 已加 caveat 但措辞仍不匹配。

**SF3 [R1] REINFORCE++ 仅 15 步，对比不公平**。REINFORCE++ 是 episode-level（不受 M2 影响），无 critic 收敛本来就慢。建议延长至 30-50 步或定位为 "initial comparison"。

**SF4 [R1] Table 1 报告标准不一致**。Cell A: best seed, Cell B: best checkpoint (step 5), Cell D: mean of two seeds——同表混用三种标准。建议统一。Round 1 改了 caption 但数据仍混用。

**SF5 [R1] 52.07% credit agreement 缺乏统计检验**。未报告样本量、binomial test p-value 和 95% CI。"与 50% 无异" 需统计证据支撑。

**SF6 [R1] SFT baseline 训练细节缺失**。2,546 demonstrations 来源（人工/GPT-4/rule-based）和 SFT 训练超参数均未提供。

**SF7 [R2] 5 篇重要相关工作遗漏**：HCAPO (arXiv:2603.08754), RC-GRPO (arXiv:2602.03025), iStar (arXiv:2509.19199), From Reasoning to Agentic survey (arXiv:2604.09459), EDGE-GRPO (arXiv:2507.21848)。

### Minor（5 项）

- **m1**: 术语不一致："step-independent" / "step-level windowing" / "window-level" 混用
- **m2**: Definition 1 "locally correct" vs Proposition 2 proof "locally good actions" 术语切换
- **m3**: Section 3 "effective learning rate 12.6%"——实算 0.656×0.191=12.5%，有微小 rounding inconsistency
- **m4**: ScienceWorld Section 4.7 中 baseline 30.1% vs restricting context "34.8% to 4.5%"——30.1% 和 34.8% 似为不同指标，未说明
- **m5**: Figure 3 和 Figure 4(b) 使用红/绿配色，对色盲读者不友好

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上达成共识 [AGREE]：

1. **80.9% vs 52% gap**（MF1）：理论与实验的差距在主文中处理不当，需要更显著的讨论
2. **Cell C 缺失**（MF3）：factorial 设计因此不完整，论文目前对此 gap 的讨论不够充分
3. **Single-seed 跨规模/跨环境证据**："preliminary" 标注已加但仍需更多 seeds
4. **Fix 无方法论新颖性**：episode-level GRPO 就是原始 GRPO 设计
5. **诊断贡献有价值**：问题 formalization 清晰，对社区有实际指导意义
6. **Overall 3.0 (Findings)**：适合 Findings 接收但不够 Conference

## Reviewer Divergence

两位 Reviewer 在以下方面有不同侧重（互补而非矛盾）：

| 维度 | R1 | R2 |
|------|----|----|
| Soundness | 2.5/5（更严格） | 3.5/5 |
| Excitement | 3.5/5 | 2.5/5（更严格） |
| 关注焦点 | 数学严谨性（Eq.6 假设、Definition 循环） | 竞争性对比（HCAPO 遗漏）和 framing |

R1 认为理论部分的严谨性问题（Eq.6 假设过强）比 R2 更严重（critical vs 未特别关注）。R2 认为缺少实验对比（HCAPO）比 R1 更严重（critical vs 未提及）。两者互补——方法论和定位均需改进。

---

## Questions（需要作者澄清）

1. Proposition 2 预测 binary 下 80.9% incorrect sign，实测 penalty 下 52% agreement。是否可在 penalty reward 下推导 closed-form P(correct|update)？如果 penalty 从 0 增大到 0.1，P(correct) 如何变化？
2. Eq.6 的 comparable magnitude 假设——实验日志中 successful vs failed episode 的平均 |Â| 比值是多少？
3. Cell C 的 KL 崩溃是否尝试过 gradient clipping per window / advantage clipping / PPO clipping？
4. Credit agreement 52.07% 的样本量和 binomial test p-value？
5. 4 个 generalized seeds 之间是否存在共同特征（初始 loss、早期 gradient norm）？可否设计 early stopping 策略？
6. HCAPO 在 ALFWorld+Qwen2.5-7B 上比 GRPO 高 13.8% 且用 step-level credit——是否意味着 step-level credit 在好的 assignment 策略下可行？核心论点需如何修正？
7. Episode-level vs h=2 的实际 wall-clock 时间比？O(T²) attention cost 是重要实际障碍。

---

## Missing References

1. **HCAPO** — Tan et al., 2026. "Hindsight Credit Assignment for Long-Horizon LLM Agents." arXiv:2603.08754. **[直接竞争——ALFWorld 实验，step-level credit 取得好效果]**
2. **RC-GRPO** — Feb 2026. arXiv:2602.03025. **[GRPO variance collapse, 与 M2 高度相关]**
3. **iStar** — Liu et al., 2025. arXiv:2509.19199. **[Implicit step rewards, WebShop SOTA]**
4. **"From Reasoning to Agentic" survey** — April 2026. arXiv:2604.09459. **[47 篇 credit assignment 综述，应 position]**
5. **EDGE-GRPO** — 2025. arXiv:2507.21848. **[Advantage collapse 直接相关]**

---

## External Review

**状态**：未配置。项目配置中未启用外部审稿（paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查 Agent 已完成（2 warning, 5 info，0 critical）。

**Warnings:**
- **Pages 1-3 无 display item**：首个 figure 在第 4 页。审稿人前 2 分钟只看到文字和公式，缺少视觉锚点。建议将 Figure 1（理论曲线）或概念架构图提前到 page 2。
- **Page 13 底部约 1/3 空白**：Table 5 下方，可调整 float 位置或上移 Figure 4/5 填充。

**Info:**
- Figure 3 和 Figure 4(b) 使用红/绿配色，对色盲读者不友好，建议改用 blue/orange 或 Okabe-Ito 色板
- Page 4 脚注 GitHub 链接 (RAGEN-AI/RAGEN)，若作者与 RAGEN 相关可能违反匿名规则
- Table 2 字号偏小但仍可读
- 附录末页内容约 60%，底部有空白（影响较小）

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 2.5 | 3.5 | 3.0 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 2.5 | 4.0 | 3.0 |
| Confidence | 4/5 | 4/5 | 4/5 |

**综合评价**：

本文提出了一个有价值的诊断——step-independent windowing 在多轮 agent RL 中引入结构性信用分配缺陷，将散见于多个工作的训练失败统一为两个可分离机制（information loss + sign misattribution）。问题 formalization 清晰，多 seed 报告诚实。

但论文存在多个影响接收级别的问题：(1) 理论核心数字 80.9% 与实验测量 52% 的差距在主文中处理不当；(2) Eq.6 累积发散论证依赖过强假设；(3) factorial 因 Cell C 缺失而不完整且种子数不足；(4) 缺少与 HCAPO 等直接竞争方法的实验对比；(5) "Fix" 仅 36% seed 泛化但标题/abstract overclaiming。

**建议**：适合 EMNLP 2026 Findings 接收。距 Conference 级别需要：(a) 补充与 HCAPO/Turn-PPO 的实验对比；(b) 解决 Eq.6 假设问题；(c) 增加 factorial seeds；(d) 更诚实地 qualify "Fix" 的可靠性。

---

## Detailed Comments（逐节）

### Abstract
- "theory predicts 80.9%...empirical measurement...yields a 52% credit agreement rate" 并列呈现两个实际上有 28.9pp 差距的数字，需要在首次出现时说明一个是 binary 理论值一个是 penalty 实测值
- "resolves both mechanisms" 过强——仅 36% seed 达到显著泛化

### Introduction
- P1: 清晰的问题引出，从 framework default 到 training instability 的叙事有效
- P2: "Concurrent methods...address symptoms but not the structural root cause" 缺乏实验支撑，HCAPO 在 ALFWorld 上的结果可能反驳此声明
- P3: "Our primary contribution is diagnostic" 定位合理
- Contribution 2: "preliminary cross-scale...evidence" 措辞已降级，但 abstract 中 "90.3% OOD" 仍给人强印象

### Method (Section 2)
- 2.1-2.3: 问题 formulation 和 dual mechanism 分析清晰
- 2.4: Episode-level training 描述准确——"not a new method, but the original GRPO design"
- 2.5: Cell C 描述需更显著讨论缺失的后果

### Theoretical Analysis (Section 3)
- Proposition 1, 2: 推导在 binary reward 假设下正确
- Eq.6: "comparable magnitude" 假设过强，需降级或提供实证支持
- "effective learning rate 12.6%"——应为 12.5%（rounding）
- Reward saturation 分析有价值

### Experiments (Section 4)
- 4.1 Setup: SFT baseline 缺训练细节（demonstration 来源、超参数）
- 4.2 Factorial: Cell C 缺失问题；2 seeds/condition 不足
- 4.3 Results: Table 1 报告标准不一致
- 4.4 Sign Verification: 52% credit agreement 需统计检验
- 4.5 Seed Variability: 诚实报告，但缺少 generalized vs stagnant seeds 的诊断分析
- 4.6 Cross-Scale: Single seed，abstract 呈现过强
- 4.7 Cross-Environment: 只有 Cell A collapse，缺 Cell D recovery；30.1% vs 34.8% 差异未说明

### Related Work (Section 5)
- 遗漏 5 篇重要相关工作（见 Missing References）
- 术语不一致需统一

### Discussion (Section 6)
- Practitioner guidance 有价值
- Seed-dependent transfer 的讨论诚实但缺深度

### Limitations
- 覆盖 3 个点（环境/规模局限、seed dependency、长 episode 限制），符合 EMNLP 要求
- 可补充 penalty reward 下理论适用性的局限