---
round: 5
review_mode: fresh
overall_score: 3.0
timestamp: 2026-05-22T13:20:05.778708+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# 审稿报告 — Round 6 (Fresh Review)

**论文**: Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis
**Venue**: EMNLP 2026 (ARR May cycle)
**Reviewer 编排**: 2 名 Reviewer（R1: 方法严谨性+实验有效性; R2: 新颖性+完整性+写作质量）+ 独立视觉审查 Agent
**流程**: Round 1 独立审稿 → 交叉分享（[AGREE]/[REBUT]） → 收敛（1 轮达成）
**注**: Reviewer 3 为独立视觉审查 Agent，不参与评分和交叉讨论，其 findings 列在 Visual Layout Check 章节。

---

## Summary

本文将 Generalizability Theory (G-theory) 应用于 LLM 评测的方差分解，在 8 个开源 7-9B 模型和 5 个 benchmark 上交叉最多 7 个 facet（约 230 万条记录）。三个核心发现：(1) multi-facet 设计比 single-condition 设计需要 10× 更少的 items 达到 G≥0.80（55 vs 552 items）；(2) MC benchmark 的 item-related variance 集中在 68-72%，FF benchmark 分散至 31-41%（format-associated pattern）；(3) BF16/FP16 在 binary scoring 下可互换（<0.1% interaction）。论文提供了 D-study budget calculator 和开源工具包。

---

## Strengths

- **S1 [共识]** 230 万条记录的全交叉析因设计（7 facets × 8 models × 5 benchmarks），是该领域首次同时交叉如此多 facets 的工作，规模可观，Henderson Method I + bootstrap CI 执行无误。
- **S2 [共识]** 9 项 robustness checks（GLMM, probit simulation, null calibration, LOMO, accuracy-range stability, estimator comparison, CI method, facet specification, reduced crossing validation）系统且诚实，方差分解可信度高。null calibration（item variance 0.08% vs 观测 58.4%）特别有说服力。
- **S3 [共识]** Claims hedging 总体恰当——论文在 §4.3 正确使用 "descriptive observation" 措辞，承认 p=0.10 和 benchmark-level CI spanning zero。
- **S4 [R1]** D-study budget calculator + intermediate design gradient（Appendix B: 从 single-condition 到 full multi-facet 的渐进路径, "minimal upgrade" 3p×3s → G=0.818）对实践者直接有用。
- **S5 [R1]** IRT 互补性展示（Table 4: IRT-selected 116 items, single-condition G=0.457 vs multi-facet G=0.895）清晰论证了 item selection 和 protocol optimization 的正交关系。
- **S6 [R1]** Text-exact-match 对照实验（G=0.007 vs binary G=0.936）有力展示了 scoring metric 对 variance structure 的根本影响。
- **S7 [R2]** 写作结构清晰，single-model → cross-model → cross-benchmark 的递进叙事逻辑好。

---

## Weaknesses

### Must-Fix（影响接收决定）

**N1 [critical, 共识] Quasi-random model facet: 8 purposively selected models 作为 random facet 的理论辩护不充分**
- 位置: §3.6, Appendix A (LOMO)
- G-theory 要求 facets 从 admissible universe 中随机抽样（Brennan 2001, Ch. 2）。8 个模型每 architecture family 仅 1 个（purposive stratified sampling），声称 "quasi-random facet" 但：(a) 零 within-family replication；(b) LOMO 功效极低（n=8, G_item span=0.012）；(c) 四模型子集验证在同一 universe 内，不证明对不同模型集成立；(d) Cross-benchmark LOMO 仅展示 DeepSeek 一个模型。
- Facet specification sensitivity（fixed vs random ΔG=0.37pp）仅测试了 temperature+ordering，未测试 model facet 本身。
- **影响**: 所有 G coefficients 和 D-study projections 均依赖此假设。若 models 为 fixed facet，G 可能被高估。
- R1 评级 critical; R2 交叉回应 AGREE with nuance（认为问题成立但 R1 略过强）。

**N2 [critical, 强共识] Format-associated pattern 统计功效不足但叙事权重过高**
- 位置: Abstract, §1 Contributions, §4.3, §5
- n=5 benchmarks (3 MC + 2 FF), permutation test p=0.10（分辨率下限），benchmark-level CI [-1.7, 5.1] 跨零。item-level d=1.73 与 benchmark-level claim 存在分析单位不匹配（ecological fallacy risk）。§4.3 内部 hedge 合理，但 Abstract 和 Contributions 措辞仍超出统计支撑。
- **影响**: 论文的第二核心发现在统计上无法与随机分配区分。
- R1-N2 + R2-N2 独立提出，交叉回应互相 AGREE。本问题在 Round 4-5 也被提出（FR4-MF1, FR5-N1），虽已修订但 fresh review 仍认为权重过高。

**N3 [critical, 共识方向一致] D-study projection 外推假设（variance component invariance）未充分讨论**
- 位置: §4.5, Table 4, Appendix B
- D-study 假设 variance components 在改变条件数量时保持不变。single-model budget 55 → cross-model 93（69% 增长）；§4.6 G 从 0.963（单模型）降到 0.71（2 模型）。论文在 §4.5 末段有 caveat（"validated within our model universe"）但不够显眼。
- R2 补充：single→cross-model 变化是 D-study 固有限制（不同 variance decomposition），非方法错误，但仍需明确讨论 projection 边界。
- R1 评级 critical; R2 AGREE with nuance。

**N4 [critical, 分歧] 与 Messing (2026) 的增量贡献界定不充分**
- 位置: §1, §2 Positioning
- Messing (2026) 已将 G-theory 引入 LLM evaluation（TEE 框架, 5 facets, judge identity 43.8%），当前 §2 仅一句话区分。
- **分歧**: R2 认为新颖性界定不充分（critical）；R1 REBUT——认为三个实质性增量（fix judge + 5 benchmarks + infrastructure facets）已在 §2 Positioning 列出，D-study cross-benchmark budgets 和 format-associated pattern 在 Messing 中完全没有。R1 认为是写作问题而非新颖性问题。
- **Director 判断**: 增量贡献在实质上存在，但 §2 的对比确实不够充分。建议用整段详细对比 TEE 框架与本文在方法论层面的异同。

**N5 → 降级为 W8 [should-fix, 分歧]**: "10× fewer items" framing 隐藏 129× 总评估量增长。R2 评为 critical，R1 REBUT（Table 4 已报告总量，Appendix B 有 intermediate designs）。Director 采纳 R1 反驳——信息未被隐藏，但 Abstract 表述可更平衡。降级为 should-fix。

---

### Should-Fix（影响评分但不一票否决）

**W1 [共识] Item-related variance bundling (σ²_p + σ²_pM) 在 LLM context 下的解释性问题**
- σ²_p（item difficulty, 跨模型一致）和 σ²_pM（DIF, 跨模型不一致）概念不同，HellaSwag σ²_pM > σ²_p（36.0% vs 34.3%）说明 bundling 可能掩盖重要结构差异。§3.1 有 psychometric justification 和 dual interpretation discussion，但正文叙事仍以 bundled 指标驱动。
- 建议：在 Table 3 和 §4.3 同时展示 bundled 和 unbundled 的 MC/FF 比较。

**W2 [共识] 模型范围过窄（7-9B instruction-tuned, 2024-2025），Abstract 语气未对齐限定**
- §3.6 和 Limitations 已限定 universe，但 Abstract 未对齐。Scale validation 仅 Qwen2.5 3B/7B（同 family）。

**W3 [共识] Reduced crossing validation 仅 MMLU，FF benchmarks 未验证**
- exp-001→exp-002 的 ΔG=0.0008 仅在 MMLU 上验证。10pp item variance redistribution 在 FF 上可能表现不同。

**W4 [共识] 200-item stratified sample 代表性未充分验证**
- 10/57 subjects (17.5%), 1.4% items。三次 resampling（CV=3.1%）仅 within same 10 subjects，未验证 subject selection robustness。其他 benchmarks 的 200-item 采样策略也未详述。

**W5 [共识] FF benchmarks 高 residual variance (40-44%) 归因推测性**
- GSM8K 39.9%, MATH 43.9% 是各自最大 component，仅一句话解释（"CoT path diversity"）。对 D-study projection 可靠性构成威胁——residual 中可能包含未建模的系统性 variance source。

**W6 [R2, R1同意] 所有发现仅限 binary scoring，未探索 partial credit**
- text-exact-match G=0.007 展示了 scoring metric 的根本影响。实际评测常用 F1/BLEU 等连续指标，但论文未探索中间方案。§3.5 和 Limitations 已承认。

**W7 [R2, R1同意] Abstract 数字过密（>20 个数值），可读性受损**
- 建议保留 3-4 个最关键数字（10×, 55 vs 552, 68-72% vs 31-41%），其余移入正文。

**W8 [从 N5 降级, 分歧] "10× fewer items" 的 cost trade-off 在 Abstract 中未呈现**
- Table 4 已报告总量，Appendix B 有 intermediate designs。但 Abstract 和 Contribution 1 仅突出 "10×"，建议加 cost context 和更显眼地推广 intermediate designs。

---

## Reviewer Consensus

以下问题两位 Reviewer 独立达成一致（交叉回应中互相 [AGREE]）：

1. **Format-associated pattern 统计功效不足 + 叙事权重过高**（R1-N2 ↔ R2-N2）— 最强共识
2. **FF residual variance 未充分解释**（R1-W6 ↔ R2-W2）
3. **模型范围过窄，Abstract 未对齐限定**（R1-W2 ↔ R2-W1）
4. **D-study projection 外推边界需讨论**（R1-N3 ↔ R2 AGREE with nuance）
5. **Quasi-random model facet 假设需更强辩护**（R1-N1 ↔ R2 AGREE with nuance）
6. **Item resampling stability 仅限 MMLU**（R1-W5 ↔ R2-Q4）
7. **Table 3 Prompt 行非对称报告**（R1-Minor ↔ R2-Minor）
8. **Abstract "no unified factorial framework exists" 过于绝对**（R1-Minor ↔ R2-Minor）
9. **遗漏 Mizrahi et al. (2024) TACL 和 HELM (2023)**（R2 → R1 AGREE）
10. **遗漏 measurement invariance 文献**（R1 → R2 AGREE）

---

## Reviewer Divergence

以下问题两位 Reviewer 存在分歧（交叉回应中有 [REBUT]）：

1. **Messing (2026) 增量贡献**：R2 认为新颖性界定不充分（critical）；R1 认为实质性增量存在（fix judge + 5 benchmarks + infrastructure facets），是写作问题非新颖性问题。
2. **"10× fewer items" 严重程度**：R2 认为隐藏 129× 成本是 critical；R1 认为 Table 4 已报告，严重性被高估。Director 采纳 R1 反驳，降级为 should-fix。
3. **IRT 对比公平性（Table 4）**：R2 认为混淆两个维度；R1 反驳认为这正是论文的有意设计（展示正交互补性），Director 采纳 R1。
4. **Precision 未覆盖 4-bit/8-bit quantization**：R1 列为 W3；R2 反驳认为 out of scope，Director 采纳 R2，仅作为 Limitations 补充建议。
5. **Ordering "structurally inert" 是否违反 balanced design**：R1-Q5 提出；R2 反驳认为零方差 facet 不影响 Henderson Method I，Director 采纳 R2。
6. **Title "Reproducibility Budgets" 是否 oversell**：R1 认为可能；R2 反驳认为合理，Director 采纳 R2。

---

## Questions（需要作者澄清）

1. D-study projections 对完全不同的 8 模型（不同 families）是否还能成立？（R1-Q1, R2-Q2）
2. Format-associated pattern 的 benchmark-level power analysis：在 n=5 (3 vs 2) 下，α=0.05 能检测到多大效应？（R1-Q2, R2-N2）
3. FF 40-44% residual 的具体构成？是否可通过增加 generation sampling 或更精细 scoring 来减少？（R1-Q3, R2-W2）
4. 2-model G=0.71 → 8-model G=0.896 的非线性关系——D-study 能否准确预测 G vs n_model 曲线？（R1-Q4）
5. Henderson Method I 在 ordering facet "structurally inert" 的 benchmarks 上是否仍满足 balanced design 假设？（R1-Q5, R2 认为不是问题）
6. 能否用 subject-level accuracy 作为 continuous outcome 进行一次验证性 G-study？（R1-Q6）
7. "10× (55 vs 552)" 来自 single-model，"ratio exceeds 10×" 来自 cross-model——混合表述是否误导？（R2-Q1）
8. HellaSwag model×item > item（36.0% vs 34.3%）是否暗示 format 之外的因素在驱动 variance structure？（R2-Q3）

---

## Missing References

### 高优先级（两位 Reviewer 共识）
1. **Mizrahi et al. (2024), "State of What Art?", TACL** — 20 LLMs × 39 tasks × 6.5M instances 分析 prompt 变体影响，呼吁 multi-prompt evaluation。与本文 motivation 高度相关。最关键遗漏。
2. **Liang et al. (2023), HELM, NeurIPS** — Holistic LLM evaluation framework，multi-scenario multi-metric。
3. **Meredith (1993) + Putnick & Bornstein (2016)** — Measurement invariance 文献，与 quasi-random model facet 假设直接相关。
4. **Efron & Tibshirani (1993)** — Bootstrap CI for variance components 的经典参考和 cautionary notes。

### 中优先级
5. **Lu et al. (2022), "Fantastically Ordered Prompts", ACL** — Few-shot ordering sensitivity。R1 认为已被 Pezeshkpour (2024) 覆盖。
6. **Song et al. (2025) "LLM psychometrics"** — 已在 references.bib 中但正文引用位置可更突出。

---

## External Review (Stanford Agentic Reviewer)

未请求。项目配置中外部审稿未启用。

---

## Visual Layout Check（非评分项，Reviewer 3 / 独立视觉审查 Agent）

视觉审查已完成（3 warnings, 9 info）。主要发现：

**Warnings:**
1. **前 4 页无 display item**: 连续 4 页纯文本（仅 p3 有 Eq.1），第一个 figure/table 直到 p5 才出现。所有 7 个 main-text display items 集中在 p5-p8，前后分布严重不均。审稿人前 4 页看不到视觉锚点。
2. **Figure 跨页漂移**: Introduction (p2) 引用 "Figure 2 visualizes the contrast" 但 Figure 2 在 p7，跨 5 页 float。
3. **p8 过于拥挤**: §4.6 + §4.7 + §5 + §6 开头全部压缩在同一页，Conclusion 不足半栏。

**Info（排版规范确认）:**
- 所有表格使用 booktabs 风格，格式正确
- Figure 3 (D-study curves) 设计清晰，质量较高
- References 格式统一，无未解析引用
- Limitations 约 1/4 页，覆盖 3 个约束点，符合 EMNLP 要求
- Appendix 内容充实（Tables 5-8 + Figure 4）
- Figure 1 内部标签偏小，打印后可能接近可读性下限
- Figure 2 使用 6-7 种颜色，灰度打印下交互项可能难辨别

---

## Overall Assessment

**Overall Score: 3.0 — Findings**

**评分分布**: R1 = 3.5 (Borderline Conference), R2 = 3.0 (Findings)

**综合评估**:

本文将 G-theory 系统应用于 LLM 评测方差分解，实验规模可观（2.3M records, 8 models × 5 benchmarks），robustness checks 覆盖面广（9 项），实用工具贡献明确（D-study budget calculator + intermediate design gradient）。10× budget finding 有直接实践价值，precision separability 为评测标准化提供了可操作的指导。

但以下问题共同阻止推荐 conference acceptance：

1. **Quasi-random model facet**（N1, 共识）: 8 个 purposively selected models 不满足 G-theory 的 random sampling 前提，验证手段（LOMO n=8, 4-model subset）功效不足。所有 G coefficients 和 D-study budgets 均依赖此假设。
2. **Format-associated pattern**（N2, 强共识）: n=5, p=0.10, benchmark-level CI 跨零，但在 Abstract 和 Contributions 中的叙事权重超出统计支撑。item-level d=1.73 与 benchmark-level claim 存在 ecological fallacy risk。
3. **D-study projection 边界**（N3, 共识方向一致）: variance component invariance 假设未充分讨论，single→cross-model 已显示实质性变化（55→93 items）。
4. **Messing (2026) 增量贡献**（N4, 分歧）: §2 对比不够充分，虽然实质性增量存在。

**置信度**: 4/5（两位 Reviewer 均为 4/5 confidence）

**接收建议**: Findings 级别接收。如果作者能在 rebuttal/修订中：(a) 补充 model facet 的 fixed vs random sensitivity analysis 或完整 8-model×5-benchmark LOMO；(b) 在 Abstract/Contributions 中将 format-associated pattern 明确降级为 preliminary observation；(c) 在 §4.5 增加 D-study projection 假设边界的显式讨论；(d) 用整段详细对比 Messing (2026) TEE 框架——论文可达到 3.5 (Borderline Conference) 水平。

---

## Detailed Comments

### §1 Introduction
- "no unified factorial framework exists" 过于绝对（Bouthillier 2021, Messing 2026 已有）。建议改为 "no unified framework has simultaneously crossed infrastructure and methodology facets across benchmarks"。
- Contribution list 应更清晰地标注统计支撑强度：Contribution 1 (D-study budgets) 强支撑；format-associated pattern 需标注 "descriptive, n=5"；Contribution 3 (toolkit) 无争议。
- 引用 "Figure 2" 距实际出现跨 5 页，建议调整 float 或延后引用。

### §2 Related Work
- Positioning 段与 Messing (2026) 的对比过于简略。建议展开为：(a) Messing 的 TEE 框架范围（5 facets, 单 benchmark, judge identity dominant）；(b) 本文的增量（fix judge, 5 benchmarks, infrastructure facets, cross-format comparison）；(c) 两项工作如何互补。
- 遗漏 Mizrahi et al. (2024) TACL、HELM (2023)。
- IRT paragraph 的最后一句（"IRT-selected items...systematically underestimate"）是 strong claim，需要 caveat。

### §3 Method
- §3.1: "item-related variance" bundling 的 LLM-specific 解释（dual interpretation）值得更深入讨论。
- §3.2: 200-item sampling 代表性论证应更充分——报告所选 10 subjects 的特征分布。
- §3.3: Ordering "structurally inert" 应更显著地标注为设计约束而非实证发现。
- §3.6: Quasi-random facet 辩护需加强——补充 model facet 的 fixed vs random sensitivity analysis。

### §4 Experiments
- §4.3: unbundled MC/FF 比较（item only: 34-38% vs 17-24%）是更干净的证据，建议在正文中给予同等权重。§4.3 内两个 ρ 并列（within-MMLU p=0.005 vs cross-benchmark p=0.089）易造成后者已被 confirmed 的误读。
- §4.4: 加入明确限定 "under binary correctness scoring, for full/half-precision formats"。
- §4.5: 增加一段讨论 D-study projection 核心假设、已观察到的假设偏离、以及 budgets 适用边界。
- §4.6: 讨论 2-model G=0.71 时区分 within-family 高相似性的混淆效应。

### Figures/Tables
- Table 3 "Prompt" 行 MC vs FF 非对称报告需更清晰的 caption 说明。
- Figure 1 内部标签偏小。
- Figure 2 灰度打印下交互项颜色可能难辨别。

### Abstract
- 数字过密（>20 个），建议精简至 3-4 个关键数字。
- "no unified factorial framework exists" → "no study has simultaneously crossed..."
- Format-associated pattern 的表述应与 §4.3 的 hedging 一致。
- 考虑加入一句 cost trade-off context。

### Limitations
- 当前覆盖 3 点，篇幅合理。建议补充：quantization 未覆盖、few-shot example identity 未交叉、reduced crossing validation 仅 MMLU。