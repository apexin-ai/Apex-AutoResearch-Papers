---
round: 28
review_mode: fresh
overall_score: 3.0 (Findings)
timestamp: 2026-05-25T21:31:18.260676+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 31 (Fresh Review)

**论文**: Output-Distribution Distillation for Contextual Sparsity Prediction in SwiGLU LLMs  
**目标 Venue**: EMNLP 2026 (ARR)  
**审稿模式**: 重新审稿（fresh）  
**Reviewer 配置**: 2 人（R1: 方法/实验严谨性; R2: 新颖性/相关工作/写作完整性）

---

## Summary

本文提出用 output-distribution KL divergence（替代传统 per-neuron BCE）训练 SwiGLU LLM 的上下文稀疏性预测器，通过 Gumbel-Sigmoid relaxation 实现端到端可微训练。在 LLaMA-3.1-8B 上 30% sparsity 下比 TEAL 降低 14.5% PPL。核心发现：KL 优化的 mask 与 magnitude-based target 偏离 68%（Jaccard distance），target-swap ablation 表明 KL 的主要贡献在于发现更优的 mask target 而非端到端梯度耦合本身。

---

## Strengths

1. **Target-swap ablation 设计巧妙且产生 actionable insight**（R1/R2 共识）。§4.4 将 KL 发现的 mask 喂给 BCE，BCE 恢复 ≤0.63pp 差距——揭示 KL 的核心价值在于 target discovery 而非 gradient coupling。这是对 distillation-for-sparsity 领域有启发性的发现。

2. **系统性实验框架**（R1/R2 共识）。在相同架构、相同超参下对比 5 种训练目标（BCE/forward KL/reverse KL/JSD/MSE），控制变量严谨，形成清晰 evidence chain。

3. **梯度分析提供理论直觉**（R2-S3）。§3.6 对 BCE vs KL 梯度结构的对比（local per-neuron vs global Jacobian coupling）直观有效。

4. **实用价值明确**（R2-S4）。Predictor <1% base model 参数，训练成本低（单卡 1000 步），复用 TEAL 推理机制，部署门槛低。

5. **Appendix 实验深度**（R1/R2）。OOD 泛化、per-layer retention、cross-seed 稳定性、cross-architecture（Mistral-7B, Qwen-14B）提供有价值补充证据。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. 无实际推理加速，acceleration 叙事脱节** [R1 Must-Fix; R2 未反驳]
- Predictor 引入 6.4% inference overhead，sparsity 未产生实际速度提升
- 论文仍含 acceleration 相关表述，与实际结果不匹配
- 影响：如果论文不能加速推理，sparsity prediction 的核心动机需要重新论证（quality preservation at given compute? mask analysis tool?）

**N2. 主表 sparsity mismatch 未严格控制** [R1 Must-Fix]
- KL predictor 实际 28.5% sparsity vs TEAL 29.3%，~0.8pp 差异可能贡献部分 PPL gain
- 需要 iso-sparsity 对比或严格论证公平性

**N3. 核心 claim "signal type > coupling scope" 依赖未充分调优的 MSE baseline** [R1 Must-Fix]
- MSE 仅用 lr=1e-3，无完整 lr sweep
- Limitations 中提到 lr=1e-4 时 gap 缩至 8.45（vs 原始 9.47），但 Contribution #2 的表述仍基于未修正数值
- 如果 MSE 在最优超参下进一步接近 KL，"signal type > coupling scope" 叙事将严重削弱

**N4. Contribution #4（task-type analysis）作为正式贡献严重不足** [R2 Must-Fix + R1 AGREE]
- 仅 3 个 task 类别（reasoning/knowledge/commonsense），n=3 无法构成有意义的 pattern claim
- GSM8K 归入 "knowledge-intensive" 分类有误（GSM8K 主要测试数学推理）
- 两位 Reviewer 共识：降级为 §4.2 的 preliminary observation

**N5. 核心方法增量性质 + 论文定位模糊** [R2 Must-Fix; R1 部分同意]
- KL distillation + Gumbel-Sigmoid + TEAL top-k 是三个已有技术的直接组合
- 论文在 method paper（§3 大篇幅写方法）和 empirical study（§4.4 target-swap 实际削弱方法论叙事）之间摇摆
- R1 认为问题识别和 target-swap insight 有独立价值，但同意 repositioning 建议
- **建议**：明确定位为 empirical investigation（"什么样的训练信号最有效？"），以 findings 为核心叙事

### Should-Fix

**S1. 与 MaskLLM 的区分论证不够深入** [R2-W3 + R1 AGREE]
- 两者共享 frozen weights + learnable masks + KL divergence 框架
- static N:M vs contextual per-token 的方法论含义（exploration space 差异、Gumbel-Softmax vs Gumbel-Sigmoid 选择、temperature schedule 需求）未分析

**S2. C1 ablation 因果推断 confound** [R1-S2]
- 二值化 mask 丢失 gating score ranking 信息
- Target-swap 的比较不干净——不能排除是信息丢失（而非 coupling 差异）导致的结果
- 需在 §4.4 增加显式讨论

**S3. Abstract "renders post-hoc compensation networks redundant" 表述过强** [R2-W5; R1 部分同意]
- 50% sparsity 下可能仍有增益
- 建议改为条件化表述（如 "substantially reduces the need for" + 注明 30% sparsity 条件）

**S4. K-curve decomposition 受 train-inference mismatch 污染** [R1-S4]
- 训练用 Gumbel 连续近似，推理用 hard top-k，gap 可能混淆归因

**S5. Table 1 taxonomy 贡献性质模糊** [R2-W4 + R1 AGREE]
- 仅指出占据特定格子，未产生可验证的 non-obvious 预测
- 建议明确定位为文献综述组织工具

**S6. 模型规模 7B-14B 有限，Conclusion 措辞暗示更广泛适用性** [R2-W6 + R1 AGREE]
- "generalizing to" 需改为 "extends to"
- Limitations 需明确 model scale 限制

**S7. 知识任务系统性退化** [R1-S1]
- MMLU/GSM8K 在 30% 已有显著退化，50% collapse 到 near-random
- 论文虽有 dual-factor 解释但讨论不够充分

### Nice-to-Have

**M1.** 训练数据单一（WikiText-103），C4 OOD PPL 恶化到 11.55 显示 non-trivial sensitivity [R2-W7 + R1 AGREE]

**M2.** 术语不一致（predictor-TEAL / KL predictor / our predictor 混用）[R2-W8 + R1 AGREE]

---

## Questions for Authors

1. Target-swap 是否意味着更简单的两阶段流程（先 KL 短训生成 targets → 再 BCE 训练）能达到等效结果？如果是，论文的方法论 narrative 如何自洽？
2. §3.6 梯度分析（KL 通过 Jacobian 耦合）与 §4.4 target-swap 结果（coupling 非关键）如何调和？
3. MSE baseline 是否尝试过完整的 lr grid search（包括 5e-4, 2e-4 等）？
4. 是否有 wall-clock 速度测量（不仅是 FLOPs）？predictor overhead 在实际推理中如何分摊？
5. 50% sparsity 下所有方法 collapse——contextual sparsity prediction 在高稀疏度下是否本质不可行？是否尝试过增加 predictor capacity？

---

## Missing References

- **Sparse MoE routing 文献**（Switch Transformer, GShard）：per-token contextual mask prediction 与 MoE router 概念类似（expert-level vs neuron-level granularity），建议 §2 增加联系讨论 [R2 建议]
- **LLM.int8() (Dettmers et al., 2022)**：mixed-precision decomposition 思路与 per-layer budget allocation 有概念联系 [R2 建议]

---

## External Review

**状态**：未请求（项目未配置外部审稿）

---

## Visual Layout Check（非评分项）

**状态**: 完成 ✓ | **Critical**: 0 | **Warning**: 0 | **Info**: 10

排版质量专业，无重大问题：
- Figure 1 在页 2 顶部（首页无 display item），对方法论文可接受
- Table 2 全宽排版 + booktabs + 粗体/下划线标注齐全
- 页 7 信息密度高（3 个 display items）但不拥挤
- Figure 8（Appendix）尺寸偏小，打印可读性可改善
- References 格式统一，无未解析引用

---

## Overall Assessment

### 评分汇总

| 维度 | Reviewer 1 | Reviewer 2 | 共识 |
|------|-----------|-----------|------|
| Overall | 3.5 (Borderline Conference) | 3.0 (Findings) | **3.0–3.5** |
| Soundness | 3.5 | 3.5 | 3.5 |
| Excitement | 3.0 | 2.5 | 2.5–3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Confidence | 4 | 4 | 4 |

### 核心分歧

R1 与 R2 的 0.5 分差距源于对 **novelty** 和 **target-swap insight 价值** 的主观估值：
- R1：问题识别 + target-swap finding 有独立贡献价值（"moderate insight"），解决 N1-N3 后可升至 4.0
- R2：核心方法是已有技术直接组合，target-swap 虽有 insight 但实际削弱了论文自身的方法论叙事，定位为 Findings 更合适

### 综合建议

**Overall: 3.0 (Findings)**

本文是一项执行扎实的实验研究，target-swap ablation 提供了对 distillation-for-sparsity 领域有价值的 empirical insight。但作为当前 framing 下的 method paper，核心方法的增量性质（KL+Gumbel+TEAL 组合）、acceleration 叙事与实际结果的脱节、以及 MSE baseline 调优不足对核心 claim 的威胁，使其难以达到 EMNLP main conference 的 novelty 和 soundness bar。

**如需升至 Borderline Conference (3.5)**，需至少解决：
1. 彻底移除 acceleration 叙事，重新论证 sparsity prediction 的动机
2. 提供 iso-sparsity 对比数据
3. 补充 MSE lr sweep 或软化 "signal type > coupling" claim
4. 将 Contribution #4 降级 + 明确 empirical study 定位

**如需升至 Conference (4.0)**，还需额外：
5. 深入讨论 MaskLLM 技术对比
6. 解决 C1 ablation binarization confound
7. 扩展 task-type analysis 到 ≥10 benchmarks

---

## Detailed Comments（按优先级排序）

### Priority 1: Framing 重构
- §1 Introduction: 移除所有 acceleration 暗示，明确定位为 "empirical investigation of training objectives for contextual sparsity predictors"
- §1 Contributions: 重组——以 findings（target-swap discovery、objective comparison）为核心，方法作为 vehicle
- Contribution #4 → §4.2 的 "preliminary observation" 段落

### Priority 2: 实验补充/修正
- Table 2: 提供 iso-sparsity（严格 30.0%）对比或补充公平性论证
- MSE baseline: 补充 lr={5e-4, 2e-4, 1e-4} sweep 完整结果到正文（不仅是 Limitations）
- 如 MSE 最优结果接近 KL，需重新校准 Contribution #2 的措辞

### Priority 3: 写作修正
- Abstract: "renders...redundant" → 条件化表述
- §2/§3.7: 增加 MaskLLM 方法论对比段（1-2 段）
- §4.4: 增加 binarization confound 显式讨论
- Conclusion: "generalizing to" → "extends to"
- 全文统一术语（建议固定为 "KL predictor"）

### Priority 4: 声明校准
- Table 1 taxonomy: 定位为文献组织工具
- §4.5 K-curve: 增加 train-inference gap caveat
- Limitations: 增加 model scale (7B-14B only) 限制说明
