# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：真实污染量级接近 mvp_003 设定（c̄≥1.0），confounding 在真实数据上可量化复现，G-MFRM 在所有 benchmark 上显著

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/795d4c15-19ee-4516-81cd-acd9c86706da.jsonl`
- **Structured JSON:** [`47c1fcda77bb046d355e.json`](../../sessions/47/47c1fcda77bb046d355e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T20:50:34.089Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T20:50:34.089Z",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：真实污染量级接近 mvp_003 设定（c̄≥1.0），confounding 在真实数据上可量化复现，G-MFRM 在所有 benchmark 上显著优于全部 7 个 baseline\n核心假设：['真实 c_n 分布均值 ≥ 1.0，至少 30% 模型 c_n > 0.8（污染非边缘现象）', 'ConStat e_i 估计与真实曝光高度一致（rank correlation ≥ 0.85）', 'd_j 与 c_n·e_i 在真实数据中非正交（|ρ| ≥ 0.3），confounding 可观测', 'MCMC 收敛良好（R̂ ≤ 1.05, ESS ≥ 200 全参数）', '8 judges 数据收集无重大缺失或异常']\n关键指标范围：{'real_c_n_mean': [1.0, 2.0], 'kendall_tau_gmfrm': [0.88, 0.94], 'kendall_tau_best_baseline': [0.82, 0.87], 'delta_tau_vs_best_baseline': [0.04, 0.1], 'rmse_reduction_vs_sequential_pct': [25, 45], 'confounding_theta_rmse_degradation_pct': [20, 45], 'scatter_pearson_r_seq_bias': [0.5, 0.7], 'convergence_max_rhat': [1.0, 1.03], 'convergence_min_ess': [200, 500], 'wilcoxon_p_joint_vs_seq': [1e-06, 0.001]}\n叙事方向：原始 framing 完全成立。Confounding claim 有真实数据强实证（degradation ≥20%）， framework claim 通过收敛和诊断验证，empirical claim 通过 Kendall-τ 显著提升验证。 论文按 paper_framing 原样推进：Section 2 用形式化命题 + 真实数据 toy example 双重论证 confounding， 主表展示 G-MFRM 全面优于 7 baselines，headline 可写 \"X% higher Kendall-τ\"。 DG-IRT 迁移的 novelty 通过三阶段 pipeline 的非平凡适配（binary→continuous,  external anchoring）自然建立。无需降低任何 claim 强度。\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gated_mfrm_judge_bias\nvenue: emnlp-2026\nfocus: 核心关注：(1) confounding claim 的实证强度是否足够支撑 AAAI 投稿 (2) 真实数据 contamination 量级若接近 mvp_001 (弱) 而非 mvp_002 (强) 时论文 story 是否仍站得住 (3) DG-IRT 迁移的 novelty 是否被 reviewer 认可 (4) 7 个 baselines 的覆盖是否充分\n\n## paper_framing.md\n\n# Paper Framing — gated_mfrm_judge_bias\n\n## Target Venue\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\n- Timeline: ~68 days from today (2026-05-21)\n\n## Core Insight\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\n\n## Core Claims (3 条，均可证伪)\n\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.\n\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single calibration, yielding bias-and-contamination-corrected \"fair scores.\"\n\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\n\n## Story Spine\n\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\n\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.\n\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external exposure anchoring via ConStat + temporal signals, (3) joint gated model with c_n as latent parameters.\n\n- **Headline result template**: \"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\"\n\n## Narrative Strategy (from distilled writing)\n\n- **Type**: \"突破局限\" (sequential has structural flaw) + \"统一框架\" (G-MFRM unifies both corrections)\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\n- **Section 2**: Toy example / formal proposition demonstrating confounding before introducing G-MFRM method\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\n\n## Venue Fit Risks\n\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Why not CyclicJudge + discard contaminated items?\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\n\n2. **\"Is confounding large enough in practice?\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\n\n3. **\"Rank-1 assumption (c_n·e_i) too strong\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\n\n4. **\"DG-IRT transfer is trivial\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing.\n\n5. **\"Contamination signal realistic?\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\n\n## MVP Evidence Summary\n\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: multi_judge_data_collection\n  claim: 3\n  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using\n    8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,\n    Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position\n    swap for pairwise.'\n  priority: P0\n  gpu_budget_hours: 130\n  deps: []\n  notes: Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900\n    budget). Position swap doubles evaluation count.\n  status: planned\n- id: exp-002\n  name: constat_exposure_estimation\n  claim: 2\n  description: 'Estimate per-item exposure e_i via ConStat: generate reference benchmark\n    variants (rephrased by GPT-5.5/Claude), validate human equivalence, compute ConStat\n    delta scores. Combine with temporal signals where available.'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  notes: ConStat is black-box, validated r²=0.94. Reference variant quality is critical\n    — need human equivalence check on sample.\n  status: planned\n- id: exp-003\n  name: gmfrm_real_data_fit\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage\n    1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare\n    fair scores θ̂ with Chatbot Arena human votes (Kendall-τ).'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  - exp-002\n  notes: NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,\n    NCP, target_accept=0.95).\n  status: planned\n- id: exp-004\n  name: baseline_comparison\n  claim: 3\n  description: 'Compare G-MFRM against 7 baselines on same data: (1) raw multi-judge\n    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) DCR Factor,\n    (6) UDA, (7) Preference Leakage calibration. Metrics: Kendall-τ, Spearman-ρ with\n    Chatbot Arena.'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-003\n  notes: CyclicJudge and UDA need reimplementation or adaptation from public code.\n    DCR requires their inference pipeline.\n  status: planned\n- id: exp-005\n  name: contamination_magnitude_calibration\n  claim: 1\n  description: 'Estimate real contamination magnitude: compare fitted c_n from exp-003\n    with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001\n    (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength.'\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  notes: 'Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This\n    experiment determines claim calibration.'\n  status: planned\n- id: exp-006\n  name: judge_count_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure\n    G-MFRM performance degradation. At what minimum judge count does G-MFRM still\n    outperform sequential?'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-003\n  status: planned\n- id: exp-007\n  name: exposure_indicator_ablation\n  claim: 2\n  description: 'Ablation: contribution of each exposure indicator (ConStat delta,\n    temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out\n    analysis.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-008\n  name: facet_fit_diagnostics\n  claim: 2\n  description: 'Measurement quality validation: report infit/outfit MNSQ for all facets\n    (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi)\n    vs Stage 3 c_n as construct coherence validation.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  name: confounding_formal_proposition\n  claim: 1\n  description: 'Formal bias analysis: derive first-order bias approximation for sequential\n    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation\n    across realistic parameter ranges. For paper Section 2.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  notes: Can run in parallel with data collection. Extends MVP synthetic analysis\n    to formal proposition.\n  status: planned\n- id: exp-010\n  name: wildbench_replication\n  claim: 3\n  description: Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark\n    generalization.\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-003\n  status: planned\n- id: exp-011\n  name: adversarial_robustness\n  claim: 2\n  description: Test G-MFRM robustness against adversarial contamination following\n    Wang et al. (ICLR 2026) fragility findings.\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    convergence: PASS\n    rho_0.0:\n      joint_gmfrm:\n        RMSE: 0.1540±0.0269\n        tau: 0.9042±0.0445\n      sequential:\n        RMSE: 0.1540±0.0242\n        tau: 0.9016±0.0467\n      p_value: 0.4782\n    rho_0.3:\n      joint_gmfrm:\n        RMSE: 0.1521±0.0283\n        tau: 0.9068±0.0419\n      sequential:\n        RMSE: 0.1527±0.0236\n        tau: 0.9011±0.0452\n      p_value: 0.3506\n    rho_0.6:\n      joint_gmfrm:\n        RMSE: 0.1529±0.0285\n        tau: 0.9047±0.0418\n      sequential:\n        RMSE: 0.1537±0.0237\n        tau: 0.9037±0.0419\n      p_value: 0.3921\n    rho_0.0_no_degradation_p: 0.9563\n    runtime_seconds: 1675.6\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL (convergence)\n    convergence:\n      max_rhat: 1.05\n      min_ess: 47\n      pass: false\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 32.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0449\n      tau: 0.8390±0.0351\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8596±0.0291\n    joint_gmfrm:\n      RMSE: 0.1486±0.0199\n      tau: 0.9028±0.0181\n    runtime_seconds: 1935.4\n    scatter_pearson_r: 0.6534\n    scatter_p: 0\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    convergence:\n      max_rhat: 1.03\n      min_ess: 224\n      pass: true\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 43.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0448\n      tau: 0.8388±0.0345\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8593±0.0293\n    joint_gmfrm:\n      RMSE: 0.1243±0.0164\n      tau: 0.9223±0.0098\n    runtime_seconds: 4385.5\n    kendall_tau_joint: 0.9223\n    kendall_tau_seq: 0.8593\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T20:50:34.095Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T20:50:34.095Z",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T20:50:34.144Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：真实污染量级接近 mvp_003 设定（c̄≥1.0），confounding 在真实数据上可量化复现，G-MFRM 在所有 benchmark 上显著优于全部 7 个 baseline
核心假设：['真实 c_n 分布均值 ≥ 1.0，至少 30% 模型 c_n > 0.8（污染非边缘现象）', 'ConStat e_i 估计与真实曝光高度一致（rank correlation ≥ 0.85）', 'd_j 与 c_n·e_i 在真实数据中非正交（|ρ| ≥ 0.3），confounding 可观测', 'MCMC 收敛良好（R̂ ≤ 1.05, ESS ≥ 200 全参数）', '8 judges 数据收集无重大缺失或异常']
关键指标范围：{'real_c_n_mean': [1.0, 2.0], 'kendall_tau_gmfrm': [0.88, 0.94], 'kendall_tau_best_baseline': [0.82, 0.87], 'delta_tau_vs_best_baseline': [0.04, 0.1], 'rmse_reduction_vs_sequential_pct': [25, 45], 'confounding_theta_rmse_degradation_pct': [20, 45], 'scatter_pearson_r_seq_bias': [0.5, 0.7], 'convergence_max_rhat': [1.0, 1.03], 'convergence_min_ess': [200, 500], 'wilcoxon_p_joint_vs_seq': [1e-06, 0.001]}
叙事方向：原始 framing 完全成立。Confounding claim 有真实数据强实证（degradation ≥20%）， framework claim 通过收敛和诊断验证，empirical claim 通过 Kendall-τ 显著提升验证。 论文按 paper_framing 原样推进：Section 2 用形式化命题 + 真实数据 toy example 双重论证 confounding， 主表展示 G-MFRM 全面优于 7 baselines，headline 可写 "X% higher Kendall-τ"。 DG-IRT 迁移的 novelty 通过三阶段 pipeline 的非平凡适配（binary→continuous,  external anchoring）自然建立。无需降低任何 claim 强度。


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gated_mfrm_judge_bias
venue: emnlp-2026
focus: 核心关注：(1) confounding claim 的实证强度是否足够支撑 AAAI 投稿 (2) 真实数据 contamination 量级若接近 mvp_001 (弱) 而非 mvp_002 (强) 时论文 story 是否仍站得住 (3) DG-IRT 迁移的 novelty 是否被 reviewer 认可 (4) 7 个 baselines 的覆盖是否充分

## paper_framing.md

# Paper Framing — gated_mfrm_judge_bias

## Target Venue
- Primary: AAAI 2027 (full paper, deadline July 28, 2026)
- Backup: ACL 2027 via ARR (submission August 3, 2026)
- Timeline: ~68 days from today (2026-05-21)

## Core Insight
Sequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.

## Core Claims (3 条，均可证伪)

1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.

2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — jointly estimates model ability, item difficulty, judge severity, and contamination susceptibility in a single calibration, yielding bias-and-contamination-corrected "fair scores."

3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.

## Story Spine

- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.

- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.

- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external exposure anchoring via ConStat + temporal signals, (3) joint gated model with c_n as latent parameters.

- **Headline result template**: "On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles."

## Narrative Strategy (from distilled writing)

- **Type**: "突破局限" (sequential has structural flaw) + "统一框架" (G-MFRM unifies both corrections)
- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)
- **Section 2**: Toy example / formal proposition demonstrating confounding before introducing G-MFRM method
- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted
- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics
- **Ablation**: Full numbers (not checkmark grid), rows = components on/off

## Venue Fit Risks

- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.
- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.

## Anticipated Reviewer Concerns & Responses

1. **"Why not CyclicJudge + discard contaminated items?"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.

2. **"Is confounding large enough in practice?"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.

3. **"Rank-1 assumption (c_n·e_i) too strong"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.

4. **"DG-IRT transfer is trivial"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing.

5. **"Contamination signal realistic?"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.

## MVP Evidence Summary

- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224
- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)
- Robustness: method effective even under model misspecification (DGP with s_j, model without)


## experiment_plan (with registry status)

- id: exp-001
  name: multi_judge_data_collection
  claim: 3
  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using
    8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,
    Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position
    swap for pairwise.'
  priority: P0
  gpu_budget_hours: 130
  deps: []
  notes: Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900
    budget). Position swap doubles evaluation count.
  status: planned
- id: exp-002
  name: constat_exposure_estimation
  claim: 2
  description: 'Estimate per-item exposure e_i via ConStat: generate reference benchmark
    variants (rephrased by GPT-5.5/Claude), validate human equivalence, compute ConStat
    delta scores. Combine with temporal signals where available.'
  priority: P0
  gpu_budget_hours: 30
  deps:
  - exp-001
  notes: ConStat is black-box, validated r²=0.94. Reference variant quality is critical
    — need human equivalence check on sample.
  status: planned
- id: exp-003
  name: gmfrm_real_data_fit
  claim:
  - 1
  - 2
  - 3
  description: 'Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage
    1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare
    fair scores θ̂ with Chatbot Arena human votes (Kendall-τ).'
  priority: P0
  gpu_budget_hours: 15
  deps:
  - exp-001
  - exp-002
  notes: NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,
    NCP, target_accept=0.95).
  status: planned
- id: exp-004
  name: baseline_comparison
  claim: 3
  description: 'Compare G-MFRM against 7 baselines on same data: (1) raw multi-judge
    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) DCR Factor,
    (6) UDA, (7) Preference Leakage calibration. Metrics: Kendall-τ, Spearman-ρ with
    Chatbot Arena.'
  priority: P0
  gpu_budget_hours: 20
  deps:
  - exp-003
  notes: CyclicJudge and UDA need reimplementation or adaptation from public code.
    DCR requires their inference pipeline.
  status: planned
- id: exp-005
  name: contamination_magnitude_calibration
  claim: 1
  description: 'Estimate real contamination magnitude: compare fitted c_n from exp-003
    with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001
    (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength.'
  priority: P0
  gpu_budget_hours: 5
  deps:
  - exp-003
  notes: 'Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This
    experiment determines claim calibration.'
  status: planned
- id: exp-006
  name: judge_count_sensitivity
  claim: 2
  description: 'Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure
    G-MFRM performance degradation. At what minimum judge count does G-MFRM still
    outperform sequential?'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - exp-003
  status: planned
- id: exp-007
  name: exposure_indicator_ablation
  claim: 2
  description: 'Ablation: contribution of each exposure indicator (ConStat delta,
    temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out
    analysis.'
  priority: P1
  gpu_budget_hours: 10
  deps:
  - exp-002
  - exp-003
  status: planned
- id: exp-008
  name: facet_fit_diagnostics
  claim: 2
  description: 'Measurement quality validation: report infit/outfit MNSQ for all facets
    (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi)
    vs Stage 3 c_n as construct coherence validation.'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - exp-003
  status: planned
- id: exp-009
  name: confounding_formal_proposition
  claim: 1
  description: 'Formal bias analysis: derive first-order bias approximation for sequential
    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation
    across realistic parameter ranges. For paper Section 2.'
  priority: P1
  gpu_budget_hours: 10
  deps: []
  notes: Can run in parallel with data collection. Extends MVP synthetic analysis
    to formal proposition.
  status: planned
- id: exp-010
  name: wildbench_replication
  claim: 3
  description: Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark
    generalization.
  priority: P2
  gpu_budget_hours: 40
  deps:
  - exp-003
  status: planned
- id: exp-011
  name: adversarial_robustness
  claim: 2
  description: Test G-MFRM robustness against adversarial contamination following
    Wang et al. (ICLR 2026) fragility findings.
  priority: P2
  gpu_budget_hours: 15
  deps:
  - exp-003
  status: planned


## registry (completed experiments)

- exp_id: mvp_001
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL
    convergence: PASS
    rho_0.0:
      joint_gmfrm:
        RMSE: 0.1540±0.0269
        tau: 0.9042±0.0445
      sequential:
        RMSE: 0.1540±0.0242
        tau: 0.9016±0.0467
      p_value: 0.4782
    rho_0.3:
      joint_gmfrm:
        RMSE: 0.1521±0.0283
        tau: 0.9068±0.0419
      sequential:
        RMSE: 0.1527±0.0236
        tau: 0.9011±0.0452
      p_value: 0.3506
    rho_0.6:
      joint_gmfrm:
        RMSE: 0.1529±0.0285
        tau: 0.9047±0.0418
      sequential:
        RMSE: 0.1537±0.0237
        tau: 0.9037±0.0419
      p_value: 0.3921
    rho_0.0_no_degradation_p: 0.9563
    runtime_seconds: 1675.6
- exp_id: mvp_002
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    verdict: FAIL (convergence)
    convergence:
      max_rhat: 1.05
      min_ess: 47
      pass: false
    wilcoxon_joint_vs_seq:
      p_value: 1.0e-06
      pass: true
    rmse_reduction: 32.8%
    raw_average:
      RMSE: 0.8063±0.0841
      tau: 0.8401±0.0347
    mfrm_only:
      RMSE: 0.2539±0.0449
      tau: 0.8390±0.0351
    sequential:
      RMSE: 0.2211±0.0376
      tau: 0.8596±0.0291
    joint_gmfrm:
      RMSE: 0.1486±0.0199
      tau: 0.9028±0.0181
    runtime_seconds: 1935.4
    scatter_pearson_r: 0.6534
    scatter_p: 0
- exp_id: mvp_003
  name: ''
  status: DONE
  conclusion: success
  metrics:
    verdict: PASS
    convergence:
      max_rhat: 1.03
      min_ess: 224
      pass: true
    wilcoxon_joint_vs_seq:
      p_value: 1.0e-06
      pass: true
    rmse_reduction: 43.8%
    raw_average:
      RMSE: 0.8063±0.0841
      tau: 0.8401±0.0347
    mfrm_only:
      RMSE: 0.2539±0.0448
      tau: 0.8388±0.0345
    sequential:
      RMSE: 0.2211±0.0376
      tau: 0.8593±0.0293
    joint_gmfrm:
      RMSE: 0.1243±0.0164
      tau: 0.9223±0.0098
    runtime_seconds: 4385.5
    kendall_tau_joint: 0.9223
    kendall_tau_seq: 0.8593

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
  "promptId": "593240d8-bd1f-41a6-a4aa-da1789229f65",
  "type": "user",
  "uuid": "84015f84-d41b-40e7-8fbe-f963c324a1cf",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T20:50:34.142Z_

```json
{
  "parentUuid": "84015f84-d41b-40e7-8fbe-f963c324a1cf",
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
  "uuid": "efb7b950-6107-4973-b5f1-4913ca38fc46",
  "timestamp": "2026-05-21T20:50:34.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T20:50:34.142Z_

```json
{
  "parentUuid": "efb7b950-6107-4973-b5f1-4913ca38fc46",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "ab48e630-cca2-4d79-9bbf-3043c23785dd",
  "timestamp": "2026-05-21T20:50:34.142Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：真实污染量级接近 mvp_003 设定（c̄≥1.0），confounding 在真实数据上可量化复现，G-MFRM 在所有 benchmark 上显著优于全部 7 个 baseline 核心假设：['真实 c_n 分布均值 ≥ 1.0，至少 30% 模型 c_n > 0.8（污染非边缘现象）', 'ConS…",
  "leafUuid": "ab48e630-cca2-4d79-9bbf-3043c23785dd",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "G-MFRM real data validation and baseline comparison",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da"
}
```

---

### Assistant

_source line 8 · 2026-05-21T20:50:46.555Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each experiment in the experiment_plan, under the "best" tier assumptions. Let me carefully go through each experiment and produce realistic predicted results consistent with the best tier definition.

Let me review the best tier:
- Real c̄ ≥ 1.0, at least 30% models c_n > 0.8
- ConStat e_i estimation rank correlation ≥ 0.85 with true exposure
- d_j and c_n·e_i non-orthogonal (|ρ| ≥ 0.3)


- MCMC convergence with R̂ ≤ 1.05 and ESS ≥ 200, plus successful data collection from all 8 judges

Now I'm looking at the expected metric ranges for these best-tier experiments: the mean real confounding should fall between 1.0 and 2.0, Kendall tau correlations with GMFRM between 0.88 and 0.94, improvements over baseline methods ranging from 4-10 percentage points, and RMSE reductions of 25-45% compared to sequential approaches.

I'm also tracking additional performance indicators including RMSE degradation between 20-45%, scatter plot correlations around 0.5-0.7, convergence diagnostics staying tight at 1.0-1.03, effective sample sizes between 200-500, and highly significant Wilcoxon test results showing joint versus sequential comparisons at p-values from 1e-6 to 0.001.

Now I'm preparing to generate detailed predictions across all 11 experiments in a structured YAML format.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "ab48e630-cca2-4d79-9bbf-3043c23785dd",
  "isSidechain": false,
  "requestId": "req_011CbGNfShsfGjkDaTHXhiEJ",
  "type": "assistant",
  "uuid": "7c617e1a-d517-4911-88d1-da02499bd483",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hj6WTLEnjT8BQ2gNmiffpB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10619,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14634,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10619
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

_source line 9 · 2026-05-21T20:54:45.393Z_

```yaml
tier: best
narrative_guidance: >
  原始 framing 完全成立。Confounding claim 有真实数据强实证（degradation ≥20%），
  framework claim 通过收敛和诊断验证，empirical claim 通过 Kendall-τ 显著提升验证。
  论文按 paper_framing 原样推进：Section 2 用形式化命题 + 真实数据 toy example 双重论证 confounding，
  主表展示 G-MFRM 全面优于 7 baselines，headline 可写 "X% higher Kendall-τ"。
  DG-IRT 迁移的 novelty 通过三阶段 pipeline 的非平凡适配（binary→continuous, external anchoring）自然建立。
  无需降低任何 claim 强度。

imagined_experiments:
  - name: multi_judge_data_collection
    plan_id: exp-001
    description: >
      8 judges（GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro,
      Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro）
      评估 22 个 target models，MT-Bench 80 items + Arena-Hard 500 items，
      position swap 产生双向评分。
    expected_results:
      n_judges: 8
      n_target_models: 22
      n_items_mtbench: 80
      n_items_arenahard: 500
      total_judgments_mtbench: 28160  # 8×22×80×2(swap)
      total_judgments_arenahard: 176000  # 8×22×500×2(swap)
      missing_rate_pct: 1.8
      position_bias_avg_swap_disagreement_pct: 12.5
      api_cost_usd: 780
      vllm_gpu_hours: 105
      inter_judge_agreement_fleiss_kappa: 0.41
      judge_severity_range_raw_std: 0.82
    result_rationale: >
      best 档假设数据收集无重大缺失。8 个 judges 涵盖 4 家厂商 + 3 个开源，
      缺失率 <2% 因 API 和 vLLM 基础设施成熟。position swap disagreement ~12.5%
      符合已知 LLM positional bias 文献（Zheng et al. 2023 报告 10-15%）。
      inter-judge Fleiss κ≈0.41 处于 "moderate agreement" 范围，这正是
      G-MFRM 需要的场景——若 judges 高度一致则无需建模 severity。
      judge severity raw std=0.82 表明 judges 间存在可量化的系统性差异，
      为后续 MFRM 的 d_j 估计提供充分变异。API 成本低于 $900 预算。
    tables:
      - name: "Table S1: Data Collection Summary"
        columns: [Judge, Provider, Type, MT-Bench_judgments, Arena-Hard_judgments, Missing_pct, Avg_score]
        rows:
          - [GPT-5.5, OpenAI, API, 3520, 22000, 1.2, 7.84]
          - [Claude Opus 4.7, Anthropic, API, 3520, 22000, 0.8, 7.52]
          - [Claude Sonnet 4.6, Anthropic, API, 3520, 22000, 1.1, 7.71]
          - [DeepSeek-V4-Pro, DeepSeek, API, 3520, 22000, 2.0, 7.63]
          - [Qwen3-235B-A22B, Alibaba, vLLM, 3520, 22000, 2.5, 7.45]
          - [Qwen3.6-27B, Alibaba, vLLM, 3520, 22000, 3.1, 7.28]
          - [Llama 4 Maverick, Meta, vLLM, 3520, 22000, 2.8, 7.39]
          - [Gemini 2.5 Pro, Google, API, 3520, 22000, 1.5, 7.68]
    figures_description:
      - "Figure S1: Judge severity heatmap (22 models × 8 judges), 色彩编码 raw score deviation from item mean, 展示 judges 间系统性差异模式"
    analysis: >
      数据质量充分支撑后续全部实验。缺失率 1.8% 可用 MCMC 内自然处理（missing at random 假设合理，
      缺失主要来自 API timeout 而非 systematic）。8 judges 的 severity 分布有足够变异（std=0.82），
      开源 judges（Qwen3.6-27B, Llama 4 Maverick）系统性偏低 0.3-0.4 分，
      为 d_j 估计提供了清晰信号。

  - name: constat_exposure_estimation
    plan_id: exp-002
    description: >
      对 MT-Bench 80 + Arena-Hard 500 items 生成 reference variants（GPT-5.5 rephrased），
      人工抽检 50 items 验证语义等价，运行 ConStat pipeline 计算 per-item exposure e_i，
      结合 temporal signals（release date proximity）形成 composite exposure indicator。
    expected_results:
      n_items_total: 580
      n_reference_variants_per_item: 3
      human_equivalence_check_n: 50
      human_equivalence_pass_rate_pct: 94.0
      constat_delta_mean: 0.38
      constat_delta_std: 0.27
      constat_rank_corr_with_temporal: 0.72
      composite_e_i_mean: 0.55
      composite_e_i_std: 0.31
      items_high_exposure_pct: 28.4  # e_i > 0.7
      items_low_exposure_pct: 35.2   # e_i < 0.3
      mtbench_avg_e_i: 0.68
      arenahard_avg_e_i: 0.49
    result_rationale: >
      best 档假设 ConStat e_i 估计与真实曝光高度一致（rank correlation ≥ 0.85）。
      MT-Bench 作为 2023 年发布的广泛使用 benchmark，items 曝光量显著高于
      Arena-Hard（动态更新），体现为 MT-Bench avg e_i=0.68 > Arena-Hard 0.49。
      ConStat delta 与 temporal signal 相关 r=0.72 表明两个独立信号的一致性，
      增强了 composite indicator 的可信度。human equivalence 94% pass rate
      表明 reference variants 质量高，未引入语义偏移。28.4% items 高曝光
      提供了充足的 contamination signal 变异范围。
    tables:
      - name: "Table S2: Exposure Estimation Summary by Benchmark"
        columns: [Benchmark, N_items, Mean_e_i, Std_e_i, High_exposure_pct, ConStat_delta_mean]
        rows:
          - [MT-Bench, 80, 0.68, 0.24, 42.5, 0.51]
          - [Arena-Hard, 500, 0.49, 0.31, 25.2, 0.34]
          - [Combined, 580, 0.52, 0.30, 28.4, 0.36]
    figures_description:
      - "Figure S2: e_i 分布直方图，MT-Bench vs Arena-Hard 分面，展示 MT-Bench 右偏（高曝光更多）"
      - "Figure S3: ConStat delta vs temporal proximity scatter，r=0.72，展示两个独立信号的一致性"
    analysis: >
      Exposure estimation 质量足够支撑 Stage 2 anchoring。MT-Bench 的高曝光占比（42.5%）
      和 Arena-Hard 的相对低曝光形成了自然对比，有利于 contamination 效应的识别。
      Composite indicator 结合了 ConStat 的 behavioral signal 和 temporal 的 prior information，
      比单独使用任一信号更鲁棒。这为 exp-003 的 Stage 2 提供了可靠的 external anchor。

  - name: gmfrm_real_data_fit
    plan_id: exp-003
    description: >
      三阶段 pipeline 在真实数据上拟合：Stage 1 MFRM 估计 θ,b,d；
      Stage 2 用 exp-002 的 e_i 作为 external anchor；
      Stage 3 joint gated model 同时估计所有 facets 含 latent c_n。
      NumPyro MCMC (warmup=2000, samples=4000, chains=4, NCP, target_accept=0.95)。
    expected_results:
      # Convergence
      convergence_max_rhat: 1.02
      convergence_min_ess: 312
      convergence_all_params_rhat_below_1_05: true
      convergence_pct_params_rhat_below_1_01: 87.3
      # Contamination estimates
      real_c_n_mean: 1.18
      real_c_n_std: 0.64
      real_c_n_median: 1.05
      pct_models_c_n_above_0_8: 45.5
      pct_models_c_n_above_1_5: 18.2
      c_n_range: [0.12, 2.41]
      # Agreement with Arena votes
      kendall_tau_arena_mtbench: 0.91
      kendall_tau_arena_arenahard: 0.90
      kendall_tau_arena_combined: 0.91
      spearman_rho_arena_combined: 0.96
      # Comparison with sequential
      kendall_tau_sequential_combined: 0.85
      delta_tau_vs_sequential: 0.06
      rmse_theta_vs_sequential_reduction_pct: 34.2
      wilcoxon_p_joint_vs_seq: 3.2e-05
      # Confounding evidence
      scatter_pearson_r_seq_bias: 0.61
      confounding_theta_rmse_degradation_pct: 28.5
      d_j_c_n_e_i_correlation_abs: 0.37
      # Runtime
      runtime_hours: 2.8
      total_mcmc_samples: 16000
    result_rationale: >
      best 档核心假设：真实 c̄≥1.0。c_n_mean=1.18 落在 [1.0, 2.0] 范围内，
      接近 mvp_003 设定（mvp_003 DGP 中 c_n~N(1.2,0.5)），表明真实污染量级
      确实不是边缘现象。45.5% 模型 c_n>0.8（远超 30% 阈值），说明污染在主流模型中普遍存在。
      收敛优于 mvp_003（R̂=1.02 < 1.03），因为真实数据的 N=580 items 远多于
      合成数据的 100 items，提供了更多信息量。ESS=312 > 200 阈值，
      real data 的 item 数量和 judge 数量给 MCMC 更充分的似然信号。
      Kendall-τ=0.91 vs sequential 0.85，delta=0.06 落在 [0.04, 0.10] 范围中部，
      因为真实数据噪声高于合成但 contamination 量级充足。
      |ρ(d_j, c_n·e_i)|=0.37 > 0.3 阈值——严格 judges 倾向于对高污染模型给出更极端分数，
      confounding 在真实数据上可观测。RMSE degradation 28.5% < mvp_003 的 43.8%
      但仍 >20% 阈值，因为真实数据中 confounding 结构不如合成 DGP 极端但仍显著。
    tables:
      - name: "Table 1 (Main): Model Ability Estimates — G-MFRM vs Sequential"
        columns: [Model, Arena_Elo, G-MFRM_θ, Sequential_θ, Raw_Avg, c_n_estimate]
        note: "22 rows, top-5 and bottom-5 shown for illustration"
        rows:
          - [GPT-5.5, 1320, 1.82, 1.95, 8.12, 1.63]
          - [Claude Opus 4.7, 1305, 1.74, 1.82, 7.98, 1.41]
          - [DeepSeek-V4-Pro, 1285, 1.61, 1.73, 7.85, 1.52]
          - [Gemini 2.5 Pro, 1275, 1.55, 1.58, 7.79, 0.89]
          - [Claude Sonnet 4.6, 1260, 1.48, 1.51, 7.72, 1.15]
          - ["...", "...", "...", "...", "...", "..."]
          - [Phi-4-mini, 1085, 0.52, 0.48, 6.41, 0.35]
          - [Llama-3.3-8B, 1065, 0.38, 0.41, 6.22, 0.28]
      - name: "Table S3: MCMC Convergence Diagnostics Summary"
        columns: [Parameter_group, N_params, Max_Rhat, Min_ESS, Median_ESS, Pct_Rhat_below_1_01]
        rows:
          - [theta (ability), 22, 1.01, 412, 1850, 95.5]
          - [b (difficulty), 580, 1.02, 312, 890, 85.2]
          - [d (severity), 8, 1.00, 2450, 3100, 100.0]
          - [c (contamination), 22, 1.02, 345, 1620, 86.4]
          - [sigma_priors, 4, 1.01, 1890, 2340, 100.0]
    figures_description:
      - "Figure 2: Bias scatter — x=c_n estimate, y=(θ_sequential − θ_joint), Pearson r=0.61, 展示 sequential 对高污染模型系统性高估 ability"
      - "Figure 3: c_n posterior distribution ridge plot (22 models), 按 Arena Elo 排序, 展示高 Elo 模型倾向于高 c_n"
      - "Figure S4: Trace plots for representative parameters (θ_1, d_3, c_5), 4 chains 混合良好"
    analysis: >
      核心发现：真实数据上 c̄=1.18 确认污染非边缘现象，G-MFRM 显著优于 sequential（τ +0.06, p=3.2e-5）。
      confounding 在真实数据上通过三条证据链确认：(1) |ρ|=0.37 表明 d_j 与 c_n·e_i 非正交，
      (2) RMSE degradation 28.5% 表明忽略任一 facet 导致显著偏差，
      (3) bias scatter r=0.61 表明 sequential 对高污染模型系统性高估。
      收敛良好（R̂≤1.02, ESS≥312），支撑 framework claim。

  - name: baseline_comparison
    plan_id: exp-004
    description: >
      在同一数据上比较 G-MFRM 与 7 个 baselines：
      (1) Raw multi-judge average, (2) MFRM-only, (3) Sequential pipeline,
      (4) CyclicJudge, (5) DCR Factor, (6) UDA, (7) Preference Leakage calibration。
      主指标 Kendall-τ 和 Spearman-ρ with Chatbot Arena votes，
      分 MT-Bench 和 Arena-Hard 两个 benchmark 报告。
    expected_results:
      # Main metrics (combined)
      raw_average_tau: 0.82
      mfrm_only_tau: 0.84
      sequential_tau: 0.85
      cyclicjudge_tau: 0.84
      dcr_factor_tau: 0.83
      uda_tau: 0.86
      pref_leakage_tau: 0.83
      gmfrm_tau: 0.91
      # Spearman
      raw_average_rho: 0.89
      mfrm_only_rho: 0.91
      sequential_rho: 0.92
      cyclicjudge_rho: 0.91
      dcr_factor_rho: 0.90
      uda_rho: 0.93
      pref_leakage_rho: 0.90
      gmfrm_rho: 0.96
      # Best baseline
      best_baseline_name: UDA
      best_baseline_tau: 0.86
      delta_tau_vs_best_baseline: 0.05
      # Statistical significance
      wilcoxon_p_gmfrm_vs_uda: 8.7e-04
      wilcoxon_p_gmfrm_vs_sequential: 3.2e-05
      wilcoxon_p_gmfrm_vs_raw: 1.4e-06
      # Bootstrap CI for tau difference (G-MFRM − best baseline)
      delta_tau_95ci: [0.02, 0.08]
    result_rationale: >
      best 档下 G-MFRM τ=0.91 落在 [0.88, 0.94] 范围，best baseline τ=0.86 落在 [0.82, 0.87] 范围。
      UDA 是最强 baseline（τ=0.86）因为其 neural K-factor 部分捕捉了 judge 间差异，
      但它是 black-box 且 contamination-unaware，无法处理 c_n 导致的系统性偏差。
      CyclicJudge（τ=0.84）消除了平均 judge bias 但无法捕捉 item-specific severity 差异。
      DCR（τ=0.83）仅建模 contamination 而忽略 judge severity，吸收了部分 d_j 效应。
      Sequential（τ=0.85）优于单独 correction 但仍受 confounding bias 影响。
      MFRM-only（τ=0.84）与 CyclicJudge 相当，因为两者都只建模 judge 效应。
      delta=0.05 vs UDA 在 bootstrap 95% CI [0.02, 0.08] 中显著，
      Wilcoxon p=8.7e-4 落在 [1e-6, 0.001] 范围内。
      G-MFRM 在所有 7 baselines 上显著优于，支撑 headline claim。
    tables:
      - name: "Table 2 (Main): Baseline Comparison — Kendall-τ with Chatbot Arena"
        columns: [Method, Bias_Correction, Contam_Correction, Joint, MT-Bench_τ, Arena-Hard_τ, Combined_τ, Combined_ρ]
        rows:
          - [Raw Average, "✗", "✗", "✗", 0.80, 0.83, 0.82, 0.89]
          - [MFRM-only, "✓", "✗", "—", 0.83, 0.85, 0.84, 0.91]
          - [CyclicJudge, "✓", "✗", "—", 0.82, 0.85, 0.84, 0.91]
          - [DCR Factor, "✗", "✓", "—", 0.81, 0.84, 0.83, 0.90]
          - [Pref Leakage, "✗", "✓", "—", 0.82, 0.84, 0.83, 0.90]
          - [Sequential, "✓", "✓", "✗", 0.84, 0.86, 0.85, 0.92]
          - [UDA, "✓(neural)", "✗", "—", 0.85, 0.87, 0.86, 0.93]
          - ["**G-MFRM (ours)**", "✓", "✓", "✓", "**0.90**", "**0.91**", "**0.91**", "**0.96**"]
      - name: "Table S4: Pairwise Significance (Wilcoxon p-values, G-MFRM vs each baseline)"
        columns: [Baseline, p_value_tau, p_value_rho, Significant_at_0_01]
        rows:
          - [Raw Average, 1.4e-06, 2.1e-06, "✓"]
          - [MFRM-only, 5.8e-05, 8.3e-05, "✓"]
          - [CyclicJudge, 7.2e-05, 1.1e-04, "✓"]
          - [DCR Factor, 2.3e-05, 3.5e-05, "✓"]
          - [Pref Leakage, 3.1e-05, 4.7e-05, "✓"]
          - [Sequential, 3.2e-05, 4.9e-05, "✓"]
          - [UDA, 8.7e-04, 1.2e-03, "✓"]
    figures_description:
      - "Figure 4: Bar chart — Kendall-τ with 95% bootstrap CI for all 8 methods, 按 τ 排序, G-MFRM 显著高于全部 baselines"
      - "Figure S5: Per-model rank comparison heatmap — rows=models, cols=methods, 色彩编码 rank deviation from Arena Elo rank"
    analysis: >
      G-MFRM 在全部 7 baselines 上显著优于，最强 baseline UDA 的差距也在统计上显著（p<0.001）。
      关键观察：bias-only 方法（MFRM, CyclicJudge）和 contam-only 方法（DCR, PrefLeakage）
      性能相近（τ=0.83-0.84），sequential 小幅提升至 0.85 但受 confounding 限制，
      只有 joint estimation 实现了 τ=0.91 的跳跃。这一模式直接支撑 confounding claim：
      sequential 无法完全解决两个 facet 的交互效应。

  - name: contamination_magnitude_calibration
    plan_id: exp-005
    description: >
      将 exp-003 估计的真实 c_n 分布与 mvp_001/002/003 的合成 DGP 设定对比，
      确定真实污染量级落在哪个区间，评估对论文 claim 强度的影响。
    expected_results:
      real_c_n_mean: 1.18
      real_c_n_std: 0.64
      real_c_n_median: 1.05
      closest_mvp: mvp_003
      mvp_001_c_mean: 0.5
      mvp_002_c_mean: 1.5
      mvp_003_c_mean: 1.2
      distance_to_mvp_003: 0.02  # |1.18 - 1.20|
      distance_to_mvp_001: 0.68
      distance_to_mvp_002: 0.32
      ks_test_vs_mvp_003_p: 0.41  # fail to reject = distributions similar
      pct_models_in_mvp_001_regime: 22.7  # c_n < 0.6
      pct_models_in_mvp_003_regime: 54.5  # 0.8 < c_n < 1.8
      pct_models_in_mvp_002_regime: 22.7  # c_n > 1.3
      top3_contaminated_models: [GPT-5.5, DeepSeek-V4-Pro, Claude Opus 4.7]
      top3_clean_models: [Phi-4-mini, Llama-3.3-8B, Mistral-Small-3.2]
    result_rationale: >
      best 档假设 c̄≥1.0。c_n_mean=1.18 最接近 mvp_003（c̄=1.2），
      KS test p=0.41 表明真实分布与 mvp_003 DGP 不可区分。这是 best 档的核心验证：
      真实污染量级确实接近 mvp_003 设定而非 mvp_001（弱），论文 story 完全成立。
      高 Elo 模型（GPT-5.5, Claude Opus 4.7, DeepSeek-V4-Pro）c_n 最高（1.4-2.4），
      因为它们训练数据最多、最可能包含 benchmark items。小模型（Phi-4-mini, Llama-3.3-8B）
      c_n 低（0.1-0.4），因为训练数据量和质量有限，benchmark 泄漏概率低。
      这种结构性模式增强了 c_n 估计的 face validity。
    tables:
      - name: "Table S5: Real vs Synthetic Contamination Distribution Comparison"
        columns: [Distribution, Mean, Std, Median, Q25, Q75, KS_p_vs_real]
        rows:
          - [Real data, 1.18, 0.64, 1.05, 0.62, 1.58, "—"]
          - [mvp_001 DGP, 0.50, 0.30, 0.45, 0.28, 0.68, 0.001]
          - [mvp_002 DGP, 1.50, 0.50, 1.48, 1.15, 1.82, 0.12]
          - [mvp_003 DGP, 1.20, 0.50, 1.18, 0.82, 1.55, 0.41]
    figures_description:
      - "Figure S6: 真实 c_n 分布 vs mvp_001/002/003 DGP 分布叠加密度图，展示真实数据最接近 mvp_003"
      - "Figure S7: 模型 c_n vs Arena Elo scatter (r=0.58), 展示高 Elo 模型更容易被污染"
    analysis: >
      真实污染量级与 mvp_003 高度一致（KS p=0.41），远非 mvp_001 的弱污染场景。
      这意味着 mvp_003 的合成结果（RMSE −43.8%, τ +6.3pp）是对真实场景的合理预测，
      real data 上观测到的效应量（RMSE −34.2%, τ +0.06）与之一致但略小，
      可归因于真实数据中 confounding 结构不如 DGP 极端。
      c_n 与 Elo 正相关（r=0.58）提供了额外的 construct validity：
      被更多使用的强模型更可能接触 benchmark data。

  - name: judge_count_sensitivity
    plan_id: exp-006
    description: >
      从 8 judges 中抽取子集（2, 4, 6 judges），对每个子集重新拟合 G-MFRM，
      测量 Kendall-τ 随 judge 数量的变化。每个 judge 数量随机抽取 20 次取均值。
      确定 G-MFRM 优于 sequential 的最小 judge 数量。
    expected_results:
      tau_2_judges_gmfrm: 0.86
      tau_2_judges_sequential: 0.84
      tau_4_judges_gmfrm: 0.89
      tau_4_judges_sequential: 0.85
      tau_6_judges_gmfrm: 0.90
      tau_6_judges_sequential: 0.85
      tau_8_judges_gmfrm: 0.91
      tau_8_judges_sequential: 0.85
      min_judges_for_significant_improvement: 4
      delta_tau_2_judges: 0.02
      delta_tau_4_judges: 0.04
      delta_tau_6_judges: 0.05
      delta_tau_8_judges: 0.06
      p_value_at_4_judges: 0.008
      p_value_at_2_judges: 0.14
      convergence_2_judges_max_rhat: 1.04
      convergence_4_judges_max_rhat: 1.03
    result_rationale: >
      G-MFRM 的优势随 judge 数量增加而单调增长，因为更多 judges 提供了更好的
      d_j 和 c_n 可辨识性——judge severity 的 cross-information 帮助分离 confounding。
      2 judges 时 G-MFRM 仍优于 sequential（Δτ=0.02），但不显著（p=0.14），
      因为 2 judges 的 d_j 估计不稳定，gating mechanism 无法充分发挥。
      4 judges 是临界点（p=0.008<0.01），此后优势稳定。
      Sequential 的 τ 对 judge 数量不敏感（0.84-0.85），因为它的 confounding bias
      不因更多 judges 而消除——这是结构性问题而非数据量问题。
      这一对比直接展示了 joint vs sequential 的本质差异。
    tables:
      - name: "Table 3: Judge Count Sensitivity Analysis"
        columns: [N_judges, G-MFRM_τ, Sequential_τ, Δτ, p_value, Max_Rhat, Min_ESS]
        rows:
          - [2, "0.86±0.03", "0.84±0.02", 0.02, 0.14, 1.04, 185]
          - [4, "0.89±0.02", "0.85±0.02", 0.04, 0.008, 1.03, 265]
          - [6, "0.90±0.01", "0.85±0.01", 0.05, 0.001, 1.02, 298]
          - [8, "0.91±0.01", "0.85±0.01", 0.06, 3.2e-05, 1.02, 312]
    figures_description:
      - "Figure 5: Line plot — Kendall-τ vs N_judges for G-MFRM (blue) and Sequential (red), shaded 95% CI, 展示 G-MFRM 收益递增而 sequential 平坦"
    analysis: >
      实用建议：4 judges 是 G-MFRM 优势显著的最低门槛。
      这对 practitioner 有价值：即使只有 4 个 judges，joint estimation 也值得。
      Sequential 的平坦曲线是 confounding claim 的另一个实证支撑——
      增加数据量（更多 judges）不能修复结构性模型误设。

  - name: exposure_indicator_ablation
    plan_id: exp-007
    description: >
      Leave-one-out ablation：依次移除 ConStat delta、temporal signal、LogProber Safe Score
      中的一个 exposure indicator，重新拟合 G-MFRM，比较 Kendall-τ 变化。
      同时测试 single-indicator 版本。
    expected_results:
      # Full composite
      full_composite_tau: 0.91
      # Leave-one-out
      without_constat_tau: 0.88
      without_temporal_tau: 0.90
      without_logprober_tau: 0.90
      # Single indicator
      constat_only_tau: 0.90
      temporal_only_tau: 0.87
      logprober_only_tau: 0.87
      # Contribution analysis
      constat_marginal_contribution: 0.03  # full - without_constat
      temporal_marginal_contribution: 0.01
      logprober_marginal_contribution: 0.01
      constat_rank_corr_with_c_n: 0.81
      temporal_rank_corr_with_c_n: 0.62
      logprober_rank_corr_with_c_n: 0.59
    result_rationale: >
      ConStat 是最关键的 exposure indicator（marginal contribution +0.03），
      因为它直接测量 behavioral contamination signal（原始 vs rephrased 表现差异），
      与 c_n 的 rank correlation 最高（0.81）。移除 ConStat 后 τ 从 0.91 降至 0.88，
      仍优于所有 baselines（best baseline UDA τ=0.86），说明 G-MFRM 的优势
      不完全依赖于 exposure estimation 质量——joint calibration 框架本身就有结构性优势。
      Temporal 和 LogProber 各贡献 0.01，它们提供的信息与 ConStat 部分重叠。
      ConStat-only 版本（τ=0.90）已接近 full composite（0.91），
      进一步确认 ConStat 是 Stage 2 的核心。
    tables:
      - name: "Table 4: Exposure Indicator Ablation"
        columns: [Configuration, Indicators_used, Kendall_τ, Δτ_vs_full, Rank_corr_with_c_n]
        rows:
          - [Full composite, "ConStat + Temporal + LogProber", 0.91, "—", 0.85]
          - ["w/o ConStat", "Temporal + LogProber", 0.88, -0.03, 0.68]
          - ["w/o Temporal", "ConStat + LogProber", 0.90, -0.01, 0.82]
          - ["w/o LogProber", "ConStat + Temporal", 0.90, -0.01, 0.83]
          - [ConStat only, ConStat, 0.90, -0.01, 0.81]
          - [Temporal only, Temporal, 0.87, -0.04, 0.62]
          - [LogProber only, LogProber, 0.87, -0.04, 0.59]
          - [No exposure (MFRM-only), None, 0.84, -0.07, "—"]
    figures_description:
      - "Figure S8: Bar chart — leave-one-out Kendall-τ with error bars, 标注每个 indicator 的 marginal contribution"
    analysis: >
      ConStat 是 Stage 2 的支柱，但 G-MFRM 即使在 ConStat 缺失时仍优于 sequential（0.88 > 0.85），
      表明 joint framework 的结构性优势独立于 exposure estimation 质量。
      这回应了潜在 reviewer 质疑："如果 ConStat 不准怎么办？"——
      答案是 G-MFRM 优雅退化但不崩溃。

  - name: facet_fit_diagnostics
    plan_id: exp-008
    description: >
      报告全部 facets（θ, b, d, c）的 infit/outfit MNSQ，
      标记 misfitting elements（MNSQ > 1.3 或 < 0.7）。
      比较 Stage 1 person-fit 指标（lz, EMRi）与 Stage 3 c_n 估计的一致性。
    expected_results:
      # Infit/Outfit
      theta_infit_mean: 1.01
      theta_infit_range: [0.78, 1.25]
      theta_outfit_mean: 1.03
      theta_pct_misfit: 4.5
      b_infit_mean: 1.00
      b_infit_range: [0.65, 1.42]
      b_pct_misfit: 5.2
      d_infit_mean: 0.98
      d_infit_range: [0.82, 1.18]
      d_pct_misfit: 0.0
      c_infit_mean: 1.02
      c_pct_misfit: 9.1
      # Person-fit vs c_n
      lz_c_n_rank_corr: 0.72
      emri_c_n_rank_corr: 0.68
      pct_agreement_flagged: 78.3  # % overlap between person-fit flagged and high c_n
    result_rationale: >
      best 档下 MFRM 拟合良好：θ 和 d 的 infit/outfit 接近 1.0，misfit 率低。
      b (items) 的 misfit 略高（5.2%），因为部分 Arena-Hard items 的难度在
      不同 judges 间变异大（某些 items 对某些 judges "特别难评"）。
      c_n 的 misfit 率最高（9.1%=2/22 models），因为 rank-1 c_n·e_i 假设
      对极端模型（极高或极低污染）拟合不完美——这正是论文中坦诚讨论 rank-1 局限性的位置。
      lz 和 c_n 的 rank correlation 0.72 表明传统 person-fit 指标确实能部分捕捉
      contamination（因为 contaminated models 在高曝光 items 上表现异常好），
      但 c_n 提供了更结构化的解释。两者 78.3% 的重叠验证了 construct coherence。
    tables:
      - name: "Table S6: Facet Fit Statistics"
        columns: [Facet, N, Infit_MNSQ_mean, Infit_MNSQ_range, Outfit_MNSQ_mean, Pct_misfit]
        rows:
          - [θ (ability), 22, 1.01, "0.78–1.25", 1.03, 4.5]
          - [b (difficulty), 580, 1.00, "0.65–1.42", 1.02, 5.2]
          - [d (severity), 8, 0.98, "0.82–1.18", 0.99, 0.0]
          - [c (contamination), 22, 1.02, "0.74–1.38", 1.05, 9.1]
      - name: "Table S7: Person-Fit vs c_n Convergent Validity"
        columns: [Metric, Rank_corr_with_c_n, p_value, Pct_overlap_flagged]
        rows:
          - [lz (person-fit), 0.72, 0.0002, 78.3]
          - [EMRi (extended), 0.68, 0.0008, 73.9]
    figures_description:
      - "Figure S9: Infit/Outfit MNSQ distribution per facet (box plots), 红色虚线标注 0.7/1.3 阈值"
      - "Figure S10: lz vs c_n scatter, r=0.72, 展示 person-fit 与 contamination 的 convergent validity"
    analysis: >
      整体拟合质量支撑 framework claim：G-MFRM 不是 overfitting 噪声，
      而是合理捕捉了数据结构。c_n 的 9.1% misfit 率可在 Limitations 中坦诚报告，
      并指向 rank-k extension 的 future work。person-fit/c_n 的 convergent validity
      (r=0.72) 是 DG-IRT 迁移成功的额外证据。

  - name: confounding_formal_proposition
    plan_id: exp-009
    description: >
      推导 sequential estimator 在 d_j/c_n·e_i 非正交条件下的一阶 bias 近似。
      形式化为 Proposition 1（Section 2）。Monte Carlo 验证 bias 近似精度。
    expected_results:
      # Formal result
      proposition_statement: >
        Under non-orthogonality (Cov(d_j, c_n·e_i) ≠ 0), the bias-first sequential
        estimator θ̂_seq has first-order bias E[θ̂_seq - θ] ≈ γ·Cov(d_j, c_n·e_i)/Var(d_j)
        where γ is the contamination gating coefficient. Direction: positive covariance
        → overestimation of high-contamination models.
      # Monte Carlo validation
      mc_n_simulations: 5000
      mc_parameter_grid_size: 50  # 50 rho values in [-0.8, 0.8]
      bias_approximation_r2: 0.94
      bias_direction_correct_pct: 97.8
      max_bias_at_rho_0_6: 0.31  # std units
      bias_at_rho_0_3: 0.14  # std units
      real_data_rho: 0.37
      real_data_predicted_bias: 0.17
      real_data_observed_bias: 0.19
      prediction_error_pct: 10.5
    result_rationale: >
      一阶 bias 近似基于 omitted variable bias 的经典结果（Angrist & Pischke 框架
      在 psychometric context 的适配）。R²=0.94 表明一阶近似在实际参数范围内精度高。
      关键洞察：bias 方向由 Cov(d_j, c_n·e_i) 决定——当严格 judges（高 d_j）
      与高污染模型×高曝光 items 的交互为正时，sequential 高估高污染模型。
      真实数据 ρ=0.37 > 0 预测正向 bias 0.17 std units，观测值 0.19 std units，
      预测误差仅 10.5%——形式化命题在真实数据上得到量化验证。
      这为 Section 2 提供了理论 + 实证双重论证。
    tables:
      - name: "Table S8: Monte Carlo Validation of Bias Approximation"
        columns: [rho_range, N_sims, Mean_true_bias, Mean_approx_bias, Approx_R2, Direction_accuracy_pct]
        rows:
          - ["[-0.8, -0.4]", 1000, -0.28, -0.26, 0.93, 98.2]
          - ["[-0.4, 0.0]", 1000, -0.09, -0.08, 0.95, 97.5]
          - ["[0.0, 0.4]", 1000, 0.10, 0.09, 0.94, 97.8]
          - ["[0.4, 0.8]", 1000, 0.32, 0.30, 0.93, 97.6]
          - [Overall, 5000, "—", "—", 0.94, 97.8]
    figures_description:
      - "Figure 1 (Section 2): Left panel: sequential pipeline diagram with confounding annotation (red arrows showing omitted variable path); Right panel: G-MFRM joint estimation DAG with all paths modeled"
      - "Figure S11: MC validation — true bias vs approximate bias scatter (5000 points), R²=0.94, 按 ρ 色彩编码"
    analysis: >
      Proposition 1 将 confounding claim 从实证观察提升为理论结果，
      MC 验证确认近似在实际参数范围内高精度（R²=0.94）。
      real data 上 predicted vs observed bias 的一致性（10.5% error）
      提供了 "theory predicts, data confirms" 的强叙事弧线。
      Section 2 可以先展示 proposition，再用 exp-003 的 bias scatter 作为实证验证。

  - name: wildbench_replication
    plan_id: exp-010
    description: >
      在 WildBench 上复制 G-MFRM pipeline：收集 8 judges × 22 models 评分，
      ConStat exposure estimation，三阶段拟合，baseline 比较。
      验证跨 benchmark 泛化性。
    expected_results:
      wildbench_n_items: 1024
      kendall_tau_gmfrm_wildbench: 0.89
      kendall_tau_sequential_wildbench: 0.84
      kendall_tau_uda_wildbench: 0.85
      delta_tau_vs_best_baseline_wildbench: 0.04
      wilcoxon_p_gmfrm_vs_seq_wildbench: 2.1e-04
      c_n_mean_wildbench: 0.95
      c_n_rank_corr_cross_benchmark: 0.82  # c_n on WildBench vs MT-Bench+Arena-Hard
      convergence_max_rhat_wildbench: 1.02
      convergence_min_ess_wildbench: 278
    result_rationale: >
      WildBench τ=0.89 略低于 MT-Bench+Arena-Hard 的 0.91，
      因为 WildBench items 更 open-ended、scoring 更主观，
      引入了 G-MFRM 无法完全捕捉的 noise。但仍显著优于全部 baselines（Δτ=0.04）。
      c_n_mean=0.95 略低于主数据集的 1.18，因为 WildBench 较新（2024），
      部分 items 未被充分泄漏。跨 benchmark c_n rank correlation 0.82
      表明 contamination 是模型属性（不是 benchmark 属性），
      支撑 c_n 作为 meaningful latent trait 的解读。
    tables:
      - name: "Table 5: Cross-Benchmark Replication (WildBench)"
        columns: [Method, WildBench_τ, MT-Bench_τ, Arena-Hard_τ]
        rows:
          - [Raw Average, 0.80, 0.80, 0.83]
          - [Sequential, 0.84, 0.84, 0.86]
          - [UDA, 0.85, 0.85, 0.87]
          - ["**G-MFRM**", "**0.89**", "**0.90**", "**0.91**"]
    figures_description:
      - "Figure 6: Cross-benchmark c_n rank comparison scatter, MT-Bench+Arena-Hard c_n vs WildBench c_n, r=0.82"
    analysis: >
      跨 benchmark 泛化成功：G-MFRM 在第三个独立 benchmark 上同样显著优于全部 baselines。
      c_n 跨 benchmark 一致性（r=0.82）是论文的加分项——
      说明 contamination susceptibility 是模型的稳定属性，G-MFRM 估计的不是 benchmark-specific 噪声。

  - name: adversarial_robustness
    plan_id: exp-011
    description: >
      模拟 Wang et al. (ICLR 2026) 的 adversarial contamination 场景：
      对 target model 注入 benchmark items（0%, 5%, 10%, 20% training data），
      测试 G-MFRM c_n 估计是否正确反映注入量，
      以及 θ 估计是否对 adversarial contamination 鲁棒。
    expected_results:
      # c_n tracking injection
      c_n_at_0pct_injection: 0.15
      c_n_at_5pct_injection: 0.82
      c_n_at_10pct_injection: 1.45
      c_n_at_20pct_injection: 2.18
      c_n_injection_correlation: 0.97
      # theta robustness
      theta_bias_at_0pct: 0.02
      theta_bias_at_5pct: 0.05
      theta_bias_at_10pct: 0.08
      theta_bias_at_20pct: 0.14
      theta_bias_sequential_at_20pct: 0.52
      robustness_ratio_20pct: 3.71  # sequential_bias / gmfrm_bias
      # Detection
      auc_detecting_contaminated: 0.94
    result_rationale: >
      G-MFRM 的 gating mechanism 设计上就是为了 absorb contamination effect into c_n，
      所以 c_n 与 injection rate 高度相关（r=0.97）是预期中的。
      θ bias 在 20% injection 时仅 0.14（vs sequential 的 0.52），
      因为 G-MFRM 将 contamination inflation 归因于 c_n 而非 θ。
      robustness ratio 3.71× 意味着 G-MFRM 的 θ 偏差仅为 sequential 的 27%。
      AUC=0.94 表明 c_n 可以作为 contamination detection 工具，
      这为论文的 practical impact 增加了一个维度。
      注意：这是在 controlled setting（已知注入量）的 validation，
      与真实场景的 unknown contamination 有区别，需在论文中说明。
    tables:
      - name: "Table S9: Adversarial Robustness — θ Bias Under Controlled Contamination"
        columns: [Injection_pct, G-MFRM_c_n, G-MFRM_θ_bias, Sequential_θ_bias, Robustness_ratio]
        rows:
          - [0, 0.15, 0.02, 0.03, 1.50]
          - [5, 0.82, 0.05, 0.18, 3.60]
          - [10, 1.45, 0.08, 0.34, 4.25]
          - [20, 2.18, 0.14, 0.52, 3.71]
    figures_description:
      - "Figure S12: Left: c_n vs injection rate (near-linear, r=0.97); Right: θ bias vs injection rate for G-MFRM (blue, flat) vs Sequential (red, steep)"
    analysis: >
      Adversarial robustness 是 reviewer concern 的预防性回应。
      G-MFRM 在极端场景（20% injection）下 θ bias 仅为 sequential 的 1/4，
      且 c_n 可作为 post-hoc contamination audit 工具（AUC=0.94）。
      这将 G-MFRM 从 "evaluation correction method" 提升为 "contamination-aware evaluation framework"。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "7c617e1a-d517-4911-88d1-da02499bd483",
  "isSidechain": false,
  "requestId": "req_011CbGNfShsfGjkDaTHXhiEJ",
  "type": "assistant",
  "uuid": "00df2ff4-615e-4d02-b327-9dd86c951834",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Hj6WTLEnjT8BQ2gNmiffpB",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 10619,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14634,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 10619,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14634,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 10619,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 10619
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

_source line 10_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：真实污染量级接近 mvp_003 设定（c̄≥1.0），confounding 在真实数据上可量化复现，G-MFRM 在所有 benchmark 上显著优于全部 7 个 baseline 核心假设：['真实 c_n 分布均值 ≥ 1.0，至少 30% 模型 c_n > 0.8（污染非边缘现象）', 'ConS…",
  "leafUuid": "00df2ff4-615e-4d02-b327-9dd86c951834",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "G-MFRM real data validation and baseline comparison",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：真实污染量级接近 mvp_003 设定（c̄≥1.0），confounding 在真实数据上可量化复现，G-MFRM 在所有 benchmark 上显著优于全部 7 个 baseline 核心假设：['真实 c_n 分布均值 ≥ 1.0，至少 30% 模型 c_n > 0.8（污染非边缘现象）', 'ConS…",
  "leafUuid": "00df2ff4-615e-4d02-b327-9dd86c951834",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "G-MFRM real data validation and baseline comparison",
  "sessionId": "795d4c15-19ee-4516-81cd-acd9c86706da"
}
```

---
