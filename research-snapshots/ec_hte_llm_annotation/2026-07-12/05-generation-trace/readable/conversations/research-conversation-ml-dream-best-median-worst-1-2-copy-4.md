# Research conversation: 你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。 你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保

**When Debiasing Hurts: An Exact Bias Identity for LLM-Annotated Treatment Effects (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 12
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/1086ee9a-0ebf-4c47-93af-a55e058db083.jsonl`
- **Structured JSON:** [`c3ec368bd99c5ed22287.json`](../../sessions/c3/c3ec368bd99c5ed22287.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-20T18:54:37.083Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-20T18:54:37.083Z",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083",
  "content": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。\n\n你需要同时定义 best / median / worst 三档：\n1. 每档的核心假设（哪些假设成立/不成立）\n2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）\n3. 每档的论文叙事方向——\n   - best: 原始 framing 完全成立，claims 无需调整\n   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验\n   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）\n\n三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性\n自行判断。但必须确保三档之间的数字和叙事逻辑一致。\n\n# Project context\nproject: ec_hte_llm_annotation\nfocus: 核心关注：(1) \"debiasing can hurt\" 的 surprise value 是否足够撑起 EMNLP main；(2) 层级贝叶斯 partial pooling 作为方法核心是否有足够技术贡献；(3) 仅有合成+半合成实验时论文是否可接受（Ashwin 数据集可能拿不到）；(4) 与 PPCI (Sui 2026) 的差异化是否清晰\n\n## paper_framing.md\n\n# Paper Framing — ec_hte_llm_annotation\n\n## Target Venue\n- Primary: EMNLP 2026 Main (via ARR)\n- Deadline: ARR submission May 25, 2026; commitment deadline August 2, 2026\n- Format: Long paper, 8 pages + unlimited references\n\n## Core Claims (3 条，可证伪)\n\n1. **Bias Mechanism Discovery**: When LLM misclassification rates for an effect modifier vary across subgroups, applying a global (pooled) correction to subgroup-level CATE estimates introduces systematic bias — over-correcting low-error subgroups and under-correcting high-error ones. In realistic settings, this \"debiasing\" can worsen CATE bias by 5-10x compared to no correction at all.\n\n2. **EC-HTE Solution**: Hierarchical Bayesian subgroup-stratified correction (EC-HTE) eliminates this bias while controlling estimation variance through partial pooling. EC-HTE achieves near-oracle CATE accuracy (|bias| < 0.02) and valid coverage (≥90%) across both high- and low-error subgroups, with expert label budgets as small as 250.\n\n3. **Diagnostic Criterion**: The product of misclassification heterogeneity × CATE heterogeneity across subgroups provides a computable diagnostic: when this product exceeds a threshold, global correction is harmful and stratified correction is needed. This criterion has standalone value independent of EC-HTE.\n\n## Story Spine\n\n- **Problem**: NLP researchers increasingly use LLM annotations as effect modifiers in heterogeneous treatment effect analysis (e.g., \"tweet contains economic framing\" moderates campaign effectiveness). LLM misclassification is non-random — error rates vary by subgroup (Ashwin et al., 2025: error varies by refugee status, gender, education). Current PPI/DSL corrections apply global rectifiers assuming homogeneous error.\n\n- **Existing approaches & gaps**: Mozer (2026) proves arm-specific rectifiers fix ATE bias under differential prediction error, but explicitly limits analysis to average treatment effects. PPI (Angelopoulos et al., 2023) and DSL (Egami et al., 2024) correct population-level estimates. PPCI (Sui et al., 2026) extends PPI to conditional functionals but corrects outcome-side measurement, not covariate-side. ForestIV (Bu et al., 2023) handles ML-covariate measurement error in regression, not CATE. **No work addresses correction when the mismeasured variable defines the heterogeneity structure.**\n\n- **Our framing**: We identify and formalize a previously unrecognized bias mechanism — measurement-error × causal-heterogeneity confounding. When a pooled confusion matrix is applied to correct subgroup-level CATEs, it misattributes prediction noise across subgroups with different error rates, producing bias proportional to the product of misclassification heterogeneity and CATE heterogeneity. This is a problem-level discovery, not a technique-level extension. EC-HTE solves it via hierarchical Bayesian stratified correction with honest causal forest integration.\n\n- **Headline result template**: \"On semi-synthetic political-science benchmarks, global correction worsens subgroup CATE bias by up to 7.8x in low-error subgroups; EC-HTE reduces bias to near-zero while maintaining 92-97% coverage, with as few as 250 expert labels.\"\n\n## Key Contributions (ordered for paper)\n\n1. **Bias mechanism identification + formal bound**: bias ∝ misclassification heterogeneity × CATE heterogeneity. Includes \"debiasing can hurt\" proposition with constructive example. (Theory + Empirical)\n2. **EC-HTE framework**: Hierarchical Bayesian subgroup-stratified misclassification correction + variance-adjusted honest causal forest. (Method)\n3. **Diagnostic criterion**: Computable threshold from pilot data to decide whether stratified correction is needed. (Practical tool)\n4. **Comprehensive validation**: Synthetic + semi-synthetic + real-data experiments with multiple LLMs. (Empirical)\n\n## Anticipated Reviewer Concerns\n\n1. **\"Why not just use expert labels directly for CATE?\"** — Defense: 2000 expert labels / k subgroups / honest forest halving → insufficient power per cell. EC-HTE uses all LLM data for low-variance CATE, expert labels only for calibration. Explicitly quantify in experiments.\n\n2. **\"How is this different from PPCI (Sui et al., 2026)?\"** — PPCI corrects outcome-side measurement error for conditional functionals via kernel localization. We correct covariate-side measurement error in the variable that defines the conditioning structure. Orthogonal problems.\n\n3. **\"Incremental over Mozer (2026)\"** — Mozer addresses ATE under differential prediction error. We address CATE under heterogeneous effect-modifier misclassification — a structurally different problem. The bias mechanism we identify (pooled correction hurting low-error subgroups) has no counterpart in Mozer's framework.\n\n4. **\"How sensitive to subgroup definition?\"** — Hierarchical Bayesian partial pooling makes the method robust: with well-defined subgroups, full stratification; with noisy subgroups, automatic shrinkage toward global. Include robustness analysis.\n\n5. **\"Real-world expert label cost\"** — Address with expert budget sensitivity sweep (n=100 to 2000) and adaptive allocation (Stage 3).\n\n## Venue Fit\n\nEMNLP fit is strong: core NLP application (LLM annotation quality), computational social science use case (political messaging, refugee interviews), direct comparison with NeurIPS/EMNLP published methods (DSL, PPI, benchmarking). Methodology is causal inference but framed through NLP lens. Potential reviewer pool: CL+CSS track.\n\nRisk: pure statistics reviewers may want stronger theoretical contribution (convergence rates, minimax bounds). Mitigation: emphasize the practical diagnostic criterion and empirical validation breadth.\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  claim: 2\n  description: 'Hierarchical Bayesian EC-HTE on synthetic data: implement HB Dirichlet-prior\n    confusion matrix estimator with partial pooling, compare against MLE/Laplace on\n    full regime sweep (extreme/moderate/homogeneous × n_expert 100-2000 × k=2,4 subgroups).\n    Primary validation of Claim 2.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU (PyMC + econml)\n  estimated_time: 12-24h (coding + 1000 MC runs)\n  deps: []\n  status: planned\n- id: exp-002\n  claim: 1\n  description: 'Formal bias bound verification: derive bias = f(misclass_heterogeneity,\n    CATE_heterogeneity) analytically, then verify empirically across systematic parameter\n    grid. Produce the ''debiasing can hurt'' proposition with constructive two-subgroup\n    example.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8-12h\n  deps: []\n  status: planned\n- id: exp-003\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Semi-synthetic benchmark: use real political-science tweet corpus\n    (e.g., CardiffNLP TweetEval or similar public dataset), inject known CATE heterogeneity\n    structure, annotate with GPT-4.1 and Qwen3-235B-A22B, measure subgroup-specific\n    misclassification rates, apply EC-HTE vs baselines. Primary empirical evidence\n    for all claims.'\n  priority: P0\n  gpu_budget_hours: 20\n  compute: GPU (LLM inference for annotation)\n  estimated_time: 24-36h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-004\n  claim:\n  - 1\n  - 2\n  description: 'Real-data validation on Ashwin et al. (2025) Rohingya refugee interview\n    dataset: LLM annotation errors correlate with refugee status, gender, education.\n    Apply EC-HTE to recover corrected CATEs. Requires dataset access.'\n  priority: P0\n  gpu_budget_hours: 10\n  compute: GPU (LLM inference)\n  estimated_time: 24h\n  deps:\n  - exp-001\n  status: planned\n  risk: Dataset access — need to check if publicly available or request from authors\n- id: exp-005\n  claim: 3\n  description: 'Diagnostic criterion validation: compute misclass_heterogeneity ×\n    CATE_heterogeneity product from pilot data across all experimental settings, show\n    it predicts when global correction fails. ROC analysis of threshold.'\n  priority: P0\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 4-8h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-006\n  claim: 2\n  description: 'Expert label budget sensitivity: systematic sweep n_expert ∈ {50,\n    100, 250, 500, 1000, 2000} × k ∈ {2, 4, 8} subgroups. Find crossover point where\n    EC-HTE > Global. Validate HB partial pooling value at small n.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-007\n  claim: 1\n  description: 'PPCI (Sui et al., 2026) baseline comparison: implement PPCI kernel-based\n    conditional correction and compare against EC-HTE on same benchmarks. Key differentiation\n    experiment.'\n  priority: P1\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 12h\n  deps:\n  - exp-001\n  - exp-003\n  status: planned\n- id: exp-008\n  claim: 2\n  description: 'Multiple LLM annotator comparison: GPT-4.1 vs Qwen3-235B-A22B vs Claude\n    Sonnet 4.6 — measure misclassification heterogeneity patterns, show EC-HTE benefit\n    varies by LLM quality.'\n  priority: P1\n  gpu_budget_hours: 15\n  compute: GPU\n  estimated_time: 12h\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  claim: 2\n  description: 'Adaptive expert annotation allocation (Stage 3): implement CATE-weighted\n    allocation targeting high-CATE × high-error subgroups, compare against uniform\n    and uncertainty-only allocation.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  - exp-006\n  status: planned\n- id: exp-010\n  claim: 2\n  description: 'Robustness to misspecified subgroup structure: test EC-HTE when subgroups\n    are noisy/overlapping or when the true subgroup structure doesn''t align with\n    the conditioning variable.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 8h\n  deps:\n  - exp-001\n  status: planned\n- id: exp-011\n  claim: 2\n  description: 'Causal forest leaf-level analysis: integrate EC-HTE correction into\n    CausalForestDML at the leaf level (corrected pseudo-outcomes + variance-adjusted\n    CIs), compare against naive forest.'\n  priority: P2\n  gpu_budget_hours: 0\n  compute: CPU\n  estimated_time: 16h\n  deps:\n  - exp-001\n  status: planned\n\n# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）\n\n```yaml\ntiers:\n  best:\n    meaning: \"...\"\n    key_assumptions: [...]\n    number_ranges: {metric_a: [low, high], metric_b: [...]}\n    narrative_direction: \"...\"\n  median:\n    meaning: \"...\"\n    ...\n  worst:\n    meaning: \"...\"\n    ...\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-20T18:54:37.087Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-20T18:54:37.087Z",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083"
}
```

---

## Round 1

10 recorded events

### User

_source line 3 · 2026-05-20T18:54:37.106Z_

你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。

你需要同时定义 best / median / worst 三档：
1. 每档的核心假设（哪些假设成立/不成立）
2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性）
3. 每档的论文叙事方向——
   - best: 原始 framing 完全成立，claims 无需调整
   - median: 部分假设未完全验证，需要调整 claims 强度或补充实验
   - worst: 核心假设不成立，需要找到新的 angle 来 reframe（但仍冲同一 venue，不降级目标）

三档的具体含义不预设——根据这个研究的 paper_framing、已有数据和方法特性
自行判断。但必须确保三档之间的数字和叙事逻辑一致。

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

# 输出格式（YAML，仅输出一个 ```yaml 块，不要任何额外说明文字）

```yaml
tiers:
  best:
    meaning: "..."
    key_assumptions: [...]
    number_ranges: {metric_a: [low, high], metric_b: [...]}
    narrative_direction: "..."
  median:
    meaning: "..."
    ...
  worst:
    meaning: "..."
    ...
```


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "c6113bdd-bbd1-4629-9d1a-fa5f2566e079",
  "type": "user",
  "uuid": "220df692-9eb7-4a22-b633-73f326c672c1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-20T18:54:37.106Z_

```json
{
  "parentUuid": "220df692-9eb7-4a22-b633-73f326c672c1",
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
  "uuid": "665b2c33-d04e-488d-a581-727f78b1ff3b",
  "timestamp": "2026-05-20T18:54:37.106Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-20T18:54:37.106Z_

```json
{
  "parentUuid": "665b2c33-d04e-488d-a581-727f78b1ff3b",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "f18001ec-fff4-49e7-b79d-c71bafd31f87",
  "timestamp": "2026-05-20T18:54:37.106Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083",
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
  "aiTitle": "Define scenario tiers for Dream simulation validation",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083"
}
```

---

### Assistant

_source line 7 · 2026-05-20T18:54:53.378Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to define three tiers (best/median/worst) for a "Dream simulation" of their research project on EC-HTE (hierarchical Bayesian subgroup-stratified correction for LLM annotation errors in heterogeneous treatment effect estimation). They want this in YAML format.

Let me analyze the research context:

Core claims:
1. Global debiasing can hurt - bias ∝ misclass_heterogeneity × CATE_heterogeneity
2. EC-HTE (hierarchical Bayesian) achieves near-oracle accuracy with small expert budgets


3. The diagnostic criterion—the product of heterogeneities—predicts when global correction fails

Key risks to consider:
- The "debiasing can hurt" finding needs to be surprising enough for EMNLP
- Whether hierarchical Bayesian partial pooling alone constitutes a sufficient technical contribution
- Limited experimental scope with only synthetic and semi-synthetic data (the Ashwin dataset may not be accessible)
- How to differentiate from PPCI (Sui 2026)

For the best/median/worst tiers, I'm thinking about what would constitute success: the bias amplification effect being dramatic enough (5-10x), EC-HTE achieving near-oracle performance with minimal expert annotations, and the diagnostic criterion having strong predictive power across different scenarios.

In the best case, semi-synthetic results on real political science data would be compelling, the Ashwin dataset would be accessible and demonstrate real-world effects, and there'd be clear separation from PPCI. For the median scenario, bias amplification would be moderate (2-4x), EC-HTE would work but require more expert labels than ideal, the diagnostic criterion would be functional but threshold-dependent, and PPCI comparisons would show EC-HTE winning with modest margins. In the worst case, bias amplification would be minimal or only appear in extreme parameter regimes, hierarchical Bayesian partial pooling wouldn't clearly outperform simpler stratified MLE, the diagnostic criterion would be noisy, real data wouldn't materialize, and reviewers would see this as incremental relative to Mozer and PPCI.

Now I need to define concrete metrics and track what matters most.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f18001ec-fff4-49e7-b79d-c71bafd31f87",
  "isSidechain": false,
  "requestId": "req_011CbEL1hMPLK6gVixD6gmkB",
  "type": "assistant",
  "uuid": "9562661a-6299-484f-a5be-ffd588e92263",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjrADGY6P8FYwYD6rG21qY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2919,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 8889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8889
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

_source line 8 · 2026-05-20T18:55:39.199Z_

```yaml
tiers:
  best:
    meaning: "三条 claims 全部在合理参数范围内得到强验证；semi-synthetic 结果足够 dramatic 撑 headline；Ashwin 数据可用或可替代"
    key_assumptions:
      - "global correction 在 moderate heterogeneity 设定下即产生显著 bias 放大（不需要极端参数）"
      - "HB partial pooling 在 n_expert=250 时已明显优于 stratified MLE（小样本优势可量化）"
      - "diagnostic criterion 有高判别力，阈值跨数据集稳定"
      - "semi-synthetic 中 GPT-4.1/Qwen3 的 misclassification heterogeneity 自然存在且足够大"
      - "至少有一个 real-data 验证（Ashwin 或替代公开数据集）"
    number_ranges:
      bias_amplification_factor_global_vs_uncorrected: [5.0, 12.0]   # global correction 使 CATE bias 恶化倍数
      ec_hte_absolute_cate_bias: [0.005, 0.02]                       # |bias| after EC-HTE
      ec_hte_coverage_90ci: [0.90, 0.97]                             # 90% CI coverage rate
      min_n_expert_for_dominance: [100, 250]                         # EC-HTE 开始优于 global 的最小标注量
      diagnostic_criterion_auroc: [0.90, 0.98]                       # 诊断准则判别 AUC
      hb_vs_stratified_mle_bias_reduction: [0.30, 0.60]              # HB partial pooling 相对 stratified MLE 的额外 bias 降幅比例
      ec_hte_vs_ppci_bias_ratio: [0.15, 0.40]                        # EC-HTE bias / PPCI bias（越小越好）
    narrative_direction: >
      原始 framing 完全成立。"Debiasing can hurt" 作为 problem-level discovery 有足够 surprise value：
      在 realistic 参数下 global correction 使 bias 恶化 5-10x，这是 NLP+CSS 社区未意识到的陷阱。
      EC-HTE 以 250 expert labels 实现 near-oracle，HB partial pooling 的小样本优势可量化。
      Diagnostic criterion 作为 standalone practical tool 给论文第三条独立贡献。
      Real data 验证锁定了 "不只是理论上可能" 的叙事。投 EMNLP main 无需降级任何 claim。

  median:
    meaning: "bias 放大效应存在但幅度中等，需更多 expert labels 才稳定；仅有合成+半合成验证；PPCI 区分度存在但不悬殊"
    key_assumptions:
      - "global correction bias 放大在 moderate heterogeneity 下可复现，但倍数不如极端设定 dramatic"
      - "HB partial pooling 优于 MLE 的优势仅在 n_expert<500 时显著，大样本下差异收敛"
      - "diagnostic criterion 有效但阈值需要 per-dataset 校准，不能直接 transfer"
      - "semi-synthetic LLM 自然 heterogeneity 存在但偏温和，需选择特定 subgroup 定义才能放大效应"
      - "Ashwin 数据不可用，无 real-data 实验"
    number_ranges:
      bias_amplification_factor_global_vs_uncorrected: [2.0, 5.0]
      ec_hte_absolute_cate_bias: [0.02, 0.05]
      ec_hte_coverage_90ci: [0.85, 0.92]
      min_n_expert_for_dominance: [250, 500]
      diagnostic_criterion_auroc: [0.78, 0.90]
      hb_vs_stratified_mle_bias_reduction: [0.10, 0.30]
      ec_hte_vs_ppci_bias_ratio: [0.40, 0.70]
    narrative_direction: >
      需要调整 claims 强度。Claim 1 从 "debiasing can hurt 5-10x" 软化为 "debiasing can hurt,
      且 hurt 的程度随 heterogeneity product 单调增长"——强调 mechanism 的 monotonic relationship
      而非绝对倍数。Claim 2 中 "250 expert labels" 上调为 "500"，partial pooling 的叙事从
      "dramatically better" 转为 "principled regularization with guaranteed non-inferiority"。
      Claim 3 的 diagnostic 从 "computable threshold" 弱化为 "computable risk score + decision
      heuristic"。无 real data 需在 limitation 中正面处理，并在 semi-synthetic 设计上加强
      ecological validity 论证（real corpus, real LLM errors, only treatment effect is synthetic）。
      仍可投 EMNLP main，但需补充：(a) 更细粒度的 sensitivity analysis 替代 dramatic headline number,
      (b) partial pooling 的理论 shrinkage 分析（bias-variance tradeoff 可视化）。

  worst:
    meaning: "bias 放大效应仅在极端/人造参数下显著，realistic 设定中 global correction 仍可接受；HB 无明显优势；需要 reframe"
    key_assumptions:
      - "bias 放大仅在 misclass heterogeneity 极端时出现（Δ error rate > 0.3），moderate 设定下 global correction 的额外 bias < 0.05，实际可忽略"
      - "HB partial pooling 与 stratified MLE 在 n_expert≥200 时无统计显著差异"
      - "semi-synthetic 中 LLM 的自然 misclassification heterogeneity 偏小（Δ < 0.10），需人为放大才出效果"
      - "diagnostic criterion 的 AUROC 偏低，false positive/negative 率高"
      - "PPCI 在 semi-synthetic 场景下表现与 EC-HTE 相当或仅略差"
    number_ranges:
      bias_amplification_factor_global_vs_uncorrected: [1.2, 2.0]
      ec_hte_absolute_cate_bias: [0.05, 0.10]
      ec_hte_coverage_90ci: [0.80, 0.88]
      min_n_expert_for_dominance: [500, 1000]
      diagnostic_criterion_auroc: [0.60, 0.78]
      hb_vs_stratified_mle_bias_reduction: [0.00, 0.10]
      ec_hte_vs_ppci_bias_ratio: [0.70, 1.00]
    narrative_direction: >
      核心 "debiasing can hurt" 的 surprise value 不足以独立撑 paper——在 realistic 设定下
      global correction 的 hurt 太小。需要 reframe，三个可行方向（不降级 venue）：
      (1) Reframe 为 "measurement error propagation in HTE" 的系统性分析论文——不再依赖
      "debiasing hurts" 的 shock value，而是提供完整的 taxonomy：何时 global 足够、何时需
      stratified、何时 correction 本身不值得做。贡献变为 decision framework 而非单一方法。
      (2) 如果 HB partial pooling 本身无优势，pivot 到 adaptive expert allocation 作为
      方法核心——用 CATE heterogeneity 引导标注预算分配，即使 correction 方法简单（MLE），
      allocation strategy 仍有独立价值。需要 exp-009 的结果支撑。
      (3) 强化 diagnostic criterion 为 pre-analysis auditing tool——面向 CSS 实践者的
      "should I even bother with stratified correction" 决策工具，降低方法贡献预期，
      提升 practical contribution 叙事。适合 EMNLP Findings 保底，但若 allocation 实验强，
      仍可冲 main。任何 reframe 都需要在 exp-001/002 的前 3 天内根据 moderate-regime
      结果做出判断，避免沉没成本。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "9562661a-6299-484f-a5be-ffd588e92263",
  "isSidechain": false,
  "requestId": "req_011CbEL1hMPLK6gVixD6gmkB",
  "type": "assistant",
  "uuid": "4c49febc-1cdf-4406-9e24-0f30f4adf215",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01EjrADGY6P8FYwYD6rG21qY",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 8889,
      "cache_read_input_tokens": 11841,
      "output_tokens": 2919,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 8889,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 2919,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 8889,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 8889
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "4c49febc-1cdf-4406-9e24-0f30f4adf215",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083"
}
```

---

### Runtime record

_source line 10_

```json
{
  "type": "ai-title",
  "aiTitle": "Define scenario tiers for Dream simulation validation",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。基于以下研究信息，为 Dream 模拟定义三档场景。  你需要同时定义 best / median / worst 三档： 1. 每档的核心假设（哪些假设成立/不成立） 2. 每档的关键实验指标预期范围（确保 best ≥ median ≥ worst 一致性） 3. 每档的论文叙事方向——    - best: 原始 framing 完全成立，claims 无需…",
  "leafUuid": "4c49febc-1cdf-4406-9e24-0f30f4adf215",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Define scenario tiers for Dream simulation validation",
  "sessionId": "1086ee9a-0ebf-4c47-93af-a55e058db083"
}
```

---
