---
round: 19
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-22T13:20:08.575980+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 21 审稿报告（Fresh Review）

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs
**Venue**: EMNLP 2026 (ARR May cycle, deadline 2026-05-25)
**Reviewers**: R1 (方法严谨性 + 实验设计) + R2 (新颖性 + 完整性 + 写作)
**模式**: Fresh review (无上轮记忆)

---

## Summary

本文研究用 KL 散度蒸馏替代 BCE 训练 SwiGLU LLM 的上下文稀疏预测器。在 LLaMA-3.1-8B 上 30% 稀疏度下，KL predictor（75.9M params, <1% base）将 TEAL 的 PPL 降低 14.5%（matched sparsity），并在 Mistral-7B（3-seed, -17.3%）和 Qwen-2.5-14B 上验证了 PPL 优势的跨架构泛化性。论文提出 signal type × coupling scope 的 2D 分类框架，通过 target-swap ablation（C1）和 per-layer KL 对照实验分析 mask quality 与 gradient coupling 的贡献。然而，论文在知识密集型任务上系统性输给 training-free baseline (TEAL)，且无实际 wall-clock 加速。

---

## Strengths

**S1. Target-swap ablation (C1) 设计精巧且证据充分。** BCE 在 KL-derived masks 上训练后 PPL 与 KL predictor 一致（max Δ≤1.70pp at 30%, 3-seed; ≤0.79pp at 50%），有力支持 mask patterns 而非 gradient coupling 作为 PPL-level 质量驱动因素。论文已适当使用 "suggests" 而非 "confirms"。(Table 3, §4.3) **[R1-S3, R2-S1: 共识]**

**S2. 全面的多种子消融实验 + 诚实的不利结果报告。** Table 4 覆盖 8 种配置（5 loss × 2 relaxation × 2 coupling scope），3-seed 评估贯穿全文（PPL σ=0.02）。MMLU/GSM8K 退化在 Abstract、§4.2 Task-Type Split、Limitations 中如实报告，未选择性隐藏。(Table 2, Table 4) **[R1-S2, R2-S2: 共识]**

**S3. 2D taxonomy 提供有用的组织框架。** Signal type × coupling scope 将 DejaVu/ShadowLLM/FastForward/SPON/本文放入统一坐标系，per-layer KL decomposition 提供定量填充。(§3.7, Table 1, Appendix L) **[R1-S1, R2-S3: 共识]**

**S4. 跨架构验证。** Mistral-7B-v0.3 (GQA+sliding window) 3-seed PPL -17.3%；Qwen-2.5-14B PPL 泛化但诚实报告 GSM8K -20pp regression。PPL advantage ratio 跨架构一致 (within 8% at ≤50%)。(§4.6, Tables 12-13) **[R1-S4, R2-S4: 共识]**

**S5. 训练效率门槛低 + 可复现性高。** 单 GPU ~45min，1000 steps，predictor <1% base params。超参/架构/评估细节充分（bottleneck/temperature/steps sensitivity in Appendix B）。 **[R1-S5, R2 Reproducibility 4/5]**

---

## Weaknesses

### Must-Fix（影响接收决定）

**W1 [Critical] 无实际推理加速，实用价值存疑。**
Pipeline 增加 6.4% latency overhead (126.78 vs 119.11 ms/fwd, Table 5)。Unstructured element-wise masks 无法转化为 wall-clock speedup。论文定位为 "primarily an empirical study"（§1），但此 disclaimer 位于括号内过于隐蔽。Introduction 叙事（"learned sparsity predictors"、"inference allocates budgets globally"）仍暗示效率目标。
**[R1-N1 Critical + R2-N2 Critical: 完全共识]**

**W2 [Critical] 与 MaskLLM 的 recipe 层面新颖性区分不足。**
Frozen weights + KL divergence + Gumbel relaxation + learnable masks 的核心组合在 MaskLLM (Fang et al., 2024, NeurIPS) 中已建立。论文在 §2 承认 "shares the recipe-level principle" 并指出 static N:M vs dynamic per-token 差异，但 (a) 未实验量化此差异（如在 activation sparsity 设定下复现 MaskLLM learnable-mask variant）；(b) 分析框架（2D taxonomy）的概念创新幅度有限。论文更接近 "MaskLLM applied to activation sparsity + post-hoc analysis"。
**[R2-N1 Critical + R1 交叉 AGREE]**

**W3 [Critical] "97.5% signal type" claim 基于非正交分解 + confounded K=1 设置。**
Per-layer KL (K=1) 训练 mask 1/32 层但推理 apply 全部 32 层，train-inference mismatch 与 coupling scope 混淆。§4.5 脚注承认 "not fully orthogonal"，但 Abstract 和 Conclusion 引用 "up to 97.5%" 时无 caveat。K=4 pilot 仅 single-seed，MMLU 反常结果（43.5 超过 E2E 40.7±1.3）和 GSM8K 负向 gap closure (-6.8%) 无法排除随机波动。Abstract "reveals task-dependent downstream structure" 对单种子结果过于自信。
**[R1-N2 Critical + R2-W1/W2 Major: 共识升级 Critical]**

### Should-Fix（影响评分）

**W4 [Major] MMLU/GSM8K 系统性退化跨架构一致，framing 偏重 PPL。**
8B MMLU -5.2pp, 14B GSM8K -20pp (σ=5.2pp), Mistral MMLU tied (43.3 vs 43.5)。KL 在知识密集型任务上系统性输给 training-free baseline (TEAL)，限制实用价值。Abstract/Introduction 以 PPL 改善为主叙事，Conclusion 以 "task- and scale-dependent" 回避。Per-layer sparsity 分析（L22-L28 at 48-57%, L14-L18 protection valley）仅为 correlational 证据——未通过 per-layer sparsity constraint 实验验证因果链。
**[R1-N3 Major + R2-W4: R2 同意核心批评但建议从 Critical 降为 Major。Director 判定 Major——论文已在 §4.2/Limitations 中报告，但 Conclusion 措辞不够直接。]**

**W5 [Major] C1 target-swap ablation 的 trajectory confound。**
Oracle masks 从特定 KL 训练轨迹提取（s42 来自 earlier run, Table 3 footnote）。3-seed 一致性（≤1.70pp）提供部分 robustness 证据，Appendix O 讨论了 trajectory 依赖。但 C1 仅证明好 masks 可 transfer，未证明 KL 是发现好 masks 的唯一/最佳途径。论文已适当使用 "suggests"——hedging 改善被两位 reviewer 认可。
**[R1-W1 Major + R2 AGREE]**

**W6 [Major] WikiText 同分布评估 + C4 OOD 覆盖不足。**
WikiText-103 训练 → WikiText-2 评估均来自 Wikipedia。C4 OOD 30% 仅 2-seed global，cross-seed variance 急剧增大（CV 6.3% vs 0.2%），seed 42 异常偏高（18.22 vs 16.37）。Limitations 已提及但未量化域敏感性的 practical implications。
**[R1-W2 Major + R2 AGREE]**

### Minor

**W7 [Minor] Sparsity mismatch 在主表中不够显著。** Table 2 中 KL 实际 28.5% vs TEAL 29.3%。Abstract 引用 matched 14.5% 而非主表 19%。Footnote + Appendix C 信息完整但正文显著性可提升。**[R2-W3, R1 REBUT 但同意可改进]**

**W8 [Minor] 缺少同类方法参考对比。** 论文控制变量比较训练目标（KL/BCE/MSE），R-Sparse/CATS 架构差异会混淆变量。但补充参考数字会增强 positioning。**[R2-W5, R1 partial REBUT]**

**W9 [Minor] MSE baseline seed 稳定性。** Seed 123 灾难性失败（PPL=15,789, 5.1% sparsity）。R2 认为 instability 本身是 finding，配置差异（λ_max=1000）有工程合理性。但缺 λ_max grid search。**[R1-W3, R2 REBUT]**

**W10 [Minor] 符号冲突：g^(ℓ) (gate activation, Eq.1) vs g1/g2 (Gumbel noise, Eq.4)。** 建议 Gumbel noise 改为 ε1, ε2。**[R1-W5, R2 AGREE]**

**W11 [Info] Figure 2 仅展示 global allocation 但 30% 时推荐 uniform。** 图表与结论 allocation 策略不一致。**[R2-M4]**

**W12 [Info] Introduction wall-clock disclaimer 位于括号内，过于隐蔽。** **[R2-M1]**

**W13 [Info] Table 2 注释过长（6行），信息密度过高。** **[R2-M2]**

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 [AGREE]：
1. **无 wall-clock 加速**是最根本的实践性缺陷 (Critical)
2. **97.5% signal type claim** 基于 confounded 非正交分解，Abstract/Conclusion 缺 caveat (Critical)
3. **K=4 pilot 单 seed** 不足以支撑推广，反常结果未排除 (Critical)
4. **MaskLLM recipe 重合**限制方法创新幅度 (Critical)
5. **MMLU/GSM8K 退化**需要更 balanced 的 framing + causal verification (Major)
6. **WikiText 同分布评估**引入偏差 (Major)
7. **C1 trajectory confound** 部分缓解但未根本解决；hedging 改善被认可 (Major)
8. **Per-layer starvation 假说**缺因果验证——per-layer sparsity constraint 实验是自然 follow-up (Major)

## Reviewer Divergence

以下问题存在分歧但已通过交叉讨论解决：

1. **Sparsity mismatch (R2-W3 Major vs R1 REBUT)**: Director 判定 **Minor**——footnote + matched-sparsity appendix 信息完整，但正文显著性可提升。
2. **MSE baseline 公平性 (R1-W3 Minor vs R2 REBUT)**: Director 判定 **Minor (Info-leaning)**——instability 本身是 finding，配置差异有工程合理性。
3. **Global MMLU variance (R1-W4 Minor vs R2 REBUT)**: Director 判定 **Info**——论文同时报告 global(σ=9.5pp) 和 uniform(σ=1.3pp)，处理得当。
4. **Missing baselines (R2-W5 Minor vs R1 partial REBUT)**: Director 判定 **Minor**——controlled comparison 逻辑成立，但参考数字有价值。
5. **R1-N3 severity (R1 Major vs R2 建议 Major)**: Director 维持 **Major**——论文已在多处报告退化，但 Conclusion 措辞过于模糊。

---

## Questions

1. 在 activation sparsity 设定下实现 MaskLLM 的 learnable-mask approach（去掉 predictor network），PPL 和下游表现如何？这能直接隔离 "predictor generalization" 的贡献。
2. K=4 是否有多种子数据？50% sparsity 下 K=4 数据是否可用？MMLU 超过 E2E KL 是否为系统性？
3. Per-layer sparsity constraint（如限制 late-layer sparsity ≤35%）是否能缓解 MMLU/GSM8K 回退？
4. BCE+compensation 的单独结果是什么？"compensation provides no benefit" 是否仅因 KL 自带补偿而 BCE 需要？
5. 更多样训练集（如 C4 subsample）是否能降低 OOD variance？

---

## Missing References

- **CATS** (Lee et al., 2024): 已提及但无实验对比——作为 training-free sophisticated baseline 值得补充
- **R-Sparse** (Zhang et al., 2025): 已提及但无对比——同为 learned predictor
- **Wanda** (Sun et al., 2024): 已提及但未讨论 activation-aware weight selection 与本文方法论关联
- **Griffin/Hawk** (De et al., 2024): R1 建议，R2 REBUT（gated linear recurrence vs SwiGLU FFN sparsity 关联弱）。Director 判定**不需要**。

---

## External Review (Stanford Agentic Reviewer)

未配置/未请求。

---

## Visual Layout Check

视觉审查 Agent 因 API 限额耗尽而失败（`agent_error: You've hit your limit · resets 6pm (UTC)`）。无排版审查结果。用户可在限额重置后重新触发。

**格式合规（Reviewer 人工确认）：**
| 项目 | 状态 |
|------|------|
| 正文 ≤ 8 页 | ✅ Sections 1-5 在 pages 1-8 |
| ACL template [review] | ✅ |
| Double-blind (Anonymous) | ✅ |
| Mandatory Limitations | ✅ 1 段，覆盖 3 点 |
| Ethics Statement | ✅ |
| References 格式 | ✅ natbib, acl_natbib.bst |
| Table/Figure 编号 | ✅ 连续正确 |

---

## Overall Assessment

**Score: 3.0 (Findings)**
**Confidence: 4/5**
**R1: 3.0 (Findings), Confidence 4/5 | R2: 3.0 (Findings), Confidence 4/5**

这是一篇执行严谨的实证研究，target-swap ablation 和 2D taxonomy 对理解稀疏预测训练目标的设计空间有贡献。多种子评估、全面消融、诚实的不利结果报告体现了良好的研究规范。

**阻止 Conference-level 接收的四个核心因素：**

1. **实践价值缺失**：+6.4% overhead 且无路径到 wall-clock speedup。对于稀疏预测领域的论文，无法展示实际效率收益是硬伤。
2. **Recipe 新颖性有限**：KL+Gumbel+frozen model 的核心组合已在 MaskLLM 中建立。迁移到 activation sparsity 设定有技术合理性但不足以构成独立方法贡献。分析框架（2D taxonomy）概念上直观。
3. **核心分析 claim 可靠性不足**：97.5% signal-type 归因基于 confounded 非正交分解；K=4 pilot 单 seed 且有反常结果；late-layer starvation → knowledge regression 的因果链缺 interventional 证据。
4. **下游 trade-off 显著**：MMLU/GSM8K 跨架构系统性输给 training-free TEAL（8B -5.2pp, 14B -20pp），限制 KL predictor 在知识密集场景下的实用性。

**适合 Findings track 发表**——分析框架和消融实验对后续 predictor-based sparsity 研究有参考价值。

**升级路径**（Borderline Conference 潜力）：
- (a) Triton block-sparse proof-of-concept 加速数据
- (b) 多种子 K=4 数据消除 mismatch confound
- (c) Per-layer sparsity constraint 实验验证 late-layer starvation 假说
- (d) Abstract/Conclusion 中 97.5% 和 K=4 claims 加充分 caveat

---

## Detailed Comments

### §1 Introduction
- "primarily an empirical study" 声明应前移到 Abstract 或 §1 首段，不应藏在 contribution 列表前。
- "(Appendix A)" 括号内的 wall-clock disclaimer 过于隐蔽，建议提升到正文句子。
- Contribution 列表第一项过长（4行），建议拆分 per-layer decomposition 和 cross-scale evidence。

### §2 Related Work
- MaskLLM 段落应更直接量化 activation sparsity 设定下的技术难点（per-token variability, OOD generalization, global allocation interaction），而非仅列举 "technically differ"。
- CATS/R-Sparse 仅列举未讨论优劣，错失 positioning 机会。

### §3 Method
- Eq.(1) g^(ℓ) vs Eq.(4) g1/g2 符号冲突——建议 Gumbel noise 改为 ε1, ε2。
- §3.5 adaptive penalty controller: "geometric doubling" 的 double/halve 条件和频率仅在 appendix，正文应补充关键实现细节。
- §3.7 Taxonomy table (Table 1): 多数 cell 为空/---，作为 visual representation 信息含量有限。

### §4 Experiments
- Table 2: 注释 6 行过长；实际 sparsity 差异（28.5% vs 29.3%）应在正文讨论而非仅 footnote。
- §4.2 Task-Type Split: per-layer sparsity 分析（L14-L18 protection valley）是 correlational，建议明确标注"correlational, not causal"。
- §4.5 Per-layer KL: "up to 97.5%" 在 Abstract/Conclusion 中需加 "(upper bound; dimensions not orthogonal)" caveat。K=4 pilot 推广时需标注 "(single seed, preliminary)"。
- §4.6: Figure 2 仅展示 global allocation 但结论推荐 uniform，不一致。
- §4.5 Compensation: BCE+compensation 的单独结果未报告——应明确 compensation 对 BCE 的效果以区分 "KL masks 好到不需要" vs "BCE masks 差到 compensation 也救不了"。

### §5 Conclusion
- "task- and scale-dependent" 过于模糊。建议改为直接陈述：KL 在 commonsense 任务上优于 TEAL，在 knowledge-intensive 任务上系统性劣于 TEAL。

### Limitations
- 覆盖 3 点，符合 EMNLP 要求。建议量化 OOD variance 的 practical implications（如 CV 从 0.2% → 6.3% 意味着什么）。

### Appendix
- Table 5 (latency) 的 +6.4% overhead 数据应在正文中更显著引用。
- K=4 pilot (Table 17) 应在标题中明确标注 "n=1 seed, preliminary"。