---
round: 14
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-20T06:52:24.910531+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 15 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May 2026 cycle, deadline 2026-05-25)
**审稿编排**: 2 Reviewers — R1 (方法严谨性 + 实验完整性), R2 (新颖性 + 完整性 + 写作质量)
**交叉轮数**: 1 轮（关键问题已收敛）

---

## Summary

本文提出用 forward KL 蒸馏替代 binary cross-entropy (BCE) 训练 SwiGLU LLM 的上下文稀疏性预测器。在 LLaMA-3.1-8B 上，KL 预测器（75.9M 参数，<1% base）在 30% sparsity 下将 TEAL 的 perplexity 从 10.82 降至 8.81（非匹配 sparsity 下 19%，匹配 sparsity 下 14.5%）。Target-swap ablation (C1) 证明 KL 发现的 mask pattern（与 magnitude mask 偏差 46-68%）是推理阶段质量的近端驱动因素。论文提出 "coupling alignment" 概念组织 sparsity prediction 方法的二维分类，但两位 Reviewer 均认为该概念缺乏形式化定义且过度包装已知原理。方法的实际可用范围窄——50% sparsity 下所有方法 downstream collapse，30% 下 downstream 为 task-dependent（commonsense 赢 4/4，knowledge 输 0/2）。

---

## Strengths

**S1. C1 Target-swap ablation 设计精巧且有说服力** [R1 S2, R2 S1, 共识]
将 mask 质量与训练机制解耦：BCE 在 KL-derived targets 上训练，复现 KL 性能（50% Δ≤0.79pp，30% retrained Δ≤1.18pp）。直接回答了"是 mask 更好还是训练过程更好"的因果问题。这是全文最有价值的实验证据。

**S2. 实验诚实度高** [R1 S4, R2 S2, 共识]
坦承 50% downstream collapse、cross-architecture 为"preliminary single-seed"、缺乏 wall-clock speedup、OOD 过拟合。在 MMLU 和 GSM8K 上的负面结果如实报告。

**S3. Multi-seed 评估规范 + Appendix 充实** [R1 S3, R2 S3/S4, 共识]
核心实验 3-seed（PPL CV=0.2%），6 downstream tasks。Appendix A-P 涵盖 bottleneck sensitivity、temperature schedule、training convergence、OOD、compensation redundancy 等，reproducibility 支持好。超参完整列出（§4.1）。

**S4. 问题定位精准** [R1 S1]
首次系统质疑"为什么 sparsity predictor 都用 BCE"，填补 Table 1 中 Per-token × Coupled 的空白。

**S5. SNR 分析诚实** [R1 交叉回应]
SNR figure (Appendix H) 用完整 1000 步 14-checkpoint 数据，诚实呈现 BCE SNR 2.3× 高于 KL 但 KL 仍产生更优 mask，支持 "target alignment not gradient clarity" 的非直觉结论。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1** [critical, 共识] **Coupling alignment 概念过度包装，缺乏形式化定义**
- R1-N1 + R2-N2，交叉后双方 AGREE
- §3.7 定义为"训练损失是否优化一个跨层组合的量"，Conclusion 首句将其称为"the decisive factor"——但本质上是"end-to-end training outperforms component-wise training when components interact"这一深度学习基本原理的重新陈述
- 论文未提供 composability 的形式化度量，未测试 intermediate coupling 目标（如 hidden-state KL），Taxonomy (Table 1) 填充空格不构成理论发现
- C1 ablation 证明 mask quality 是 proximate driver、gradient coupling 仅在 discovery 阶段必要——这与 "coupling alignment is decisive" 的结论存在内部张力
- **修复方向**: 降低理论抱负，定位为"已知原理在 sparsity prediction 场景的经验验证"；或补充 hidden-state KL 对照实验

**N2** [critical, 共识] **Abstract headline "19% PPL improvement" 在非匹配 sparsity 下报告**
- R1-N2 + R2-W3，交叉后双方 AGREE
- KL actual 28.5% vs TEAL ~30%。匹配 sparsity (28.5%) 下改善为 14.5%（§4.2 括号内承认但 Abstract 未修正）
- Abstract 选择性呈现：突出 ARC +4.4pp、HellaSwag +7.8pp，MMLU -5.2pp 仅给标签，完全未提及绝对退化幅度（MMLU dense 65.27%→sparse 40.7%）
- **修复方向**: Abstract 使用 14.5% 或明确标注 sparsity 差异；加入 MMLU 绝对退化

**N3** [critical, 共识] **实际可用 regime 仅 30%，且 downstream 为 task-dependent**
- R1-N3 + R2-W1，交叉后双方 AGREE
- 50% sparsity：所有方法 MMLU≈28%（≈random），GSM8K<2.2%，capacity-limited collapse
- 30% sparsity：commonsense 4/4 win (ARC +4.4pp, WG +3.9pp, HS +7.8pp, PIQA +2.2pp)，knowledge 0/2 lose (MMLU -5.2pp, GSM8K -1.3pp)。TEAL 在 MMLU/GSM8K 上更好且无需训练
- KL predictor 增加 6.4% latency overhead，无实际 wall-clock speedup（无 sparse kernel support）
- 方法的 unambiguous advantage 仅在"30% × PPL"这一窄窗口
- **修复方向**: Abstract/Intro 更平衡呈现 task-type split；分析 forward KL mode-covering 与 knowledge tasks 的 tradeoff

**N4** [critical, R2 critical + R1 partial rebut] **与 MaskLLM 的新颖性边界不够清晰**
- R2-N1 critical，R1 REBUT（结构性差异成立），R2 部分接受
- MaskLLM (NeurIPS 2024) 已使用 frozen weights + KL + Gumbel + learnable masks 的完整框架
- R1 论证三个结构性差异（sparsity type、mask generation、allocation）是实质性的而非 domain 差异；但论文未明确论证为什么 global allocation 场景让 KL vs BCE 差异更 pronounced
- **修复方向**: §2 加入"why global allocation amplifies KL-BCE gap"的论证；讨论 MaskLLM 中是否存在类似 gap

### Should-Fix（影响评分但不一票否决）

**W1** [warning, 共识] **跨架构/跨规模证据过薄**
- R1-W1 + R2-W2，交叉后 AGREE
- Mistral-7B 和 Qwen-14B 均 single seed
- 14B 结果反转核心优势：GSM8K -20pp（32.1±5.2% vs TEAL 52.1%），MMLU -2.79pp
- Abstract/Conclusion 将 cross-architecture 作为 contribution claim，与 "preliminary single-seed" 证据强度不匹配

**W2** [warning, 共识] **BCE+Gumbel 交互效应未量化**
- R1-W4，R2 AGREE
- BCE+Gumbel (32.22) 比 standard BCE (27.97) 差 4.25 PPL
- §4.5 的 additive decomposition（loss effect 5.1× relaxation effect）假设独立性，但交互效应的存在说明不独立
- 需补 BCE+STE 对照（控制 relaxation），或正式承认 KL×Gumbel 正向交互

**W3** [warning, 共识] **Training data 单一性 + OOD downstream 未评估**
- R2-W4 新提出，R1 AGREE
- 所有 predictor 仅在 WikiText-103 训练 1000 步
- C4 OOD 仅报告 PPL 未报告 downstream；C4 cross-seed CV=6.3% vs WikiText-2 CV=0.2%（30× 增大）
- Limitations 已承认"partially overfits to training-domain activation patterns"但未补充 OOD downstream 数据

**W4** [warning, 共识] **MSE baseline λ_max 不匹配 (1000 vs 5000) 且 single seed**
- R1-W2 + R2-M2，交叉后 AGREE
- Appendix G 已补 MSE 配置（同 Gumbel/optimizer/data），但 λ_max 差异未解释
- 50% gap (229 vs 23.9) 足够大，seed sensitivity 不影响结论；30% (20.4 vs 10.8) 需确认

**W5** [warning, R1 提出] **梯度分析 (§3.6) 缺乏定量支撑**
- §3.6 定性推导正确（BCE gradient decomposed, KL gradient coupled through downstream Jacobian）
- SNR 分析 (Appendix H) 有效但不能区分"gradient direction 更好"和"gradient 更 coupled"
- 缺少直接度量 coupling 强度的实验（如 cross-layer gradient correlation）

**W6** [warning, R1 提出] **Adaptive penalty controller 在 30% 时 λ 触顶 5000**
- Appendix C Table 10：30% target 时 λ=5000 (cap), actual=28.5% (5% deviation)
- 控制器在最实用 regime 表现最差——如果目标是 25% 可能完全失效

---

## Reviewer Consensus [AGREE]

1. Coupling alignment 是已知原理的重新包装，需降级 claim 或补充形式化 [R1-N1 + R2-N2]
2. Abstract 19% headline 在非匹配 sparsity 下报告，构成选择性呈现 [R1-N2 + R2-W3]
3. 50% downstream collapse + 30% task-dependent wins = 实用 regime 过窄 [R1-N3 + R2-W1]
4. Cross-architecture 证据不足以支撑 contribution claim [R1-W1 + R2-W2]
5. C1 target-swap ablation 是全文最有价值的贡献 [R1-S2 + R2-S1]
6. 实验诚实度高，Limitations 讨论充分 [R1-S4 + R2-S2]

## Reviewer Divergence [REBUT → 部分收敛]

1. **MaskLLM 新颖性** — R2 认为核心框架已被 MaskLLM 覆盖 (Excitement 2.5/5)；R1 认为 activation sparsity + predictor + global allocation 是结构性不同问题 (Excitement 3.5/5)。交叉后 R2 部分接受结构性差异但维持 critical。**Director 判断**: R1 的结构性差异论证有效，但论文确实需要更 explicit 地论证新颖性边界——列为 N4 (critical)。
2. **Overall 评分** — R1: 3.5 (Borderline Conference)，R2: 3.0 (Findings)。分歧主要在 excitement。

---

## Questions for Authors

1. [R1-Q1] 反向 C1：用 KL 训练在 magnitude-based oracle targets 上性能如何？测试 KL coupled gradient 在 suboptimal targets 上是否仍有优势。
2. [R1-Q3 + R2-Q2] Forward KL 的 mode-covering 是否解释了 knowledge-intensive tasks 的退化？是否考虑过 task-specific 的 KL 方向选择？30% 下有无方法恢复 MMLU 差距？
3. [R2-Q1] MaskLLM 中 KL vs BCE 的 PPL gap 是多少？与本文 2.4× gap 可比吗？
4. [R2-Q3 + R1-W4] Gumbel 对 KL 有利但对 BCE 有害——能否量化 KL×Gumbel 的交互效应？BCE+STE 的结果？
5. [R1-Q2] λ_max 提高到 50000 能否达到 30% actual sparsity？PPL 是否会因过强惩罚恶化？

---

## Missing References

- **共识**: §2 line 172-173 "All prior predictor-based methods use decomposed or intermediate objectives" 需限定为 "for activation sparsity prediction"（MaskLLM 已在 weight sparsity 用 KL）
- **R2 提出**: "A Sparsity Predicting Approach via Activation Pattern Clustering" (Dhar et al., 2025); "Universal Properties of Activation Sparsity in Modern LLMs" (arXiv:2509.00454)
- **R1 提出**: Wortsman et al. (2023) training stability（tangentially related）; quantization+sparsity 交叉工作（论文未讨论）
- **引用修复**: xu2026spon bib year=2026 应为 2025 (ICML 2025)；de2024griffin OpenAlex 未找到，需确认 venue 信息

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（2 warning, 3 info, 0 critical）。

| 严重度 | 位置 | 发现 |
|--------|------|------|
| ⚠️ warning | Pages 1-4 | 连续 4 页纯文本无 display item（figure/table），Figure 1 在 page 3 首次引用但漂移到 page 5。建议将 Figure 1 提前至 page 2-3 |
| ⚠️ warning | Page 17 | Figure 7 仅占页面 1/3，上方 2/3 空白。建议合并或补充内容 |
| ℹ️ info | Page 5 | Figure 1（架构图）为单栏宽度，文字接近可读性下限，考虑 figure* 全宽 |
| ℹ️ info | Page 13 | 单页 4 个表格（Tables 7-10），密集但未溢出，附录可接受 |
| ℹ️ info | Page 8 | Figure 2 折线图仅 2 条线，建议增加 marker 形状差异确保灰度打印可辨 |

---

## Overall Assessment

**评分: 3.0 / 5 — Findings**
**置信度: 4 / 5**

**理由**:

本文做出了有价值的实证贡献——C1 target-swap ablation 精巧地隔离了 mask 质量的因果作用，"KL-derived masks diverge 46-68% from magnitude yet produce lower PPL"是非直觉且有启发性的发现。实验设计规范（3-seed、6 downstream tasks、全面 ablation），科学诚实度高。

但论文有四个结构性问题阻止其达到主会议水平：

1. **理论贡献过度包装**: "Coupling alignment"是对已知原理的重新陈述而非新发现，但论文将其作为核心贡献。如果降级为经验验证，论文就缺少除 C1 ablation 之外的概念性贡献。

2. **新颖性边界模糊**: MaskLLM 已使用 KL+Gumbel+frozen weights+learnable masks 的完整技术栈。虽然 activation sparsity + predictor + global allocation 是不同问题（R1 论证有效），但论文未充分论证为什么这些差异让 contribution 不可从 MaskLLM 直接推导。

3. **实用 regime 过窄**: 50% downstream collapse，30% downstream task-dependent（knowledge tasks 输 TEAL），无 wall-clock speedup。方法的 unambiguous advantage 仅在"30% × PPL"窄窗口——用户为何不直接用 training-free TEAL？

4. **Headline 数字准确性**: Abstract 19% 在非匹配 sparsity 下报告，选择性呈现 downstream 结果。

R1 评分 3.5 (Borderline Conference)，R2 评分 3.0 (Findings)。综合考虑：如果修复 headline 准确性、降低 coupling alignment claim、更 explicit 论证 vs MaskLLM 的新颖性，论文可升至 3.5。当前版本适合 Findings track。

---

## Detailed Comments（逐节）

### Abstract
- "19% relative to TEAL" → 使用匹配 sparsity 14.5% 或标注 sparsity 差异
- "moderate downstream degradation" → 不准确：MMLU -24.6pp（dense→sparse）不是"moderate"
- "improving commonsense reasoning (ARC +4.4pp, HellaSwag +7.8pp) while knowledge-intensive benchmarks (MMLU −5.2pp) favor TEAL" → 数字选择性：应加入绝对退化或更平衡表述
- "Preliminary single-seed evaluation on Mistral-7B-v0.3 and Qwen-2.5-14B" → 适当降调，Conclusion 也应一致

### §1 Introduction
- Line 8: MaskLLM 讨论应更早且更 explicit——当前读者到 §2 才了解最近的 KL-based 先例
- Line 94: "primarily an empirical study" 与 §3.6-3.7 的理论抱负（gradient analysis + coupling alignment taxonomy）定位不一致。建议选择一个方向
- Contributions list: 第 4 条 "Analysis of allocation-to-downstream interactions at 7-14B" 应注明 "preliminary single-seed"

### §3 Method
- §3.5: λ 在 30% 触顶 5000 → 讨论 sensitivity to λ_max
- §3.6: "suggestive" hedge 适当，但随后 §3.7 将 coupling alignment 提升为 "decisive factor"，语气跳跃
- §3.7: 需要形式化定义或明确降级为描述性分类

### §4 Experiments
- Table 2: MSE single seed 行应标注
- §4.2: Task-type split 分析良好，但 Abstract 未反映
- §4.4 C1: 最有价值的贡献。s42 oracle 来自不同 run 的 confound 已通过 retrained seeds (s123/s456) 缓解
- §4.5 Table 4: BCE+Gumbel 行需要更 explicit 的交互效应讨论；additive decomposition caveat
- §4.6: Cross-architecture 结果应标注 single-seed limitation in section title 或 opening sentence

### Limitations
- 内容全面，科学诚实度高
- 建议增加：(1) OOD downstream 评估缺失；(2) training data 单一性对 predictor generalization 的影响

### References
- xu2026spon: bib year 2026 → 2025
- de2024griffin: 确认 venue 信息
- §2 line 172-173: 限定范围为 "for activation sparsity prediction"