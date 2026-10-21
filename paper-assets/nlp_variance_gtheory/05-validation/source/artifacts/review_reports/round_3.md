---
round: 3
review_mode: fresh
overall_score: 3.5 (Borderline Conference)
timestamp: 2026-05-22T10:08:59.536802+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 4 (Fresh Review)

**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis
**Venue**: EMNLP 2026 via ACL Rolling Review (ARR)
**截止日期**: 2026-05-25
**审稿模式**: Fresh（重新审稿，无历史记忆）
**Reviewers**: R1（方法严谨性 + 实验设计）、R2（新颖性 + 完整性 + 格式合规）。本轮为 EMNLP 一般会议编排（2 Reviewers），R3 未在本轮分配任务。
**轮次**: 1 轮独立审稿 + 1 轮交叉分享，关键问题达成共识

---

## Summary

本文将 Generalizability theory (G-theory) 应用于 LLM 评测的方差分解，在 8 个开源 7-9B 参数模型和 5 个 benchmark（3 MC + 2 FF）上设计了最多 7 个 facet 的完全交叉实验，共约 2.3M 条评测记录。主要发现：(1) item-related variance（item + model×item DIF）在 MC benchmark 上集中于 68-72%，在 FF benchmark 上分散至 31-41%，五个 benchmark 无重叠；(2) 多 facet 设计达到 G≥0.80 所需 item 数是单条件设计的 1/10（55 vs 552）；(3) BF16/FP16 在 binary scoring 下功能等价；(4) 发布 D-study 预算计算器。

---

## Strengths

**S1. 规模和系统性无出其右** [R1, R2 共识]
7 facets × 8 models × 5 benchmarks 的完全交叉设计在 LLM evaluation 文献中首屈一指。最接近的 Messing (2026) 仅覆盖 1 个 benchmark + 5 个 methodology facets。2.3M 记录提供了充分的 item-level 统计功效。Table 1 的设计矩阵清晰完整。

**S2. Robustness 验证堪称典范** [R1, R2 共识]
8 项独立稳健性分析（GLMM complement、accuracy-range stability、REML comparison、CI method、facet specification、LOMO、null calibration、reduced crossing validation）+ 3 个独立采样验证（CV=3.1%），远超同类 empirical study 标准。null calibration（100 次 Bernoulli 模拟）和 LOMO 设计精巧。

**S3. D-study budgets 的即时实用价值** [R1, R2 共识]
"Multi-facet 55 items vs single-condition 552 items" 和 cross-model per-benchmark projections（Table 5, bootstrap CIs 确认所有 ratios >10×）对 benchmark 设计者可直接操作。与 IRT 的正交互补定位（Table 4, IRT 116 items: G=0.457 → 0.895 under multi-facet）清晰有力，避免了与 tinyBenchmarks/PSN-IRT 的虚假竞争。

**S4. 写作透明诚实** [R1, R2 共识]
通篇使用 "suggest"/"format-associated" 而非因果性语言；主动报告 p=0.10、benchmark-level CI 跨零；Limitations 诚实承认三项 scope constraints。这种透明度在 submitted papers 中少见。

**S5. Reproducibility 达标** [R1, R2 共识]
实验设计详尽（8 模型 HuggingFace ID、6 prompt 模板全文、seed 值、vLLM 版本、GPU 型号均列出）。承诺 publication 后发布代码/数据/calculator。

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF1. [critical] Format-associated claim 的 benchmark-level 统计功效严重不足** [R1-N2, R2-N1 共识]
- 位置：Section 4.3, Abstract, Contribution 1, Conclusion
- n=5 benchmarks（3 MC vs 2 FF），permutation test p=0.10（C(5,3)=10 exhaustive permutations，分辨率上限 = 1/10），benchmark-level CI 跨零 [-1.7, 5.1]（noncentral t, df=3）。即使真实效应无穷大，p 最小只能到 0.10——这是设计层面限制，非分析可修复。
- Abstract "with no overlap across all five benchmarks" 字面准确但语用上暗示远强于 p=0.10 的结论。这是论文排名第一的贡献和标题的核心叙事。
- **建议**：(a) Abstract 明确标注为 n=5 的观察性 pattern（如 "across the five benchmarks studied"）；(b) 讨论 permutation test 的 power ceiling；(c) 考虑 Bayesian 补充分析；(d) 将 D-study budgets 提升为 primary contribution，format-associated pattern 降为 secondary observation。增加 benchmarks 可彻底解决但可能超出 revision 周期。

**MF2. [critical] Item-related variance bundling（σ²_p + σ²_pM）放大 item 主导叙事** [R1-N1 must-fix, R2-W1 should-fix; 交叉后实质共识]
- 位置：Section 3.1 定义, Abstract, Contribution 1, Section 4.3, Conclusion
- 将 model×item DIF 全部归入 "item-related" 使 item 表观贡献翻倍（MMLU: 37.9% → 68.1%）。model×item 在 LLM 场景中同时是 model property（architecture-specific capability profiles），不同于教育测量中 person×item 的单向 interpretation。
- R2 指出：unbundled 差距 ~15pp（MC 34-38% vs FF 17-24%），bundled 放大至 ~30pp。但 unbundled 下 MC/FF 仍无重叠。
- **建议**：(a) Abstract/Contribution 并列报告 bundled 和 unbundled 数字；(b) Section 3.1 讨论 bundling 在 LLM vs 教育测量场景中的语义差异；(c) Section 4.3 增加 unbundled 对比表。
- **严重性分歧**：R1 判定 must-fix，R2 判定 should-fix（因 Section 3.1 已有方法论论证且 unbundled 仍无重叠）。报告将其列为 must-fix，因 Abstract 的信息对称性不足。

**MF3. [critical] Binary scoring 作为 FF variance structure 的混淆因素** [R2-W3 首次提出, R1 交叉后同意升级]
- 位置：Section 4.1, 4.3, Limitations
- Binary scoring 将 FF 任务的 partial credit 信息（推理路径质量、中间步骤）压缩为 0/1，可能是 FF 高 residual (40-44%) 和低 item-related variance 的主要原因之一。Section 4.1 的 text-exact-match G=0.007（temperature 主导 79.7%）已证明 scoring metric 根本性地改变 variance structure。
- 如果使用 partial credit scoring，FF 的 item-related variance share 可能上升，format-associated gap 可能缩小——意味着当前观察到的 format gap 可能部分是 scoring-metric artifact。
- **建议**：Limitations 明确 "all conclusions conditional on binary scoring; partial credit scoring may alter FF variance structure and reduce format-associated gap"；Section 4.3 讨论 scoring granularity 作为混淆因素。

### Should-Fix（影响评分但不一票否决）

**SF1. [warning] Format-associated pattern 的 trivial explanation 未充分排除** [R2-N2 critical, R1 partial rebut → should-fix]
- MC 天然约束输出到 A/B/C/D，item 主导是 response format 的固有属性。R2 认为这是 tautological consequence；R1 以 within-MMLU ρ=0.806 分析和 HellaSwag 反例（model×item > item）部分反驳，认为不是 tautological 但需更充分的 mechanism discussion。
- **分歧记录**：R2 列为 critical（novelty 受威胁），R1 列为 should-fix（有合理内核但非 tautological）。
- **建议**：Section 4.3 增加 1-2 段 mechanism discussion，区分 "format constrains generation noise"（mechanistic explanation）和 "item difficulty heterogeneity drives variance"（substantive finding）。

**SF2. [warning] Quasi-random model facet 的 target universe 定义模糊** [R1-W1, R2-W2 共识]
- 8 模型均为 open-weight, instruction-tuned, 7-9B。LOMO 和 4-model subset 仅验证 within-sample stability，不能证明对 universe 的代表性。排除 API/base/70B+/domain-adapted。
- **建议**：Section 3.2/3.4 明确界定 target universe；D-study calculator 增加 applicability caveat。

**SF3. [warning] Exp-002 reduced crossing 验证仅基于 MMLU** [R1-W2, R2-W4 共识]
- ΔG=0.0008 仅在 MMLU 上验证，其他 4 个 benchmark（特别是 FF）未经同等验证。FF benchmarks 的 temperature sensitivity 可能更高（chain-of-thought generation）。
- **建议**：补充至少 1 个 FF benchmark 的 sensitivity check，或明确声明 transferability assumption。

**SF4. [warning] MATH 排除 DeepSeek（7/8 models）影响未讨论** [R1-W3, R2 交叉同意]
- DeepSeek 系列在数学推理有特定优化，其排除可能系统性影响 MATH 的 variance structure。MATH residual 高达 43.9%——是否部分因 7-model 设计 underestimates model-related variance？
- **建议**：报告 DeepSeek 在其他 4 个 benchmark 上的 LOMO 分析；讨论排除对 MATH 结论的影响方向。

**SF5. [warning] Bootstrap resampling 未 respect stratified design** [R1-W4, R2 交叉同意]
- 200 items 来自 10 subjects × 20 items，item-level bootstrap 未做 stratified resampling。每次 resample ~127 unique items，某些 subjects 可能被完全遗漏。
- **建议**：说明是否为 stratified bootstrap；若否，对比 stratified bootstrap 的 CI 宽度。

**SF6. [warning] References 格式不完整 + double-blind 合规疑虑** [R2-W5, R1 验证同意]
- `varannot2025gtheory` author 为 `{Anonymous}`——需确认非 self-citation 泄露（ARR double-blind policy）
- 多个条目使用 "and others" 代替完整 author list
- `kipnis2025metabench`, `li2025atlas` 缺 URL
- **建议**：补全所有 bib 条目；确认 varannot2025gtheory 合规性。

**SF7. [warning] 遗漏 4 篇相关工作** [R1, R2 各提 2 篇]
- Gruber et al. (2024) "Towards Reproducible LLM Evaluation" — benchmark uncertainty quantification
- Wang et al. (2025) "Benchmark2" — benchmark meta-evaluation
- Yin et al. (2025) "From Crowdsourcing to Benchmarking" — evaluation reliability
- Burnell et al. (2023) "Rethink reporting of evaluation results in AI" — evaluation reporting standards

---

## Reviewer Consensus

以下关键问题 R1 和 R2 达成完全共识 [AGREE]：
1. Format-associated claim 在 benchmark-level 统计功效不足（p=0.10, n=5, CI 跨零）→ **must-fix**
2. Item-related variance bundling 的实质性问题（Abstract 信息不对称）→ **must-fix**（R1）/ **should-fix**（R2）
3. Binary scoring 作为 FF variance 混淆因素 → **must-fix level discussion needed**
4. D-study budgets 是最强且最不受争议的贡献
5. Robustness 验证全面性远超同类研究
6. 写作透明度高（主动报告限制）
7. Model scope、reduced crossing 验证、DeepSeek exclusion、bootstrap 策略 → **should-fix**

## Reviewer Divergence

| 议题 | R1 | R2 | 分歧性质 |
|------|-----|-----|----------|
| Trivial explanation (MC response space) | Should-fix: within-MMLU ρ=0.806 + HellaSwag 反例削弱 tautological 论点 | Critical/must-fix: novelty 受威胁，20 items anecdotal | R1 认为有反例证据反驳纯 tautological 解释；R2 认为反例不够系统性 |
| Excitement | 3.5/5 | 2.5/5 | R1 认为 D-study/toolkit novelty 独立于 format claim；R2 认为 format claim trivial 拉低整体 excitement |
| Bundling 严重性 | Must-fix（信息不对称） | Should-fix（有方法论论证 + unbundled 仍无重叠） | 对同一问题的严重性判断不同，实质同意 |

---

## Questions（需作者澄清）

**Q1.** [R1, R2] unbundled item_id 单独指标下的 MC/FF separation 是否也做了 formal permutation test？
**Q2.** [R1] Probit simulation ρ=0.732——具体哪些 components 的 rank 在 dichotomization 后变化？主要影响小 components 还是也影响主要 components？
**Q3.** [R1, R2] Text-exact-match 下 G=0.007 的 implication 和对非 binary scoring 实践者的指导意义？
**Q4.** [R2] 使用 partial/rubric-based scoring 替代 binary scoring，FF variance structure 是否实质变化？（排除 binary scoring 作为混淆因素的关键实验）
**Q5.** [R2] D-study budgets 是否有 out-of-sample validation（第 9 个模型或新 benchmark）？
**Q6.** [R1] 能否在控制 difficulty dispersion 后看 format 是否仍有独立效应？（ρ=0.806 分析仅在 MMLU 10 subjects 内进行）
**Q7.** [R1, R2] `varannot2025gtheory` 在 bib 中 author 为 "Anonymous"——是否为作者自己的工作？ARR double-blind 合规？

---

## Missing References

1. Gruber et al. (2024) "Towards Reproducible LLM Evaluation: Quantifying Uncertainty in LLM Benchmark Scores" (arXiv:2410.03492) [R2]
2. Wang et al. (2025) "Benchmark2: Systematic Evaluation of LLM Benchmarks" (arXiv:2601.03986) [R2]
3. Yin et al. (2025) "From Crowdsourcing to Benchmarking: A Framework for Evaluating LLMs with Human Preferences" [R1]
4. Burnell et al. (2023) "Rethink reporting of evaluation results in AI" [R1]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：**未请求**（项目未启用 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 2 warnings, 3 info）：

- **[warning]** 前 4 页连续纯文本无任何 display item，第一个视觉锚点（Table 1 + Figure 1）延迟到第 5 页。建议将 Figure 1（G-theory 设计概念图）前移至 Introduction 末尾或 Method 开头（P2-P3）。
- **[warning]** Display items 分布严重不均：前 4 页 0 个，后 4 页 7 个。建议前移至少 1 个 display item 平衡视觉节奏。
- **[info]** Figure 1 尺寸偏小（单栏底部），建议放大或改为 figure* 全宽展示。
- **[info]** Figure 2 堆叠柱状图 6-7 种颜色，灰度打印时部分浅色段难以辨别。建议增加 hatching pattern 或 Okabe-Ito 色板。
- **[info]** 末页（附录 C）填充约 60%，内容为 prompt 模板展示，不影响审稿体验。

---

## Overall Assessment

**Overall Score: 3.5 (Borderline Conference)**

| 维度 | R1 | R2 | 共识 |
|------|-----|-----|------|
| Soundness | 4/5 | 4/5 | **4/5** |
| Excitement | 3.5/5 | 2.5/5 | **3.0/5**（折中） |
| Reproducibility | 4/5 | 4/5 | **4/5** |
| Overall | 3.5 | 3.5 | **3.5** |
| Confidence | 4/5 | 4/5 | **4/5** |

**判断依据**：

方法论贡献扎实（首个大规模多 facet G-theory 分析 + D-study calculator），robustness 验证达到该子领域新标准，写作严谨透明。D-study reproducibility budgets 是最强且最不受争议的贡献，具有直接实用价值。

主要顾虑集中在三点：(1) 核心 format-associated claim 的 benchmark-level 统计功效不足（n=5, p=0.10, CI 跨零），使得论文最突出的 finding 停留在 "observed pattern" 而非 "established result"；(2) item-related variance bundling 的 Abstract 呈现不够透明；(3) binary scoring 作为 FF variance structure 的潜在混淆因素未充分讨论。

**接收建议**：当前版本适合 Findings 接收（Soundness 和 Reproducibility 达标）。若目标是 main conference，需要：(a) 重构 contribution 排序（D-study budgets 升为 primary），(b) 增加 benchmarks 或提供 Bayesian 补充分析以增强 format claim，(c) 在 Abstract 并列报告 bundled/unbundled 数字，(d) 讨论 binary scoring 混淆。在 revision 周期内可完成 (a)(c)(d)，(b) 中增加 benchmarks 可能超出时间预算。

---

## Detailed Comments（按章节）

### Abstract
- "with no overlap across all five benchmarks"：需加 "studied" 或其他 scope qualifier
- 应并列报告 unbundled item_id（34-38% vs 17-24%）和 bundled item-related（68-72% vs 31-41%）
- "2.3 million evaluation records"：MATH 仅 7 模型，实际约 2,246,400，建议 "approximately 2.3 million"

### Introduction
- 开头引用的 "34-38%" 和 "&lt;3%" 来自不同实验条件（cross-model 和 single-model），需更清楚标注来源
- Contribution 排序建议调整：D-study budgets 升为 #1，format-associated pattern 降为 #2

### Method (Section 3)
- Section 3.1: bundling 定义处增加 LLM vs 教育测量场景的语义差异讨论
- Section 3.2: 明确界定 quasi-random model facet 的 target universe 边界
- Section 3.3: 声明 reduced crossing 的 cross-benchmark transferability assumption
- Section 3.4: probit ρ=0.732 应补充 top-3 component rank preservation 数据

### Experiments (Section 4)
- Section 4.1: text-exact-match G=0.007 的 implication 需 1-2 段讨论（对 non-binary metrics 实践者的意义）
- Section 4.3: 增加 mechanism discussion（response space constraint vs item heterogeneity）；增加 unbundled 对比表；讨论 scoring granularity 混淆
- Section 4.3 Table 3: "prompt" 列在 MC/FF 含义不同——caption 有解释但表内应加标注
- Section 4.3 label `format_conditional` vs 标题 "Format-Associated"——内部命名不一致
- Section 4.5: D-study 增加 out-of-sample validation 讨论
- Section 4.6: Qwen 3B vs 7B 的 prompt×item 差异（12.2% vs 8.8%）需报告 CI

### Conclusion
- "will be released upon publication"：如能 camera-ready 附 anonymous repo link 更佳

### Limitations
- 增加第四个 scope constraint：所有结论 conditional on binary scoring
- 明确 partial credit scoring 可能改变 FF variance structure

### References
- 补全 author lists（"and others" → 完整）
- 补全缺失 URL
- 确认 varannot2025gtheory 的 double-blind 合规性
- 补充 4 篇遗漏相关工作

### Appendix
- 混用 $\sigma^2_p$ 和 `\texttt{item_id}` 指代同一概念，建议统一术语