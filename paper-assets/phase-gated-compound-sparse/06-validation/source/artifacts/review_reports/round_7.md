---
round: 7
overall_score: borderline
timestamp: 2026-05-15T12:47:08.512336+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 7 (Fresh Review)

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models
**目标 Venue**: EMNLP 2026 Main Conference (ARR May 2026 cycle)
**审稿人**: Reviewer 1 (方法严谨性/实验/统计) + Reviewer 2 (新颖性/完整性/相关工作/格式)
**模式**: 圆桌 Round 1 独立初审 → 交叉分享逐条回应 → 收敛汇总

---

## Summary

本文研究 compound sparsity（attention head pruning + KV cache eviction 同时施加）的退化严重程度是否受推理阶段（phase）和驱逐策略（eviction strategy）调控。在 DeepSeek-R1-Distill-Qwen-7B（n=496）和 Qwen2.5-7B-Instruct（n=475）上，使用 MATH-500 数据集，跨 4 个对称 sparsity level（s∈{0.15,0.20,0.25,0.30}），论文发现：(1) importance-based eviction 下，compound severity 在 low-sparsity phase 集中放大（G=7.5–79.8×），而 random eviction 仅有微弱的 phase gradient（G≈0.5–1.3×）；(2) DeepSeek 上存在 strategy ranking crossover（importance 在 high-sparsity phase 优于 random，但在 low-sparsity phase 劣于 random）；(3) discrimination collapse（head pruning 压平 importance score 分布）作为相关性机制解释。

---

## Strengths

**S1. 统计方法论远超 NLP 领域平均水平 [两位 Reviewer 共识]**
Bootstrap CI (B=10,000, seed=42) + Wilcoxon signed-rank（paired within-model）+ Mann-Whitney U（cross-model）+ Jonckheere-Terpstra dose-response test + permutation test (n=50 profiling) + Bonferroni correction (k=4 per family) + BH-FDR robustness check (44 tests) + multiple segmentation granularity sensitivity analysis (tercile/quartile/quintile) + minimum phase length sensitivity (5/10/20)。这种多层次、多方法的统计验证在 NLP empirical work 中罕见。

**S2. Random eviction 作为 falsification control 设计精良 [两位 Reviewer 共识]**
Random eviction 的 near-unity G（0.5–1.3×）证明 phase gradient 不是 phase segmentation 或 metric 本身的 artifact，而是 importance-based eviction 特有的。这是论文方法论上的核心亮点。

**S3. Crossover 效应是真正新颖的发现 [两位 Reviewer 共识]**
DeepSeek 上的 strategy ranking reversal（importance 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）是 single-axis 分析无法预测的定性新现象。虽然 model-dependent（Qwen 无此效应），但作为新发现有独立价值。

**S4. 写作诚实透明 [两位 Reviewer 共识]**
Limitations section 详尽且全面（model scale, task coverage, symmetric sparsity, mechanism, PPL vs accuracy, sparsity range）。LLaMA 跨架构结果的 hedging 恰当（"preliminary", "suggestive", "mixed evidence"）。Pilot failure 直接报告（18% recovery, gate FAIL）。Discrimination collapse 明确标记为 "correlational" 而非 causal。Negative results 不隐藏。

**S5. 相关工作覆盖全面 [Reviewer 2]**
33 篇引用覆盖 compound compression、KV cache eviction、phase-aware inference 三个方向的核心工作，包括 2026 最新文献。引用验证未发现 fabrication。仅有 2 个轻微遗漏（MUSTAFAR NeurIPS 2025; LKV 2026），均非重大。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. [Critical, 两位 Reviewer 共识] 缺少 downstream accuracy 验证——construct validity 根本缺陷**

论文的核心指标 Interaction Index (II) 完全基于 perplexity（Eq. 1），但 MATH-500 的实际任务指标是 problem-level accuracy。PPL 和 accuracy 之间存在已知的非线性关系。论文声称 "motivate phase-aware compression budgets for mathematical reasoning models"（Abstract/Discussion/Conclusion），但未提供任何 accuracy 层面的验证。

R2 补充的关键论点：low-sparsity phase 对应 exploratory reasoning，此 phase 的 token 对最终答案的贡献可能远低于 high-sparsity phase（structured computation），因此即使 low-sparsity phase PPL 退化严重（G≫1），如果退化集中在对 final answer 不关键的 reasoning trace 上，整体 accuracy 可能不受影响——这将从根本上改变论文的结论。

**建议**：报告不同 sparsity level 和 phase 下的 problem-level accuracy drop；分析 per-problem II 与 accuracy loss 的 rank correlation。这不需要新实验，只需在现有数据上做 regression analysis。

**N2. [Critical, 两位 Reviewer 共识] G 指标定义不一致，Abstract CI 呈现误导**

- Eq. (2) 定义 per-problem G^(i) 的 median（median of ratios），Table 2 使用此定义；Appendix B Table 4 使用 ratio of medians。s=0.15 时差异达 9.2×（7.5 vs 69）。当 II_high ≈ 0 时 per-problem ratio 爆炸。
- Abstract 的 "bootstrap 95% CI: [4.1, 96.5]" 是 4 个独立 sparsity level 的 CI lower/upper bound 拼接，不是任何单一参数的置信区间，具有统计误导性。

**建议**：统一使用 median-of-ratios + bootstrap CI；明确标注 Appendix Table 4 使用不同定义；修改 Abstract CI 呈现。

**N3. [Critical, 两位 Reviewer 共识] 仅测试一种 importance 评分方法，但做类别性结论**

论文仅使用 position-normalized cumulative attention mass (Eq. 3)，但 Discussion 声称 "broad applicability" 基于 H2O/SnapKV/PyramidKV 共享 attention-mass 评分。实际上这些方法的具体实现差异很大（H2O: heavy-hitter + recent token; SnapKV: observation window; Ada-KV: per-head adaptive budgets）。

R2 的 nuance：定性方向可能 generalizable（head pruning 改变 attention 分布这一事实独立于具体评分公式），但定量结论的泛化无证据支持。

**建议**：Option A: 至少测试一种替代 importance 方法（如 H2O）。Option B: 将所有 claims 限定为 "cumulative-attention-mass-based scoring"，将 "broad applicability" 改为 "directionally consistent prediction"。

### Should-Fix（影响评分但不一票否决）

**W1. [Warning, R2 critical / R1 agrees with qualification] Generalizability 受限：单基准 + 单规模 + 同架构 "cross-model"**
- 仅 MATH-500，仅 7B。两个 Qwen2 模型共享 backbone（28L/28H/4-group GQA），§5.4 "Cross-Model Replication" 标题误导。LLaMA n=49 证据薄弱（~1/40 magnitude, mixed significance）。
- **建议**：改 §5.4 标题；增加至少一个非数学 benchmark 或更大规模模型，或明确缩窄 title/claims。

**W2. [Warning, 两位 Reviewer 共识，分歧仅在严重性] Pilot failure vs "motivate" framing 矛盾**
- Oracle reallocation 18% recovery (gate FAIL)，heuristic 32% (CI 跨零)。Conclusion "motivate phase-aware sparsity allocation" 与 failed pilot 不一致。
- R1 认为 characterization paper 不需 solution（should-fix）；R2 认为 motivation claim 无支撑（critical）。
- **共识**：framing 需从 "motivate solution" 调整为 "characterize phenomenon as prerequisite for future solutions"。

**W3. [Warning, 两位 Reviewer 共识] Crossover 效应 model-dependent 但在 Introduction 被过度依赖**
- Crossover 仅在 DeepSeek 出现，Qwen 无此效应。Introduction 用 "sign reversal" 作为核心论证 non-deducibility。
- **建议**：降低 Introduction 中的论证权重，明确标记 model-dependent。

**W4. [Warning, 两位 Reviewer 共识] Discrimination collapse "structural specificity" 缺乏定量证据**
- 6–16% Gini reduction 到 7.5–79.8× severity amplification 的巨大 gap 未被 bridged。"Structural specificity" 停留在定性推测。
- **建议**：提供 pruned-head overlap 分析或明确承认假说未验证。

**W5. [Warning, 两位 Reviewer 共识] LLaMA n=49 证据不足**
- 未解释为何不跑 n=500。n=49 暗示 profiling subset 遗留。Post-hoc power 未报告。
- **建议**：解释 n=49 原因；报告 post-hoc power；考虑运行完整 n=500 或降级为 Appendix。

**W6. [Warning, 两位 Reviewer 共识] 43:1 mean/median ratio 的极端离群值未分析**
- 可能来源：phase segmentation 边界效应、特定题型、bfloat16 numerical artifacts。
- **建议**：添加 Appendix outlier 分析，验证去除 top-5% outlier 后结论稳健。

### Minor Issues

- **M1**: Table 2 Qwen s=0.15 II_high = -0.000——负 II 应解释为 numerical noise（bfloat16 精度）。
- **M2**: Figure 1 使用 n=50 profiling subset，应更新为 n=496 full-scale 数据。
- **M3**: §5.3 报告 1.498 vs Table 2 报告 1.514（同一量），Qwen s=0.25 也有类似不一致（1.043 vs 1.053）。需统一数据源。
- **M4**: pyramidkv-2024 bib year 应为 2025（Conference on Language Modeling 2025）。
- **M5**: p 值精度过高（p < 10^{-69}），简化为 p ≪ 10^{-10}。
- **M6**: \paragraph label 前缀用 sec: 不规范。

---

## Reviewer Consensus

以下问题两位 Reviewer 达成 [AGREE]：
- N1 (缺 accuracy): 两位均标为 critical
- N2 (G 定义不一致 + CI 误导): 两位均同意
- N3 (单一 importance 方法): R1 critical, R2 agree (定量层面)
- W1 (Generalizability): 基本共识，措辞力度有差异
- W3 (Crossover model-dependent): 共识
- W4 (Structural specificity 缺证据): 共识
- W5 (LLaMA n=49): 共识
- W6 (Outlier 未分析): 共识
- W2 (Pilot failure framing): 共识需调整 framing，分歧在严重性

## Reviewer Divergence

| 议题 | R1 | R2 | 解读 |
|------|----|----|------|
| Pilot failure 严重性 | Should-Fix（characterization 不需 solution） | Critical（motivate claim 无支撑） | 方向一致，分歧仅在是否阻塞接收。Director 判断：作为 framing 问题处理（should-fix），但 Conclusion 措辞必须修改。 |
| "Emergent" 用词 | Rebut（标准科学含义） | Warning（ML 社区有特定含义） | 低优先级分歧。两种解读均合理，不影响核心评估。 |
| Bonferroni k=4 分组 | Warning（可能宽松） | Rebut（family 定义合理 + BH-FDR 已验证） | R2 的 rebut 有力——BH-FDR 结果证明核心结论不受影响。此分歧无实际后果。 |

---

## Questions（供 Author Response）

1. 是否有 problem-level accuracy 数据可以展示 II gradient 与 accuracy 退化的关系？
2. 为何 LLaMA 实验仅跑 n=49？
3. 是否考虑过在 H2O 或 SnapKV 的 importance scoring 上重复实验？
4. Table 4 (G=69–274) vs Table 2 (G=7.5–79.8) 的差异——哪个更准确反映效应量级？
5. §5.3 中 1.498 vs Table 2 中 1.514（及 Qwen 类似不一致）的数据来源差异是什么？
6. Crossover 在 Qwen 上不出现——是否与 distillation vs instruction tuning 的训练方法相关？
7. Oracle mitigation 18% recovery 失败的根因分析——是 budget reallocation 不够，还是 phase boundary 不精确，还是需要 strategy switching？

---

## Missing References

两个轻微遗漏（非重大）：
1. **MUSTAFAR (NeurIPS 2025)** — Joo et al., arXiv:2505.22913. Unstructured KV cache sparsity. 与本文的 structured pruning 不同但在 "KV cache eviction" 段落中值得一提。
2. **LKV (2026)** — arXiv:2605.06676. End-to-end learning of head-wise budgets and token selection. 与 head pruning 影响 KV eviction 的主题直接相关。

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。

---

## Overall Assessment

**评分: Borderline (weak reject for main conference / acceptable for Findings track)**

R1: 3.0/5 (Findings acceptance)
R2: 2.5/5 (Borderline Findings / 需修改重投)
Director 综合: **Borderline — weak reject for EMNLP main conference, recommend Findings track**

**置信度**: 4/5

**理由**：

论文在有限范围内展示了严谨的实证方法论——统计控制水平远超 NLP 平均，random baseline 的 falsification 设计精良，crossover 效应是真正新颖的发现，写作诚实透明。

然而，三个 critical 问题共同构成了对 EMNLP main conference 接收的障碍：

1. **Construct validity gap**：核心指标是 perplexity-based II，但 claim 关于 reasoning quality 和 deployment。如果 PPL 退化不转化为 accuracy 下降（特别是 low-sparsity phase 可能对应 non-critical tokens），整个 motivation 不成立。这是最严重的问题。

2. **Claims 超出 scope**：单一 importance scoring 方法→类别性结论；单一 benchmark + 单一规模 + 同架构 "cross-model"→"Mathematical Reasoning Models" 的 title-level claim。论文在测试范围内的验证是充分的，但 claims 一致性地超出了证据覆盖范围。

3. **Practical value uncertain**：论文声称 "motivate phase-aware compression budgets" 但 (a) 自己的 pilot 失败，(b) 无 throughput/latency 评估，(c) 无 accuracy 验证。作为 pure characterization，论文有科学价值；但需要调整 framing 以匹配实际贡献。

如果作者能在 author response 中提供 problem-level accuracy 与 II 的 correlation 分析（不需新实验，现有数据即可），并调整 claims scope，论文有望达到 Findings track 的接收标准。

---

## Detailed Comments（按论文章节）

### Abstract
- G 的 CI 呈现方式需修改（N2）
- "motivate phase-aware compression budgets" overclaim（W2）
- "emergent" 用词有争议（低优先级）

### §1 Introduction
- "Why can't existing single-axis findings predict our results?" 的论证过度依赖 model-dependent 的 crossover（W3）
- "This emergent coupling is not deducible from single-axis characterizations" 对于 Qwen（无 crossover）需 qualify

### §3 Background
- II additive null 假设合理，multiplicative null 已在 Appendix 验证
- G 定义（Eq. 2）需在首次使用时明确区分 median-of-ratios vs ratio-of-medians（N2）

### §4 Experimental Setup
- 应解释为什么仅 MATH-500、仅 7B
- float16→bfloat16 的 NaN 问题值得更深入讨论

### §5 Results
- §5.1/§5.2: 核心发现在测试范围内有充分统计支撑
- §5.3 crossover: 需明确标记 model-dependent
- §5.4 "Cross-Model Replication": 改标题
- §5.5 LLaMA: 解释 n=49；考虑降级
- 数值不一致（1.498 vs 1.514）需修正

### §6 Analysis
- "Correlational diagnostic" 的 framing 适当
- "Structural specificity" 需更多定量支持或明确标记为假说

### §7 Discussion
- "motivate phase-aware compression budgets" → "characterize phase-dependent phenomenon"
- Pilot failure 的 root cause 分析不足

### §8 Conclusion
- "motivate phase-aware sparsity allocation for reasoning model deployment" 需弱化
- 应增加 scope 限定

### Limitations
- 全面且诚实
- 建议在 "Perplexity vs accuracy" 段落加强——这是最核心的 limitation

### Appendix
- Table 4 与 Table 2 的 G 定义差异需明确标注
- Outlier 分析应添加
