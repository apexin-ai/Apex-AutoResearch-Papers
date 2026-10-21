---
round: 7
review_mode: fresh
overall_score: 3.5
timestamp: 2026-05-22T15:28:36.734322+00:00
reviewer_ids: [1, 2, 3]
cross_response_reviewer_ids: [1, 2, 3]
force_resubmit: False
---

# Round 8 审稿报告 — nlp_variance_gtheory

**论文**: "Reproducibility Budgets for Open-Weight LLM Evaluation: A Generalizability Theory Analysis"
**Venue**: EMNLP 2026 (ACL Rolling Review)
**审稿模式**: Fresh (重新审稿)
**Reviewer 编排**: 2 人 — R1 方法严谨性, R2 新颖性/完整性（R3 本轮未激活）
**轮次**: Round 1 独立审稿 → 交叉分享 → 收敛（1 轮完成）

---

## Summary

本文将 Generalizability Theory (G-theory) 系统性应用于 LLM 评估的方差分解，在 8 个 7-9B 开源 instruction-tuned 模型和 5 个 benchmark 上交叉 7 个 facets（item, model, precision, prompt, seed, temperature, ordering），总计约 2.3M binary evaluation records。核心贡献是将方差分量转化为 D-study reproducibility budgets：推荐的 3-prompt × 3-seed 设计将 item 需求从 552 降至 178（G ≥ 0.80），full multi-facet 设计进一步降至 55 items。附带发现包括 precision separability（BF16/FP16 functionally identical）和 format-associated variance patterns（MC item-dominated vs. FF interaction-dominated，但统计功效不足 p=0.10）。

---

## Strengths

**S1. 实验规模与设计严谨性**。7-facet fully crossed design 跨 5 benchmarks，2.3M observations——目前最大规模的 LLM evaluation variance decomposition study。Factorial design 允许估计交互效应，是 piecemeal 研究无法实现的。[R1, R2 共识]

**S2. 鲁棒性验证异常充分**。9 项 robustness analyses（GLMM complement ρ=1.0, REML <0.5pp, item resampling CV=3.1%, LOMO CV≤1.25%, null calibration 1.0008, probit simulation, accuracy-range stability, facet specification sensitivity, reduced crossing validation）远超同类论文。[R1, R2 共识]

**S3. 统计报告的诚实性**。Format comparison 标注为 "exploratory" and "suggestive but underpowered"（p=0.10）；binary scoring conditionality 贯穿全文；random-model G 作为 conservative specification；partial-credit pilot 明确展示方差结构根本性改变（G 0.759→0.553, ρ=0.26）。这种诚实性在当前 ML 文献中难得。[R1, R2 共识]

**S4. Practical D-study gradient**。Appendix C Table 9 的 7 级 adoption gradient（from single-condition to full multi-facet）和 3×3 "minimal sufficient" 推荐为 practitioners 提供了可操作的工具。IRT 互补性论证清晰（Table 4: IRT 116 items single-condition G=0.457 vs multi-facet G=0.895）。[R1, R2 共识]

**S5. 格式完全合规**。正文 ≤8 页，ACL 模板 [review] 模式，Anonymous ACL submission，Limitations 独立一节，无 de-anonymization 风险。[R2 确认]

**S6. Reproducibility 承诺**。实验设计矩阵（Table 1）、模型标识符（Table 10）、完整 prompt 模板（Appendix E）、vLLM 版本号均已公开；代码、数据和 D-study calculator 承诺发布。[R1 4/5, R2 4/5]

---

## Weaknesses

### Must-Fix（影响接收决定）

**MF-1** [critical, 强共识] **D-study 方差分量不变性假设缺乏充分验证**
- D-study 从 observed variance components 外推到不同 design budgets，核心假设是方差分量在 item pool expansion、model universe expansion 和 temporal drift 下保持不变。
- Forward prediction (Table 8) 从 4 个 exp-001 models 预测到 8 个 models（MC |ΔG|≤0.029, FF |ΔG|≤0.065），但这 4 个模型是 8 个模型的子集——**in-sample cross-validation 而非 out-of-sample validation**。
- LOMO (Table 5) 验证 benchmark-level stability，不直接验证 item pool expansion。
- Temporal drift 在 Limitations 中提及但**无任何 empirical evidence**。
- §4.5 的 caveat（"All projections assume the 2024-2025 model generation; we recommend periodic re-estimation"）方向正确但不够充分。
- **影响**：D-study budget 推荐（Table 4, Table 7）是论文核心实用价值，如果方差分量在 model universe 扩展后变化，这些推荐便不可用。
- **建议**：(1) 明确承认 forward prediction 的 in-sample 性质；(2) 使用 held-out models 做 out-of-sample validation；(3) 讨论 temporal drift 的 plausibility bounds。
- [R1 N2 critical + R2 AGREE]

**MF-2** [critical, 强共识] **"10× fewer items" framing 掩盖总评估成本的大幅增加**
- Abstract 以 "55 vs 552 items" 和 "item reductions exceed 10×" 为核心 headline，但总评估量对比完全不同：
  - Full multi-facet: 55 items × 1,296 conditions = **71,280** vs 552 × 1 = **552** evaluations → **129× 更多**
  - Cross-model MMLU: 93 items × 2,304 conditions = **214,272** vs 1,216 × 1 = **1,216** evaluations → **176× 更多**
  - 推荐 3×3 设计: 178 × 9 = **1,602** vs 552 evaluations → **2.9× 更多**（但仅 3.1× fewer items，远非 10×）
- 10× headline 的信息优先级远高于 conditions 细节。粗心的读者可能误认为 multi-facet evaluation 更"便宜"。
- 论文的 value proposition 是 "同等 reliability 下更少 items（但更多 conditions per item）"——适用于 **item construction 是瓶颈** 的场景（如构建新 benchmark），不适用于 **compute 是瓶颈** 的场景。
- **建议**：(1) Abstract/Intro 明确报告 items × conditions 总评估量；(2) 将 3×3 推荐设计（3.1× item reduction, 2.9× more evals）作为 headline 而非 full multi-facet 的 10×；(3) 讨论 use case tradeoff。
- [R2 N1 critical + R1 AGREE]

**MF-3** [critical, 强共识] **FF benchmarks 40-44% 残差方差缺乏解释性分析**
- Table 3: GSM8K residual 39.9%, MATH 43.9%——**最大 component 是未建模的残差**。G-theory 模型对 FF benchmarks 的解释力严重不足。
- 论文仅以一句话承认 "likely reflect sources not captured by our facets: chain-of-thought path diversity, generation stochasticity, and answer extraction heuristics"，但未做任何验证分析。
- 未分析 item 特征（difficulty, length, reasoning steps）如何预测 model×item interaction 或残差大小。未量化 CoT path diversity 作为 variance source。
- **影响**：当残差占主导时，D-study projections 的基础被削弱——D-study 假设所有 systematic variance 已被 facets 捕获。如果残差含 systematic（未建模）variance，Table 7 的 FF budgets 可能过于乐观。
- **建议**：(1) 对 FF benchmarks 做 item-level regression 分析残差 predictors；(2) 讨论 residual 中 systematic vs random 的 plausible 比例；(3) 明确 G-theory 对 FF benchmarks 的适用性边界。
- [R2 N3 critical + R1 AGREE]

### Should-Fix（影响评分但不一票否决）

**SF-1** [warning, 共识] **Partial-credit pilot 发现的 implications 被低估**
- Binary vs partial credit: prompt variance 25.5%→1.2%, residual 28.2%→46.9%, G 0.759→0.553, item difficulty ρ=0.26。方差结构发生质变。
- "item difficulty dominates variance" 可能部分是 binary threshold artifact。
- **建议**：在 §4.4 或 §5 增加独立段落讨论 implications。
- [R1 W1 + R2 AGREE]

**SF-2** [warning, 共识] **Format analysis (§4.3) 统计基础薄弱且存在 confounds**
- n=5 benchmarks, permutation p=0.10 是组合分辨率下限。MC/FF 设计不对称性（ordering, prompt semantics）混淆 format effect。
- **建议**：§4.3 明确讨论 confounds；§5 降低为 "hypothesis-generating observation"。
- [R1 W2 + R2 W5, 双向 AGREE]

**SF-3** [warning, 共识] **Data contamination 作为 model×item interaction 的混淆变量未讨论**
- Model×item 30-36% 可能部分来自 benchmark memorization 而非 genuine DIF。
- **建议**：§4.2 或 Limitations 讨论；引用 Golchin & Surdeanu (2023)。
- [R2 W1 + R1 AGREE]

**SF-4** [warning, 共识] **8 个 quasi-random models 的辩护有待加强**
- LOMO/Cohen's κ 证明 internal consistency 但非 representativeness。
- **建议**：更精确定义 target universe；讨论 breakdown conditions。
- [R1 W3 + R2 AGREE (partial)]

**SF-5** [warning, 分歧降级] **标题/Abstract scope 限定不够**
- R1 认为 critical（标题应加限定），R2 认为 should-fix（标题 factually accurate）。
- Director 判定 Should-Fix：Abstract 已有限定，标题修改推荐但非必须。
- [R1 N3 vs R2 REBUT]

**SF-6** [warning, 共识] **Contribution 层级权重不均**
- C2 (null result) 和 C3 (toolkit) 不应与 C1 (D-study budgets) 并列。
- **建议**：C2 降级为 C1 sub-finding；C3 移至 practical implications。
- [R2 W2 + R1 部分同意]

**SF-7** [warning, 共识] **Bootstrap CI 仅 item-level resampling**
- 未纳入 model-level uncertainty。LOMO 部分回应但未转化为 CI 比较。
- **建议**：注明 item-level uncertainty only；可选补充 model-level jackknife。
- [R1 W4 + R2 AGREE]

**SF-8** [warning, 共识] **ARC model×prompt 异常 (8.0%) 未讨论**
- Table 3 ARC model×prompt 远高于其他 MC benchmarks。
- [R2 W3 + R1 AGREE]

**SF-9** [warning, 共识] **Conclusion 过于简短**
- 缺 practical implications、use case guidance、future directions。
- [R2 W4 + R1 AGREE]

---

## Reviewer Consensus

以下问题两位 Reviewer 达成共识 [AGREE]：
1. D-study 不变性假设缺乏 out-of-sample validation [MF-1]
2. 10× cost framing 误导 [MF-2]
3. FF 残差未分析 [MF-3]
4. Partial-credit implications 被低估 [SF-1]
5. Format analysis confounds [SF-2]
6. Data contamination 未讨论 [SF-3]
7. Quasi-random model 辩护不充分 [SF-4]
8. Bootstrap CI limitation [SF-7]
9. ARC anomaly [SF-8]
10. Conclusion 过短 [SF-9]

## Reviewer Divergence

**1. Henderson Method I binary validation (R1 N1 critical vs R2 REBUT)**
- R1: Probit ρ=0.73 仅中等相关；缺 bias/RMSE 报告。
- R2: 证据链整体强度足够——理论无偏 + REML <0.5pp + null calibration 1.0008。ρ=0.73 反映 dichotomization 信息损失，不是 estimator bias。
- Director 判定：降级为 Should-Fix。补充 bias/RMSE 报告即可。

**2. 相对 Messing (2026) 增量贡献 (R2 N2 critical vs R1 REBUT)**
- R2: 三个增量中两个是零效应/underpowered；D-study 是标准操作。
- R1: Infrastructure null results 有实用价值；cross-benchmark insight 一致非随机；本文与 Messing 互补非增量。
- Director 判定：维持 Should-Fix。加强 D-study practical framing。

**3. 标题 overclaiming (R1 N3 critical vs R2 REBUT)**
- 已降级为 SF-5。

---

## Questions for Authors

Q1: 请提供 Table 4 和 Table 7 中每个 design 的**总评估量** (items × conditions) 对比。[R2]
Q2: 是否考虑过使用 held-out models 做 out-of-sample forward prediction？[R1]
Q3: Binary ρ=0.26 是否意味着 "item difficulty dominates" 是 binary threshold artifact？[R1]
Q4: Model×item 30-36% 中有多少可能来自 data contamination？[R2]
Q5: FF 残差方差是否有 item-level feature predictors？[R2]
Q6: 能否报告 probit simulation 各方差分量的 bias/RMSE？[R1]
Q7: ARC model×prompt 8.0% 如何解释？[R2]
Q8: 何时选择 single-condition 552 items 而非 3×3 的 178 items？[R2]

---

## Missing References

1. **Cardinet, Johnson & Pini (2010)** — G-theory dichotomous data 标准参考 [R1, R2]
2. **Golchin & Surdeanu (2023)** / **Sainz et al. (2023)** — Benchmark data contamination [R2, R1]
3. **Kiela et al. (2021)** — DynaBench, benchmark temporal drift [R1, R2]

---

## External Review (Stanford Agentic Reviewer)

外部审稿：未请求（项目未配置 paperreview.ai）。

---

## Visual Layout Check（非评分项）

视觉审查已完成（0 critical, 1 warning, 10 info）。

**Warning:**
- **Pages 3-4**: 连续两页纯文本，无 figure/table 穿插。建议将 Table 1 或 Figure 2 提前打破纯文本墙。

**Info**: Figure 2 偏小、Table 3 字号接近下限、Figure 3 建议确认灰度可辨别性、Figure 1 建议确认色盲友好性。Tables 格式规范，Limitations/References 无问题。

---

## Overall Assessment

**评分: 3.5 (Borderline Conference)**
**置信度: 4/5**

本文将 G-theory 系统性引入 LLM 评估是有价值的方法论贡献，实验规模和鲁棒性验证领先同类工作。但三个系统性问题限制当前接收：(1) D-study 外推缺乏 out-of-sample validation，(2) 10× cost framing 误导，(3) FF 残差 40-44% 未分析。如果三个 Must-Fix 充分 address（特别是 cost framing 重构和 FF 残差分析），评分有望提升至 4.0 (Conference)。

**注**: R3 本轮未激活——EMNLP 为一般会议，Director 编排决定使用 2 位 Reviewer（方法严谨性 + 新颖性/完整性），覆盖充分。R3 的 reviewer slot 来自项目历史配置，本轮不适用。