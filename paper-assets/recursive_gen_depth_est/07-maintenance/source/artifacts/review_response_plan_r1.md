# Adversarial Review R1 Response Plan

> Review score: 5/10 (Borderline reject). DDL: EMNLP ARR May 25 (9 days remaining).

## Critical Issues

### C1: Ecological validity gap undermines practical framing
- **审稿原文摘要**: Benchmark uses Wikipedia+LoRA+BOS-seeded generation. Real-world involves full pretraining, prompt-conditioned generation, mixed-source corpora, unknown proportions. WikiText/C4 calibration only tests FPR on human text, never on realistically contaminated web text. Paper should reframe or provide realistic-pipeline experiment.
- **当前回应**: 
  - wild_data_calibration_005 (FineWeb FPR=15.3%) ✅ 已验证 human web text 上的 FPR
  - wild_data_calibration_003/004 (C4 FPR=20.2%, OpenWebText FPR=0.9-2.8%) ✅ 多数据源覆盖
  - 但这些只测 FPR（human text 被误分类率），**未测在真实递归污染文本上的 recall**
  - §4.5 Temperature Robustness 已新增
- **需要的行动**:
  1. **Writing 调整 (P0)**: 将 Introduction 和 Abstract 的 practical framing 降级为 "controlled proof-of-concept establishing the scientific foundation"。明确 scope 为 controlled setting，ecological transfer 列为 future work。引用 Reviewer 建议的 "realistic contamination simulation" 作为 future work 方向。
  2. **混合比例实验 (P1)**: 按审稿建议，在已有 d0/d1 数据上做 90%d0+10%d1 混合测试，验证 classifier 能否识别 contaminated fraction。**可用现有数据 zero-cost 实现**（无需新数据生成）。
  3. **FPR 叙事加强 (P0)**: 将现有 FineWeb/C4/OpenWebText FPR 结果包装为 "wild data calibration" subsection，明确说这验证了 type-I error 在可接受范围。
- **优先级**: P0 (writing) + P1 (mixing experiment)
- **预计耗时**: Writing 2h, mixing experiment 3h (利用已有特征数据)

### C2: Scale limitation threatens "universality" claim
- **审稿原文摘要**: Three models are all 1-1.5B. At this scale recursive finetuning induces rapid memorization. Modern 7B-70B+ generate more fluent text—tail features may be compressed below noise at scale. Need at least one 7B model result.
- **当前回应**: 
  - **cross_scale_qwen7b_001 ✅ DONE**: Qwen2.5-7B, 4-class acc=60.1%, 6-class acc=52.1%
  - Pairwise AUC: d0v1=0.921, d1v2=0.634, d2v3=0.683
  - Consecutive binary AUC: d0v1=0.969, d1v2=0.729, d2v3=0.709, d3v4=0.732, d4v5=0.772
  - **EDD estimate: >5** (all consecutive binary AUC > 0.70)
  - **直接回应**: 7B 模型 depth signal 依然存在且 EDD 更高（>5 vs 1.5B 模型 EDD=4）
- **需要的行动**:
  1. **Writing (P0)**: 将 Qwen 7B 结果写入 Section 5 或 Discussion 作为 cross-scale validation。强调：(a) depth signal 在 7B 依然存在 (acc=60.1% >> chance 25%)；(b) EDD>5 暗示更大模型的 depth boundary 更深，与 "tail features compressed below noise" 预测相反；(c) 但 d1v2 AUC (0.634) 低于 1.5B 模型 (0.86)，表明 adjacent depth separation 确实更难。
  2. **Framing (P0)**: 将 "universality" claim 修改为 "generality across 1B-7B scale"，明确不 claim 70B+。
- **优先级**: P0
- **预计耗时**: Writing 2h (实验已完成)

### C3: Cross-strategy transfer failure makes deployment infeasible
- **审稿原文摘要**: Headline 59.1% drops to 45.9% excluding d0. Temperature d1/d2 AUC inversion (0.13-0.25) means actively wrong rankings. Two-stage pipeline is hypothetical. System cannot be deployed on web text where strategy is unknown.
- **当前回应**:
  - **two_stage_strategy_pipeline_001 ✅ DONE**: Strategy classification mean acc=57.5% (chance 33.3%), depth estimation with predicted strategy=70.6% vs naive pooled=72.0% vs oracle=78.4%
  - lr_zscore_cross_strategy_001 ✅: Z-score normalization improves LR cross-strategy acc (25%→61%) but does not recover d1v2 AUC
  - cross_strategy_loo_001 ✅: Comprehensive LOO results with mechanistic explanation (temperature accelerates convergence)
  - §4.5 Temperature Robustness 已新增
  - Cross-strategy 已降级为 limitation in paper_framing
- **需要的行动**:
  1. **Writing (P0)**: 将 two_stage_strategy_pipeline_001 结果写入论文。关键数据点：
     - Strategy classification 57.5% >> chance (33.3%)，证明 strategy 可从文本识别
     - Oracle two-stage (78.4%) ≈ within-strategy (78.2%)，证明 upper bound 可达
     - Predicted two-stage (70.6%) vs cross-strategy LOO (59.1%) = **+11.5pp improvement**
     - 但 predicted two-stage (70.6%) < naive pooled (72.0%)，说明 strategy misclassification 有成本
  2. **Scope 调整 (P0)**: 明确写 "cross-strategy deployment requires further work; current best practical path is strategy-conditioned classifiers, which recover +11.5pp over strategy-agnostic transfer but do not fully close the gap to within-strategy performance."
  3. **不需要额外实验**: two_stage 实验已充分回应，关键是 writing 如何呈现。
- **优先级**: P0
- **预计耗时**: Writing 2h

## Major Issues

### M1: Headline accuracy inflation (d0 confound)
- **审稿原文摘要**: Abstract reports 70-85% but d0 is trivially separable (>98% recall). Meaningful performance is d1-d3: 58.8-82.6% in-distribution, 55.4% cross-model, 45.9% cross-strategy. Current framing overstates performance.
- **当前回应**: 
  - R3-W1 d0 inflation headline ✅ 已修改
  - d1-d3 accuracy 已作为 companion metric 报告 (Dream D002)
  - granularity_ablation_rf_001: 3-class (d1/d2/d3) mean acc = 72.1%
- **需要的行动**: 
  1. **Writing (P0)**: Abstract 和 Introduction 中首先报告 d1-d3 performance，4-class 作为 companion。改为："Feature-based classifiers achieve 72% three-class accuracy on the harder d1-d3 discrimination (chance=33%), and 70-85% four-class accuracy including the trivially separable d0 class."
- **优先级**: P0
- **预计耗时**: 30min (已有数据，仅需调整措辞)

### M2: Curation PoC does not support framing
- **审稿原文摘要**: Table 9 shows rf_soft vs unfiltered p=0.407. RF filtering does NOT improve over unfiltered. Only shows RF >> random (trivially true). Discussion overstates.
- **当前回应**:
  - downstream_curation_poc_001 ✅ 结果确认 negative (rf_soft vs unfiltered p=0.407)
  - rf_soft vs random_moderate is significant
- **需要的行动**:
  1. **Writing (P0)**: 诚实报告 PoC 结果。调整 Discussion 措辞为："Depth-based filtering provides informed data selection that significantly outperforms random subsampling (p<0.01), but does NOT demonstrate improvement over using all available data unfiltered (p=0.407). This suggests depth estimation's practical value may lie in efficiency (achieving comparable quality with less data) rather than quality improvement."
  2. **Scope 降级**: Claim 3 (curation implication) 明确标注为 "preliminary exploration" 而非 demonstrated application。
- **优先级**: P0
- **预计耗时**: 1h

### M3: EDD=4 claim requires qualification in abstract
- **审稿原文摘要**: Abstract states EDD_{0.75}=4 as general finding, but only 1/3 models statistically significant (Pythia p=0.001, OLMo p=0.091, GPT-2 XL p=0.505).
- **当前回应**:
  - D026/D027 决策 ✅：已降级为 "graded confidence" + 连续 AUC 衰减曲线叙事
  - Body text 已修改透明报告 CI 和 p-values
- **需要的行动**:
  1. **Writing (P0)**: 确保 Abstract 使用 D027 批准的措辞："d3v4 AUC consistently clusters near 0.75 (0.750–0.784) across all three models, while d4v5 uniformly falls below 0.70"。不写 "EDD=4" 作为硬结论。
  2. **Qwen 7B 补充**: cross_scale_qwen7b_001 显示 EDD>5（all consecutive AUC > 0.70），加强 "depth signal persists at scale" 叙事。
- **优先级**: P0
- **预计耗时**: 30min (已有决策，仅确保 abstract 一致)

### M4: Reference model information leak
- **审稿原文摘要**: All features computed via GPT-2 base (124M). When GPT-2 XL generates text, architectural overlap exists. Need sensitivity analysis with independent reference model (e.g., Llama-2-7B).
- **当前回应**: 
  - Paper notes GPT-2 XL holdout (67.6%) doesn't exceed OLMo (69.2%)
  - 但无独立 reference model 实验
- **需要的行动**:
  1. **Writing (P1)**: 加强现有论证——GPT-2 XL holdout ≤ OLMo holdout 表明 architectural overlap 未造成系统性 inflation。如果 overlap 有利，GPT-2 XL 应最高，但实际不是。
  2. **实验 (P2, 如果时间允许)**: 用 Qwen2.5-7B 或 Pythia-410M 作为 alternative reference model，在 1 个 setting 上验证。这是 "nice to have" 而非 must-have。
  3. **Limitation (P0)**: Discussion 中添加 caveat: "We use GPT-2 base as reference model throughout; while cross-model LOO results suggest no systematic bias from architectural overlap, validation with a completely independent reference model family remains as future work."
- **优先级**: P1 (writing) + P2 (experiment, optional)
- **预计耗时**: Writing 30min; experiment 4h if pursued

### M5: Feature collinearity inflates complexity
- **审稿原文摘要**: VIF>10 for 14-16 of 19 features, effective dimensionality ~4-5. Paper frames as "19 candidate features" but ~4 independent features do the work.
- **当前回应**:
  - feature_ablation_9cell ✅: Feature ablation 完成
  - SHAP analysis 显示 top-4 features 跨 9 cells 一致
  - Paper already reports VIF and collinearity
- **需要的行动**:
  1. **Writing (P0)**: 在 feature description section 前置 effective dimensionality 信息："While we explore 19 candidate features, VIF analysis reveals effective dimensionality of ~4-5 (VIF>10 for 14-16 features). The key independent signal families are: (1) perplexity tail (p90_ppl), (2) surprisal variance, (3) vocabulary diversity (distinct_ratio), (4) repetition structure (rep_frac)."
  2. **不需要额外实验**: 数据已有，纯 writing 调整。
- **优先级**: P0
- **预计耗时**: 1h

## Minor Issues

### m1: Zero-shot LLM baselines are under-explored
- **审稿原文摘要**: n=500 zero-shot is weak. No CoT, no few-shot, no SOTA reasoning models. Feels designed to fail.
- **当前回应**:
  - zeroshot_llm_500_001 ✅: DeepSeek-v3.2 acc=36.2%
  - zeroshot_qwen7b_500_001 ✅: Qwen2.5-7B-Instruct acc=30.4%
  - §4 已写入 n=500 充分性论证 (42pp gap >> CI 4pp)
- **需要的行动**:
  1. **Writing (P1)**: 添加 caveat: "We use zero-shot prompting to establish a lower bound; few-shot or chain-of-thought prompting could narrow the gap, though the 42pp deficit suggests fundamental task difficulty for LLMs without explicit statistical computation." 
  2. **不做 few-shot 实验**: GPT-4/Claude API costs + time constraint。gap 足够大 (42pp) 使得即使 few-shot 提升 10-15pp 仍远低于 RF。
- **优先级**: P1
- **预计耗时**: 30min (writing only)

### m2: No instruction-tuned generators tested
- **审稿原文摘要**: All three base models. Instruction-tuned models dominate real-world generation and may produce different signatures.
- **当前回应**: 无直接回应。Qwen2.5-7B 在 cross_scale 实验中用的是 base model。
- **需要的行动**:
  1. **Writing (P1)**: Limitations section 添加: "Our generators are all base models with LoRA finetuning on domain data; instruction-tuned models generating in response to prompts may exhibit different statistical signatures and represent an important direction for future work."
  2. **不做新实验**: 需要完整 recursive chain 生成 pipeline（instruction-tuned model + prompt-conditioned generation），时间不允许。
- **优先级**: P1
- **预计耗时**: 15min (limitation caveat)

### m3: Fixed passage length (512 tokens) unrealistic
- **审稿原文摘要**: Real text varies in length. How sensitive are tail statistics to passage length? No sensitivity analysis at 128/256/1024.
- **当前回应**: 无直接回应。
- **需要的行动**:
  1. **实验 (P2)**: Passage length sensitivity analysis 在现有数据上 truncating to 128/256 tokens 并 re-computing features。Zero-cost (无需新生成)，仅需 feature re-extraction + classification。
  2. **Writing (P1)**: 如果时间不够做实验，在 Limitations 中 acknowledge: "We fix passage length at 512 tokens; shorter passages may reduce tail statistic reliability."
- **优先级**: P2 (experiment) / P1 (writing fallback)
- **预计耗时**: Experiment 4h, writing 15min

### m4: Discussion section overstuffed
- **审稿原文摘要**: Mixed-depth documents, adversarial robustness, scaling predictions each get 1-2 paragraphs of pure speculation. Reads like "future work laundry list."
- **当前回应**: R3-W2 Discussion 扩展已处理
- **需要的行动**:
  1. **Writing (P1)**: 将投机性段落移至 Appendix "Extended Discussion"。主 Discussion 保留：(a) cross-strategy findings 的 mechanism, (b) scaling implications (现在有 7B 数据支持), (c) 1-2 句 future work 概述。
- **优先级**: P1
- **预计耗时**: 1h

### m5: "Depth Degradation Atlas" branding oversells
- **审稿原文摘要**: Atlas is essentially tables and feature rankings. "Atlas" creates expectations of richer cartographic metaphors.
- **当前回应**: 无直接修改
- **需要的行动**:
  1. **Figure (P0)**: 确保 Atlas heatmap figure (Dream D002 要求) 足够 "cartographic"——使用 feature×depth×model 热力图让 "Atlas" 名称实至名归。
  2. **Writing (P1)**: 首次使用时简短解释 "Atlas" 隐喻的含义："We term this systematic map of feature trajectories across depth, model, and strategy dimensions the Depth Degradation Atlas."
- **优先级**: P1
- **预计耗时**: 30min (writing) + figure work (already in pipeline)

### m6: Decision boundary dilution is well-known
- **审稿原文摘要**: Binary pair classifiers outperforming multi-class is well-known in ordinal classification literature. Presenting as finding rather than methodological choice misrepresents novelty.
- **当前回应**: 无直接修改
- **需要的行动**:
  1. **Writing (P1)**: 引用 ordinal classification 文献 (Frank & Hall 2001, Cardoso & da Costa 2007) 并 reframe: "Consistent with ordinal classification theory (Frank & Hall, 2001), binary pairwise classifiers outperform multi-class formulation on per-pair metrics. We report pairwise AUC as the more informative metric for depth separation." 不作为 finding，作为 methodological justification。
- **优先级**: P1
- **预计耗时**: 30min

## 优先级排序总结

### P0 — Must do before submission (Days 1-4)
| # | 行动 | 类型 | 耗时 | 回应的 Issue |
|---|------|------|------|-------------|
| 1 | Reframe scope (controlled PoC, not deployment-ready) | Writing | 2h | C1, C3, M2 |
| 2 | Write up Qwen 7B cross-scale results | Writing | 2h | C2 |
| 3 | Write up two-stage pipeline results | Writing | 2h | C3 |
| 4 | Fix headline metrics (d1-d3 first, 4-class companion) | Writing | 30min | M1 |
| 5 | EDD abstract qualification | Writing | 30min | M3 |
| 6 | Feature collinearity reframing | Writing | 1h | M5 |
| 7 | Curation PoC honest reporting | Writing | 1h | M2 |

**Total P0 writing: ~9h**

### P1 — Should do if time allows (Days 4-7)
| # | 行动 | 类型 | 耗时 | 回应的 Issue |
|---|------|------|------|-------------|
| 8 | Mixing experiment (90%d0 + 10%d1 contamination) | Experiment | 3h | C1 |
| 9 | Reference model limitation caveat | Writing | 30min | M4 |
| 10 | LLM baseline caveat + instruction-tuned limitation | Writing | 45min | m1, m2 |
| 11 | Discussion trim (move speculation to appendix) | Writing | 1h | m4 |
| 12 | Atlas naming justification + ordinal classification refs | Writing | 1h | m5, m6 |
| 13 | Passage length limitation note | Writing | 15min | m3 |

**Total P1: ~6.5h**

### P2 — Nice-to-have (Days 7-9, if surplus time)
| # | 行动 | 类型 | 耗时 | 回应的 Issue |
|---|------|------|------|-------------|
| 14 | Passage length sensitivity experiment (128/256/512/1024) | Experiment | 4h | m3 |
| 15 | Alternative reference model experiment (1 setting) | Experiment | 4h | M4 |

**Total P2: ~8h**

## 关键判断

1. **不做的事**:
   - 不做 few-shot LLM baseline (gap 已足够大)
   - 不做 instruction-tuned generator 全 chain (时间不够)
   - 不做 full realistic contamination simulation (需要 pre-training, 超出 scope)
   - cross_scale_llama3_8b_001 失败不重试 (Qwen 7B 已成功回应 C2)

2. **审稿的核心攻击面是 framing 而非 results**: 审稿承认方法论严谨 (Strengths 2-4)，主要攻击 practical claims 和 generality claims 超出实验支持范围。**回应策略以 writing scope 调整为主，而非补实验。**

3. **Qwen 7B 结果是最大的反击武器**: EDD>5 + acc=60.1%>>chance 直接反驳 "tail features compressed at scale" 的预测，甚至比 reviewer 预期更好。

4. **Two-stage pipeline 虽然不完美 (+11.5pp) 但证明了方向**: 从 "entirely hypothetical" 升级为 "empirically validated direction with known bottleneck (strategy classification accuracy)"。

5. **Curation PoC 需要诚实面对**: 不要试图 spin negative result。诚实报告 + 降低 claim strength 比强行辩护更得分。
