---
round: 25
review_mode: fresh
overall_score: 3.0 - Findings
timestamp: 2026-05-24T03:15:35.931618+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs

**Target Venue**: EMNLP 2026 (ARR May cycle)  
**Category**: Long Paper  
**Review Round**: 28 (fresh)  
**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）

---

## Summary

本文系统对比了 SwiGLU LLM 上下文稀疏性预测器的训练目标。核心方法：用 forward KL divergence 替代传统 BCE，通过 Gumbel-Sigmoid 松弛训练轻量级预测器（75.9M, <1% 参数量）。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL 预测器 PPL 比 TEAL 低 14.5%（8.81±0.02 vs 10.30，matched sparsity），跨架构验证（Mistral-7B -17.3%, Qwen-14B）确认泛化性。target-swap ablation (C1) 显示 KL 发现的 mask 模式可迁移到 BCE（PPL gap ≤0.79pp）。per-layer KL 分解尝试分离 signal type 和 coupling scope 的贡献。但知识密集型任务出现系统性退步（MMLU -5.2pp on 8B, GSM8K -20.1pp on 14B vs TEAL at same sparsity）。论文定位为 empirical study，不提供 wall-clock 加速。

---

## Strengths

**S1** [双方共识] **PPL 改善显著且跨架构一致**。14.5%（30%）到 50%（50%）的 PPL 改善在 LLaMA-8B、Mistral-7B、Qwen-14B 上复现，是一个实质性的经验发现。C4 OOD 评估进一步确认泛化性。

**S2** [双方共识] **实验覆盖面广**。3-seed 评估、5 种 loss variants（forward KL/reverse KL/JSD/BCE/MSE）、3 种架构（7B-14B）、2 种稀疏度、多种 allocation 策略、isocompute 对比。对于 empirical study 来说覆盖面高于多数同类工作。

**S3** [双方共识] **C1 target-swap ablation 有独立 insight 价值**。证明 KL 发现的 mask patterns（而非 gradient coupling 本身）是 PPL 优势的主要来源，为后续工作提供了 "先用 KL 找 mask，再用 BCE 训练" 的实用路径。

**S4** [双方共识] **诚实报告负面结果**。MMLU/GSM8K 回退、per-layer 分解的局限性、MSE 50% 的 catastrophic failure 等均如实报告。对 claim 的 hedging（"directional", "upper bound", "exploratory"）比多数论文更透明。

**S5** [双方共识] **可复现性良好**。训练细节充分（lr, schedule, GPU, batch size, steps, exp_id），承诺代码开源。Taxonomy（Table 1）提供了该领域的清晰组织框架。

**S6** [R1] **补偿网络冗余性发现有工程简化价值**。KL 预测器在两个稀疏度下均使 FastForward-style compensation (+67.2M) 冗余，减少推理开销。

---

## Weaknesses

### Must-Fix（影响接收决定）

**C1** [双方共识, critical] **Per-layer KL 分解存在根本性 train-inference mismatch，核心 decomposition claim 站不住脚**

K=1 per-layer KL 训练时每步只 mask 1/32 层，推理时 32 层同时 mask——这是无法通过实验设计消除的根本性 mismatch。K=1 (PPL 9.05) 与 E2E (8.81) 的 2.7% gap 被论文解读为 "signal type accounts for a substantial portion of PPL gap"，但此 gap 之所以小是因为 K=1 训练条件近似 dense（31/32 层完整）。

决定性证据：50% 下 K=1 PPL=34.85 vs E2E=11.84（2.94×），mismatch 灾难性放大；K=4 在 50% 更差（44.23 vs K=1 的 34.85），论文自己承认 "the decomposition is interpretable only at 30%"（§4.5）。K-curve 非单调（K=2 最差 10.75, K=16 最优 8.67），说明层间交互有复杂非线性效应。

论文已做了多项改进（标注 "upper bound"、"exploratory"、补充 K=2/8/16 3-seed K-curve），但 "may account for a substantial portion" 的措辞对于 admittedly exploratory 且仅在 30% 有效的分析仍然过强。per-layer update count confound（K=2 ~62 updates/layer vs K=8 ~250）也未解决。

*[跨轮追踪: R20-W1, 连续 9 轮被标记]*

**C2** [双方共识, critical] **下游知识任务（MMLU/GSM8K）系统性退步缺乏机制性解释**

KL 在所有模型/规模上系统性损害 MMLU 和 GSM8K：
- LLaMA-8B 30%: MMLU 40.7±1.3 vs TEAL 45.86（同 uniform allocation, -5.2pp）
- Qwen-14B 30%: GSM8K 32.0±5.2 vs TEAL 52.1（-20.1pp）
- Mistral-7B: MMLU tied, GSM8K reverses

论文排除了训练数据偏差（C4 控制），提出 forward KL mode-covering 稀释稀有激活假设，但无直接验证（如分析 KL mask 是否 prune 了 factual neurons）。Constraint analysis（remove valley → MMLU +3.4pp）说明 allocation pattern 有影响但非 mechanism 解释。跨 scale 退步暗示 structural limitation 但论文未追问 *why*。

对于声称改善稀疏预测质量的论文，PPL 改善与 downstream 退步的矛盾是核心张力。缺乏缓解方向讨论（如 hybrid loss、task-aware allocation）。

*[跨轮追踪: R20-N2, 连续 11 轮被标记]*

**C3** [双方共识, critical] **n=3 下 downstream metrics 统计功效严重不足**

- KL global 30% MMLU: 35.7±9.5pp (n=3)，95% CI ≈ [22.1, 49.3]——覆盖从 random chance 到 dense 的大部分范围
- Qwen-14B GSM8K: 32.0±5.2pp (n=3)，CV=16.3%
- TEAL 是 deterministic single-run，无方差信息，与 KL 的 CI 直接对比不对等

论文在 §4.2 承认 "95% CI for individual downstream tasks overlap"，在 abstract 已改用 "directional commonsense gains (n=3)"，但 conclusion 和 abstract 中仍报告具体的 gap 数值（-5.2pp, -20.1pp）作为确定性结论。增加 seed 数至 ≥5（或至少 upfront disclosure 14B 的计算预算限制）是必要的。

*[跨轮追踪: R24-W2, 连续 5 轮被标记]*

### Should-Fix（影响评分但不一票否决）

**W1** [双方共识] **C1 target-swap ablation confound 未充分控制**。s42 oracle 来自 non-seed-matched earlier training run；BCE+Gumbel (32.22) vs BCE (27.97) 显示 Gumbel 对 BCE 有害，使 C1 的 "target quality vs gradient coupling" 分离不够干净。s123/s456 seed-matched ≤1.18pp 部分缓解。

**W2** [双方共识] **MSE 50% baseline 不可信**。s123 仅达 5.1% sparsity（PPL=15,789），2/3 seed 失败。Table 4 虽有 § 标注但仍在主表中，有误导性。

**W3** [双方共识] **30% 下缺少 BCE isocompute (2700 steps) 对比**。BCE isocompute 仅在 50% 有 3-seed，无法确认 30% 下 KL 对 BCE 的优势在更多训练步数后是否缩小。

**W4** [双方共识] **主评估指标单一**。所有主要比较基于 WikiText-2 PPL（与训练数据 WikiText-103 同源）。C4 OOD 30% 仅 2-seed，uniform 3-seed CV=6.3% vs in-domain 0.2%。

**W5** [双方共识] **Conclusion 仅 2 句话**。对于涉及复杂 trade-off（PPL vs downstream, signal type vs coupling, commonsense vs knowledge）的论文，缺乏 broader implications、future directions、knowledge regression 解决方向的讨论。

**W6** [R2, R1 partial agree] **Contribution C3/C4 标注 "Practical" 在无 wall-clock 加速下有误导性**。Predictor +6.4% latency，无 sparse kernel 支持。论文已多处声明无加速，但 contribution 标签应改为 "Analytical" 或 "Empirical"。

**W7** [R2, R1 partial agree] **训练规模极小（1000 步, ~8.2M tokens）**。虽然 convergence analysis 显示 step 800 后饱和、isocompute 分析支持 KL 优势非因训练不足，但更大规模下相对优势是否保持未验证。

---

## Reviewer Consensus

以下问题双方达成完全共识（标注 [AGREE]）：

1. [AGREE] Per-layer KL 分解的 train-inference mismatch 是根本性问题，仅在 30% 下 "interpretable"，50% 下完全失效
2. [AGREE] 知识任务退步是系统性的且缺乏机制性解释，C4 控制排除数据偏差后问题更 structural
3. [AGREE] n=3 统计功效不足，高方差下游指标的 CI overlap 使多数比较无统计意义
4. [AGREE] PPL 改善显著且一致，是论文的核心实质性贡献
5. [AGREE] C1 target-swap ablation 有 insight 价值但存在残余 confound（soft→hard binarization, non-seed-matched oracle）
6. [AGREE] Conclusion 过短，缺 future directions
7. [AGREE] Overall 3.0 (Findings)

---

## Reviewer Divergence

以下问题存在分歧（均为严重程度分歧，非方向性分歧）：

1. **MaskLLM novelty 区分**
   - R2: Critical。MaskLLM 共享 recipe-level principle，contextual vs static 区别缺实验验证，"KL > BCE" 符合信息论直觉不够 surprising
   - R1: Not critical。MaskLLM 是 static N:M sparsity，与 contextual unstructured 是不同范式，要求跨范式直接对比不合理
   - **Director 判断**: Should-fix。R1 关于不同范式的论点成立——直接实验对比不可行。但 R2 关于 insight novelty 的质疑也合理——论文应更清晰地阐述为什么 contextual 下的 KL 行为可能与 static 下 qualitatively 不同

2. **无 wall-clock 加速的严重程度**
   - R2: Critical。+6.4% latency 且 "Practical" 标签 misleading
   - R1: Should-fix。论文已充分 disclaimer，这是 empirical study 不是 systems paper
   - **Director 判断**: Should-fix。论文的 self-positioning 已足够清晰，但 "Practical" 标签确实应修改

3. **Excitement 评分**
   - R1: 3/5（C1 ablation 和广覆盖面有价值）
   - R2: 2.5/5（核心发现 expected，无实际加速，退步限制启发性）
   - **Director 判断**: 2.5-3/5。PPL 改善本身 expected，但 mask divergence pattern 和 C1 transferability 有 non-trivial insight

---

## Questions

1. TEAL uniform 30% MMLU 45.86 显著高于 KL 40.7±1.3。对实际部署，TEAL 在 knowledge-critical 场景是否更优？论文应明确 use-case dependent recommendation。
2. C4-trained predictor PPL 更差（11.55 vs 8.82）但 downstream 基本不变（MMLU 40.0% vs 40.7%）——这是否表明 WikiText-103 的文本特性有助于学习更好的稀疏 pattern？
3. 20-25% sparsity 下 downstream gap 是否更小？Figure 3 显示此区间 PPL gap 收窄。
4. ShadowLLM 在 Table 1 归入 "Per-token × Intermediate (MSE)" 但其使用 attention-based routing——分类是否准确？
5. Per-layer KL 的 per-layer update count confound（K=2 ~62/layer vs K=8 ~250/layer）是否可以通过 epoch-normalized training 控制？

---

## Missing References

**双方共识遗漏**：
- ActTail (2026, arXiv:2603.12272)：基于 Heavy-Tailed Self-Regularization 的全局激活稀疏性分配
- WiSparse (2026, arXiv:2602.14452)：Weight-Aware Mixed Activation Sparsity

**R1 建议、R2 反驳**（weight pruning 方法，与 activation sparsity prediction 相关性有限）：
- LoRAShear, ZipLM

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置，不适用。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warning, 22 info）。

**Warnings**：
1. Abstract 视觉长度偏长，可能接近 200 words 上限（实测 ~190 words，合规）
2. Page 7 三张表格（Table 2/3/4）集中在同一页，视觉密度偏高

**格式合规**：
- 正文 8 页 ✓
- Limitations 在正文（page 9）✓
- 匿名（"Anonymous ACL submission"）✓
- 引用格式 ACL natbib ✓
- 无 margin 溢出 ✓
- Display items 密度 0.88/页，正常 ✓

---

## Overall Assessment

**Overall**: 3.0 (Findings)

**置信度**: 4/5（双方 Reviewer 均 4/5，核心问题高度共识）

### 维度汇总

| 维度 | R1 | R2 | 合议 |
|------|-----|-----|------|
| Soundness | 3/5 | 3.5/5 | 3/5 |
| Excitement | 3/5 | 2.5/5 | 2.5/5 |
| Reproducibility | 4/5 | 4/5 | 4/5 |
| Overall | 3.0 | 3.0 | 3.0 |

### 理由

本文做出了一个有价值的经验贡献：系统证明 output-distribution KL 在稀疏预测器的 PPL 表现上显著优于 BCE/MSE，且 KL 发现的 mask 模式可迁移（C1）。实验覆盖面广，报告透明诚实。

三个 critical 问题阻止主会议推荐：

**(1) 核心分析贡献（per-layer KL decomposition）方法学缺陷**。该分解存在无法消除的 train-inference mismatch（1/32 vs 32/32 layers masked），仅在 30% 有效且是 upper bound。如果去掉这个 decomposition contribution，论文退化为 "KL 在 PPL 上更好但 downstream 更差" 的实验报告。

**(2) 知识任务系统性退步未解决**。MMLU/GSM8K 在所有模型/规模上退步，C4 控制排除了数据偏差但 mode-covering 假设无直接验证。对于声称改善稀疏预测质量的论文，这构成核心方法有效性的质疑——PPL 改善未转化为 deployment-relevant metrics 的提升。

**(3) 统计功效不足**。n=3 下高方差 downstream metrics（MMLU σ=9.5pp）的 95% CI 覆盖从 random chance 到 near-dense 的范围，多数下游比较不具统计意义。

当前贡献——"KL 训练在 PPL 上更好但知识任务更差" + "mask 模式可迁移" + "补偿网络冗余"——达到 Findings 的接收标准（soundness sufficient, reproducible, some insight value），但 excitement 和 impact 不足以推荐主会议。如果作者能 (a) 对 knowledge regression 提供机制性证据或缓解方案，(b) 将 decomposition claim 进一步弱化或提供新的控制实验，(c) 增加 downstream seed 数，论文在下一轮有望达到 conference 水平。

---

## Detailed Comments

### Abstract
- ~190 words 合规，但信息密度极高
- "directional commonsense gains (n=3)" 适当 hedged
- "MMLU −5.2pp on 8B; GSM8K −20.1pp on 14B" 量化了退步，但在 n=3 高方差下这些数字的确定性被高估
- "may account for a substantial portion" 对 exploratory analysis 仍偏强

### Introduction
- 数字过多（~20 个），信息过载（R2 W4，R1 disagree as style preference）
- Gradient analysis (§3.6) 自称 "suggestive" 但在 contributions list 中被隐含列为核心贡献——应区分 verified empirical findings 和 suggestive analysis
- Contributions list 中 "Practical" 标签在 +6.4% latency 下应改为 "Analytical"

### Method (§3)
- 7 个 subsection (~2.5 页) 对 empirical study 定位稍重，但保证了 reproducibility
- Gumbel-Sigmoid vs STE 对比 convincing（PPL 15.77 → 11.79, 33.8% improvement）
- Geometric penalty schedule: ε=0.02 缺 sensitivity analysis（R1 W4，R2 认为低优先级）
- Forward KL vs reverse KL 的理论动机（mode-covering for false negatives）清晰

### Experiments (§4)
- Table 2: 6 列数据充实，但 HellaSwag/PIQA 仅在 Appendix（R2 W6）
- Table 2 中 TEAL 是 deterministic single-run vs KL 3-seed 对比不对等
- §4.2 Knowledge-Task Regression: C4 控制和 constraint analysis 是好的尝试，但未达到 mechanism-level 解释
- §4.3 Isocompute: BCE 2700 steps 仅在 50%，30% 缺失
- §4.4 C1 ablation: s42 non-seed-matched oracle 是历史遗留问题
- §4.5 Per-layer KL: "Exploratory Decomposition" 的标注是诚实的，但 "may account for a substantial portion" 仍过强
- §4.6 Cross-Architecture: PPL 泛化确认，但 Qwen-14B downstream std=5.2pp

### Conclusion (§5)
- 仅 2 句话严重不足
- 缺：knowledge regression implications、future directions（hybrid loss, task-aware allocation）、method limitations summary、broader impact

### Limitations
- 3 个点覆盖合理（sparsity sweet spot, knowledge regression, evaluation scope）
- 缺：仅验证 SwiGLU 架构、训练规模极小、无实际部署验证

### Appendix
- 25 个 section (A-Y, ~11 页)，认知负担大但内容充实
- 关键数据（HellaSwag/PIQA downstream, K=4 full downstream）适合部分提升到主文
- AI usage disclosure (Appendix Y) 合规