---
round: 6
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-24T23:19:06.229604+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 6 审稿报告：Sign Misattribution in Step-Independent Agent RL

**审稿模式**：Fresh（重新审稿）
**Reviewer 配置**：2 人（R1: 方法严谨性/理论-实验对齐 | R2: 新颖性/竞争力/完整性）
**圆桌轮数**：1 轮初审 + 交叉分享（达成收敛，无需第二轮）

---

## Summary

本文诊断 multi-turn agent RL 中 step-independent windowing 的两个失败机制：(1) M1: Policy information loss（窗口截断上下文导致性能天花板）；(2) M2: Advantage sign misattribution（episode 级 reward 投射到窗口级 advantage 导致梯度方向错误）。通过 ALFWorld 上 partial factorial 实验（3-of-4 cells，Cell C 因 NaN 崩溃缺失）隔离两机制。Episode-level GRPO 修复两者，在 1.7B 上实现 17.2% mean OOD 成功率（vs 6.7% SFT），但 11 seed 中仅 36% 达到统计显著 OOD 泛化。8B 和 ScienceWorld 提供单种子初步证据。

---

## Strengths

**S1. 形式化理论框架在同期工作中独特（两位共识）**
Proposition 1（locally correct action advantage sign 趋近 base success rate p）和 Proposition 2（correct sign gradient 上界 ≤ p/[1-(1-p)^K]）提供 closed-form bounds。在 15+ 同期 agent RL 方法论文中，本文的形式化分析深度独一无二。

**S2. Factorial 实验设计（两位共识）**
2×2 factorial（step/episode context × step/episode advantage）正交分离 M1 和 M2，方法论 clean。Cell A vs B 隔离 sign misattribution 增量效应，Cell B vs D 隔离 information loss。

**S3. 三种互补的 Sign Misattribution 验证指标（两位共识）**
Sign-episode correlation、credit agreement rate、P(correct|update) 从不同角度验证 M2。Figure 4 binary vs penalty reward 对比清晰展示 sign-episode 的近确定性映射。

**S4. 诚实的负面结果报告（两位共识）**
36% 泛化率、种子不稳定性（Section 5.5, Table 2）均如实报告，在当前 agent RL 文献中值得肯定。

**S5. 统一解释框架覆盖同期工作（两位共识）**
Section 5（Related Work）讨论 15+ 同期方法，以 M1/M2 框架解释其设计选择。"diagnostic complement" 定位清晰。

**S6. Figure 1 核心思想可视化有效（两位共识）**

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [Critical | 两位共识] **Cell C 缺失削弱因果推断，factorial 设计不完整**
- Cell C（full context + step-level advantage，隔离 M2 alone）因 NaN 崩溃缺失，2×2 factorial 缺一角。
- R1：框架应从"两个独立机制"降级为"两个共生机制"——NaN 崩溃暗示 M1-M2 非可加性交互。Section 5.2 承认 "the M1-M2 interaction may be non-additive"，Section 6 推测 "M1 may unintentionally stabilize training"。
- R2 补充：Appendix D 报告 6 次尝试涵盖 β∈{0.001, 0.01, 0.04} 和 lr∈{5×10⁻⁷, 10⁻⁶}，但未尝试论文自己在 Appendix D 末尾提到的 gradient clipping per window position——表明作者认识到可能路径但未执行。
- **跨轮状态**：连续 6 轮（Round 1-6）。
- **建议**：(a) 全文 "factorial" → "partial factorial / 3-of-4 factorial"；(b) 更深入讨论 NaN 崩溃对机制独立性假设的含义。

**N2** [Critical | R1 提出, R2 强烈同意] **Factorial cells 仅 2 seeds，统计效力不足**
- 论文自身用 11 seeds 展示三种截然不同的结果类型（27% collapsed, 36% stagnant, 36% generalized），直接证明 2 seeds 无法可靠代表任何条件的真实效果分布。
- Cell B（M1 only）OOD 5.97% 基于仅 2 seeds——若 Cell B 也存在类似 Cell D 的 seed variability，此数值可能仅反映碰巧的 stagnant 种子。Cell B 是 A→B→D 因果链的关键中间节点，其结果的可靠性直接影响论文的核心论证。
- **建议**：Cell B 增加到 5+ seeds（最低要求）。

### Should-Fix（影响评分但不一票否决）

**W1** [Major | 两位共识] **Binary 理论与 ternary 实验的桥接断裂**
- Propositions 1-2 假设 binary reward r∈{0,1}，实验用 ternary r∈{-0.1, 0, 1}。19.1% 理论上界 vs 52.1% 实测 credit agreement 仅有定性桥接（penalty introduces within-group variance）。
- R2 补充：Appendix A.2 的 "two calibers" 分析提供有用解释框架（19.1% = deterministic misattribution, 52.1% = near-random noise），两者均远低于有效学习水平，定性结论成立。但缺乏 ternary 形式化上界。
- **跨轮状态**：连续 6 轮（Round 1-6）。
- **建议**：推导 ternary corollary 或补充纯 binary 实验。

**W2** [Major | 两位共识] **Eq.6 magnitude ratio 仅有单点测量**
- |Â_correct|/|Â_wrong| ≈ 1.32 来自 step 5 的单一快照。论文自己承认 "whether this ratio holds across training stages remains to be verified"。
- **跨轮状态**：连续 6 轮。
- **建议**：至少在 step 1, 5, 10, 15 四个点测量。

**W3** [Major | 两位共识] **"addresses both failure modes" 措辞与 36% 泛化率不匹配**
- Abstract: "addresses both failure modes, yielding 17.2% mean OOD success"。机制层面确实消除了 M1 和 M2，但 36% 成功率表明消除这两个机制是 necessary but not sufficient。
- R1 建议更准确措辞："structurally eliminates both failure modes but remains seed-dependent"。R2 同意。
- **建议**：全文校准 "addresses"/"resolves" 相关表述，添加 seed-dependent qualifier。

**W4** [Major | 两位共识] **Single-seed 结果与论文自身展示的 seed variability 矛盾**
- 论文用 11 seeds 建立 seed variability 的重要性（Section 5.5），但 window size sweep（Section 5.3, 大部分 single-seed）、8B（Appendix C, single-seed）、ScienceWorld（Section 5.6, single-seed）均为单种子。方法论自相矛盾。
- **跨轮状态**：连续多轮。

**W5** [Major/Minor 分歧 | R1=Major, R2=Minor] **REINFORCE++ 对比作为 "standard remedies" 可能误导**
- R1：仅 15 步、唯一 non-GRPO baseline，不足以支撑 "standard remedies fail"。
- R2 REBUT：主文 Section 5.3 仅简要提及 "Appendix D"，详细结果和 caveats 在 Appendix D（"This is a preliminary comparison over 15 training steps; we cannot conclude..."）。caveats 已存在，严重程度降为 Minor。
- **合并判定**：Minor 偏 Major。主文 "standard remedies" 措辞应改为 "preliminary comparisons in Appendix D suggest..."。

**W6** [Major | R2 提出] **缺乏与同期方法的直接实验对比**
- 15+ 同期方法在 Related Work 讨论但实验零对比。Discussion 间接引用 HCAPO/GiGPO 公开数据不足以替代受控实验。Limitations 已声明但不充分。
- **跨轮状态**：连续 5 轮（Round 2-6）。

### Minor Issues

**M1** [Minor | 两位共识] **Definition 1 操作化存在代理偏差**
- 理论用 oracle advantage，经验用 action validity（非 invalid 即 valid）。包含形式正确但策略无用的 action（如重复搜索同一位置）。论文承认 "conservative" proxy，但未充分讨论代理引入的偏差。

**M2** [Minor | 两位共识] **Proposition 1 与 Proposition 2 关系需更明确阐述**
- Prop 1 建立 P(correct sign) → p 的渐近结果，Prop 2 给出有限 K 条件上界。两者关系（Prop 2 是 Prop 1 的有限样本细化）应在正文更明确阐述。

**M3** [Minor | 两位共识] **Table 2 seed100 出现两次**
- Table 2 caption 声明 "best checkpoint per seed"，但 seed100 有 step 5（11.19%）和 step 10（12.69%）两行。数据呈现不一致。

**M4** [Minor | 两位共识] **Footnote 5 等价性条件**
- "mild assumption that policy drift remains small during early training" 在训练后期不一定成立。鉴于分析聚焦训练早期（baseline p=12.5%），近似在目标场景下合理，但应更显式地限定适用范围。

**M5** [Minor | 两位共识] **"原始 GRPO" 表述不精确**
- "Episode-level GRPO (not a new method, but the original GRPO design)"——原始 GRPO（DeepSeekMath, Shao et al. 2024）是 single-turn 数学推理场景，从未在多轮 agent 场景使用。更准确表述："restoring GRPO's original per-sample granularity to the episode level"。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全达成共识（交叉回应中均为 [AGREE]）：
- **N1** Cell C 缺失 (Critical)
- **N2** 2 seeds 统计效力不足 (Critical)
- **W1** Binary/ternary 理论-实验 gap (Major)
- **W2** Eq.6 单点测量 (Major)
- **W3** "addresses both" 措辞 (Major)
- **W4** Single-seed 自相矛盾 (Major)
- **W6** 无同期方法对比 (Major)
- **M1-M5** 全部 Minor issues (Minor)
- **S1-S6** 全部 Strengths

## Reviewer Divergence

唯一分歧：
- **W5** REINFORCE++ 比较严重性：R1=Major vs R2=Minor。分歧仅在严重程度（Minor vs Major），实质问题一致。R2 认为 caveats 已在 Appendix 充分标注，主文仅简要提及。合并判定 Minor 偏 Major。

---

## Questions to Authors

**Q1** [R1]: Cell C 的 NaN 崩溃是否尝试过 gradient clipping per window position？论文在 Appendix D 末尾提到此方案但选择不追求——作为 scope 决定可理解，但削弱了 Cell C 分析完整性。

**Q2** [R2]: 4 个成功种子中 OOD 性能的方差有多大？性能集中还是分散？

**Q3** [R1]: 论文的理论框架能否预测 VinePPO（tree-search credit assignment）的 step-level credit 是否也受 sign misattribution 影响？若 VinePPO 避免了该问题，则说明 sign misattribution 源于组归一化而非 step-level granularity 本身。

**Q4** [两位]: "原始 GRPO" 的表述在技术上成立（每个 sample 一个 advantage），但原始设计是 single-turn 数学推理。将 episode-level multi-turn GRPO 等同于 "原始设计" 是否是过度简化？

**Q5** [R1]: 早期是否有指标可预测 Generalized vs Collapsed 种子？Appendix I 的 mutual information signal 虽有 Cohen's d=1.11 但 p=0.19，n=4/group 样本量不足。

---

## Missing References

**仍缺失（两位共识）：**
- **ArCHer** (Zhou et al., 2024) — hierarchical RL for multi-turn interaction，与 M1（information loss）替代方案直接相关
- **VinePPO** (Kazemnejad et al., 2024) — tree-search credit assignment，若其 step-level credit 避免 sign misattribution 则说明问题在组归一化而非 step-level 本身
- **Let's Verify Step by Step** (Lightman et al., 2023) — outcome vs process supervision 对比，与 episode vs step advantage 讨论直接相关

---

## External Review

**状态**：未请求。本轮未启用外部审稿。

---

## Visual Layout Check（非评分项）

**状态**：已完成（0 critical, 0 warning, 6 info）

主要发现：
1. [Info] 首页无 display item，Figure 1 在 page 2 顶部出现——可接受但非最优，若能提至 page 1 右栏底部可强化审稿人第一印象
2. [Info] Page 4 无 display item（理论分析：Proposition 1 + 证明草案），因含数学推导故可接受
3. [Info] Figure 3 图例/轴标签字号接近可读下限（约正文 70%），建议适当增大
4. [Info] Table 2 含 11 行种子级数据，信息密度高，字号略小但可读
5. [Info] Pages 11-12 连续纯文本（数学证明），如有空间可考虑汇总表打破视觉单调
6. [Info] Figure 6 柱状图标签字号偏小，建议 ≥9pt

本轮视觉审查整体排版质量合格，无需修改。

---

## Overall Assessment

### 评分

| 维度 | R1 | R2 | 合并 |
|------|----|----|------|
| Soundness | 3.5/5 | 3/5 | **3/5** |
| Excitement | 3/5 | 2.5/5 | **2.5/5** |
| Confidence | 4/5 | 4/5 | **4/5** |
| **Overall** | **3.5 (Borderline Conference)** | **3.0 (Findings)** | **3.0 (Findings)** |

### 合并评分理由

**Overall 3.0 (Findings)**。

**相对 Round 5 的变化**：R1 从 3.0→3.5，R2 从 2.5→3.0。两位 Reviewer 均上调 0.5，反映论文在措辞校准、格式合规和叙事清晰度方面的改进。但核心实验和理论问题在 6 轮审稿中始终未根本解决。

**支持 Findings (3.0) 的论据**：
- 双机制理论框架（Propositions 1-2 + factorial decomposition）在同期工作中的形式化深度独特，具有独立学术价值
- Factorial 设计理念 clean，即使实际执行不完整（3-of-4 cells）
- 三种 sign misattribution 验证指标增强诊断可信度
- 诚实报告种子不稳定性符合学术规范
- Related Work 覆盖全面，"diagnostic complement" 定位恰当

**阻止 Borderline Conference (3.5) 的论据**：
- Solution 完全无新颖性——episode-level GRPO = 原版 GRPO 设计回退（W6 天花板）
- Cell C 缺失使 factorial 不完整，且 NaN 崩溃暗示 M1-M2 非可加性交互未被充分讨论（N1，连续 6 轮）
- 仅 2 seeds 的 factorial cells 在论文自身 11-seed variability 证据面前统计效力不足（N2）
- Binary 理论与 ternary 实验的桥接始终仅为定性（W1，连续 6 轮）
- 缺乏同期方法的任何实验对比（W6，连续 5 轮）

**Rebuttal 可改变评分的条件**：
- Cell B 增加到 5+ seeds，验证 OOD 5.97% 可靠性 → 部分化解 N2
- Binary reward 纯对照实验或 ternary corollary 推导 → 化解 W1
- Eq.6 magnitude ratio 多时间点测量 → 化解 W2
- 主文措辞全面校准（partial factorial、preliminary comparison、seed-dependent qualifier）→ 积累可信度
- 以上组合可能将评分推至 3.0-3.5 区间

**无法通过 rebuttal 解决的结构性问题**：
- Solution 无新颖性——论文定位决定的天花板
- Cell C NaN 崩溃——可能根本无法运行
- 缺乏同期方法完整复现——需大量额外实验和 GPU 时间

---

## Reviewer 交叉回应摘要

### R2 对 R1 意见的回应
- [AGREE] N1 (Cell C 缺失): 同意 Critical。补充 Appendix D 未尝试 gradient clipping per window position。
- [AGREE] N2 (2 seeds): 强烈同意。Cell B 是因果链关键节点，需 5+ seeds。
- [AGREE] W1 (Binary/ternary gap): 同意。"two calibers" 分析提供定性框架但缺形式化。
- [AGREE] W2 (Eq.6 单点): 同意。建议 step 1, 5, 10, 15 四点。
- [AGREE] W3 ("addresses both" 措辞): 同意 R1 建议的更准确表述。
- [AGREE] W4 (Single-seed 矛盾): 同意。与自己 W2/W6 相同问题。
- [REBUT] W5 (REINFORCE++ 比较): 部分不同意——降级 Minor。主文仅简要提及，详细 caveats 在 Appendix。
- [AGREE] Minor 1-4: 全部同意。
- [AGREE] S1-S5: 全部同意。
- **维持 Overall 3.0 (Findings), Excitement 2.5/5。**

---

## 跨轮持续问题（Round 1→6 仍 open）

1. **Binary/ternary reward gap** (W2) — 6 轮
2. **Cell C 缺失** (W8) — 6 轮
3. **h-sweep single seed** (W5) — 6 轮
4. **Eq.6 单点测量** (W11) — 6 轮
5. **Table 1/2 报告标准不一致** (W12) — 6 轮
6. **REINFORCE++ 不公平对比** (W9) — 6 轮
7. **缺乏同期方法实验对比** (R2-N1) — 5 轮
8. **Factorial 2 seeds 统计效力不足** (R6-N2) — 新增 Critical