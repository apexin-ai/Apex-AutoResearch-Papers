# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：bias 放大效应存在但幅度中等，需更多 expert labels 才稳定；仅有合成+半合成验证；PPCI 区分度存在但不悬殊 核心假设：['gl

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 18
- **Recorded user turns:** 1
- **Tool calls:** 2
- **Original source:** `logs/chats/exported-trajectories/account-3/4e19aba4-a633-4d8d-a9a7-f416f6782e3a.jsonl`
- **Structured JSON:** [`89f20e6419b36df13255.json`](../../sessions/89/89f20e6419b36df13255.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:00:23.059Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:00:23.059Z",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：bias 放大效应存在但幅度中等，需更多 expert labels 才稳定；仅有合成+半合成验证；PPCI 区分度存在但不悬殊\n核心假设：['global correction bias 放大在 moderate heterogeneity 下可复现，但倍数不如极端设定 dramatic', 'HB partial pooling 优于 MLE 的优势仅在 n_expert<500 时显著，大样本下差异收敛', 'diagnostic criterion 有效但阈值需要 per-dataset 校准，不能直接 transfer', 'semi-synthetic LLM 自然 heterogeneity 存在但偏温和，需选择特定 subgroup 定义才能放大效应', 'Ashwin 数据不可用，无 real-data 实验']\n关键指标范围：{'bias_amplification_factor_global_vs_uncorrected': [2.0, 5.0], 'ec_hte_absolute_cate_bias': [0.02, 0.05], 'ec_hte_coverage_90ci': [0.85, 0.92], 'min_n_expert_for_dominance': [250, 500], 'diagnostic_criterion_auroc': [0.78, 0.9], 'hb_vs_stratified_mle_bias_reduction': [0.1, 0.3], 'ec_hte_vs_ppci_bias_ratio': [0.4, 0.7]}\n叙事方向：需要调整 claims 强度。Claim 1 从 \"debiasing can hurt 5-10x\" 软化为 \"debiasing can hurt, 且 hurt 的程度随 heterogeneity product 单调增长\"——强调 mechanism 的 monotonic relationship 而非绝对倍数。Claim 2 中 \"250 expert labels\" 上调为 \"500\"，partial pooling 的叙事从 \"dramatically better\" 转为 \"principled regularization with guaranteed non-inferiority\"。 Claim 3 的 diagnostic 从 \"computable threshold\" 弱化为 \"computable risk score + decision heuristic\"。无 real data 需在 limitation 中正面处理，并在 semi-synthetic 设计上加强 ecological validity 论证（real corpus, real LLM errors, only treatment effect is synthetic）。 仍可投 EMNLP main，但需补充：(a) 更细粒度的 sensitivity analysis 替代 dramatic headline number, (b) partial pooling 的理论 shrinkage 分析（bias-variance tradeoff 可视化）。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nfocus: 核心关注：(1) \"debiasing can hurt\" 的 surprise value 是否足够撑起 EMNLP main；(2) 层级贝叶斯 partial pooling 作为方法核心是否有足够技术贡献；(3) 仅有合成+半合成实验时论文是否可接受（Ashwin 数据集可能拿不到）；(4) 与 PPCI (Sui 2026) 的差异化是否清晰\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 5-10x compared to no correction at all.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. EC-HTE achieves near-oracle CATE accuracy (|bias| < 0.02) and valid coverage (≥90%) across both high- and low-error subgroups, with expert label budgets as small as 250.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., \"tweet contains economic framing\" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration.\n\n- **Headline result template**: \"On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n## Key Contributions (ordered for paper)\n\n1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes \"debiasing can hurt\" proposition with constructive example. (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI (Sui et al., 2026)?\"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Semi-synthetic benchmark: use real political-science tweet corpus\n    (e.g., CardiffNLP TweetEval or similar public dataset), inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 and Qwen3-235B-A22B, measure subgroup-specific\n    misclassification rates, apply EC-HTE vs baselines. Primary empirical evidence\n    for all claims.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  description: 'Real-data validation on Ashwin et al. (2025) Rohingya refugee interview\n    dataset: LLM annotation errors correlate with refugee status, gender, education.\n    Apply EC-HTE to recover corrected CATEs. Requires dataset access.'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference)\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: Dataset access — need to check if publicly available or request from authors\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1\n  description: 'PPCI (Sui et al., 2026) baseline comparison: implement PPCI kernel-based\n    conditional correction and compare against EC-HTE on same benchmarks. Key differentiation\n    experiment.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 12h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest leaf-level analysis: integrate EC-HTE correction into\n    CausalForestDML at the leaf level (corrected pseudo-outcomes + variance-adjusted\n    CIs), compare against naive forest.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:00:23.063Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:00:23.063Z",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---

## Round 1

16 recorded events

### User

_source line 3 · 2026-05-20T19:00:23.085Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：bias 放大效应存在但幅度中等，需更多 expert labels 才稳定；仅有合成+半合成验证；PPCI 区分度存在但不悬殊
核心假设：['global correction bias 放大在 moderate heterogeneity 下可复现，但倍数不如极端设定 dramatic', 'HB partial pooling 优于 MLE 的优势仅在 n_expert<500 时显著，大样本下差异收敛', 'diagnostic criterion 有效但阈值需要 per-dataset 校准，不能直接 transfer', 'semi-synthetic LLM 自然 heterogeneity 存在但偏温和，需选择特定 subgroup 定义才能放大效应', 'Ashwin 数据不可用，无 real-data 实验']
关键指标范围：{'bias_amplification_factor_global_vs_uncorrected': [2.0, 5.0], 'ec_hte_absolute_cate_bias': [0.02, 0.05], 'ec_hte_coverage_90ci': [0.85, 0.92], 'min_n_expert_for_dominance': [250, 500], 'diagnostic_criterion_auroc': [0.78, 0.9], 'hb_vs_stratified_mle_bias_reduction': [0.1, 0.3], 'ec_hte_vs_ppci_bias_ratio': [0.4, 0.7]}
叙事方向：需要调整 claims 强度。Claim 1 从 "debiasing can hurt 5-10x" 软化为 "debiasing can hurt, 且 hurt 的程度随 heterogeneity product 单调增长"——强调 mechanism 的 monotonic relationship 而非绝对倍数。Claim 2 中 "250 expert labels" 上调为 "500"，partial pooling 的叙事从 "dramatically better" 转为 "principled regularization with guaranteed non-inferiority"。 Claim 3 的 diagnostic 从 "computable threshold" 弱化为 "computable risk score + decision heuristic"。无 real data 需在 limitation 中正面处理，并在 semi-synthetic 设计上加强 ecological validity 论证（real corpus, real LLM errors, only treatment effect is synthetic）。 仍可投 EMNLP main，但需补充：(a) 更细粒度的 sensitivity analysis 替代 dramatic headline number, (b) partial pooling 的理论 shrinkage 分析（bias-variance tradeoff 可视化）。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: ec_hte_llm_annotation
focus: 核心关注：(1) "debiasing can hurt" 的 surprise value 是否足够撑起 EMNLP main；(2) 层级贝叶斯 partial pooling 作为方法核心是否有足够技术贡献；(3) 仅有合成+半合成实验时论文是否可接受（Ashwin 数据集可能拿不到）；(4) 与 PPCI (Sui 2026) 的差异化是否清晰

## paper_framing.md

# Paper Framing — ec_hte_llm_annotation

## Target Venue
- Primary: EMNLP 2026 Main (via ARR)
- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026
- Format: Long paper, 8 pages + unlimited references

## Core Claims (3 条，可证伪)

1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this "debiasing" can worsen CATE bias by 5-10x compared to no correction at all.

2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. EC-HTE achieves near-oracle CATE accuracy (|bias| < 0.02) and valid coverage (≥90%) across both high- and low-error subgroups, with expert label budgets as small as 250.

3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.

## Story Spine

- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., "tweet contains economic framing" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.

- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**

- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration.

- **Headline result template**: "On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels."

## Key Contributions (ordered for paper)

1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes "debiasing can hurt" proposition with constructive example. (Theory + Empirical)
2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)
3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)
4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)

## Anticipated Reviewer Concerns

1. **"Why not just use expert labels directly for CATE?"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.

2. **"How is this different from PPCI (Sui et al., 2026)?"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.

3. **"Incremental over Mozer (2026)"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.

4. **"How sensitive to subgroup definition?"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.

5. **"Real-world expert label cost"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).

## Venue Fit

EMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.

Risk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.


## experiment_plan (with registry status)

- id: exp-001
  claim: 2
  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior
    confusion matrix estimator with partial pooling, compare against MLE/Laplace on
    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).
    Primary validation of Claim 2.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU (PyMC + econml)
  estimated_time: 12-24h (coding + 1000 MC runs)
  deps: []
  status: planned
- id: exp-002
  claim: 1
  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,
    CATE_heterogeneity) analytically, then verify empirically across systematic parameter
    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup
    example.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 8-12h
  deps: []
  status: planned
- id: exp-003
  claim:
  - 1
  - 2
  - 3
  description: 'Semi-synthetic benchmark: use real political-science tweet corpus
    (e.g., CardiffNLP TweetEval or similar public dataset), inject known CATE heterogeneity
    structure, annotate with GPT-4.1 and Qwen3-235B-A22B, measure subgroup-specific
    misclassification rates, apply EC-HTE vs baselines. Primary empirical evidence
    for all claims.'
  priority: P0
  gpu_budget_hours: 20
  compute: GPU (LLM inference for annotation)
  estimated_time: 24-36h
  deps:
  - exp-001
  status: planned
- id: exp-004
  claim:
  - 1
  - 2
  description: 'Real-data validation on Ashwin et al. (2025) Rohingya refugee interview
    dataset: LLM annotation errors correlate with refugee status, gender, education.
    Apply EC-HTE to recover corrected CATEs. Requires dataset access.'
  priority: P0
  gpu_budget_hours: 10
  compute: GPU (LLM inference)
  estimated_time: 24h
  deps:
  - exp-001
  status: planned
  risk: Dataset access — need to check if publicly available or request from authors
- id: exp-005
  claim: 3
  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×
    CATE_heterogeneity product from pilot data across all experimental settings, show
    it predicts when global correction fails. ROC analysis of threshold.'
  priority: P0
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 4-8h
  deps:
  - exp-001
  - exp-003
  status: planned
- id: exp-006
  claim: 2
  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,
    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where
    EC-HTE > Global. Validate HB partial pooling value at small n.'
  priority: P1
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 8h
  deps:
  - exp-001
  status: planned
- id: exp-007
  claim: 1
  description: 'PPCI (Sui et al., 2026) baseline comparison: implement PPCI kernel-based
    conditional correction and compare against EC-HTE on same benchmarks. Key differentiation
    experiment.'
  priority: P1
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 12h
  deps:
  - exp-001
  - exp-003
  status: planned
- id: exp-008
  claim: 2
  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude
    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit
    varies by LLM quality.'
  priority: P1
  gpu_budget_hours: 15
  compute: GPU
  estimated_time: 12h
  deps:
  - exp-003
  status: planned
- id: exp-009
  claim: 2
  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted
    allocation targeting high-CATE × high-error subgroups, compare against uniform
    and uncertainty-only allocation.'
  priority: P2
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 16h
  deps:
  - exp-001
  - exp-006
  status: planned
- id: exp-010
  claim: 2
  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups
    are noisy/overlapping or when the true subgroup structure doesn''t align with
    the conditioning variable.'
  priority: P2
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 8h
  deps:
  - exp-001
  status: planned
- id: exp-011
  claim: 2
  description: 'Causal forest leaf-level analysis: integrate EC-HTE correction into
    CausalForestDML at the leaf level (corrected pseudo-outcomes + variance-adjusted
    CIs), compare against naive forest.'
  priority: P2
  gpu_budget_hours: 0
  compute: CPU
  estimated_time: 16h
  deps:
  - exp-001
  status: planned

# 输出格式（YAML，仅输出一个 ```yaml 块）

```yaml
tier: median
narrative_guidance: "..."
imagined_experiments:
  - name: "..."
    plan_id: "..."
    description: "..."
    expected_results: {metric: value, ...}
    result_rationale: "..."
    tables: []
    figures_description: []
    analysis: "..."
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "6b523d89-d9ab-4383-a424-1df7e82983c6",
  "type": "user",
  "uuid": "4908e34a-b25b-45bb-a483-6235641676b0",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:00:23.084Z_

```json
{
  "parentUuid": "4908e34a-b25b-45bb-a483-6235641676b0",
  "isSidechain": false,
  "attachment": {
    "type": "deferred_tools_delta",
    "addedNames": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "addedLines": [
      "AskUserQuestion",
      "CronCreate",
      "CronDelete",
      "CronList",
      "EnterPlanMode",
      "EnterWorktree",
      "ExitPlanMode",
      "ExitWorktree",
      "Monitor",
      "NotebookEdit",
      "PushNotification",
      "RemoteTrigger",
      "TaskOutput",
      "TaskStop",
      "TodoWrite",
      "WebFetch",
      "WebSearch"
    ],
    "removedNames": []
  },
  "type": "attachment",
  "uuid": "f8b28c9c-b3f1-4653-8c27-19ccc8f274b5",
  "timestamp": "2026-05-20T19:00:23.084Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:00:23.084Z_

```json
{
  "parentUuid": "f8b28c9c-b3f1-4653-8c27-19ccc8f274b5",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0837c6f7-1f90-4ab1-bf11-0c92ec65ed80",
  "timestamp": "2026-05-20T19:00:23.084Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE: Subgroup-stratified LLM misclassification correction",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---

### Tool call

_source line 7 · 2026-05-20T19:00:27.461Z_

<details open><summary>🔧 Tool call — Read · `toolu_011ToqoZzqLa8cRYht4UoTwf`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520/.claude/CLAUDE.md"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0837c6f7-1f90-4ab1-bf11-0c92ec65ed80",
  "isSidechain": false,
  "requestId": "req_011CbELTCcE7DMDMJTsTdj6t",
  "type": "assistant",
  "uuid": "1bfd0d23-c51a-4ca8-8cf3-85af203fae63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFXwNk8tMZYHzDu8HsUzwM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9384,
      "cache_read_input_tokens": 11841,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9384,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 147,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9384
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 8 · 2026-05-20T19:00:27.480Z_

<details><summary>↩ Tool result · `toolu_011ToqoZzqLa8cRYht4UoTwf`</summary>

```text
1	
2	## 输出风格
3	
4	- 回复简洁直接，不说废话
5	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
6	- 不要复述用户的问题
7	- 不要给未被要求的建议或补充说明
8	- 推理要彻底，但输出只保留结论和必要信息
9	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "1bfd0d23-c51a-4ca8-8cf3-85af203fae63",
  "isSidechain": false,
  "promptId": "6b523d89-d9ab-4383-a424-1df7e82983c6",
  "type": "user",
  "uuid": "4bdc6c90-9d58-4f06-b3b9-264676860c3a",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 1,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "1bfd0d23-c51a-4ca8-8cf3-85af203fae63",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Tool call

_source line 9 · 2026-05-20T19:00:27.761Z_

<details open><summary>🔧 Tool call — Glob · `toolu_012Tpj7KudL1yNgj3g9B6jQ4`</summary>

```json
{
  "pattern": "**/*.md",
  "path": "/home/ubuntu/.agent-ml-research-idea_gen_0520"
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4bdc6c90-9d58-4f06-b3b9-264676860c3a",
  "isSidechain": false,
  "requestId": "req_011CbELTCcE7DMDMJTsTdj6t",
  "type": "assistant",
  "uuid": "06430ce0-3239-49a4-905c-19579ffe3f85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01JFXwNk8tMZYHzDu8HsUzwM",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9384,
      "cache_read_input_tokens": 11841,
      "output_tokens": 147,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9384,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 147,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9384,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9384
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Tool result

_source line 10 · 2026-05-20T19:00:27.772Z_

<details><summary>↩ Tool result · `toolu_012Tpj7KudL1yNgj3g9B6jQ4`</summary>

```text
projects/ec_hte_llm_annotation/.claude/sessions/agent_a6149ddb/CLAUDE.md
projects/ec_hte_llm_annotation/.claude/sessions/agent_a6149ddb/AGENTS.md
projects/ec_hte_llm_annotation/docs/IDEA_BRIEF.md
projects/ec_hte_llm_annotation/ROADMAP.md
projects/ec_hte_llm_annotation/.claude/sessions/reviewer_4d5fd1e4/CLAUDE.md
projects/ec_hte_llm_annotation/.claude/sessions/reviewer_4d5fd1e4/AGENTS.md
.claude/CLAUDE.md
AGENTS.md
projects/ec_hte_llm_annotation/.claude/CLAUDE.md
projects/ec_hte_llm_annotation/AGENTS.md
projects/ec_hte_llm_annotation/.claude/sessions/director_f2a3b60e/CLAUDE.md
projects/ec_hte_llm_annotation/.claude/sessions/director_f2a3b60e/AGENTS.md
projects/ec_hte_llm_annotation/paper_framing.md
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "06430ce0-3239-49a4-905c-19579ffe3f85",
  "isSidechain": false,
  "promptId": "6b523d89-d9ab-4383-a424-1df7e82983c6",
  "type": "user",
  "uuid": "6c232e43-dd31-4ce8-b128-c723c6c019ca",
  "toolUseResult": {
    "filenames": [
      "projects/ec_hte_llm_annotation/.claude/sessions/agent_a6149ddb/CLAUDE.md",
      "projects/ec_hte_llm_annotation/.claude/sessions/agent_a6149ddb/AGENTS.md",
      "projects/ec_hte_llm_annotation/docs/IDEA_BRIEF.md",
      "projects/ec_hte_llm_annotation/ROADMAP.md",
      "projects/ec_hte_llm_annotation/.claude/sessions/reviewer_4d5fd1e4/CLAUDE.md",
      "projects/ec_hte_llm_annotation/.claude/sessions/reviewer_4d5fd1e4/AGENTS.md",
      ".claude/CLAUDE.md",
      "AGENTS.md",
      "projects/ec_hte_llm_annotation/.claude/CLAUDE.md",
      "projects/ec_hte_llm_annotation/AGENTS.md",
      "projects/ec_hte_llm_annotation/.claude/sessions/director_f2a3b60e/CLAUDE.md",
      "projects/ec_hte_llm_annotation/.claude/sessions/director_f2a3b60e/AGENTS.md",
      "projects/ec_hte_llm_annotation/paper_framing.md"
    ],
    "durationMs": 6,
    "numFiles": 13,
    "truncated": false
  },
  "sourceToolAssistantUUID": "06430ce0-3239-49a4-905c-19579ffe3f85",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：bias 放大效应存在但幅度中等，需更多 expert labels 才稳定；仅有合成+半合成验证；PPCI 区分度存在但不悬殊 核心假设：['global correction bias 放大在 moderate heterogeneity 下可复现，但倍数不如极端设定 dramatic', 'HB p…",
  "leafUuid": "6c232e43-dd31-4ce8-b128-c723c6c019ca",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE: Subgroup-stratified LLM misclassification correction",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---

### Assistant

_source line 13 · 2026-05-20T19:00:30.449Z_

<details><summary>Logged reasoning block</summary>

```text
Let me look at the existing project files to understand the full context before generating the detailed experiment predictions.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "6c232e43-dd31-4ce8-b128-c723c6c019ca",
  "isSidechain": false,
  "requestId": "req_011CbELTYM8MjTskhiSjUd7n",
  "type": "assistant",
  "uuid": "84990687-d24a-4354-888f-9456a01aa0fd",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tw367PBvLk3CrBD2coDmVy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 21225,
      "output_tokens": 13292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13292,
          "cache_read_input_tokens": 21225,
          "cache_creation_input_tokens": 657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Assistant

_source line 14 · 2026-05-20T19:04:25.461Z_

```yaml
tier: median
narrative_guidance: >
  Claims 需全面软化。Claim 1 从 "debiasing can hurt 5-10x" 转为 "debiasing can hurt, 且 hurt 程度与 heterogeneity product 单调递增"——强调 mechanism 而非极端倍数。
  Claim 2 的 expert budget 从 250 上调至 500，partial pooling 叙事从 "dramatically better" 转为 "principled regularization with guaranteed non-inferiority"。
  Claim 3 的 diagnostic 从 "computable threshold" 弱化为 "computable risk score + decision heuristic"，承认阈值需 per-dataset 校准。
  无 real data (exp-004 不可用) 需在 limitation 正面处理，semi-synthetic 设计需加强 ecological validity 论证（real corpus, real LLM errors, only treatment effect is synthetic）。
  补充细粒度 sensitivity analysis 替代 headline number，加入 shrinkage bias-variance tradeoff 可视化。仍可投 EMNLP main。

imagined_experiments:
  - name: "HB EC-HTE Synthetic Validation"
    plan_id: "exp-001"
    description: >
      在合成数据上实现 HB Dirichlet-prior confusion matrix estimator with partial pooling，
      与 MLE/Laplace 基线对比。扫描 extreme/moderate/homogeneous heterogeneity × n_expert {100,250,500,1000,2000} × k∈{2,4} subgroups，
      共 1000 MC runs per cell。
    expected_results:
      ec_hte_absolute_cate_bias_moderate: 0.035
      ec_hte_absolute_cate_bias_extreme: 0.028
      ec_hte_absolute_cate_bias_homogeneous: 0.015
      ec_hte_coverage_90ci_moderate: 0.88
      ec_hte_coverage_90ci_extreme: 0.86
      ec_hte_coverage_90ci_homogeneous: 0.93
      hb_vs_stratified_mle_bias_reduction_n100: 0.28
      hb_vs_stratified_mle_bias_reduction_n250: 0.22
      hb_vs_stratified_mle_bias_reduction_n500: 0.15
      hb_vs_stratified_mle_bias_reduction_n1000: 0.08
      hb_vs_stratified_mle_bias_reduction_n2000: 0.04
      min_n_expert_for_hb_dominance_k2: 300
      min_n_expert_for_hb_dominance_k4: 450
    result_rationale: >
      Median 档下，moderate heterogeneity 意味着 subgroup 间 misclassification rate 差异约 0.08-0.15（非极端的 0.2+），
      CATE 差异约 0.05-0.10。HB partial pooling 的优势来源于 shrinkage：当 n_expert per subgroup 较小时（<125/subgroup for k=4），
      MLE 方差大导致 confusion matrix 估计不稳定，HB 通过向 global prior 收缩获得 ~20-28% bias reduction。
      但随着 n_expert 增长至 500+，MLE 本身已足够稳定，shrinkage 的边际收益递减至 <10%，两者收敛。
      Coverage 在 moderate 设定下略低于 90% 标称值（~88%），因为 moderate heterogeneity 使得部分 subgroup 的 posterior 
      对 prior specification 敏感，需要更多数据才能完全覆盖。k=4 比 k=2 需要更多 expert labels 才能 dominate，
      因为每个 subgroup 分到的样本量更少，MLE 更不稳定但 HB 的 pooling 结构也更复杂。
    tables:
      - name: "Table 1: EC-HTE vs MLE vs Laplace — Synthetic Bias & Coverage"
        columns: ["Method", "Heterogeneity", "n_expert", "k", "|CATE Bias|", "90% Coverage", "RMSE"]
        key_rows:
          - ["EC-HTE (HB)", "moderate", 250, 2, 0.038, 0.87, 0.061]
          - ["EC-HTE (HB)", "moderate", 500, 2, 0.031, 0.89, 0.048]
          - ["EC-HTE (HB)", "moderate", 250, 4, 0.042, 0.85, 0.073]
          - ["EC-HTE (HB)", "moderate", 500, 4, 0.035, 0.88, 0.058]
          - ["Stratified MLE", "moderate", 250, 2, 0.049, 0.82, 0.078]
          - ["Stratified MLE", "moderate", 500, 2, 0.036, 0.87, 0.053]
          - ["Stratified MLE", "moderate", 250, 4, 0.058, 0.76, 0.095]
          - ["Stratified MLE", "moderate", 500, 4, 0.041, 0.84, 0.065]
          - ["Laplace-smoothed", "moderate", 250, 2, 0.044, 0.84, 0.070]
          - ["Laplace-smoothed", "moderate", 500, 2, 0.034, 0.88, 0.051]
          - ["Global correction", "moderate", 500, 2, 0.112, 0.63, 0.135]
          - ["No correction", "moderate", 500, 2, 0.045, 0.81, 0.068]
    figures_description:
      - "Figure: Shrinkage bias-variance tradeoff 可视化 — x 轴 n_expert，y 轴 split 为 bias² 和 variance 两条线，展示 HB 在小样本处 variance 显著低于 MLE，bias 略高（shrinkage cost），但 MSE = bias² + var 在 n<500 时 HB 始终优于 MLE，n>500 后两者重叠"
      - "Figure: Posterior shrinkage 系数 vs n_expert — 展示 HB 在 n=100 时 shrinkage ~0.6（强烈向 global pooling），n=500 时 shrinkage ~0.15（几乎完全 stratified）"
    analysis: >
      核心发现：HB partial pooling 在 n_expert<500 时提供 principled regularization，非 dramatically better 但 guaranteed non-inferior。
      叙事应强调 shrinkage 的 adaptive 特性：数据少时自动保守（向 global 收缩），数据多时自动放手（接近 stratified MLE）。
      k=4 subgroups 是论文的 realistic sweet spot——足够展示 heterogeneity 但不会因 subgroup 过多导致每组样本量不足。
      Limitation：Dirichlet prior 的超参数选择对 n<200 的结果有 ~5-10% 影响，需报告 sensitivity。

  - name: "Bias Bound Formal Verification"
    plan_id: "exp-002"
    description: >
      解析推导 bias = f(Δπ, Δτ) 的 closed-form（两个 subgroup 情形），
      然后在系统化参数网格上（Δπ ∈ [0,0.3], Δτ ∈ [0,0.2], step=0.02）empirically 验证。
      生成 "debiasing can hurt" 的 constructive example。
    expected_results:
      bias_amplification_factor_moderate_heterogeneity: 3.2
      bias_amplification_factor_high_heterogeneity: 4.8
      bias_amplification_factor_extreme_heterogeneity: 7.5
      bias_monotonic_in_product: true
      analytic_vs_empirical_correlation: 0.97
      constructive_example_bias_ratio: 3.5
    result_rationale: >
      Median 档下关注 moderate heterogeneity 区间（Δπ~0.10, Δτ~0.08），此时 global correction 的 bias amplification factor 约 2-5x。
      机制：global confusion matrix 是各 subgroup 的加权平均，当 subgroup A 的 error rate 低于 global average 时，
      global correction 会"过度矫正" A（减去了本不属于 A 的噪声），反之 subgroup B 被"欠矫正"。
      Bias 与 Δπ×Δτ 的 product 呈 monotonic 关系源于 Taylor 展开的一阶项主导：bias ≈ Δπ·Δτ·f(base rates)。
      在 moderate 设定下这个 product 不够大，所以 amplification 在 3-5x 范围而非 7-10x。
      但 monotonicity 是 robust 的——这比极端倍数更有 generalizability，适合作为 paper 的核心 narrative。
      Analytic 与 empirical 高度一致（r≈0.97）因为两个 subgroup 情形的 closed-form 是 exact 的，偏差仅来自 MC 采样噪声。
    tables:
      - name: "Table 2: Bias Amplification Factor across Heterogeneity Regimes"
        columns: ["Δπ (misclass het.)", "Δτ (CATE het.)", "Δπ×Δτ", "Bias(global)/Bias(uncorrected)", "Analytic Prediction"]
        key_rows:
          - [0.04, 0.04, 0.0016, 1.4, 1.5]
          - [0.08, 0.06, 0.0048, 2.1, 2.2]
          - [0.10, 0.08, 0.008, 3.2, 3.3]
          - [0.12, 0.10, 0.012, 3.8, 3.9]
          - [0.15, 0.12, 0.018, 4.8, 4.7]
          - [0.20, 0.15, 0.030, 7.5, 7.2]
          - [0.25, 0.18, 0.045, 9.8, 9.5]
    figures_description:
      - "Figure: Heatmap — x 轴 Δπ, y 轴 Δτ, color = bias amplification factor。等高线清晰展示 product 的 monotonic structure。moderate 区域 (Δπ∈[0.08,0.15], Δτ∈[0.06,0.12]) 用框标出，对应 2-5x amplification"
      - "Figure: Scatter — analytic prediction vs empirical bias amplification，每个 grid point 一个点，R²=0.94，展示 closed-form 的预测精度"
    analysis: >
      Median 档的叙事转向：不再追求 "debiasing hurts 7-10x" 的 shock value，而是强调 mechanism 的 monotonic、predictable 特性。
      论文应呈现完整 heatmap 让读者看到 amplification 随 product 连续变化，moderate 设定下 3-5x 已经 non-trivial 
      且更 realistic。constructive two-subgroup example 用 Δπ=0.10, Δτ=0.08 得到 ~3.5x amplification，
      足以 motivate stratified correction 但需要 sensitivity analysis 支撑而非单一 headline number。

  - name: "Semi-Synthetic Political Science Benchmark"
    plan_id: "exp-003"
    description: >
      使用 real political-science tweet corpus (CardiffNLP TweetEval sentiment/stance subset)，
      inject known CATE heterogeneity structure (synthetic treatment effect varying by tweet topic/framing)，
      用 GPT-4.1 和 Qwen3-235B-A22B 标注 effect modifier，测量 subgroup-specific misclassification rates，
      对比 EC-HTE vs Global correction vs No correction vs PPCI vs Oracle。
    expected_results:
      gpt4_1_overall_accuracy: 0.82
      gpt4_1_misclass_heterogeneity_delta_pi: 0.09
      qwen3_overall_accuracy: 0.76
      qwen3_misclass_heterogeneity_delta_pi: 0.13
      ec_hte_cate_bias_gpt4_1: 0.032
      ec_hte_cate_bias_qwen3: 0.028
      global_correction_cate_bias_gpt4_1: 0.095
      global_correction_cate_bias_qwen3: 0.118
      no_correction_cate_bias_gpt4_1: 0.041
      no_correction_cate_bias_qwen3: 0.058
      ec_hte_coverage_90ci_gpt4_1: 0.88
      ec_hte_coverage_90ci_qwen3: 0.86
      global_coverage_90ci_gpt4_1: 0.61
      global_coverage_90ci_qwen3: 0.54
      bias_amplification_global_vs_uncorrected_gpt4_1: 2.3
      bias_amplification_global_vs_uncorrected_qwen3: 2.0
      ec_hte_vs_ppci_bias_ratio: 0.55
    result_rationale: >
      Semi-synthetic 设计的核心张力：real LLM errors 提供 ecological validity，但 natural heterogeneity 偏温和。
      GPT-4.1 整体准确率 ~82%，其 misclassification heterogeneity 受 tweet topic 分布影响——
      political framing 类 tweets 因语义复杂度更高导致 error rate 偏高（~0.22），而 factual reporting 类较低（~0.13），
      Δπ≈0.09。这比纯合成设定温和，因此 bias amplification 仅 ~2.3x（非 5-10x），但仍统计显著。
      Qwen3 整体准确率较低（~76%），heterogeneity 更大（Δπ≈0.13），但因 base error rate 高，
      amplification 倍数反而略低（2.0x）——这是因为 denominator（no-correction bias）本身也更大。
      EC-HTE 在两个 LLM 上都将 bias 降至 0.03 左右，但 coverage 略低于 90%（88% 和 86%），
      因为 semi-synthetic 的 CATE heterogeneity 是 injected 的且幅度 moderate（Δτ~0.06-0.08），
      posterior uncertainty 在某些 subgroup 边界处偏大。
      EC-HTE vs PPCI bias ratio ~0.55 表明 EC-HTE 在 covariate-side correction 上 clearly better，
      但 PPCI 并非完全无效（它能捕捉部分 outcome-side 的 correction），差距不悬殊。
      无 real data 是关键 limitation，但 semi-synthetic 的 ecological validity 论证有力：
      real corpus → real LLM annotation patterns → real error heterogeneity → only the treatment effect is synthetic。
    tables:
      - name: "Table 3: Semi-Synthetic Benchmark — CATE Estimation Performance"
        columns: ["Method", "LLM", "|CATE Bias|", "90% Coverage", "RMSE", "Bias Amplification"]
        key_rows:
          - ["Oracle (true labels)", "—", 0.008, 0.94, 0.022, "—"]
          - ["EC-HTE (HB)", "GPT-4.1", 0.032, 0.88, 0.055, "—"]
          - ["EC-HTE (HB)", "Qwen3-235B", 0.028, 0.86, 0.051, "—"]
          - ["Global correction", "GPT-4.1", 0.095, 0.61, 0.122, "2.3x"]
          - ["Global correction", "Qwen3-235B", 0.118, 0.54, 0.148, "2.0x"]
          - ["No correction", "GPT-4.1", 0.041, 0.81, 0.068, "1.0x (ref)"]
          - ["No correction", "Qwen3-235B", 0.058, 0.74, 0.085, "1.0x (ref)"]
          - ["PPCI", "GPT-4.1", 0.058, 0.76, 0.082, "—"]
          - ["PPCI", "Qwen3-235B", 0.072, 0.69, 0.098, "—"]
      - name: "Table 4: Subgroup-Level Misclassification Rates"
        columns: ["LLM", "Subgroup", "Error Rate", "n_tweets", "CATE (true)"]
        key_rows:
          - ["GPT-4.1", "Political framing", 0.22, 3200, 0.12]
          - ["GPT-4.1", "Economic framing", 0.17, 2800, 0.08]
          - ["GPT-4.1", "Factual reporting", 0.13, 4000, 0.04]
          - ["Qwen3-235B", "Political framing", 0.28, 3200, 0.12]
          - ["Qwen3-235B", "Economic framing", 0.23, 2800, 0.08]
          - ["Qwen3-235B", "Factual reporting", 0.19, 4000, 0.04]
    figures_description:
      - "Figure: Subgroup-level CATE estimates ± 90% CI — 每个 subgroup 一组 bars (Oracle / EC-HTE / Global / No correction / PPCI)，清晰展示 global correction 在 low-error subgroup (Factual reporting) 的 over-correction 和 high-error subgroup (Political framing) 的 under-correction"
      - "Figure: Ecological validity 论证 — scatter plot of LLM error rates across subgroups，展示 natural heterogeneity pattern 是 real 而非 artificial"
    analysis: >
      Semi-synthetic 实验的核心发现：natural LLM error heterogeneity 存在但偏温和，bias amplification 在 2-3x 而非 5-10x。
      这要求论文叙事从 "shocking headline" 转向 "principled mechanism + monotonic relationship"。
      GPT-4.1 vs Qwen3 的对比展示了一个 nuanced pattern：更差的 LLM 并不总意味着更大的 amplification ratio，
      因为 base bias（no correction）也更大。EC-HTE 在两个 LLM 上都显著优于 global correction 和 PPCI，
      但 coverage 略低于 nominal——这需要在论文中诚实报告并讨论 calibration。
      PPCI 作为 baseline 表现合理（它不是 designed for covariate-side correction），差异化清晰但不极端。

  - name: "Ashwin Real-Data Validation (Unavailable)"
    plan_id: "exp-004"
    description: >
      Ashwin et al. (2025) Rohingya 难民访谈数据集的 real-data validation。
      在 median 档假设下，数据集不可用。
    expected_results:
      dataset_available: false
      status: "dropped — dataset access denied or no response from authors"
    result_rationale: >
      Median 档核心假设之一是 Ashwin 数据不可用。这是 EMNLP 审稿中最大的 empirical weakness。
      没有 real-data 实验意味着所有验证都基于合成或半合成数据，reviewer 可能质疑 external validity。
      Mitigation 策略：(1) semi-synthetic 设计强调 ecological validity（real corpus, real LLM errors），
      (2) limitation 中正面承认并讨论 generalizability boundary，
      (3) 强调 bias mechanism 是 analytic result 不依赖特定数据集。
    tables: []
    figures_description: []
    analysis: >
      论文需在 Section 7 (Limitations) 正面处理：
      "Our empirical validation relies on synthetic and semi-synthetic benchmarks. While the semi-synthetic design preserves 
      real LLM annotation patterns (real corpus, real errors, synthetic treatment effects only), validation on a fully real 
      causal inference pipeline remains future work. The bias mechanism identified in Claim 1 is an analytic result that 
      holds regardless of data source; the empirical question is the magnitude of naturally occurring heterogeneity in practice."
      同时在 semi-synthetic 设计部分加重 ecological validity 论证的篇幅。

  - name: "Diagnostic Criterion Validation"
    plan_id: "exp-005"
    description: >
      计算所有实验设定中的 Δπ×Δτ product，作为 "when does global correction fail" 的 diagnostic score。
      ROC analysis：以 "global correction bias > no-correction bias" 为 positive label，
      product 为 classifier score。
    expected_results:
      diagnostic_criterion_auroc: 0.84
      diagnostic_criterion_auprc: 0.79
      optimal_threshold_synthetic: 0.005
      optimal_threshold_semisynthetic: 0.008
      threshold_transferability: "poor — thresholds differ ~60% across settings"
      sensitivity_at_90_specificity: 0.72
      specificity_at_90_sensitivity: 0.68
    result_rationale: >
      Median 档下 diagnostic criterion 有效但不悬殊。AUROC ~0.84 表示 product 确实 predictive，
      但远非 perfect classifier。原因：(1) product 是 bias 的一阶近似，忽略了 base rates、sample size 等高阶项，
      在 moderate heterogeneity 下这些高阶项的相对贡献更大；(2) semi-synthetic 的 natural heterogeneity 
      比纯合成的 parameter grid 更 noisy，CATE heterogeneity 的测量本身有误差。
      阈值不可直接 transfer（synthetic optimal ~0.005 vs semi-synthetic ~0.008）是 median 档的关键限制：
      这意味着不能给出 universal threshold，只能给 "risk score + decision heuristic"。
      论文应将 diagnostic 定位为 practitioner tool（"compute this score; if high, consider stratified correction"）
      而非 formal decision rule。
    tables:
      - name: "Table 5: Diagnostic Criterion ROC Performance"
        columns: ["Setting", "AUROC", "Optimal Threshold", "Sensitivity@90%Spec", "Specificity@90%Sens"]
        key_rows:
          - ["Synthetic (all regimes)", 0.88, 0.005, 0.78, 0.74]
          - ["Semi-synthetic (GPT-4.1)", 0.82, 0.008, 0.68, 0.64]
          - ["Semi-synthetic (Qwen3)", 0.83, 0.007, 0.70, 0.66]
          - ["Pooled", 0.84, 0.006, 0.72, 0.68]
    figures_description:
      - "Figure: ROC curves — synthetic vs semi-synthetic settings overlaid，展示 diagnostic 在 synthetic 上更 discriminative (AUROC 0.88) 而 semi-synthetic 上稍弱 (0.82-0.83)，暗示 natural noise 降低了区分度"
      - "Figure: Calibration plot — predicted risk (product score) vs actual probability of global correction failure，展示 monotonic 但非 perfectly calibrated relationship"
    analysis: >
      Diagnostic criterion 的叙事需从 "computable threshold" 弱化为 "computable risk score + decision heuristic"。
      AUROC 0.84 足以 justify standalone value（"this score helps practitioners decide"），
      但阈值不可 transfer 意味着实际使用时需要 pilot study 或 cross-validation 来 calibrate。
      论文应提供 recommended workflow：(1) annotate small pilot with expert labels, (2) compute product score,
      (3) if score > dataset-specific threshold (estimated from pilot), use stratified correction。

  - name: "Expert Label Budget Sensitivity"
    plan_id: "exp-006"
    description: >
      系统化扫描 n_expert ∈ {50, 100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups。
      找到 EC-HTE > Global correction 的 crossover point，验证 HB partial pooling 在小 n 时的价值。
    expected_results:
      crossover_n_expert_k2: 150
      crossover_n_expert_k4: 300
      crossover_n_expert_k8: 600
      hb_advantage_n50_k4: "HB 0.065 bias vs MLE 0.112 bias — 42% reduction but both still high"
      hb_advantage_n250_k4: "HB 0.042 bias vs MLE 0.058 bias — 28% reduction"
      hb_advantage_n500_k4: "HB 0.035 bias vs MLE 0.041 bias — 15% reduction"
      hb_advantage_n1000_k4: "HB 0.029 bias vs MLE 0.031 bias — 6% reduction, practically equivalent"
      hb_advantage_n2000_k4: "HB 0.025 bias vs MLE 0.026 bias — 4% reduction, negligible"
      min_n_for_paper_claim: 500
    result_rationale: >
      Median 档下 min_n_expert_for_dominance 在 250-500 范围。k 的影响是线性的：
      每个 subgroup 需要 ~75 expert labels 才能稳定估计 2×2 confusion matrix（4 参数），
      因此 k=2 需 ~150，k=4 需 ~300，k=8 需 ~600。
      HB partial pooling 的价值在 n/k < 125 时最显著（shrinkage 系数 >0.3），
      此时 MLE 方差过大导致 confusion matrix 估计震荡。
      但 n=50 时即使 HB 也表现不佳（bias 0.065），因为 prior 的信息量有限，
      不应在论文中 claim "EC-HTE works with 50 labels"。
      Safe claim 是 "500 expert labels for k≤4 subgroups"，这个 bar 比原始 framing 的 250 更保守，
      但也更 defensible。n=250 对 k=2 已足够但对 k=4 边缘，论文应分 k 讨论。
    tables:
      - name: "Table 6: Expert Budget Sensitivity — |CATE Bias| by Method × n_expert × k"
        columns: ["n_expert", "k", "EC-HTE (HB)", "Stratified MLE", "Global", "No Correction"]
        key_rows:
          - [50, 4, 0.065, 0.112, 0.110, 0.045]
          - [100, 4, 0.054, 0.082, 0.110, 0.045]
          - [250, 4, 0.042, 0.058, 0.110, 0.045]
          - [500, 4, 0.035, 0.041, 0.110, 0.045]
          - [1000, 4, 0.029, 0.031, 0.110, 0.045]
          - [2000, 4, 0.025, 0.026, 0.110, 0.045]
          - [250, 2, 0.035, 0.045, 0.110, 0.045]
          - [250, 8, 0.055, 0.085, 0.110, 0.045]
    figures_description:
      - "Figure: n_expert vs |CATE Bias| 曲线，分 k=2/4/8 三个 panel，每个 panel 含 EC-HTE / MLE / Global / No-correction 四条线。Global 和 No-correction 是 flat lines（不依赖 n_expert）。关键视觉：EC-HTE 和 MLE 从上方逐渐下降并 converge，crossover 点用竖线标出"
      - "Figure: HB shrinkage coefficient vs n_expert/k — 展示每个 subgroup 分到的样本量如何决定 shrinkage 强度"
    analysis: >
      Expert budget 实验为 Claim 2 的 "500 labels" claim 提供直接 support。
      关键 insight：EC-HTE 的 advantage 随 n 单调递减——这不是 weakness 而是 feature，
      表明 HB 是 "guaranteed non-inferior"（大 n 时等价于 MLE，小 n 时 strictly better）。
      k=8 的结果展示 scalability concern：需要 600+ labels，对很多应用场景不现实，
      论文应建议 "start with coarse subgroups (k≤4) unless you have budget for 1000+ labels"。

  - name: "PPCI Baseline Comparison"
    plan_id: "exp-007"
    description: >
      实现 Sui et al. (2026) PPCI kernel-based conditional correction，
      在 synthetic 和 semi-synthetic benchmarks 上与 EC-HTE 对比。
      关键差异化：PPCI 纠正 outcome-side measurement error，EC-HTE 纠正 covariate-side。
    expected_results:
      ppci_cate_bias_synthetic_moderate: 0.068
      ec_hte_cate_bias_synthetic_moderate: 0.035
      ec_hte_vs_ppci_bias_ratio_synthetic: 0.51
      ppci_cate_bias_semisynthetic_gpt: 0.058
      ec_hte_cate_bias_semisynthetic_gpt: 0.032
      ec_hte_vs_ppci_bias_ratio_semisynthetic: 0.55
      ppci_coverage_90ci_synthetic: 0.78
      ppci_coverage_90ci_semisynthetic: 0.76
      ppci_better_when_outcome_noise: true
      ec_hte_better_when_covariate_noise: true
    result_rationale: >
      PPCI 被设计用于 outcome-side conditional correction（Y 的测量误差），不是 covariate-side（X 的测量误差）。
      当 problem 是 covariate-side misclassification（我们的设定），PPCI 的 kernel localization 只能 partially 
      capture bias，因为它在 mismeasured covariate 空间中做 local correction，而 local neighborhoods 
      在 mismeasured 空间中与 true 空间不一致。
      EC-HTE/PPCI bias ratio ~0.5-0.55（median 档）表示 EC-HTE roughly halves PPCI 的 bias，
      差距 meaningful 但非 order-of-magnitude。这是因为 moderate heterogeneity 下 
      covariate misclassification 导致的 subgroup mixing 是 partial 的——PPCI 的 kernel 仍能 
      capture 部分 local structure。在 extreme heterogeneity 下差距会更大（ratio ~0.3），
      但 median 档不以此为主要卖点。
      叙事应强调 orthogonality：PPCI 和 EC-HTE 解决不同问题，可以 complement（future work），
      而非 EC-HTE "beats" PPCI。
    tables:
      - name: "Table 7: EC-HTE vs PPCI Head-to-Head"
        columns: ["Setting", "Method", "|CATE Bias|", "90% Coverage", "RMSE"]
        key_rows:
          - ["Synthetic moderate", "EC-HTE", 0.035, 0.88, 0.055]
          - ["Synthetic moderate", "PPCI", 0.068, 0.78, 0.089]
          - ["Synthetic moderate", "Global", 0.112, 0.63, 0.135]
          - ["Semi-syn (GPT-4.1)", "EC-HTE", 0.032, 0.88, 0.053]
          - ["Semi-syn (GPT-4.1)", "PPCI", 0.058, 0.76, 0.082]
          - ["Semi-syn (GPT-4.1)", "Global", 0.095, 0.61, 0.122]
          - ["Semi-syn (Qwen3)", "EC-HTE", 0.028, 0.86, 0.051]
          - ["Semi-syn (Qwen3)", "PPCI", 0.072, 0.69, 0.098]
          - ["Semi-syn (Qwen3)", "Global", 0.118, 0.54, 0.148]
    figures_description:
      - "Figure: Side-by-side bar chart — EC-HTE vs PPCI vs Global vs No-correction，分 synthetic / semi-synthetic panels，展示 EC-HTE consistently better than PPCI on covariate-side correction task"
      - "Figure: Conceptual diagram — 展示 PPCI (outcome-side) vs EC-HTE (covariate-side) 的 problem space，强调 orthogonality"
    analysis: >
      PPCI 比较是 reviewer concern #2 的直接回应。Median 档下差异 meaningful 但 moderate，
      应以 "complementary approaches for different error sources" 定位而非 "EC-HTE dominates"。
      论文可提出 future work：combined framework that handles both outcome-side and covariate-side error simultaneously。

  - name: "Multiple LLM Annotator Comparison"
    plan_id: "exp-008"
    description: >
      GPT-4.1 vs Qwen3-235B-A22B vs Claude Sonnet 4.6 三个 LLM 的 annotation，
      测量 misclassification heterogeneity pattern，展示 EC-HTE 的 benefit 随 LLM quality 变化。
    expected_results:
      gpt4_1_accuracy: 0.82
      gpt4_1_delta_pi: 0.09
      qwen3_accuracy: 0.76
      qwen3_delta_pi: 0.13
      claude_sonnet_accuracy: 0.84
      claude_sonnet_delta_pi: 0.07
      ec_hte_benefit_gpt4_1: "bias 0.032 vs global 0.095 — 66% reduction"
      ec_hte_benefit_qwen3: "bias 0.028 vs global 0.118 — 76% reduction"
      ec_hte_benefit_claude: "bias 0.035 vs global 0.078 — 55% reduction"
      heterogeneity_pattern_correlation_across_llms: 0.72
    result_rationale: >
      三个 LLM 展示不同的 accuracy-heterogeneity profile：
      Claude Sonnet 4.6 最准确 (0.84) 但 heterogeneity 最小 (Δπ=0.07)——高质量 LLM 的 errors 更 uniform，
      因此 global correction 的 harm 较小（amplification ~1.9x），EC-HTE 的 marginal benefit 也较小。
      Qwen3 最不准确 (0.76) 且 heterogeneity 最大 (Δπ=0.13)——这对 combination 是 EC-HTE 的 sweet spot。
      GPT-4.1 居中。三个 LLM 的 heterogeneity pattern 有中等相关 (r=0.72)：
      所有 LLM 都在 "political framing" subgroup 上 error rate 最高，但具体 Δπ 幅度不同。
      这个相关性表明 LLM 共享某些 difficulty patterns（语义复杂度），但 magnitude 因 model capability 而异。
      Median 档下的 implication：EC-HTE 对所有 LLM 都有帮助，但 cost-benefit 因 LLM 质量而异。
      最好的 LLM (Claude Sonnet) 使得 global correction 的 harm 较小，EC-HTE 的 added value 也较小——
      这是 honest finding，不需要 hide。
    tables:
      - name: "Table 8: LLM Comparison — Error Patterns & EC-HTE Benefit"
        columns: ["LLM", "Overall Acc.", "Δπ", "Global Bias", "EC-HTE Bias", "Bias Reduction %", "Amplification"]
        key_rows:
          - ["Claude Sonnet 4.6", 0.84, 0.07, 0.078, 0.035, "55%", "1.9x"]
          - ["GPT-4.1", 0.82, 0.09, 0.095, 0.032, "66%", "2.3x"]
          - ["Qwen3-235B-A22B", 0.76, 0.13, 0.118, 0.028, "76%", "2.0x"]
    figures_description:
      - "Figure: LLM quality spectrum — x 轴 overall accuracy, y 轴 misclass heterogeneity Δπ，三个 LLM 作为 data points，展示 accuracy-heterogeneity 的 trade-off pattern"
      - "Figure: Subgroup-level error rate profiles — grouped bar chart, 3 LLMs × 3 subgroups，展示 shared difficulty pattern but different magnitudes"
    analysis: >
      Multi-LLM 实验为 generalizability 提供 evidence：EC-HTE 的 benefit 不限于特定 LLM，
      而是 structural（只要 misclassification heterogeneity 存在就有用）。
      但同时展示了 nuance：最好的 LLM 减少了 problem severity，暗示 LLM improvement 是 partial substitute for EC-HTE。
      论文应 frame 为 "EC-HTE is most valuable when annotation quality is moderate and heterogeneous — 
      which is precisely the regime where LLM annotations are most commonly used"。

  - name: "Adaptive Expert Allocation"
    plan_id: "exp-009"
    description: >
      实现 CATE-weighted allocation（targeting high-CATE × high-error subgroups），
      对比 uniform allocation 和 uncertainty-only allocation。基于 exp-006 的 budget sensitivity 结果。
    expected_results:
      adaptive_vs_uniform_bias_reduction: 0.18
      adaptive_vs_uncertainty_only_bias_reduction: 0.08
      adaptive_optimal_allocation_ratio: "high-CATE×high-error subgroup gets ~2.5x more labels"
      improvement_significant_only_when_n_small: true
      crossover_n_where_uniform_catches_up: 800
    result_rationale: >
      Adaptive allocation 的理论优势在于将 expert labels 集中于 information gain 最高的 subgroups。
      Moderate heterogeneity 下 CATE 差异和 error 差异都不极端，因此 adaptive 的 marginal benefit 有限：
      ~18% bias reduction vs uniform。这是因为 moderate 设定下各 subgroup 的 information need 差异不大（
      high-CATE subgroup 需要更精确但也只比 low-CATE 高 0.06-0.08）。
      Uncertainty-only allocation（只关注 error rate 不考虑 CATE magnitude）已经 capture 了大部分 benefit，
      额外加入 CATE weighting 仅 ~8% incremental improvement。
      当 n≥800 时 uniform allocation 已足够（每个 subgroup ≥200 labels），adaptive 的 overhead 不 justified。
      这是 P2 实验——nice to have 但不改变 paper narrative。
    tables:
      - name: "Table 9: Adaptive vs Uniform Expert Allocation"
        columns: ["Allocation", "n_expert", "k", "|CATE Bias|", "90% Coverage", "Labels to Best Subgroup"]
        key_rows:
          - ["CATE-weighted", 250, 4, 0.038, 0.87, "40%"]
          - ["Uncertainty-only", 250, 4, 0.041, 0.86, "35%"]
          - ["Uniform", 250, 4, 0.046, 0.84, "25%"]
          - ["CATE-weighted", 500, 4, 0.033, 0.89, "35%"]
          - ["Uniform", 500, 4, 0.036, 0.88, "25%"]
    figures_description:
      - "Figure: Allocation strategy comparison — n_expert vs bias curves for three strategies，展示 adaptive 在 n<500 时有优势但 n>800 后 converge"
    analysis: >
      Adaptive allocation 是 paper 的 "cherry on top"，不是 main contribution。
      Median 档下 improvement 是 modest，论文应 present 为 "practitioners with limited budget can further optimize 
      by allocating expert labels proportional to subgroup importance" 而非 claim breakthrough。

  - name: "Robustness to Misspecified Subgroups"
    plan_id: "exp-010"
    description: >
      测试 EC-HTE 在 subgroup structure 与 true effect modification 不对齐时的表现。
      Scenarios: (a) noisy subgroup labels (5-20% mislabeled), (b) true k=4 但 model 用 k=2, 
      (c) continuous effect modifier 被 discretized。
    expected_results:
      noisy_5pct_bias_increase: 0.004
      noisy_10pct_bias_increase: 0.012
      noisy_20pct_bias_increase: 0.028
      k_misspec_4to2_bias: 0.048
      k_misspec_4to2_vs_correct_k4: "38% more bias but still better than global (0.048 vs 0.110)"
      discretization_bias: 0.041
      hb_shrinkage_rescues_moderate_misspec: true
    result_rationale: >
      HB partial pooling 提供 natural robustness against moderate misspecification：
      当 subgroup labels 有 5-10% noise 时，posterior 自动增加 uncertainty 并向 global 收缩，
      bias 增加仅 0.004-0.012。但 20% noise 使 subgroup structure 接近 random，
      shrinkage 过度导致 EC-HTE 退化为 near-global correction（bias 0.028 increase，总 bias ~0.063）。
      k misspecification (true k=4, model k=2) 损失明显（bias 从 ~0.035 升至 ~0.048），
      因为两个 coarse subgroups 各自内部仍有 heterogeneity 未被 capture。但仍优于 global（0.110），
      因为 even coarse stratification captures the dominant heterogeneity mode。
      这些结果 support 论文的 reviewer concern #4 response：HB partial pooling 使 EC-HTE 
      对 moderate misspecification robust（"degrade gracefully"），但 severe misspecification 
      仍然 problematic。
    tables:
      - name: "Table 10: Robustness to Subgroup Misspecification"
        columns: ["Scenario", "EC-HTE Bias", "Δ vs Correct Spec", "Global Bias", "Still Better?"]
        key_rows:
          - ["Correct specification (k=4)", 0.035, "ref", 0.110, "Yes"]
          - ["5% noisy labels", 0.039, "+0.004", 0.110, "Yes"]
          - ["10% noisy labels", 0.047, "+0.012", 0.110, "Yes"]
          - ["20% noisy labels", 0.063, "+0.028", 0.110, "Yes (marginal)"]
          - ["k misspec (4→2)", 0.048, "+0.013", 0.110, "Yes"]
          - ["Continuous discretized", 0.041, "+0.006", 0.110, "Yes"]
    figures_description:
      - "Figure: Degradation curve — x 轴 noise level (0-25%), y 轴 EC-HTE bias，展示 graceful degradation with HB shrinkage，标注 global correction 作为 flat reference line"
    analysis: >
      Robustness 实验为 reviewer concern #4 提供直接 evidence。
      Key message：EC-HTE 在 moderate misspecification 下 gracefully degrades，且始终优于 global correction。
      只有在 severe misspecification (>20% noise 或 k grossly wrong) 时才接近 global performance。
      建议 practitioners "err on the side of fewer, well-defined subgroups (k=2-4) rather than many noisy ones"。

  - name: "Causal Forest Leaf-Level Integration"
    plan_id: "exp-011"
    description: >
      将 EC-HTE correction 集成到 CausalForestDML 的 leaf level：
      corrected pseudo-outcomes + variance-adjusted CIs。对比 naive forest（uncorrected outcomes）。
    expected_results:
      leaf_corrected_vs_naive_bias_reduction: 0.22
      leaf_corrected_coverage_improvement: 0.08
      leaf_corrected_vs_subgroup_ec_hte_bias: "comparable (0.033 vs 0.035) but more granular"
      computational_overhead: "~3x slower due to per-leaf posterior inference"
      practical_value: "marginal over subgroup-level EC-HTE for k≤4, potentially valuable for k≥8"
    result_rationale: >
      Leaf-level integration 将 EC-HTE 的 correction 粒度从 pre-defined subgroups 提升到 forest-determined partitions。
      Moderate heterogeneity 下，causal forest 的 leaves 大致对应 pre-defined subgroups（
      因为 effect modifier 的 CATE heterogeneity 主要沿 subgroup 定义变化），
      所以 leaf-level correction 的 bias (0.033) 与 subgroup-level (0.035) 接近。
      但 leaf-level 的 coverage 更好 (+0.08)，因为 variance-adjusted CIs 更精确地 account for 
      每个 leaf 的 local confusion matrix uncertainty。
      3x computational overhead 来自每个 leaf 需要独立的 posterior inference，
      当 forest 有 ~50 leaves 时这比 k=4 subgroups 慢很多。
      Median 档下这是 P2 实验——methodologically interesting 但对 paper narrative 贡献有限，
      因为 k≤4 的 subgroup-level EC-HTE 已经 sufficient for the claimed results。
    tables:
      - name: "Table 11: Leaf-Level vs Subgroup-Level EC-HTE"
        columns: ["Method", "|CATE Bias|", "90% Coverage", "RMSE", "Compute Time (relative)"]
        key_rows:
          - ["Leaf-level EC-HTE", 0.033, 0.91, 0.052, "3.2x"]
          - ["Subgroup-level EC-HTE (k=4)", 0.035, 0.88, 0.055, "1.0x"]
          - ["Naive forest (no correction)", 0.045, 0.81, 0.068, "0.8x"]
          - ["Global-corrected forest", 0.108, 0.62, 0.132, "0.9x"]
    figures_description:
      - "Figure: CATE heterogeneity map — leaf-level resolution vs subgroup-level resolution 的 visual comparison，展示 leaf-level 在 subgroup boundary 处更 smooth"
    analysis: >
      Leaf-level integration 是 methodological extension，在 median 档下不改变 main narrative。
      建议放在 appendix 或 future work，除非 reviewer 要求更 fine-grained analysis。
      对 k≥8 的 scenario 有 practical value（避免手动定义很多 subgroups），但 median 档的 paper scope 是 k≤4。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "84990687-d24a-4354-888f-9456a01aa0fd",
  "isSidechain": false,
  "requestId": "req_011CbELTYM8MjTskhiSjUd7n",
  "type": "assistant",
  "uuid": "4887812a-6b8c-4c05-acb8-db8e6a6abbec",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Tw367PBvLk3CrBD2coDmVy",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 657,
      "cache_read_input_tokens": 21225,
      "output_tokens": 13292,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 657,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 13292,
          "cache_read_input_tokens": 21225,
          "cache_creation_input_tokens": 657,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 657
          },
          "type": "message"
        }
      ],
      "speed": "standard"
    },
    "diagnostics": null
  }
}
```

</details>

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：bias 放大效应存在但幅度中等，需更多 expert labels 才稳定；仅有合成+半合成验证；PPCI 区分度存在但不悬殊 核心假设：['global correction bias 放大在 moderate heterogeneity 下可复现，但倍数不如极端设定 dramatic', 'HB p…",
  "leafUuid": "4887812a-6b8c-4c05-acb8-db8e6a6abbec",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE: Subgroup-stratified LLM misclassification correction",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---

### Runtime record

_source line 17_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：bias 放大效应存在但幅度中等，需更多 expert labels 才稳定；仅有合成+半合成验证；PPCI 区分度存在但不悬殊 核心假设：['global correction bias 放大在 moderate heterogeneity 下可复现，但倍数不如极端设定 dramatic', 'HB p…",
  "leafUuid": "4887812a-6b8c-4c05-acb8-db8e6a6abbec",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---

### Runtime record

_source line 18_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE: Subgroup-stratified LLM misclassification correction",
  "sessionId": "4e19aba4-a633-4d8d-a9a7-f416f6782e3a"
}
```

---
