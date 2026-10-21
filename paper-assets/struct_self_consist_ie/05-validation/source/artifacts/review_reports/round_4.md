---
round: 4
overall_score: borderline (Findings)
timestamp: 2026-05-15T07:08:36.957412+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---

# 审稿报告 — Round 4

**论文**: Strong Predictors, Weak Selectors: A Systematic Comparison of Confidence Signals for Test-Time Scaling in Information Extraction
**Venue**: EMNLP 2026 Findings (ACL ARR May 2026 cycle)
**Reviewer 编排**: 2 人（R1: 方法严谨性+实验设计; R2: 新颖性+完整性+写作质量+Round 3 修复验证）
**流程**: Round 1 独立审稿 → 交叉分享（逐条 AGREE/REBUT）→ 收敛汇总
**Round 3 修复评估**: R2 系统审查了 13 个 Round 3 遗留问题——8 个 RESOLVED，4 个 PARTIALLY RESOLVED，0 个 UNRESOLVED

---

## Summary

本文系统比较了三族（structural / surface / model-internal）五种 confidence signal 在生成式信息抽取（NER + RE）中的 quality estimation 和 sample selection 性能。核心发现 "correlation-selection gap"：instance-level consistency signal 在质量估计上有效（ρ 最高 0.38, AUROC 最高 0.75），但在 best-of-N selection 中无信号显著超越 greedy decoding（p>0.39）。经四轮迭代，论文统计方法论已达到高水平（TOST, bootstrap CI, 3-seed, Bonferroni），但核心贡献的 framing 和可复现性仍需改进。

---

## Strengths

**S1. 统计方法论显著改善。** Bootstrap CI (B=10,000)、TOST 等价检验（区分"无显著差异"与"确认等价"）、3-seed 稳定性验证、Bonferroni 校正声明——四轮迭代后统计分析在 NLP 实证论文中属上乘。TOST 揭示 EM/Voting 在 RE 上即使 ±5pp 也不等价于 greedy（系统性劣化）。[R1-S2, R2-S1 一致]

**S2. 质量估计 vs. 样本选择的解耦是清晰的方法论贡献。** Per-sample vs. instance-level 信号的形式化区分（Eq. 1-7）和 ρ-AUROC dissociation 分析为后续工作提供了好的评估框架。[R1-S1, R2-S2 一致]

**S3. 任务难度梯度分析有实际指导意义。** CoNLL（easy）→ SciERC（medium）→ WNUT-17（capability boundary）三级设计精良。WNUT-17 conditional ρ=0.038 (n.s.) 揭示高 failure rate 下信号表现为 artifactual。EM 在简单任务领先、结构化信号在复杂任务领先的 crossover 有实用价值。[R1-S3, R2-S3 一致]

**S4. MBR decoding 连接概念优雅。** §5 将 selection strategies 形式化为 MBR 框架下不同 utility function 的实例化，有理论统一价值。[R1-S5, R2-S4 一致]

**S5. Limitations section 诚实且具体。** 覆盖了 RE 单数据集、模型规模、constrained decoding、logprob 温度敏感性缺失等。[R1-S4, R2-S5 一致]

**S6. 引用质量高。** 55 条引用经 OpenAlex 验证，0 orphan / 0 missing bib，51 条完全验证通过。Round 3 要求补充的 MBR decoding 等引用已到位。[R1-S6]

---

## Weaknesses

### Must-Fix（影响接收决定）

**[Critical] W-C1: Correlation-selection gap 的 framing 需要区分"定义性 gap"和"经验性 gap"**
- 两位 Reviewer 独立提出（R1-N1, R2-N1），交叉回应后共识
- 4/5 信号是 instance-level，对同一 input 的 N 个候选给出相同分数——其 selection 失败是设计层面的先验预期。论文 §5 承认 "Four of five signals are instance-level by construction and cannot rank N candidates"，但这与 §4.3 和 abstract 中将 gap 作为核心 empirical contribution 的定位存在张力
- 真正的经验贡献是：(1) logprob（唯一 per-sample 信号）也失败（75% comparisons are ties, Cohen's d=0.038）; (2) consensus-proximity/MBR 策略未能弥合 gap
- R1 部分 rebut R2 的严厉程度——认为 MBR 在 MT 中成功但 IE 中失败的对比是非平凡的，但同意论证可加强
- **共识建议**：(a) Introduction 正面论证 "why the gap is not obvious a priori"——MBR 在 MT 中成功为何 IE 中失败？(b) Discussion 明确分离两层论证：定义性局限 (instance-level by construction) vs. 经验性失败 (logprob + consensus-proximity)；(c) 聚焦 logprob ties 的 75% 统计数据做深入分析

**[Critical] W-C2: 训练配置和 prompt template 缺失，影响独立复现**
- 两位 Reviewer 独立提出（R1-N3, R2-N2），无分歧
- §4.1 仅报告 LoRA rank=32, α=64, 5 epochs, LLaMA Factory，缺少：learning rate、batch size、warmup、weight decay、optimizer、early stopping 策略、train/dev split、prompt template（NER/RE 各用什么格式？）、LoRA target modules、max sequence length、schema constraint 定义
- LoRA 微调对 lr 和 target modules 敏感，不同配置可能影响 output diversity 和信号表现
- **共识建议**：附录补充完整训练配置表 + prompt template 示例

### Should-Fix（影响评分）

**[Warning] W-S1: Constrained decoding 对 logprob 信号语义的影响需进一步量化**
- R1 列 critical (N2), R2 列 should-fix (W1)——存在严重性分歧，取交集为 elevated should-fix
- 论文自承 "75% of comparisons are effectively ties"、"logprob primarily reflects grammar compliance under constrained decoding"——但未实验验证此归因
- R1 建议分析 non-tie 的 25% 上 logprob 是否能成功 select；R2 建议讨论 constrained decoding 如何压缩 logprob 判别力
- R1 rebut R2 的 free-form baseline 建议：constrained decoding 对 structured IE 是方法论必要条件，free-form 引入新混淆变量
- **共识建议**：(a) 量化 logprob 分布——tie 的定义（Δlogprob < ε）、non-tie 子集上 logprob 的 selection 能力；(b) 在 Discussion 中讨论 constrained decoding 如何从 grammar compliance 层面压缩 logprob 区分度；(c) 限定 gap 结论的 scope 为 constrained decoding regime

**[Warning] W-S2: RE 证据需进一步加强**
- 两位 Reviewer 一致（R1-W1, R2-N2 initial）
- R0-C3 的 claim 降级已完成（Conclusion 有 hedge），但 Abstract/Introduction 仍将 RE 作为等权证据
- 40% zero-F1 floor effect 严重压缩信号可区分范围，gap 的 RE 证据（-0.9pp, p=0.80）统计说服力弱
- **共识建议**：(a) SciERC RE non-zero F1 子集 selection 分析；(b) Abstract/Introduction 中 RE 标记为 preliminary/exploratory evidence

**[Warning] W-S3: SJ vs EM 优势叙事应改为 difficulty-dependent complementarity**
- 两位 Reviewer 一致（R1 同意 R2-W4）
- SJ vs EM: Δρ=+0.065, CI 下界 +0.003, Bonferroni 下不显著；CoNLL 上 EM 反超
- **共识建议**：弱化 "structural advantage" 叙事，强调在不同难度下 structural 和 surface signal 互补

**[Warning] W-S4: Abstract 过于密集**
- 两位 Reviewer 一致
- 第 4 行含多层嵌套括号的超长句子
- **建议**：核心发现拆分为 2-3 个独立句子

**[Warning] W-S5: "confidence signal" vs "consistency signal" 术语不一致**
- 两位 Reviewer 一致，Round 3 遗留（R3-W7 部分解决）
- logprob 不是 consistency signal 但被 "consistency signals" 统称覆盖
- **建议**：Section 3.2 开头增加明确 taxonomy 定义

**[Warning] W-S6: Introduction novelty claim 缺 hedge**
- R2 提出，Round 3 遗留（R3-W6 部分解决）
- Conclusion 已有 hedge 但 Introduction 仍断言式
- **建议**：Introduction 的 contribution claim 与 Conclusion 的 hedge 对齐

**[Warning] W-S7: 缺少 Xiong et al. (2024) "Can LLMs Express Their Uncertainty?" ICLR 2024**
- 两位 Reviewer 一致
- 系统评估 LLM 置信度获取方法（verbalized, consistency-based, logit-based），与本文多族信号比较直接相关
- **建议**：Related Work "Uncertainty estimation" 段引用并区分

### Minor Issues

**[Info] W-M1**: Table 1 N=16 block 大面积空白，建议补脚注或合并呈现 [R1, R2 一致]
**[Info] W-M2**: Ethics Statement 位于 Limitations 内——建议改为独立 section [R2]
**[Info] W-M3**: Figure 1 caption 未解释 consensus-proximity 转换策略 [R2]
**[Info] W-M4**: Semantic entropy footnote 引用不可比数字——建议强化 caveat [R1]
**[Info] W-M5**: Entity Voting 公式 (5) 分母为 0 的边界条件未注明 [R1]
**[Info] W-M6**: Appendix reliability diagram ECE 的 bin 数量未报告 [R1]
**[Info] W-M7**: TOST δ 选择（±2, ±3, ±5 pp）缺乏实践意义论证 [R1]
**[Info] W-M8**: FK excess agreement negative 值含义可进一步解释 [R1]
**[Info] W-M9**: SJ normalizer max(|g_i|,|g_j|) vs |g_i∪g_j| 未对比 [R1]

---

## Round 3 Issue Resolution Status

| ID | 问题 | Round 4 状态 | 说明 |
|----|------|-------------|------|
| R3-C1 | Constrained decoding confound | PARTIALLY RESOLVED | 承认但未量化 → 降为 W-S1 |
| R3-C2 | Failure-to-reject 措辞 | RESOLVED | TOST 已补充 |
| R3-C3 | N=8 single seed | RESOLVED | 3-seed 验证已补充 |
| R3-W1 | 多重比较校正 | RESOLVED | Bonferroni 声明已加 |
| R3-W2 | Gap tautological | PARTIALLY RESOLVED | 改善但核心张力仍在 → 升级为 W-C1 |
| R3-W3 | MBR 连接缺失 | RESOLVED | §5 MBR 段已写入 |
| R3-W4 | FK 独立性 | RESOLVED | Excess agreement 数据已补 |
| R3-W5 | Cross-model → cross-architecture | RESOLVED | 措辞已统一 |
| R3-W6 | First multi-family claim scope | PARTIALLY RESOLVED | Conclusion 有 hedge 但 Introduction 无 → W-S6 |
| R3-W7 | 术语不一致 | PARTIALLY RESOLVED | 表格缩写仍不统一 → W-S5 |
| R3-W8 | 遗漏引用 | RESOLVED | 已补全 |
| R0-C3 | RE 单数据集 | RESOLVED (claim降级) | 但 RE 证据仍薄弱 → W-S2 |
| R1-W1 | SJ 形式化歧义 | RESOLVED | 补全 |

**总结**: Round 3 的 13 个 in_progress 问题中，8 个已完全解决，4 个部分解决（回归为本轮 issue），0 个完全未解决。论文在统计方法论上的改进（TOST、3-seed、Bonferroni、MBR 连接）是实质性的。

---

## Reviewer Consensus [AGREE]

1. **Gap framing 需分层论证**：定义性局限 (instance-level) 和经验性失败 (logprob + consensus-proximity) 应明确分离 [R1-N1 ≈ R2-N1, 共识]
2. **训练细节/prompt template 必须补充**：独立复现的基本要求 [R1-N3 = R2-N2, 完全共识]
3. **RE 证据仍然薄弱**：claim 降级已做但可进一步加强 [R1-W1, R2 确认]
4. **SJ 优势叙事应改为互补性**：Bonferroni 下不显著，CoNLL 上 EM 反超 [R1 agree R2-W4]
5. **术语需统一 + Abstract 需简化**：[双方一致]
6. **Xiong et al. (2024) 应引用**：高度相关的 LLM 置信度评估工作 [双方一致]
7. **统计方法论已达高水准**：四轮迭代的改进得到两位 Reviewer 一致认可 [双方一致]

## Reviewer Divergence [REBUT]

1. **Constrained decoding 严重性**：R1 列 critical（需实验量化）→ R2 列 should-fix（需更多讨论）→ **共识为 elevated should-fix**，量化 logprob 分布而非增加 free-form 实验
2. **Gap 非平凡性的严厉程度**：R2 认为 excitement 仅 2.5（gap 可预测）→ R1 rebut（MBR 类比非平凡，logprob ties 是经验发现）→ **共识评分 3.0/5**
3. **Free-form generation baseline**：R2 建议增加 → R1 rebut（constrained decoding 是方法论必要条件）→ **共识为不需要 free-form 实验，但需量化 diversity 压缩效应**
4. **BibTeX 键名 nedellec2026consistency**：R2 建议修改 → R1 rebut（内部细节，\citet 输出正确）→ **共识降至 minor**

---

## Questions to Authors

1. Logprob ties（75%）的具体定义是什么？Δlogprob < ε 的 ε 取值？在 non-tie 子集上，logprob 作为 selector 的表现如何？
2. SciERC RE non-zero F1 子集上的 selection gap 分析结果是否与主文结论一致？
3. 是否考虑过在 Introduction 中正面论证 "why the gap is not obvious"——例如引用 MBR 在 MT 中的成功作为对比？
4. LoRA target modules 具体是 all linear 还是 q_proj/v_proj only？这对 output diversity 的影响有多大？
5. Prompt template 中 schema constraint 如何定义？是否有 few-shot examples？

---

## Missing References

1. **Xiong et al. (2024)** "Can LLMs Express Their Uncertainty? An Empirical Evaluation of Confidence Elicitation in LLMs" ICLR 2024 — 高度相关 [两位 Reviewer 一致]
2. **Ye et al. (2025)** "Do LLMs Estimate Uncertainty Well in Instruction Following?" ICLR 2025 — 中等相关 [R2]
3. **Bertsch et al. (2024)** "In-Context Learning with Long-Context Models" — 与 test-time scaling 相关 [R1]
4. **Wiher et al. (2022)** "On Decoding Strategies for Neural Text Generators" — 与 constrained decoding diversity 相关 [R1]
5. **Müller & Sennrich (2021)** "Understanding the Properties of MBR Decoding in NMT" — 与 §5 MBR 连接直接相关 [R1]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未启用

---

## Overall Assessment

**Overall Score: 3.0 / 5 (Findings: borderline)**
**Confidence: 4/5**

**判断依据**：

两位 Reviewer 交叉回应后评分收敛至 3.0/5（R1: 3.0 维持不变, R2: 3.5→3.0 下调）。

**支持接收的因素**：
- 统计方法论经四轮迭代达到高水准（TOST, bootstrap CI, 3-seed, Bonferroni）
- QE vs. selection 的解耦框架有方法论贡献价值
- 任务难度梯度分析和 WNUT-17 capability boundary 发现有实用指导意义
- MBR decoding 连接提供理论统一
- Round 3 的 13 个 issue 中 8 个完全解决，改进幅度显著

**制约接收的因素**：
- 核心贡献 "correlation-selection gap" 的 framing 仍未清晰区分定义性局限和经验性发现（W-C1），削弱 novelty
- 训练细节/prompt template 缺失影响独立复现（W-C2）
- Constrained decoding 对 logprob 信号语义的影响仍为 unquantified confound（W-S1）
- RE 证据薄弱（W-S2），SJ 优势 marginal（W-S3）

**修订优先级**（按影响排序）：
1. **[Must]** Gap framing 分层（定义性 vs 经验性）——决定核心贡献的 novelty 定位
2. **[Must]** 训练配置 + prompt template 补充——复现基本要求
3. **[Should]** Constrained decoding 下 logprob 分布量化——加强 gap 解释力
4. **[Should]** RE conditional analysis + 进一步降级——减少过度泛化
5. **[Should]** SJ narrative 调整 + Abstract 简化 + 术语统一——写作质量
6. **[Minor]** Table 格式、Ethics 位置、引用补充