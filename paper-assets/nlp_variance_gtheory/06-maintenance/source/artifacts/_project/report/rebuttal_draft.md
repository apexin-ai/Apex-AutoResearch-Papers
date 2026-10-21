# Rebuttal 框架文档

> 项目：nlp_variance_gtheory | 目标：EMNLP 2026 via ARR | DDL 2026-05-25
> 基于 Round 8 审稿意见，三个 Must-Fix + 防御论点 + 新增分析汇总

---

## 1. Round 8 三个 Must-Fix 的回应

### MF-1: FF Residual Regression 分析

**审稿原文摘要**：Free-form benchmark 的 residual variance 偏高（GSM8K 51.9%, MATH 56.3%），是否说明 G-theory 框架对 FF 任务的解释力不足？需要分析 residual 的结构——是随机噪声还是可归因的系统性效应。

**我们的回应要点**：

1. FF 高 residual 是**系统性的**，不是随机噪声。我们对每个 benchmark 的 per-item residual variance 进行 OLS 回归，使用 item difficulty（含二次项）及 benchmark-specific 特征作为预测变量：
   - MATH: R²=0.856 (adj R²=0.847)，difficulty 二次项为最强预测因子（inverted-U pattern）
   - GSM8K: R²=0.468 (adj R²=0.454)，difficulty 同样主导（difficulty-only R²=0.449）
   - FF 平均 R²=0.662 vs MC 平均 R²=0.252（MMLU 0.377, ARC 0.221, HellaSwag 0.156）

2. **Inverted-U mechanism**：中等难度 item 的 residual 最高——太简单（所有模型都对）或太难（都错）的 item 天然方差小，中等难度 item 对 prompt/seed 变化最敏感。FF benchmark 正好集中在中等难度区间，这解释了 residual 偏高的结构性原因。

3. FF 的高 residual 不是框架失败，而是**有信息的**：它量化了 FF 任务中 prompt×item 和 seed×item 交互效应的大小——这些在 MC 任务中被 item difficulty 的 dominant signal 所"压制"。

**支撑数据/图表**：
- 回归结果：`artifacts/exp004/ff_residual_analysis/ff_residual_regression.json`
- 5 个 difficulty-vs-residual scatter plot（每个 benchmark 一张）：`artifacts/exp004/ff_residual_analysis/difficulty_vs_residual_{mmlu,arc,gsm8k,math,hellaswag}.pdf`
- 论文 Appendix E（R²(diff. only) 数据已修正）

---

### MF-2: 72B Scale Validation

**审稿原文摘要**：实验仅覆盖 7B-9B 模型，variance structure 是否在更大 scale 下保持？需要 out-of-sample scale validation。

**我们的回应要点**：

1. **72B 单模型 G-study**（Qwen2.5-72B-Instruct, MMLU, 200 items × 288 conditions = 57,600 records）：
   - item_id=83.25%, G_item=0.979, grand_mean=0.870
   - 方差结构与 7B/9B 一致：item_id 主导，prompt:item 次之（6.81%），residual 7.45%
   - **Within-family 3-point comparison**：3B item_id=75.3% (G=0.963) → 7B 73.4% (G=0.956) → 72B 83.2% (G=0.979)
   - 更大模型更稳定（accuracy 更高 → 更多 item 接近 ceiling → item difficulty variance 比例更高）

2. **3 模型 crossed G-study**（3B/7B/72B, 172,800 records）：
   - model:item=38.55% > item_id=35.71%（model×item 交互成为第一大源——因为 scale 差异带来 DIF）
   - G_item=0.720（低于单 scale 的 0.95+，因为 model:item 作为 error 进入 δ）
   - Model 主效应=4.84%（scale 差异本身解释的方差）

3. **Item difficulty 跨 scale 保持**：
   - 7B-72B Spearman ρ=0.571 (p<1e-18)，3B-72B ρ=0.509 (p<1e-14)
   - 相关性中等偏弱（非 ρ>0.9），归因于 ceiling effect：72B accuracy=87%，许多 item 对 72B 来说太简单，区分力下降
   - **结论**：item difficulty 结构跨 scale 保持（qualitatively invariant），但 scale 差异引入了 substantial DIF

**支撑数据**：
- 72B 单模型：`artifacts/exp004/data/exp003_72b_single_gstudy.json`（exp003_scale_72b）
- 3 模型 crossed：`artifacts/exp004/data/exp003_scale_crossed_3model.json`
- Item difficulty 相关：`artifacts/exp004/data/scale_item_difficulty_correlation.json`
- 7B 参考：`exp003_scale_7b` (item_id=73.37%, G=0.956)
- 3B 参考：`exp003_scale_3b` (item_id=75.32%, G=0.963)

---

### MF-3: Probit Simulation / Binary Data 的 G Coefficient

**审稿原文摘要**：Binary (0/1) 数据的方差分析是否需要 probit 或 tetrachoric 修正？Henderson Method I 在 binary 数据上的 G 估计是否可靠？

**我们的回应要点**：

1. **理论考量**：Binary 数据的 G coefficient 理论上可以通过 tetrachoric correlation 或 probit link function 修正。然而 G-theory 文献中（Brennan 2001, Chapters 4-5），Henderson Method I 基于 ANOVA 的方差分量估计**对 binary 数据仍然有效**，因为它是矩估计（method of moments），不依赖正态性假设。

2. **实证一致性验证**：
   - Binary G=0.759 → Partial-credit G=0.553（GSM8K, Llama-3.1-8B, exp006_partial_credit）
   - Binary 得到更高 G 是**预期行为**：binary 压缩了信息（多步推理→0/1），减少了条件间的变异性，从而膨胀了 item 信号的相对占比
   - 方差结构排序在两种 scoring 下保持一致：item_id 和 prompt:item 仍是 top 2

3. **Marginal logit ANOVA cross-check**：对 binary 数据做 logit 变换后重新 ANOVA，所有 7 个 grouped component 排名完全保持（ρ=1.0），与 MQL-1 理论预期一致（在 p̄≈0.70 时 logit 变换近似线性）。

4. **实用立场**：我们在论文中明确讨论 binary scoring 的局限性（§5 Limitations），同时指出：(a) Henderson I 是矩估计，不依赖分布假设；(b) logit cross-check 确认排名稳定性；(c) partial-credit pilot 显示趋势方向一致。

**支撑数据**：
- Partial-credit comparison：`artifacts/exp006_partial_credit/partial_credit_comparison.json`
- Binary G=0.759, item_id=19.98%; Partial G=0.553, item_id=12.74%
- Logit ANOVA cross-check：见 paper_framing.md GLMM cross-check 部分

---

## 2. Messing 增量争议（FR6-N4）防御论点

**审稿原文摘要**：Messing (2026, arXiv:2604.11581) 已经将 G-theory 应用于 LLM evaluation。本文相对于 Messing 的增量贡献是什么？

**核心定位**：Messing = rater agreement 框架（judge identity 43.8%, prompt×judge 12.4%）；本文 = multi-facet variance decomposition + D-study design optimization。两者互补但方法论目标不同。

**三个具体论点**：

### 论点 1：Item×Model 交互分解（DIF）
- Messing 研究 LLM-as-judge 场景，facets 是 judge、prompt、system instruction 等——模型是被评估的对象，item 作为 fixed context
- 本文将 model 作为 crossed quasi-random facet，分解出 **model×item interaction (DIF)**：8 模型 MMLU model:item=30.21%，这是 Messing 框架中根本不存在的方差源
- **具体例子**：某些 MMLU item 在 Qwen 上容易但在 Mistral 上难（DIF），这种 model-specific difficulty 占总方差的 30%+。Messing 的 rater agreement 框架无法捕捉这一效应

### 论点 2：Multi-benchmark 方差结构比较
- Messing 仅在单一 benchmark 上分析
- 本文跨 5 个 benchmark（MMLU/ARC/HellaSwag/GSM8K/MATH, 2,304,000 records）揭示 **format-associated variance pattern**：MC item_id 34-38% vs FF 17-24%（Cohen's d=1.73），并识别 item difficulty heterogeneity 作为机制（within-MMLU ρ=0.806, p=0.005）
- 这是 Messing 无法获得的跨 benchmark comparative insight

### 论点 3：D-study Reproducibility Budget
- Messing 报告方差分量百分比但**不提供 D-study 优化建议**
- 本文的核心实用贡献：D-study 投影显示 3×3 design（3 prompts × 3 seeds, 178 items, 1,602 evals/model）即可达到 G≥0.80（MMLU），相比 single-condition 的 552 items 实现 3.1× item 缩减
- **具体例子**：如果 reviewer 只有资源评估 1000 个 item-model pair，D-study 告诉你用 3 prompts × 3 seeds × 111 items（=999 evals）比 1×1×1000 items 更可靠（G 更高）

**小结**：Messing 和本文的关系类似 Cohen's κ 和 G-theory 的关系——前者给出 agreement 度量，后者给出 variance decomposition + 设计优化。本文引用 Messing 作为 confirmatory evidence（G-theory 在 LLM evaluation 中可行），同时明确区分贡献维度。

---

## 3. 新增分析摘要（Round 6-8 补充分析）

### 3.1 Fixed vs Random Model Assumption
- **结论**：Treating model as fixed inflates G by mean +0.093 (range 0.077-0.113)。Random-model treatment 更保守也更适合 generalization。
- All-random G mean=0.882, fixed G mean=0.975
- **数据**：`artifacts/exp004/data/fixed_vs_random_model.json`

### 3.2 LOMO 8×5 (Leave-One-Model-Out, 8 models × 5 benchmarks)
- **结论**：40 个 7-model subsets 全部保持 item_id dominance（MMLU/ARC/MATH）或 model:item dominance（HellaSwag/GSM8K）。G_item CV < 1.3%（MMLU 0.49%, ARC 0.94%, HellaSwag 1.09%, GSM8K 1.25%, MATH 1.20%）。
- MMLU G range: 0.877-0.894 (spread=0.012)
- Max |ΔG| across all benchmarks: 0.030 (GSM8K, removing Gemma-2-9B)
- **数据**：`artifacts/exp004/data/lomo_8x5_full.json`

### 3.3 Cohen's κ Pairwise Agreement
- **结论**：MC 平均 κ 高于 FF。MMLU mean κ=0.461, ARC κ=0.376, HellaSwag κ=0.332; GSM8K κ=0.335, MATH κ=0.326。
- MC 的 item agreement 高于 FF，与 G-study 中 MC item_id% 更高的结论一致
- **数据**：`artifacts/exp004/data/cohens_kappa_pairwise.json`

### 3.4 Partial-Credit Pilot
- **结论**：Binary G=0.759 → Partial-credit G=0.553（GSM8K, Llama-3.1-8B）。Binary 压缩信息导致 G 膨胀。
- Partial-credit item_id 从 19.98% 降至 12.74%，residual 从 28.2% 升至 46.0%
- **数据**：`artifacts/exp006_partial_credit/partial_credit_comparison.json` (exp006_partial_credit)

### 3.5 Forward Prediction (4→8 模型)
- **结论**：用 4-model variance components 预测 8-model G_item，mean |ΔG|=0.035。
- Per-benchmark: MMLU |ΔG|=0.009, ARC 0.012, HellaSwag 0.029, GSM8K 0.059, MATH 0.065
- FF benchmark 预测误差更大（source 4-model variance components 不稳定），但方向一致
- **数据**：`artifacts/exp004/forward_prediction/forward_prediction_results.json`

### 3.6 D-study 3×3 Budget
- **结论**：3 prompts × 3 seeds × n items 设计下 min items for G_model≥0.80：
  - MMLU: 347 items (full 288-cond: 75)
  - HellaSwag: 32 items (full: 29)
  - MATH: 15 items (full: 10)
  - ARC: **impossible** (g_asymptotic=0.534)
  - GSM8K: **impossible** (g_asymptotic=0.785)
- ARC 和 GSM8K 的 model:item 交互太大，即使无限 items 也无法达到 G_model≥0.80（3×3 设计下）
- 注：此处 G 的 object of measurement 是 model（区分模型能力），非 item
- **数据**：`artifacts/exp004/data/dstudy_3x3_budget.json`

### 3.7 Budget Sensitivity（|ΔG|=0.035 的影响）
- **结论**：Forward prediction 的 |ΔG|=0.035 误差对应 ~23% 额外 items 需求。
- 各 benchmark Δn：MMLU +41, ARC +13, HellaSwag +19, GSM8K +67, MATH +51
- 百分比稳定（22.9-24.5%），因为 G-formula 比率是 variance-component-independent
- **数据**：`artifacts/exp004/data/budget_sensitivity_delta_g.json`

### 3.8 Subject-Level G-Study (MMLU 10 subjects × 20 items)
- **结论**：Mean G_item=0.843, 9/10 subjects G≥0.778。
- 最高：international_law G=0.930 (item_id=44.4%), clinical_knowledge G=0.923 (item_id=47.5%)
- 最低：high_school_mathematics G=0.614 (item_id=10.4%, model:item=41.9%——数学推理类 subject 表现类似 FF benchmark)
- 与整体 200-item G=0.896 的差距来自 n_items 缩小（20 vs 200）
- **数据**：`artifacts/exp004/data/mmlu_subject_level_gstudy.json`

### 3.9 72B vs 7B Item Difficulty Correlation
- **结论**：Spearman ρ=0.571 (p<1e-18), Pearson r=0.428。
- 中等相关，受 72B ceiling effect 影响（accuracy 87%，大量 item p→1.0）
- 3B-72B: ρ=0.509, r=0.450
- Item difficulty ranking 跨 scale 保持（qualitatively invariant）但非 identical
- **数据**：`artifacts/exp004/data/scale_item_difficulty_correlation.json`

---

## 附录：关键数字速查表

| Metric | Value | Source |
|--------|-------|--------|
| 总记录数 | ~2.3M | 8 models × 5 benchmarks |
| 8-model MMLU item_id% | 37.88% | exp004 |
| 8-model MMLU model:item% | 30.21% | exp004 |
| 8-model MMLU G_item | 0.896 | exp004 |
| MC mean item_id% | 36.68% | MMLU/ARC/HellaSwag |
| FF mean item_id% | 20.45% | GSM8K/MATH |
| Cohen's d (MC vs FF) | 1.73 | exp004 |
| Within-MMLU gradient ρ | 0.806 (p=0.005) | exp004 |
| 72B single G_item | 0.979 | exp003_scale_72b |
| 72B single item_id% | 83.25% | exp003_scale_72b |
| 3-model crossed G_item | 0.720 | exp003 crossed |
| FF residual R² (MATH) | 0.856 | ff_residual_analysis |
| FF residual R² (GSM8K) | 0.468 | ff_residual_analysis |
| FF mean R² | 0.662 | ff_residual_analysis |
| MC mean R² | 0.252 | ff_residual_analysis |
| Fixed vs random ΔG | +0.093 mean | fixed_vs_random_model |
| LOMO max |ΔG| | 0.030 | lomo_8x5_full |
| Forward prediction mean |ΔG| | 0.035 | forward_prediction |
| Budget sensitivity | ~23% more items | budget_sensitivity |
| Partial-credit ΔG | binary 0.759 → partial 0.553 | exp006_partial_credit |
| Subject-level mean G | 0.843 (9/10 ≥ 0.778) | subject_level_gstudy |
