# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：三条 claims 全部在合理参数范围内得到强验证；semi-synthetic 结果足够 dramatic 撑 headline；Ashwin 数据可

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/94f0a1eb-767c-4fff-9455-a90d87bab21c.jsonl`
- **Structured JSON:** [`e336a30ea6169c5f4425.json`](../../sessions/e3/e336a30ea6169c5f4425.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T18:55:42.113Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T18:55:42.113Z",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：三条 claims 全部在合理参数范围内得到强验证；semi-synthetic 结果足够 dramatic 撑 headline；Ashwin 数据可用或可替代\n核心假设：['global correction 在 moderate heterogeneity 设定下即产生显著 bias 放大（不需要极端参数）', 'HB partial pooling 在 n_expert=250 时已明显优于 stratified MLE（小样本优势可量化）', 'diagnostic criterion 有高判别力，阈值跨数据集稳定', 'semi-synthetic 中 GPT-4.1/Qwen3 的 misclassification heterogeneity 自然存在且足够大', '至少有一个 real-data 验证（Ashwin 或替代公开数据集）']\n关键指标范围：{'bias_amplification_factor_global_vs_uncorrected': [5.0, 12.0], 'ec_hte_absolute_cate_bias': [0.005, 0.02], 'ec_hte_coverage_90ci': [0.9, 0.97], 'min_n_expert_for_dominance': [100, 250], 'diagnostic_criterion_auroc': [0.9, 0.98], 'hb_vs_stratified_mle_bias_reduction': [0.3, 0.6], 'ec_hte_vs_ppci_bias_ratio': [0.15, 0.4]}\n叙事方向：原始 framing 完全成立。\"Debiasing can hurt\" 作为 problem-level discovery 有足够 surprise value： 在 realistic 参数下 global correction 使 bias 恶化 5-10x，这是 NLP+CSS 社区未意识到的陷阱。 EC-HTE 以 250 expert labels 实现 near-oracle，HB partial pooling 的小样本优势可量化。 Diagnostic criterion 作为 standalone practical tool 给论文第三条独立贡献。 Real data 验证锁定了 \"不只是理论上可能\" 的叙事。投 EMNLP main 无需降级任何 claim。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: ec_hte_llm_annotation\nfocus: 核心关注：(1) \"debiasing can hurt\" 的 surprise value 是否足够撑起 EMNLP main；(2) 层级贝叶斯 partial pooling 作为方法核心是否有足够技术贡献；(3) 仅有合成+半合成实验时论文是否可接受（Ashwin 数据集可能拿不到）；(4) 与 PPCI (Sui 2026) 的差异化是否清晰\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 5-10x compared to no correction at all.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. EC-HTE achieves near-oracle CATE accuracy (|bias| < 0.02) and valid coverage (≥90%) across both high- and low-error subgroups, with expert label budgets as small as 250.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., \"tweet contains economic framing\" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration.\n\n- **Headline result template**: \"On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n## Key Contributions (ordered for paper)\n\n1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes \"debiasing can hurt\" proposition with constructive example. (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI (Sui et al., 2026)?\"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Semi-synthetic benchmark: use real political-science tweet corpus\n    (e.g., CardiffNLP TweetEval or similar public dataset), inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 and Qwen3-235B-A22B, measure subgroup-specific\n    misclassification rates, apply EC-HTE vs baselines. Primary empirical evidence\n    for all claims.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  description: 'Real-data validation on Ashwin et al. (2025) Rohingya refugee interview\n    dataset: LLM annotation errors correlate with refugee status, gender, education.\n    Apply EC-HTE to recover corrected CATEs. Requires dataset access.'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference)\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: Dataset access — need to check if publicly available or request from authors\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1\n  description: 'PPCI (Sui et al., 2026) baseline comparison: implement PPCI kernel-based\n    conditional correction and compare against EC-HTE on same benchmarks. Key differentiation\n    experiment.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 12h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest leaf-level analysis: integrate EC-HTE correction into\n    CausalForestDML at the leaf level (corrected pseudo-outcomes + variance-adjusted\n    CIs), compare against naive forest.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T18:55:42.117Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T18:55:42.117Z",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-20T18:55:42.140Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：三条 claims 全部在合理参数范围内得到强验证；semi-synthetic 结果足够 dramatic 撑 headline；Ashwin 数据可用或可替代
核心假设：['global correction 在 moderate heterogeneity 设定下即产生显著 bias 放大（不需要极端参数）', 'HB partial pooling 在 n_expert=250 时已明显优于 stratified MLE（小样本优势可量化）', 'diagnostic criterion 有高判别力，阈值跨数据集稳定', 'semi-synthetic 中 GPT-4.1/Qwen3 的 misclassification heterogeneity 自然存在且足够大', '至少有一个 real-data 验证（Ashwin 或替代公开数据集）']
关键指标范围：{'bias_amplification_factor_global_vs_uncorrected': [5.0, 12.0], 'ec_hte_absolute_cate_bias': [0.005, 0.02], 'ec_hte_coverage_90ci': [0.9, 0.97], 'min_n_expert_for_dominance': [100, 250], 'diagnostic_criterion_auroc': [0.9, 0.98], 'hb_vs_stratified_mle_bias_reduction': [0.3, 0.6], 'ec_hte_vs_ppci_bias_ratio': [0.15, 0.4]}
叙事方向：原始 framing 完全成立。"Debiasing can hurt" 作为 problem-level discovery 有足够 surprise value： 在 realistic 参数下 global correction 使 bias 恶化 5-10x，这是 NLP+CSS 社区未意识到的陷阱。 EC-HTE 以 250 expert labels 实现 near-oracle，HB partial pooling 的小样本优势可量化。 Diagnostic criterion 作为 standalone practical tool 给论文第三条独立贡献。 Real data 验证锁定了 "不只是理论上可能" 的叙事。投 EMNLP main 无需降级任何 claim。


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
tier: best
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
  "promptId": "4c8ced44-269c-4bdf-90be-70c94efa8f66",
  "type": "user",
  "uuid": "1c377e56-9763-4233-b3c1-2c858e7c0394",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T18:55:42.139Z_

```json
{
  "parentUuid": "1c377e56-9763-4233-b3c1-2c858e7c0394",
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
  "uuid": "059eed03-6f6c-4bcd-a943-60f590b7625b",
  "timestamp": "2026-05-20T18:55:42.139Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T18:55:42.139Z_

```json
{
  "parentUuid": "059eed03-6f6c-4bcd-a943-60f590b7625b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "9b00592f-e7ca-4899-8c40-b405d8eecc2c",
  "timestamp": "2026-05-20T18:55:42.139Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c",
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
  "aiTitle": "EC-HTE for LLM annotation debiasing: Phase 1 best-tier validation",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c"
}
```

---

### Assistant

_source line 7 · 2026-05-20T18:55:51.813Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each experiment in the experiment plan, under the "best" tier assumptions. I need to provide concrete metric predictions with rationales for why those results would occur under the best-case scenario defined in Phase 1.

Let me carefully go through each experiment and predict results that are consistent with the "best" tier definition:

Key metric ranges for "best":


- bias_amplification_factor_global_vs_uncorrected: [5.0, 12.0]
- ec_hte_absolute_cate_bias: [0.005, 0.02]
- ec_hte_coverage_90ci: [0.9, 0.97]
- min_n_expert_for_dominance: [100, 250]
- diagnostic_criterion_auroc: [0.9, 0.98]
- hb_vs_stratified_mle_bias_reduction: [0.3, 0.6]
- ec_hte_vs_ppci_bias_ratio: [0.15, 0.4]

Now I'm working through each experiment to assign specific predicted values within these ranges, selecting numbers that reflect realistic best-case performance while maintaining consistency across the different metrics and their underlying relationships.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9b00592f-e7ca-4899-8c40-b405d8eecc2c",
  "isSidechain": false,
  "requestId": "req_011CbEL6VGkQVk564xU8sAd3",
  "type": "assistant",
  "uuid": "8182c34a-69ad-4f22-b0d6-4edb106ae5fe",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4xvvj2bm3otPujtHD9X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9270,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9270,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9270
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

_source line 8 · 2026-05-20T19:00:20.639Z_

```yaml
tier: best
narrative_guidance: >
  三条 claims 全部在合理参数范围内得到强验证。Global correction 在 moderate heterogeneity 下产生 5-10x bias 放大，
  EC-HTE 以 250 expert labels 实现 near-oracle，diagnostic criterion AUROC > 0.9。
  Semi-synthetic 结果足够 dramatic 撑 headline，real data 验证锁定叙事。投 EMNLP main 无需降级任何 claim。

imagined_experiments:
  - name: "HB EC-HTE synthetic validation"
    plan_id: "exp-001"
    description: >
      HB Dirichlet-prior confusion matrix estimator + partial pooling，full regime sweep
      (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4)，1000 MC runs per cell。
    expected_results:
      # Extreme heterogeneity regime (Δ_miscls = 0.25, CATE_range = 0.15)
      extreme_k2_n250_abs_bias: 0.008
      extreme_k2_n250_coverage_90ci: 0.94
      extreme_k4_n250_abs_bias: 0.013
      extreme_k4_n250_coverage_90ci: 0.92
      # Moderate heterogeneity regime (Δ_miscls = 0.12, CATE_range = 0.08)
      moderate_k2_n250_abs_bias: 0.006
      moderate_k2_n250_coverage_90ci: 0.95
      moderate_k4_n250_abs_bias: 0.010
      moderate_k4_n250_coverage_90ci: 0.93
      # Homogeneous regime (Δ_miscls ≈ 0, control)
      homogeneous_k2_n250_abs_bias: 0.005
      homogeneous_k2_n250_coverage_90ci: 0.96
      # HB vs stratified MLE comparison at n_expert=250, k=4, extreme
      hb_bias_at_n250_k4: 0.013
      stratified_mle_bias_at_n250_k4: 0.031
      hb_vs_mle_bias_reduction_pct: 0.58
      # HB vs stratified MLE at n_expert=100, k=4 (small sample stress test)
      hb_bias_at_n100_k4: 0.018
      stratified_mle_bias_at_n100_k4: 0.052
      hb_vs_mle_bias_reduction_pct_n100: 0.65
      # HB vs global correction at n_expert=250, k=2, extreme
      global_correction_bias_at_n250_k2_extreme: 0.062
      ec_hte_bias_at_n250_k2_extreme: 0.008
    result_rationale: >
      HB partial pooling 在 best 档的核心优势来自两个机制：(1) Dirichlet 先验在小样本下自动将 subgroup-specific
      confusion matrix 向 global pooled estimate 收缩，避免了 stratified MLE 在 n/k 小时的高方差问题——
      当 n_expert=250, k=4 时每 subgroup 仅 ~63 个 label，MLE 估计的 confusion matrix 方差很大，
      而 HB 通过 hyperprior 借信息，bias 减少 ~58%；(2) 在 homogeneous regime 下 HB 自动退化为
      near-global 估计（收缩强），不会因为不必要的分层而增加方差。Coverage 在 0.92-0.96 范围是因为
      HB 的后验区间天然校准——PyMC 采样给出的 credible intervals 包含了参数不确定性传播。
      k=4 比 k=2 略差是因为每 subgroup 样本更少，但 partial pooling 缓冲了这个退化。
    tables:
      - caption: "Table 1: EC-HTE absolute CATE bias (×10³) across regimes, n_expert, and k"
        rows:
          - ["Regime", "k", "n=100", "n=250", "n=500", "n=1000", "n=2000"]
          - ["Extreme", "2", "12", "8", "6", "5", "5"]
          - ["Extreme", "4", "19", "13", "9", "7", "6"]
          - ["Moderate", "2", "9", "6", "5", "5", "5"]
          - ["Moderate", "4", "15", "10", "7", "6", "5"]
          - ["Homogeneous", "2", "7", "5", "5", "5", "5"]
          - ["Homogeneous", "4", "10", "7", "5", "5", "5"]
      - caption: "Table 2: HB vs Stratified MLE bias reduction (%) at varying n_expert, k=4, extreme regime"
        rows:
          - ["n_expert", "HB bias", "MLE bias", "Reduction %"]
          - ["100", "0.018", "0.052", "65%"]
          - ["250", "0.013", "0.031", "58%"]
          - ["500", "0.009", "0.018", "50%"]
          - ["1000", "0.007", "0.011", "36%"]
          - ["2000", "0.006", "0.008", "25%"]
    figures_description:
      - "Fig 1: Heatmap of |CATE bias| across (n_expert × regime) for HB vs MLE vs Global, k=4. HB column 整体蓝色(低 bias)，Global 列在 extreme/moderate 行呈红色。"
      - "Fig 2: Coverage probability vs n_expert 折线图，HB 线稳定在 0.92-0.96 带内，MLE 线在 n<500 时大幅下坠至 0.75-0.82。"
      - "Fig 3: Bias reduction (HB over MLE) vs n_expert 曲线，展示 partial pooling 优势随样本量增加而递减——经典 shrinkage 行为。"
    analysis: >
      关键发现：HB partial pooling 的优势集中在 n_expert ≤ 500 区间，且随 k 增大而更显著。
      这正好命中论文的核心场景——expert labels 昂贵，subgroup 数量不少。在 n=2000 时 HB 与 MLE 趋同，
      符合理论预期（数据充足时先验影响消退）。Global correction 在 heterogeneous regimes 下
      bias 是 EC-HTE 的 5-8x，直接支撑 Claim 1 的 "debiasing can hurt" 叙事。

  - name: "Formal bias bound verification"
    plan_id: "exp-002"
    description: >
      解析推导 bias = f(Δ_miscls, Δ_CATE) 的 closed-form bound，
      在二分类 × 两 subgroup 的 canonical case 下给出精确表达式，
      然后在系统参数网格上 MC 验证 bound tightness。
    expected_results:
      # Analytical bound: bias_global ≈ Δ_π × Δ_τ / (1 - π_avg) where Δ_π = FPR/FNR heterogeneity, Δ_τ = CATE heterogeneity
      bias_bound_form: "Δ_bias_global ≈ (Δ_FPR - Δ_FNR) × Δ_CATE / (1 - avg_error_rate)"
      # Constructive two-subgroup example
      example_subgroup_low_error_fpr: 0.05
      example_subgroup_high_error_fpr: 0.25
      example_pooled_fpr: 0.15
      example_cate_subgroup_low: 0.12
      example_cate_subgroup_high: 0.04
      example_uncorrected_bias_low_subgroup: 0.012
      example_global_corrected_bias_low_subgroup: 0.094
      bias_amplification_factor_constructive: 7.8
      # MC verification: bound tightness
      bound_covers_empirical_fraction: 0.97
      median_bound_tightness_ratio: 1.35
      # Parameter grid sweep results
      bias_amplification_range_moderate: [5.2, 8.1]
      bias_amplification_range_extreme: [7.5, 11.6]
      bias_amplification_at_homogeneous: [0.9, 1.1]
    result_rationale: >
      Bias 放大机制的直觉：global correction 用 pooled confusion matrix C_global 修正所有 subgroup。
      对于低错误率 subgroup g_low (FPR=0.05)，C_global 过估了其误分类率 (pooled FPR=0.15)，
      导致过度修正——将本来接近正确的 LLM label 分布往错误方向推。具体地，
      修正公式 p_corrected = C^{-1} × p_observed，当 C 比真实 C_g 差异大时，
      修正引入的 bias 正比于 (C_global - C_g) 作用在 subgroup 真实分布上。
      在两 subgroup case 下这退化为 Δ_FPR × Δ_CATE 的乘积形式。
      Amplification factor 7.8x 出现在 moderate 参数下 (Δ_FPR=0.20, Δ_CATE=0.08)，
      因为 uncorrected bias 仅来自 subgroup 自身的误分类（~0.012），而 global correction
      引入的跨 subgroup 信息污染远大于此。Homogeneous regime 下 amplification ≈ 1.0
      是因为 Δ_FPR ≈ 0 使得额外 bias 项消失。Bound tightness ratio 1.35 表示
      analytic bound 略保守（upper bound），覆盖 97% 的 MC realizations。
    tables:
      - caption: "Table 3: Bias amplification factor (global-corrected / uncorrected) across parameter grid"
        rows:
          - ["Δ_miscls \\ Δ_CATE", "0.04", "0.08", "0.12", "0.16"]
          - ["0.05", "2.1", "3.4", "4.8", "5.5"]
          - ["0.10", "3.8", "5.2", "7.1", "8.4"]
          - ["0.15", "5.1", "7.0", "9.2", "10.3"]
          - ["0.20", "5.9", "7.8", "10.1", "11.6"]
      - caption: "Table 4: Constructive two-subgroup example — debiasing hurts"
        rows:
          - ["Estimator", "Bias (g_low)", "Bias (g_high)", "Max |bias|"]
          - ["Uncorrected", "0.012", "0.038", "0.038"]
          - ["Global-corrected", "0.094", "0.021", "0.094"]
          - ["EC-HTE (oracle C_g)", "0.003", "0.005", "0.005"]
          - ["EC-HTE (HB, n=250)", "0.008", "0.011", "0.011"]
    figures_description:
      - "Fig 4: 3D surface plot — bias amplification factor as function of (Δ_miscls, Δ_CATE)，>5x 区域用红色标注，覆盖大部分 moderate-to-extreme 参数空间。"
      - "Fig 5: 两 subgroup 的 bias decomposition bar chart：uncorrected vs global-corrected，显示 g_low 在 global correction 后 bias 从 0.012 跳到 0.094。这是论文 Figure 1 的候选——一目了然的 'debiasing can hurt' 证据。"
      - "Fig 6: Bound tightness Q-Q plot — analytic bound vs MC empirical bias，点沿 45° 线分布但略偏上方，确认 bound 为 tight upper bound。"
    analysis: >
      这个实验提供 Claim 1 的理论基础。Amplification factor 在 5-12 范围精确落入 best 档指标。
      关键叙事：即使 Δ_miscls 仅 0.10 (moderate)，只要 Δ_CATE 也有 0.08，amplification 就达 5.2x。
      这说明 "debiasing can hurt" 不需要极端参数，在 NLP+CSS 社区的 typical 使用场景下就会发生。
      两 subgroup constructive example 直接进论文 Section 3 作为 Proposition 1 的证明。

  - name: "Semi-synthetic benchmark (GPT-4.1 + Qwen3)"
    plan_id: "exp-003"
    description: >
      使用公开政治推文语料（CardiffNLP TweetEval stance subset 或 LIAR 数据集），
      注入 known CATE heterogeneity 结构，用 GPT-4.1 和 Qwen3-235B 标注，
      测量 subgroup-specific misclassification rates，应用 EC-HTE vs baselines。
    expected_results:
      # LLM annotation quality & heterogeneity (measured)
      gpt41_overall_accuracy: 0.82
      gpt41_subgroup_accuracy_range: [0.74, 0.91]
      gpt41_delta_miscls: 0.14
      qwen3_overall_accuracy: 0.76
      qwen3_subgroup_accuracy_range: [0.65, 0.87]
      qwen3_delta_miscls: 0.19
      # Injected ground truth
      true_cate_range: [0.02, 0.14]
      true_delta_cate: 0.10
      n_total_tweets: 12000
      k_subgroups: 4
      n_expert_labels: 250
      # EC-HTE results
      ec_hte_max_abs_cate_bias_gpt41: 0.011
      ec_hte_avg_abs_cate_bias_gpt41: 0.008
      ec_hte_coverage_90ci_gpt41: 0.93
      ec_hte_max_abs_cate_bias_qwen3: 0.016
      ec_hte_avg_abs_cate_bias_qwen3: 0.012
      ec_hte_coverage_90ci_qwen3: 0.91
      # Baseline results — Global correction
      global_max_abs_cate_bias_gpt41: 0.068
      global_avg_abs_cate_bias_gpt41: 0.043
      global_coverage_90ci_gpt41: 0.52
      global_max_abs_cate_bias_qwen3: 0.089
      global_avg_abs_cate_bias_qwen3: 0.061
      global_coverage_90ci_qwen3: 0.38
      # Baseline results — Uncorrected
      uncorrected_max_abs_cate_bias_gpt41: 0.032
      uncorrected_avg_abs_cate_bias_gpt41: 0.021
      # Baseline results — PPCI
      ppci_max_abs_cate_bias_gpt41: 0.048
      ppci_avg_abs_cate_bias_gpt41: 0.033
      ec_hte_vs_ppci_bias_ratio_gpt41: 0.24
      # Bias amplification factor
      bias_amplification_global_vs_uncorrected_gpt41: 6.8
      bias_amplification_global_vs_uncorrected_qwen3: 8.2
      # Headline number
      worst_subgroup_amplification_gpt41: 7.8
    result_rationale: >
      Semi-synthetic 的核心设计：真实推文提供 realistic text distribution，LLM 标注误差是真实的
      （不是模拟的），CATE 结构是注入的（已知 ground truth）。GPT-4.1 在政治文本分类上 overall 82%
      准确率是合理的（political stance 是 known hard task），但关键是 subgroup 间差异大——
      涉及 informal language/slang 的推文 (如 youth-oriented political content) 错误率显著高于
      formal policy discussion。这种 heterogeneity 是 LLM 的已知特征，不需要人为制造。
      Qwen3 作为 open-weight model 整体弱于 GPT-4.1，且 heterogeneity 更大 (Δ=0.19 vs 0.14)，
      因为其 training data 对英文政治文本的覆盖不如 GPT-4.1 均匀。
      Global correction 在 GPT-4.1 上产生 6.8x amplification 是因为：pooled confusion matrix
      混合了 low-error formal subgroup 和 high-error informal subgroup 的误差率，
      对 formal subgroup 过度修正，直接将 bias 从 0.032 推到 0.068。
      EC-HTE 的 0.011 max bias 来自 HB 在 250 labels / 4 subgroups 下仍有限的估计精度，
      但已接近 oracle（~0.005）。Coverage 93% 在 90% nominal 之上，
      说明 HB posterior 的 uncertainty quantification 略保守但正确。
      PPCI 表现介于 global 和 EC-HTE 之间：它做了 localized correction 但不是针对 covariate-side
      measurement error 设计的，所以 kernel localization 只部分捕获了 subgroup 结构。
    tables:
      - caption: "Table 5: CATE estimation accuracy on semi-synthetic benchmark (GPT-4.1 annotations)"
        rows:
          - ["Method", "Max |bias|", "Avg |bias|", "Coverage 90%", "RMSE"]
          - ["Uncorrected", "0.032", "0.021", "0.71", "0.028"]
          - ["Global correction", "0.068", "0.043", "0.52", "0.051"]
          - ["DSL (Egami 2024)", "0.059", "0.038", "0.58", "0.045"]
          - ["PPCI (Sui 2026)", "0.048", "0.033", "0.64", "0.039"]
          - ["Stratified MLE", "0.022", "0.016", "0.82", "0.024"]
          - ["EC-HTE (HB, n=250)", "0.011", "0.008", "0.93", "0.014"]
          - ["Oracle (true C_g)", "0.005", "0.003", "0.95", "0.009"]
      - caption: "Table 6: Same benchmark, Qwen3-235B annotations"
        rows:
          - ["Method", "Max |bias|", "Avg |bias|", "Coverage 90%", "RMSE"]
          - ["Uncorrected", "0.041", "0.029", "0.63", "0.036"]
          - ["Global correction", "0.089", "0.061", "0.38", "0.072"]
          - ["PPCI (Sui 2026)", "0.062", "0.044", "0.55", "0.051"]
          - ["EC-HTE (HB, n=250)", "0.016", "0.012", "0.91", "0.019"]
          - ["Oracle (true C_g)", "0.006", "0.004", "0.94", "0.010"]
      - caption: "Table 7: Measured LLM misclassification heterogeneity by subgroup"
        rows:
          - ["Subgroup", "GPT-4.1 Acc", "Qwen3 Acc", "True CATE"]
          - ["Formal policy", "0.91", "0.87", "0.04"]
          - ["News commentary", "0.85", "0.79", "0.08"]
          - ["Informal opinion", "0.79", "0.72", "0.11"]
          - ["Youth slang/meme", "0.74", "0.65", "0.14"]
    figures_description:
      - "Fig 7 (论文 Figure 2 候选): Subgroup-level CATE estimates with 90% CI，四个 panel 对应四个 subgroup。每个 panel 内横向排列 methods (Uncorrected, Global, PPCI, EC-HTE, Oracle)，纵轴为 CATE。True CATE 用水平虚线标注。Global correction 在 Formal policy subgroup 的 CI 明显偏离 truth，EC-HTE 紧贴。"
      - "Fig 8: Bias amplification heatmap — rows = subgroups, columns = methods, cell color = |bias| / |uncorrected bias|。Global correction 行颜色深（amplification），EC-HTE 行颜色浅（reduction）。"
      - "Fig 9: GPT-4.1 vs Qwen3 misclassification rate by subgroup 对比 bar chart，展示 Qwen3 的 heterogeneity 更大。"
    analysis: >
      这是论文的核心实证。Headline number: "global correction worsens subgroup CATE bias by up to
      7.8x; EC-HTE reduces bias to near-zero with 250 expert labels" 直接来自此表。
      GPT-4.1 和 Qwen3 两个 LLM 提供了 generalizability：即使 LLM 质量差异大，
      EC-HTE 的优势一致。PPCI 表现合理但不如 EC-HTE，因为它不是为 covariate-side error 设计的——
      这精确支撑了 "orthogonal problems" 的 differentiation 论点。
      Coverage 数据尤其重要：global correction 的 52% coverage 意味着研究者会大量产生
      false-positive heterogeneity findings，这是一个严重的实践问题。

  - name: "Real-data validation (Ashwin et al. 2025)"
    plan_id: "exp-004"
    description: >
      在 Ashwin et al. (2025) Rohingya 难民访谈数据集上应用 EC-HTE。
      LLM 标注误差已知与 refugee status, gender, education 相关。
      若原始数据不可获取，使用 Afrobarometer survey 数据作为替代。
    expected_results:
      # Data characteristics (from Ashwin et al. paper description)
      n_interviews: 4200
      n_expert_coded: 800
      k_subgroups_by_education: 3
      k_subgroups_by_gender: 2
      # Measured LLM misclassification heterogeneity
      llm_accuracy_high_education: 0.88
      llm_accuracy_low_education: 0.71
      delta_miscls_education: 0.17
      llm_accuracy_male: 0.82
      llm_accuracy_female: 0.76
      delta_miscls_gender: 0.06
      # CATE results (education subgroups — higher heterogeneity)
      uncorrected_cate_bias_range_education: [0.015, 0.045]
      global_corrected_cate_bias_range_education: [0.028, 0.082]
      ec_hte_cate_bias_range_education: [0.006, 0.018]
      bias_amplification_global_education: 5.4
      ec_hte_coverage_90ci_education: 0.92
      # CATE results (gender subgroups — lower heterogeneity)
      bias_amplification_global_gender: 2.1
      ec_hte_improvement_over_global_gender: 0.35
      # Diagnostic criterion
      diagnostic_product_education: 0.017
      diagnostic_product_gender: 0.005
      diagnostic_correctly_flags_education: true
      diagnostic_correctly_ignores_gender: true
    result_rationale: >
      Ashwin et al. 的数据特别适合验证我们的理论，因为他们已经 documented 了 LLM 误差与
      受访者特征的相关性。Education 维度的 heterogeneity (Δ=0.17) 落入 moderate-to-high 范围：
      低教育程度受访者的回答更口语化、更短、更多使用方言，导致 LLM 理解困难。
      Gender 维度的 heterogeneity 较小 (Δ=0.06)，因为性别对语言风格的影响不如教育程度直接。
      这提供了一个自然的 positive/negative control：education 分层应该触发 diagnostic criterion
      （product = 0.17 × 0.10 = 0.017 > threshold），而 gender 分层不应该 (product = 0.06 × 0.08 = 0.005 < threshold)。
      Bias amplification 5.4x 比 semi-synthetic 的 7.8x 低，因为 real data 的 CATE heterogeneity
      可能不如注入的那么 dramatic，但仍然在 best 档的 [5.0, 12.0] 范围内。
      EC-HTE 的表现略弱于 semi-synthetic (bias 上限 0.018 vs 0.011)，因为 real data
      的 subgroup 结构不完美——受访者特征是 proxy，不是 true latent subgroup。
    tables:
      - caption: "Table 8: CATE estimation on Ashwin et al. refugee data (education subgroups)"
        rows:
          - ["Method", "Max |bias|", "Avg |bias|", "Coverage 90%"]
          - ["Uncorrected", "0.045", "0.028", "0.68"]
          - ["Global correction", "0.082", "0.052", "0.47"]
          - ["EC-HTE (HB)", "0.018", "0.011", "0.92"]
      - caption: "Table 9: Diagnostic criterion on real data"
        rows:
          - ["Subgroup Dim", "Δ_miscls", "Δ_CATE", "Product", "Flag?", "Correct?"]
          - ["Education (3-level)", "0.17", "0.10", "0.017", "Yes", "Yes"]
          - ["Gender (2-level)", "0.06", "0.08", "0.005", "No", "Yes"]
    figures_description:
      - "Fig 10: Real-data CATE estimates by education level — 三层 (low/mid/high education) 的 point estimates + 90% CI。Global correction 在 high-education group 严重 over-corrects (估计值远离 ground truth 方向)。"
      - "Fig 11: LLM confusion matrix heatmap by education subgroup — 可视化误分类 pattern 随教育程度的变化，low-education 的 off-diagonal 明显更大。"
    analysis: >
      Real data 验证的核心价值：(1) 证明 misclassification heterogeneity 在真实社会科学数据中
      自然存在且量级足够触发问题；(2) education vs gender 的对比展示 diagnostic criterion 的
      实用性——不是所有 subgroup 变量都需要 stratified correction；(3) 即使在 noisy real-world
      条件下 EC-HTE 仍显著优于 global correction。这锁定了 "不只是理论上可能" 的叙事。

  - name: "Diagnostic criterion validation"
    plan_id: "exp-005"
    description: >
      在 exp-001 (synthetic) 和 exp-003 (semi-synthetic) 的所有实验设定上
      计算 misclass_heterogeneity × CATE_heterogeneity 乘积，
      以 "global correction 是否有害" 为 binary label 做 ROC 分析。
    expected_results:
      # ROC performance
      auroc_synthetic: 0.96
      auroc_semisynthetic: 0.93
      auroc_combined: 0.95
      # Threshold analysis
      optimal_threshold_youden: 0.008
      threshold_sensitivity: 0.93
      threshold_specificity: 0.91
      # Cross-dataset stability
      threshold_from_synthetic_applied_to_semisynthetic_auroc: 0.91
      threshold_from_semisynthetic_applied_to_synthetic_auroc: 0.94
      threshold_stability_range: [0.006, 0.010]
      # Edge cases
      false_negative_rate_at_optimal: 0.07
      false_positive_rate_at_optimal: 0.09
      false_negatives_characterization: "borderline cases with moderate Δ_miscls but low Δ_CATE"
    result_rationale: >
      Diagnostic criterion AUROC 0.95 的高判别力来自 bias 放大机制的 multiplicative 结构：
      当 Δ_miscls × Δ_CATE > threshold 时，global correction 引入的额外 bias 近似正比于
      这个乘积（exp-002 的解析结果），而当乘积为 0（任一因子为 0）时额外 bias 消失。
      这种 sharp transition 天然产生高 AUROC。Synthetic 上 AUROC 略高于 semi-synthetic
      是因为 synthetic 的 subgroup 结构更 clean。Cross-dataset threshold stability
      ([0.006, 0.010]) 表示从一个 dataset 学到的 threshold 可以 transfer，
      因为 underlying mechanism 是 parameter-free 的（不依赖具体的 confusion matrix 形状，
      只依赖 heterogeneity 的量级）。7% false negative rate 出现在 borderline cases
      （乘积 ≈ threshold），这些 case 中 global correction 只 mildly harmful，
      所以 miss 的实际影响小。
    tables:
      - caption: "Table 10: Diagnostic criterion ROC performance"
        rows:
          - ["Dataset", "AUROC", "Optimal Threshold", "Sensitivity", "Specificity"]
          - ["Synthetic (1000 MC settings)", "0.96", "0.008", "0.94", "0.92"]
          - ["Semi-synthetic (GPT-4.1)", "0.93", "0.009", "0.91", "0.89"]
          - ["Semi-synthetic (Qwen3)", "0.94", "0.008", "0.92", "0.90"]
          - ["Combined", "0.95", "0.008", "0.93", "0.91"]
      - caption: "Table 11: Cross-dataset threshold transfer"
        rows:
          - ["Train on", "Test on", "AUROC", "Sensitivity"]
          - ["Synthetic", "Semi-synthetic (GPT-4.1)", "0.91", "0.89"]
          - ["Synthetic", "Semi-synthetic (Qwen3)", "0.92", "0.90"]
          - ["Semi-synthetic", "Synthetic", "0.94", "0.92"]
          - ["Ashwin real data", "Synthetic", "0.90", "0.88"]
    figures_description:
      - "Fig 12 (论文 Figure 3 候选): ROC curve，三条线 (synthetic, semi-synthetic, combined) 近乎重叠，AUC 标注在图例中。对角虚线作为 reference。"
      - "Fig 13: Scatter plot — x 轴 = diagnostic product (Δ_miscls × Δ_CATE), y 轴 = bias amplification factor。点按 dataset 着色。清晰的 monotonic relationship，vertical line 标注 threshold = 0.008。"
      - "Fig 14: Threshold sensitivity analysis — x 轴 = threshold value, 双 y 轴 = sensitivity (蓝) + specificity (红)。两条线交叉点 ≈ 0.008，对应 Youden index 最优。"
    analysis: >
      Diagnostic criterion 作为 Claim 3 的独立贡献，其价值在于 actionability：
      研究者标注 200-300 个 pilot samples，计算 subgroup-specific confusion matrices，
      算出 diagnostic product，查 threshold 即可决定是否需要 stratified correction。
      Cross-dataset stability 是关键——如果 threshold 不稳定则实用价值大减。
      [0.006, 0.010] 的窄范围说明 mechanism-driven threshold 可以 generalize。

  - name: "Expert label budget sensitivity"
    plan_id: "exp-006"
    description: >
      系统 sweep n_expert ∈ {50, 100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8}，
      找 EC-HTE > Global 的 crossover point，验证 HB partial pooling 在小 n 下的价值。
    expected_results:
      # Crossover points (n where EC-HTE first beats Global)
      crossover_n_k2_extreme: 75
      crossover_n_k4_extreme: 120
      crossover_n_k8_extreme: 200
      crossover_n_k2_moderate: 100
      crossover_n_k4_moderate: 180
      crossover_n_k8_moderate: 350
      # EC-HTE at minimum budget (n=50)
      ec_hte_bias_n50_k2: 0.022
      ec_hte_bias_n50_k4: 0.035
      ec_hte_bias_n50_k8: 0.058
      ec_hte_coverage_n50_k2: 0.88
      ec_hte_coverage_n50_k4: 0.79
      ec_hte_coverage_n50_k8: 0.65
      # HB vs MLE gap at small n
      hb_vs_mle_bias_ratio_n100_k4: 0.42
      hb_vs_mle_bias_ratio_n100_k8: 0.35
      hb_vs_mle_bias_ratio_n250_k4: 0.52
      hb_vs_mle_bias_ratio_n1000_k4: 0.78
      # Diminishing returns threshold
      n_for_90pct_oracle_perf_k4: 500
      n_for_95pct_oracle_perf_k4: 1000
    result_rationale: >
      Crossover point 在 k=4 时约 n=120-180 是因为 EC-HTE 只需要每 subgroup ~30-45 个 labels
      就能估出比 pooled CM 更准的 subgroup CM——HB 先验在此处发挥最大作用，
      将极端的 MLE 估计 (基于 <30 samples 的 subgroup) shrink 向 global 估计。
      k=8 时 crossover 推后到 200-350 因为每 subgroup 样本降至 ~25-44，
      HB 需要更多数据才能区分 subgroup-specific signal 和 noise。
      n=50 时 k=8 的 coverage 只有 65%——此时每 subgroup 仅 6 个 labels，
      即使 HB 也救不了，posterior 过度依赖先验而非数据。
      HB vs MLE gap 随 n 增大而缩小 (ratio 从 0.35 → 0.78) 是经典 shrinkage 行为：
      数据量大时 MLE 自身就 consistent，先验的边际贡献递减。
      min_n_expert_for_dominance 在 k=4 moderate regime 下为 180，落入 best 档的 [100, 250]。
    tables:
      - caption: "Table 12: Crossover n_expert (EC-HTE first outperforms Global) by k and regime"
        rows:
          - ["k \\ Regime", "Extreme", "Moderate", "Homogeneous"]
          - ["2", "75", "100", "N/A (Global ≈ EC-HTE)"]
          - ["4", "120", "180", "N/A"]
          - ["8", "200", "350", "N/A"]
      - caption: "Table 13: HB partial pooling advantage — bias ratio (HB/MLE) at k=4"
        rows:
          - ["n_expert", "HB |bias|", "MLE |bias|", "Ratio", "HB advantage"]
          - ["50", "0.035", "0.089", "0.39", "61%"]
          - ["100", "0.019", "0.045", "0.42", "58%"]
          - ["250", "0.013", "0.025", "0.52", "48%"]
          - ["500", "0.009", "0.015", "0.60", "40%"]
          - ["1000", "0.007", "0.009", "0.78", "22%"]
          - ["2000", "0.006", "0.007", "0.86", "14%"]
    figures_description:
      - "Fig 15 (论文 Figure 4 候选): Bias vs n_expert 折线图，k=4 panel。四条线: Global (flat, high), MLE (decreasing steeply), HB (decreasing gently from lower start), Oracle (flat, low)。HB-MLE gap 在 n=100-500 区间最显著。"
      - "Fig 16: Coverage vs n_expert heatmap, rows = k ∈ {2,4,8}, 颜色 = coverage。k=8, n<100 区域为红色 (under-coverage), k=2 几乎全绿。"
      - "Fig 17: Crossover point visualization — n_expert vs k 的 phase diagram，shaded region = 'EC-HTE dominates', boundary line 清晰标注。"
    analysis: >
      这个实验为论文的 practical advice 提供基础：n_expert=250 是 sweet spot，
      在 k≤4 的 typical 设定下已经足够。n=100 时 HB 的优势最大 (58% bias reduction over MLE)，
      这直接回应 reviewer concern #5 (expert label cost)。
      k=8 的结果也重要——它设定了方法的适用边界，诚实地展示 limitations。

  - name: "PPCI baseline comparison"
    plan_id: "exp-007"
    description: >
      实现 PPCI (Sui et al., 2026) kernel-based conditional correction，
      在 exp-001 synthetic 和 exp-003 semi-synthetic 的相同 benchmark 上对比。
    expected_results:
      # Synthetic benchmark (extreme regime, k=4, n=250)
      ppci_abs_bias_synthetic_extreme: 0.038
      ec_hte_abs_bias_synthetic_extreme: 0.013
      ec_hte_vs_ppci_ratio_synthetic: 0.34
      ppci_coverage_synthetic: 0.72
      # Semi-synthetic GPT-4.1
      ppci_abs_bias_semi_gpt41: 0.033
      ec_hte_abs_bias_semi_gpt41: 0.008
      ec_hte_vs_ppci_ratio_semi: 0.24
      ppci_coverage_semi_gpt41: 0.64
      # Semi-synthetic Qwen3
      ppci_abs_bias_semi_qwen3: 0.044
      ec_hte_abs_bias_semi_qwen3: 0.012
      ec_hte_vs_ppci_ratio_qwen3: 0.27
      ppci_coverage_semi_qwen3: 0.55
      # PPCI strength: outcome-side error
      ppci_better_on_outcome_error_scenario: true
      outcome_error_ppci_bias: 0.009
      outcome_error_ec_hte_bias: 0.015
    result_rationale: >
      PPCI 设计目标是 outcome-side measurement error 的 conditional correction，
      其 kernel localization 在 covariate space 做 local bandwidth selection。
      当问题是 covariate-side error (我们的设定) 时，PPCI 的 kernel 在 mismeasured covariate 上
      做 smoothing，但这只能部分恢复 subgroup 结构——kernel bandwidth 太大则退化为 global，
      太小则方差爆炸。结果是 PPCI 表现介于 global 和 EC-HTE 之间。
      EC-HTE/PPCI ratio 在 0.24-0.34 范围 (best 档 [0.15, 0.4]) 是因为 EC-HTE 精确建模了
      问题结构 (subgroup-specific confusion matrices)，而 PPCI 用 generic nonparametric smoothing
      近似这个结构。在 outcome-side error 场景下 PPCI 反而优于 EC-HTE——这是公平呈现，
      也强化了 "orthogonal problems, complementary solutions" 的论点。
    tables:
      - caption: "Table 14: EC-HTE vs PPCI head-to-head comparison"
        rows:
          - ["Setting", "EC-HTE |bias|", "PPCI |bias|", "Ratio", "EC-HTE Coverage", "PPCI Coverage"]
          - ["Synthetic extreme k=4", "0.013", "0.038", "0.34", "0.92", "0.72"]
          - ["Semi-synth GPT-4.1", "0.008", "0.033", "0.24", "0.93", "0.64"]
          - ["Semi-synth Qwen3", "0.012", "0.044", "0.27", "0.91", "0.55"]
          - ["Outcome-error scenario", "0.015", "0.009", "1.67", "0.91", "0.93"]
    figures_description:
      - "Fig 18: EC-HTE vs PPCI paired comparison — scatter plot，每个点 = 一个实验设定，x = PPCI bias, y = EC-HTE bias。所有 covariate-error 点在对角线下方 (EC-HTE wins)，outcome-error 点在上方 (PPCI wins)。"
      - "Fig 19: Method taxonomy diagram — 2×2 grid (covariate vs outcome error × average vs conditional)，标注每个方法的适用区域。EC-HTE 占 covariate × conditional cell，PPCI 占 outcome × conditional cell。"
    analysis: >
      PPCI 对比是回应 reviewer concern #2 的关键实验。结果清晰展示两个方法解决不同问题：
      EC-HTE 在 covariate-side error 下 bias 仅为 PPCI 的 24-34%，但在 outcome-side error
      下 PPCI 更优。这不是 "我们更好" 而是 "我们解决不同问题"，更有说服力。

  - name: "Multiple LLM annotator comparison"
    plan_id: "exp-008"
    description: >
      GPT-4.1 vs Qwen3-235B vs Claude Sonnet 4.6，测量 misclassification heterogeneity patterns，
      展示 EC-HTE benefit 随 LLM 质量变化。
    expected_results:
      # Per-LLM misclassification heterogeneity
      gpt41_overall_acc: 0.82
      gpt41_delta_miscls: 0.14
      gpt41_heterogeneity_pattern: "accuracy drops on informal/slang text"
      qwen3_overall_acc: 0.76
      qwen3_delta_miscls: 0.19
      qwen3_heterogeneity_pattern: "larger drop on informal text + non-English code-switch"
      claude_sonnet_overall_acc: 0.85
      claude_sonnet_delta_miscls: 0.11
      claude_sonnet_heterogeneity_pattern: "most uniform, slight drop on very short tweets"
      # EC-HTE benefit by LLM
      ec_hte_bias_reduction_vs_global_gpt41: 0.84
      ec_hte_bias_reduction_vs_global_qwen3: 0.87
      ec_hte_bias_reduction_vs_global_claude: 0.79
      # Correlation: heterogeneity → EC-HTE benefit
      correlation_delta_miscls_vs_benefit: 0.91
      # Key finding: even best LLM needs correction
      claude_global_correction_bias_amplification: 4.2
      claude_ec_hte_still_needed: true
    result_rationale: >
      三个 LLM 的 heterogeneity pattern 差异反映 training data 和 architecture 差异：
      GPT-4.1 在 formal 文本上强但 informal text 下降明显；Qwen3 作为 open-weight model
      整体弱且 code-switching 处理差；Claude Sonnet 最均匀但仍有 heterogeneity。
      EC-HTE benefit 与 Δ_miscls 强相关 (r=0.91) 正是理论预测：
      bias 放大正比于 heterogeneity，correction 的价值也正比于 heterogeneity。
      即使 best LLM (Claude, Δ=0.11) 的 global correction 仍有 4.2x amplification，
      说明这不是 "只有差的 LLM 才有这个问题"——这强化了论文的普适性论点。
    tables:
      - caption: "Table 15: LLM annotator comparison on semi-synthetic benchmark"
        rows:
          - ["LLM", "Overall Acc", "Δ_miscls", "Global Amplification", "EC-HTE |bias|", "EC-HTE Reduction"]
          - ["Qwen3-235B", "0.76", "0.19", "8.2x", "0.012", "87%"]
          - ["GPT-4.1", "0.82", "0.14", "6.8x", "0.008", "84%"]
          - ["Claude Sonnet 4.6", "0.85", "0.11", "4.2x", "0.010", "79%"]
    figures_description:
      - "Fig 20: 三 LLM 的 subgroup accuracy profile radar chart / parallel coordinates plot。"
      - "Fig 21: EC-HTE benefit vs LLM heterogeneity scatter — 三个点 + regression line，r=0.91。"
    analysis: >
      多 LLM 对比强化了 generalizability：不同 LLM 有不同的 error pattern，
      但 EC-HTE 一致有效。Claude Sonnet 的结果特别有说服力——即使最强最均匀的 LLM
      仍需要 stratified correction，说明这是一个 structural 问题而非 LLM 质量问题。

  - name: "Adaptive expert annotation allocation"
    plan_id: "exp-009"
    description: >
      实现 CATE-weighted allocation (高 CATE × 高 error subgroups 分配更多 expert labels)，
      与 uniform 和 uncertainty-only allocation 对比。
    expected_results:
      # Allocation strategies at n_total=250, k=4
      uniform_per_subgroup: [63, 63, 63, 63]
      uncertainty_allocation: [40, 50, 70, 90]
      cate_weighted_allocation: [30, 45, 80, 95]
      # Bias comparison
      uniform_avg_bias: 0.013
      uncertainty_avg_bias: 0.011
      cate_weighted_avg_bias: 0.009
      # Efficiency gain
      cate_weighted_vs_uniform_equivalent_n: 180
      efficiency_gain_pct: 28
      # At reduced budget n=150
      uniform_n150_bias: 0.019
      cate_weighted_n150_bias: 0.012
    result_rationale: >
      CATE-weighted allocation 的逻辑：overall estimation error 是各 subgroup error 的
      CATE-weighted sum，因此高 CATE subgroup 的 confusion matrix 估计精度更重要。
      同时，高 error subgroup 的 confusion matrix 估计需要更多 samples (因为 off-diagonal
      元素更大，Dirichlet posterior 的 effective sample size 分散到更多 cells)。
      两者乘积给出最优分配。28% efficiency gain 意味着 CATE-weighted 用 180 个 labels
      达到 uniform 250 个的效果——这是一个 practical 且 implementable 的改进。
    tables:
      - caption: "Table 16: Expert allocation strategies comparison (n=250, k=4, extreme regime)"
        rows:
          - ["Strategy", "Avg |bias|", "Max |bias|", "Coverage 90%", "Equivalent uniform n"]
          - ["Uniform", "0.013", "0.019", "0.92", "250 (baseline)"]
          - ["Uncertainty-only", "0.011", "0.016", "0.93", "210"]
          - ["CATE-weighted", "0.009", "0.013", "0.94", "180"]
    figures_description:
      - "Fig 22: Allocation visualization — stacked bar chart 展示三种策略在 4 个 subgroups 上的 label 分配。"
      - "Fig 23: Bias vs n_expert 曲线，三种策略分别画线，CATE-weighted 在所有 n 下最优。"
    analysis: >
      P2 优先级但结果 clean。28% efficiency gain 足够进论文但不改变 main story。
      适合放 Section 5.3 或 Appendix，作为 practical extension。

  - name: "Robustness to misspecified subgroups"
    plan_id: "exp-010"
    description: >
      测试 EC-HTE 在 subgroup 定义 noisy 或与 true structure 不对齐时的表现。
      HB partial pooling 应自动 shrink 向 global estimate。
    expected_results:
      # Scenario 1: noisy subgroup labels (10% random flip)
      clean_subgroup_ec_hte_bias: 0.013
      noisy_10pct_ec_hte_bias: 0.017
      noisy_10pct_global_bias: 0.041
      degradation_from_noise_pct: 31
      # Scenario 2: 50% random subgroup labels (near useless)
      noisy_50pct_ec_hte_bias: 0.024
      noisy_50pct_global_bias: 0.038
      ec_hte_still_better_at_50pct: true
      # Scenario 3: misaligned subgroups (4 defined, true structure is 2)
      misaligned_ec_hte_bias: 0.015
      misaligned_mle_stratified_bias: 0.028
      hb_graceful_degradation: true
      # Scenario 4: continuous subgroup variable discretized
      continuous_discretized_3bins_bias: 0.014
      continuous_discretized_6bins_bias: 0.016
      continuous_discretized_12bins_bias: 0.022
    result_rationale: >
      HB partial pooling 的 robustness 来自 shrinkage 机制：当 subgroup 信号弱（noisy labels
      或 misaligned structure），subgroup-specific posteriors 被 hyperprior 拉向 global estimate，
      自动实现 bias-variance tradeoff。10% noise 只导致 31% 性能退化（0.013 → 0.017），
      因为 HB 将 noisy subgroups 的估计 shrink 向 pooled，有效地 denoise。
      即使 50% random (near-meaningless subgroups)，EC-HTE 仍优于 global，
      因为 HB 退化为接近 global 但不会比 global 差——worst case 是 not stratifying。
      Misaligned subgroups (定义 4 个但 true structure 是 2 个) 场景下，
      MLE 在 4 个 subgroup 上分别估计导致高方差，而 HB 将相似的 subgroup 估计 shrink 在一起。
      Continuous 变量离散化时，bin 数过多 (12) 导致性能退化但仍可接受——
      这给出 practical guidance: 不要过度分层。
    tables:
      - caption: "Table 17: Robustness analysis — EC-HTE under subgroup misspecification"
        rows:
          - ["Scenario", "EC-HTE |bias|", "Global |bias|", "Stratified MLE |bias|", "EC-HTE still best?"]
          - ["Clean subgroups", "0.013", "0.043", "0.031", "Yes"]
          - ["10% noisy labels", "0.017", "0.041", "0.039", "Yes"]
          - ["50% noisy labels", "0.024", "0.038", "0.061", "Yes"]
          - ["Misaligned (4 def, 2 true)", "0.015", "0.043", "0.028", "Yes"]
          - ["Continuous → 3 bins", "0.014", "0.043", "0.025", "Yes"]
          - ["Continuous → 12 bins", "0.022", "0.043", "0.048", "Yes"]
    figures_description:
      - "Fig 24: Robustness profile plot — x 轴 = noise level (0% to 50%), y 轴 = |bias|，三条线 (EC-HTE, Global, MLE)。EC-HTE gracefully degrades, MLE degrades faster, Global is flat (unaffected by subgroup noise since it ignores subgroups)。"
    analysis: >
      直接回应 reviewer concern #4 (sensitivity to subgroup definition)。
      核心 takeaway: EC-HTE never does worse than global correction，即使 subgroup 定义完全错误。
      这消除了 "如果 subgroup 选错了怎么办" 的顾虑。HB 的 automatic shrinkage 是关键卖点。

  - name: "Causal forest leaf-level integration"
    plan_id: "exp-011"
    description: >
      将 EC-HTE correction 集成到 CausalForestDML leaf level：
      corrected pseudo-outcomes + variance-adjusted CIs，对比 naive forest。
    expected_results:
      # Forest-level CATE estimation
      naive_forest_avg_bias: 0.035
      ec_hte_forest_avg_bias: 0.010
      ec_hte_forest_coverage: 0.92
      naive_forest_coverage: 0.61
      # Heterogeneity detection
      naive_forest_het_test_power: 0.45
      ec_hte_forest_het_test_power: 0.88
      # Subgroup ranking
      naive_forest_subgroup_rank_correlation: 0.72
      ec_hte_forest_subgroup_rank_correlation: 0.96
    result_rationale: >
      Naive causal forest 用 mismeasured covariate 做 splitting，
      导致 (1) splits 不对齐 true subgroup boundaries，(2) leaf-level treatment effect
      估计被 misclassification 污染。EC-HTE forest 用 corrected pseudo-outcomes
      使得每个 leaf 的 treatment effect 是 debiased 的，同时 variance adjustment
      给出 honest CIs。Heterogeneity test power 从 0.45 提升到 0.88 是因为
      naive forest 的 leaf effects 被 measurement error attenuated——
      heterogeneity signal 被 noise 淹没。Subgroup ranking 的 rank correlation
      从 0.72 到 0.96 表示 EC-HTE forest 几乎完美恢复了 true effect ordering。
    tables:
      - caption: "Table 18: Causal forest integration results"
        rows:
          - ["Metric", "Naive Forest", "EC-HTE Forest", "Oracle Forest"]
          - ["Avg |CATE bias|", "0.035", "0.010", "0.006"]
          - ["Coverage 90% CI", "0.61", "0.92", "0.95"]
          - ["Het. test power", "0.45", "0.88", "0.94"]
          - ["Subgroup rank τ", "0.72", "0.96", "1.00"]
    figures_description:
      - "Fig 25: CATE heterogeneity heatmap — true vs estimated by naive forest vs EC-HTE forest。Naive 版本 washed out (heterogeneity attenuated)，EC-HTE 版本接近 true。"
    analysis: >
      P2 但支撑 method section 的 completeness。Heterogeneity test power 的提升 (0.45 → 0.88)
      是一个 compelling 数字——意味着 naive approach 会 miss 超过一半的 true heterogeneity。
      适合论文 Section 5.2 或 Appendix。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8182c34a-69ad-4f22-b0d6-4edb106ae5fe",
  "isSidechain": false,
  "requestId": "req_011CbEL6VGkQVk564xU8sAd3",
  "type": "assistant",
  "uuid": "1c9467c7-918a-463b-92a6-1e886e3fedc7",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0196U4xvvj2bm3otPujtHD9X",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 9270,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15863,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 9270,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15863,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 9270,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 9270
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 claims 全部在合理参数范围内得到强验证；semi-synthetic 结果足够 dramatic 撑 headline；Ashwin 数据可用或可替代 核心假设：['global correction 在 moderate heterogeneity 设定下即产生显著 bias 放大（不需要极端参…",
  "leafUuid": "1c9467c7-918a-463b-92a6-1e886e3fedc7",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE for LLM annotation debiasing: Phase 1 best-tier validation",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：三条 claims 全部在合理参数范围内得到强验证；semi-synthetic 结果足够 dramatic 撑 headline；Ashwin 数据可用或可替代 核心假设：['global correction 在 moderate heterogeneity 设定下即产生显著 bias 放大（不需要极端参…",
  "leafUuid": "1c9467c7-918a-463b-92a6-1e886e3fedc7",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "EC-HTE for LLM annotation debiasing: Phase 1 best-tier validation",
  "sessionId": "94f0a1eb-767c-4fff-9455-a90d87bab21c"
}
```

---
