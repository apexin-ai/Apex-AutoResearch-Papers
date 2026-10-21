---
round: 20
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T17:30:58.451376+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 22 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计, R2: 新颖性+写作完整性）
**圆桌轮次**: 1 轮初审 + 1 轮交叉分享（达成收敛）

---

## Summary

本文提出用 forward KL 蒸馏训练 SwiGLU LLM 的上下文稀疏性预测器，替代传统 BCE 训练。在 LLaMA-3.1-8B 上，KL 预测器在 30% 稀疏度下将 TEAL 的困惑度降低 14.5%（matched sparsity），在 50% 下降低 50%。论文进行了系统性分析：target-swap ablation (C1) 探索 mask pattern 的可迁移性，per-layer KL 分解（K=1/K=4 控制实验）尝试解耦 signal type 和 coupling scope 的贡献，跨三个架构（LLaMA-8B, Mistral-7B, Qwen-14B）验证泛化性。论文自我定位为实证研究（"primarily an empirical study"），不涉及 wall-clock 加速。

---

## Strengths

**S1 [共识]** 实验设计严谨且覆盖面广：5 种 loss function 对比（KL, reverse KL, JSD, BCE, MSE）、3-seed 评估、3 个架构、6+ 下游任务、C1 target-swap、K=1/K=4 分解、SNR 分析、bottleneck/temperature/training steps sensitivity。总实验量远超一般 EMNLP 投稿（registry 显示 374 个实验）。

**S2 [共识]** Target-swap ablation (C1) 是一个巧妙的分析方法，能够部分解耦 mask quality 和 training mechanism 的贡献。尽管因果声明存在过强问题（见 Weakness N1），实验设计本身具有方法论参考价值。

**S3 [共识]** Per-layer KL 分解（K=1 和 K=4 控制实验）对 signal type vs coupling scope 的定量分解是该领域的新颖分析维度，即使精确数字不可靠（见 N2），分析框架本身有贡献。

**S4 [共识]** 诚实的自我定位：论文明确声明 "primarily an empirical study"，详细讨论了 confounds、upper bounds、和 limitations。这种学术诚实在该领域并不常见。

**S5 [共识]** 可复现性好：所有超参数完整报告，exp_id 标注在 LaTeX 注释中，训练仅需 ~45 min 单卡，19 页 Appendix 提供充分补充材料。

**S6 [R1]** 梯度分析 (§3.6) 虽基于标准 chain rule，但在稀疏性预测场景下的应用新颖：BCE 梯度仅依赖 neuron j，KL 梯度通过下游 Jacobian 耦合所有层。配合 SNR 分析（KL 信号更噪但 mask 更好）构成 "search mechanism > gradient clarity" 的有趣叙事。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [共识 Critical]** C1 Target-Swap Ablation 的因果声明过强

论文在 Abstract 和 §4.4 中声称 "the discovered patterns—not the training mechanism itself—as the proximate quality driver"。两位 Reviewer 一致认为此 claim 超出实验证据：

- **循环性**：KL-derived masks 本身是 KL coupling 的产物。C1 仅证明 mask patterns 的可迁移性（BCE trained on KL targets approaches KL-level PPL），而非 mask patterns 是 "唯一" 质量驱动因素。
- **s42 不一致**：s42 使用 earlier checkpoint oracle (PPL gap 0.65pp)，而 s123/s456 使用 matched retrained oracle (gap ≤0.03pp)。Table 3 footnote † 容易忽略。
- **下游方向不一致**：s42 C1 在 MMLU +1.7pp 优于 KL，但 s456 C1 在 MMLU −0.96pp 劣于 KL。如果 mask pattern 是唯一驱动因素，方向应一致。
- **Soft-vs-hard confound**：BCE+Gumbel (32.22) vs standard BCE (27.97) 的控制实验不干净——Gumbel 在 BCE 设置下有害，无法作为 "softness 不是主因" 的中性控制。

**建议**: 将 claim 降级为 "KL-discovered masks are transferable: BCE trained on KL-derived targets approaches KL-level PPL, suggesting mask patterns carry substantial quality information"。删除 "not the training mechanism itself" 的排除性声明。

**N2 [共识 Critical]** 97.5% Signal Type Decomposition 受严重混淆变量影响

97.5% 出现在 Abstract（第5句）、Introduction（contribution #1）、Conclusion（第1句）的核心位置，但实验证据不支持这一精确数字：

- **K=1 train-inference mismatch**：训练时仅 mask 1/32 层，推理时 mask 全部 32 层。论文在 Footnote 5 承认 "not fully orthogonal"，但 caveat 的显著性远不及 97.5% 的反复出现。
- **K=4 引入新 confound**：K=4 的 near-uniform per-layer sparsity (std=0.003) 恰好匹配 uniform eval allocation，导致 MMLU >100% gap closure——这是 allocation alignment artifact，非 coupling 效应。
- **Metric 分歧**：ARC-c gap closure 2.6%（coupling-dominated）vs PPL 66.7%（mismatch-dominated）vs MMLU >100%（anomalous）。四个 metric 指向截然不同结论，无法支撑单一叙事。
- **50% 缺 K=4**：50% 仅有 K=1 结果（per-layer KL 34.85 vs E2E 11.92, +192%），恰恰是 coupling 贡献最大的区间却缺少 mismatch 控制。

**建议**: 将 "97.5%" 替换为定性描述 "signal type accounts for the majority of the PPL gap (upper bound; confounded by train-inference mismatch)"。在主文而非 footnote 中讨论 orthogonality limitation。如可行，补充 K=4 at 50% 的 3-seed 实验。

**N3 [R2 Critical, R1 borderline Must-Fix]** MMLU/GSM8K 跨架构系统性退化

KL predictor 在所有测试规模上系统性逊于 TEAL：
- LLaMA-8B 30%: MMLU −5.2pp (40.7 vs 45.86), GSM8K −1.3pp
- Qwen-14B 30%: GSM8K −20pp, MMLU −8pp (uniform)
- Mistral-7B 30%: GSM8K 8.6 vs 15.9 (TEAL wins)

论文的 "distribution-matching objectives sacrifice reasoning pathways" 是描述非解释。更关键的是，Appendix T (Remove Valley) 实验显示 MMLU +3.3pp 可恢复——这表明退化部分源于可纠正的 allocation 问题，但论文未追踪此线索（如 task-aware allocation）。Forward KL 的 mode-covering 动机（§3.4: "false negatives cascade"）与 reasoning 退化之间的矛盾未讨论。

**建议**: 深入分析 KL mask 在哪些层与 reasoning-critical activations 冲突；基于 Remove Valley 发现讨论 task-aware allocation 可能性；讨论 mode-covering 与 reasoning 退化的 trade-off。

---

### Should-Fix（影响评分但不一票否决）

**W1 [分歧 → Director 判定 Warning]** 无实际推理加速

R2 将此列为 Critical，R1 列为 Should-Fix。论文在 Introduction 已明确定位为 empirical study 且声明不涉及 latency optimization。R1 正确指出 predictor 产生的 mask 可 plug into TEAL 的 kernel pipeline。**但**论文的 opening motivation 仍以 inference allocation 为核心，且 Table 5 显示 +6.4% 延迟。Director 判定：Should-Fix。论文应在主文中更显著说明 speedup 所需条件。

**W2 [分歧 → Director 判定 Warning]** 与 MaskLLM 区分度

R2 列为 Critical，R1 REBUT（contextual vs static masks 是 fundamental difference）。R1 的论证有力——per-token generalization、cross-layer allocation、OOD robustness 确实是本质差异而非应用场景差异。但核心 recipe（frozen model + KL + Gumbel masks）的重合不可否认。Director 判定：Warning。§2 已做 3-point differentiation，但论文应更明确定位为 systematic empirical analysis 而非暗示方法论创新。

**W3 [共识]** Table 2 actual sparsity mismatch (KL 28.5% vs TEAL 29.3%)

Table 2 的 ‡ 脚注容易忽略。Raw comparison (8.81 vs 10.82 = 18.6% improvement) 夸大优势，matched 28.5% comparison (14.5%) 仅在 Appendix。建议 Table 2 增加 TEAL at 28.5% 行或更显著标注。

**W4 [共识]** KL global 50% 下游仅 s42 单种子

Table 2 中 KL global 50% 的 ARC-c (32.85)、WG (63.46)、GSM8K (1.29) 无 ± 标注，与同表 KL uniform 50%（全部 3-seed）标准不一致。

**W5 [共识]** 规模泛化仅 7–14B

Qwen-14B 的 GSM8K −20pp 暗示 reasoning 退化可能随规模恶化。如无法补充更大规模实验，应在 Limitations 中明确讨论 scale trade-off。

**W6 [共识]** Figure 2 仅展示 global allocation 但 §4.2 推荐 uniform

作为正文仅有的两张 figure 之一，Figure 2 的 framing 效果很强，但 uniform allocation 下 TEAL 在 MMLU 上系统性优于 KL。建议加入 uniform 曲线或在 caption 中明确说明。

**W7 [共识]** Abstract 第5句信息密度过高

约 60 词包含多层嵌套数字和条件，首次阅读几乎不可能理解。建议简化为 high-level takeaway。

**W8 [共识]** Conclusion 引用 BoolQ 但不在 Table 2

BoolQ 仅在 Appendix K=4 表中出现且 variance 极高 (std=11.5)，不应在 Conclusion 中引用。

---

### Minor（不影响接收）

- **M1**: Table 2 注释过多（†, ‡, *, ±, §），BCE 30% 使用 TEAL global 与其他行不一致
- **M2**: §3.5 deadzone margin ε=0.02 缺乏 justification
- **M3**: §4.3 BCE 2700 steps 与 KL 1000 steps wall-clock 接近 (~46 vs ~45 min) 需解释（BCE 无 dense forward pass）
- **M4**: "Adaptive Penalty Controller" 命名不准确——实际是 geometric doubling + deadzone，非经典 dual ascent
- **M5**: References 中 FastForward (arXiv:2602.00397) 如已被会议接收应更新
- **M6**: Limitations 未讨论 sequence length 对 predictor mask 质量的影响
- **M7**: Table 1 (Taxonomy) 中 SPON 归入 "Static × Coupled" 的合理性应在正文讨论

---

## Reviewer Consensus

以下问题两位 Reviewer 达成 **[AGREE]**：

1. **C1 因果声明过强** — 应降级为 transferability claim（R1-N1 + R2-W4）
2. **97.5% decomposition 不可靠** — 应替换为定性描述（R1-N2 + R2 交叉同意升级 Critical）
3. **MMLU/GSM8K 退化需更深分析** — Remove Valley 线索未追踪（R2-N2 + R1 borderline Must-Fix）
4. **Table 2 sparsity mismatch 不够显著** — 需更显著标注（R1-W2 + R2 AGREE）
5. **KL global 50% 下游缺 3-seed** — 标准不一致（R1-W4 + R2 AGREE）
6. **Figure 2 global/uniform 误导** — 需补充 uniform 曲线（R2-W2 + R1 AGREE）
7. **Abstract/Conclusion 写作问题** — 密度过高 + BoolQ 不当引用（R2-W3/W5 + R1 AGREE）
8. **研究问题有价值** — 训练目标如何影响 mask quality 是 under-explored 但重要的问题
9. **实验覆盖面远超同类工作** — 消融设计用心，可复现性好

---

## Reviewer Divergence

**分歧 1: Wall-clock speedup 的严重程度**
- **R2**: Critical (N1) — 作为 efficiency-motivated 工作，+6.4% 延迟且无加速证据是核心缺陷
- **R1**: Should-Fix (W1, REBUT) — 论文已定位为 analysis work；predictor masks 可 plug into TEAL kernel pipeline；如果将此升级为 Must-Fix，大量分析性论文都会因 "无端到端系统集成" 被拒
- **Director 判定**: **Warning** — R1 论证有力，论文的自我定位清晰且合理，但应在主文更显著说明 speedup 路径

**分歧 2: MaskLLM 区分度**
- **R2**: Critical (N3) — 核心 recipe 完全共享，3 个差异是应用场景差异非方法论创新
- **R1**: REBUT (Minor/Should-Fix) — contextual vs static masks 是 fundamental architectural difference；cross-layer allocation 是本文独有的；recipe 层面的共享不等于方法论重叠（类似 knowledge distillation 的标准 recipe）
- **Director 判定**: **Warning** — R1 的 REBUT 有效，contextual vs static 确实是本质差异；但论文应更诚实定位为 systematic empirical analysis

**分歧 3: K=4 at 50% 缺失的严重程度**
- **R1**: Should-Fix (W5) — 50% 是 coupling 贡献最大的区间，缺少 K=4 无法判断真实贡献
- **R2**: REBUT (不应为 Should-Fix) — 50% 是 capacity-limited regime，所有方法 downstream 接近 random，K=4 decomposition 在 noise floor 附近意义不大
- **Director 判定**: 保留为 **Warning**。R2 的 rebut 有道理但论文应解释原因

---

## Questions

1. **[R1-Q1]** "Reverse C1"——在 magnitude-based masks 上训练 KL（而非 BCE）结果如何？如果 KL coupling 在 magnitude targets 上也效果好，则弱化 "mask patterns are the driver" 声明。
2. **[R1-Q2]** 为何 50% 没做 K=4？是资源限制还是训练不稳定？
3. **[R1-Q3 / R2-Q1]** Remove Valley 可恢复 MMLU +3.3pp，为何不探索 task-aware allocation？这是低悬果实。
4. **[R2-Q3]** "14.5% PPL reduction" 基于 matched 28.5% sparsity——Table 2 呈现方式是否会让读者误读为 18.6%？
5. **[R2-Q5]** §3.6 声称 gradient coupling 发现 68% divergent masks，但 C1 说 mask patterns（而非 coupling）是 driver——两者关系需更清晰阐述。如果 coupling 主要用于 discover masks，是否可以 KL 训练后提取 masks 再用 BCE 部署？
6. **[R1-Q4]** 30% target λ 达 cap (5000) 但实际仅 28.5%（5% deviation）。提高 λ_max 能否逼近 30%？

---

## Missing References

1. **LaRoSA** (2025, arXiv:2507.01299) — Layerwise Rotated Sparse Activation，在 SwiGLU 模型上实现 wall-clock speedup，高度相关但未引用
2. **Geva et al. (2023)** "Dissecting Recall of Factual Associations" — 已在 bib 中但正文未引用，与 MMLU regression 讨论相关

---

## External Review (Stanford Agentic Reviewer)

**状态**: 已跳过（用户在审稿群中跳过了外部审稿请求）

---

## Visual Layout Check（非评分项）

**状态**: 完成但 Agent 报错（rate limit: "You've hit your limit · resets 6pm (UTC)"），无有效视觉审查发现。用户可在 rate limit 重置后重新触发。

格式合规检查由 R2 手动完成：
| 项目 | 状态 |
|------|------|
| 正文页数 | ✅ §1-§5 在第8页结束 |
| Limitations | ✅ p9，不计入页数，3个关键点 |
| Ethics | ✅ p9，简短适当 |
| 匿名化 | ✅ "Anonymous ACL submission" |
| Appendix 双栏 | ✅ ACL 格式 |
| 引用格式 | ✅ acl_natbib |

---

## Overall Assessment

**评分**: 3.0 (Findings)
**置信度**: 4/5

**R1**: 3.5 (Borderline Conference) — Soundness 3.5, Excitement 3.0
**R2**: 3.0 (Findings) — Soundness 3.5, Excitement 2.5
**Director 综合**: 3.0 (Findings)

**理由**: 论文的核心发现（KL distillation 优于 BCE 训练稀疏性预测器）可信且有实验支撑，实验设计的系统性和覆盖面是明显优势。但两个核心分析贡献（C1 target-swap ablation 和 97.5% signal-type decomposition）的 claim 强度超出实验证据——这两个声明出现在 Abstract、Introduction contributions list、和 Conclusion 的核心位置，是论文三大贡献中的两个。加之 MMLU/GSM8K 在所有测试规模上系统性逊于 training-free baseline TEAL，且缺乏 wall-clock speedup，整体贡献更适合 Findings 而非主会议。

**升级路径**: 如果 (1) N1/N2 的 claim 调整为更审慎的措辞，(2) 基于 Remove Valley 发现追踪 task-aware allocation，(3) 补充 K=4 at 50% 实验，论文有望升至 3.5 (Borderline Conference)。如进一步补充 wall-clock speedup 数据（即使仅一个 sparsity level），可达 4.0 (Conference)。

---

## Detailed Comments

### §1 Introduction
- Contribution list 第1条过长（4行），建议拆分为 per-layer decomposition 和 cross-scale evidence
- "14.5% over TEAL at matched sparsity" 的 "matched sparsity" 在此处首次出现但未解释，建议明确 (KL 28.5% vs TEAL 28.5%)

### §3 Method
- §3.5 Adaptive Penalty Controller: ε=0.02 的选择缺乏 justification；"adaptive" 命名可能误导——实际是 geometric doubling + deadzone
- §3.6 Gradient Analysis: 与 §4.4 C1 的关系需要更清晰阐述——§3.6 argue coupling 是优势来源，§4.4 argue mask patterns（而非 coupling）是 driver。当前叙事的矛盾是：coupling 的作用仅在于 training-time discovery 还是 inference-time maintenance？
- §3.7 Taxonomy: Table 1 有用但本身不构成 intellectual contribution；SPON 的 "Static × Coupled" 分类应在正文简要讨论

### §4 Experiments
- Table 2: 注释过多（5 种 footnote symbols）；BCE 30% 使用 TEAL global (†) 与其他行不一致且容易被忽略
- §4.3 Extended Training: BCE 2700 steps wall-clock 与 KL 1000 steps 接近 (~46 vs ~45 min) 需解释——BCE 不需要 dense forward pass，每步应更快
- §4.4 C1 Ablation: "suggests" hedging 是好的，但 Abstract 中的 "as the proximate quality driver" 措辞过于绝对
- §4.5 Per-Layer KL: "97.5%" 的精确数字与 Footnote 5 的 "not fully orthogonal" caveat 之间的显著性严重不对称；K=4 MMLU anomaly (>100% gap closure) 应在正文而非 Appendix 讨论

### §5 Conclusion
- 仅 2 句话 (~130 词)，信息密度过高
- 引用了 BoolQ (仅 Appendix, high variance) 但未引用 HellaSwag/PIQA (Table 11, stable)
- 完全没有提及 limitations (MMLU regression, no speedup, scale bounds)

### Appendix
- 19 页 Appendix 提供了充分补充，信息分配总体合理
- Appendix T (Constraint Analysis) 的发现（Remove Valley: MMLU +3.3pp）应在正文获得更多讨论，而非仅作为 supporting evidence