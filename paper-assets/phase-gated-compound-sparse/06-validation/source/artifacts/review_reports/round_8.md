---
round: 8
overall_score: weak reject
timestamp: 2026-05-15T14:01:36.816342+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# Round 8 Consolidated Review Report
## Phase-Modulated Compound Sparsity: Strategy-Dependent Severity Gradients in Mathematical Reasoning Models
**Venue**: EMNLP 2026 Main Conference (via ACL Rolling Review)
**Reviewers**: R1 (方法严谨性 + 实验设计), R2 (新颖性 + 相关工作 + 写作)
**评分**: R1 3/5, R2 2.5/5 → **综合: Weak Reject (main conference) / Borderline Accept (Findings track)**

---

## Summary

本文研究 compound sparsity（attention head pruning + KV cache eviction 联合）在数学推理模型中的 phase-dependent severity。通过在 DeepSeek-R1-Distill-Qwen-7B (n=496) 和 Qwen2.5-7B-Instruct (n=475) 上的实验，作者发现：(1) importance-based eviction 的 severity gradient 远大于 random eviction（amplification ratio G=7.5×–79.8× vs ≈1×）；(2) DeepSeek 上出现 strategy ranking crossover（model-dependent）；(3) discrimination collapse 作为 correlational diagnostic。论文自我定位为 diagnostic study，统计方法论严谨，robustness 验证充分。

---

## Strengths

**S1. 统计方法论在同类论文中罕见的严谨度** [R1+R2 共识, Soundness 3.5/5]
Bootstrap CI (B=10,000)、Wilcoxon signed-rank、Bonferroni + BH-FDR 双重校正、Jonckheere-Terpstra dose-response test、paired permutation test、post-hoc power analysis——每一步都有合适的非参数检验和多重比较校正。

**S2. 充分的多维度 robustness 验证** [R1+R2 共识]
min_phase_length 敏感性、分割粒度（tercile/quartile/quintile）、outlier winsorization (5%/10%)、multiplicative null、BH-FDR correction——核心结论经多角度交叉验证。

**S3. Crossover effect 有不可预测的定性新颖性** [R1 主张, R2 未进一步反驳]
Importance-based eviction 在 high-sparsity phase 优于 random 但在 low-sparsity phase 劣于 random 的 strategy ranking reversal，不可从 ThinKV + HIES 等单轴工作组合推导。R1 在交叉回应中成功论证了这一点。

**S4. 诚实且充分的 limitation 披露** [R1+R2 共识]
Correlational mechanism、单一基准、LLaMA 弱结果、pilot mitigation 失败——论文对自身弱点的讨论比大多数投稿更坦诚。

**S5. 清晰的 diagnostic study 定位与精巧的对照组设计** [R1+R2 共识]
Random eviction 对照组有效隔离了 strategy-specific 效应。Diagnostic study 自我定位一致。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1. [critical] Additive null 假设与论文自身 causal coupling 论述存在内在矛盾** [R1 提出, R2 同意]
论文以"两轴作用于不相交维度"正当化 additive null (II = r_b − r_a − r_k + 1)，但论文自身在 §3 明确指出 "head pruning alters the importance ranking used for eviction"，§6 详细分析 discrimination collapse 即两轴的直接因果耦合。Multiplicative null 下 G=58–211（additive G=7.5–79.8 的 4–8×），两种 null 的数值差异直接影响 headline 数字的含义。II 是论文所有定量结论的根基。
**建议**: (a) 在 §3 正面论证为什么存在因果耦合却仍采用 additive null（不能靠一句"不相交"带过）；(b) 主文并列报告两种 null 下的 G 和 Δ。

**N2. [critical] 单一基准 MATH-500 严重限制泛化性** [R1 提出, R2 同意]
所有定量结论仅基于 MATH-500。标题 "Mathematical Reasoning Models" 暗示一般性，但不同推理任务的 attention dynamics 可能截然不同。作为 diagnostic study，单一数据源的诊断外部效度存疑。
**建议**: 增加至少一个不同类型推理基准（GSM8K 最低成本，HumanEval/GPQA 更有说服力），哪怕仅 n=50 profiling 规模。

**N3. [critical] PPL construct validity: answer-region 分析反而削弱核心叙事** [R1 提出 Must-Fix, R2 升级同意]
§5.7 报告 93.2% 答案 token 在 high-sparsity phase (G ≤ 1)，答案 token PPL degradation (1.3–5.3×) 远低于推理痕迹 (5.7–43.5×)。论文描述为 "partially shielded"，但更准确的解读是：巨大 G 值集中在对最终答案影响最小的 phase。缺乏直接准确率测量使 "severity" 的实际含义悬而未决。论文试图说服读者 compound severity 是严重问题，但自己的分析表明最终答案可能基本不受影响——framing 与证据之间存在根本张力。
**建议**: (a) 在至少一个 sparsity level 上测量实际 MATH-500 准确率变化；(b) 如果主要影响推理痕迹质量而非最终答案，重新框定 severity gradient 的价值定位。

**N4. [critical] 数字声明 "3–30×" 包含非显著 random 条件** [R2 提出, R1 同意]
Abstract/Contribution 1 中 "3–39×" 或 "3–30×" 的上界取自 s ≤ 0.20 的条件，而这些条件下 random Δ 非显著（CI spans zero）。在 random Δ 统计显著的条件 (s ≥ 0.25) 下，实际比率为 DS 15–17×，QW 2.7–3.5×，跨模型 2.7–17×。
**建议**: 修正为 "3–17× where both strategies show significant phase gradients"，或明确标注上界来自非显著条件。

### Should-Fix

**W1. [warning] Pilot mitigation (oracle 18%, gate FAIL) 削弱 diagnostic value 叙事** [R2 提出 Must-Fix, R1 同意]
§7 声称 "severity gradient provides a natural signal for allocating compression budgets"，但 oracle recovery 仅 18%（低于 30% pre-registered gate），heuristic 32% 但 CI 跨 zero。叙事内部矛盾。
**建议**: 移除 pilot 或移至 Appendix 附失败分析，避免与 "natural signal" 正面叙事冲突。

**W2. [warning] Discrimination collapse 解释力存在 order-of-magnitude 缺口** [R1+R2 共识]
Importance/random Gini drop 差异 < 10%（如 s=0.25: −0.065 vs −0.060），但 severity 差异 15–17×。r=0.62–0.76 structural specificity 证据部分 circular（Frobenius norm 与 Gini 共享 magnitude sensitivity）。Entropy redistribution 仅 2/4 Qwen 条件复现。
**建议**: 坦诚讨论 Gini drop 与 severity divergence 之间的定量缺口；降低对该机制的依赖。

**W3. [warning] "Cross-model replication" 实为同架构不同训练范式** [R1+R2 共识]
DeepSeek 和 Qwen 共享 Qwen2ForCausalLM。LLaMA (n=49) 效应量 ~1/40 且 strategy contrast 大幅减弱，暗示定量特征可能 Qwen2 特有。
**建议**: 使用 "cross-training-paradigm replication on same architecture"，更突出讨论 LLaMA 结果对泛化性的负面含义。

**W4. [warning] Phase segmentation 缺乏理论先验** [R1+R2 共识]
基于 attention sparsity tercile 的分割纯数据驱动。Robustness checks (mpl sensitivity, quartile/quintile) 部分缓解，但未独立论证 attention sparsity 作为 reasoning phase boundary 的合理性。
**建议**: 引用独立文献支持 attention sparsity 作为 phase proxy 的合理性，或讨论替代分割方法的可能结果。

**W5. [warning] Novelty argument: Introduction 的 "linear combination" 反驳为 strawman** [R2 提出, R1 部分同意]
没有人会预期两个非线性交互的压缩轴产生 "linear combination"。ThinKV + HIES 的组合可定性预测 phase-modulated severity。但 R1 成功论证 crossover 和 dose-response 的严格单调性是不可预测的。
**建议**: 重写 novelty argument，聚焦 crossover 和 dose-response 的不可预测性，而非 strawman 反驳。同时在 headline claims 中并列 Δ 和 G，明确讨论 G 的 near-zero denominator 放大效应。

**W6. [warning] Sparsity 范围窄 (s=0.15–0.30, 仅 4 点)** [R1 提出, R2 部分同意]
4 点足以验证 monotonicity (JT test) 但不足以刻画 G(s) functional form。实际部署常涉及更高 sparsity (s > 0.50)。
**建议**: 增加 1-2 个更极端的 sparsity level。

**W7. [warning] 缺失引用** [R2 提出, R1 同意]
- ThinK (ICLR 2025): channel-level KV pruning compound compression
- ForesightKV (arXiv 2602.03203): reasoning-specific learned importance
- Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026): compression order interaction, Progressive Intensity Hypothesis

**W8. [warning] "Discrimination collapse" 命名可能混淆** [R2 提出, R1 部分同意]
"Collapse" 在 ML 中有 mode collapse、neural collapse 等既有含义。
**建议**: 改为 "importance discrimination collapse" 或 "score discrimination flattening"。

---

## Reviewer Consensus

两位 Reviewer 达成以下关键共识：
1. **PPL-only 度量 + answer-region shielding 削弱 practical significance** (R1-N3 = R2-W5→升级) — 最终答案 token 大多在 G≤1 的 phase，severity gradient 的实际影响可能被系统性高估
2. **Pilot mitigation gate FAIL 削弱 diagnostic value narrative** (R1-W5 = R2-N2)
3. **单一基准限制泛化性** (R1-N2, R2 AGREE)
4. **数字声明不一致** (R2-N3, R1 AGREE)
5. **Discrimination collapse 解释力不足** (R1-W2, R2 AGREE)
6. **统计方法论堪称典范** (两位 Soundness 3.5, Reproducibility 4)

## Reviewer Divergence

唯一实质分歧在 **Excitement / Novelty** 的评估：
- **R1 (3/5)**: Crossover effect 是不可从单轴工作推导的定性新颖性，为论文提供了独立于定量放大之外的贡献
- **R2 (2.5/5)**: 核心发现"importance-based eviction 在 attention 分散的 phase 更差"定性上可预期；G 指标因 near-zero denominator 被人为放大

经交叉回应，R1 关于 crossover 新颖性的论证更有说服力（R2 未进一步反驳）。但 R2 关于 G 指标放大效应的关切同样成立。**综合判断**：论文有真正的新颖性（crossover + dose-response），但 headline framing 过度依赖被放大的 G 值。

---

## Questions for Authors

1. **Additive vs. multiplicative null**: 两种 null 下 G 差异 4–8×，作者如何论证读者应信赖 additive null 的数字？特别是当论文自身描述了两轴的因果耦合时？
2. **Answer-region shielding**: 93.2% 答案 token 在 G ≤ 1 的 phase。是否有证据表明推理痕迹的 PPL 退化会 cascade 到最终答案质量？如果不会，论文的实际 implication 是什么？
3. **Profiling vs. full G discrepancy**: 已确认为统计量定义差异（ratio-of-medians vs median-of-per-problem-ratios）而非 sample size artifact。但请在正文中更显著地标注此差异，避免误读。
4. **Crossover model-dependence**: DeepSeek 展现 crossover 但 Qwen 不展现。什么模型属性决定 crossover 是否出现？缺乏 explanatory hypothesis 是明显弱点。

---

## Missing References

| 论文 | 相关性 | 来源 |
|------|--------|------|
| ThinK (ICLR 2025) | Channel-level KV pruning compound compression | R2 |
| ForesightKV (arXiv 2602.03203) | Reasoning-specific KV eviction with learned long-term importance | R2 |
| Prune-then-Quantize or Quantize-then-Prune? (ICLR 2026) | Compression order interaction, Progressive Intensity Hypothesis | R2 |
| PPL-accuracy nonlinear relationship formal analysis | 加强 §5.7 讨论 | R1 |

---

## External Review (Stanford Agentic Reviewer)

未配置外部审稿。

---

## Overall Assessment

**Score: Weak Reject (for main conference) / Borderline Accept (for Findings track)**
**Confidence: 4/5** (两位 Reviewer 均仔细阅读全文含附录)

这是一篇执行力出色的诊断研究。统计方法论在 KV cache compression 领域属上乘，robustness 验证近乎完备，crossover effect 是真正新颖的发现。

但四个核心问题将其限制在 Findings 级别：

1. **Construct validity gap**: PPL 度量的 practical significance 被论文自身的 answer-region 分析削弱（93.2% 答案 token 在 severity 最低的 phase），且无直接准确率验证
2. **Single benchmark**: MATH-500 独木难支泛化性——一个额外基准（哪怕 n=50）即可大幅增强
3. **Additive null 矛盾**: 论文核心度量 II 的 null hypothesis 与论文自身的 causal coupling 叙事不自洽，headline G 值缺乏可靠解释基准
4. **Numerical inconsistency**: "3–30×" 声明混入非显著条件比率

**升级路径**：(a) 增加一个额外基准 + 至少一个 sparsity level 的准确率数据；(b) 主文并列报告 additive/multiplicative null 结果；(c) 修正数字声明；(d) 移除或下移 pilot experiment。完成这些修改后，论文有望达到 main conference 水平。

---

## Detailed Comments

### Section 1 (Introduction)
- ¶3 的 "linear combination" 论证是 strawman——改为聚焦 crossover 和 dose-response 的不可预测性
- Contribution 1 的 "3–39×" / "3–30×" 需修正为 significant-only 范围

### Section 3 (Background)
- Additive null 的论证（"disjoint dimensions"）需正面回应 causal coupling 的存在
- Phase segmentation 的 attention sparsity proxy 缺乏独立理论支持

### Section 5 (Results)
- §5.4 标题 "Replication Across Training Paradigms" 已改进（R7），但正文仍应更显著地讨论 LLaMA ~1/40 效应量对泛化性的负面含义
- §5.7 Answer-region 分析需重新框定——当前 "partially shielded" 用词淡化了 93.2% 答案 token 在 G≤1 phase 的含义

### Section 6 (Analysis)
- Discrimination collapse 作为 correlational diagnostic 定位合理，但 Gini drop ~10% vs severity 15–17× 的定量缺口需正面讨论
- 命名建议改为 "importance discrimination collapse"

### Section 7 (Discussion)
- Pilot experiment 移至 Appendix 或删除——oracle 18% recovery 直接反驳 "natural signal" 声明
- G 的 near-zero denominator 放大效应需在 headline claims 中明确讨论

### Format
- 确认正文是否严格在 8 页限制内
- 清理 LaTeX 源码中的 `% exp_id:` 注释
- LKV 引用修正（"Anonymous" → arXiv ID）
- Table 3 caption 明确 Δ 的计算方式