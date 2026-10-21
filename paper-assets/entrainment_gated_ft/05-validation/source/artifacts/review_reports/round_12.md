---
round: 12
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T09:00:29.911221+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 12 审稿报告

**论文**: Per-Example Predictive Multiplicity in Hybrid Linear Recurrent Architectures
**Venue**: EMNLP 2026 (ARR May 2026 cycle, Long Paper)
**Reviewer 编排**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 写作质量）
**交叉分享**: 完成（R1→R2, R2→R1）
**审稿轮次**: 1 轮收敛（关键问题达成共识，novelty 分歧为合理审美差异）

---

## Summary

本文利用 Wang et al. (2025) 的受控 model zoo（3 种 hybrid linear recurrent 架构 × 5 个 attention ratios × 2 个规模 = 30 配置），系统分析了 hybrid recurrent 架构在 aggregate 指标等价下的 per-example predictive multiplicity。核心发现：(1) per-example multiplicity 随 task 类型变化（α = 0.14–0.30），pairwise Jaccard 始终 ≤ 0.10；(2) LAMBADA 上有 exploratory evidence 表明 aggregate convergence 与 per-example divergence decoupled（Bonferroni-adjusted p = .100，未达常规显著性）；(3) Majority vote 无法利用 15–45% 的 per-example disagreement，而 oracle accuracy 显示 7–14pp 未被利用的互补性。

## Strengths

**S1. 受控实验设计出色。** Wang et al. (2025) model zoo 控制了 training data/tokenizer/hyperparameters，仅变化架构和 attention ratio，是隔离 architectural effects 的理想实验设置。显著优于从 HuggingFace 随意收集模型进行比较。（R1, R2 共识）

**S2. 统计方法论透明度 above-average。** §3.5 主动披露 n=5 ordinal levels 的 power limitation（仅 ρ=±1.0 达 p<.05）、BCa CI 的 heuristic 性质（n=3 架构 degenerate resamples）、Bonferroni 校正的 exact calculation、one-sided vs two-sided test 对比。多数 NLP 论文不会报告 power analysis。（R1, R2 共识）

**S3. Per-example multiplicity findings 扎实。** 低 Jaccard（≤ 0.10, 所有 p < .01）、task-dependent α（0.14–0.30）、normalized effect size 排除 floor effect（仅达 achievable range 的 6–7%）——这些描述性统计不依赖争议性假设检验，是论文最 robust 的贡献。（R1, R2 共识）

**S4. Confidence margin 分析增加 mechanistic 深度。** AUC 0.70–0.74 的 within-architecture 预测力 + rescue thresholds architecture-invariant（spread 1%）vs disruption thresholds vary 47% 的不对称性，超越简单的 agreement counting，为理解 *why* architectures diverge 提供了线索。（R1, R2 共识）

**S5. Appendix 极其充实。** ~10 页 appendix 覆盖 GDN confound 分析、attention weight 分析、cross-scale 对比、complementarity decomposition、subsample sensitivity 等 20+ 个 sensitivity analyses，为主文 claims 提供全面补充支撑。（R1, R2 共识）

**S6. Jaccard saturation pattern 跨 benchmark 一致。** Per-example Jaccard 在首个 attention level（~4%）即饱和至 ~0.095，在全部四个主 benchmark 上成立（all ρ ≤ 0.80, p ≥ 0.333）——这是具有实践意义的具体发现。（R1, R2 共识）

## Weaknesses

### Critical

**C1. Convergence claim 的叙事权重与证据强度严重不匹配。**（R1-N1 Critical + R2-N1 Critical，交叉共识）
- LAMBADA convergence（ρ = −1.0）是论文核心叙事之一，但：Bonferroni-adjusted p = .100 未达 α = 0.05；排除 GDN 后降至 ρ = −0.7, p = .233；GDN h3-1 使用 16 heads（其他配置 32），存在 confound；在 340M scale 上不成立（ρ = −0.50, p = .45）；10 个 benchmarks 中仅 LAMBADA 一个显示此趋势；全 10 benchmarks Bonferroni (α/10=0.005) 下连 LAMBADA 都不显著。
- 然而约 40% 正文空间用于 convergence 分析（§4.1 + §4.3/§4.4 convergence 部分），与 exploratory 定性严重不匹配。9/10 benchmarks 的 ρ 值不显著但 §4.1 仍大量讨论这些趋势。
- **两位 Reviewer 共识：需大幅压缩 convergence 叙事权重，将重心转移到更 robust 的 per-example multiplicity findings。**

**C2. 单训练 run 导致 architecture 与 seed 效应完全混淆。**（R1-N2 Critical + R2-N2 Critical，交叉共识）
- 每个配置仅一次训练 run，无法区分 architecture-specific vs seed-specific 效应。McCoy et al. (2020) 和 MultiBERTs (Sellam et al., 2022) 已证明同一架构不同 seed 之间也存在显著 per-example disagreement。
- Within- vs cross-architecture Jaccard 的 3× gap（§4.3）作为 proxy evidence，但这本身也受 seed 影响——within-architecture Jaccard（跨 attention ratio）与 cross-architecture Jaccard（跨架构）比较的是不同维度，不能直接作为 architecture-dominance proxy。
- 论文未与 seed-based multiplicity 基线做定量对比。无法确定 cross-architecture α = 0.14–0.30 是否显著大于 within-architecture seed variation 所产生的 α。
- **两位 Reviewer 共识：结构性限制，不可在当前 model zoo 框架内修复。需在 Limitations 中更充分讨论，最好引用 MultiBERTs 等文献的 seed-based α 做 contextual comparison，或将 contribution 措辞进一步软化。**

### Major

**M1. 新颖性主要在 setting 而非 method/theory。**（R2-W2 Major; R1 给 Excitement 4/5 但 R2 给 2.5/5，分歧未完全解决）
- 核心分析工具——Jaccard similarity、ambiguity α、permutation test、helped/hurt 分类——全部来自先前工作。方法论增量贡献薄弱。
- "Decoupling" 发现（aggregate convergence vs per-example divergence）部分可预期——aggregate means 收敛但 individual-level variation 持续是 ecological fallacy 的变体。真正新颖的是 Jaccard 在首个 attention level 饱和的 specific pattern。
- R1 认为研究问题本身 genuinely novel（hybrid recurrent architectures 中 per-example multiplicity 此前未被系统研究），给 Excitement 4/5；R2 认为缺乏方法论或理论创新，给 Excitement 2.5/5。
- **Director 判断：novelty 足以支撑 Findings，但不足以达到 main conference threshold。**

**M2. Practical implications 缺乏验证。**（R2-W2 Warning）
- MV 失败（LAMBADA: −0.2pp）但 oracle 显示 +7–14pp gap。论文已有 confidence margin AUC 0.70–0.74 基础，但未尝试 confidence-based selection 或任何 informed combination method。
- Oracle gap 的 "untapped complementarity" 被用于支撑 "selection methods beyond naive ensembling" 的建议，但缺乏实证验证。

### Warning

**W1. 因果语言在 observational design 下残余越界。**（R1-W4 + R2-W4，交叉共识）
- 多处残余因果表述：Abstract "attention provides direct token-level access"、§4.1 "attention reduces differences"、§4.1 "creating divergent retrieval capacities that attention may bypass"、§5 "each backbone develops architecture-specific response patterns"、§4.2 "thresholds that produce the observed divergence"。
- 在 observational design 下应统一使用关联语言。

**W2. "Predictive multiplicity" 术语与 Rashomon set 原始定义的关系需澄清。**（R2-W1 Warning）
- Marx et al. (2020) 定义 multiplicity 为 Rashomon set 内近最优模型的分歧。本文应用于不同架构（不同 inductive biases, aggregate σ_pure = 2.41），虽然 α 指标计算正确，但术语暗示 Rashomon set 语境可能误导。
- 建议在 §2/§3 明确区分 variation source。

**W3. GDN h3-1 16-head confound 正文处理不充分。**（R1-W1 Warning）
- 移除 GDN 后 MMLU 从 ρ = −0.7 反转到 +0.7，正文 §4.4 仅一句带过。Table 1 有 ‡ 脚注但不够醒目。

**W4. Abstract 信息密度过高。**（R2-W3 Warning）
- ~200 词内 15+ 个数字，第一次阅读无法提取核心 message。建议削减至 5–6 个关键数字。

**W5. Bonferroni 校正 confirmatory/exploratory 划分缺乏预注册。**（R1-W3 Warning）
- 事后声明 6 confirmatory benchmarks，无外部 timestamp。Wang et al. (2025) 原始论文已有 benchmark 结果——作者可能已了解趋势。Appendix A 已含 10-benchmark sensitivity check（adj-p = 0.170），但正文未充分讨论。

**W6. Binary decomposition 丢弃 continuous confidence 信息。**（R1-W2 Warning）
- Confidence 0.49→0.51 = "helped"，0.51→0.99 = "unchanged"。§4.2 和 Appendix O 补充了 confidence margin 分析，但与 Jaccard 分析分离——未展示 continuous threshold 下 Jaccard 如何变化。

### Minor

- lm-eval-harness 版本标为 "v0.4.x"，应具体到 minor version；某些 benchmark 默认不使用 greedy decoding，需澄清（R1）
- Table 2 中 α 值的 scale 不直观，缺乏 effect size 参照（R1）
- Appendix L "Transformer Entrainment Comparison" 中 "entrainment" 未定义（R2 初审）
- Figure 1(b) y 轴范围（~0.05–0.12）使 saturation 视觉上不够明显（R2）
- 正文 pp.3–5 连续 3 页纯文本无 display items（视觉审查）

## Reviewer Consensus

以下问题两位 Reviewer 达成共识：
1. **[AGREE] Convergence 证据不足 + 叙事过重**：两位独立认为 convergence 仅基于单一 benchmark、marginal significance、GDN-dependent、scale-dependent，但占 ~40% 叙事空间，严重不匹配。
2. **[AGREE] Seed confound 是核心结构性限制**：两位独立认为单 run 设计无法区分 architecture vs seed 效应，3× Jaccard gap 是间接证据。需更充分讨论并与 MultiBERTs 等做 contextual comparison。
3. **[AGREE] 因果语言需系统修正**：两位均发现残余因果表述，建议统一改为关联语言。
4. **[AGREE] Per-example multiplicity findings 是最强贡献**：低 Jaccard、task-dependent α、normalized effect size 排除 floor effect——这些不依赖争议性假设检验。
5. **[AGREE] 统计透明度值得赞赏**：power limitations、CI heuristic 性质、Bonferroni exact calculation 的主动披露远超 NLP 论文平均水平。
6. **[AGREE] Findings 级别是当前论文的合理定位**：即使在 novelty 评价上分歧（见下），两位均认为论文至少达到 Findings 水平。

## Reviewer Divergence

1. **Excitement / Novelty 评价**：R1 给 Excitement 4/5（认为研究问题本身 genuinely novel，per-example multiplicity 在 hybrid recurrent architectures 中此前未被系统研究）；R2 给 2.5/5（认为核心贡献是已有指标在新 setting 的应用，decoupling 是 ecological fallacy 变体，缺乏方法论或理论创新）。这是关于 "empirical novelty of setting vs. methodological novelty" 的合理审美分歧。
2. **Overall Score**：R1 给 3.5（Borderline Conference），R2 给 3.0（Findings）。分歧源于 novelty 评价。
3. **页数问题**：R2 初审标记正文超 8 页为 Critical，但 PDF 验证和视觉审查均确认正文在 8 页内（Limitations 从 p8 底部开始，不计入页数）。R2 交叉回应中已撤回。

## Questions

以下为两位 Reviewer 提出的关键问题（去重合并）：

1. **Seed baseline**: Model zoo 中是否有任何不同 seed 同架构的 pair？如有，能否报告 within-architecture seed-based Jaccard 与 cross-architecture Jaccard 做定量对比？（R1-Q1, R2-Q1）
2. **全局 Bonferroni**: 全 10 benchmarks Bonferroni 校正（α/10=0.005）下，LAMBADA p=0.017 也不显著——整篇论文在严格多重比较下没有一个显著结果。如何回应？（R1-Q2）
3. **Continuous confidence**: 是否分析过 raw log-likelihood（非 binary acc_norm）计算的 per-example 效应？Continuous threshold 下 Jaccard 是否 qualitatively 一致？（R1-Q3, R2-Q5）
4. **MMLU GDN confound**: MMLU exclusion-GDN 后 ρ 从 −0.7 反转到 +0.7，MMLU convergence 是否完全由 GDN 16-head confound 驱动？（R1-Q4）
5. **Scale 限定**: 340M 下 convergence 消失，是否应限定 convergence claim 为 "1.3B scale only"？（R1-Q5, R2-Q5）
6. **Confidence-based selection**: 已有 confidence margin AUC 0.70–0.74，是否尝试过 confidence-based selection 替代 naive majority vote？（R2-Q3）
7. **Decoupling 数学推导**: Aggregate convergence 与 per-example Jaccard saturation 的关系是否可从数学上推导？是否因 binarization 对 small probability shifts 不敏感？（R2-Q1）
8. **Pre-registration**: Task taxonomy 声称 pre-specified，但无外部 timestamp。能否提供 commit history 或预注册记录？（R2-Q4）

## Missing References

两位 Reviewer 建议补充的引用（去重）：

1. **Kuncheva & Whitaker (2003)** — ensemble diversity measures（Q-statistic, disagreement measure）。Jaccard 本质是 diversity measure，应讨论选择理由。（R2）
2. **Fisher et al. (2019), Semenova et al. (2022)** — Rashomon set 理论框架，为 multiplicity 何时出现提供理论基础。（R2）
3. **Wortsman et al. (2022)** — Model Soups，与 ensemble/oracle 讨论直接相关。（R2）
4. **Guo et al. (2017)** — On Calibration of Modern Neural Networks，confidence margin 差异可能由 calibration 差异部分解释。（R2）
5. **Dodge et al. (2020)** — seed variation 在 fine-tuning 中对 per-example 行为的影响。（R2）

## External Review

外部审稿未配置，本轮未请求。

## Visual Layout Check（非评分项）

视觉审查已完成（状态: done）。

**Findings:**
- **Warning**: 正文 pp.3–5 连续 3 页纯文本（Related Work + Method），无 figure/table/equation 穿插，审稿人在此段会失去视觉锚点。建议在 Method 中加入方法概览图或关键公式 display math。
- **Warning**: 主正文仅 4 个 display items（2 figure + 2 table），对实证为主的 8 页论文偏少（通常 5–8 个）。核心实验结果大量依赖 inline 数字。
- **Warning**: Figure 1（p2）和 Figure 2（p6）之间跨越 3 页无 display item。
- **Warning**: 末页（p20）仅使用 ~25% 空间。
- **Info**: Figure 1 子图 axis labels 偏小；Figure 2 灰色调区分度有限；Tables 使用 booktabs 风格，格式规范；无排版缺陷；参考文献格式统一。
- **关键确认**: 正文在 8 页内（Limitations 从 p8 底部开始），格式合规。

## Overall Assessment

**Overall Score: 3.0 (Findings)**

**评分分布**: R1 = 3.5, R2 = 3.0, Director 综合 = 3.0

### 评分理由

**支持 3.0+ 的因素：**
- 受控实验设计（matched training, single variable）是该研究问题的 gold standard approach
- Per-example multiplicity findings（低 Jaccard、task-dependent α）由描述性统计直接支持，robust 且有实践意义
- 统计透明度 above-average（主动披露 power limitations, CI heuristic nature）
- Confidence margin 分析提供了超越 agreement counting 的 mechanistic insight
- Jaccard saturation pattern 跨 4 个 benchmark 一致，是 non-trivial 的 empirical finding
- 充实的 sensitivity analyses（~10 页 appendix, 29 个表格）

**限制在 3.0 的因素：**
- **Convergence claim 证据不足但叙事过重**（Bonferroni p=.100, GDN-dependent, LAMBADA-only, scale-dependent → ~40% 叙事空间）
- **Seed confound 无法排除**——单 run 设计使核心 claim（"architectural variation drives structured per-example divergence"）缺乏 definitive evidence
- **新颖性主要是 observational**——核心工具全来自先前工作（Jaccard, α, permutation tests），insight 有价值但未推进方法论或理论
- **Practical implications 未 closed**——发现 oracle gap 但未提供 actionable 解决方案
- **因果语言残余**——observational design 下仍有多处因果表述

**从 3.0 提升至 3.5+ 的路径：**
1. 大幅压缩 convergence 叙事（降至 ~20% 叙事空间或合并为 decoupling 的背景信息）
2. 补充 seed baseline 定量对比（引用 MultiBERTs α/Jaccard，或在 model zoo 内找 proxy）
3. 增加一个 confidence-based selection 的 proof-of-concept（已有 AUC 0.70–0.74 基础）
4. 在 §2/§3 明确区分本文的 multiplicity source（architectural variation）与 Marx (2020) 原始定义（Rashomon set）
5. 全文因果语言系统替换为关联语言

**置信度: 4/5** — 两位 Reviewer 仔细阅读了全文及全部附录，熟悉 predictive multiplicity、underspecification 和 hybrid architecture 相关文献。关键问题达成共识，novelty 分歧为合理审美差异。

## Detailed Comments

### §1 Introduction
- Contribution 1（per-example multiplicity）措辞合理——"arises under matched training conditions where the only controlled variable is the recurrent backbone"
- Contribution 2（decoupling）应进一步降级——convergence 证据 exploratory 但 C2 措辞仍暗示 robust finding
- "aggregate convergence and per-example divergence follow different trajectories" 应标注 LAMBADA-specific + exploratory

### §3 Method
- §3.5 Power considerations 段优秀，但应在 §4.1 首次引用 LAMBADA p=.017 时再次提醒
- §3.4 binarization bias 方向讨论（"conservative bias strengthens the multiplicity claim"）是好的补充
- lm-eval-harness 版本应具体化

### §4.1 Task-Specific Convergence
- 需大幅压缩。当前 ~40% 叙事空间给一个 Bonferroni p=.100 的 exploratory finding 不匹配
- Table 1 应更醒目地区分 LAMBADA（唯一显著）与其余 9 个不显著的 benchmark——当前仅 bold ρ 不够
- 对 9 个不显著 benchmark 趋势的讨论应明确标记为 descriptive（无统计支撑）

### §4.2 Per-Example Divergence
- 论文最强部分。低 Jaccard、normalized effect size、confidence margin mechanism 构成多层次证据
- Rescue/disruption 不对称性是有趣的 mechanistic finding
- 建议将 confidence margin 的关键结果（AUC, threshold asymmetry）从 Appendix 提升到主文

### §4.3 Decoupling
- Jaccard saturation 的具体 pattern（4% attention 即饱和）是论文的 non-trivial 贡献
- 但 "decoupling" framing 过于宏大——aggregate-vs-individual divergence 本身是 known statistical possibility
- 建议以 per-example saturation 为主线，convergence 作为对比背景

### §4.4 Robustness
- GDN exclusion 对 MMLU 的影响（ρ 反转）应在此节显著提及，不仅仅 LAMBADA 弱化

### §5 Conclusion
- "per-example audits whenever hybrid designs achieve comparable aggregate scores" 过度泛化——应限定为 "within the scope of the architectures and conditions studied"
- MV failure + oracle gap 数据有价值，但建议加一句 "future work should explore informed selection methods"