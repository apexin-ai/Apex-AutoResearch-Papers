---
round: 6
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T05:04:42.133939+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 6 审稿报告

**论文**: How Pruning Criteria Shape Post-RLVR Recovery in Reasoning Language Models
**Venue**: EMNLP 2026 (ARR)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性）
**轮次**: Round 1（fresh 审稿），交叉分享后达成共识，1 轮收敛

---

## Summary

论文研究不同剪枝评分标准（CKA-only、Standard importance、RASP、Random）对推理型语言模型 RLVR 恢复能力的影响。采用严格控制变量设计（四种方法共享同一 structural analysis pipeline，仅变化 scoring criterion），在 DeepSeek-R1-Distill-Qwen-7B 上通过 SFT→GRPO 两阶段 pipeline 验证。核心发现：基于 CKA 冗余度的剪枝显著优于基于梯度重要性的方法，形成 "recovery capacity spectrum"，并观察到 reward-accuracy decoupling 现象。

---

## Strengths

**S1. 控制变量实验设计（双 Reviewer 共识，论文最大亮点）**
四种剪枝标准共享完全相同的 structural analysis pipeline，唯一变量是 scoring criterion。这种设计在 LLM 剪枝文献中极为少见，使归因分析干净可靠。R1 指出此设计 "在剪枝文献中少见"。[R1-S1, R2-S1]

**S2. 多维度训练动态诊断**
reward trajectory、f_b（全零 reward batch 比例）、gradient norm、KL divergence 四维诊断体系超越常见的 final-checkpoint accuracy 报告，提供了丰富的训练行为洞察。[R1-S2, R2-S2]

**S3. Actionable finding**
CKA-based >> gradient importance for RL recovery 是可直接指导 pruning practitioners 实践的发现。[R1-S1, R2-S2]

**S4. Reward-accuracy decoupling 观察**
作为科学发现有独立价值，揭示 RL reward 优势不等于下游准确率优势。[R1-S4, R2-S4]

**S5. 可复现性高**
超参数表完整（Table 4, Appendix A），Algorithm 1 伪代码清晰，硬件报告充分。[R1-S3, R2-S4]

**S6. RASP 负面结果的指导价值**
RASP 的失败为社区提供了 "不应做什么" 的实际参考。[R2-S3]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1** [critical, 双 Reviewer 共识] **GSM8K 单基准 GRPO 主实验，Title/Abstract 做一般性声明**
所有 GRPO 主实验（recovery capacity spectrum、reward-accuracy decoupling、training dynamics）仅在 GSM8K 上进行。补充基准证据不够有力：MATH-500 受 2048-token 截断影响方法间差异被压缩至噪声水平（|Δ| ≤ 1.2pp）；MBPP 四个受控方法 margin 仅 ~1pp。Title "How Pruning Criteria Shape Post-RLVR Recovery" 和 Abstract 均为一般性措辞，与单基准实验支撑不匹配。R1 补充：MBPP 受控方法内排序与 GSM8K 一致（CKA-only 领先），但 margin 过小不具统计说服力。
→ 至少需一个非 GSM8K 基准的完整 GRPO 实验，或严格限定 scope 至 "mathematical reasoning on GSM8K"。[R2-N1, R1-AGREE]

**MF2** [critical, 双 Reviewer 共识] **RASP/Random 仅 1 GRPO seed，统计标准不对称**
CKA-only 和 Standard 各有 3 seeds（Table 11, Appendix I），RASP 和 Random 为 N=1。论文声称 "RASP collapses permanently (0.061)" 和 "Random stagnates"，但 RASP α=4.0 在 preliminary 实验中显示 active learning（peak reward 0.256, Section 4.4），说明 CKA 权重微小变化可翻转训练动态。Spectrum 的下半部分（Random > Standard > RASP）排序可靠性存疑。R1 补充：RASP collapse 虽极端但 Standard（peak 0.081）与 Random（0.14-0.19）之间的排序是否稳健需多 seed 验证。
→ 为 RASP 和 Random 各补充至少 3 GRPO seeds。[R1-N1, R2-W3, mutual AGREE]

**MF3** [critical, 双 Reviewer 共识] **跨架构验证仅 SFT、N=200，与论文自身逻辑矛盾**
Qwen2.5-Math-7B 验证仅到 SFT 阶段（Table 13），N=200 且自标 "preliminary"，但 Abstract 声称 "provide initial evidence for generality"。论文自身在 Section 4.4 明确指出 "Post-SFT accuracy does not predict GRPO outcome"。R1 精准指出：按论文自己的逻辑，SFT-only 结果不能推断 RLVR generality，此处构成自相矛盾。且两个模型共享 Qwen2.5 base architecture，跨架构多样性不足。
→ 完成 GRPO 验证或将 Abstract claim 严格限定为 "SFT-level structural effects generalize"。[R1-N2, R2-N3, mutual AGREE]

**MF4** [critical, 双 Reviewer 共识] **Contribution 3 "representational diversity" 机制证据仅为相关性，列为 numbered contribution 是 overclaim**
Section 4.5 证据链：CKA heatmap 视觉观察 → overlap analysis 描述性统计。无因果干预实验。R2 指出将 correlational observation 升格为 numbered contribution 不当；R1 完全同意并指出 "plausible mechanism" 的 hedging 不足以支撑 numbered contribution 地位。R1 建议一个可行的因果验证思路：人工构造等量剪枝但 diversity 不同的模型对比 GRPO recovery。
→ 降级为 observation/hypothesis 置于 Discussion，或增加因果干预实验。[R2-N2, R1-AGREE]

**MF5** [critical, R1 提出] **Layer-depth pruning pattern 与 representational diversity 混淆（confound 未排除）**
CKA-only 将 72.5% 移除集中在 early layers (L0-9)，Standard 均匀分布（Appendix N）。论文将优势归因于 "preserved representational diversity"，但同样合理的解释是 CKA-only 碰巧保留了对推理关键的 late layers。此 confound 未被排除，使 Contribution 3 的归因可能不准确。
→ 增加 depth-controlled baseline（如 "Late-Layer-First" pruning），或在 Discussion 中充分讨论此 confound。[R1-N3; R2 未直接评论但其 MF4 覆盖类似关切]

**MF6** [critical, R2 提出] **缺失高度相关文献**
"RL Finetunes Small Subnetworks" (arXiv:2505.11711) 揭示 RL fine-tuning 只更新 5–30% 参数，在 GRPO 等 7 种 RL 算法上均成立。与本文核心主题直接相关：如果 RL 只在小子网络上操作，剪枝标准是否保留了该子网络可能才是解释 CKA-only 优势的关键因素。
→ 在 Related Work 讨论并引入 Section 4.5 机制分析。[R2-N2 交叉回应]

### Should-Fix（影响评分但不一票否决）

**SF1** [warning] Welch's t-test at N=3 统计功效极低（Section 4.2, p=0.0009）。补充 Cohen's d 和 bootstrap 95% CI。[R1-W1]

**SF2** [warning] α/κ 消融不完整：α 消融仅用 post-prune accuracy（Table 6），缺 GRPO reward 全景；RASP 只测 κ=1.0 就结论 collapse，缺 κ∈{0.25,0.5,2.0,4.0} 消融。[R1-W2, R2-W1]

**SF3** [warning] 40% per-layer capacity floor 未消融（Section 3.3, Limitations）。建议 floor ∈ {30%, 50%, 60%}。[R1-W3]

**SF4** [warning] Reward-accuracy decoupling 未区分 format compliance vs reasoning quality。f_b 混淆格式崩塌和推理错误两种失败模式，需细粒度分析。建议报告各方法 EOS rate 和 format compliance rate 随 step 变化。[R2-W2, R1-AGREE]

**SF5** [warning] MLP channel pruning scope 未在 Title/Abstract 限定。实验严格限定在 MLP channel group pruning，但 Title 完全一般化。建议加入 "structured MLP pruning" 限定。[R2-W1, R1-AGREE]

**SF6** [warning] 术语不一致："recovery capacity spectrum"（Abstract）vs "recovery capacity gradient"（Table 1 caption）。应统一。[R2-W4, R1-AGREE]

**SF7** [warning] 遗漏 3 篇相关工作：(1) "On the Limits of Layer Pruning for Generative Reasoning in LLMs" (arXiv:2602.01997, Feb 2026)；(2) "Prune as You Generate: Online Rollout Pruning for RLVR" (arXiv:2603.24840, March 2026)；(3) LaCo (Yang et al., 2024, EMNLP Findings)。R1 web search 确认前两篇真实存在。[R2-W5, R2-W2, R1-AGREE]

**SF8** [warning] 15%/25% sparsity 实验为 single-seed，"sparsity-dependent decoupling" 统计基础不足。[R2-W5]

**SF9** [warning] RASP 表现差于 Standard 缺乏充分解释。需分析 importance 和 CKA overlap 的相关性，解释 multiplicative 组合为何失效。[R1-W5]

**SF10** [warning] 引用错误：正文 "Dong et al. (2026)" vs 参考文献 "Longyi Deng"。[R2-W3]

---

## Reviewer Consensus

以下问题双 Reviewer 明确达成 [AGREE]：
1. GSM8K 单基准是最大结构性弱点（MF1）
2. RASP/Random 单 seed 统计不充分（MF2）
3. SFT-only 跨架构验证与论文自身 "SFT ≠ GRPO prediction" 论点自相矛盾（MF3）
4. Contribution 3 机制证据仅相关性，列为 numbered contribution 是 overclaim（MF4）
5. Table 1 脚注 "Only redundancy-based pruning sustains RL recovery" 与 Random 排第二矛盾（SF7 小问题）
6. Section 5 Discussion 偏薄（SF8）
7. **控制变量设计是论文最大亮点**——双 Reviewer 一致认为此设计在 LLM 剪枝文献中有独特价值

## Reviewer Divergence

**评分分歧**：R1 初始 3.5 (Borderline Conference)，R2 初始 3.0 (Findings)。交叉分享后 R1 表示 "R2 的 3.0 合理"，分歧实质消解。

**MF5 (Layer-depth confound)**：R1 单独提出为 critical。R2 未直接评论此具体 confound，但其对 mechanism 证据的质疑（MF4）覆盖了类似关切。

**MF6 (Missing literature: RL Finetunes Small Subnetworks)**：R2 在交叉回应中新增。R1 未评论此具体论文。

**Excitement 评分**：R1 给 3/5，R2 给 2.5/5。R2 认为贡献主要是经验发现，无新方法或可落地工具，CKA-only 评分本身非原创（源自 Lachance &amp; Bhatt, 2022）。

---

## Questions

1. RASP α=4.0 的 active learning（peak reward 0.256, Section 4.4）是否说明 RASP collapse 是超参问题而非方法本质问题？完整的 α/κ 消融结果如何？
2. CKA-only 的 layer-depth pruning pattern（72.5% 移除集中 L0-9）是否是 recovery 优势的真正原因？是否有 depth-controlled ablation 数据？
3. 如果 RL fine-tuning 只更新 5–30% 参数（per arXiv:2505.11711），CKA-based pruning 是否恰好保留了这些关键子网络？
4. Reward-accuracy decoupling 中，各方法的 format compliance rate 随 GRPO step 如何变化？reward 差异是否主要来自格式合规差异？
5. "Post-SFT accuracy does not predict GRPO outcome" 仅基于 4 个数据点（四种方法），是否有更多数据支撑？

---

## Missing References

1. **RL Finetunes Small Subnetworks** (arXiv:2505.11711) — RL 只更新小子网络，与 pruning+RLVR 主题直接相关 [R2-N2, critical]
2. **On the Limits of Layer Pruning for Generative Reasoning in LLMs** (arXiv:2602.01997, Feb 2026) — layer pruning 对推理的影响 [R2-W5, R1 confirmed]
3. **Prune as You Generate: Online Rollout Pruning for RLVR** (arXiv:2603.24840, March 2026) — 同方向并行工作 [R2-W5, R1 confirmed]
4. **LaCo** (Yang et al., 2024, EMNLP Findings) — structured pruning 核心文献 [R2-W2]

---

## External Review

**外部审稿（Stanford Agentic Reviewer）**：未请求。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2026-05-22 04:39→04:42，耗时 ~3min）。

**发现**：
- **[warning]** 连续 3 页纯文本（p3-5），Method 段缺少视觉锚点。建议在 Section 3 中插入示意图（如 scoring criteria 对比或 two-stage recovery 流程图）打破纯文本节奏
- **[info]** Figure 3 子图 axis label 和 legend 字号偏小（约 6-7pt），打印/标准缩放下需仔细辨认
- **[info]** Figure 4 热力图标注文字偏小
- **[info]** Figure 5 尺寸较小（单栏宽度，约占 1/4 页面），若为重要补充结果可考虑放大
- **[info]** 附录 E-K 多个小节挤在同一页，内容密度极高
- **[info]** 首页无 display item，Figure 1 在第 2 页出现（非必须修改，但提前到首页底部可强化第一印象）

统计：0 critical, 1 warning, 5 info。无阻断性排版问题。

---

## Overall Assessment

**Overall Score: 3.0 / 5 (Findings)**

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3.0 | 3.0 | 3.0 |
| Excitement | 3.0 | 2.5 | 2.75 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5→3.0* | 3.0 | 3.0 |
| Confidence | 4.0 | 4.0 | 4.0 |

*R1 交叉分享后认同 R2 的 3.0 评估。

**理由**：
论文的控制变量实验设计是其核心方法论贡献，在 LLM 剪枝文献中有独特价值。CKA-based >> gradient importance for RL recovery 的发现有实践指导意义。多维度训练动态诊断和 reward-accuracy decoupling 观察丰富了论文的分析深度。

然而，6 个 critical 问题（含双 Reviewer 共识 4 个）严重削弱了论文的可接收性：
1. **Empirical scope 过窄**：核心 claim 的实验支撑限于单模型（DeepSeek-R1-Distill-Qwen-7B）、单基准（GSM8K）、部分方法单 seed，但 Title/Abstract 做一般性声明
2. **机制解释不可靠**：Contribution 3 仅为相关性证据，且存在未排除的 layer-depth confound
3. **内部逻辑矛盾**：论文自身的 "SFT ≠ GRPO prediction" 发现与 SFT-only 跨架构 generality claim 直接冲突

论文适合 Findings track。若能补充以下修改，有望达到 3.5 (Borderline Conference)：
- 至少一个非 GSM8K 基准的完整 GRPO 实验
- RASP/Random 补充多 seed
- Contribution 3 降级为 observation
- 讨论 layer-depth confound
- 引入 "RL Finetunes Small Subnetworks" 等缺失文献

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution 3 "identified representational diversity as a key mechanism" 措辞过强 → "observed evidence consistent with representational diversity playing a role"
- "recovery capacity spectrum" 需在首次使用时前置定义

### Section 2 (Related Work)
- 缺少 4 篇高度相关工作（见 Missing References），特别是 arXiv:2505.11711 对机制解释有直接影响
- LaCo 作为 EMNLP 2024 Findings 的 structured pruning 核心工作应被讨论

### Section 3 (Method)
- κ=1.0 single setting 不足以评判 RASP → 需 κ 消融（κ∈{0.25,0.5,2.0,4.0}）
- 40% capacity floor 是关键设计决策但无消融支撑
- Algorithm 1 清晰，但 scope 限定（MLP channel pruning）应更早明确

### Section 4.1-4.2 (Main Results)
- Table 1 spectrum ordering 的统计支撑不对称（CKA/Standard N=3 vs RASP/Random N=1）
- Table 1 脚注 "Only redundancy-based pruning sustains RL recovery" 与 Random 排第二矛盾 → 改为 "Only redundancy-based pruning enables active RL learning"
- Welch's t-test at N=3 应补充 Cohen's d effect size 和 bootstrap 95% CI

### Section 4.3 (Reward-Accuracy Decoupling)
- 需区分 format compliance vs reasoning quality 对 reward 的贡献
- 建议报告各方法的 EOS rate 和 format compliance rate 随 step 变化
- "Reward-accuracy decoupling" 首次使用时无正式定义
- 15% sparsity 作为 decoupling 不成立的操作点值得更多讨论

### Section 4.4 (α Analysis)
- α=4.0 "full evaluation pending" 应在提交前完成
- κ 消融缺失，仅 κ=1.0 不足以判定 RASP 方法本身

### Section 4.5 (Representational Diversity &amp; Cross-Architecture)
- **Layer-depth confound 必须讨论**：CKA-only 保留 late layers 的模式可能是优势真正来源
- "Post-SFT accuracy does not predict GRPO outcome" 仅基于 4 个数据点
- Qwen2.5-Math-7B N=200 样本量不足，且仅 SFT 阶段

### Section 5 (Discussion)
- 仅半页，对控制变量比较研究而言不足
- 缺少：(1) CKA-based redundancy 与 RL exploration 的关系讨论，(2) 对 pruning practitioners 的 actionable 建议，(3) 与 Lottery Ticket Hypothesis 的联系

### Writing &amp; Format
- "recovery capacity spectrum" vs "recovery capacity gradient" 术语不一致
- Figure 2 y 轴标签需标注 mean vs peak reward
- Figure 2 四条曲线区分度不够，建议不同 line style + marker
- 引用错误："Dong et al. (2026)" vs "Longyi Deng"
- Method 段（p3-5）连续纯文本，缺视觉锚点（视觉审查 warning）