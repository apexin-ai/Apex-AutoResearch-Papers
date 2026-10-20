---
round: 4
overall_score: weak reject
timestamp: 2026-05-15T07:49:59.758091+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 圆桌审稿报告 — Round 1

**论文**: Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Reasoning Models
**Venue**: EMNLP 2026 ARR (Main Conference)
**截止日期**: 2026-05-25
**Reviewer 编排**: R1（方法严谨性）+ R2（新颖性/完整性）
**轮次**: Round 1（独立审稿 + 交叉分享完成，达成收敛）

---

## Summary

本文研究 compound sparsity（同时进行 attention head pruning 和 KV cache eviction）在 reasoning model 生成过程中的 phase-dependent severity。核心发现：在 importance-based eviction 下，compound interaction 的严重程度（以 Interaction Index 衡量）集中在 low-sparsity reasoning phases，severity gradient 从 69× (s=0.15) 增长到 274× (s=0.30)；random eviction 无此现象（7/8 conditions non-significant）。在 Qwen2.5-7B-Instruct 上部分复现（s≥0.20），在 LlamaForCausalLM 上仅获得微弱方向性一致证据。提出 entropy-discrimination collapse 作为机制解释。

---

## Strengths

**S1** [consensus] **研究问题有价值且定义清晰**。将 compound sparsity 的 phase-invariance assumption 作为明确攻击目标，对 efficient inference 部署有直接指导意义。

**S2** [consensus] **统计方法论严谨**。非参数 bootstrap (B=10,000)、paired permutation tests、Bonferroni correction、Cohen's d_z、报告中位数处理右偏分布——统计意识优于绝大多数 ML 论文。

**S3** [consensus] **Random eviction 作为 falsification control 设计巧妙**。7/8 conditions 下 random eviction 无显著 phase gradient，有效隔离了 strategy-specific amplification，构成强 counterfactual。

**S4** [consensus] **Crossover 发现有 non-trivial insight**。§5.3 的 strategy ranking reversal（importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random）对部署有直接启示——uniform budget 必然在某个 phase 是 suboptimal 的。

**S5** [consensus] **Multiplicative null verification** (Appendix A) 增强了 Interaction Index 定义的鲁棒性。

**S6** [consensus] **Limitations 写作坦诚**，多数局限在 limitations section 中有诚实讨论。

---

## Weaknesses（按严重性排序）

### Must-Fix（影响接收决定）

**MF1** [critical, consensus R1+R2] **论文严重未完成：40+ placeholders 未填充**
- Abstract 中 Qwen random s=0.30 的 Δ̃ 值缺失
- Table 4（LLaMA cross-architecture validation, §5.5）整表 16 个数据 cell 全部空白
- §5.4 cross-model: NULL_PCT、N_LLAMA 未填
- §7 Discussion: oracle pilot experiment 4 个关键指标（ORACLE_PCT、ORACLE_P、HEUR_PCT、HEUR_P）全部缺失
- Appendix: Qwen effective-n table 12 cells 空白、per-problem concordance ρ/p 未填（尽管 LaTeX 注释中有数据）、多处 LLaMA random p-value 缺失
- **影响**：Table 4 是本文最重要的 generalization 证据，Discussion 中的 oracle pilot 是唯一从 characterization 走向 actionable mitigation 的部分——两者的核心数据全部缺失。论文以当前状态提交将被视为 incomplete submission，无法进入实质性审稿。

**MF2** [critical, consensus R1+R2] **Cross-architecture 证据薄弱且 overclaim**
- LLaMA 绝对 magnitude 仅为 DeepSeek 的 ~1/40、Qwen 的 ~1/7
- 4 个 sparsity levels 中仅 s=0.30 的 Bonferroni-corrected Wilcoxon 达显著 (p=0.029)
- 统计指标自相矛盾：s=0.15 时 CI 排除零但 Wilcoxon NS；s=0.30 时 CI 跨零但 Wilcoxon significant
- Random eviction 在 LLaMA 上也展现 non-trivial phase gradient，严重削弱 strategy-specificity claim
- Table 4 完全空白，上述数字仅来自文本叙述
- **Overclaim 位置**：Title "Reasoning Models"（复数暗示广泛适用）；Abstract line 10 "directionally consistent evidence for cross-architecture generalization"；Contribution 2 "replicates across three models spanning two architectures"
- **建议**：将 LLaMA 降级为 exploratory supplement；Title/Abstract/Contribution 使用 "suggestive" 或 "preliminary" 等限定词

**MF3** [critical, consensus R1+R2] **单一 benchmark (MATH-500) 严重限制泛化性**
- 仅测试数学推理，Title/Abstract 使用 "Reasoning Models" 的一般性表述
- 不同推理任务（code generation、multi-hop QA）会产生完全不同的 attention phase structure
- 作为以 "characterization" 为核心贡献的论文，characterization 的范围直接决定贡献大小
- **建议**：至少添加一个非数学推理 benchmark，或在 Title/Abstract 中明确限定为 "mathematical reasoning"

**MF4** [critical R1 / should-fix R2, consolidated: critical] **50 题样本量缺乏 power analysis**
- 从 MATH-500 中仅抽取 50 题（10% 采样率），无事先 power analysis
- 分层方案（stratified sampling）未报告各层样本量
- 有效样本因排除进一步减少：DS n=49、QW n=46、LLaMA n=49
- Qwen s=0.15 的 d_z=0.28 且 CI 包含零，可能是 underpowered 的表现
- R2 指出 paired design 提供 power advantage，DeepSeek 主结论统计充分（所有 p_Bonf < 0.005）——power 疑虑主要限于 Qwen 低 sparsity 和 LLaMA 全局
- **建议**：报告 post-hoc power analysis；解释为何不用全部 500 题；在 Methodology 中完整报告排除标准

**MF5** [critical R1 / should-fix R2, consolidated: should-fix→critical borderline] **机制分析（entropy-discrimination collapse）纯 correlational**
- 无 causal intervention（如固定 entropy 水平观察 II 变化）
- Entropy redistribution 在 Qwen s=0.25 出现符号反转（ΔH = +0.045，22/30 problems 熵增），paper 称 "secondary model-dependent amplifier" 但这实质是 ad hoc 解释
- Analysis 叙述偏 causal（"head pruning flattens..."、"degrading the discriminative power..."）但证据仅 correlational
- **缓解因素**（R2 指出）：论文已使用 hedged language ("We propose...as the primary mechanism")；Gini coefficient 在 16/16 conditions 一致为负；random eviction immunity 构成 partial counterfactual
- **建议**：§6 标题和叙述改为更 hedged 的表述；至少标注 "correlational evidence"；如条件允许设计一个 causal experiment

### Should-Fix（影响评分但不一票否决）

**SF1** [warning, consensus] **Phase segmentation (tercile-based) 缺乏充分论证**
- ThinKV 使用 explicit `<think>` delimiters，本文使用 attention sparsity quantile tercile——方法论完全不同但论文称 "following ThinKV"
- 强制将每个 sequence 分为三等份，即使 attention sparsity 是 unimodal 的
- 为什么用 3 phases 而非 4 或 5？min_phase_length=10 依据？无 sensitivity analysis
- **建议**：修正 ThinKV 引用措辞；添加 segmentation sensitivity analysis

**SF2** [warning, consensus] **G 的数值稳定性问题**
- 当 II_high ≈ 0.006 (s=0.15) 时，G 对分母微小波动极敏感
- G 的 bootstrap CI 未报告，可能在 [33, 133] 范围（vs point estimate 69）
- **建议**：报告 G 的 CI；用 Δ 作主指标，G 降级为辅助

**SF3** [warning, consensus] **Bonferroni 校正范围 (k=4) 可能不足**
- 实际 test 数远多于 4：2 strategies × 4 sparsity × 3 models × multiple test types
- Family-wise error rate 可能被低估
- **建议**：论证 k=4 的 family 划分依据，或采用 FDR

**SF4** [warning, R2 critical → R1 rebuts → consolidated warning] **与 HIES (2025) 区分不充分**
- HIES 已报告 single-axis head discrimination collapse under heavy pruning
- Related Work 仅一句话提及，Analysis §6 完全未讨论两者区别
- R1 指出关键 delta：HIES 是 single-axis，本文 extend 到 compound + phase-dependent setting（crossover 现象是 HIES 框架中不存在的 prediction）——novelty 有清晰区分，但论文未充分展示这一区分
- **建议**：在 Related Work 和 Analysis 中添加 explicit comparison

**SF5** [warning, consensus] **Symmetric sparsity assumption 的实践代表性**
- 实际部署中两轴 budget 通常不同
- **建议**：讨论局限或提供 1-2 个 asymmetric spot check

**SF6** [warning, consensus] **Spearman ρ=1.0 on 4 points 被 over-interpret**
- 4 个数据点的 exact permutation p = 0.042，barely significant
- 未注明 sample size，读者可能误以为高 power 证据
- Table 1 (segment-level Δ) vs Table 4 (problem-level paired Δ̃) 数字差异未解释
- **建议**：标注 sample size caveat；在 caption 解释两表差异

**SF7** [warning, consensus] **排除标准未在 Methodology 中说明**
- DS 50→49 排除原因未提及；QW 50→46 仅在 Appendix 解释
- **建议**：在 §4 中完整报告

**SF8** [warning, partial consensus] **Related Work 可能遗漏 RLKV、LongFlow、PM-KVQ**
- R2 列出遗漏；R1 同意但指出需确认这些工作是否涉及 compound interaction 或 phase-dependent effects
- **建议**：评估相关性后补充直接相关引用

**SF9** [warning, consensus] **Abstract 过长过密**
- 14 行含 10+ 统计数字，可读性差
- LLaMA 详细统计量（Δ̃、p_Bonf）属于 Results 而非 Abstract
- **建议**：精简到核心 claim + 1-2 headline numbers

### Info 级别

- **h2o-neurips2023** bib entry 缺 title 字段；deepseek-r1-2025、snapkv-neurips2024、unicomp-2026 author 信息有偏差
- LaTeX source 中 **REVIEWER-ATTACK/REBUTTAL** 注释应在提交前删除（ARR 某些情况下可下载源码）
- **s=0.35 supplementary experiment** (Appendix D) 仅一句话提及无完整数据——要么报告完整要么删除
- 无 **代码/数据开源** 声明，影响 reproducibility

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致 **[AGREE]**：
1. Placeholder 未填充是 showstopper（MF1）
2. Cross-architecture LLaMA 证据不支撑当前 framing（MF2）
3. 单一 benchmark 限制泛化（MF3）
4. Phase segmentation 需 sensitivity analysis（SF1）
5. G 数值不稳定（SF2）
6. Bonferroni scope 偏窄（SF3）
7. Abstract 过密（SF9）
8. 排除标准未说明（SF7）

## Reviewer Divergence

| 问题 | R1 | R2 | 合并判定 |
|------|----|----|----------|
| Sample size power (MF4) | critical | should-fix (paired design power) | critical（缺 power analysis 本身是方法论缺陷） |
| Mechanism causality (MF5) | critical | should-fix (hedged language, 16/16 consistent) | critical borderline（降级叙述 assertiveness 后可降为 warning） |
| HIES novelty overlap (SF4) | should-fix | critical | warning（有清晰 delta 但讨论不充分） |
| Empirical finding venue fit | N/A | W1 warning | dismissed（R1 rebuts: ACL/EMNLP 接受高质量 empirical finding） |
| REVIEWER-ATTACK comments | optional cleanup | should-clean | info |

---

## Questions for Authors

1. Table 4 的所有 placeholder 何时能填充？如果 LLaMA 实验数据已有但未整理完，建议在 resubmission 时完整报告。如果实验尚未完成，建议删除 Section 5.5 并降低 cross-architecture claim。
2. 能否提供 HIES (2025) single-axis discrimination collapse 与本文 compound + phase-dependent collapse 的 explicit comparison？HIES 是否观察到 phase-dependent discrimination loss？
3. 为什么只用 50/500 题？在全部 500 题上运行一个 configuration 的 GPU 时间成本是多少？
4. Phase segmentation 对结果的敏感性：如果改用 quartile 或 quintile 分割，main findings 是否 robust？
5. LLaMA 上 random eviction 也展现 non-trivial phase gradient——这是否意味着在某些架构上 phase modulation 不是 strategy-specific 而是 compound sparsity 的 inherent property？
6. Qwen s=0.25 entropy 反转（ΔH = +0.045）与该 sparsity level 的 severity gradient 有无 quantitative 关联？
7. Oracle pilot experiment（Discussion）是否已执行？如果已执行且 below gate，为什么不填入数据？
8. 是否计划开源代码和实验数据？

---

## Missing References

R2 指出以下可能遗漏的近期相关工作（R1 同意需评估相关性）：
- **RLKV** (OpenReview 2026): RL 优化 per-head cache + reasoning quality
- **LongFlow** (arXiv 2603.11504): reasoning model long-output KV cache compression
- **PM-KVQ** (OpenReview 2026): Progressive mixed-precision KV cache quantization for long-CoT

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未配置（项目无 `external_review.paperreview_ai.enabled` 设置）。

---

## Overall Assessment

**评分: Weak Reject (2.5/5)**
**置信度: 4/5**（两位 Reviewer 均具备 KV cache compression + 统计方法背景，交叉验证后达成高度共识）

论文提出了一个有价值的 empirical finding——compound sparsity severity 的 phase-strategy interaction——统计方法论优于多数 ML 论文，random eviction 作为 falsification control 设计巧妙。DeepSeek 上的主实验结果可信且有部署启示。

但当前论文有**实质性缺陷**阻碍接收：
1. **论文未完成**：40+ placeholders 包括核心 Table 和 Abstract，以此状态提交将被 desk reject
2. **Cross-architecture generalization 被 overclaim**：LLaMA 证据极弱（1/4 significant, ~1/40 magnitude, random eviction 也有 phase gradient），不支撑 Title/Abstract 的 framing
3. **泛化范围过窄**：50 题 MATH-500，无 power analysis，无其他 reasoning benchmark
4. **机制分析 correlational only**：entropy-discrimination collapse 在 Qwen 上仅部分 replicate

如果 (1) 填充所有数据并确认 cross-arch 结论、(2) 诚实限定 claim scope、(3) 补充 power analysis 和 segmentation sensitivity——论文有潜力达到 borderline accept / Findings track。当前状态建议 revise and resubmit。

---

## Detailed Comments

### Per-Section Notes

**Abstract**: 过密（14 行 10+ 统计量）；LLaMA 细节应移至 Results；至少一处 placeholder 未填。

**§1 Introduction**: Contribution 2 "replicates across three models spanning two architectures" 需降级措辞。整体写作清晰。

**§2 Related Work**: 对 HIES (2025) 讨论严重不足——一句话提及但未在 Analysis 中对比。可能遗漏 RLKV/LongFlow/PM-KVQ。

**§3 Background**: G 定义在 II_high → 0 时数值不稳定，需 CI 或降级为辅助指标。Phase segmentation 引用 ThinKV 但方法不同，需修正措辞。

**§4 Methodology**: 缺 power analysis；排除标准未报告；symmetric sparsity 假设未讨论；sampling 分层方案缺失。

**§5 Results**: Table 1-2 (DeepSeek) 可信；Table 3 (LLaMA) 完全空白；Spearman ρ=1.0 on 4 points 被 over-interpret；Table 1 vs Table 4 数字差异未解释。

**§6 Analysis**: "Entropy-Discrimination Collapse" 标题过于 assertive for correlational evidence；Qwen s=0.25 entropy reversal 的 "model-dependent amplifier" 解释 ad hoc；需与 HIES 做 explicit comparison。

**§7 Discussion**: Oracle pilot experiment 数据全部为 placeholder——这是论文唯一走向 actionable mitigation 的部分，缺失严重影响 impact。LLaMA architecture-dependent 讨论诚实但与 title/abstract framing 矛盾。

**Limitations**: 坦诚且全面，但 LaTeX 注释中的 REVIEWER-ATTACK/REBUTTAL 预设回应应删除。

**Appendix**: Multiplicative null verification (A) 是加分项；其余 appendix 有大量 placeholder。s=0.35 实验仅一句话提及。

**References**: 29 篇引用均为真实论文，无幻觉引用。h2o-neurips2023 缺 title 字段；3 篇 author mismatch。
