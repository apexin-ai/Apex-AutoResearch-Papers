---
round: 10
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-23T03:22:20.950940+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Round 11（Fresh Review）

**论文**: When Does Detect-and-Reweight Work? Epoch Confounds and Adaptive Reweighting in Continued LM Pretraining
**Venue**: EMNLP 2026 via ACL Rolling Review
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性/实验/统计；R2: 新颖性/Related Work/写作/格式）
**交叉轮次**: 1 轮（达成共识，无需第二轮）

---

## Summary

本文研究 detect-and-reweight 范式在 LM continued pretraining 中的有效性条件。通过 Qwen3-0.6B 在 132M FineWeb tokens 上的受控实验（ρ=0.4，3 seeds），论文提出三个发现：(1) D&R 评估中的 epoch confound——>95% 的 PPL 优势来自多 epoch 暴露而非过滤质量；(2) 有效 reweighting 需要检测器同时具备足够的判别力（AUC）和良好的校准（ECE）；(3) minimum intervention 优于 unconstrained maximization。基于此，论文推导了一个 dual-constrained adaptive b*，在 ρ≥0.4 时持续优于 uniform（Δ=−0.020 at ρ=0.4，Δ=−0.032 at ρ=0.6），但下游任务无显著改善。

---

## Strengths

1. **Epoch confound 分析设计精巧且结论有力** [R1, R2 一致]
   - 通过 epoch-matched 对照（Table 1）将 D&R 优势从 0.396 分解为仅 Δ=0.017，严格证明 >95% 来自多 epoch 暴露
   - Independent-LR replication（Δ=0.006）排除了 LR schedule 混淆
   - Permuted-score control 确认 detector signal 是 load-bearing 的
   - 这对整个 D&R 文献是重要的方法论校正

2. **三条 effectiveness conditions 形成实用决策框架** [R1, R2 一致]
   - Table 3 的决策矩阵（detector AUC ≥ 0.9, ECE ≤ 0.05, ρ ≥ 0.4）对从业者有直接参考价值
   - 每个条件通过消融实验建立，逻辑结构清晰

3. **诚实的 negative results 报告** [R1, R2 一致]
   - 坦承下游零改善（Table 4）、α_eff 校正后不显著（p_BH=0.078）、ρ=0.2 时退化、N=3 的统计限制
   - 透明度值得肯定

4. **LR-controlled verification 等实验细节严谨** [R2]
   - 对 epoch-matched 结果用独立 LR schedule 二次验证，排除 confound
   - Appendix 覆盖广泛（proofs、grid search、sensitivity、cross-model、low contamination），信息密度高

5. **可复现性良好** [R1: 4/5]
   - 超参数、训练配置、检测器细节（temperature scaling T=0.204）报告充分
   - 承诺 release code/data（review 期间无匿名 repo）

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1. N=3 seeds 统计检验力严重不足** [R1 Must-Fix, R2 Should-Fix→交叉后升级为 Agree]
- 全部主实验仅 3 random seeds（42, 123, 456），paired t-test 仅 2 自由度
- 核心 claim Δ=−0.020 的 95% BCa bootstrap CI [−0.028, −0.012]：BCa 的 bias-correction 和 acceleration 参数需从 jackknife 估计，N=3 时仅 3 个 jackknife 样本，参数估计本身极不稳定，覆盖率无保证
- Per-seed 方差极小（SD≈0.007），可能被 deterministic training recipe 人为压缩，低估真实实验不确定性
- Bonferroni-Holm 校正后 ρ=0.4 的 p_BH=0.078 未达显著水平
- **注**：R2 补充指出 epoch confound 的定性结论（>95% 来自 multi-epoch）受此影响较小，因方向在 3 seeds 中完全一致；统计效力问题主要影响 adaptive b* 的定量精度

**C2. α_eff proxy 可靠性严重不足** [R1 Must-Fix, R2 Should-Fix→交叉后 Agree]
- α_eff 与 true batch-level real fraction 的 Pearson r≈0.70（R²≈0.49），仅解释一半方差
- Pearson r=0.70 vs Spearman ρ=0.40 差距巨大：线性相关强但秩相关弱，暗示少数极端 batch 驱动相关，大多数 batch 排序不可靠——对 threshold-based 决策（α_eff ≥ τ）尤其危险
- 跨 seed 不稳定：Table 11 Pearson r 从 0.17 到 0.75 变化极大，r=0.17 的种子意味着 proxy 几乎完全失效（R²≈0.03）
- Table 11 仅基于 5 个离散 b 值（0, 0.25, 0.5, 0.75, 1），相关系数的估计本身不稳定
- 整个 adaptive 方法的 "自适应" 部分依赖 α_eff 作为 quality signal，proxy 不可靠则 bisection 找到的 b* 可能系统性偏离最优值

**C3. 下游任务零改善 + 效应量极小，论文 framing 存在 overclaim** [R1 Must-Fix + Should-Fix, R2 Must-Fix]
- Table 4: 5 个下游任务 adaptive (0.5414) = uniform (0.5414)，"All differences within standard error"
- Epoch-matched 条件下 adaptive vs uniform 的真实改善仅 Δ=−0.020 PPL（~0.11% relative）
- 即使 grid-best（post-hoc oracle），改善也仅 ~0.2%（17.657 vs 17.694），整个方法类别的天花板极低
- Abstract 中 "yielding a practical adaptive method" 构成 overclaim：一个在下游任务上零改善的方法难以被称为 "practical"
- 论文在 §6 和 Limitations 中坦承了这些事实，但 Abstract/Intro 的 framing 与实际结果不匹配

**C4. 实验范围过窄，不足以支撑一般性结论** [R1 Should-Fix, R2 Must-Fix]
- 仅 Qwen3-0.6B（0.6B params）、FineWeb 132M tokens、self-generated contamination（generator=trainee）
- Self-contamination 使 AUC=0.94 具有人为优势：generator=trainee 时检测器可利用自身 decoding 的统计规律性，真实 web contamination 中 AUC 可能显著更低
- Cross-model 实验（Appendix O, Llama-3.2-3B）仅单 seed 且结果 mixed（MMLU↑, HellaSwag↓）
- ρ=0.2 时方法 degrade（Appendix Q, Δ=+0.046），而 20% 正是论文自己引用的 web contamination 估计下限
- "Three effectiveness conditions" 的一般性结论缺乏多模型/多数据集/cross-model contamination 验证
- **R1 补充**：三个条件作为 necessary conditions 的逻辑结构合理，但论文措辞有时暗示了更强的一般性

### Should-Fix（影响评分但不一票否决）

**W1. Adaptive b* 方法新颖性不足** [R2 Must-Fix, R1 Should-Fix]
- w=(1−q)^b 框架完全来自 Drayson et al. (2025)
- Dual-constrained b* 本质是参数选择启发式：两约束优化 + bisection 求解，Proposition 1-2 为标准单调性推导
- Adaptive vs grid-best: 17.674 vs 17.657，效果几乎无差异
- **R1 补充（部分反驳 R2）**：adaptive 方法的价值在于 zero-cost 接近 grid-best（grid search 需 9 次完整训练），17.674 vs 17.657 说明方法有效而非无价值。问题在于 positioning 而非方法无效
- **共识**：新颖性问题可通过明确 analysis paper 定位缓解——将 adaptive b* 降级为 practical corollary

**W2. Analysis paper vs method paper 定位不清晰** [R1 Agree, R2 Should-Fix]
- Abstract 同时 claim "we analyze when, why, and how" + "we derive a dual-constrained adaptive b*"
- Epoch confound 分析远比 adaptive method 有说服力
- 建议明确以分析为主线，adaptive b* 为实践推论

**W3. Related Work 遗漏近期 instance-level reweighting 工作** [R2 提出, R1 部分同意]
- 可能遗漏的直接相关工作：
  - Dynamic Loss-Based Sample Reweighting (arXiv:2502.06733, Feb 2025)
  - Self-Influence Guided Data Reweighting (ICLR 2025)
  - ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695, 2025)
  - LLM-Generated Text Detection Survey (Wu et al. 2025, Computational Linguistics)
- 论文应讨论 provenance-based reweighting 与 loss-based/influence-based 信号的区别
- R1 提醒：blind review 条件下需核实这些引用的真实性和相关性

**W4. Epoch confound 讨论缺乏对 prior work 的具体分析** [R1 Agree, R2 提出]
- "过滤数据→更多 epoch" 概念上非完全出乎意料
- 贡献在于严格实验验证，但需讨论：Drayson et al. 等 prior work 是否控制了 epoch？为何被忽略？
- 可能原因包括：prior work 关注 absolute performance 而非 epoch-controlled comparison；from-scratch pretraining 中 confound 不如 continued pretraining 明显

### Minor（不影响接收）

**m1. ESS/α_eff 约束冲突行为缺乏明确分析** [R1 提出, R2 部分反驳]
- 约束冲突时退回 b=b_ESS 的频率和后果未明确报告
- R2 反驳：ESS-only baseline（Table 2, 17.737）已隐式展示约束冲突的极端行为；minimum intervention 原则保证退回行为合理
- 共识：建议补充真正冲突（α_eff < τ at b=b_ESS）的 batch 比例，但不构成 fundamental threat

**m2. 格式小问题** [R1, R2]
- Figure 2 偏小，legend 接近可读性下限（~7-8pt），灰度打印下 marker 难区分
- 12+ 脚注含关键技术细节（footnote 1 batch composition, footnote 2 rounding），建议关键内容移入正文
- Table 2 小数位不一致
- "practical" 一词使用频率过高

**m3. Appendix 过于庞大** [R1, R2]
- 5 页 17 个子附录（A-Q）
- Appendix K（α_eff validation）和 Appendix N（low contamination）对核心论点很重要但正文引用不充分

---

## Reviewer Consensus

| 问题 | R1 | R2 | 交叉后一致性 |
|------|----|----|-------------|
| N=3 统计效力不足 | Must-Fix (N1) | Should-Fix (W3) → AGREE 升级 | **一致：Must-Fix** |
| α_eff proxy 不可靠 | Must-Fix (N2) | Should-Fix (W5) → AGREE | **一致：Must-Fix** |
| 下游零改善 + 效应量小 | Must-Fix (N3) + Should-Fix (W3) | Must-Fix (N1) | **一致：Must-Fix** |
| 实验范围过窄 | Should-Fix (W1) | Must-Fix (N2) | **一致：Critical** |
| 方法新颖性 | Should-Fix (W2) | Must-Fix (N3) → R1 PARTIALLY REBUT | **轻微分歧：R1 认为 should-fix（zero-cost 有价值），R2 认为 critical** |
| 论文定位 | AGREE (W4) | Should-Fix (W4) | **一致** |
| Missing references | PARTIALLY AGREE (W1) | Should-Fix (W1) | **一致** |

## Reviewer Divergence

**唯一实质分歧**：Adaptive b* 新颖性的严重程度
- R2：Must-Fix critical——本质是参数选择启发式，Proposition 1-2 trivial，与 grid-best 几乎无差异
- R1：Should-Fix——zero-cost 接近 grid-best 有实践价值（省去 9 次完整训练），问题在于 positioning 而非方法无效
- **Director 判断**：R1 的论点更有说服力。Adaptive b* 确实新颖性有限，但 zero-cost 替代 grid search 是有实际意义的工程贡献。归类为 Should-Fix，可通过论文定位调整（analysis paper + practical corollary）缓解。

---

## Questions

1. **Power analysis**：给定 Δ=0.020, SD≈0.007，N=3 的 statistical power 是多少？80% power 需要多少 seeds？
2. **α_eff 散点图**：Pearson r=0.70 vs Spearman ρ=0.40 差异的原因？能否提供 α_eff vs true real fraction 的散点图？
3. **α_eff 与 downstream 的直接关系**：α_eff → PPL 链条已建立，但 α_eff → downstream accuracy 未验证
4. **Cross-model contamination**：三个 effectiveness conditions 在 generator≠trainee 场景下是否成立？
5. **ρ=0.2 代表性**：方法在论文自己引用的 contamination 下限（20%）即退化，是否意味着仅适用于高污染场景？
6. **Drayson et al. 的 epoch confound**：他们的实验是否控制了 content epochs？他们的 b=10 结果中有多少可用 epoch confound 解释？

---

## Missing References

1. Dynamic Loss-Based Sample Reweighting for LLM Pretraining (arXiv:2502.06733, 2025) — instance-level dynamic reweighting
2. Self-Influence Guided Data Reweighting for LM Pre-training (ICLR 2025) — self-influence based reweighting
3. ToReMi: Topic-Aware Data Reweighting (arXiv:2504.00695, 2025) — topic-aware dynamic reweighting
4. A Survey on LLM-Generated Text Detection (Wu et al. 2025, Computational Linguistics) — 最新 MGT detection 综述

（注：以上引用由 R2 提出，R1 在 blind review 条件下无法独立核实，建议作者核实后酌情引用）

---

## External Review

外部审稿：未配置（项目未启用 paperreview.ai）。

---

## Visual Layout Check（非评分项）

状态：**已完成**（耗时约 4 分钟）

| 严重性 | 数量 |
|--------|------|
| Critical | 0 |
| Warning | 1 |
| Info | 6 |

关键发现：
- **[Warning] Pages 3-4 连续两页无 display item**：Page 3 有数学公式（部分缓解），但 Page 4（Experimental Setup）为纯文本 + bullet list，可能造成视觉疲劳。建议从 Appendix 提前一个表或图至 p.4。
- **[Info] Figure 1 为文字摘要式概览框**：对 analysis 论文可行，但替换为因果关系流程图可能更有效。
- **[Info] Figure 2 偏小**：legend 和 axis label 接近可读性下限（~7-8pt），marker 形状区分尚可。
- **[Info] Table 1 caption 信息自包含度优秀**，Table 3 排版整洁有 actionable 价值。
- **[Info] Appendix 图表密度高但可接受**。

---

## Overall Assessment

**评分：3.0 — Findings**
**置信度：4/5**（两位 Reviewer 独立达成一致评分，交叉后核心问题高度收敛）

### 评分理由

**论文的核心价值在于 epoch confound 的分析发现，而非 adaptive reweighting 方法本身。**

Epoch confound 分析（>95% 的 D&R 优势来自多 epoch 暴露）是对 D&R 文献有价值的方法论校正，实验设计精巧（epoch-matched controls + LR replication + permuted-score control），足以支撑 Findings 级别接收。

但论文未达到主会议（4.0）门槛，原因如下：
1. **统计基础脆弱**：N=3 seeds（2 df），BH 校正后 ρ=0.4 不显著（p=0.078），bootstrap CI 可靠性存疑
2. **方法贡献的核心 proxy 不可靠**：α_eff R²=0.49，跨 seed r 从 0.17 到 0.75，Spearman 校正后不显著
3. **实际影响极小**：Δ=−0.020 PPL（~0.11%），下游任务零改善，整个方法类别的 upper bound 也仅 ~0.2%
4. **实验范围过窄**：单模型/单数据集/self-contamination，ρ=0.2 时退化，cross-model 结果 mixed
5. **方法新颖性有限**：w=(1−q)^b 完全来自 Drayson et al.，adaptive b* 是增量式参数选择规则

### 与 EMNLP 2026 评分标准的对应
- 3.0 = Findings：有价值的分析贡献（epoch confound），但效应量、实验范围和方法新颖性不足以进入主会议
- 不够 3.5 (Borderline Conference)：缺少更广泛的实验验证和有意义的下游改善
- 高于 2.5 (Borderline Findings)：epoch confound 发现对社区有实际价值，实验设计严谨，报告诚实

---

## Detailed Comments

### §1 Introduction
- "yielding a practical adaptive method" 措辞建议修改为更谦虚的表述，如 "as a practical corollary, we derive..."（论文部分已这么做，但 Abstract 和 Intro 的 leading sentence 仍偏强）
- Figure 1 的 TikZ 概览框有效但可考虑改为因果流程图

### §3 Method
- 已从 Round 10 的 1.5 页压缩至 ~0.75 页，改进明显
- Proposition 1-2 虽正确但 trivial，建议保留在 Appendix
- α_eff 的 Pearson r≈0.70 在正文中提及，但未提及 Spearman ρ=0.40 和跨 seed 不稳定性——正文应更完整地反映 proxy 的局限

### §4 Experimental Setup
- Self-contamination 预告句已加，但讨论仍不足——建议增加一句关于 generator=trainee 对 detector AUC 的人为优势
- Page 4 无 display item，视觉节奏偏单调

### §5 Results
- Table 1（epoch-matched）和 Table 2（main results）设计清晰，caption 信息自包含
- §5.1 建议在开头就明确区分 "full advantage (0.396)" 和 "epoch-controlled advantage (0.020)"
- §5.2-5.3 的 ablation/sensitivity 分析充实

### §6 Discussion
- Effect size 讨论和 downstream null 分析已有改进
- α_eff 方差分解段落有价值，但应补充跨 seed 不稳定性的讨论
- "When uniform beats reweighting" 段落对从业者有实际指导价值

### §7 Conclusion
- 与 Abstract 基调一致但偏乐观，batch-size amplification 的外推是 speculative（论文已承认）

### Limitations
- 覆盖模型规模、数据范围、seed 数量、self-contamination，合理但可以更强调 ρ=0.2 退化的 implications

### References
- 格式基本一致，部分 arXiv preprint 未标注会议版本（如已被接收）
- 建议核实并补充 R2 提出的 4 篇遗漏引用

### Appendix
- 内容丰富（A-Q, 17 节），但 Appendix K（α_eff validation）和 Appendix N（low contamination）的结论对核心 claims 影响大，建议在正文更显著地引用