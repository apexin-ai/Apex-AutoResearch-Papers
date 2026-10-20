---
round: 0
review_mode: 
overall_score: borderline
timestamp: 2026-05-21T08:48:58.456856+00:00
reviewer_ids: [1, 2]
cross_response_reviewer_ids: [1, 2]
force_resubmit: False
---


# 审稿报告 — nlp_variance_gtheory (Round 1)

**审稿日期**: 2026-05-21
**Reviewer 编制**: 2 人（R1: 方法论/实验严谨性; R2: 新颖性/scope/完整性）
**交叉分享**: 完成（Round 1 即达成收敛）

---

## Summary

论文将 Generalizability Theory (G-theory) 应用于 LLM evaluation，对 5 个 benchmarks（MMLU, HellaSwag, ARC-Challenge, GSM8K, MATH）× 4-6 个模型 × 多 facets（prompt, seed, temperature, ordering, precision, GPU architecture）进行 ~4.25M records 的 crossed factorial 方差分解。核心发现为 cross-benchmark variance gradient——item difficulty dominance 从 knowledge-retrieval tasks (MMLU 42.1%) 向 reasoning tasks (MATH 18.1%) 递减，model×item interaction 反向递增——并提供 benchmark-specific D-study reproducibility budgets。

---

## Strengths

**S1. 实验规模和 factorial 覆盖度为该领域最全面。** 5 benchmarks × 6 models × 2 GPU architectures × multiple facet levels，总计 ~4.25M records 的 fully crossed design，远超现有 LLM evaluation variance 文献。

**S2. Robustness analysis 体系完整且系统性强。** 6 项独立验证（bootstrap CI, jackknife, item resampling, REML cross-check, fixed vs random sensitivity, binary null simulation）形成了对方法论质疑的全面 defense layer。

**S3. Cross-benchmark gradient 作为定性发现有实质价值。** "variance structure is benchmark-conditional" 解释了文献中关于 "item 重要还是 model 重要" 的矛盾结论，即使 gradient 的定量精度和适用范围需要修正，这一定性 insight 仍然成立。

**S4. Practitioner toolkit 有直接实用价值。** Table 9 的 D-study budget calculator 和 Section 6.3 的实操建议（benchmark-specific item × prompt × seed × ordering 组合）是 immediately actionable 的 guidelines。

**S5. Separability finding 支持孤立因子研究的组合。** Hardware × methodology < 0.18%（binary）意味着独立研究 hardware 和 methodology 的文献结论可以合法组合，这是一个有实际意义的 methodological contribution。

**S6. Metric qualification 避免了过度泛化。** Binary vs text-exact-match 下 separability 的差异（0.18% vs 0.72%）提供了必要的 metric-conditional qualification。

---

## Weaknesses

### Must-Fix（3 个，均为两位 Reviewer 共识）

**MF1. [method, critical] Binary data 上 ANOVA-based G-theory 缺乏理论辩护 (R1-N1, R2 AGREE)**

Henderson Method I 直接应用于 0/1 binary responses，G-theory 线性模型假设近似正态分布，binary data 系统性违反。论文 Section 5.7 的 null simulation 证明了 signal 存在（observed item_id 是 null 的 737×），但未证明方差分量估计无偏。论文引用了 Jung et al. (2017) logistic-link generalized G-theory 和 Shavelson et al. (1989) binary G-theory 但未使用也未解释原因。

R2 在交叉回应中补充了关键分析：Bernoulli variance ceiling p(1-p) 对不同 accuracy benchmarks 影响不同——GSM8K (acc≈0.485, p(1-p)=0.250) 比 MMLU (acc≈0.67, p(1-p)=0.221) 高约 13%，部分 inflate 了 GSM8K 的 model×item 分量，cross-benchmark gradient 可能部分是 Bernoulli ceiling artifact 而非 task complexity 真实效应。

论文的 logprob scoring robustness check（continuous measure，不受 Bernoulli 约束）显示 gradient preserved，部分缓解但不完全解决——因为 primary claims 全部基于 binary scoring。

**要求**: (a) 运行 logistic-link G-theory sensitivity check（Jung et al. 2017）与 ANOVA-based 结果对比；或 (b) 提供严格理论论证说明 balanced design 下 Henderson I 对 binary data 的 bias bounded；(c) 讨论 accuracy distribution 对 Bernoulli-adjusted variance decomposition 的 cross-benchmark differential 影响。

**MF2. [method, critical] 仅 4 个模型作为 crossed random facet，model×item 估计不稳定 (R1-N2, R2 AGREE)**

4 个 7-9B 模型（Llama-3.1-8B, Gemma-2-9B, Mistral-7B, Qwen3-8B）是 purposive selection（4 个 architecture families），非 random sample from population。Bootstrap CI 宽度较大（MMLU model×item [28.4, 37.9], GSM8K [39.8, 53.7]）。Leave-one-model-out spread 0.023，但 4 选 3 的 jackknife 统计 power 极低。14B extension 仅 2 个模型，不构成有效 scale validation。

R2 在交叉回应中补充：4 个模型共享大量 training data（Common Crawl, Wikipedia），导致 model×item 可能被系统性低估——若纳入 training pipeline 差异更大的模型，gradient 可能更陡。但 LOMO 分析显示 variance hierarchy 的 qualitative 结论（item_id dominance on MMLU）对 model selection 有一定鲁棒性。

**要求**: (a) 承认 model 为 fixed 或 quasi-random facet，调整 G-coefficient 公式和 D-study interpretation；(b) 在 Table 11 fixed vs random sensitivity analysis 中展示 model-as-fixed 完整分析；(c) 讨论 purposive vs random sampling 对 generalizability 的影响。

**MF3. [framing, critical] Cross-benchmark gradient generality claim 超出实验基础 (R2-N1, R1 AGREE)**

5 个 benchmarks 全部落在 "factual knowledge retrieval → multi-step mathematical reasoning" 一条轴上（closed-form QA），完全未覆盖 code generation、translation、summarization、instruction following、open-ended generation 等 task types。Title "Across Benchmarks" 和 Abstract "no universal reproducibility recipe" 暗示跨所有 benchmark 类型的普遍性，但实验仅支持一个 task dimension。n=5 的 monotonicity 统计功效低（Spearman ρ=1.0 在 n=5 时 p≈0.017 单侧，且 ranking non-independent from data）。

R1 在交叉回应中补充：item_id 与 model×item 之间存在机械负相关（两者是 variance decomposition 中最大分量，总和受约束），"双向 monotonic" 的证据价值低于表面——一个方向 monotonic 几乎机械保证另一个方向也 monotonic。

**要求**: (1) Abstract/Conclusion 限定 gradient 适用范围为 "knowledge-to-reasoning continuum of closed-form QA benchmarks"；(2) Discussion 讨论 gradient 在其他 task dimensions 上的未知性；(3) 用 independent measure 验证 benchmark ordering（如 average reasoning chain length）或 permutation test（5!=120 排列中多少种使双方 monotonic）；(4) 弱化 "no universal recipe" 为 "recipe varies along the knowledge-reasoning spectrum"。

### Should-Fix（10 个）

**SF1. [experiment] D-study 外推缺乏 progressive validation (R1-W1, R2 AGREE)**
从 200 items 外推至 1320 items（6.6×），未验证方差分量在 200→400→800 items 时是否稳定。建议在至少一个 benchmark 上运行 progressive validation，或明确声明 D-study projections 为 model-based extrapolation。

**SF2. [framing] Post-hoc reasoning complexity ordering 缺乏独立操作定义 (R1-W2, R2 强烈 AGREE)**
HellaSwag 是 commonsense completion 而非典型 reasoning，ARC-Challenge 是 science QA 而非纯 reasoning。item_id 与 model×item 的机械负相关意味着论文应只 claim 一个方向（item_id gradient），将 model×item 对称性描述为机械推论。建议 permutation test + independent complexity measure。

**SF3. [experiment] Design matrix 不一致且缺少汇总表 (R1-W3, R2 AGREE)**
Gemma 仅 BF16+FP32 无 FP16，MMLU 用 3×3 其他用 2×2，analysis subset 选择分散在不同 section。建议提供 design matrix 表（benchmark × model × precision 数据状态）。

**SF4. [method] Ordering facet 在开放式 benchmarks 上定义不明 (R1-W4, R2 AGREE)**
GSM8K/MATH 的 ordering 操作化（option ordering vs few-shot ordering）未明确。如使用不同操作化，不应使用相同 facet 名称。

**SF5. [method] T=0 下 seed 效应需 temperature-stratified 分析 (R1-W5, R2 部分 REBUT)**
R1 认为 T=0 greedy decoding 理论上 seed 无效应；R2 指出 vLLM batched inference 的 floating-point non-associativity 可能导致 T=0 下仍有 seed-correlated variation。**共识**：应报告 temperature-stratified seed variance（T=0 vs T>0），讨论 pooling 影响。

**SF6. [framing] IRT vs G-theory 对比 (C3) 应降级 (R2-W1, R1 AGREE)**
G-theory 建模更多 variance sources 必然需要更多 items，方向上是数学必然。建议将 C3 表述为 "first empirical quantification of the multi-facet reliability gap" 而非 primary contribution。

**SF7. [framing] "No universal recipe" 叙事需 recalibrate (R2-W2, R1 部分 REBUT)**
跨 benchmark 推荐差异主要在 item count（414 vs 648, 1.6×），methodological facets 推荐几乎一致。R1 指出 item count 差异本身实质性（56% increase），但同意 "no universal recipe" 措辞 overclaim。**共识**：更准确表述为 "item budget is benchmark-conditional; methodological protocol is largely transferable"。

**SF8. [framing] 与 Mesting (2026) 差异化偏增量 (R2-W3, R1 AGREE)**
三个 extension（infrastructure, multi-benchmark, model as random facet）均属 G-theory straightforward 应用。建议明确承认方法论增量性，将重心放在 empirical findings 独特性上。

**SF9. [writing] Related Work 缺少关键文献方向 (R2-W4, R1 AGREE)**
缺少：(a) 教育测量 cross-test G-study 比较文献；(b) benchmark contamination/saturation 对 item_id variance 解释的影响（特别是若模型在训练中见过 benchmark items）；(c) GLMM 在 NLP evaluation 中的应用（与 MF1 binary data 直接相关）。

**SF10. [framing] Fine-tuning G-study 超出核心 scope (R2-W5, R1 AGREE)**
RoBERTa fine-tuning 是 encoder-only model 的 training variance，与 LLM inference evaluation 是不同 paradigm。建议压缩至 2-3 句 Discussion mention 或标注为 out-of-scope preliminary observation。

---

## Reviewer Consensus

以下问题两位 Reviewer 完全一致（[AGREE]）：

| Issue | 共识内容 |
|-------|---------|
| MF1 (binary data) | ANOVA-based G-theory 应用于 binary data 需要 logistic-link sensitivity check 或严格理论辩护 |
| MF2 (model facet) | 4 个 purposive-selected 模型不满足 random facet 假设，需重新定位为 fixed/quasi-random |
| MF3 (scope overclaim) | Gradient claim 需限定为 knowledge-to-reasoning continuum，"no universal recipe" 需弱化 |
| SF1 (D-study extrapolation) | 需 progressive validation 或明确声明为 model-based extrapolation |
| SF2 (post-hoc ordering) | 需独立操作定义 + permutation test |
| SF3 (design matrix) | 需汇总表 |
| SF4 (ordering definition) | 需明确每个 benchmark 的操作化 |
| SF6 (IRT comparison) | C3 应降级为 practical implication |
| SF8 (vs Mesting) | 应承认方法论增量性 |
| SF9 (related work) | 需补充教育测量 G-study、benchmark contamination、GLMM |
| SF10 (fine-tuning scope) | 应压缩或删除 |

## Reviewer Divergence

两处轻微分歧，均不影响整体判断：

**SF5 (seed at T=0)**：R1 认为 T=0 下 seed 理论上无效应；R2 认为 vLLM 的 floating-point non-associativity 可能导致实际存在 variation。**共识着陆点**：报告 temperature-stratified 分析，无需排除 seed facet。

**SF7 ("no universal recipe")**：R2 认为推荐差异小到不支持 "no universal recipe"；R1 认为 item budget 56% 差异是实质性的。**共识着陆点**：叙事需 recalibrate，但不应完全反转为 "recipe is largely stable"。

---

## Questions for Authors

1. 为什么引用 Jung et al. (2017) logistic-link generalized G-theory 但未使用？是否存在计算/工具限制？
2. Ordering facet 在 GSM8K/MATH 上的具体操作化是什么？是 few-shot demonstration 排列还是其他？
3. 如果将 model 视为 fixed facet，Table 1 的 variance decomposition 百分比如何变化？
4. Bernoulli p(1-p) correlation = 0.42（Section 5.7）——是否计算过 Bernoulli-adjusted variance decomposition 在不同 accuracy 水平 benchmarks 间的差异？
5. Cross-benchmark gradient 的 monotonicity 是否在 permutation test 下仍显著（5!=120 排列中 item_id 和 model×item 同时 monotonic 的概率）？

---

## Missing References

1. **教育测量 cross-test G-study 对比文献**（如 Briesch et al., 2014）——直接先驱，论文未讨论
2. **Benchmark contamination/saturation**（如 Jacovi et al., 2023; Oren et al., 2023）——影响 item_id variance 解释
3. **GLMM 在 NLP evaluation 中的应用**——与 binary data G-theory 方法论重叠，提供替代方案
4. **G-theory for binary data 的教育测量文献**——Shavelson et al. (1989) 已引用但未讨论具体结论

---

## External Review (Stanford Agentic Reviewer)

**状态**: 未请求。本轮未启用外部审稿。

---

## Visual Layout Check

**状态**: 未派发。本轮未启动视觉审查 Agent。

---

## Overall Assessment

**评分: Borderline (3.0)**
**置信度: High**

论文在实验规模、factorial 覆盖度和 robustness 分析体系上达到了高水准，cross-benchmark variance gradient 作为定性发现有真实的 empirical 和 practical 价值。但 3 个 converged critical issues 共同限制了评分上限：

1. **Binary data 方法论缺陷 (MF1)** 动摇了所有定量 variance decomposition 百分比的可信度——全部 primary findings 建立在可能有偏的估计之上。
2. **Model facet 不足 (MF2)** 使 model×item interaction 的 generalizability 受限——gradient 的定量精度对模型选择敏感。
3. **Scope overclaim (MF3)** 使 headline claims ("no universal recipe", "across benchmarks") 显著超出实验基础。

三个问题存在交叉放大效应：MF1 的 Bernoulli ceiling 与 MF3 的 scope 问题叠加（gradient 可能部分是 accuracy-dependent artifact）；MF2 的 model-as-fixed 与 MF3 的 scope 叠加（进一步缩小 generalizability）；MF2 与 SF8 叠加（弱化与 Mesting 的差异化）。

但所有问题均为 **fixable**——(a) logistic-link sensitivity check 或 logprob 提升为 primary 可解决 MF1；(b) model 重定位为 quasi-fixed + 补充 2-4 个模型可解决 MF2；(c) scope qualification + permutation test 可解决 MF3。若 revision 实质性处理这三个问题，论文可达 Weak Accept (3.5-4.0)。

---

## Detailed Comments

### Section 1 (Introduction)
- C3 (IRT vs G-theory comparison) 作为 primary contribution 期望过高，建议降级为 practical implication（SF6）

### Section 2 (Related Work)
- 与 Mesting (2026) 的差异化需更明确承认方法论增量性（SF8）
- 缺少教育测量 cross-test G-study、benchmark contamination、GLMM 文献（SF9）

### Section 3 (Background)
- 缺少 balanced vs unbalanced design 对 Henderson I 估计量影响的讨论
- "Standard G-theory assumes continuous responses" 不应仅在 Limitations 一句带过——这是核心方法论假设（MF1）

### Section 4 (Experimental Design)
- Ordering facet 在 GSM8K/MATH 上需明确操作定义（SF4）
- 需提供 design matrix 汇总表（SF3）

### Section 5.3 (Cross-benchmark Gradient)
- "Reasoning complexity" 排序需独立操作定义（SF2）
- Monotonicity 需 permutation test 支持（MF3）
- 应讨论 item_id 与 model×item 的机械负相关对 gradient 解读的影响（SF2）

### Section 5.5 (IRT vs G-theory)
- "At IRT's recommended 116 items, G-theory G = 0.529" 是有力论点，建议提前到 Section 5.3 或 Abstract 强调

### Section 5.6 (D-Study)
- 外推至 6.6× 需 progressive validation 或明确标注为 model-based extrapolation（SF1）

### Section 5.7 (Binary Data Validation)
- Null simulation 证明 signal 存在但未证明估计无偏（MF1）
- 需讨论 Bernoulli ceiling 在不同 accuracy benchmarks 上的 differential 影响（MF1）

### Section 5.8 (14B Extension)
- 2 个模型不足以论证 scale-invariance——Table 13 的 delta 在 2-model 设计下无统计意义（MF2）

### Section 6.2 (Fine-tuning)
- 超出核心 scope，建议压缩或删除（SF10）

### Section 6.3 (Practical Recommendations)
- "No universal recipe" 措辞需 recalibrate（SF7）

### Section 6.5 (Limitations)
- 应将 task type coverage 列为首要 limitation（MF3）
- Binary data 假设讨论过于轻描淡写（MF1）

### Table 1
- Residual+other 从 single-model 21.2% 降至 cross-model 11.5% 未解释去向，应交叉引用 Section 5.7 的 3-way interactions

### Table 6
- Caption 应注明使用 reduced design (2×2) 数据
- "trend" 列建议用 Spearman ρ + p-value 替代 ↓/↑ 标注
