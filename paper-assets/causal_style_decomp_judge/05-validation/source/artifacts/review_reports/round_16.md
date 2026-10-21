---
round: 16
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-23T14:43:49.419635+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告：The Likert Blindspot: Measurement-Mode Divergence in LLM Judge Style Evaluation

**Venue**: EMNLP 2026 via ACL Rolling Review (May 2026 cycle)
**审稿模式**: Fresh（重新审稿）
**Reviewer 编排**: 2 人（R1 方法严谨性 + R2 新颖性/完整性）
**轮次**: 1 轮初审 + 1 轮交叉分享，关键问题达成共识

---

## Summary

本文定义了 "Likert Blindspot"——LLM judge 的 pairwise comparison 能检测到显著风格敏感性而 Likert scoring 检测不到的现象。提出 Controlled Style Decomposition (CSD) 框架，整合 NLI-gated 内容控制、per-axis 风格分解和 position-controlled pairwise comparison。在 5 个 judge（GPT-4o, Qwen3-32B, Llama-3.3-70B, Gemini-2.5-Flash, Claude Sonnet 4）、2 个 primary 风格轴（formality, verbosity）+ 1 个 exploratory（register）、3 个 benchmark（LLMBar, AlpacaEval, MT-Bench）上实验，结果一致显示 pairwise BT 显著（p < 0.001）而 Likert 不显著（p > 0.17），7 种统计方法交叉确认。GEE 条件分解揭示 per-axis confound structure：verbosity 是 style-dominated（Style OR 8–13, Originality OR < 1），formality 是 quality-confounded（两个 predictor 都显著）。论文坦诚提出三种非排他解释（attenuation, amplification, construct divergence）。

---

## Strengths

**S1. 卓越的实验严谨性。** 六层控制设计（NLI gate, position swap, double-rewrite, debiased prompting, cross-rewriter validation, GEE confound decomposition）在 LLM judge bias 文献中属于最严格的方法控制之一。七种统计方法全部一致确认 Blindspot（Table 14, Appendix M），bootstrap CI、TOST、Bayesian equivalence testing 的组合使用展现了统计成熟度。[R1-S3, R1-S5, R2-S1, 双方 AGREE]

**S2. Per-axis confound structure 是 genuinely novel 的发现。** GEE decomposition 揭示 verbosity 是 style-dominated 而 formality 是 quality-confounded，这种 per-axis 差异不是经典心理测量学能预测的，对 LLM judge 审计策略有直接实践意义——不同风格轴需要不同的审计方法。[R2-S2, R1-S2, 双方 AGREE]

**S3. 诚实的 claim hedging。** 论文主动提出三种非排他解释（§5.1），明确承认 residual confounding 未完全消除，用 "complements" 而非 "surpasses" 描述与经典框架的关系。DAG 标注为 "assumed data-generating process, not a claim of perfect identification"。在 LLM 领域论文中属于少见的审慎态度。[R2-S3, R1-S4, 双方 AGREE]

**S4. 方法论体系化与实践相关性。** CSD 将 NLI gating、style-controlled rewriting、GEE decomposition 组合成完整分析框架，各环节有明确方法论依据。结论直接指向 LLM alignment pipeline 的审计盲区——Likert-based reward model 评估可能漏检 pairwise 能发现的风格偏差。[R2-S4, R2-S5, R1-S1, R1-S2]

**S5. Robustness 检查远超平均水准。** 11 个 NLI 阈值、一致性筛选对比、独立 rewriter、人工标注（100 pairs, AC₁=0.96）、6 个 amplification controls、cross-benchmark 复制、n=355 scaled replication——超过同类论文的平均水准。Bootstrap attenuation analysis 比标准 post-hoc power 更合理。[R1-S3, R1-S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] GEE 小样本膨胀严重，仅 1/9 配置有 n=355 复制** [R1-N1, R2-N2, 双方 AGREE]
- Qwen3-32B formality Style OR 从 n=88 的 4.20 降至 n=355 的 2.15，shrinkage 达 49%（Table 2）。但 9 个 judge×axis 配置中仅 1 个做了大样本复制。
- GPT-4o formality Style OR 2.58 [1.41, 4.73] 经 49% shrinkage 后约 1.32，CI 可能跨 1.0（失去显著性）。Gemini formality Style OR 1.64 [0.91, 2.98] 在 n=88 时已不显著，shrinkage 后几乎必然为零。
- Verbosity 的外推（"projected 4–6.5, still ≫ Orig OR < 1"，§5.2）逻辑成立但未经实证验证。
- **R2 重要补充**：此问题主要威胁 GEE per-axis 定量结论，Blindspot 存在性（BT 非参数显著性）不受影响。
- **建议**：至少对一个 verbosity cell 做 n=355 复制验证 shrinkage 预测；正文更突出标注 n=88 OR 为 upper-bound estimates；讨论 GPT-4o formality 的 shrinkage 风险。

**MF2. [critical] 新颖性定位不够精确——核心发现是 Thurstone 1927 的 domain transfer** [R2-N1, R1 AGREE with nuance]
- 核心经验发现（pairwise 比 Likert 更敏感）本质上是 Thurstone (1927) Law of Comparative Judgment 的验证。论文在 §1 引用了 Thurstone 并说 "quantitatively consistent"，但 Title "The Likert Blindspot" 和 Abstract 仍暗示新发现的现象。
- Introduction 的三个 "LLM-specific distinctions" 中，(c) "near-complete binary split" 被论文自己承认与经典理论一致（"consistent with classical predictions when accounting for effect-size-dependent power"），不构成独立贡献。
- **R1 补充**：GEE per-axis decomposition（Table 2 的 style-dominated vs quality-confounded 结构差异）是 genuinely novel 的实证发现，不是 Thurstone 能预测的。CSD pipeline 作为完整诊断工具也有组合创新。
- **共识定位**：contribution 应定位为 "systematic empirical demonstration in LLM judges + per-axis structure discovery + practical diagnostic tool"，而非 "new phenomenon"。删除 (c) binary split 作为独立 distinction 或降级为"与经典理论一致的验证"。

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] Cross-benchmark 复制为选择性报告（6/24 cells）** [R1-N2, R2 AGREE but suggests downgrade]
- 论文在 AlpacaEval 和 MT-Bench 上仅测试 24 个可能 cells 中的 6 个，选择标准为 "targeting the strongest effects"（§5.3）。3 个例外（‡ 行）被 post-hoc 解释为 effect-size dependence，未被前瞻性验证。
- **R2 缓解**：论文将 cross-benchmark 定位为 exploratory（§4.1），主要 claims 建立在 LLMBar 上。但 §1 Contribution 2 的 "the first at this scale" 暗示了更全面的覆盖。
- **建议**：Contribution 2 弱化为 "with selective cross-benchmark evidence"；报告选择标准；考虑补充一个中等效应配置。

**SF2. [warning] Likert Blindspot 缺少正式的 divergence 检验** [R1-W1, R2 AGREE]
- 论文分别展示 "BT 显著" 和 "Likert 不显著"，但从未正式检验二者的 effect size 是否 significantly different。Absence of evidence ≠ evidence of absence。
- n=355 TOST 和 bootstrap attenuation 间接回应，但缺少正式的 measurement-mode interaction test。
- **建议**：Bootstrap the difference in effect sizes between BT and Likert，检验差异是否显著异于零。

**SF3. [warning] Qwen3-32B evaluator-producer overlap（~22% inflation）** [R1-W2, R2-W2, 双方 AGREE]
- Qwen3-32B 同时为 rewriter 和 target judge。独立 GPT-4o rewriter 测试（Appendix E）显示 verbosity Style OR 下降 22%（13.10 → 10.17）。Overlap inflation 是 axis-dependent（verbosity 22% > formality 2.1pp）。
- n=355 唯一复制恰好选用有 overlap 的 Qwen3-32B，不是最 clean 的验证。
- Appendix E 确认 Blindspot 仍然存在（独立 rewriter: Style OR = 10.17, p = 0.001），overlap 影响效应量级而非现象存在性。
- **建议**：Table 1 脚注标注 overlap caveat；至少一个 scaled replication 使用非 overlap 配置。

**SF4. [warning] Claude Sonnet 4 负对照不充分** [R1-W3, R2 AGREE]
- TOST 在 Δ=12pp 时才显著（p=.035），Δ=10pp 不显著（p=.100）。BF₀ < 3（inconclusive）。等价边界 Δ=12pp 的选择是 data-driven 而非 a priori。
- **R2 补充**：Claude 的价值更在于 discriminative validity（LLMBar n.s. vs AEval verbosity OR = 4.76 significant），说明 CSD 不是 universal false positive machine。
- **建议**：将 Claude 定位为 "weak-bias case" 或 "discriminative validity evidence" 而非 "negative control"；提供等价边界的独立理由。

**SF5. [warning] FK grade 的 mediator vs. confounder 辨识不足** [R1-W4, R2 AGREE]
- §5.3 声称 "FK lies on the causal pathway S → FK → Y... making FK a mediator"。但 Sobel 建立的是统计中介而非因果中介。替代因果结构（FK 为 collider 或独立 confounder）在统计上不可区分。
- Mediator 解释下 controlled OR = 2.15，confounder 解释下为无混淆 OR——对应不同政策含义。
- **建议**：呈现两种因果解释并讨论各自含义，而非仅断言 mediator。

**SF6. [warning] Title "Blindspot" 暗示单一因果方向** [R2-W1, R1 AGREE moderate severity]
- "Blindspot" 预设 attenuation 解释（Likert 漏检），与 §5.1 三种非排他解释矛盾。如果 amplification 是主因，应称 "pairwise 放大镜" 而非 "Likert 盲点"。
- **R1 缓解**：实证证据权重（n=355 attenuation d→0, 76.6% concordance, 6 amplification controls）整体更支持 attenuation。Title 方向与证据一致，只是过于确定。
- **建议**：保留 Title，但在 Abstract 更早 qualify——加入 "an operational descriptor without committing to a specific causal mechanism"。

### Minor（不影响接收）

- **M1.** "Consistent pattern" 与 exceptions 的张力——R2 计算 ~30% exception rate，R1 反驳（Claude 是负对照、Gemini 是 spectrum，实际 8/8 bias-positive cells 全部显示 Blindspot）。建议在 Conclusion 量化复制率。[分歧记录]
- **M2.** Register 轴结果弱（BT .553–.635, quality-confounded）——R2 建议移至 Appendix，R1 反驳（需要 per-axis diversity 展示谱系）。[分歧记录]
- **M3.** GEE omitted variable bias——R1 建议报告 E-value，R2 部分反驳（GEE 定位为 descriptive），但同意 E-value 是低成本改进。[轻微分歧]
- **M4.** 论文使用 1-10 整数量表称 "Likert"，严格应为 interval rating scale，缺 Likert (1932) 原始引用。
- **M5.** Table 1 "Cat." 列标注（†, †_e, †_c, ---）难以解析，建议改为文字标签。
- **M6.** Figure 5 y 轴 "Odds Ratio" log scale 应标注，Figure 2 DAG 注释字号偏小。
- **M7.** BT choix regularization α=10⁻⁶ 实质为零正则化，建议报告 α 敏感性。
- **M8.** 100-point continuous Likert（Appendix O）未报告评分分布——是否有 evidence judges 利用了 granularity？

---

## Reviewer Consensus [AGREE]

1. **Scaled replication 覆盖不足**是论文最大弱点——9 个 judge×axis 配置仅 1 个有 n=355 验证，GEE 定量结论的可靠性存疑。[R1-N1 + R2-N2]
2. **核心发现是 Thurstone domain transfer**，novelty 主要来自 GEE per-axis decomposition 和 CSD 诊断工具，需要更精确定位。[R2-N1 + R1 AGREE]
3. **Qwen3-32B evaluator-producer overlap** 影响效应量级（~22%），但不影响现象存在性。[R1-W2 + R2-W2]
4. **缺少正式 divergence 检验**——论文未正式检验 BT 和 Likert 的 effect size 是否 significantly different。[R1-W1 + R2 AGREE]
5. **Claude 负对照的 TOST boundary** 是 data-driven，不够严格。[R1-W3 + R2 AGREE]
6. **FK mediator claim** 需要降级为 "plausible under assumed causal model"。[R1-W4 + R2 AGREE]
7. **实验执行和 robustness 检查**远超同类论文水准。[双方一致]

## Reviewer Divergence [REBUT]

1. **Cross-benchmark 严重性**：R1 列为 Must-Fix（确认偏差），R2 建议降级 Should-Fix（论文标注为 exploratory，主 claims 不依赖）。→ 报告采纳 Should-Fix（SF1）。
2. **Register 轴位置**：R2 建议移至 Appendix（结果弱、quality-confounded），R1 反驳（需要 per-axis diversity 展示 verbosity/formality/register 谱系）。→ 记录分歧，不列为 action item。
3. **"Consistent" 措辞**：R2 认为 ~30% exception rate 下过强，R1 反驳（Claude 是负对照不是例外，实际 8/8 bias-positive cells）。→ 建议量化复制率让读者自行判断。
4. **GEE omitted variables**：R1 要求 E-value（Should-Fix），R2 认为 GEE 是 descriptive 定位（nice-to-have）。→ 建议报告但不列为 Must-Fix。

---

## Questions to Authors

1. n=355 复制是否使用相同 NLI gating threshold (0.90)？pass rate 是否与 n=88 可比？[R1-Q1]
2. 各 judge 的 Likert 评分分布是什么（histogram）？如果 judges 集中在某几个分数点，这直接解释 tie rate 和 Blindspot 机制。[R1-Q2]
3. §1 "76–92% of preferences originate from style cues" 如何计算？引用他人 claim 时其 operationalization 是否与本文一致？[R1-Q3]
4. 为什么 n=355 复制只选了 Qwen3-32B formality——是否有资源约束？[R1-Q4]
5. 76.6% non-tie concordance 中 23.4% discordance——在哪个效应量阈值以下 construct divergence 可能成为主导解释？[R2-Q1]
6. GEE exchangeable correlation α̂ ∈ [−0.25, +0.11]——−0.25 不算"接近零"，论文应改为 "correlation structure choice does not affect estimates due to sandwich robustness" 而非声称接近零。[R2-Q4, R1 交叉确认]

---

## Missing References

1. **Likert (1932)**. A technique for the measurement of attitudes. 论文大量使用 "Likert" 但未引用原始文献。[R1 提出, R2 AGREE]
2. **Polo et al. (2024)**. TinyBenchmarks — IRT 在 NLG evaluation 中的应用，与 measurement-mode 讨论直接相关。[R2 提出, R1 AGREE]
3. **Likert scale anchoring effects** 相关文献——LLM judge 可能以不同方式解释 1-10 scale 锚点。[R2 提出]

---

## External Review

**状态**：未配置。项目未启用外部审稿（paperreview.ai）。

---

## Visual Layout Check（非评分项）

**状态**：已完成（耗时 ~5 分钟）。7 个 info 级建议，无 critical 或 warning。

主要发现：
- 首页无 display item（Figure 1 在 page 2），ACL 双栏常见但可考虑 teaser figure
- Figure 1 caption 较简短，建议补充每阶段核心操作的一句话描述
- Figure 2 DAG 中部分注释文字字号偏小，建议确认打印后可读
- Page 8 左栏 Figure 5 + Figure 6 连续放置，视觉密度较高但内容相关可接受
- Figure 5/6 axis label 和 legend 字号接近正文 70% 下限，建议验证 camera-ready 打印可读性
- 附录末页约 30% 空白，可接受

---

## Overall Assessment

**评分**: 3.5 / 5 — Borderline Conference

| 维度 | R1 | R2 | 共识 |
|------|----|----|------|
| Soundness | 3.5 | 4.0 | 3.75 |
| Excitement | 3.0 | 3.0 | 3.0 |
| Reproducibility | 4.0 | 4.0 | 4.0 |
| Overall | 3.5 | 3.5 | **3.5** |

**接收建议**：Borderline Conference — 修改后可能达到 Conference (4.0) 水平。

**拉向 3.5 而非 3.0 的因素**：
1. 实验规模和控制的 thoroughness 在同类工作中突出（5 judges × 3 benchmarks × 3 axes + n=355 replication）
2. GEE per-axis decomposition 提供了超越 Thurstone 框架的 genuinely new insight
3. 实践相关性强——directly actionable for RLHF/DPO pipeline audits
4. Robustness 检查远超平均（7 种统计方法、11 NLI 阈值、人工标注 AC₁=0.96）

**阻止达到 4.0 的因素**：
1. 核心现象是经典测量理论的 domain transfer，novelty ceiling 有限（Excitement 3.0）
2. GEE 定量结论依赖 n=88 膨胀估计，仅 1/9 配置有大样本验证
3. Cross-benchmark 覆盖为选择性报告（6/24 cells）
4. 缺少正式的 measurement-mode divergence 检验

**修改路径**：补做至少一个 verbosity cell 的 n=355 复制 + 精确定位 novelty（降低 "new phenomenon" 暗示）+ 补充 formal divergence test → 预计可提升至 4.0。

---

## Detailed Comments

### Abstract (~162 词，符合 200 词限制)
- "consistently" 一词在仅 2 primary axes 基础上过强，建议改为 "across two primary style axes, with varying effect sizes across judges"
- 缺少操作性定义的 early qualification——读者从 "Likert Blindspot" 获得单一方向印象

### §1 Introduction
- 三个 LLM-specific distinctions 中 (c) binary split 应删除或降级——论文自己承认 "consistent with classical predictions"
- Contribution 2 "the first at this scale" 暗示全面的 cross-benchmark 覆盖，但实际仅 6/24 cells
- "76–92% of preferences originate from style cues" 引用外部 claim，其 operationalization 与本文是否一致需澄清

### §3 Method
- §3.1 style classifier (Qwen3-32B) 的系统性偏差风险需讨论，虽然 NLI gate 和 direction asymmetry analysis 提供了缓解
- §3.3 "forced choice" 描述准确，但应注明 1-10 量表与 Likert (1932) 原始定义的区别

### §4 Experiments
- §4.1 BT regularization α=10⁻⁶ 的敏感性应报告
- n=355 复制应说明是否使用相同 NLI threshold

### §5 Analysis
- §5.1 需补充正式的 measurement-mode divergence 检验
- §5.2 GEE OR 的 upper-bound nature 应在正文更突出讨论，不仅是 Table 2 caption
- §5.2 verbosity GEE 定量结论应标注为 "projected, pending large-sample validation"
- §5.3 FK mediator claim 需降级为 "plausible under assumed causal model"
- §5.3 cross-benchmark 选择标准应透明化
- §5.4 Claude TOST boundary 需提供独立理由

### §6 Conclusion
- 建议量化复制率："8/11 primary+confirmatory cells, 6/24 cross-benchmark cells"

### Limitations
- 3 个点覆盖适当（residual confounding, detection vs. amplification, scope），符合 EMNLP 要求
- evaluator-producer overlap 的 22% inflation 应作为第 4 个 limitation 点提及

### 格式合规
- ✅ 正文 8 页（Section 1-6 至 page 8）
- ✅ Limitations 在 page 9，不计入页数
- ✅ Abstract ~162 词 ≤ 200
- ✅ 匿名性："Anonymous ACL submission"，无泄露
- ✅ ACL template with [review] option
- ⚠️ 缺 Likert (1932) 原始引用
- ⚠️ 部分引用 arXiv preprint 与正式发表版本混用（camera-ready 前检查）