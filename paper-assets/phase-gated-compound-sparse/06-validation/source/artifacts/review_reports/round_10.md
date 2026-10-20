---
round: 10
overall_score: weak reject
timestamp: 2026-05-16T02:24:40.357863+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 10

**论文**: Phase-Modulated Compound Sparsity Severity in 7B-Scale Mathematical Reasoning Models
**Venue**: EMNLP 2026 Main Conference (ACL ARR May 2026 cycle)
**审稿编排**: 2 Reviewers（R1: 方法严谨性+实验设计+统计分析；R2: 新颖性+完整性+相关工作+写作格式）
**轮次**: Round 1 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 7B 推理模型的不同推理阶段（phase）中产生的质量退化差异。在 DeepSeek-R1-Distill-Qwen-7B（n=496）和 Qwen2.5-7B-Instruct（n=475）上，importance-based eviction 的 compound interaction 呈现显著的 phase 依赖性：低稀疏度阶段的 severity 比高稀疏度阶段高 7.5-79.8×（G 值），paired median difference Δ 从 0.39 增至 8.48（DeepSeek）和 0.07 增至 3.16（Qwen）。论文提出 importance discrimination collapse 作为相关性机制解释，并在 GSM8K（n=50）和 LLaMA-8B（n=49，exploratory）上做了有限验证。

---

## Strengths

1. **统计方法论出色**：Nonparametric bootstrap + Wilcoxon + permutation test + Jonckheere-Terpstra + BH-FDR 多重验证，附 post-hoc power analysis、winsorized robustness、multiplicative null verification，远超该领域平均水平。
2. **Robustness analysis 全面**：mpl sensitivity（5/10/20）、segmentation granularity（tercile/quartile/quintile）、asymmetric sparsity、outlier analysis、<think> token validation（κ=0.887）。
3. **诚实的 Limitations section**：坦诚承认 scale 限制、architecture 限制、sparsity 范围限制、PPL-accuracy gap、mechanism 仅为 correlational。
4. **Phase-Strategy Crossover 是非显然发现**：s=0.25 时 importance vs random 的 phase-dependent ranking reversal（2.2-4.0×）不能从已有 single-axis 文献直接推出。
5. **Clean experimental design**：对称 sparsity、additive/multiplicative null 对比、Δ 作为 primary metric 配 G 作为 auxiliary。

---

## Weaknesses

### Must-Fix（影响接收决定）

**[W-Critical-1] MUSTAFAR 引用完全伪造**（R1-N3 + R2-N1，unanimous AGREE）

`mustafar-neurips2025` bib 条目的标题（"Multi-Stage Transformer Architecture for Adaptive Reasoning with KV Cache Compression"）、作者（Joo Wonyong, Kim Sungmin, Park Sehyun, Yoo Kang Min）、内容描述（"learned budgets"）均为虚构。实际论文为 "Promoting Unstructured Sparsity for KV Cache Pruning in LLM Inference"（Donghyeon Joo, Helya Hosseini, Ramyad Hadidi, Bahar Asgari; NeurIPS 2025, OpenReview ID: C69741fMFX）。R1 通过 NeurIPS 官方页面独立验证。这是典型的 LLM 生成幻觉引用，触及学术诚信底线。

→ 必须立即修正。建议全面审查所有 bib 条目是否存在类似问题。

**[W-Critical-2] Novelty 不足以支撑 Main Conference**（R2-N2，R1 部分 REBUT 但同意 Findings）

R2 认为核心发现（低稀疏度阶段更脆弱）在 ThinKV/Sparse Frontier 之后直觉可预期。R1 部分反驳：compound interaction 的 phase-dependence ≠ individual effect 的 phase-dependence；crossover 是非显然发现。但 R1 同意不够 Main Conference。

两位 Reviewer 共识：**Findings track 合适**。Compound interaction 量化（G=7.5-79.8×）和 crossover 是新的 empirical evidence，但未达到 Main Conference 对 novelty 的要求——量化一个 directionally predictable 的现象不等于揭示 counter-intuitive knowledge。

**[W-Critical-3] Cross-architecture generalization 严重不足**（R1-N1 + R2-W1，unanimous AGREE）

两个主模型（DeepSeek、Qwen）共享 Qwen2ForCausalLM backbone（28L/28H/4-group GQA）。"Cross-model replication" 实质是 cross-training-paradigm on same architecture。唯一跨架构证据 LLaMA n=49：effect size ~1/40 of DeepSeek、power 0.26-0.63、仅 s=0.30 Bonferroni-significant、CI 和 Wilcoxon 系统性矛盾。Abstract 中 "exploratory evidence suggesting the pattern may extend beyond Qwen2" 具有误导性。

→ 增加至少一个不同架构的完整验证（n≥200），或在 Abstract/Intro/Contributions 中严格限定为 Qwen2 family。

**[W-Critical-4] Phase segmentation 验证不足 + circularity 隐患**（R1-N2，R2 部分 AGREE）

κ=0.887 验证仅在 1 model × 1 benchmark × 48 samples（DeepSeek GSM8K）上完成。Qwen 完全无验证。主 benchmark MATH-500 也无验证。R1 指出潜在循环论证：低稀疏度阶段 = 注意力分散 → eviction 对分散注意力伤害本来就大。R2 部分反驳：crossover 发现（importance vs random 差异 15-17×）partially 打破了 circularity，说明不仅仅是 attention distribution 的机械后果。但 R2 同意在 LLaMA 上 circularity concern 部分成立（random 也有 non-trivial phase gradient）。

→ 在 MATH-500 上做 <think> 验证；明确论证 compound interaction 的 phase-dependence 独立于 individual effect 的 phase-dependence。

**[W-Critical-5] Mechanism 解释力存在数量级缺口**（R2-N3，R1 AGREE）

Table 9 显示 Gini drop 为 -0.030 到 -0.081（baseline 的 ~3-10%），但 severity divergence 达 7.5-79.8×（1-2 个数量级 gap）。Per-phase Gini decomposition 缺失——无法验证 "collapse has maximum impact in low-sparsity phases" 的 claim。Contribution 3 使用 causal 语言（"necessary but not sufficient"），但仅有 correlational evidence。Entropy redistribution 仅在 DeepSeek 一致（Qwen 2/4 replicates）。

→ 报告 per-phase Gini delta；修订 Contribution 3 避免 causal language。

### Should-Fix（影响评分但不一票否决）

**[W-Warning-1] PPL-accuracy construct validity gap**（R1-W3，R2 AGREE）

93.2% answer tokens 在 high-sparsity phase（G≈1）——compound interaction 几乎不影响 answer region。"Silent reasoning errors" 是推测，缺乏实证。Accuracy validation 中 DeepSeek s≤0.20 degradation 主要由 truncation 驱动（non-truncated accuracy 68-71%）。Qwen 的 accuracy cliff at s=0.30（δ=-27pp）提供了部分支撑，但 PPL → accuracy 的 non-linear mapping 削弱了 "severity gradient → practical consequence" 的 narrative。

→ 引用 CoT faithfulness 文献（Lanham 2023, Turpin 2023）支撑 "silent reasoning errors"；设计 phase-specific accuracy proxy。

**[W-Warning-2] 仅 4 个 sparsity levels，dose-response claim 过强**（R1-W1，R2 AGREE）

s∈{0.15, 0.20, 0.25, 0.30} 4 个点可确认 monotonicity（JT test），但无法区分 functional form。Figure 1 连续线连接离散点暗示未验证的平滑关系。

→ 增加采样点（如 s∈{0.10, 0.35, 0.40}），或将 monotonicity claim 限定为 "at four tested levels"；修改 Figure 1 为 scatter+error bar。

**[W-Warning-3] 仅测试一种 importance scoring method**（R2-W4，R1 AGREE）

KV eviction 仅用 position-normalized cumulative attention mass。§7 声称泛化到 H2O/SnapKV/PyramidKV 但无实验。如果 phase-modulated severity 在替代 scoring 下消失，核心 claim 变成 method-specific。

→ 至少做一种替代 scoring 的 spot check，或降级泛化声明为 explicit hypothesis。

**[W-Warning-4] GSM8K n=50 缺少 power analysis + confounds**（R1-W6，R2 部分 REBUT）

Importance-based 的 significance 是充分的后验 power 证据，但 random eviction 的 null results 缺少 power analysis（无法区分 "无效应" vs "power 不足"）。DeepSeek 30-40% language switching confound 未在 MATH-500 上确认。

→ 为 random null results 报告 power analysis；确认 language switching 在 MATH-500 上的 prevalence。

**[W-Warning-5] Bonferroni family 定义不一致**（R1-W4，R2 AGREE）

不同 section 的 Bonferroni family 各自独立定义（k=4），但实际 test family 远大于 4。BH-FDR（Appendix）部分 addresses，对核心结果影响有限（p~10^-10），但 marginal random eviction cases 受影响。

→ 明确 family 定义理由；在主文中引用 BH-FDR appendix。

**[W-Warning-6] G metric 两种定义差异巨大（7.5× vs 69×）**（R1-W2，R2 部分 REBUT）

Per-problem G 与 ratio-of-medians G 差异 3.4-5.6×。R2 指出 Δ 是 primary metric（definition-invariant），G 是 auxiliary。共识：Δ 是 robust 的，但 Abstract/Intro 以 G 为 headline 创造了 inflated impression。

→ Abstract/Intro 以 Δ 为 headline，G 降级为 supporting evidence。

---

## Reviewer Consensus

| 问题 | R1 | R2 | 交叉结果 |
|------|----|----|----------|
| MUSTAFAR 伪造 | Critical | Critical | **Unanimous AGREE** |
| Novelty ≤ Findings | Weak Reject (2/5) | Borderline Findings (2.5/5) | **Consensus: Findings track** |
| Cross-architecture 不足 | Critical (N1) | Warning (W1) | **Unanimous AGREE** |
| Phase segmentation 验证 | Critical (N2) | Partial AGREE | **Consensus: insufficient, crossover partially mitigates circularity** |
| Mechanism gap | AGREE with R2-N3 | Critical (N3) | **Unanimous AGREE** |
| PPL-accuracy gap | Warning (W3) | AGREE | **Unanimous AGREE** |
| Page limit | R2 flags; R1 REBUT | Warning (W3) | **Resolved: within 8 pages** |
| Throughput | R2 flags; R1 REBUT | Warning (W6) | **Divergence: R1 says not needed for diagnostic study; R2 disagrees. Director note: R1's position is reasonable given paper positioning.** |
| Pilot framing | R2 flags; R1 REBUT | Warning (W5) | **Minor divergence: current framing adequate but CI should be mentioned in Discussion** |

## Reviewer Divergence

**Novelty severity**：R1 认为 compound interaction phase-dependence 和 crossover 有一定 novelty（不能从 single-axis 文献推出），给 Excitement 3/5；R2 认为核心方向可预期，给 Excitement 2/5。两人均认为不够 Main Conference 但可达 Findings。Divergence 在程度而非方向上。

---

## Questions for Authors

1. **Phase segmentation circularity**：如何证明 compound interaction 的 phase-dependence 独立于 individual eviction effect 的 phase-dependence？（R1-N2，crossover 仅 partial defense）
2. **Per-phase Gini delta**：是否能提供低/高稀疏度阶段分别的 Gini 变化？这可能 partially bridge mechanism 的数量级 gap。（R2-N3 Q1）
3. **LLaMA effect size ~1/40**：这是架构差异、训练差异、还是 power 不足导致的 attenuation？对非 Qwen2 架构的 practical 意义？（R1-Q3）
4. **Language switching**：DeepSeek 在 GSM8K 上 30-40% 出现中文乱码——MATH-500 是否也存在？PPL 测量是否被污染？（R1-Q4）
5. **93.2% answer tokens in G≈1**：如果 severity 集中在 reasoning trace 而非 answer，phase-aware mitigation 的 deployment value 何在？（R1-Q5）

---

## Missing References

**两位 Reviewer 共识推荐**：
- CoT faithfulness literature: Lanham et al. (2023), Turpin et al. (2023)——支撑 §5.7 "silent reasoning errors" 论断

**R1 推荐**：
- Sparse Sinkhorn Attention (Tay et al., 2020)
- Wanda (Sun et al., 2024), SparseGPT (Frantar & Alistarh, 2023)——R2 REBUT: weight pruning 与 inference-time pruning 不同层面，非 critical missing

**R2 推荐**：
- KVzip (NeurIPS 2025), ShadowKV (2024), MiniCache (2024)——R1 认为 coverage 已足够（40 篇引用），这些为 optional

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置。

---

## Overall Assessment

**Score: Weak Reject / Borderline Findings (2.25/5)**
- R1: 2/5 (Weak Reject)
- R2: 2.5/5 (Borderline Findings)
- Averaged: 2.25/5

**Confidence**: 4/5（两位 Reviewer 均 4/5）

**一句话总结**：论文在 Qwen2 架构的 7B 模型上提供了 compound sparsity severity 的 phase-dependent 特性的 suggestive evidence，统计执行质量高，但 (1) MUSTAFAR 引用伪造不可接受；(2) novelty 不足以支撑 Main Conference；(3) generalization 局限于 Qwen2 family；(4) mechanism 存在数量级解释缺口；(5) phase segmentation 验证不足。

**建议**：修正引用后投 EMNLP 2026 **Findings track**。如投 Main Conference，需增加跨架构验证（n≥200）、per-phase mechanism 分析、替代 scoring method 验证。

---

## Detailed Comments

### Section 1 (Introduction)
- Contribution 2 "replicates across two Qwen2-architecture models" 技术上准确但有误导性——应明确为 "cross-training-paradigm replication within the Qwen2 architecture family"
- Contribution 3 使用 "necessary but not sufficient" 是 causal language，仅有 correlational support
- Novelty argument 应强调 compound interaction（not individual effect）的 phase-dependence 是非 trivial 的

### Section 3 (Background)
- Phase segmentation 定义为 "operationalization choice"——恰当，但应在此处预告 <think> validation（目前仅在 Appendix）
- II 定义的 additive null 现在正确定位为 "conservative baseline" + 承认 causal coupling

### Section 4 (Experimental Setup)
- Footnote 2: "An earlier bfloat16 configuration produced sporadic NaN values; bfloat16 eliminated all occurrences" 自相矛盾——应为 "float16 → bfloat16"
- GPU 型号（RTX PRO 6000 Blackwell 96GB）可能间接 deanonymize——建议泛化

### Section 5 (Results)
- §5.1-5.2: 核心结果 solid，Δ 和 G 在 DeepSeek/Qwen 上一致
- §5.3 Crossover: 最有 novelty 的发现，但仅 DeepSeek 有——应更突出 model-dependence
- §5.5 Cross-Arch: "exploratory evidence" 过于乐观，应为 "preliminary but inconclusive"
- §5.6 GSM8K: random eviction null results 缺 power analysis
- §5.7 Answer-Region: "silent reasoning errors" 需 CoT faithfulness 文献支撑
- §5.8 Accuracy: Qwen data (truncation ≤4%) 比 DeepSeek (truncation 16→76%) 更 informative

### Section 6 (Analysis)
- §6.1: Per-phase Gini decomposition 是 key missing analysis
- §6.2: Entropy mechanism 的 model-dependence 应在 section title 中反映（如 "Entropy Redistribution: A Model-Dependent Secondary Effect"）

### Section 7 (Discussion)
- Pilot mention 应加 "though confidence intervals span zero"
- 泛化声明（H2O/SnapKV/PyramidKV）需降级为 hypothesis 或补实验

### Section 8 (Conclusion)
- 无重大问题

### Limitations
- 全面且诚实——论文在此方面优于领域平均水平

### Appendix
- Figure 1: 连续线连接离散点，建议改为 scatter+error bar
- Table 5 (profiling subset): G 定义差异的讨论到位
- Appendix K (pilot): CI span zero 应更突出