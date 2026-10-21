---
round: 18
review_mode: fresh
overall_score: 3.0 = Findings
timestamp: 2026-05-25T21:46:34.052271+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 20 (Fresh Review)

**论文**: A Systematic Comparison of Execution-Free Verification Formulations for Code Repair
**Venue**: EMNLP 2026 (via ARR)
**Reviewers**: R1（方法严谨性、实验设计、统计分析）, R2（新颖性、完整性）
**模式**: Fresh Review（无历史记忆）

---

## Summary

本文对代码修复中三种 execution-free 验证方案（CLS 分类、CWM 输出生成、TRAJ 轨迹评分）进行首次系统受控对比，在 ≤8B LoRA 微调下跨两个 LLM 家族（Qwen3、DeepSeek-Coder）、两个复杂度层级（function/repo-level）控制实验。核心发现：函数级 CLS-CWM 统计等价（TOST p=0.007），CLS-TRAJ 等价在 Holm 校正后 inconclusive（p=0.128）；仓库级 CLS 领先 CWM 18-26pp，归因于 format collapse（53-74% unparseable）。统计框架包含 TOST + Holm-Bonferroni + clustered bootstrap + Bayesian ROPE + mixed-effects LPM。

---

## Strengths

**S1 [共识]. 统计分析深度远超同类 NLP 论文。** TOST 等价检验（而非仅 NHST）、clustered bootstrap 处理 within-problem 相关性、Holm-Bonferroni 多重比较校正、Bayesian ROPE、mixed-effects LPM——这套组合在 ACL/EMNLP 论文中极为罕见。

**S2 [共识]. 受控对比设计。** 固定 model capacity、training data、evaluation protocol，仅变化 verification formulation。多数先前工作在不同 formulation 间使用不同模型或数据，本文的控制变量设计是方法论改进。

**S3 [共识]. Failure mode taxonomy 有实用价值。** Format collapse / decision collapse / aggregation penalty 三分类（Table 4, §4.5），结合 Figure 4 量化分析，为从业者提供可操作的诊断框架。

**S4 [共识]. 消融覆盖面广。** LoRA rank、downsampling、few-shot prompting、majority voting、model scaling 等多维度排查 confound。对潜在混淆变量的排查意识强。

**S5 [共识]. Cross-family 验证。** Qwen3 + DeepSeek-Coder 两个独立家族方向一致，增强结论 robustness。

**S6 [共识]. 诚实的 Limitations。** §4.7 列出 5 个 confound，透明度值得肯定。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1 [Critical, 共识] TRAJ 训练配置差异严重混淆 CLS-TRAJ 等价结论**

R1-N1 提出，R2 完全 AGREE 并补充量化证据。

TRAJ 与 CLS/CWM 存在三重训练配置差异：(a) 标签粒度——TRAJ variant-level vs CLS per-test；(b) 数据量——repo-level ~400 vs ~70K 实例；(c) learning rate——2×10⁻⁴ vs 5×10⁻⁵。CLS-TRAJ TOST 在 Holm 校正后 adjusted p=0.128，不成立。Appendix J 的 seed-level 最小等价边际仅 ±0.37pp，说明即使微小的 SESOI 收紧也会推翻等价。Appendix B.6 的 downsampling 消融仅控制了数据量，**未控制 label granularity**——论文自身承认这点。

**要求**：将 "function-level equivalence" claim 限缩为 "CLS-CWM equivalence established; CLS-TRAJ inconclusive under current training configurations"。在正文显著位置（而非仅脚注/Appendix）标注 TRAJ 比较的三重混淆。Abstract 中 "all formulations achieve comparable accuracy" 需修正。

**MF2 [Critical→Should-Fix after cross-sharing, 分歧] Repo-level 因果语言需降级**

R1-N2 标 Critical：2-3 seeds 不支撑 "complexity moderates the classification-generation tradeoff" 因果叙述。R2 部分反驳：18-26pp 效应量远超 seed noise（SD 2-3pp），跨模型方向完全一致（Qwen3 +25.50pp, DeepSeek +18.53pp），format collapse 机制分析提供结构性解释（Table 4: 53-74% unparseable），足够支撑描述性结论。

**Director 裁定 Should-Fix**。R2 反驳有力——效应量极大 + 跨模型一致 + 机制分析。但 R1 关于因果语言的批评正确。**要求**：将 "complexity moderates" 改为 "CLS consistently outperforms CWM at repo level across both model families, associated with CWM's format collapse under increased output complexity"。

**MF3 [共识] Error complementarity 被过度声称**

R2-W2 提出，R1 完全 AGREE。Oracle combination 90.63% vs CLS 88.43%，gap 仅 ~2.2pp。Simple heuristics <0.4pp。论文自身承认 "complementarity is instance-specific, so simple heuristics are insufficient"（§4.4）。Figure 5 显示 oracle advantage 主要集中在 T=1（最难 route 的场景）。**要求**：从 key contribution 降级为 analysis finding。

**MF4 [共识] Abstract/Conclusion 的 claim 泛化性超出证据范围**

R2-W3 提出，R1 AGREE。Abstract "Our central finding is that code complexity moderates the classification-generation tradeoff" 是一般性结论，但证据仅来自 ≤8B LoRA。14B 数据（Table 2）显示 gap 从 ~2.6pp 缩窄到 ~1pp，趋势暗示更大规模下所有方法可能收敛。R1 补充：qualitative finding（format collapse 作为 failure mode）可能在更大规模持续，但 quantitative magnitude 缩小——论文应区分这两个层面。**要求**：Abstract/Conclusion 明确 "under ≤8B LoRA fine-tuning" 条件。

### Should-Fix（影响评分但不一票否决）

**SF1 [强共识] LPM vs GEE 矛盾必须在正文讨论**

R1-W4 提出，R2 交叉回应称 **"最重要的 Should-Fix"**。Appendix M 报告：LPM formulation×complexity interaction p<0.001（t=-23.7），但 GEE 对同一交互项 p=0.449——两种合理的统计模型给出相反结论。论文归因于 "limited clusters (k<25)"，但反向解释同样成立：LPM 在小 cluster 下 sandwich estimator 可能 size-distorted（Moulton, 1990）。**建议**：提升到正文 §4.6 讨论；补充 logistic regression 作为第三方验证。

**SF2 [分歧, Director 裁定 Should-Fix] 核心发现可预测性与 novelty**

R2-W1 标 Must-Fix：generation 在 repo-level format collapse 可从第一性原理预测。R1 反驳三点：(a) GenRM 先验文献指向相反方向——生成式验证在数学推理中优于判别式，代码中相反是 non-trivial 发现；(b) Function-level CLS-CWM 统计等价是 counter-intuitive——如果 CWM 天然劣势，function level 也应更差；(c) Failure mode 分布（format/decision/aggregation 的比例）不可先验推导。

**Director 裁定 Should-Fix**：R1 反驳有道理，但论文 framing 未充分利用这些 counter-intuitive 角度。**建议**：Introduction 明确 articulate 哪些先验被推翻；将 GenRM domain contrast 提升到主文（见 SF3）。

**SF3 [强共识] GenRM domain contrast 被埋在 Appendix**

R2-W4 提出，R1 AGREE（"全文最有洞察力的部分"）。p.22 Appendix 讨论了 GenRM 在数学推理中生成式优于判别式但在代码中相反，解释为 output space complexity（数学自然语言 vs 代码执行轨迹严格语法）。这一 domain-specific divergence 对 community 的指导价值可能高于 format collapse taxonomy 本身，但仅一段话在 Appendix。**建议**：提升到 §4.6 或独立 subsection，formalize "output space rigidity" 假设。

**SF4 [共识] TOST ±2pp 缺乏领域论证**

R1-W1 提出，R2 AGREE。Lakens (2017) 和 Wellek (2010) 是方法论引用，非对 ±2pp 阈值的论证。Figure 3 sensitivity analysis 显示 CLS-CWM 最小等价边际 ±1.63pp——如果 SESOI 设为 ±1.5pp，等价结论变得 marginal。**建议**：基于 verification accuracy 对下游 repair 成功率的影响量化 SESOI。

**SF5 [共识] Checkpoint 选择不一致**

R1-W2 提出，R2 AGREE。CLS val-based selection vs CWM final-epoch（因 NaN validation loss）。CWM convergence analysis（Appendix O）显示 eval loss 在 step 300-400 达最小值后递增，暗示 final checkpoint 可能过拟合。但 format collapse 从训练早期即存在，非 late-training artifact。**建议**：CWM checkpoint 消融或统一 early stopping。

**SF6 [共识] Sequence length 作为未控制 confound**

R1-W3 提出，R2 AGREE。CLS 输出 1 token vs CWM 需分配 context。跨模型 eval length 不同（Qwen3: 8192, DeepSeek: 4096）。seq4096→8192 仅 +0.81pp 且 unparseable rate 不变——sequence length 非 format collapse 主因，但仍是未完全控制的 confound。**建议**：报告 CWM 平均/P95 生成长度和截断率。

**SF7 [共识] CWM 退化可能是 capacity-contingent**

R1-W5 提出，R2 AGREE。Conclusion "generation-based verification suffers format collapse" 过于绝对。14B 时 gap 缩窄至 ~1pp。GenRM 在数学领域证明 generative > discriminative。**建议**：改为 "under ≤8B LoRA fine-tuning, generation-based verification suffers format collapse at repository level"。

### Minor

**M1** [R1-M1, R2 AGREE] Table 1 "†" 标记含义不清——CLS/CWM 同样 fine-tuned，应改为 "different training configuration"
**M2** [R2-M2, R1 AGREE] Limitations 未明确提及仅限 Python
**M3** [R1-M4] Appendix J TOST sensitivity 仅覆盖 5-seed variant-level，缺 per-test/repo-level sensitivity
**M4** [R2-M5] §2 PRM 在代码领域的应用讨论不够深入
**M5** [R2-Q5, R1 AGREE] Mixed-effects LPM 应报告 standardized effect size，n=66K 下几乎任何效应都显著
**M6** [R2-M1] Figure 1 "Expected 6" 含义不清楚
**M7** [R1-M5] §4.6(d) CWM SD 0.37pp vs CLS 0.78pp——可能是 floor effect 而非 CWM 更稳定（R2 反驳 CWM 87.97% 不在 floor，Director：替代解释不可排除但非主要关切）

---

## Reviewer Consensus

1. **TRAJ 等价 claim 需限缩** — CLS-TRAJ 在 Holm 校正后 inconclusive，三重训练配置混淆不可忽略 [MF1]
2. **因果语言需降级** — "complexity moderates" → 描述性/关联性语言 [MF2]
3. **Error complementarity 降级** — oracle gap 仅 2.2pp，无实际利用路径，不应作为 key contribution [MF3]
4. **Scope qualifier 必要** — Abstract/Conclusion 需 "≤8B LoRA" 限定 [MF4]
5. **LPM vs GEE 矛盾提升到正文** — 两种统计模型对核心交互项结论相反，是统计可信度核心问题 [SF1]
6. **GenRM domain contrast 提升到主文** — 最有 novelty 潜力的角度，不应仅在 Appendix 一段话 [SF3]
7. **统计框架严谨** — TOST + Holm + clustered bootstrap + Bayesian ROPE + LPM 远超同类论文 [S1]
8. **Failure mode taxonomy 有实用价值** — format/decision/aggregation 分类可操作 [S3]

## Reviewer Divergence

1. **N2 严重性** — R1 标 Critical（2-3 seeds 不支撑因果），R2 降为 Should-Fix（效应量 + 跨模型 + 机制足够描述性结论）。**Director 采纳 Should-Fix**——效应量极大且跨模型一致，但因果语言确需降级。
2. **W1 核心发现可预测性** — R2 标 Must-Fix（方向可预期），R1 反驳（GenRM 先验、function-level 等价 counter-intuitive、failure mode 分布不可先验推导）。**Director 采纳 Should-Fix**——R1 反驳有道理但论文 framing 需改进。
3. **W7 Execution-based upper bound** — R2 要求 Should-Fix，R1 反驳 trivially 100%（ground truth 本身通过执行获得）。**Director 采纳 R1 反驳，降为 informational**。
4. **W5 CWM default assignment** — R2 标 Should-Fix，R1 反驳信息已存在于论文中（§4.5 + Appendix N + Table 4），仅是 presentation 改进。**Director 采纳 R1，降为 minor**。

---

## Questions

**Q1.** [R1] LPM vs GEE 对 formulation×complexity 交互项结论矛盾（p<0.001 vs p=0.449）的根本原因是什么？
**Q2.** [R1] TRAJ 的 variant-level label 是 formulation 固有约束还是实现选择？能否改造为 per-test scoring？
**Q3.** [R1] 是否考虑过更激进的干预（chain-of-thought prompting for CWM、test-case-specific generation）？
**Q4.** [R1] CWM format collapse 与 max_seq_length 截断的关系——给更长生成窗口 format collapse 率是否下降？
**Q5.** [R2] 14B 仅 Qwen3——gap 缩窄是否 Qwen3-specific？是否有 14B DeepSeek 结果？
**Q6.** [R2] Hybrid TRAJ 粗筛 + CLS 细筛方案的可行性？
**Q7.** [R2] Constrained decoding（grammar-guided generation）能否显著缓解 format collapse？
**Q8.** [R2] HumanEval+/MBPP 合成 mutant 分布是否代表真实 bug？
**Q9.** [R2] Mixed-effects LPM 的 formulation×complexity interaction effect size（Cohen's d / marginal effect）？

---

## Missing References

**共识**：
- Constrained decoding 文献（Guidance, Outlines, LMQL）— 直接关联 CWM format collapse mitigation [R2 提出, R1 AGREE]
- Test-time compute scaling（Snell et al., 2024）— 与 formulation efficiency 分析相关 [R2 提出, R1 AGREE]
- Code verification/generation scaling law 文献 [R1 提出]

**分歧**：
- Self-debugging / iterative repair — R1 反驳 scope 不同，§2 已引用。Director：低优先级。

---

## External Review

**状态**：未请求。

---

## Visual Layout Check（非评分项）

**状态**：已完成（0 critical, 1 warning, 14 info）。

- **[Warning]** Page 1-2 连续纯文本（Abstract + Intro + Related Work），第一个 display item 直到 page 3 才出现。建议考虑 page 1 底部或 page 2 加入 teaser figure / 核心结果预览表。
- **[Info]** Figure 3（p.6）legend 字号偏小，打印后可能需凑近查看。
- **[Info]** Table 3（p.6）列数较多，水平间距较紧。
- **[Info]** Abstract ~180-200 words，符合 EMNLP ≤200 words 要求。
- **[Info]** 全文无 LaTeX 渲染错误、margin 溢出。所有表格使用 booktabs 风格。References 格式一致（ACL style）。
- 整体排版质量良好，无阻断性问题。

---

## Overall Assessment

| 维度 | R1 | R2 | 综合 |
|------|----|----|------|
| Soundness | 3/5 | 3/5 | **3/5** |
| Excitement | 3/5 | 3/5 | **3/5** |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5 | 3.0 | **3.0** |
| Confidence | 4/5 | 4/5 | **4/5** |

### Overall: 3.0 = Findings

**理由**：

研究问题实用（execution-free verification formulation 选择是 practitioners 面临的实际问题），统计框架在 NLP 实证研究中属上乘（S1-S2），failure mode taxonomy 有独立实用价值（S3），cross-family 验证增强 robustness（S5）。

但以下问题将评分压在 Findings 区间：
- **TRAJ 等价 claim 在校正后不成立且受三重训练配置混淆**（MF1）——论文核心 narrative 的 1/3 缺乏充分支撑
- **Abstract/Conclusion 的 claim 泛化性超出 ≤8B LoRA 证据范围**（MF4），14B 数据暗示更大规模下结论可能改变
- **LPM vs GEE 对核心交互项结论矛盾**（SF1）未在正文讨论
- **核心发现可预测性**限制 novelty（SF2），GenRM domain contrast 是最有价值但被埋在 Appendix 的角度（SF3）
- **Error complementarity 作为 contribution 过度声称**（MF3），oracle gap 仅 2.2pp 且无落地路径

### 修复后预期评分

如能完成以下修改，预期可达 **3.5 = Borderline Conference**：
1. MF1：限缩 TRAJ claim 为 "CLS-CWM equivalence established; CLS-TRAJ inconclusive"
2. MF2：因果语言降级为描述性/关联性
3. MF3：Error complementarity 从 contribution 降级
4. MF4：Abstract/Conclusion 加 scope qualifier
5. SF1：LPM vs GEE 矛盾提升到正文
6. SF3：GenRM domain contrast 提升到主文，重新 frame novelty narrative

**Excitement 上限受限**：作为 empirical comparison paper，即使所有修改完成，Excitement 预计维持 3/5。Findings 接收是合理定位。

---

## Detailed Comments

### Abstract
- "all formulations achieve comparable accuracy" → 区分 CLS-CWM（confirmed, TOST p=0.007）和 CLS-TRAJ（inconclusive, p=0.128 after Holm）
- 加 "under ≤8B LoRA fine-tuning" scope qualifier
- Error complementarity 降低叙事权重

### §1 Introduction
- 明确 articulate 哪些先验被推翻（GenRM domain divergence, function-level 等价的 counter-intuitive 性）
- Error complementarity 从 key contribution 降级为 analysis finding

### §4.4 Function-Level Results
- CLS-TRAJ 等价的 inconclusive 结论需更显著标注（不仅脚注）
- TOST ±2pp 提供领域论证（或明确 post-hoc 属性和 sensitivity analysis 的限制）

### §4.5-4.6 Repo-Level / Analysis
- "complexity moderates the classification-generation tradeoff" → 描述性语言
- LPM vs GEE 不一致性从 Appendix M 提升到正文讨论，补充 logistic regression 作为 robustness check
- GenRM domain contrast 从 Appendix p.22 提升到此处或独立 subsection
- 报告 mixed-effects interaction 的 standardized effect size

### §5 Conclusion
- "generation-based verification suffers format collapse" → "under ≤8B LoRA fine-tuning, ..."
- 区分 qualitative finding（format collapse 作为 failure mode 可能持续）和 quantitative finding（gap magnitude 随 scale 缩小）

### Tables
- Table 1 "†" 改为 "different training configuration; see §4.5"
- 报告 CWM 平均/P95 生成长度和截断率

### Limitations
- 明确提及仅限 Python