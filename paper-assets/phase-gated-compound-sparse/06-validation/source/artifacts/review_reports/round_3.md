---
round: 3
overall_score: weak reject
timestamp: 2026-05-14T13:19:11.743199+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Phase-Modulated Compound Sparsity
**项目**: phase-gated-compound-sparse
**Venue**: EMNLP 2026 Main Conference (ARR May 2026)
**审稿轮次**: Round 1
**Reviewer 配置**: 2 人（R1: 方法严谨性+实验评估, R2: 新颖性+相关工作+写作+格式）
**外部审稿**: 未配置

---

## Summary

本文研究 compound sparsity（head pruning + KV cache eviction）在推理模型不同推理阶段的严重程度差异。在 DeepSeek-R1-Distill-Qwen-7B 和 Qwen2.5-7B-Instruct 上对 MATH-500 的 50 道题实验，发现 importance-based eviction 的 severity 在 low-sparsity phase 显著高于 high-sparsity phase（作者称 69×-274× severity gradient），而 random eviction 不显示此梯度。提出 entropy-discrimination collapse 作为机制假说。

---

## Strengths

1. **Random eviction 作为 falsification control 设计精巧**：7/8 random 条件不显著，有效排除了 trivial 解释，证明 severity gradient 是 strategy-specific 而非 compound sparsity 固有属性 [R1, R2 共识]
2. **统计方法严谨**：nonparametric bootstrap + paired permutation test + Bonferroni correction + effect sizes with CI 的组合在 ML 论文中罕见 [R1, R2 共识]
3. **Phase-strategy crossover 有实际意义**：importance-based eviction 在不同 phase 优劣反转，对实际 compression 策略选择有指导价值 [R1, R2 共识]
4. **Multiplicative null verification**：主动检验 additive vs multiplicative null 的 robustness [R1]
5. **Limitations 诚实全面**：对样本量、架构限制、因果性限制等的讨论坦诚 [R2]

---

## Weaknesses（按严重程度排序）

### Critical Issues（两位 Reviewer 共识）

**C1. Severity gradient G 的 69×-274× 倍数具有误导性** [R1-N2, R2-N2]
- G = Π̃_low / Π̃_high，分母 Π̃_high 极小（0.006-0.053），比值对噪声极度敏感
- 论文核心叙事（标题、Abstract、Conclusion）围绕 "order of magnitude" 展开，但这个数字本质是近零分母的放大效应
- 绝对差异 Δ（0.39-14.59）更稳健但远不如 G 震撼
- **要求**：报告 G 的 bootstrap CI；将 G 降为辅助指标，改用 Δ 和 d_z 作为主要效应量

**C2. 样本量严重不足** [R1-N1, R2-N3]
- n=50（实际 49/46），仅占 MATH-500 的 10%
- Bootstrap CI 极宽（s=0.30 时 CI=[0.70, 16.29]，跨一个数量级）
- Qwen s=0.15 效应不显著（d_z=0.28, CI 含零），但 Abstract 写 "replicates at s≥0.20" 给读者全面复现印象
- 未报告问题选择的 random seed
- **要求**：使用全部 500 题；报告 post-hoc power analysis；至少做 split-half stability analysis

**C3. 同架构 "跨模型复现" 严重高估泛化性** [R1-N3, R2-N3]
- DeepSeek 和 Qwen 共享 Qwen2ForCausalLM 架构（28 layers, 28 heads, 4-group GQA）
- "Cross-model replication"（§5.4 标题）措辞误导——实际验证同架构不同训练配置
- Per-problem concordance 不显著（mean ρ = −0.11）
- Qwen 效应量仅为 DeepSeek 的 ~1/5，更接近 marginal replication
- **要求**：增加至少一个非 Qwen 架构；或将 "cross-model" 改为 "cross-training-regime" 并弱化泛化声明

**C4. Discrimination collapse 仅相关性证据** [R1-N4, R2-W1]
- Gini 下降与 severity gradient 共现，但未排除混淆因素
- Entropy redistribution 在 Qwen s=0.25 出现符号反转，削弱机制普遍性
- 论文称 "mechanistic explanation" 但证据仅为 correlational
- **要求**：改 "mechanism" 为 "hypothesis"/"correlational evidence"；或设计 causal intervention

**C5. 贡献深度不足——纯观察无方法** [R2-N1; R1 moderate concern]
- 三条贡献均为经验观察（identify/show/propose mechanism），无可操作方法
- Phase-aware controller 仅停留概念层面
- R2 视为 critical（Excitement 2.5/5），R1 视为 moderate concern（Excitement 3/5）
- **要求**：实现 phase-aware compression budget（至少 oracle 版本）；或大幅扩大评估规模

**C6. 数值不一致** [R1 initial N1]
- Abstract/Table 1: Δ=14.59 vs §5.1: Δ=11.59
- 主文 n=50 vs Appendix E n=49（1 excluded）
- §6.2 ΔH ∈ [−0.080, −0.047] vs Table 7 ΔH ∈ [−0.047, −0.040]
- Cohen's d: Abstract 0.41 vs 正文 0.44
- **要求**：全面核对，确保所有数值一致

**C7. Spearman ρ=1.0 (n=4) 统计无效** [R1 initial N2]
- p=1/24≈0.042，未做 Bonferroni 修正后不再显著
- 论文据此在 §7 声称 "perfect ordinal agreement" 作为泛化主要论据
- **要求**：承认功效不足；降低泛化声明力度

**C8. Limitations 节格式违反 ARR 要求** [R2 initial N1, R1 W7]
- 当前为 §7.1 编号子节
- ARR 要求独立无编号节于 Conclusion 后、References 前
- **Desk reject 风险**
- **要求**：立即修正格式

**C9. 相关工作遗漏严重** [R2 initial N2, R2 updated]
- 极高优先级：R-KV (NeurIPS 2025), Lethe (AAAI 2026), RLKV, "Hold Onto That Thought" (NeurIPS 2025)
- 高优先级：RAC (NeurIPS 2025), RaaS (已在 bib 未引用), Scissorhands, FastGen, StreamingLLM
- **要求**：补充所有极高/高优先级工作的讨论

### Should-Fix Issues

**S1.** Phase segmentation 缺乏 sensitivity analysis（tercile 切分未做 robustness check）[R1, R2]
**S2.** 正文仅 ~5 页，关键表格（Table 2/3/5）应移入正文，充分利用 8 页空间 [R1, R2]
**S3.** Abstract ~600 词，信息过载，应精简至 150-200 词 [R2]
**S4.** 多重比较校正不充分（实际检验数远超 4，应用 FDR 校正）[R1]
**S5.** Sparsity 范围窄（仅 4 levels），monotonicity 证据不足 [R1]
**S6.** 仅 PPL 无 task accuracy 评估 [R1, R2]
**S7.** II 与已有 super-additivity 概念区分不清 [R2]
**S8.** Footnote 2 硬件信息泄露匿名性风险 [R1, R2]
**S9.** Bibliography 管理问题（7 orphan entries, h2o title 空, 年份不一致）[R1, R2]
**S10.** Appendix B 与 D 文本疑似重复 [R2]
**S11.** Interaction Index 的 additive null 假设与核心论点（轴间交互）内在矛盾 [R1]

---

## Reviewer Consensus

两位 Reviewer 在以下关键问题上完全一致 [AGREE]：
1. G 指标近零分母 → 69×-274× 不可靠，需 CI + 降级
2. n=50 不足 → 需扩至全部 MATH-500
3. 同架构 ≠ 跨模型泛化 → 需非 Qwen 架构验证
4. Discrimination collapse 是相关性非因果 → 降低 claim 或做 intervention
5. 正文过短，关键表格应移入正文
6. Phase segmentation 需 sensitivity analysis
7. 相关工作遗漏严重（R-KV, Lethe, RLKV 等）

## Reviewer Divergence

**D1. 贡献深度 / Excitement**：
- R2：critical，Excitement 2.5/5——EMNLP main conference 需要方法贡献，纯观察不够
- R1：moderate concern，Excitement 3/5——观察性发现有价值但需更大规模支撑
- 两者均认为当前不达 main conference 标准，分歧在严重程度

**D2. Interaction Index 方法论**：
- R1：additive null 假设（轴间独立）与论文核心论点（轴间交互）矛盾，建议增加 cross-entropy 空间分析
- R2：关注 II 与已有 super-additivity 概念的区分
- 视角不同但不冲突

---

## Questions for Authors

1. 为什么不使用全部 500 道 MATH-500 题？如为计算资源限制请说明。
2. G 的 bootstrap 95% CI？特别是 s=0.15 分母 II_high≈0.006 时。
3. 各条件下 MATH-500 solve rate（accuracy）？PPL 恶化是否对应答案错误？
4. 是否尝试过非 Qwen 架构（LLaMA 3, Mistral）？
5. Phase-aware compression budget 的 oracle 版本相比 uniform budget 能提升多少 accuracy？
6. Discrimination collapse 的 Gini 下降与 severity gradient 之间的 correlation coefficient？
7. §5.1 "11.59" vs Table 1 "14.59" 哪个正确？Cohen's d 0.41 vs 0.44？
8. 是否做过 split-half stability analysis 或 multiple generation seeds？
9. 用 token position 等分或 think 标记做 phase segmentation 结果如何？
10. 为什么选 Frobenius norm 而非 gradient-based importance 做 head pruning？论文提到 "attention-independent metrics should produce flatter severity gradients" 为何不验证？

---

## Missing References（合并去重）

| 优先级 | 论文 | Venue | 理由 |
|--------|------|-------|------|
| 极高 | R-KV (Cai et al.) | NeurIPS 2025 | Reasoning model KV compression，直接相关 |
| 极高 | Lethe (Zeng et al.) | AAAI 2026 | Phase-aware KV pruning，直接竞争 |
| 极高 | RLKV / "Which Heads Matter" (Du et al.) | 2025/2026 | Head importance for reasoning，与 discrimination collapse 相关 |
| 极高 | "Hold Onto That Thought" (Liu et al.) | NeurIPS 2025 | 系统评估 KV compression 对 reasoning 影响 |
| 高 | RAC | NeurIPS 2025 | Reasoning model pruning via CoT reconstruction |
| 高 | RaaS (Hu et al.) | ACL 2025 | 已在 bib 但未引用，reasoning-aware attention sparsity |
| 高 | Scissorhands (Liu et al.) | NeurIPS 2023 | KV eviction 基础方法 |
| 高 | FastGen (Ge et al.) | ICLR 2024 | Per-head adaptive KV cache |
| 高 | StreamingLLM (Xiao et al.) | ICLR 2024 | Attention sink 基础 |
| 高 | Titanus (Chen et al.) | GLSVLSI 2025 | KV pruning+quantization 复合效果 |
| 中 | EVICPRESS (Fang et al.) | 2025 | Joint KV compression + eviction |
| 中 | SparseGPT | ICML 2023 | 权重稀疏化基础 |
| 中 | Wanda | ICLR 2024 | 轻量 pruning |
| 中 | MInference | NeurIPS 2024 | 注意力稀疏模式分析 |
| 中 | Cohen (1988) | — | Statistical Power Analysis（effect size 解读依据） |
| 中 | LLM-Pruner (Ma et al.) | NeurIPS 2023 | Coupled pruning 开创性工作 |

---

## Overall Assessment

**Score: Weak Reject (2.5/5)**
**Confidence: 4/5**

两位 Reviewer 独立评估后均给出 2.5/5（R1 从初始 3/5 在交叉分享后下调至 2.5/5，R2 维持 2.5/5）。

**核心判断**：论文发现了一个有价值的经验现象（compound sparsity severity 的 phase 依赖性），实验设计有亮点（random eviction control），统计方法论严谨。但存在 9 个 critical 问题：
1. 核心指标 G 受近零分母膨胀，headline 数字不可靠
2. 样本量仅 50 题，统计功效不足
3. 同架构"跨模型"验证高估泛化性
4. 纯观察性贡献无方法提出
5. Discrimination collapse 仅相关性证据
6. 多处数值不一致
7. Spearman ρ=1.0 (n=4) 统计无效
8. Limitations 节格式违反 ARR 要求（desk reject 风险）
9. 相关工作遗漏严重

**建议路径**：
- **立即修复（deadline 前可完成）**：C6(数值一致性), C7(弱化 ρ claim), C8(Limitations 格式), C9(补充引用), S2-S3(正文扩展), S8-S10(格式清理)
- **需实验补充（可能需延期）**：C1(G 的 CI), C2(扩至 500 题), C3(增加非 Qwen 模型), C5(oracle phase-aware budget), S1(segmentation sensitivity), S5(更多 sparsity levels), S6(accuracy 指标)
- **需重新定位**：C4(降低因果 claim), C5(如不加方法则转 Findings)

当前状态不适合 EMNLP 2026 main conference。解决 C1-C3、C6-C9 + S1-S6 后可达 **Findings** 接收水平。如额外解决 C4-C5（加方法贡献 + 跨架构验证），可重投 main conference。

---

## Detailed Comments（逐节）

### Abstract
- 过长（~600 词），需精简至 150-200 词
- 多处数值需核对（Δ=14.59 vs 11.59, d=0.41 vs 0.44）
- "over an order of magnitude" 依赖不可靠的 G 指标

### §1 Introduction
- 贡献列表三条均为观察性，缺乏方法贡献
- "replicates across models" 措辞需弱化

### §2 Related Work
- 遗漏 R-KV, Lethe, RLKV, Hold Onto That Thought 等 10+ 篇高相关工作
- 第一段疑似混入 Experimental Setup 内容

### §3 Background & Methods
- G 定义的 ε 阈值未说明
- II 与已有 super-additivity 概念区分不清
- Additive null 假设与核心论点存在内在矛盾

### §4 Experimental Setup
- n=50 不足，选题标准不透明
- 仅 2 模型同架构，4 sparsity levels
- 仅 PPL 无 accuracy

### §5 Results
- §5.1: "11.59" vs Table 1 "14.59" 不一致
- §5.2: G 的近零分母问题
- §5.4: ρ=1.0 (n=4) 统计功效不足
- §5.6: Discrimination collapse 仅相关性

### §6 Discussion
- Phase-aware controller 仅概念层面
- ΔH range 与 Table 7 不一致

### §7 Conclusion & Limitations
- Limitations 格式违反 ARR（§7.1 编号子节 → 应为独立无编号节）

### References & Appendix
- 7 orphan bib entries
- h2o-neurips2023 title 空
- Appendix B 与 D 文本重复
- Footnote 2 硬件信息泄露匿名性