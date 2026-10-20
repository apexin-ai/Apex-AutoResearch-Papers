# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Real contamination magnitude matches mvp_002/003 assumptions (strong), G-MFR

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/3035166a-19af-4924-a7d4-3c797a8e405f.jsonl`
- **Structured JSON:** [`9ab84f46cab1a00721ec.json`](../../sessions/9a/9ab84f46cab1a00721ec.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T21:58:34.358Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T21:58:34.358Z",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Real contamination magnitude matches mvp_002/003 assumptions (strong), G-MFRM converges cleanly on real data, and ranking correction is statistically and practically significant across benchmarks\n核心假设：['Real contamination is strong: fitted c_n median ≥ 0.8 across target models (Tier A)', 'G-MFRM converges on real data with acceptable diagnostics (R̂ ≤ 1.05, ESS ≥ 200)', 'e_i estimation pipeline (performance gap + temporal + LogProber) produces reliable exposure indicators (exp-012 σ=0.2 θ̂ degradation < 5%)', 'G-MFRM fair scores beat ALL 8 baselines on Kendall-τ with Chatbot Arena, including CyclicJudge+discard', 'Rank changes are interpretable and non-trivial: ≥ 3 models shift ≥ 2 positions, top-5 changes', 'ConStat per-model delta validates fitted c_n (Spearman ρ ≥ 0.7)']\n关键指标范围：{'real_contamination_c_n_median': [0.8, 1.5], 'kendall_tau_gmfrm': [0.88, 0.95], 'delta_tau_vs_best_baseline': [0.04, 0.08], 'rmse_reduction_vs_sequential_pct': [30, 50], 'convergence_max_rhat': [1.0, 1.05], 'convergence_min_ess': [200, 500], 'error_prop_theta_rmse_degradation_sigma02_pct': [0, 5], 'c_n_recovery_rmse_synthetic': [0.05, 0.15], 'rank_changes_ge2_positions': [3, 8], 'constat_cn_validation_spearman': [0.7, 0.95], 'judge_count_min_for_significant_gain': [3, 4]}\n叙事方向：Full Tier A. All three claims at full strength. Lead with quantitative shock: joint estimation corrects X% RMSE / +Y Kendall-τ over best sequential baseline on real benchmarks. Confounding Claim proven both formally (OVB observation) and empirically (real-data rank distortions). Framework Claim validated by convergence + diagnostics. Empirical Claim demonstrated across MT-Bench and Arena-Hard. Paper title emphasizes 'joint calibration corrects systematic rank distortions'. Headline: contamination and judge bias confound each other in practice, and only joint estimation resolves it.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gated_mfrm_judge_bias\nvenue: emnlp-2026\nfocus: Verify framing improvements: (1) Claim 2 now says \"staged joint calibration\" not \"joint estimation\", (2) Proposition 1 downgraded to Observation citing OVB, (3) new exp-012 error propagation sensitivity added, (4) expanded exp-004 rank change analysis, (5) new Reviewer Concerns 6-8 added. Check if these changes resolve the prior round's critical issues R1-N1 and R1-N2.\n\n## paper_framing.md\n\n# Paper Framing — gated_mfrm_judge_bias\n\n## Target Venue\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\n- Timeline: ~68 days from today (2026-05-21)\n\n## Core Insight\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\n\n## Core Claims (3 条，均可证伪)\n\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding.\n\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected \"fair scores.\" (Note: \"staged joint\" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use \"staged joint calibration\" or \"conditional joint estimation,\" never \"fully joint.\")\n\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\n\n## Story Spine\n\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\n\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.\n\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.\n\n- **Headline result template**: \"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\"\n\n## Narrative Strategy (from distilled writing)\n\n- **Type**: \"突破局限\" (sequential has structural flaw) + \"统一框架\" (G-MFRM unifies both corrections)\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\n- **Section 2**: Toy example / formal **observation** (NOT \"proposition\" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\n\n## Venue Fit Risks\n\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Why not CyclicJudge + discard contaminated items?\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\n\n2. **\"Is confounding large enough in practice?\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\n\n3. **\"Rank-1 assumption (c_n·e_i) too strong\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\n\n4. **\"DG-IRT transfer is trivial\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).\n\n4b. **\"Staged estimation ≠ joint estimation\"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.\n\n5. **\"Contamination signal realistic?\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\n\n6. **\"Chatbot Arena Elo as ground truth — circular reasoning?\"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.\n\n7. **\"c_n ≥ 0 assumption too restrictive?\"** — Half-Cauchy prior enforces non-negativity, appropriate for the \"contamination as unfair advantage\" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.\n\n8. **\"≥4 judges needed — too expensive?\"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.\n\n## Two-Tier Narrative (contingent on exp-005 contamination magnitude)\n\n**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:\n- Lead with ranking correction as primary contribution\n- Claim 3 at full strength: \"G-MFRM achieves X% higher Kendall-τ\"\n- Headline: joint estimation dramatically outperforms sequential\n\n**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:\n- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)\n- Reframe: \"even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)\"\n- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude\n- Claim 3 softened to \"comparable or better rankings PLUS interpretable diagnostic outputs\"\n\nexp-005 determines which tier. Decision point: after exp-005 results, before paper writing.\n\n## MVP Evidence Summary\n\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: multi_judge_data_collection\n  claim: 3\n  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using\n    8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,\n    Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position\n    swap for pairwise.'\n  priority: P0\n  gpu_budget_hours: 130\n  deps: []\n  notes: Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900\n    budget). Position swap doubles evaluation count.\n  status: planned\n- id: exp-002\n  name: item_exposure_estimation\n  claim: 2\n  description: 'Estimate per-item exposure e_i via three-source pipeline: (1) Primary:\n    item-level performance gap between original items and GPT-5.5/Claude-rephrased\n    reference variants, averaged across reference models, with spline difficulty correction\n    (ConStat-inspired). (2) Temporal: performance gap on pre-cutoff vs post-cutoff\n    item variants where available. (3) LogProber: token logprob memorization scores\n    for models with logprob API. Sources combined via weighted composite (weights\n    tuned on validation split). ConStat per-model delta used as external validation\n    of fitted c_n, not as e_i source.'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  notes: 'Main bottleneck: reference benchmark variant construction + quality validation.\n    ConStat per-model delta validates G-MFRM c_n, not used for per-item e_i.'\n  status: planned\n- id: exp-003\n  name: gmfrm_real_data_fit\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage\n    1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare\n    fair scores θ̂ with Chatbot Arena human votes (Kendall-τ).'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  - exp-002\n  notes: 'NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,\n    NCP, target_accept=0.95). Include per-benchmark analysis: if any benchmark has\n    contamination ≈ 0, verify G-MFRM degrades gracefully to MFRM level (real-data\n    graceful degradation check).'\n  status: planned\n- id: exp-004\n  name: baseline_comparison\n  claim: 3\n  description: 'Compare G-MFRM against 8 baselines on same data: (1) raw multi-judge\n    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) CyclicJudge\n    + contaminated item discard, (6) DCR Factor, (7) UDA, (8) Preference Leakage calibration.\n    Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena. MUST include rank change analysis:\n    show which specific models change rank, by how many positions, and top-k stability\n    (k=5,10).'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-003\n  notes: 'Baseline (5) is the strongest trivial alternative — addresses Reviewer Concern\n    #1. CyclicJudge/UDA/DCR/PrefLeakage need public code check. Budget may not include\n    debug time. Rank change analysis addresses Dream R2-W3.'\n  status: planned\n- id: exp-005\n  name: contamination_magnitude_calibration\n  claim: 1\n  description: 'Estimate real contamination magnitude: compare fitted c_n from exp-003\n    with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001\n    (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength.'\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  notes: 'Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This\n    experiment determines claim calibration.'\n  status: planned\n- id: exp-006\n  name: judge_count_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure\n    G-MFRM performance degradation. At what minimum judge count does G-MFRM still\n    outperform sequential?'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-003\n  status: planned\n- id: exp-007\n  name: exposure_indicator_ablation\n  claim: 2\n  description: 'Ablation: contribution of each exposure indicator (ConStat delta,\n    temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out\n    analysis.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-008\n  name: facet_fit_diagnostics\n  claim: 2\n  description: 'Measurement quality validation: report infit/outfit MNSQ for all facets\n    (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi)\n    vs Stage 3 c_n as construct coherence validation. MUST also report: divergent\n    transition count, posterior predictive check, trace plots for key parameters.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  name: confounding_formal_observation\n  claim: 1\n  description: 'Formal bias analysis: derive first-order bias approximation for sequential\n    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation\n    across realistic parameter ranges. For paper Section 2. Frame as ''Observation''\n    (standard OVB from Angrist & Pischke 2009), not ''Proposition''. MUST include\n    synthetic c_n point-estimate validation: generate data with known ground-truth\n    c_n, fit G-MFRM, report per-model c_n RMSE and 95% credible interval coverage\n    probability.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  notes: Can run in parallel with data collection. Extends MVP synthetic analysis.\n    Downgraded from 'Proposition' to 'Observation' per Dream review. Synthetic c_n\n    validation addresses Dream R1-N3.\n  status: planned\n- id: exp-012\n  name: error_propagation_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis for staged estimation: inject Gaussian noise\n    into e_i estimates at σ=0.1,0.2,0.5 before Stage 3 fitting. Measure θ̂ RMSE degradation\n    and c_n recovery accuracy. Shows three-stage pipeline is robust to e_i estimation\n    error. Use synthetic data with known ground truth.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  notes: Addresses Dream R2-W5 and R1-N1. Can run on MVP codebase with modifications.\n    Critical for defending staged estimation design choice.\n  status: planned\n- id: exp-010\n  name: wildbench_replication\n  claim: 3\n  description: Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark\n    generalization.\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-003\n  status: planned\n- id: exp-011\n  name: adversarial_robustness\n  claim: 2\n  description: Test G-MFRM robustness against adversarial contamination following\n    Wang et al. (ICLR 2026) fragility findings.\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    convergence: PASS\n    rho_0.0:\n      joint_gmfrm:\n        RMSE: 0.1540±0.0269\n        tau: 0.9042±0.0445\n      sequential:\n        RMSE: 0.1540±0.0242\n        tau: 0.9016±0.0467\n      p_value: 0.4782\n    rho_0.3:\n      joint_gmfrm:\n        RMSE: 0.1521±0.0283\n        tau: 0.9068±0.0419\n      sequential:\n        RMSE: 0.1527±0.0236\n        tau: 0.9011±0.0452\n      p_value: 0.3506\n    rho_0.6:\n      joint_gmfrm:\n        RMSE: 0.1529±0.0285\n        tau: 0.9047±0.0418\n      sequential:\n        RMSE: 0.1537±0.0237\n        tau: 0.9037±0.0419\n      p_value: 0.3921\n    rho_0.0_no_degradation_p: 0.9563\n    runtime_seconds: 1675.6\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL (convergence)\n    convergence:\n      max_rhat: 1.05\n      min_ess: 47\n      pass: false\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 32.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0449\n      tau: 0.8390±0.0351\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8596±0.0291\n    joint_gmfrm:\n      RMSE: 0.1486±0.0199\n      tau: 0.9028±0.0181\n    runtime_seconds: 1935.4\n    scatter_pearson_r: 0.6534\n    scatter_p: 0\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    convergence:\n      max_rhat: 1.03\n      min_ess: 224\n      pass: true\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 43.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0448\n      tau: 0.8388±0.0345\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8593±0.0293\n    joint_gmfrm:\n      RMSE: 0.1243±0.0164\n      tau: 0.9223±0.0098\n    runtime_seconds: 4385.5\n    kendall_tau_joint: 0.9223\n    kendall_tau_seq: 0.8593\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T21:58:34.362Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T21:58:34.362Z",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T21:58:34.382Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Real contamination magnitude matches mvp_002/003 assumptions (strong), G-MFRM converges cleanly on real data, and ranking correction is statistically and practically significant across benchmarks
核心假设：['Real contamination is strong: fitted c_n median ≥ 0.8 across target models (Tier A)', 'G-MFRM converges on real data with acceptable diagnostics (R̂ ≤ 1.05, ESS ≥ 200)', 'e_i estimation pipeline (performance gap + temporal + LogProber) produces reliable exposure indicators (exp-012 σ=0.2 θ̂ degradation < 5%)', 'G-MFRM fair scores beat ALL 8 baselines on Kendall-τ with Chatbot Arena, including CyclicJudge+discard', 'Rank changes are interpretable and non-trivial: ≥ 3 models shift ≥ 2 positions, top-5 changes', 'ConStat per-model delta validates fitted c_n (Spearman ρ ≥ 0.7)']
关键指标范围：{'real_contamination_c_n_median': [0.8, 1.5], 'kendall_tau_gmfrm': [0.88, 0.95], 'delta_tau_vs_best_baseline': [0.04, 0.08], 'rmse_reduction_vs_sequential_pct': [30, 50], 'convergence_max_rhat': [1.0, 1.05], 'convergence_min_ess': [200, 500], 'error_prop_theta_rmse_degradation_sigma02_pct': [0, 5], 'c_n_recovery_rmse_synthetic': [0.05, 0.15], 'rank_changes_ge2_positions': [3, 8], 'constat_cn_validation_spearman': [0.7, 0.95], 'judge_count_min_for_significant_gain': [3, 4]}
叙事方向：Full Tier A. All three claims at full strength. Lead with quantitative shock: joint estimation corrects X% RMSE / +Y Kendall-τ over best sequential baseline on real benchmarks. Confounding Claim proven both formally (OVB observation) and empirically (real-data rank distortions). Framework Claim validated by convergence + diagnostics. Empirical Claim demonstrated across MT-Bench and Arena-Hard. Paper title emphasizes 'joint calibration corrects systematic rank distortions'. Headline: contamination and judge bias confound each other in practice, and only joint estimation resolves it.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gated_mfrm_judge_bias
venue: emnlp-2026
focus: Verify framing improvements: (1) Claim 2 now says "staged joint calibration" not "joint estimation", (2) Proposition 1 downgraded to Observation citing OVB, (3) new exp-012 error propagation sensitivity added, (4) expanded exp-004 rank change analysis, (5) new Reviewer Concerns 6-8 added. Check if these changes resolve the prior round's critical issues R1-N1 and R1-N2.

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

2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected "fair scores." (Note: "staged joint" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use "staged joint calibration" or "conditional joint estimation," never "fully joint.")

3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.

## Story Spine

- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.

- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. No existing work (0/12 surveyed papers, through May 2026) jointly models both within a single calibration framework.

- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.

- **Headline result template**: "On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles."

## Narrative Strategy (from distilled writing)

- **Type**: "突破局限" (sequential has structural flaw) + "统一框架" (G-MFRM unifies both corrections)
- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)
- **Section 2**: Toy example / formal **observation** (NOT "proposition" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method
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

4. **"DG-IRT transfer is trivial"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).

4b. **"Staged estimation ≠ joint estimation"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.

5. **"Contamination signal realistic?"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.

6. **"Chatbot Arena Elo as ground truth — circular reasoning?"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.

7. **"c_n ≥ 0 assumption too restrictive?"** — Half-Cauchy prior enforces non-negativity, appropriate for the "contamination as unfair advantage" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.

8. **"≥4 judges needed — too expensive?"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.

## Two-Tier Narrative (contingent on exp-005 contamination magnitude)

**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:
- Lead with ranking correction as primary contribution
- Claim 3 at full strength: "G-MFRM achieves X% higher Kendall-τ"
- Headline: joint estimation dramatically outperforms sequential

**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:
- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)
- Reframe: "even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)"
- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude
- Claim 3 softened to "comparable or better rankings PLUS interpretable diagnostic outputs"

exp-005 determines which tier. Decision point: after exp-005 results, before paper writing.

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
  name: item_exposure_estimation
  claim: 2
  description: 'Estimate per-item exposure e_i via three-source pipeline: (1) Primary:
    item-level performance gap between original items and GPT-5.5/Claude-rephrased
    reference variants, averaged across reference models, with spline difficulty correction
    (ConStat-inspired). (2) Temporal: performance gap on pre-cutoff vs post-cutoff
    item variants where available. (3) LogProber: token logprob memorization scores
    for models with logprob API. Sources combined via weighted composite (weights
    tuned on validation split). ConStat per-model delta used as external validation
    of fitted c_n, not as e_i source.'
  priority: P0
  gpu_budget_hours: 30
  deps:
  - exp-001
  notes: 'Main bottleneck: reference benchmark variant construction + quality validation.
    ConStat per-model delta validates G-MFRM c_n, not used for per-item e_i.'
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
  notes: 'NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,
    NCP, target_accept=0.95). Include per-benchmark analysis: if any benchmark has
    contamination ≈ 0, verify G-MFRM degrades gracefully to MFRM level (real-data
    graceful degradation check).'
  status: planned
- id: exp-004
  name: baseline_comparison
  claim: 3
  description: 'Compare G-MFRM against 8 baselines on same data: (1) raw multi-judge
    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) CyclicJudge
    + contaminated item discard, (6) DCR Factor, (7) UDA, (8) Preference Leakage calibration.
    Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena. MUST include rank change analysis:
    show which specific models change rank, by how many positions, and top-k stability
    (k=5,10).'
  priority: P0
  gpu_budget_hours: 20
  deps:
  - exp-003
  notes: 'Baseline (5) is the strongest trivial alternative — addresses Reviewer Concern
    #1. CyclicJudge/UDA/DCR/PrefLeakage need public code check. Budget may not include
    debug time. Rank change analysis addresses Dream R2-W3.'
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
    vs Stage 3 c_n as construct coherence validation. MUST also report: divergent
    transition count, posterior predictive check, trace plots for key parameters.'
  priority: P1
  gpu_budget_hours: 5
  deps:
  - exp-003
  status: planned
- id: exp-009
  name: confounding_formal_observation
  claim: 1
  description: 'Formal bias analysis: derive first-order bias approximation for sequential
    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation
    across realistic parameter ranges. For paper Section 2. Frame as ''Observation''
    (standard OVB from Angrist & Pischke 2009), not ''Proposition''. MUST include
    synthetic c_n point-estimate validation: generate data with known ground-truth
    c_n, fit G-MFRM, report per-model c_n RMSE and 95% credible interval coverage
    probability.'
  priority: P1
  gpu_budget_hours: 10
  deps: []
  notes: Can run in parallel with data collection. Extends MVP synthetic analysis.
    Downgraded from 'Proposition' to 'Observation' per Dream review. Synthetic c_n
    validation addresses Dream R1-N3.
  status: planned
- id: exp-012
  name: error_propagation_sensitivity
  claim: 2
  description: 'Sensitivity analysis for staged estimation: inject Gaussian noise
    into e_i estimates at σ=0.1,0.2,0.5 before Stage 3 fitting. Measure θ̂ RMSE degradation
    and c_n recovery accuracy. Shows three-stage pipeline is robust to e_i estimation
    error. Use synthetic data with known ground truth.'
  priority: P1
  gpu_budget_hours: 5
  deps: []
  notes: Addresses Dream R2-W5 and R1-N1. Can run on MVP codebase with modifications.
    Critical for defending staged estimation design choice.
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
  "promptId": "0dee52dc-7f8e-4286-b0d9-d30a9ebf13de",
  "type": "user",
  "uuid": "b237bcf8-e36d-4a80-a097-73421d3f3f3a",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T21:58:34.381Z_

```json
{
  "parentUuid": "b237bcf8-e36d-4a80-a097-73421d3f3f3a",
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
  "uuid": "01be91b6-be78-47ca-b513-7309369d412e",
  "timestamp": "2026-05-21T21:58:34.381Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T21:58:34.381Z_

```json
{
  "parentUuid": "01be91b6-be78-47ca-b513-7309369d412e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "3854e100-4ba4-4614-8978-0cb1dbaeee27",
  "timestamp": "2026-05-21T21:58:34.381Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real contamination magnitude matches mvp_002/003 assumptions (strong), G-MFRM converges cleanly on real data, and ranking correction is statistically and p…",
  "leafUuid": "3854e100-4ba4-4614-8978-0cb1dbaeee27",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Staged joint calibration corrects LLM judge bias and benchmark contamination",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f"
}
```

---

### Assistant

_source line 8 · 2026-05-21T21:58:51.141Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each planned experiment in the experiment plan, under the "best" tier (Tier A) assumptions. I need to provide result_rationale for each prediction explaining why we'd get those results under this scenario.

Let me carefully go through each experiment and generate realistic predictions consistent with:
- Real contamination magnitude matches mvp_002/003 assumptions (strong)
- G-MFRM converges cleanly on real data
- Ranking correction is statistically and practically significant

Key metrics ranges for "best" tier:
- real_contamination_c_n_median: [0.8, 1.5]


- kendall_tau_gmfrm: [0.88, 0.95]
- delta_tau_vs_best_baseline: [0.04, 0.08]
- rmse_reduction_vs_sequential_pct: [30, 50]
- convergence_max_rhat: [1.0, 1.05]
- convergence_min_ess: [200, 500]
- error_prop_theta_rmse_degradation_sigma02_pct: [0, 5]
- c_n_recovery_rmse_synthetic: [0.05, 0.15]

Now I'm laying out the expected performance ranges across convergence diagnostics, ranking accuracy, and parameter recovery metrics that define what success looks like under optimal conditions.

Looking at the remaining validation thresholds for ranking stability, judge count requirements, and Spearman correlation on held-out data. Now I'm ready to generate predictions for each experiment—starting with the infrastructure setup, then moving through item exposure estimation, the core G-MFRM fit on real data, baseline comparisons across eight methods, contamination sensitivity analysis, judge count degradation curves, ablation studies on exposure indicators, and the remaining experiments.

Writing YAML format...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3854e100-4ba4-4614-8978-0cb1dbaeee27",
  "isSidechain": false,
  "requestId": "req_011CbGTrDSJWRdDzR5Unqvy2",
  "type": "assistant",
  "uuid": "e8056cee-f485-439e-92e2-a21b8009a41f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yHuDPZn8uYCYyyuHVCTr4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11970,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16960,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16960,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11970
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

_source line 9 · 2026-05-21T22:03:46.986Z_

```yaml
tier: best
narrative_guidance: >
  Full Tier A narrative. Lead with quantitative shock: G-MFRM joint calibration corrects
  ~40% θ-RMSE and +5-6pp Kendall-τ over best sequential baseline on real MT-Bench/Arena-Hard
  data. Real contamination is strong (median c_n ≈ 0.95), validating the core premise that
  confounding is not a theoretical curiosity but a measurable distortion in current LLM
  evaluation practice. Paper title: "Joint Calibration of Judge Bias and Benchmark
  Contamination Corrects Systematic Rank Distortions in LLM Evaluation." Section 2 opens
  with the OVB observation on a 3-model toy example, then pivots to G-MFRM. Main result
  table is the centerpiece: G-MFRM beats all 8 baselines on both benchmarks, with
  CyclicJudge+discard as strongest competitor but still 4-5pp behind. Rank change analysis
  provides the narrative hook — at least 4 models shift ≥2 positions, and 2 top-5 models
  swap, making the correction practically consequential for deployment decisions. ConStat
  external validation (ρ≥0.78) closes the loop: fitted c_n is not a MCMC artifact but
  tracks an independently measurable contamination signal.

imagined_experiments:
  - name: multi_judge_data_collection
    plan_id: exp-001
    description: >
      Collect multi-judge evaluation data on MT-Bench (80 items × 20 target models × 8 judges
      × 2 positions) and Arena-Hard (500 items × 20 target models × 8 judges × 2 positions).
      Total ~185,600 pairwise judgments after position swap.
    expected_results:
      total_judgments: 185600
      mt_bench_judgments: 25600
      arena_hard_judgments: 160000
      target_models_evaluated: 20
      judges_used: 8
      judge_list: "GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro"
      position_bias_rate_mean: 0.58
      position_bias_rate_std: 0.07
      inter_judge_agreement_fleiss_kappa: 0.42
      api_cost_usd: 820
      vllm_gpu_hours: 95
      missing_data_rate_pct: 1.2
    result_rationale: >
      Best 档要求数据收集完整且质量高。8 个 judge 中 4 个开源（vLLM 部署）+ 4 个 API，
      覆盖不同模型族以最大化 judge 多样性。Position swap 产生 ~58% 的平均位置偏差率
      （与 CyclicJudge 2024 报告的 55-62% 一致），证明 position bias 是普遍存在的。
      Fleiss κ ≈ 0.42 表明 moderate agreement，与已发表的 LLM-as-judge 文献一致
      （Zheng et al. 2024 报告 κ=0.38-0.47）。缺失率 <2% 因为 API 调用有重试机制，
      vLLM 部署稳定。数据量足够支撑 G-MFRM 的参数估计（20 models × 8 judges ≫ 参数数）。
    tables:
      - name: "Table A1: Judge Panel Summary"
        columns: [judge, type, model_family, position_bias_rate, mean_score_stringency, cost_per_1k_judgments]
        rows:
          - [GPT-5.5, API, OpenAI, 0.55, 0.12, "$4.20"]
          - [Claude Opus 4.7, API, Anthropic, 0.61, -0.08, "$5.10"]
          - [Claude Sonnet 4.6, API, Anthropic, 0.54, 0.03, "$1.80"]
          - [DeepSeek-V4-Pro, API, DeepSeek, 0.63, -0.21, "$0.90"]
          - [Qwen3-235B-A22B, vLLM, Alibaba, 0.59, 0.18, "$0.35"]
          - [Qwen3.6-27B, vLLM, Alibaba, 0.56, 0.31, "$0.12"]
          - [Llama 4 Maverick, vLLM, Meta, 0.60, -0.15, "$0.28"]
          - [Gemini 2.5 Pro, API, Google, 0.57, 0.05, "$3.60"]
    figures_description:
      - "Fig A1: Heatmap of inter-judge agreement (Cohen κ pairwise) — 8×8 matrix showing
        judge clustering by model family. Anthropic judges cluster together (κ=0.56),
        indicating shared severity profile that G-MFRM's d_j facet should capture."
    analysis: >
      数据收集构成整个 pipeline 的基础。在 best 档下，所有 8 个 judge 正常工作，数据质量高。
      关键观察：judge 间一致性仅为 moderate（κ=0.42），且不同模型族的 judge 表现出系统性的
      severity 差异（score_stringency 从 -0.21 到 +0.31），证实了 judge bias 的存在且
      幅度足以影响排名。这为 G-MFRM 的 d_j facet 提供了充足的信号。

  - name: item_exposure_estimation
    plan_id: exp-002
    description: >
      构建 per-item exposure indicator e_i。三源融合：(1) Performance gap 主通道：
      对 MT-Bench/Arena-Hard 的每个 item 生成 GPT-5.5 和 Claude 改写的 reference variant，
      计算 original vs reference 的平均性能差并做 spline difficulty correction；
      (2) Temporal 通道：利用 pre/post-cutoff item variant 的性能差；
      (3) LogProber 通道：对有 logprob API 的模型计算 token-level memorization score。
      加权融合后输出 e_i ∈ [0,1]。
    expected_results:
      mt_bench_items_with_reference: 80
      arena_hard_items_with_reference: 485
      reference_variant_quality_human_check_pass_rate: 0.93
      performance_gap_signal_noise_ratio: 3.8
      temporal_signal_coverage_pct: 35
      logprober_signal_coverage_pct: 60
      weighted_composite_e_i_mean: 0.41
      weighted_composite_e_i_std: 0.28
      weighted_composite_e_i_median: 0.35
      high_exposure_items_e_gt_07_pct: 18
      spearman_gap_vs_logprober: 0.72
      spearman_gap_vs_temporal: 0.65
      spearman_composite_vs_constat_item_level: 0.68
    result_rationale: >
      Best 档下 real contamination 强，因此 performance gap 信号显著。对于高曝光 item
      （e_i > 0.7，约 18%），original 与 reference variant 的性能差在 contaminated model 上
      可达 0.3-0.5 标准差，经 difficulty correction 后信噪比约 3.8。这与 ConStat (2024) 报告
      的 r²=0.94 效应量一致——当 contamination 真实存在时，performance gap 方法有很强的
      检测力。Temporal 信号覆盖率较低（35%）因为只有部分 item 有明确的 pre/post-cutoff
      variant，但覆盖到的 item 与 gap 信号相关性好（ρ=0.65）。LogProber 覆盖 60%
      （仅限有 logprob API 的模型），与 gap 的相关性更高（ρ=0.72），因为两者都直接
      测量 memorization 效应。加权融合后 e_i 分布右偏（mean=0.41, median=0.35），
      符合大多数 item 低曝光、少数 item 高曝光的预期模式。
    tables:
      - name: "Table 2: Exposure Indicator Source Comparison"
        columns: [source, coverage_pct, mean_signal, snr, spearman_with_composite]
        rows:
          - [Performance Gap (primary), 100, 0.38, 3.8, 0.94]
          - [Temporal, 35, 0.42, 2.9, 0.78]
          - [LogProber, 60, 0.35, 4.1, 0.85]
          - [Weighted Composite, 100, 0.41, "-", 1.00]
    figures_description:
      - "Fig 3: Histogram of e_i distribution (MT-Bench + Arena-Hard combined) — right-skewed,
        with ~18% items above 0.7 threshold. Inset: scatter of performance gap vs LogProber
        score colored by benchmark, showing strong agreement (ρ=0.72)."
      - "Fig A2: Spline difficulty correction effect — before vs after correction scatter,
        showing removal of difficulty confound from raw performance gap."
    analysis: >
      e_i 估计质量是 staged estimation 可靠性的关键。在 best 档下，performance gap 主通道
      信噪比高（3.8），多源融合提供 robustness。18% 的 item 高曝光意味着约 100 个 item
      （MT-Bench + Arena-Hard）携带强 contamination 信号，足以支撑 c_n 的可辨识性。
      e_i 与 ConStat item-level 指标的 ρ=0.68 提供了外部效度验证。

  - name: gmfrm_real_data_fit
    plan_id: exp-003
    description: >
      在 exp-001/002 的真实数据上拟合 G-MFRM 三阶段 pipeline。Stage 1: 标准 MFRM 估计
      初始 θ,b,d。Stage 2: 固定 exp-002 的 e_i。Stage 3: NumPyro MCMC 联合估计
      θ,b,d,c_n（e_i 固定）。报告收敛诊断、fair score、与 Chatbot Arena 的 Kendall-τ。
    expected_results:
      convergence_max_rhat: 1.03
      convergence_min_ess: 287
      convergence_divergent_transitions: 0
      mcmc_warmup: 2000
      mcmc_samples: 4000
      mcmc_chains: 4
      runtime_hours: 3.2
      theta_fair_score_kendall_tau_arena_mtbench: 0.91
      theta_fair_score_kendall_tau_arena_arenahard: 0.93
      theta_fair_score_spearman_arena_mtbench: 0.94
      theta_fair_score_spearman_arena_arenahard: 0.96
      c_n_median: 0.95
      c_n_mean: 1.02
      c_n_std: 0.48
      c_n_max: 2.1
      c_n_min: 0.08
      d_j_range: [-0.35, 0.42]
      d_j_std: 0.22
      posterior_predictive_p_value: 0.47
      graceful_degradation_low_contam_benchmark_tau_delta: 0.005
    result_rationale: >
      Best 档的核心假设是 G-MFRM 在真实数据上干净收敛。mvp_003 已在合成数据上实现
      R̂=1.03, ESS=224；真实数据的维度更大（20 models × 580 items × 8 judges vs
      合成的 15×50×8）但信号也更丰富。使用相同的 MCMC 设置（warmup=2000, samples=4000,
      chains=4, NCP, target_accept=0.95）加上更大的数据量，ESS 提升至 287 是合理的。
      R̂=1.03 与合成结果持平。c_n median=0.95 落在 best 档的 [0.8,1.5] 范围内，接近
      mvp_002/003 的假设（c~1.0-1.5）。c_n 的模型间变异大（std=0.48, max=2.1）反映了
      现实中不同模型的 contamination 程度差异巨大——开源模型（训练数据不透明）倾向于
      更高的 c_n，而 closed-source 模型（如 GPT-5.5）的 c_n 较低。Kendall-τ 在
      Arena-Hard 上（0.93）高于 MT-Bench（0.91）因为 Arena-Hard 有更多 item 提供更精确
      的 ability 估计。posterior predictive p=0.47 表明模型拟合良好（接近 0.5 的均匀分布）。
      对于 contamination 接近 0 的 benchmark 子集，G-MFRM 的 τ 仅比 MFRM 高 0.005，
      验证了 graceful degradation——gating 机制在 e_i≈0 时自动关闭 contamination 校正。
    tables:
      - name: "Table 3: G-MFRM Convergence Diagnostics"
        columns: [parameter_group, n_params, max_rhat, min_ess, mean_ess]
        rows:
          - [θ (model ability), 20, 1.02, 312, 890]
          - [b (item difficulty), 580, 1.03, 287, 650]
          - [d (judge severity), 8, 1.01, 1450, 2100]
          - [c (contamination), 20, 1.03, 295, 720]
      - name: "Table 4: G-MFRM Fair Score Agreement with Chatbot Arena"
        columns: [benchmark, kendall_tau, spearman_rho, "95% CI (τ)"]
        rows:
          - [MT-Bench, 0.91, 0.94, "[0.86, 0.95]"]
          - [Arena-Hard, 0.93, 0.96, "[0.89, 0.96]"]
          - [Combined (weighted), 0.92, 0.95, "[0.88, 0.95]"]
    figures_description:
      - "Fig 2: G-MFRM parameter estimates visualization. Left: θ̂ (fair score) vs Chatbot
        Arena Elo with 95% credible intervals — tight linear relationship. Right: c_n
        estimates with credible intervals, sorted by magnitude — clear separation between
        high-contamination and low-contamination models."
      - "Fig A3: Trace plots for 4 representative parameters (one per facet) showing clean
        mixing across 4 chains. No divergent transitions."
      - "Fig A4: Posterior predictive check — observed vs predicted response distribution
        histograms showing good calibration (p=0.47)."
    analysis: >
      这是整个论文的核心实验。收敛诊断全面通过（R̂≤1.03, ESS≥287, 0 divergent transitions）
      证明 G-MFRM 的参数化在真实数据规模上是可行的。c_n median=0.95 确认 Tier A 叙事：
      contamination 不是理论上的可能性，而是量级足够大到系统性扭曲排名的现实问题。
      d_j 的范围 [-0.35, 0.42] 表明最 lenient 和最 strict 的 judge 之间存在 0.77 标准差
      的 severity 差异，足以影响 model ranking。

  - name: baseline_comparison
    plan_id: exp-004
    description: >
      在相同数据上对比 G-MFRM 与 8 个 baseline 的排名准确性。包含 rank change 分析：
      哪些模型在校正后排名变化 ≥2 位，top-5/top-10 稳定性。
    expected_results:
      raw_avg_kendall_tau_mtbench: 0.82
      raw_avg_kendall_tau_arenahard: 0.84
      mfrm_only_kendall_tau_mtbench: 0.84
      mfrm_only_kendall_tau_arenahard: 0.86
      sequential_kendall_tau_mtbench: 0.85
      sequential_kendall_tau_arenahard: 0.87
      cyclic_judge_kendall_tau_mtbench: 0.85
      cyclic_judge_kendall_tau_arenahard: 0.87
      cyclic_judge_discard_kendall_tau_mtbench: 0.87
      cyclic_judge_discard_kendall_tau_arenahard: 0.88
      dcr_factor_kendall_tau_mtbench: 0.83
      dcr_factor_kendall_tau_arenahard: 0.85
      uda_kendall_tau_mtbench: 0.86
      uda_kendall_tau_arenahard: 0.87
      pref_leakage_kendall_tau_mtbench: 0.84
      pref_leakage_kendall_tau_arenahard: 0.86
      gmfrm_kendall_tau_mtbench: 0.91
      gmfrm_kendall_tau_arenahard: 0.93
      delta_tau_vs_best_baseline_mtbench: 0.04
      delta_tau_vs_best_baseline_arenahard: 0.05
      wilcoxon_p_gmfrm_vs_best_baseline: 0.003
      rank_changes_ge2_positions: 5
      rank_changes_ge3_positions: 2
      top5_models_changed: 2
      top10_models_changed: 4
      max_rank_shift: 4
      most_shifted_model: "Qwen3-235B-A22B"
      most_shifted_direction: "down"
    result_rationale: >
      Best 档下 G-MFRM 以显著优势击败所有 baseline。逻辑链：
      (1) Raw average（τ=0.82/0.84）最差，因为同时受 judge bias 和 contamination 影响。
      (2) MFRM-only（+2pp）校正了 judge bias 但 contamination 仍在。
      (3) Sequential（+3pp over raw）先 bias 后 contamination，但因 OVB 效应，第一阶段
      的 bias 校正已被 contamination 污染，改善有限。
      (4) CyclicJudge（≈sequential level）通过 round-robin 消除平均 bias，但无法处理
      item-specific judge 效应，且完全忽略 contamination。
      (5) CyclicJudge+discard（最强 baseline，τ=0.87/0.88）额外丢弃高疑似 contaminated
      items，但丢弃策略浪费信息且阈值任意——best 档下它仍比 G-MFRM 低 4-5pp。
      (6) DCR Factor（τ=0.83/0.85）量化 contamination 效应但忽略 judge variation。
      (7) UDA（τ=0.86/0.87）神经 K-factor 调整 inter-judge variance 但黑盒且不 model
      contamination。
      (8) Pref Leakage（τ=0.84/0.86）校准偏好泄漏但不联合估计。
      G-MFRM（τ=0.91/0.93）的优势来自联合估计：同时建模 d_j 和 c_n·e_i 避免了相互吸收。
      Rank change 分析：c_n 高的开源模型（如 Qwen3-235B-A22B）在校正后排名下降
      （contamination 膨胀被移除），而 c_n 低的 closed-source 模型相对上升。5 个模型
      移动 ≥2 位，最大移动 4 位，top-5 中有 2 个交换——这对模型选择决策有实质性影响。
    tables:
      - name: "Table 1: Main Results — Agreement with Chatbot Arena Human Rankings"
        columns: [method, type, "τ (MT-Bench)", "τ (Arena-Hard)", "τ (Combined)", "Δτ vs G-MFRM"]
        rows:
          - [Raw Multi-Judge Avg, naive, 0.82, 0.84, 0.83, -0.09]
          - [MFRM-only, bias-only, 0.84, 0.86, 0.85, -0.07]
          - [Sequential (bias→contam), sequential, 0.85, 0.87, 0.86, -0.06]
          - [CyclicJudge, bias-only, 0.85, 0.87, 0.86, -0.06]
          - [CyclicJudge + Discard, bias+heuristic, 0.87, 0.88, 0.875, -0.045]
          - [DCR Factor, contam-only, 0.83, 0.85, 0.84, -0.08]
          - [UDA, bias-only (neural), 0.86, 0.87, 0.865, -0.055]
          - [Pref Leakage Calib, contam-only, 0.84, 0.86, 0.85, -0.07]
          - [G-MFRM (ours), joint, 0.91, 0.93, 0.92, "—"]
      - name: "Table 5: Rank Change Analysis (G-MFRM vs Raw Average)"
        columns: [model, raw_rank, gmfrm_rank, shift, c_n_estimate, interpretation]
        rows:
          - [Qwen3-235B-A22B, 3, 7, -4, 1.82, "High contamination inflated raw rank"]
          - [Llama 4 Maverick, 5, 8, -3, 1.45, "Moderate-high contamination"]
          - [Model-X-70B, 8, 5, +3, 0.12, "Low contamination — undervalued by raw"]
          - [Claude Sonnet 4.6, 4, 2, +2, 0.21, "Low contamination — rose after correction"]
          - [DeepSeek-V4-Pro, 6, 4, +2, 0.35, "Modest contamination — net rise"]
    figures_description:
      - "Fig 1 (main): Left panel — sequential pipeline diagram with confounding arrows annotated.
        Right panel — G-MFRM three-stage pipeline with gating mechanism highlighted.
        Visual contrast between 'broken' sequential and 'correct' joint approach."
      - "Fig 4: Bump chart showing rank changes from raw average to G-MFRM fair score for all
        20 target models. Lines colored by c_n magnitude. High-c_n models (red) consistently
        drop, low-c_n models (blue) rise. 5 models cross ≥2 positions."
      - "Fig 5: Bar chart of Kendall-τ with Chatbot Arena for all 9 methods on both benchmarks.
        G-MFRM clearly separated from the cluster of baselines. Error bars from bootstrap."
    analysis: >
      这是论文的主表。G-MFRM 在两个 benchmark 上一致地以 4-5pp τ 优势击败最强 baseline
      （CyclicJudge+discard），p=0.003（Wilcoxon）。关键叙事：CyclicJudge+discard 是
      Reviewer Concern #1 的最强 trivial alternative，但它 (a) 浪费被丢弃 item 的信息，
      (b) 不产生 per-model c_n 诊断，(c) 丢弃阈值需要启发式调优。G-MFRM 在所有维度上
      都优于它。Rank change 分析提供了实际影响力的证据：如果一个团队基于 raw score 选择
      了 rank-3 的 Qwen3-235B 而非 rank-7 的 Model-X-70B，他们可能选择了一个 contamination
      膨胀的模型，真实 ability 其实更低。

  - name: contamination_magnitude_calibration
    plan_id: exp-005
    description: >
      比较 exp-003 拟合的真实 c_n 分布与 MVP 合成假设，确定 contamination 处于哪个 tier。
      用 ConStat per-model delta 做外部验证。
    expected_results:
      c_n_median_real: 0.95
      c_n_mean_real: 1.02
      c_n_q25: 0.42
      c_n_q75: 1.48
      c_n_iqr: 1.06
      models_with_c_n_gt_1: 8
      models_with_c_n_gt_05: 14
      models_with_c_n_lt_02: 3
      closest_mvp_scenario: "mvp_002/003 (strong)"
      constat_delta_spearman_with_c_n: 0.82
      constat_delta_pearson_with_c_n: 0.78
      tier_determination: "Tier A"
      ratio_real_vs_mvp003_median: 0.95
    result_rationale: >
      Best 档的核心前提是 real contamination 强度匹配 mvp_002/003 假设。c_n median=0.95
      非常接近 mvp_003 的设定（c~1.0）。这意味着对于一个典型的高曝光 item（e_i=0.8），
      contaminated model 的 expected score 膨胀约 0.76 logits（0.95×0.8），这是一个
      非常显著的效应，足以将一个中等 ability 模型提升 2-4 个排名位。14/20 个模型的
      c_n > 0.5 表明 contamination 是广泛存在的，不仅仅是个别模型的问题。ConStat 外部
      验证 ρ=0.82 在 best 档范围 [0.7, 0.95] 内偏高，说明 G-MFRM 拟合的 c_n 与独立的
      ConStat contamination 指标高度一致——这不是 MCMC 的 artifact，而是捕捉到了真实的
      contamination 结构。3 个模型 c_n < 0.2（基本无 contamination）提供了自然的负对照。
    tables:
      - name: "Table 6: Contamination Magnitude — Real vs Synthetic"
        columns: [scenario, c_n_median, c_n_mean, c_n_std, convergence, kendall_tau_gain]
        rows:
          - [mvp_001 (weak), 0.50, 0.52, 0.15, PASS, "+0.3pp (n.s.)"]
          - [mvp_002 (strong, poor convergence), 1.20, 1.25, 0.40, FAIL, "+4.3pp"]
          - [mvp_003 (strong, tuned), 1.00, 1.05, 0.35, PASS, "+6.3pp"]
          - [Real Data (exp-003), 0.95, 1.02, 0.48, PASS, "+4.5pp"]
      - name: "Table 7: ConStat External Validation"
        columns: [metric, value, "95% CI"]
        rows:
          - [Spearman ρ (c_n vs ConStat Δ), 0.82, "[0.65, 0.92]"]
          - [Pearson r (c_n vs ConStat Δ), 0.78, "[0.58, 0.89]"]
          - [Concordance (top-5 c_n ∩ top-5 ConStat), "4/5", "—"]
    figures_description:
      - "Fig 6: Scatter of G-MFRM fitted c_n vs ConStat per-model delta with regression line
        and 95% CI band. Points labeled with model names. Strong positive relationship
        (ρ=0.82) validates c_n against independent contamination measure."
      - "Fig A5: c_n posterior distributions for all 20 models (violin plot), sorted by median.
        Clear separation between contamination clusters."
    analysis: >
      此实验是 Tier A/B 决策点。c_n median=0.95 明确指向 Tier A。与 mvp_003 的比较
      显示真实数据几乎完美匹配合成假设（ratio=0.95），验证了 MVP 阶段的参数校准。
      ConStat 验证（ρ=0.82）是论文的关键防线：它证明 c_n 不是模型过拟合的产物，
      而是与独立测量工具一致的真实信号。top-5 concordance（4/5）特别有说服力——
      G-MFRM 和 ConStat 几乎完全同意哪些模型受 contamination 影响最大。

  - name: judge_count_sensitivity
    plan_id: exp-006
    description: >
      敏感性分析：逐步减少 judge 数量（8→6→4→2），观察 G-MFRM 性能退化曲线。
      确定 G-MFRM 优于 sequential 的最低 judge 数量。
    expected_results:
      tau_8_judges: 0.92
      tau_6_judges: 0.905
      tau_4_judges: 0.885
      tau_3_judges: 0.87
      tau_2_judges: 0.84
      sequential_tau_8_judges: 0.865
      sequential_tau_4_judges: 0.855
      sequential_tau_2_judges: 0.845
      min_judges_for_significant_gain: 3
      degradation_rate_per_judge_removed: 0.012
      gmfrm_2_judge_vs_mfrm_2_judge_delta: 0.005
      convergence_failure_at_2_judges: false
      convergence_rhat_at_2_judges: 1.08
    result_rationale: >
      G-MFRM 需要多 judge 数据来分离 d_j 和 c_n·e_i。在 best 档下，8 judges 提供
      丰富信号（τ=0.92）。减至 6 judges 损失温和（-1.5pp），因为仍有足够的 judge
      变异来估计 d_j。减至 4 judges 是关键拐点（-3.5pp），但仍比 sequential 4-judge（0.855）
      好 3pp。3 judges 是 G-MFRM 显著优于 sequential 的最低阈值——对应 best 档的
      judge_count_min_for_significant_gain=[3,4] 范围。2 judges 时 G-MFRM 基本退化到
      MFRM 水平（delta 仅 0.5pp），因为 2 个 judge 不足以可靠估计 d_j，gating 机制
      也因信号不足而趋于保守。R̂ 在 2-judge 时升至 1.08，刚好超过阈值，但未发散。
      这回应了 Reviewer Concern #8：在 2-judge 场景下 G-MFRM 不会崩溃，只是退化到
      MFRM baseline 水平。
    tables:
      - name: "Table 8: Judge Count Sensitivity"
        columns: [n_judges, "τ (G-MFRM)", "τ (Sequential)", "Δτ", "p-value", max_rhat, min_ess]
        rows:
          - [8, 0.920, 0.865, +0.055, 0.003, 1.03, 287]
          - [6, 0.905, 0.860, +0.045, 0.008, 1.03, 245]
          - [4, 0.885, 0.855, +0.030, 0.021, 1.04, 198]
          - [3, 0.870, 0.852, +0.018, 0.048, 1.05, 165]
          - [2, 0.840, 0.845, -0.005, 0.62, 1.08, 89]
    figures_description:
      - "Fig 7: Line plot of Kendall-τ vs number of judges for G-MFRM (solid) and Sequential
        (dashed). Shaded region shows 95% CI. Lines cross at ~2.5 judges. Annotation at
        J=3 marks minimum significant advantage point."
    analysis: >
      此分析为实践者提供了成本效益指导。结论清晰：≥4 judges 推荐（G-MFRM gain ~3pp+），
      3 judges 勉强可行（gain 1.8pp, p<0.05），2 judges 不建议用 G-MFRM（退化至 MFRM）。
      这回应了 Reviewer Concern #8 的成本问题，并为 Limitations 提供了量化数据。

  - name: exposure_indicator_ablation
    plan_id: exp-007
    description: >
      对 e_i 估计 pipeline 做 leave-one-out 消融：分别去掉 performance gap、temporal、
      LogProber 中的一个 source，观察对最终 θ̂ 和 c_n 估计质量的影响。
    expected_results:
      full_pipeline_theta_tau: 0.92
      without_performance_gap_theta_tau: 0.87
      without_temporal_theta_tau: 0.915
      without_logprober_theta_tau: 0.91
      full_pipeline_cn_recovery_spearman: 0.82
      without_performance_gap_cn_recovery_spearman: 0.55
      without_temporal_cn_recovery_spearman: 0.80
      without_logprober_cn_recovery_spearman: 0.78
      performance_gap_contribution_pct: 72
      temporal_contribution_pct: 8
      logprober_contribution_pct: 12
      interaction_effect_pct: 8
    result_rationale: >
      Performance gap 是 e_i 的主通道（100% 覆盖，SNR=3.8），去掉后 τ 下降 5pp——
      这是因为没有 gap 信号，e_i 估计退化为 temporal+LogProber 的稀疏覆盖
      （仅 35%+60% 项有信号，交集更小），大量 item 的 e_i 几乎无信息。相反，去掉
      temporal 或 LogProber 各自影响很小（-0.5pp 和 -1pp），因为它们是补充信号，
      覆盖率有限。但 c_n recovery 的 spearman 对 performance gap 的依赖更强
      （Δρ=0.27 vs Δρ=0.02/0.04），因为 c_n 的可辨识性直接依赖于 e_i 的准确性——
      e_i 差则 c_n·e_i 项无法正确分离 c_n。这证明了 performance gap 是不可或缺的，
      而 temporal 和 LogProber 是有用但非必要的补充。
    tables:
      - name: "Table 9: Exposure Indicator Ablation"
        columns: [configuration, "τ (Arena)", "Δτ", "c_n ρ", "Δρ"]
        rows:
          - [Full pipeline (3 sources), 0.920, "—", 0.82, "—"]
          - [− Performance Gap, 0.870, -0.050, 0.55, -0.27]
          - [− Temporal, 0.915, -0.005, 0.80, -0.02]
          - [− LogProber, 0.910, -0.010, 0.78, -0.04]
          - [Gap only, 0.912, -0.008, 0.79, -0.03]
    figures_description:
      - "Fig A6: Stacked bar chart showing relative contribution of each e_i source.
        Performance gap dominates (72%), with LogProber (12%) and Temporal (8%)
        providing marginal but consistent improvements."
    analysis: >
      消融结果支持 pipeline 设计的合理性。Performance gap 是必要条件（去掉后严重退化），
      而 temporal 和 LogProber 提供边际改进。"Gap only" 配置仅比 full pipeline 低 0.8pp，
      说明如果资源有限，只使用 performance gap 也是可行的最小方案。这为实践者提供了
      模块化部署指导。

  - name: facet_fit_diagnostics
    plan_id: exp-008
    description: >
      报告 G-MFRM 所有 facet 的测量质量诊断：infit/outfit MNSQ、divergent transitions、
      posterior predictive check、trace plots。标记 misfit 元素。
    expected_results:
      theta_infit_mean: 1.02
      theta_infit_range: [0.85, 1.18]
      theta_outfit_mean: 1.05
      theta_outfit_range: [0.78, 1.35]
      theta_misfit_count: 1
      b_infit_mean: 1.00
      b_infit_range: [0.72, 1.42]
      b_outfit_mean: 1.03
      b_outfit_range: [0.65, 1.55]
      b_misfit_count: 12
      d_infit_mean: 0.98
      d_infit_range: [0.88, 1.10]
      d_outfit_mean: 1.01
      d_outfit_range: [0.85, 1.15]
      d_misfit_count: 0
      c_infit_mean: 1.04
      c_infit_range: [0.82, 1.25]
      divergent_transitions: 0
      posterior_predictive_ppp: 0.47
      posterior_predictive_rmse: 0.18
      stage1_lz_flagged_models: 2
      stage3_cn_gt_0_for_lz_flagged: true
    result_rationale: >
      Best 档要求诊断全面良好。Infit/outfit MNSQ 接近 1.0 表示 Rasch 模型拟合良好。
      Item facet（b）有 12 个 misfit（outfit > 1.4 的 item），占 580 items 的 ~2%，
      这在 IRT 实践中是正常水平——这些 item 可能有特殊结构（如依赖特定领域知识）
      导致模型不完全适用。1 个 θ misfit 模型可能是有异常评分模式的 target model。
      Judge facet（d）完全无 misfit（仅 8 个 judge，且都是主流 LLM），这符合预期。
      0 divergent transitions 和 PPP=0.47 证实整体模型规范正确。Stage 1 的 person-fit
      指标（lz）标记了 2 个模型，Stage 3 中这 2 个模型都有 c_n > 0（分别为 1.2 和 0.8），
      证实了 construct coherence：Stage 1 的 misfit 信号确实来自 contamination 而非
      ability 维度的问题。
    tables:
      - name: "Table A2: Facet Fit Summary (Infit/Outfit MNSQ)"
        columns: [facet, n, mean_infit, mean_outfit, misfit_count, "misfit_%"]
        rows:
          - [θ (model ability), 20, 1.02, 1.05, 1, 5.0]
          - [b (item difficulty), 580, 1.00, 1.03, 12, 2.1]
          - [d (judge severity), 8, 0.98, 1.01, 0, 0.0]
          - [c (contamination), 20, 1.04, "—", 0, 0.0]
      - name: "Table A3: MCMC Diagnostics Summary"
        columns: [diagnostic, value, threshold, status]
        rows:
          - [Max R̂, 1.03, "≤ 1.05", PASS]
          - [Min ESS, 287, "≥ 200", PASS]
          - [Divergent transitions, 0, "= 0", PASS]
          - [PPP, 0.47, "[0.1, 0.9]", PASS]
          - [Posterior predictive RMSE, 0.18, "—", "—"]
    figures_description:
      - "Fig A7: Wright map (variable map) showing θ, b, d, c on common logit scale.
        Good coverage — item difficulties span the model ability range."
      - "Fig A8: Infit/outfit bubble chart for all items, colored by benchmark.
        12 misfit items highlighted with IDs for examination."
      - "Fig A3 (ref): Trace plots for representative parameters across 4 chains."
    analysis: >
      诊断全面支持 G-MFRM 的测量质量。2.1% 的 item misfit 率在 IRT 文献中属于正常范围。
      Stage 1 lz → Stage 3 c_n 的 coherence 是一个巧妙的验证：如果 person-fit 异常
      是由 contamination 引起的，那么在建模 contamination 后应该被解释掉——实验证实了这一点。

  - name: confounding_formal_observation
    plan_id: exp-009
    description: >
      形式化推导 sequential estimator 在 d_j 和 c_n·e_i 非正交条件下的一阶 bias
      近似。Monte Carlo 验证。合成数据上的 c_n 点估计验证。
    expected_results:
      bias_first_order_formula: "bias(θ̂_seq) ≈ Σ_j (X'X)^{-1} X' Cov(d_j, c_n·e_i)"
      monte_carlo_n_reps: 500
      monte_carlo_bias_mean_rho_0: 0.001
      monte_carlo_bias_mean_rho_03: 0.048
      monte_carlo_bias_mean_rho_06: 0.112
      monte_carlo_bias_std_rho_06: 0.035
      monte_carlo_rmse_degradation_rho_06_pct: 43.2
      synthetic_cn_recovery_rmse: 0.09
      synthetic_cn_coverage_95ci: 0.93
      synthetic_cn_spearman_recovery: 0.96
      synthetic_cn_bias: -0.02
    result_rationale: >
      形式化分析是标准 OVB 理论在 LLM 评估场景的应用。当 d_j 和 c_n·e_i 正交
      （ρ=0）时，bias ≈ 0（0.001 是有限样本噪声），sequential 无害。但在现实中，
      judge 的 severity 和 model 的 contamination susceptibility 不独立——harsh judges
      可能对 contaminated 回答更 lenient（因为 contaminated 回答通常更流畅、更自信），
      导致 ρ > 0。在 ρ=0.6 时（mvp 模拟的现实估计），RMSE 退化 43.2%，与 mvp_003 的
      43.8% 高度一致。合成 c_n recovery 的 RMSE=0.09 落在 best 档范围 [0.05, 0.15] 内，
      95% CI coverage=0.93（接近 nominal 0.95），说明贝叶斯推断的 uncertainty
      quantification 是准确的。ρ_recovery=0.96 表明即使点估计有噪声，排序几乎完美保留。
    tables:
      - name: "Table 10: Monte Carlo Bias Analysis (500 replications)"
        columns: [ρ(d,ce), "bias(θ̂_seq)", "θ RMSE (seq)", "θ RMSE (joint)", "RMSE reduction %"]
        rows:
          - [0.0, 0.001, 0.124, 0.123, 0.8]
          - [0.15, 0.021, 0.138, 0.124, 10.1]
          - [0.3, 0.048, 0.162, 0.125, 22.8]
          - [0.45, 0.078, 0.189, 0.124, 34.4]
          - [0.6, 0.112, 0.221, 0.125, 43.2]
      - name: "Table 11: Synthetic c_n Recovery (G-MFRM)"
        columns: [metric, value]
        rows:
          - [c_n RMSE, 0.09]
          - [c_n bias, -0.02]
          - [c_n Spearman ρ (fitted vs true), 0.96]
          - ["95% CI coverage", 0.93]
          - ["Mean CI width", 0.38]
    figures_description:
      - "Fig 2 (Section 2): Toy example illustrating OVB in sequential estimation.
        3 models, 2 judges, 2 contamination levels. Visual proof that bias-first
        estimation absorbs contamination into θ̂."
      - "Fig A9: Monte Carlo bias as function of ρ(d,ce) — smooth monotonic increase
        with 95% band from 500 replications. G-MFRM bias stays flat near 0."
      - "Fig A10: c_n recovery scatter (fitted vs true) for 20 synthetic models — tight
        clustering around identity line with 95% credible intervals."
    analysis: >
      此实验为 Confounding Claim 提供形式化+实证双重支持。OVB observation 是已有理论
      的直接应用，不需要 novelty——关键贡献是证明这个理论问题在 LLM 评估中量级显著
      （43.2% RMSE 退化）。c_n recovery 验证确认 G-MFRM 不仅纠正了 θ̂ bias，还能
      准确恢复潜在的 contamination 结构，coverage probability 接近 nominal 说明
      posterior inference 是 well-calibrated 的。

  - name: error_propagation_sensitivity
    plan_id: exp-012
    description: >
      Staged estimation 的误差传播敏感性：向 e_i 注入 σ=0.1/0.2/0.5 的高斯噪声后
      重新拟合 Stage 3，测量 θ̂ RMSE 退化和 c_n recovery 精度。合成数据。
    expected_results:
      sigma_0_theta_rmse: 0.124
      sigma_01_theta_rmse: 0.127
      sigma_01_theta_rmse_degradation_pct: 2.4
      sigma_02_theta_rmse: 0.133
      sigma_02_theta_rmse_degradation_pct: 7.3
      sigma_05_theta_rmse: 0.168
      sigma_05_theta_rmse_degradation_pct: 35.5
      sigma_0_cn_rmse: 0.09
      sigma_01_cn_rmse: 0.12
      sigma_02_cn_rmse: 0.18
      sigma_05_cn_rmse: 0.41
      sigma_02_cn_spearman: 0.89
      sigma_05_cn_spearman: 0.62
      robustness_threshold_sigma: 0.25
    result_rationale: >
      Best 档要求 σ=0.2 时 θ̂ RMSE 退化 < 5%。预测值 7.3% 略超此阈值，但仍属于
      实际可接受范围（需在论文中 acknowledge）。逻辑：e_i 噪声通过 c_n·e_i 项传播到
      θ̂——当 σ 小（0.1）时，e_i 的 rank order 基本保持，gating 机制仅微调幅度，
      对 θ̂ 影响很小（2.4%）。σ=0.2 时 e_i 的 rank 开始受扰动，部分
      high-exposure item 被错误降权、low-exposure item 被错误升权，导致 c_n 估计
      偏移（RMSE 从 0.09→0.18），但因为 θ̂ 同时受多个 item 信息约束（580 items），
      单个 item 的 e_i 误差被平均化，θ̂ 退化相对温和。σ=0.5 是破坏性水平（35.5% 退化），
      此时 e_i 信号几乎被噪声淹没。robustness_threshold ≈ 0.25 意味着 exp-002 的 e_i
      估计只要噪声不超过 0.25 就安全——考虑到 performance gap 的 SNR=3.8，实际噪声
      约 σ≈0.15，处于安全区内。注意：σ=0.2 处 θ̂ degradation 为 7.3% 而非 <5%。
      在论文中需诚实报告，但可论证 (a) 这是 worst-case 均匀噪声注入，实际噪声结构更
      favorable，(b) 7.3% degradation 仍使 G-MFRM 大幅优于 sequential baseline。
    tables:
      - name: "Table 12: Error Propagation Sensitivity (Synthetic)"
        columns: [e_i_noise_σ, "θ̂ RMSE", "θ̂ degrad. %", "c_n RMSE", "c_n ρ", "τ (Arena proxy)"]
        rows:
          - [0.0, 0.124, "—", 0.09, 0.96, 0.922]
          - [0.1, 0.127, 2.4, 0.12, 0.94, 0.918]
          - [0.2, 0.133, 7.3, 0.18, 0.89, 0.910]
          - [0.3, 0.145, 16.9, 0.27, 0.79, 0.893]
          - [0.5, 0.168, 35.5, 0.41, 0.62, 0.862]
    figures_description:
      - "Fig 8: Dual-axis plot — θ̂ RMSE degradation % (left axis, blue) and c_n Spearman ρ
        (right axis, red) as function of e_i noise σ. Dashed vertical line at σ=0.25
        marks robustness threshold. Shaded green region shows estimated real-data noise level
        (σ ≈ 0.12-0.18)."
    analysis: >
      此实验是 Reviewer Concern #4b 和 Dream R1-N1 的核心回应。结论：staged estimation
      在 σ≤0.2 时 robust（θ̂ 退化 <8%），在 σ≤0.1 时几乎无损（<2.5%）。exp-002 的
      实际 e_i 噪声估计约 σ=0.15（基于 SNR=3.8 和 multi-source 融合），落在安全区内。
      σ=0.5 的崩溃点提供了理论下界。论文 Limitations 中需讨论 σ=0.2 处的 7.3% 超过了
      预设 5% 阈值，但结合实际噪声水平论证 staged estimation 的可接受性。

  - name: wildbench_replication
    plan_id: exp-010
    description: >
      在 WildBench 上复制完整 G-MFRM pipeline 作为第三个 benchmark，验证跨 benchmark
      泛化性。
    expected_results:
      wildbench_items: 1024
      wildbench_judges_used: 6
      gmfrm_kendall_tau_wildbench: 0.90
      sequential_kendall_tau_wildbench: 0.86
      delta_tau_wildbench: 0.04
      c_n_spearman_wildbench_vs_mtbench: 0.88
      convergence_max_rhat: 1.04
      convergence_min_ess: 210
      wildbench_high_exposure_items_pct: 14
    result_rationale: >
      WildBench 是更 "wild" 的 benchmark（用户真实 query），contamination 模式应与
      MT-Bench/Arena-Hard 不同但 G-MFRM 方法论应仍然有效。best 档下 τ=0.90（略低于
      Arena-Hard 的 0.93），因为 WildBench 的 item 更异质、标注噪声更大。Δτ=0.04
      与 MT-Bench 上的 0.04 一致，证明 G-MFRM 的优势不是 benchmark-specific 的。
      c_n 在 WildBench 和 MT-Bench 之间的 ρ=0.88 说明同一组模型的 contamination
      susceptibility 跨 benchmark 是稳定的——这是一个重要的 construct validity 证据，
      说明 c_n 测量的是模型的固有属性而非 benchmark-specific artifact。仅使用 6 个
      judge（2 个 API 不支持 WildBench 格式）但收敛仍然良好。
    tables:
      - name: "Table 13: Cross-Benchmark Generalization"
        columns: [benchmark, "τ (G-MFRM)", "τ (Best Baseline)", "Δτ", items, judges]
        rows:
          - [MT-Bench, 0.91, 0.87, +0.04, 80, 8]
          - [Arena-Hard, 0.93, 0.88, +0.05, 500, 8]
          - [WildBench, 0.90, 0.86, +0.04, 1024, 6]
    figures_description:
      - "Fig A11: c_n estimates scatter — WildBench vs MT-Bench. Strong agreement (ρ=0.88)
        demonstrates contamination susceptibility is a stable model property across benchmarks."
    analysis: >
      跨 benchmark 复制成功。三个 benchmark 上 G-MFRM 一致优于 best baseline 4-5pp，
      消除了 "方法只在特定 benchmark 上有效" 的顾虑。c_n 跨 benchmark 稳定性是
      bonus finding：可以在 Discussion 中论证 c_n 有作为 "model contamination audit
      index" 的潜力。

  - name: adversarial_robustness
    plan_id: exp-011
    description: >
      测试 G-MFRM 对抗 adversarial contamination 的鲁棒性，遵循 Wang et al. (ICLR 2026)
      的 fragility analysis 框架。
    expected_results:
      adversarial_attack_types: 3
      attack1_targeted_item_injection_theta_shift: 0.15
      attack2_judge_collusion_theta_shift: 0.22
      attack3_exposure_manipulation_theta_shift: 0.08
      gmfrm_detection_rate_attack1: 0.85
      gmfrm_detection_rate_attack2: 0.70
      gmfrm_detection_rate_attack3: 0.90
      sequential_detection_rate_attack1: 0.40
      infit_flags_adversarial_items: true
      c_n_inflation_under_attack: 0.3
    result_rationale: >
      G-MFRM 的 person-fit diagnostics（infit/outfit）提供了对 adversarial manipulation
      的自然检测机制。Attack 1（targeted item injection：在特定 item 上注入异常高分）
      被 item-level outfit 检测到（85%），因为注入的分数违反了 Rasch 模型的 sufficiency
      假设。Attack 2（judge collusion：多个 judge 协调给高分）更难检测（70%），因为
      一致的 judge behavior 可以被 d_j 吸收——但 c_n 会出现异常膨胀（+0.3）作为
      间接信号。Attack 3（exposure manipulation：人为修改 e_i 输入）反而最容易防御
      （90%），因为 Stage 2 的 multi-source 融合和 ConStat 外部验证能交叉检验 e_i
      的一致性。Sequential baseline 在 Attack 1 上检测率仅 40%，因为没有 contamination
      模型来标记异常。总体而言 G-MFRM 不是完全 adversarial-proof 的（scope 声明已排除），
      但比 sequential 有更强的内在鲁棒性。
    tables:
      - name: "Table A4: Adversarial Robustness"
        columns: [attack, "θ̂ shift (G-MFRM)", "θ̂ shift (Sequential)", "G-MFRM detection rate"]
        rows:
          - [Targeted item injection, 0.15, 0.38, 0.85]
          - [Judge collusion (2/8), 0.22, 0.31, 0.70]
          - [Exposure manipulation, 0.08, "N/A", 0.90]
    figures_description:
      - "Fig A12: θ̂ perturbation under three attack scenarios — G-MFRM (blue) vs Sequential
        (orange). G-MFRM consistently shows smaller shifts and higher detection rates."
    analysis: >
      P2 优先级实验，为 Discussion/Limitations 提供材料。G-MFRM 不声称 adversarial
      robustness 作为贡献，但展示其 diagnostic 框架提供了 "免费的" 异常检测能力。
      Judge collusion 是最大弱点——如果超过 50% 的 judge 被操纵，d_j 无法区分真实
      severity 和操纵。这是一个 honest limitation。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e8056cee-f485-439e-92e2-a21b8009a41f",
  "isSidechain": false,
  "requestId": "req_011CbGTrDSJWRdDzR5Unqvy2",
  "type": "assistant",
  "uuid": "b1434df4-4ce7-466e-841c-ac83268facea",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_019yHuDPZn8uYCYyyuHVCTr4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 11970,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16960,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 11970,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16960,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 11970,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 11970
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real contamination magnitude matches mvp_002/003 assumptions (strong), G-MFRM converges cleanly on real data, and ranking correction is statistically and p…",
  "leafUuid": "b1434df4-4ce7-466e-841c-ac83268facea",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Staged joint calibration corrects LLM judge bias and benchmark contamination",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real contamination magnitude matches mvp_002/003 assumptions (strong), G-MFRM converges cleanly on real data, and ranking correction is statistically and p…",
  "leafUuid": "b1434df4-4ce7-466e-841c-ac83268facea",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Staged joint calibration corrects LLM judge bias and benchmark contamination",
  "sessionId": "3035166a-19af-4924-a7d4-3c797a8e405f"
}
```

---
