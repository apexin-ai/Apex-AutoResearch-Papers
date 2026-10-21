---
round: 0
overall_score: weak reject
timestamp: 2026-05-17T00:40:43.138420+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 合并审稿报告 — Round 1 (Dream Review)

**论文**：Episode-Level RL for Multi-Turn Agents: Why Step-Independent Training Fails and How to Fix It
**日期**：2026-05-17
**Reviewers**：R1（方法+实验）3/6 Borderline Reject, R2（新颖性+相关工作）4/10 Reject

---

## Summary

论文识别了 multi-turn agent RL 训练中 step-independent reward assignment 的失败现象，提出 episode-level GRPO 作为替代方案。在 ALFWorld 和 ScienceWorld 上通过 h-sweep 和多 seed 实验验证了 episode-level 训练的优势（24.3% vs 0%）。跨环境和跨规模实验进一步验证泛化性。

---

## Strengths

1. **问题方向有价值**：Multi-turn agent RL 的 credit assignment 是实际且重要的瓶颈 [R1, R2 共识]
2. **h-sweep 实验范式有启发性**：通过 context window 大小扫描探测 credit assignment 行为是一个有信息量的实验设计 [R1, R2]
3. **实验覆盖面有意识**：跨环境（ALFWorld→ScienceWorld）、跨规模（1.7B→7B）验证 [R1, R2]
4. **结构紧凑**：8 页内完整呈现问题-方法-实验，无明显冗余 [R1]
5. **实用价值**：对使用 RAGEN/GRPO 训练 multi-turn agent 的研究者有直接指导意义 [R2]

---

## Weaknesses（按严重性排序）

### Critical（影响接收决定）

**C1. Eq.1 γ^(T-h) 理论框架与 GRPO 实际算法不匹配** [R1-N1, R2 AGREE]
- 标准 GRPO 使用 group-relative advantage A_i = (r_i - mean(r))/std(r)，不含显式 γ discount
- 论文将问题框架化为 γ^(T-h) → 0 指数衰减，但这对应 standard discounted policy gradient，非 GRPO
- 如果 Eq.1 只是类比而非推导，"credit assignment decay" 的"发现"不成立，论文核心理论贡献坍塌
- **必须明确**：step-independent training 的精确算法伪代码 + γ 在实现中的角色 + Eq.1 是推导还是类比

**C2. 核心新颖性不足** [R2-N1, R1 AGREE]
- Episode-level return 是 REINFORCE 的 default，非新方法
- γ^(T-h) decay 是 Sutton & Barto Ch.13 eligibility traces 的基础内容
- 实际贡献降级为"发现 RAGEN 框架在 multi-turn 场景下有 bug-like behavior 并用标准方法修复"
- R1 补充：如果论文能深入分析"为什么 LLM agent 社区默认走向 step-independent training"（context window 限制？token-level loss 惯性？框架设计偶然？），该分析本身可能构成更有价值的贡献

**C3. 统计 Power 全面不足** [R1-N2, R2 AGREE]
- 核心结果 24.3%±6.0% (3 seeds) → 95% CI = [9.4%, 39.2%]
- h-sweep (Table 1) 除 h=full 外全部 single seed
- Cross-env (Table 5) 和 model scale (Table 6) 疑似 single seed
- Step-independent baseline 0% 未经多 seed 验证（可能是 single unlucky run）
- Per-task r=-0.42 (n=6) 远未达统计显著 (critical value ~0.81, p≈0.41)

**C4. Baseline 比较严重不足** [R1-N3, R2 AGREE]
- 只对比两个极端：step-independent vs episode-level
- 缺少：GAE (λ=0.95)、γ=1 step-level GRPO、reward reshaping、hindsight credit assignment
- 无法判断 episode-level 是否为唯一方案或仅为"任何合理 credit assignment"的特例（即 GAE with λ=1, γ=1）

**C5. 相关工作严重不足（10 引用）** [R2-N2, R1 AGREE]
- 缺失：PPO、REINFORCE、GAE、HER (Andrychowicz 2017)、AgentQ（正文提及无引用条目）、WebAgent、AgentTuning、FireAct、Reflexion、Reward shaping (Ng 1999)、AgentBench、WebShop、InterCode
- 对于声称解决"credit assignment"问题的论文，不引用 GAE 和 reward shaping 经典文献不可接受

**C6. 与 Self-Guide 的性能差距未解释** [R2-N3, R1 AGREE with nuance]
- Self-Guide 用同样的 Qwen-1.7B 在 ALFWorld 达到 72.7%（本文 24.3%，差 3 倍）
- Discussion 中 "model capacity is separate bottleneck" 被 Self-Guide 直接反驳
- R1 补充：即使 Self-Guide 用了 expert demonstrations（不同 paradigm），论文仍必须正面回应——解释读者为何应关注 from-scratch RL 的 24.3%，以及何种场景下纯 RL 是唯一选择

### Warning（影响评分）

**W1. Overclaiming**："eliminates this bottleneck" 但只有 25% success [R2-W1, R1 AGREE]
- 叠加 CI [9%, 39%] 更严重——不仅 success rate 低，估计还极不确定
- 建议改为 "significantly alleviates" 或 "enables non-zero learning"

**W2. Contribution (1) 与 (3) 冗余** [R2-W2, R1 PARTIALLY AGREE]
- (3) h-sweep 是 (1) credit assignment decay 的实验验证，分列有凑数嫌疑
- R1 指出：如果增加 seeds 后 cliff 稳健存在，(3) 可独立为 "empirical characterization contribution"——前提是统计支撑到位

**W3. Future directions 暴露 stepping-stone 定位** [R2-W3, R1 AGREE]
- 列出大量"下一步应该做"的方向 = 告诉审稿人当前只完成最简方案

**W4. h-sweep cliff claim 不可靠** [R1-W1, R2 AGREE]
- Single seed + 6% noise band，cliff 可能是 artifact
- 需 h=3,4,5 各跑 3 seeds 验证

**W5. 跨环境/跨规模泛化 claim 基础薄弱** [R1-W2, R2 AGREE]
- 疑似 single seed，single-number 对比不构成"泛化"证据

**W6. Negative results 未报告** [R1-W5]
- Selective verification/reward ablation 等方向的失败经验有信息量
- NeurIPS 社区越来越欢迎 negative results reporting

**W7. 叙事转型痕迹可能残留** [R2-W4, R1 PARTIALLY AGREE]
- §4.5 Table 4 (Verification Value) 与当前"纯 training methodology"定位是否一致需审查

---

## Reviewer Consensus

两位 Reviewer 在所有关键问题上完全一致（R2 对 R1 全部 [AGREE]，R1 对 R2 全部 [AGREE]/[PARTIALLY AGREE]，无任何 [REBUT]）：

| 问题 | R1 | R2 | 交叉验证 |
|------|----|----|----------|
| Eq.1 理论严谨性 | N1 (critical) | AGREE + 加强 | 互补打击：技术+新颖性 |
| 新颖性不足 | AGREE + 补充 | N1 (critical) | 教科书内容 + 框架 bug 修复 |
| 统计 power 不足 | N2 (critical) | AGREE | CI [9%,39%] |
| 缺少标准 baseline | N3 (critical) | AGREE | GAE 既缺引用也缺实验 |
| 引用不足 | W4→AGREE | N2 (critical) | 10 vs 需要 30-50 |
| Self-Guide 差距 | AGREE with nuance | N3 (critical) | 需正面回应 |
| Overclaiming | AGREE | W1 | "eliminates" → "alleviates" |
| h-sweep single seed | W1 | AGREE | cliff 可能 artifact |
| Per-task correlation | W3 | AGREE | n=6, p≈0.41 |

---

## Reviewer Divergence

无实质性分歧。R1 对 R2-N3 (Self-Guide) 有 nuance（区分了 expert-guided vs from-scratch RL 两种场景），但结论一致：论文必须正面回应。R1 对 R2-W2 (Contribution 冗余) 持部分异议：认为如果 h-sweep 统计支撑到位，可独立成立——但当前 single seed 下确实不成立。

---

## Questions（需作者澄清）

1. "Step-independent training"的精确算法是什么？Reward 如何分配到每步？γ 的值是多少？请给出伪代码。
2. Eq.1 是从 GRPO 目标函数严格推导，还是对 standard discounted PG 的类比？
3. Step-independent baseline 的 0% 是在多少 seeds 上验证的？是 systematic failure 还是 single unlucky run？
4. Self-Guide 与本文方法的本质区别是什么（training paradigm? data requirement?）？为什么同模型性能差 3 倍？
5. 为什么不尝试 GAE (λ=0.95) 或 γ=1 作为中间 baseline？Episode-level GRPO 是否等价于 GAE(λ=1, γ=1)？
6. h-sweep 的 cliff boundary (h=3-5) 是否在 multi-seed 下仍然 sharp？
7. "为什么 LLM agent 社区默认走向 step-independent training 而传统 RL 不会？" 能否深入分析其 root cause？

---

## Missing References

**RL Foundations**:
- PPO (Schulman et al. 2017)
- REINFORCE (Williams 1992)
- GAE (Schulman et al. 2015/2016)

**Credit Assignment Classics**:
- Reward Shaping (Ng et al. 1999)
- HER (Andrychowicz et al. 2017)

**LLM Agent Training**:
- AgentQ (具体引用缺失)
- WebAgent (Gur et al. 2023)
- AgentTuning (Zeng et al. 2023)
- FireAct (Chen et al. 2023)
- Reflexion (Shinn et al. 2023)

**Agent Benchmarks**:
- AgentBench (Liu et al. 2023)
- WebShop (Yao et al. 2022)
- InterCode (Yang et al. 2023)

**RLHF**:
- Ouyang et al. 2022 / Ziegler et al. 2019

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求。

---

## Overall Assessment

**评分：Weak Reject**
**置信度：High（两位 Reviewer 完全一致，confidence 均 4/5，交叉回应零 REBUT）**

论文识别的问题方向有价值（multi-turn agent RL 的 credit assignment），但当前版本存在多个互相叠加的根本性缺陷：

1. **理论贡献不成立**：Eq.1 公式化与 GRPO 不匹配（R1）+ 即使正确也是教科书内容（R2）= 理论 contribution 归零
2. **实验贡献不可靠**：统计 power 全面不足，claims 的 CI 过宽，无法确认效果的稳健性
3. **对比不充分**：只比两个极端缺标准方法（GAE）+ 与 Self-Guide 的 3 倍性能差距未解释
4. **学术规范不足**：10 引用远低于顶会标准，核心相关工作完全缺失

**两位 Reviewer 共识建议**：
- 诚实重新定位贡献——不是"发现了新问题"而是"在 LLM agent RL 工程实践中验证了经典解决方案的有效性"
- 深入分析"为什么 LLM agent 社区默认采用 step-independent training"作为真正有价值的贡献
- 加入 GAE/γ=1 等标准 baseline 证明 episode-level 的独特价值
- 与 Self-Guide 做 head-to-head differentiation 或明确 paradigm 差异
- 所有关键实验增至 5-8 seeds
- 扩充引用至 30+ 篇
- 修改规模已超出 revision，建议 resubmission

---

## Detailed Comments

### §1 Introduction
- "eliminates this bottleneck" overclaims，改为 "alleviates" / "enables non-zero learning"
- Contribution (1) 和 (3) 建议合并（除非 h-sweep 获得多 seed 统计支撑）
- 需铺垫"为什么 LLM agent 社区默认 step-independent"的分析

### §2 Related Work
- 需增加至少两个 subsection：Credit Assignment in RL (GAE/eligibility traces/reward shaping) + LLM Agent Training (WebAgent/AgentTuning/FireAct/Reflexion)
- AgentQ 提及但无引用条目——引用错误
- HER 提及但无 Andrychowicz 2017 引用
- 需解释 episode-level GRPO 与 GAE(λ=1, γ=1) 的关系

### §3 Method
- Eq.1: 必须明确是推导还是类比；给出 step-independent 的完整算法伪代码
- Eq.2: γ^(T-h) decay analysis 需连接到 GRPO 的实际 advantage computation——如果 GRPO 无 γ，decay 来自何处？
- Eq.3: Episode-level GRPO 需与标准 REINFORCE 做差异化——否则"贡献"是"用了 REINFORCE"
- 如果 decay 来自其他机制（reward dilution? KL 累积? gradient variance?），需重新推导并更新叙事

### §4 Experiments
- Table 1: h-sweep cliff boundary (h=3,4,5) 需 ≥3 seeds 验证
- Table 2: 3 seeds → 5-8 seeds；step-independent 0% 也需多 seed 证明 systematic
- Table 3: Correlation 统计方法未说明（Pearson/Spearman? 样本量?）
- Table 4: verify vs no-verify +10pp 在 sd=6% noise 下需 significance test；§4.5 与"纯 training methodology"定位的一致性需审查
- Table 5-6: 需标注 seed 数量；generalization claims 需 ≥3 seeds
- Table 7: r=-0.42 (n=6) 不显著——删除 correlation claim 或增大样本量
- 整体缺少 GAE(λ=0.95)/γ=1 step-level/reward reshaping 中间 baseline
- 建议增加 "Negative Results" subsection 报告 selective verification 等失败方向

### §5 Discussion
- "Model capacity is separate bottleneck" 被 Self-Guide 反驳——需修改或删除，正面回应 performance gap
- 如果 Self-Guide 用了 expert data，需明确本文方法的优势场景（何时 expert demonstrations 不可得）
- Future directions 不应暗示当前工作是 stepping stone——强调独立价值
- 建议加入 negative results 简述

### References
- 10 → 至少 30-40，系统补充 RL foundations + credit assignment classics + agent training concurrent work + benchmarks