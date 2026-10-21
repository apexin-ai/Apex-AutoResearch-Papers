---
round: 3
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-23T16:30:52.013962+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Sign Misattribution in Step-Independent Agent RL

**Venue**: EMNLP 2026 (ARR)  
**Reviewers**: R1（方法严谨性 + 实验设计）, R2（新颖性 + 完整性 + 格式合规）  
**轮次**: Round 1（fresh review）  
**交叉回应**: 完成（R1↔R2 全部 W/Q 逐条回应）

---

## Summary

本文诊断了多轮 LLM agent RL 中 step-independent windowing 训练的一种结构性信用分配病理，由两种机制驱动：(1) 策略信息丢失（M1），窗口截断跨步上下文导致恒定性能天花板；(2) 优势符号错误归因（M2），episode 级二值奖励使多数梯度更新方向错误。理论分析推导出 binary reward 下仅 19.1% 梯度更新方向正确。2×2 factorial 实验在 ALFWorld 上隔离两种机制，episode-level GRPO 消除两种失败模式但仅 36% seeds 泛化。初步的 8B 和 ScienceWorld 单 seed 验证。

## Strengths

**S1. Factorial 实验设计有方法论价值。** 2×2 设计（trajectory scope × advantage granularity）超越 ad-hoc ablation，提供清晰的因果隔离框架。A→B 对比隔离 M2，B→D 对比隔离 M1，逻辑链条完整。[R1, R2 一致]

**S2. 可验证的理论预测。** Proposition 2 给出 binary reward 下 P(correct|update) = p/(1-(1-p)^K) 的闭式表达式，在 p=12.5%, K=8 时预测 19.1%，数学推导经验证正确。[R1, R2 一致]

**S3. 实验报告诚实度高。** 36% seed 泛化率、Cell C 训练不稳定、OOD 评估高方差（seed5 的 30pp range）、seed-dependent transfer 作为 open question——不利结果均被明确报告。11-seed 系统评估揭示了 episode-level GRPO 的真实高方差，为社区提供了诚实预期。[R1, R2 一致]

**S4. Related Work 覆盖全面。** 讨论了 15+ 同期方法（Turn-PPO, HCAPO, GAGPO, GiGPO, SWEET-RL, iStar, EDGE-GRPO, MC-GRPO, RC-GRPO, OAR, GRPO-λ, IRC, MT-GRPO, RAGEN-2, GRPO-Collapse），定位公平。[R2]

**S5. 可视化清晰有效。** Figure 1 的机制对比图直观；Figure 2 将理论预测可视化；训练动态图清楚展示了不同 Cell 的行为差异。[R2]

## Weaknesses

### Critical

**W-C1. 完全缺乏与同期方法的实验对比。** [R2-W2, R1 AGREE] Related Work 讨论了 15+ 方法但实验部分零对比。HCAPO 在同一 ALFWorld benchmark 上用 Qwen2.5-7B 取得 +13.8%。论文自称 "inform when finer-grained credit is safe"（Section 5）但无实验支撑这一声明。一篇定位于"诊断 + 指导"的论文，必须展示诊断如何指导实践——至少应与 HCAPO（同 benchmark）或 Turn-PPO（同问题）做实验对比，或用 M1/M2 框架分析其成功/失败条件。

**W-C2. Cell C 缺失破坏 factorial 因果推断。** [R1-W2, R2-W3, 一致 AGREE] Cell C（full trajectory + step-level advantage）本应隔离 M2 的独立效应。其训练不稳定性（6 次不同超参数均 NaN）不仅是缺失数据，更暗示 M1-M2 之间存在非加性交互效应——Cell C 出现与 Cell A 不同的失败模式（NaN instability vs gradual collapse），说明 M1 的 context truncation 可能有某种"稳定化"作用。论文的加性分离框架未能捕捉这一交互。Appendix D 仅报告现象未分析机制。

**W-C3. 理论（binary reward）与实验（penalty reward）脱节。** [R1-W3, R2 AGREE] Proposition 1/2 在 binary reward R∈{0, r₊} 下推导 19.1% correct sign rate。主实验使用含 -0.1 步罚的 penalty reward，实测 52%。19.1% vs 52% 的巨大差距仅以 "reflects the reward structure difference" 一笔带过，未提供 penalty reward 下的理论分析。核心量化预测在主实验设置下从未被直接验证。此外 Section 4.1 称 "Reward is binary" 与实际 reward 结构存在描述矛盾。

**W-C4. 主实验 factorial 对比仅 2 seeds。** [R2-W4, R1 AGREE] Table 1 核心因果隔离声明建立在 n=2 之上。11-seed 评估已显示 OOD 从 0% 到 38.7% 的巨大方差。Cell D 的 2 seeds 中一个 OOD 10.4%（低于 SFT baseline 12.56%），2-seed mean 恰好落在有利区间——再多一个不幸的 seed 就可能推翻结论。

### Major

**W-M1. Episode-level GRPO 无方法论新颖性。** [R2-W1, R1 AGREE] 论文明确承认 episode-level training "is GRPO's original design"。将回归原始算法包装为 Contribution 3（"Episode-level fix"）膨胀了贡献声明。R1 建议合并到 Contribution 2 作为 factorial 结论之一。

**W-M2. 双机制诊断形式化了已知问题。** [R2-W5, R1 partial REBUT] M1 本质是 partial observability，M2 是经典 credit assignment 在 GRPO 框架下的具体实例。多个同期工作（RAGEN-2, GRPO-Collapse, HCAPO, IRC, MC-GRPO）独立识别了类似问题。R1 认为 GRPO 特定的量化诊断（Proposition 2）有增量价值，但同意 novelty claim 应下调。**此为本报告唯一分歧点**：R2 认为新颖性不足（Excitement 2.5），R1 认为有增量价值（Excitement 3.5）。

**W-M3. Proposition 1/2 隐含假设与 Definition 1 矛盾。** [R1-W1, R2 AGREE] Proposition 1 将成功 episode 中所有窗口视为获得 correct sign，但 Definition 1 要求窗口在 oracle 下独立获得正 advantage。成功 episode 可包含次优窗口。19.1% 应标注为上界而非精确值。方向上强化了论文论点（真实值更低），但理论表述不够严谨。

**W-M4. 52% credit agreement rate 统计力弱且措辞过强。** [R1-W4, R2 AGREE] n≈3000 下 52% vs 50% 的 z≈2.19, p≈0.028 仅 marginal significance，但论文称 "confirms sign misattribution as the causal driver"。R2 补充：核心论证应是"52%≈50% 说明 advantage sign 几乎不携带 local quality 信息"而非"52% 显著高于 50%"，论文混淆了这两种论证。

**W-M5. Table 1 报告标准不一致。** [R1-W5, R2 AGREE] Cell A=best seed, Cell B=best checkpoint (step 5), Cell D=mean of 2 seeds。不一致虽不改变 D>B>A 排序但降低严谨度。

**W-M6. 8B 单 seed hedge 不充分。** [R1-W6, R2 partial REBUT] Abstract 中 "preliminary" 修饰充分，但 Introduction Contribution 3 中 "substantial OOD improvement at both 1.7B and 8B scales" 缺乏 "preliminary" 修饰。给定 1.7B 的 36% seed 泛化率，8B 单 seed 几乎无统计力。

**W-M7. REINFORCE++ 对比不公平。** [R1-W7, R2 AGREE] 仅 15 步训练不足以判定 REINFORCE++ 的能力。论文自己承认可能 insufficient 但仍用作佐证。

### Minor

**W-m1. Window-size sweep threshold claim 基于单 seed。** [R1-W8, R2 AGREE]

**W-m2. Eq.6 comparable magnitude 假设依赖单点测量（1.32）。** [R1-W9, R2 AGREE] 未报告多训练步/多 seed 的分布。

**W-m3. Definition 1 操作化与理论定义有 gap。** [R1-W10, R2 AGREE] 操作化（valid actions + episode success）是理论定义（oracle advantage）的宽松近似，gap 未量化。

**W-m4. Conclusion 泛化声明超出实验证据。** [R2-W6, R1 AGREE] "applies to any agent RL method" 远超 ALFWorld/ScienceWorld 实验范围。

**W-m5. 引用准确性问题。** [R2-W7, R1 AGREE] Turn-PPO arXiv ID 错误、MC-GRPO 标题错误、IRC 作者名拼写有误。

**W-m6. 潜在匿名性泄露。** [R2-W8, R1 AGREE] Page 5 脚注 1 代码链接可能违反 double-blind。

## Reviewer Consensus [AGREE]

两位 Reviewer 在以下关键问题上达成完全共识：

1. **Cell C 缺失是最严重的实验缺陷**，其不同于 Cell A 的失败模式暗示 M1-M2 非独立交互
2. **缺乏同期方法实验对比**严重限制了论文的 impact（Related Work 讨论 15+ 方法但零对比）
3. **理论-实验脱节**（binary reward 理论 vs penalty reward 实验，19.1% vs 52%）
4. **主实验 2-seed 统计力不足**，核心因果声明缺乏统计证据
5. **Episode-level GRPO 无方法论新颖性**，Contribution 3 应降级或合并
6. **论文核心价值在于诊断（Contributions 1-2），而非修正方案**

## Reviewer Divergence [REBUT]

**唯一分歧：诊断新颖性的程度**

- R2: M1/M2 是已知问题（partial observability + credit assignment）的重新 formalize，多个同期工作独立发现。**Excitement 2.5/5。**
- R1: 虽然个体概念已知，但 GRPO 特定的量化诊断（Proposition 2 的 19.1% + factorial 分离）有增量价值。**Excitement 3.5/5。**

此分歧不影响接收建议——双方均认为论文适合 Findings 而非主会议。

## Questions（需作者澄清）

**Q1.** Cell C 为什么出现 NaN instability 而非 Cell A 那样的 gradual collapse？是否暗示 M1 对 M2 有调节作用（moderation effect）？[R1, R2 一致]

**Q2.** 论文的理论框架预测存在 phase transition（p ≈ 39% 时 majority 梯度方向正确）。Step-independent training 是否只需更好的初始化（higher p at start）即可工作？[R2, R1 partial REBUT — 认为论文应补充此分析]

**Q3.** 36% 泛化 seeds 与 64% 停滞 seeds 有何可辨识的区别？是否分析了初始化特征或早期训练动态？[R1, R2 一致]

**Q4.** Cell D 的两个 seed 中 OOD 10.4% 的 seed 是否属于 stagnant？Table 1 报告 mean 是否 misleading？[R1, R2 一致]

**Q5.** "training duration does not explain the gap" 仅基于 seed100 的 n=1 观察。有更系统性的证据吗？[R1, R2 一致]

**Q6.** Binary reward 下 sign-episode correlation 100% 与 Proposition 2 的 19.1% correct sign 如何同时成立？（R2 已解释两者测量不同指标，但论文应明确区分。）[R1 提出, R2 REBUT 并解释]

**Q7.** Collapsed/Stagnant/Generalized 分类阈值（>50% drop, ≥3 consecutive steps, Fisher p<0.01）是否敏感？[R1]

**Q8.** 诊断框架能否预测 HCAPO 的成功条件？如果不能，"inform when finer-grained credit is safe" 的声明缺乏支撑。[R2, R1 AGREE]

## Missing References

- **Harutyunyan et al. (2019)**, "Hindsight Credit Assignment" (NeurIPS) — 与 M2 直接相关 [R2, R1 AGREE]
- **Arjona-Medina et al. (2019)**, "RUDDER: Return Decomposition for Delayed Rewards" (NeurIPS) — reward attribution 问题 [R2, R1 AGREE]
- **POMDP 文献** — M1 本质是 partial observability，缺少理论锚定 [R2]

## External Review (Stanford Agentic Reviewer)

**状态：未请求。** 项目未启用外部审稿。

## Visual Layout Check（非评分项）

**状态：已完成** (耗时 ~3 分钟)

| 严重度 | 位置 | 发现 |
|--------|------|------|
| Warning | Page 10 | 参考文献末页仅顶部 2 条条目（~5% 页面），其余 95% 空白。系 appendix 前 \clearpage 所致。 |
| Warning | Page 1-2 | 连续 2 页无 display item。Figure 1 直到第 3 页才出现，处于 3 页窗口边界。 |
| Info | Page 3 | Figure 1 使用红-绿色对（色盲不友好），建议换用蓝-橙或 Okabe-Ito 色板。 |
| Info | Page 6 | Figure 3 图例文字偏小，打印时可能难读。 |
| Info | Page 7 | Table 2 信息密度高（11 seeds × 多列 + 脚注），可读但略拥挤。 |
| Info | Page 15 | 附录末页底部有较大空白（优先级低）。 |

## Overall Assessment

### ARR 维度评分

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 3.5 | 2.5 | 3.0 |
| Reproducibility | 3.0 | 4.0 | 3.5 |

### Overall Score: **3.0 / 5 (Findings)**

### Confidence: **4 / 5**

### 总评

论文提出了一个有价值的诊断框架，将 step-independent agent RL 的训练失败分解为两种可分离机制（信息丢失 + 符号错误归因），理论分析在 binary reward 假设内正确，factorial 实验设计在方法论上有新意，11-seed 系统评估和诚实的局限报告值得肯定。

然而，四个结构性缺陷限制了论文对主会议的竞争力：(1) 完全缺乏与 15+ 同期方法的任何实验对比，削弱了诊断框架的实践指导价值；(2) Cell C 缺失破坏了 factorial 因果推断的完整性，且其不同于 Cell A 的失败模式暗示论文的加性分离框架可能不成立；(3) 理论仅覆盖 binary reward 但主实验使用 penalty reward，核心量化预测从未被直接验证；(4) 核心 factorial 对比仅 2 seeds，在已知高方差的条件下不构成统计证据。

此外，episode-level GRPO 作为"修正方案"是 GRPO 的原始设计而非新方法，且 36% seed 泛化率限制了其实用价值。诊断的新颖性存在争议——个体概念（partial observability, credit assignment）已知，但 GRPO 特定的量化分析有增量贡献。

**建议：Findings track 可接收。** 若目标为主会议接收，需补充：(a) 至少一个同期方法（如 HCAPO）的实验对比或 M1/M2 框架预测分析；(b) penalty reward 下的理论推导或 pure binary 实验验证；(c) factorial 核心条件增加到 ≥5 seeds。

## Detailed Comments

### Abstract (~155 words, ≤200 ✓)
"eliminates both failure modes" 措辞过强，与 Conclusion 的 "addresses" 不一致。Abstract 中 8B/ScienceWorld 的 "preliminary" 修饰充分。

### Introduction
三个贡献结构清晰。"Our primary contribution is diagnostic" 的自我定位与将 episode-level GRPO 列为独立 Contribution 3 之间存在张力。Introduction 中 "causes the majority of gradient updates for locally correct actions to carry incorrect sign" 隐含 80.9%（binary reward），但主实验 penalty reward 下仅 ~48%——"majority" 在实际实验条件下不成立。

### Method
POMDP 形式化标准正确。M1/M2 概念区分清晰。但 M1 本质是 partial observability，未与 POMDP 文献建立联系。Factorial 设计是实验骨架，Cell C 缺失在此已埋下因果推断隐患。

### Theoretical Analysis
Proposition 1/2 在 binary reward 假设内数学正确。P(correct|update) = p/(1-(1-p)^K) 推导可验证。但 (1) 隐含 "episode success ⟹ all windows locally correct" 假设与 Definition 1 矛盾，19.1% 应为上界；(2) Eq. 5 的 cumulative divergence 将 wrong-sign gradient 等同于 policy divergence，过度简化（忽略 KL constraint, learning rate 等因素）；(3) comparable magnitude 假设依赖单点测量。

### Experiments
Factorial 实验是最大亮点但 2-seed 是最大弱点。Window-size sweep 揭示 h=10-20 阈值暗示中间方案可能有效（larger/overlapping windows），但论文将问题呈现为二元。Section 4.4 sign verification 是强有力的经验证据，但 52% 的统计力弱。Cross-scale 和 cross-environment 标记为 preliminary 但增加了可信度。

### Related Work
覆盖全面，15+ 同期方法定位公平。"We diagnose why the default fails, informing when finer-grained credit is safe" 有吸引力但无实验支撑。缺失 Hindsight Credit Assignment (2019), RUDDER (2019), POMDP 文献。

### Discussion
M1-M2 vicious cycle 论述有洞察力但缺乏定量支撑。Practitioner guidance 简洁实用（"episode-level when feasible, h≥20 otherwise"）。

### Conclusion & Limitations
Conclusion 措辞适当（"addresses" 而非 "eliminates"），但 "applies to any agent RL method" 泛化过度。Limitations 涵盖 4-5 个要点，内容实质，位置正确（Conclusion 后 References 前），长度略超 EMNLP 建议的"一小段，3 个点"但可接受。

### 格式合规
| 项目 | 状态 |
|------|------|
| 正文 ≤8 页 | ✓ |
| Limitations 位置 | ✓ Conclusion 后 References 前 |
| 单一 Limitations | ✓ Appendix 无重复 |
| Abstract ≤200 words | ✓ ~155 words |
| Double-blind | ⚠ 脚注 1 代码链接存疑 |
| 引用格式 | ⚠ 部分引用有准确性问题 |
| 无 Anonymous 引用 | ✓ |
| 图表质量 | ✓ 清晰、位置合理 |
