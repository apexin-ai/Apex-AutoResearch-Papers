# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：bias 放大效应仅在极端/人造参数下显著，realistic 设定中 global correction 仍可接受；HB 无明显优势；需要 refr

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/254b57df-1b7f-4d24-9c56-510276f6e169.jsonl`
- **Structured JSON:** [`f140e22e923935ce19ef.json`](../../sessions/f1/f140e22e923935ce19ef.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T19:04:27.971Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T19:04:27.971Z",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：bias 放大效应仅在极端/人造参数下显著，realistic 设定中 global correction 仍可接受；HB 无明显优势；需要 reframe\n核心假设：['bias 放大仅在 misclass heterogeneity 极端时出现（Δ error rate > 0.3），moderate 设定下 global correction 的额外 bias < 0.05，实际可忽略', 'HB partial pooling 与 stratified MLE 在 n_expert≥200 时无统计显著差异', 'semi-synthetic 中 LLM 的自然 misclassification heterogeneity 偏小（Δ < 0.10），需人为放大才出效果', 'diagnostic criterion 的 AUROC 偏低，false positive/negative 率高', 'PPCI 在 semi-synthetic 场景下表现与 EC-HTE 相当或仅略差']\n关键指标范围：{'bias_amplification_factor_global_vs_uncorrected': [1.2, 2.0], 'ec_hte_absolute_cate_bias': [0.05, 0.1], 'ec_hte_coverage_90ci': [0.8, 0.88], 'min_n_expert_for_dominance': [500, 1000], 'diagnostic_criterion_auroc': [0.6, 0.78], 'hb_vs_stratified_mle_bias_reduction': [0.0, 0.1], 'ec_hte_vs_ppci_bias_ratio': [0.7, 1.0]}\n叙事方向：核心 \"debiasing can hurt\" 的 surprise value 不足以独立撑 paper——在 realistic 设定下 global correction 的 hurt 太小。需要 reframe，三个可行方向（不降级 venue）： (1) Reframe 为 \"measurement error propagation in HTE\" 的系统性分析论文——不再依赖 \"debiasing hurts\" 的 shock value，而是提供完整的 taxonomy：何时 global 足够、何时需 stratified、何时 correction 本身不值得做。贡献变为 decision framework 而非单一方法。 (2) 如果 HB partial pooling 本身无优势，pivot 到 adaptive expert allocation 作为 方法核心——用 CATE heterogeneity 引导标注预算分配，即使 correction 方法简单（MLE）， allocation strategy 仍有独立价值。需要 exp-009 的结果支撑。 (3) 强化 diagnostic criterion 为 pre-analysis auditing tool——面向 CSS 实践者的 \"should I even bother with stratified correction\" 决策工具，降低方法贡献预期， 提升 practical contribution 叙事。适合 EMNLP Findings 保底，但若 allocation 实验强， 仍可冲 main。任何 reframe 都需要在 exp-001/002 的前 3 天内根据 moderate-regime 结果做出判断，避免沉没成本。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nfocus: 核心关注：(1) \"debiasing can hurt\" 的 surprise value 是否足够撑起 EMNLP main；(2) 层级贝叶斯 partial pooling 作为方法核心是否有足够技术贡献；(3) 仅有合成+半合成实验时论文是否可接受（Ashwin 数据集可能拿不到）；(4) 与 PPCI (Sui 2026) 的差异化是否清晰\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 5-10x compared to no correction at all.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. EC-HTE achieves near-oracle CATE accuracy (|bias| < 0.02) and valid coverage (≥90%) across both high- and low-error subgroups, with expert label budgets as small as 250.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., \"tweet contains economic framing\" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration.\n\n- **Headline result template**: \"On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n## Key Contributions (ordered for paper)\n\n1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes \"debiasing can hurt\" proposition with constructive example. (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI (Sui et al., 2026)?\"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Semi-synthetic benchmark: use real political-science tweet corpus\n    (e.g., CardiffNLP TweetEval or similar public dataset), inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 and Qwen3-235B-A22B, measure subgroup-specific\n    misclassification rates, apply EC-HTE vs baselines. Primary empirical evidence\n    for all claims.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  description: 'Real-data validation on Ashwin et al. (2025) Rohingya refugee interview\n    dataset: LLM annotation errors correlate with refugee status, gender, education.\n    Apply EC-HTE to recover corrected CATEs. Requires dataset access.'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference)\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: Dataset access — need to check if publicly available or request from authors\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1\n  description: 'PPCI (Sui et al., 2026) baseline comparison: implement PPCI kernel-based\n    conditional correction and compare against EC-HTE on same benchmarks. Key differentiation\n    experiment.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 12h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest leaf-level analysis: integrate EC-HTE correction into\n    CausalForestDML at the leaf level (corrected pseudo-outcomes + variance-adjusted\n    CIs), compare against naive forest.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T19:04:27.974Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T19:04:27.974Z",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-20T19:04:27.994Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：bias 放大效应仅在极端/人造参数下显著，realistic 设定中 global correction 仍可接受；HB 无明显优势；需要 reframe
核心假设：['bias 放大仅在 misclass heterogeneity 极端时出现（Δ error rate > 0.3），moderate 设定下 global correction 的额外 bias < 0.05，实际可忽略', 'HB partial pooling 与 stratified MLE 在 n_expert≥200 时无统计显著差异', 'semi-synthetic 中 LLM 的自然 misclassification heterogeneity 偏小（Δ < 0.10），需人为放大才出效果', 'diagnostic criterion 的 AUROC 偏低，false positive/negative 率高', 'PPCI 在 semi-synthetic 场景下表现与 EC-HTE 相当或仅略差']
关键指标范围：{'bias_amplification_factor_global_vs_uncorrected': [1.2, 2.0], 'ec_hte_absolute_cate_bias': [0.05, 0.1], 'ec_hte_coverage_90ci': [0.8, 0.88], 'min_n_expert_for_dominance': [500, 1000], 'diagnostic_criterion_auroc': [0.6, 0.78], 'hb_vs_stratified_mle_bias_reduction': [0.0, 0.1], 'ec_hte_vs_ppci_bias_ratio': [0.7, 1.0]}
叙事方向：核心 "debiasing can hurt" 的 surprise value 不足以独立撑 paper——在 realistic 设定下 global correction 的 hurt 太小。需要 reframe，三个可行方向（不降级 venue）： (1) Reframe 为 "measurement error propagation in HTE" 的系统性分析论文——不再依赖 "debiasing hurts" 的 shock value，而是提供完整的 taxonomy：何时 global 足够、何时需 stratified、何时 correction 本身不值得做。贡献变为 decision framework 而非单一方法。 (2) 如果 HB partial pooling 本身无优势，pivot 到 adaptive expert allocation 作为 方法核心——用 CATE heterogeneity 引导标注预算分配，即使 correction 方法简单（MLE）， allocation strategy 仍有独立价值。需要 exp-009 的结果支撑。 (3) 强化 diagnostic criterion 为 pre-analysis auditing tool——面向 CSS 实践者的 "should I even bother with stratified correction" 决策工具，降低方法贡献预期， 提升 practical contribution 叙事。适合 EMNLP Findings 保底，但若 allocation 实验强， 仍可冲 main。任何 reframe 都需要在 exp-001/002 的前 3 天内根据 moderate-regime 结果做出判断，避免沉没成本。

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
tier: worst
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
  "promptId": "d34b8990-86cf-4827-8154-a0262580a64e",
  "type": "user",
  "uuid": "26a28add-e59f-4466-a3cf-ff68c9d4f7f2",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T19:04:27.993Z_

```json
{
  "parentUuid": "26a28add-e59f-4466-a3cf-ff68c9d4f7f2",
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
  "uuid": "584ee72b-2e9e-4f09-8fd5-cb0ea15aabc8",
  "timestamp": "2026-05-20T19:04:27.993Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T19:04:27.993Z_

```json
{
  "parentUuid": "584ee72b-2e9e-4f09-8fd5-cb0ea15aabc8",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3b4406cc-cbb9-4697-8b38-7e1f704b740b",
  "timestamp": "2026-05-20T19:04:27.993Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169",
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
  "aiTitle": "Reframe EC-HTE narrative for realistic settings",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169"
}
```

---

### Assistant

_source line 7 · 2026-05-20T19:04:41.146Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed "worst tier" predictions for each planned experiment in their experiment plan. They've defined what "worst" means in their context and want me to fill out the YAML format with specific predicted results, rationales, tables, figures, and analysis for each experiment.

Let me carefully go through each experiment and predict what would happen under the "worst" scenario they've defined.

Key characteristics of the "worst" tier:
- Bias amplification only significant under extreme/artificial parameters
- In realistic settings, global correction is still acceptable
- HB has no clear advantage
- Need to reframe the paper
- Core assumptions about what happens in this tier are listed


Now I'm reviewing the specific metric ranges they've established for the worst-case scenarios across all experiments, which will guide my predictions for bias amplification factors, coverage rates, sample size requirements, and diagnostic performance.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b4406cc-cbb9-4697-8b38-7e1f704b740b",
  "isSidechain": false,
  "requestId": "req_011CbELmFVcSw8kDqNRAeoTh",
  "type": "assistant",
  "uuid": "0a630b97-a1ad-4269-8ca2-fbd5d804fc8b",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMHmVf15ctgXLiigLZW7AF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11640,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9522
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

_source line 8 · 2026-05-20T19:08:20.090Z_

```yaml
tier: worst
narrative_guidance: >
  核心 "debiasing can hurt" 的 surprise value 不足以独立撑 paper——在 realistic 设定下 global correction 的 hurt 太小。
  HB partial pooling 相对 stratified MLE 无统计显著优势（n_expert≥200 时），方法贡献被削弱。
  需要 reframe：推荐方向 (1) "measurement error propagation in HTE" 系统性分析论文 + decision framework，
  或 (2) pivot 到 adaptive expert allocation（若 exp-009 结果可用）。
  前 3 天（exp-001/002 moderate regime 结果出炉后）必须做出 reframe 决策，避免沉没成本。

imagined_experiments:
  - name: "HB EC-HTE synthetic validation"
    plan_id: "exp-001"
    description: >
      在合成数据上实现 HB Dirichlet-prior confusion matrix estimator，
      对比 MLE/Laplace，跑 extreme/moderate/homogeneous × n_expert × k 的全 regime sweep。
    expected_results:
      extreme_regime_ec_hte_bias: 0.018
      extreme_regime_global_bias: 0.14
      moderate_regime_ec_hte_bias: 0.065
      moderate_regime_global_bias: 0.09
      moderate_regime_global_vs_uncorrected_amplification: 1.4
      homogeneous_regime_ec_hte_bias: 0.03
      homogeneous_regime_global_bias: 0.035
      ec_hte_coverage_90ci_extreme: 0.88
      ec_hte_coverage_90ci_moderate: 0.82
      hb_vs_stratified_mle_bias_reduction_n200: 0.02
      hb_vs_stratified_mle_bias_reduction_n500: 0.01
      hb_vs_stratified_mle_pvalue_n200: 0.18
      min_n_expert_for_ec_hte_dominance: 750
      k4_vs_k2_bias_increase_factor: 1.6
    result_rationale: >
      Extreme regime（Δ error rate > 0.3）下 EC-HTE 仍能显著优于 global，但这是人造极端设定。
      Moderate regime（Δ error rate ~ 0.10-0.15）下，global correction 的额外 bias 仅约 0.025
      （global 0.09 vs uncorrected 0.065），amplification factor 仅 1.4x，远低于 paper framing 中
      声称的 5-10x。EC-HTE 在 moderate 下 bias 0.065 未达 Claim 2 要求的 < 0.02，因为 partial
      pooling 在 heterogeneity 不够大时过度 shrink 向 global。HB 与 stratified MLE 在 n≥200 时
      无统计显著差异（p=0.18），因为充足样本下 MLE 已足够好，Bayesian shrinkage 的优势消失。
      Coverage 在 moderate 下仅 0.82，低于 0.90 目标，因为 posterior 低估了 correction 的不确定性。
      k=4 时 bias 增加 1.6x 因为每组 n_expert 被摊薄，但 HB pooling 本应缓解此问题——
      实际缓解幅度不够显著。dominance crossover 在 n=750 才出现，意味着 EC-HTE 需要大量
      expert labels 才能稳定优于 global，削弱了 "250 labels 即够" 的叙事。
    tables:
      - title: "Table 1: Synthetic regime sweep — CATE bias by correction method"
        columns: ["Regime", "Δ_error", "CATE_het", "Uncorrected", "Global", "Strat-MLE", "EC-HTE(HB)", "Amplification"]
        rows:
          - ["Extreme", "0.35", "0.30", "0.10", "0.14", "0.020", "0.018", "1.4x→uncorr"]
          - ["Moderate", "0.12", "0.20", "0.065", "0.09", "0.068", "0.065", "1.38x"]
          - ["Homogeneous", "0.02", "0.20", "0.04", "0.035", "0.038", "0.030", "0.88x (helps)"]
      - title: "Table 2: HB vs Stratified MLE — bias reduction by n_expert"
        columns: ["n_expert", "Strat-MLE bias", "HB bias", "Δ bias", "p-value (paired t)"]
        rows:
          - ["100", "0.095", "0.072", "0.023", "0.08"]
          - ["200", "0.068", "0.065", "0.003", "0.18"]
          - ["500", "0.042", "0.038", "0.004", "0.31"]
          - ["1000", "0.025", "0.022", "0.003", "0.42"]
    figures_description:
      - "Fig 1: Heatmap of CATE bias (color) across Δ_error (x) × CATE_het (y) grid，三种方法各一面板。worst 下 EC-HTE 面板在 moderate 区域仍有可见黄色（bias 0.05-0.07），仅极端角落为深蓝。"
      - "Fig 2: Line plot of HB vs MLE bias gap (y) vs n_expert (x)，带 95% CI band。CI 在 n≥200 后包含 0，视觉上两线重合。"
    analysis: >
      核心发现：EC-HTE 的优势几乎完全集中在 extreme regime，而 extreme regime 要求 Δ error rate > 0.3，
      这在真实 LLM annotation 中很少见。moderate regime 下 global correction 的 hurt 太小（amplification 1.4x），
      不足以 motivate 复杂的 HB 方法。HB partial pooling 相对 MLE 无显著优势，
      意味着 Claim 2 的方法贡献核心（partial pooling）站不住。
      建议：前 3 天出 moderate 结果后立即评估 reframe 方向。

  - name: "Formal bias bound verification"
    plan_id: "exp-002"
    description: >
      解析推导 bias = f(misclass_het, CATE_het)，然后在系统性参数网格上验证。
      产出 "debiasing can hurt" proposition。
    expected_results:
      theoretical_bound_tightness_ratio: 0.55
      bias_product_correlation_r2: 0.78
      debiasing_hurts_threshold_delta_error: 0.25
      moderate_regime_amplification_max: 1.8
      extreme_regime_amplification_max: 3.2
      proportion_parameter_space_where_hurts: 0.22
    result_rationale: >
      理论 bound 可以推导出来（bias ∝ Δ_misclass × Δ_CATE），但 bound 较 loose（tightness ratio 0.55，
      即实际 bias 仅为 bound 的 55%），因为 bound 忽略了 confusion matrix 非对角项间的部分抵消效应。
      R² = 0.78 说明 product 解释了大部分 variance 但非全部——剩余 22% 来自高阶交互项和 sample noise。
      关键问题："debiasing can hurt" 的参数空间占比仅 22%，且集中在 Δ error > 0.25 区域。
      在 moderate 设定下 amplification 最大仅 1.8x（不是 5-10x），这使得 "shock value" 大打折扣。
      Proposition 本身数学上成立，但 practical relevance 受限：reviewer 会问 "在什么实际场景下
      Δ error rate 会达到 0.25？"——答案是很少。
    tables:
      - title: "Table 3: Bias amplification factor across parameter grid"
        columns: ["Δ_error_rate", "CATE_het", "Amplification (global/uncorrected)", "EC-HTE corrects?"]
        rows:
          - ["0.05", "0.10", "0.95 (helps)", "marginal"]
          - ["0.05", "0.30", "1.1", "marginal"]
          - ["0.15", "0.10", "1.2", "yes but small"]
          - ["0.15", "0.30", "1.5", "yes"]
          - ["0.30", "0.10", "1.8", "yes"]
          - ["0.30", "0.30", "3.2", "yes, clearly"]
          - ["0.40", "0.30", "5.1", "yes, strongly"]
      - title: "Table 4: Bound tightness analysis"
        columns: ["Regime", "Theoretical upper bound", "Empirical bias", "Tightness ratio"]
        rows:
          - ["Extreme", "0.24", "0.14", "0.58"]
          - ["Moderate", "0.12", "0.065", "0.54"]
          - ["Homogeneous", "0.02", "0.01", "0.50"]
    figures_description:
      - "Fig 3: 3D surface plot of amplification factor over (Δ_error, CATE_het) grid。worst 下 surface 在大部分平面上低于 2.0，仅在远角（Δ>0.3, CATE_het>0.25）才陡升。"
      - "Fig 4: Scatter plot of theoretical bound (x) vs empirical bias (y)，带 y=x 参考线。点系统性低于参考线，斜率约 0.55。"
    analysis: >
      理论结果数学上成立但 practical significance 不足。"debiasing can hurt" 仅在参数空间的 22% 成立，
      且需要 Δ error > 0.25。这支持 reframe 方向 (1)：不再依赖 shock value，
      而是提供 "何时 global 够用、何时需 stratified" 的 decision framework。
      Bound 的 looseness（0.55）也意味着实际风险比理论预测小，进一步削弱 alarm 叙事。

  - name: "Semi-synthetic benchmark"
    plan_id: "exp-003"
    description: >
      用真实政治科学 tweet corpus 注入已知 CATE heterogeneity，
      GPT-4.1 和 Qwen3-235B-A22B 标注，测 subgroup-specific misclassification，
      对比 EC-HTE vs baselines。
    expected_results:
      gpt4_1_overall_accuracy: 0.88
      gpt4_1_delta_error_across_subgroups: 0.07
      qwen3_overall_accuracy: 0.82
      qwen3_delta_error_across_subgroups: 0.09
      natural_cate_heterogeneity: 0.12
      global_correction_cate_bias: 0.04
      ec_hte_cate_bias: 0.035
      uncorrected_cate_bias: 0.055
      global_amplification_vs_uncorrected: 1.15
      ec_hte_coverage_90ci: 0.83
      ec_hte_vs_global_improvement_percent: 12.5
    result_rationale: >
      这是 worst tier 最关键的打击点。LLM 的自然 misclassification heterogeneity 偏小：
      GPT-4.1 在 tweet 分类上准确率高（0.88），subgroup 间 Δ error 仅 0.07——远低于
      synthetic 实验中制造的 0.30+ 极端值。Qwen3 稍差但 Δ 也仅 0.09。
      这直接验证了 worst tier 的核心假设：semi-synthetic 中需要人为放大才能出效果。
      自然 heterogeneity（Δ=0.07）× 注入的 CATE heterogeneity（0.12）= product 0.0084，
      远低于 diagnostic criterion 会建议 stratified correction 的阈值。
      结果是 global correction 的 bias（0.04）与 EC-HTE（0.035）差距微小（仅 12.5% improvement），
      且 global 相对 uncorrected 的 amplification 仅 1.15x——几乎可以忽略。
      Coverage 0.83 < 0.90 因为 subgroup sample size 在 semi-synthetic 中被进一步稀释。
      这个结果让 reviewer 直接质疑："在真实 LLM 上，你的方法解决的问题根本不存在。"
    tables:
      - title: "Table 5: LLM misclassification heterogeneity in semi-synthetic benchmark"
        columns: ["LLM", "Overall Acc", "Subgroup 1 Acc", "Subgroup 2 Acc", "Δ error", "Natural?"]
        rows:
          - ["GPT-4.1", "0.88", "0.91", "0.84", "0.07", "yes"]
          - ["Qwen3-235B", "0.82", "0.86", "0.77", "0.09", "yes"]
          - ["GPT-4.1 (amplified)", "0.88", "0.95", "0.60", "0.35", "no, artificial"]
      - title: "Table 6: Semi-synthetic CATE bias comparison (natural heterogeneity)"
        columns: ["Method", "CATE bias (subgroup 1)", "CATE bias (subgroup 2)", "Mean |bias|", "Coverage 90%"]
        rows:
          - ["Uncorrected", "0.06", "0.05", "0.055", "0.78"]
          - ["Global correction", "0.03", "0.05", "0.04", "0.80"]
          - ["Stratified MLE", "0.04", "0.04", "0.04", "0.81"]
          - ["EC-HTE (HB)", "0.03", "0.04", "0.035", "0.83"]
          - ["Oracle", "0.01", "0.01", "0.01", "0.93"]
    figures_description:
      - "Fig 5: Bar chart 对比四种方法在 natural vs amplified heterogeneity 下的 CATE bias。Natural 下四根 bar 高度几乎相同（0.035-0.055），amplified 下才拉开差距。视觉上 natural 部分毫无戏剧性。"
      - "Fig 6: Subgroup-specific error rate distribution (violin plot) for GPT-4.1 和 Qwen3。Violin 高度重叠，中位数差距小，支撑 Δ error 偏小的结论。"
    analysis: >
      Semi-synthetic 是论文 empirical evidence 的核心，但在 worst 下它直接瓦解了主叙事：
      真实 LLM 的 misclassification heterogeneity 太小，global correction 不会 hurt。
      如果要在 paper 中展示 semi-synthetic 结果，必须同时展示 amplified 版本，
      但 reviewer 会追问 "为什么 natural 设定下效果不明显"。
      Reframe 方向 (1)（系统性分析）可以正面拥抱这个结果："我们的贡献是告诉你何时不需要 stratified"。

  - name: "Ashwin real-data validation"
    plan_id: "exp-004"
    description: >
      在 Ashwin et al. (2025) Rohingya 难民访谈数据集上验证 EC-HTE。
      LLM annotation errors 与 refugee status/gender/education 相关。
    expected_results:
      dataset_access_obtained: false
      fallback_public_dataset_delta_error: 0.08
      ec_hte_improvement_over_global_percent: 10
      practical_significance: "marginal"
    result_rationale: >
      Worst tier 下有两层打击：(1) 数据集大概率拿不到（Ashwin 数据涉及难民敏感信息，
      需伦理审批，短期内无法获取）；(2) 即使用替代公开数据集，真实 misclassification
      heterogeneity 同样偏小（Δ ~ 0.08），与 exp-003 的 semi-synthetic 结论一致。
      没有 real-data validation，论文只有 synthetic + semi-synthetic，
      reviewer concern 会加剧："claims 未在真实因果推断场景中验证"。
      替代方案（公开 CSS 数据集）的 improvement 仅 ~10%，不够 compelling。
    tables:
      - title: "Table 7: Real-data validation results (fallback public dataset)"
        columns: ["Method", "CATE bias", "Coverage", "Improvement vs Global"]
        rows:
          - ["Uncorrected", "0.07", "0.76", "—"]
          - ["Global", "0.055", "0.79", "baseline"]
          - ["EC-HTE", "0.05", "0.82", "10%"]
    figures_description:
      - "Fig 7: (May not exist) — 如果 Ashwin 数据不可得，此实验可能仅有替代数据集的 bar chart，视觉效果弱。"
    analysis: >
      数据不可得是 worst tier 的高概率事件。建议：(1) 立即联系 Ashwin 团队确认数据可用性；
      (2) 准备 2-3 个公开 CSS 数据集作为 fallback；(3) 在 reframe 叙事中不再将 real-data 作为
      核心贡献，而是 "illustrative application"。

  - name: "Diagnostic criterion validation"
    plan_id: "exp-005"
    description: >
      在所有实验设定中计算 misclass_het × CATE_het product，
      验证其预测 global correction 失败的能力。ROC 分析。
    expected_results:
      diagnostic_auroc: 0.68
      optimal_threshold: 0.035
      false_positive_rate_at_90_sensitivity: 0.45
      false_negative_rate_at_90_specificity: 0.52
      correlation_product_vs_bias_gap: 0.62
    result_rationale: >
      AUROC 仅 0.68，勉强优于随机（0.50）。原因：(1) "global correction fails" 的定义本身
      模糊——在 worst 下 amplification 多数时候 < 2x，hard cutoff 不好定；
      (2) product metric 是一阶近似，忽略了 confusion matrix 结构（non-diagonal 交互）、
      样本量、CATE estimation noise 等因素；(3) semi-synthetic 的 natural heterogeneity 太小，
      导致 positive cases 集中在 artificial 设定，ROC 曲线在 realistic 区域表现差。
      False positive rate 高（0.45 at 90% sensitivity）意味着 criterion 会频繁建议
      不必要的 stratified correction，增加无谓的 expert label 成本。
      作为 "practical tool" 其可用性存疑——实践者无法信任一个 FPR=0.45 的决策工具。
    tables:
      - title: "Table 8: Diagnostic criterion ROC performance"
        columns: ["Sensitivity", "Specificity", "FPR", "Threshold"]
        rows:
          - ["0.90", "0.55", "0.45", "0.020"]
          - ["0.80", "0.65", "0.35", "0.035"]
          - ["0.70", "0.72", "0.28", "0.050"]
          - ["0.60", "0.80", "0.20", "0.070"]
      - title: "Table 9: AUROC by data regime"
        columns: ["Regime", "AUROC", "N cases"]
        rows:
          - ["Extreme only", "0.82", "120"]
          - ["Moderate only", "0.58", "180"]
          - ["Mixed (all)", "0.68", "400"]
    figures_description:
      - "Fig 8: ROC curve with 95% bootstrap CI band。曲线在左上角不够凸，CI band 宽（尤其 moderate regime 子集），AUC=0.68 标注。"
      - "Fig 9: Scatter of product metric (x) vs actual bias gap (y)，带 LOESS smoothing line。散点分散，R²=0.62 标注，moderate regime 点（标红）聚集在原点附近。"
    analysis: >
      AUROC 0.68 不足以支撑 Claim 3 作为独立贡献。但在 reframe 方向 (3) 下，
      可以降低预期：不声称是 "high-accuracy diagnostic"，而是 "pre-analysis screening heuristic"，
      告诉实践者 "如果 product < 0.02，你几乎肯定不需要 stratified correction"。
      这种 negative-predictive-value 叙事可能比 AUROC 更有说服力，但需要重新分析。

  - name: "Expert label budget sensitivity"
    plan_id: "exp-006"
    description: >
      n_expert ∈ {50,100,250,500,1000,2000} × k ∈ {2,4,8} 的系统性 sweep。
      找 EC-HTE > Global 的 crossover point，验证 HB pooling 在小 n 下的价值。
    expected_results:
      crossover_n_k2: 500
      crossover_n_k4: 750
      crossover_n_k8: 1200
      hb_advantage_at_n50_k4: 0.08
      hb_advantage_at_n100_k4: 0.04
      hb_advantage_at_n250_k4: 0.015
      hb_vs_mle_significant_at_n50: true
      hb_vs_mle_significant_at_n250: false
      ec_hte_coverage_at_n100_k8: 0.72
    result_rationale: >
      Crossover point（EC-HTE 稳定优于 Global 的最小 n_expert）远高于预期：k=2 时 500，
      k=4 时 750，k=8 时 1200。这意味着 "250 expert labels 即够" 的叙事不成立。
      HB 在极小 n（n=50, k=4, 即每组仅 12.5 个 expert labels）时确实优于 MLE
      （Bayesian shrinkage 在极端数据稀缺时有价值），但 n≥250 后优势消失。
      这个 "HB 仅在极小 n 有用" 的结论与 Claim 2 矛盾：如果 n 足够大 MLE 就够了，
      如果 n 太小任何方法都不可靠（coverage 0.72 at n=100, k=8）。
      k=8 时 crossover 在 1200，说明 fine-grained subgroup structure 需要大量 expert labels，
      削弱了方法的 practical scalability。
    tables:
      - title: "Table 10: Crossover n_expert by number of subgroups"
        columns: ["k", "Crossover n", "n_per_group at crossover", "HB advantage at crossover"]
        rows:
          - ["2", "500", "250", "0.008"]
          - ["4", "750", "187", "0.012"]
          - ["8", "1200", "150", "0.015"]
      - title: "Table 11: HB vs MLE bias difference by (n, k)"
        columns: ["n_expert", "k=2 Δbias", "k=4 Δbias", "k=8 Δbias"]
        rows:
          - ["50", "0.05*", "0.08*", "0.12*"]
          - ["100", "0.025", "0.04*", "0.07*"]
          - ["250", "0.008", "0.015", "0.03"]
          - ["500", "0.004", "0.006", "0.015"]
          - ["1000", "0.002", "0.003", "0.005"]
    figures_description:
      - "Fig 10: Line plot of EC-HTE bias (y) vs n_expert (x)，分 k=2/4/8 三条线，带 Global correction 水平参考线。Crossover 点用竖线标出，均在 500+。"
      - "Fig 11: Heatmap of HB-MLE bias difference across (n, k) grid。仅左上角（小n, 大k）为深色，大部分面积接近 0。"
    analysis: >
      Expert budget sensitivity 结果对方法叙事是双刃剑。一方面，确认了 HB 在极小 n 时有价值；
      另一方面，crossover 太高且 HB 优势窗口太窄。如果 pivot 到 reframe (2)（adaptive allocation），
      这些结果反而有用：allocation strategy 的价值在于用更少 total budget 达到 crossover，
      而不是让 HB 本身更好。

  - name: "PPCI baseline comparison"
    plan_id: "exp-007"
    description: >
      实现 PPCI (Sui 2026) kernel-based conditional correction，
      在相同 benchmark 上与 EC-HTE 对比。关键差异化实验。
    expected_results:
      ppci_cate_bias_extreme: 0.06
      ec_hte_cate_bias_extreme: 0.018
      ppci_cate_bias_moderate: 0.055
      ec_hte_cate_bias_moderate: 0.065
      ec_hte_vs_ppci_bias_ratio_extreme: 0.30
      ec_hte_vs_ppci_bias_ratio_moderate: 1.18
      ppci_coverage_90ci: 0.87
      ppci_computation_time_ratio: 0.3
    result_rationale: >
      PPCI 是 outcome-side correction，与 EC-HTE 的 covariate-side correction 理论上正交。
      但在 worst 下的核心问题是：moderate regime 下 PPCI 表现与 EC-HTE 相当甚至略优
      （bias ratio 1.18，即 EC-HTE 的 bias 是 PPCI 的 1.18 倍）。这是因为在 Δ error 小的
      moderate 设定下，covariate-side error 本身不大，outcome-side correction（PPCI 擅长的）
      反而是主要误差来源，PPCI 的 kernel localization 天然能处理 conditional heterogeneity。
      仅在 extreme regime（Δ error > 0.3）下 EC-HTE 才明显优于 PPCI（ratio 0.30）。
      更致命的是 PPCI 计算效率高 3x（无需 MCMC），coverage 也更好（0.87 vs 0.83）。
      这让 reviewer 直接质疑："为什么不直接用 PPCI？只有在人造极端场景下 EC-HTE 才更好。"
    tables:
      - title: "Table 12: EC-HTE vs PPCI comparison"
        columns: ["Regime", "EC-HTE bias", "PPCI bias", "Ratio (EC/PPCI)", "EC-HTE coverage", "PPCI coverage"]
        rows:
          - ["Extreme", "0.018", "0.060", "0.30", "0.88", "0.85"]
          - ["Moderate", "0.065", "0.055", "1.18", "0.82", "0.87"]
          - ["Homogeneous", "0.030", "0.028", "1.07", "0.85", "0.89"]
          - ["Semi-synthetic (natural)", "0.035", "0.032", "1.09", "0.83", "0.87"]
    figures_description:
      - "Fig 12: Paired bar chart of EC-HTE vs PPCI bias 按 regime 分组。Moderate 和 homogeneous 组 PPCI bar 略低，仅 extreme 组 EC-HTE 明显低。"
      - "Fig 13: Computation time comparison bar chart。PPCI 快 3x，visual 上差距明显。"
    analysis: >
      PPCI 对比是 worst 下最危险的结果。如果 moderate regime 下 PPCI 略优，
      reviewer 会质疑 EC-HTE 的独立价值。防御策略：(1) 强调两者解决不同问题
      （covariate-side vs outcome-side），可以 compose；(2) 展示 combined EC-HTE+PPCI
      优于单独使用的结果；(3) reframe 叙事中将 PPCI 作为互补而非竞争方法。
      但 "compose" 需要额外实验验证。

  - name: "Multiple LLM annotator comparison"
    plan_id: "exp-008"
    description: >
      GPT-4.1 vs Qwen3-235B-A22B vs Claude Sonnet 4.6 的 misclassification heterogeneity
      patterns 对比，展示 EC-HTE benefit 随 LLM quality 变化。
    expected_results:
      gpt4_1_delta_error: 0.07
      qwen3_delta_error: 0.09
      claude_sonnet_delta_error: 0.06
      gpt4_1_ec_hte_improvement_pct: 12
      qwen3_ec_hte_improvement_pct: 18
      claude_sonnet_ec_hte_improvement_pct: 8
      cross_llm_delta_error_range: [0.06, 0.09]
      correlation_llm_quality_vs_delta_error: -0.75
    result_rationale: >
      三个 LLM 的 Δ error 都偏小（0.06-0.09），验证了 worst tier 假设：
      现代高质量 LLM 的 misclassification heterogeneity 自然很低。
      更高质量的 LLM（Claude Sonnet）heterogeneity 更低（0.06），
      EC-HTE improvement 也更小（8%）。Qwen3 质量略低，Δ error 略大，
      但仍远低于 EC-HTE 显著有效所需的 0.25+ 阈值。
      隐含结论令人不安：随着 LLM 质量提升，EC-HTE 的价值持续缩小——
      方法解决的问题正在被模型进步自然消解。
      这个 "diminishing relevance" 叙事是 reviewer 最可能提出的根本性质疑。
    tables:
      - title: "Table 13: Multi-LLM misclassification heterogeneity"
        columns: ["LLM", "Overall Acc", "Δ error", "EC-HTE improvement %", "Need stratified?"]
        rows:
          - ["GPT-4.1", "0.88", "0.07", "12%", "marginal"]
          - ["Qwen3-235B-A22B", "0.82", "0.09", "18%", "marginal"]
          - ["Claude Sonnet 4.6", "0.90", "0.06", "8%", "no"]
    figures_description:
      - "Fig 14: Scatter plot of LLM accuracy (x) vs Δ error (y) vs EC-HTE improvement (bubble size)。三个点几乎在一条负斜率线上，bubble 都小。"
    analysis: >
      多 LLM 对比加强了 worst 叙事：问题随 LLM 进步在消失。
      但可用于 reframe (1)：系统性分析 "不同 LLM 质量档位下何时需要 stratified correction"
      本身是有价值的实证贡献——告诉实践者 "如果你用 GPT-4.1 级别模型，global 够了"。

  - name: "Adaptive expert annotation allocation"
    plan_id: "exp-009"
    description: >
      实现 CATE-weighted allocation（targeting high-CATE × high-error subgroups），
      对比 uniform 和 uncertainty-only allocation。
    expected_results:
      adaptive_vs_uniform_bias_reduction: 0.15
      adaptive_vs_uniform_budget_saving: 0.20
      adaptive_vs_uncertainty_only_improvement: 0.05
      adaptive_allocation_crossover_reduction: 0.18
      optimal_allocation_identifiability: "weak"
    result_rationale: >
      Adaptive allocation 在 worst 下有中等结果：相比 uniform 有 15% bias reduction 和
      20% budget saving，但这些改进在绝对值上不大（因为 moderate regime 下 bias 本身小）。
      相比 uncertainty-only allocation 仅 5% improvement——因为在 worst 下 CATE heterogeneity
      信号弱，CATE-weighted 和 uncertainty-weighted 的 allocation 差异不大。
      "Optimal allocation identifiability" 弱是因为需要先估 CATE heterogeneity 才能分配，
      但估 CATE 本身就需要 expert labels（鸡生蛋问题），pilot round 估计 noisy。
      Crossover n 仅降低 18%（如 k=4 从 750 降到 615），改善有限。
      这个结果对 reframe (2)（pivot to allocation）不够支撑——allocation 策略
      的独立价值不足以作为 paper 核心方法贡献。
    tables:
      - title: "Table 14: Allocation strategy comparison (k=4, total n=500)"
        columns: ["Strategy", "Mean CATE bias", "Worst-subgroup bias", "Coverage"]
        rows:
          - ["Uniform", "0.065", "0.09", "0.82"]
          - ["Uncertainty-only", "0.058", "0.08", "0.84"]
          - ["CATE-weighted (adaptive)", "0.055", "0.07", "0.85"]
          - ["Oracle allocation", "0.040", "0.05", "0.89"]
    figures_description:
      - "Fig 15: Bar chart of three allocation strategies + oracle。Adaptive 略优于 uniform 但距 oracle 远。差异视觉上不够 dramatic。"
    analysis: >
      Adaptive allocation 有 modest improvement 但不足以独立撑 reframe (2)。
      如果与 reframe (1)（decision framework）结合，可以作为 framework 的一部分：
      "如果 diagnostic 判断需要 stratified，用 adaptive allocation 节省 20% budget"。
      这是 supporting contribution，不是核心。

  - name: "Robustness to misspecified subgroups"
    plan_id: "exp-010"
    description: >
      当 subgroup 定义有 noise 或与 true conditioning structure 不一致时，
      测试 EC-HTE 的 robustness。
    expected_results:
      ec_hte_bias_under_20pct_noise: 0.08
      ec_hte_bias_under_50pct_noise: 0.12
      global_bias_under_50pct_noise: 0.10
      hb_shrinkage_behavior: "over-shrinks to global under noise"
      ec_hte_worse_than_global_at_noise_pct: 35
    result_rationale: >
      当 subgroup 定义含 20% noise 时 EC-HTE bias 升至 0.08（clean 时 0.065），尚可接受。
      但 50% noise 时 bias 升至 0.12，反而比 global（0.10）更差——因为 HB 在错误
      subgroup structure 下的 partial pooling 既不是 full global（会更好）也不是 correct stratified，
      而是在错误分层上做了 "精确但错误" 的 correction。HB 的 shrinkage 在 noise 大时
      倾向于 over-shrink 到 global，但 shrinkage 量不够（仍保留了错误分层的部分信息），
      导致 worse-than-global 的尴尬结果。
      EC-HTE 从 noise=35% 开始就不如 global——这意味着如果实践者的 subgroup 定义
      有 >35% 的错误率（在自然语言 subgroup 定义中很常见），方法反而有害。
    tables:
      - title: "Table 15: Robustness to subgroup misspecification"
        columns: ["Noise %", "EC-HTE bias", "Global bias", "EC-HTE better?"]
        rows:
          - ["0%", "0.065", "0.09", "yes"]
          - ["10%", "0.07", "0.09", "yes"]
          - ["20%", "0.08", "0.09", "marginal"]
          - ["35%", "0.10", "0.09", "no (crossover)"]
          - ["50%", "0.12", "0.10", "no"]
    figures_description:
      - "Fig 16: Line plot of EC-HTE bias (blue) vs Global bias (red, flat) vs noise level (x)。两线在 35% 处交叉，之后 EC-HTE 线高于 Global。"
    analysis: >
      Robustness 结果是 worst 下的额外风险：EC-HTE 对 subgroup 定义质量敏感。
      在 reframe (1) 中可正面利用："我们的 framework 不仅告诉你何时需要 stratified，
      还告诉你 subgroup 定义质量的最低要求"。这增加了 decision framework 的完整性。

  - name: "Causal forest leaf-level integration"
    plan_id: "exp-011"
    description: >
      将 EC-HTE correction 集成到 CausalForestDML 的 leaf level
      （corrected pseudo-outcomes + variance-adjusted CIs），对比 naive forest。
    expected_results:
      leaf_level_ec_hte_bias_reduction: 0.03
      leaf_level_coverage_improvement: 0.04
      computational_overhead_factor: 8.5
      convergence_issues_pct: 15
      leaf_level_vs_subgroup_level_improvement: 0.01
    result_rationale: >
      Leaf-level integration 在 worst 下面临实际困难：(1) 每个 leaf 的 expert labels 极少
      （forest 有数百 leaves，即使 n_expert=2000 每 leaf 平均 < 10），HB 在如此小 n 下
      posterior 高度依赖 prior，correction 本质上退化为 global；(2) 计算开销 8.5x
      因为每个 leaf 需要独立 MCMC；(3) 15% 的 leaves 出现 MCMC convergence issues
      （divergent transitions）因为每 leaf 数据太少。
      最终 leaf-level 相对 subgroup-level 的额外 improvement 仅 0.01（bias reduction 从
      subgroup-level 的 0.065 到 leaf-level 的 0.055），不值得 8.5x 计算开销。
      这直接削弱了 "将 EC-HTE 深度集成到 causal forest" 的技术叙事。
    tables:
      - title: "Table 16: Subgroup-level vs leaf-level EC-HTE"
        columns: ["Integration level", "CATE bias", "Coverage", "Compute time (min)", "Convergence issues"]
        rows:
          - ["Subgroup (k=4)", "0.065", "0.82", "12", "0%"]
          - ["Leaf-level", "0.055", "0.86", "102", "15%"]
          - ["Leaf-level (converged only)", "0.048", "0.88", "102", "—"]
    figures_description:
      - "Fig 17: Trade-off scatter plot of compute time (x) vs CATE bias (y)。Subgroup-level 在左下（快+低 bias），leaf-level 在右下但仅略低，性价比差。"
    analysis: >
      Leaf-level integration 在 worst 下不值得。但这个 negative result 在 reframe (1) 中有价值：
      "subgroup-level correction 已足够，更细粒度 correction 收益递减"——
      这是 decision framework 的又一条实用建议。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0a630b97-a1ad-4269-8ca2-fbd5d804fc8b",
  "isSidechain": false,
  "requestId": "req_011CbELmFVcSw8kDqNRAeoTh",
  "type": "assistant",
  "uuid": "84b7ee94-9041-461e-915c-b3e3a43eec16",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EMHmVf15ctgXLiigLZW7AF",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9522,
      "cache_read_input_tokens": 11841,
      "output_tokens": 11640,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9522,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 11640,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9522,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9522
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

_source line 9_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：bias 放大效应仅在极端/人造参数下显著，realistic 设定中 global correction 仍可接受；HB 无明显优势；需要 reframe 核心假设：['bias 放大仅在 misclass heterogeneity 极端时出现（Δ error rate > 0.3），moderate…",
  "leafUuid": "84b7ee94-9041-461e-915c-b3e3a43eec16",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe EC-HTE narrative for realistic settings",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：bias 放大效应仅在极端/人造参数下显著，realistic 设定中 global correction 仍可接受；HB 无明显优势；需要 reframe 核心假设：['bias 放大仅在 misclass heterogeneity 极端时出现（Δ error rate > 0.3），moderate…",
  "leafUuid": "84b7ee94-9041-461e-915c-b3e3a43eec16",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Reframe EC-HTE narrative for realistic settings",
  "sessionId": "254b57df-1b7f-4d24-9c56-510276f6e169"
}
```

---
