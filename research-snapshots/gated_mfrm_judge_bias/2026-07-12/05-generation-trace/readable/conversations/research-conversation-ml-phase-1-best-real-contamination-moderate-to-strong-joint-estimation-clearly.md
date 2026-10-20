# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Real contamination moderate-to-strong, joint estimation clearly dominates se

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 14
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f77fcd49-85a9-4148-bebd-f522d7131fae.jsonl`
- **Structured JSON:** [`a82678d8457a3a393907.json`](../../sessions/a8/a82678d8457a3a393907.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T04:13:30.412Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T04:13:30.412Z",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Real contamination moderate-to-strong, joint estimation clearly dominates sequential on real data, all three claims hold at full strength — Tier A narrative\n核心假设：['Real c_n distribution has median ≥ 0.8 (closer to mvp_002/003 regime)', 'd_j and c_n·e_i empirically non-orthogonal on real data (confounding scatter r ≥ 0.4)', 'G-MFRM converges cleanly on real data (R̂ ≤ 1.05, ESS ≥ 150)', 'e_i estimation pipeline produces coherent signal (ConStat c_n validation corr ≥ 0.6)', '≥ 6 judges produce sufficient facet variance for identifiability', 'Chatbot Arena Elo is sufficiently stable as ground truth (test-retest τ ≥ 0.90)']\n关键指标范围：{'real_cn_median': [0.8, 1.5], 'kendall_tau_gmfrm': [0.82, 0.92], 'kendall_tau_best_baseline': [0.75, 0.85], 'delta_tau_vs_best_baseline': [0.04, 0.1], 'delta_tau_p_value': [0.001, 0.03], 'theta_rmse_reduction_vs_sequential': [0.2, 0.45], 'confounding_scatter_r': [0.4, 0.7], 'convergence_rhat_max': [1.0, 1.05], 'convergence_ess_min': [150, 500], 'cn_constat_validation_corr': [0.6, 0.9], 'ei_pipeline_internal_consistency': [0.5, 0.8]}\n叙事方向：Original framing holds: joint estimation is methodologically necessary AND empirically superior. Lead with ranking correction magnitude. All 3 claims at full strength. Headline: 'G-MFRM achieves X% higher τ with Arena while providing interpretable contamination diagnostics.' AAAI main conference positioning confident.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gated_mfrm_judge_bias\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — gated_mfrm_judge_bias\n\n## Target Venue\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\n- Timeline: ~68 days from today (2026-05-21)\n\n## Core Insight\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\n\n## Core Claims (3 条，均可证伪)\n\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding. (Note: OVB formalization supports this claim as mechanism explanation — \"identify and quantify confounding in LLM evaluation\" — not as independent theoretical contribution. Cite Angrist & Pischke 2009 as source.)\n\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected \"fair scores.\" (Note: \"staged joint\" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use \"staged joint calibration\" or \"conditional joint estimation,\" never \"fully joint.\")\n\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\n\n## Story Spine\n\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\n\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. In LLM evaluation literature, no existing work jointly models both within a single calibration framework. (Note: educational measurement has MFRM+DIF joint modeling — Eckes 2011, Patz et al. 2002, Fox & Glas 2001, Wind & Peterson 2018 — but these address test fairness, not LLM contamination. G-MFRM is the first to apply continuous-exposure gating within MFRM for LLM evaluation. \"First\" claim must be precisely scoped to LLM evaluation with continuous exposure.)\n\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.\n\n- **Headline result template**: \"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\"\n\n## Narrative Strategy (from distilled writing)\n\n- **Type**: \"突破局限\" (sequential has structural flaw) + \"统一框架\" (G-MFRM unifies both corrections)\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\n- **Section 2**: Toy example / formal **observation** (NOT \"proposition\" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\n\n## Venue Fit Risks\n\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Why not CyclicJudge + discard contaminated items?\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\n\n2. **\"Is confounding large enough in practice?\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\n\n3. **\"Rank-1 assumption (c_n·e_i) too strong\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\n\n4. **\"DG-IRT transfer is trivial\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).\n\n4b. **\"Staged estimation ≠ joint estimation\"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.\n\n5. **\"Contamination signal realistic?\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\n\n6. **\"Chatbot Arena Elo as ground truth — circular reasoning?\"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.\n\n7. **\"c_n ≥ 0 assumption too restrictive?\"** — Half-Cauchy prior enforces non-negativity, appropriate for the \"contamination as unfair advantage\" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.\n\n8. **\"≥4 judges needed — too expensive?\"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.\n\n9. **\"No judge-model interaction term?\"** — G-MFRM has d_j (judge-level) and c_n·e_i (model-item), but no f_{nj} (judge-model interaction). Preference Leakage shows same-model PLS≈23.6%, same-family≈8.9%. When GPT-5.5 judges GPT-5.5, this bias distributes uniformly across items and gets absorbed into θ̂_n. Mitigation: (a) exp-006 leave-one-judge-out residual diagnostic detects if specific judges inflate same-family models; (b) Limitations section acknowledges scope boundary; (c) rank-k extension with judge-model interaction is future work.\n\n## Two-Tier Narrative (contingent on exp-005 contamination magnitude)\n\n**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:\n- Lead with ranking correction as primary contribution\n- Claim 3 at full strength: \"G-MFRM achieves X% higher Kendall-τ\"\n- Headline: joint estimation dramatically outperforms sequential\n\n**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:\n- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)\n- Reframe: \"even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)\"\n- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude\n- Claim 3 softened to \"comparable or better rankings PLUS interpretable diagnostic outputs\"\n\n**Tier B+ — Diagnostics as sole primary (if Claim 1 ρ≈0 AND Claim 3 Δτ non-significant)**:\n- Diagnostics become the **sole** primary contribution (not co-primary)\n- Paper becomes \"tool paper\": G-MFRM as diagnostic framework for LLM evaluation auditing\n- Contribution: per-model c_n (training data audit), per-item e_i (item retirement), per-judge d_j (judge calibration) — unified diagnostic outputs no existing tool provides\n- Risk: \"tool paper\" positioning may be weaker for Main Conference; strong for Findings\n\nexp-005 determines which tier. Decision point: after exp-005 results, before paper writing.\n\n## Novelty Supplementation Strategy\n\nDream R2 exposed a novelty ceiling: \"MFRM + 1 term\" + \"textbook OVB\" = combinatorial novelty. Even with best-case data, Main Conference bar may not be met on novelty alone. Supplement with:\n\n1. **Identifiability analysis** (Method section): Prove necessary and sufficient conditions for (θ, b, d, c) identifiability when e_i is fixed. This is a non-trivial technical contribution beyond \"adding a term.\"\n2. **Formal e_i uncertainty propagation**: Beyond sensitivity analysis (exp-012), provide theoretical treatment of how e_i estimation error propagates to c_n credible intervals. Compare to two-step estimator literature (Heckman 1979, Murphy & Topel 1985).\n3. **Diagnostic framework formalization**: Frame the four-dimensional output (θ, d_j, c_n, e_i) as a principled measurement framework, not just parameter estimates. Connect to DIF (Differential Item Functioning) tradition.\n\n## Bibliography Strategy (Paper Agent input)\n\nRequired references by positioning role:\n- **Foundational IRT**: Rasch 1960, Lord & Novick 1968, Fox 2010 (Bayesian IRT)\n- **MFRM ancestor**: Linacre 1989, Engelhard 2002/2013, Eckes 2011/2015\n- **DG-IRT ancestor**: Shu et al. 2013 (Psychometrika), Robitzsch 2020\n- **MFRM+DIF (educational)**: Wind & Peterson 2018, Patz et al. 2002, Fox & Glas 2001\n- **LLM contamination**: Golchin & Surdeanu 2023, Shi et al. 2023 (Min-K%), ConStat, DCR\n- **LLM judge bias**: Zheng et al. 2023 (MT-Bench), CyclicJudge, UDA, Preference Leakage\n- **Benchmarks**: Arena-Hard original, WildBench original, LiveBench\n- **Econometrics**: Angrist & Pischke 2009 (OVB), Heckman 1979 (two-step)\nTarget: 30-40 references total.\n\n## MVP Evidence Summary\n\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: multi_judge_data_collection\n  claim: 3\n  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using\n    8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,\n    Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position\n    swap for pairwise.'\n  priority: P0\n  gpu_budget_hours: 130\n  deps: []\n  notes: Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900\n    budget). Position swap doubles evaluation count. MUST also collect judge response\n    generations (--generate-judge-responses) for UDA baseline compatibility.\n  status: planned\n- id: exp-002\n  name: item_exposure_estimation\n  claim: 2\n  description: 'Estimate per-item exposure e_i via three-source pipeline: (1) Primary:\n    item-level performance gap between original items and GPT-5.5/Claude-rephrased\n    reference variants, averaged across reference models, with spline difficulty correction\n    (ConStat-inspired). (2) Temporal: performance gap on pre-cutoff vs post-cutoff\n    item variants where available. (3) LogProber: token logprob memorization scores\n    for models with logprob API. Sources combined via weighted composite (weights\n    tuned on validation split). ConStat per-model delta used as external validation\n    of fitted c_n, not as e_i source.'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  notes: 'Main bottleneck: reference benchmark variant construction + quality validation.\n    ConStat per-model delta validates G-MFRM c_n, not used for per-item e_i.'\n  status: planned\n- id: exp-003\n  name: gmfrm_real_data_fit\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage\n    1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare\n    fair scores θ̂ with Chatbot Arena human votes (Kendall-τ).'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  - exp-002\n  notes: 'NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,\n    NCP, target_accept=0.95). Include per-benchmark analysis: if any benchmark has\n    contamination ≈ 0, verify G-MFRM degrades gracefully to MFRM level (real-data\n    graceful degradation check).'\n  status: planned\n- id: exp-004\n  name: baseline_comparison\n  claim: 3\n  description: 'Compare G-MFRM against 8 baselines on same data: (1) raw multi-judge\n    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) CyclicJudge\n    + contaminated item discard, (6) DCR Factor, (7) UDA, (8) Preference Leakage calibration.\n    Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena. MUST include rank change analysis:\n    show which specific models change rank, by how many positions, and top-k stability\n    (k=5,10).'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-003\n  notes: 'Baseline (5) is the strongest trivial alternative — addresses Reviewer Concern\n    #1. CyclicJudge/UDA/DCR/PrefLeakage need public code check. Budget may not include\n    debug time. Rank change analysis addresses Dream R2-W3. MUST include post-hoc\n    power analysis: compute statistical power for Wilcoxon test to detect observed\n    Δτ at α=0.05 with N models. If power < 0.80, discuss implications and consider\n    increasing items/judges.'\n  status: planned\n- id: exp-005\n  name: contamination_magnitude_calibration\n  claim: 1\n  description: 'Estimate real contamination magnitude: compare fitted c_n from exp-003\n    with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001\n    (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength.'\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  notes: 'Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This\n    experiment determines claim calibration.'\n  status: planned\n- id: exp-006\n  name: judge_count_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure\n    G-MFRM performance degradation. At what minimum judge count does G-MFRM still\n    outperform sequential? Include leave-one-judge-out residual diagnostic: check\n    if removing a judge that shares model family with targets systematically changes\n    residuals (preference leakage detection).'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-003\n  status: planned\n- id: exp-007\n  name: exposure_indicator_ablation\n  claim: 2\n  description: 'Ablation: contribution of each exposure indicator (ConStat delta,\n    temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out\n    analysis.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-008\n  name: facet_fit_diagnostics\n  claim: 2\n  description: 'Measurement quality validation: report infit/outfit MNSQ for all facets\n    (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi)\n    vs Stage 3 c_n as construct coherence validation. MUST also report: divergent\n    transition count, posterior predictive check, trace plots for key parameters.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  name: confounding_formal_observation\n  claim: 1\n  description: 'Formal bias analysis: derive first-order bias approximation for sequential\n    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation\n    across realistic parameter ranges. For paper Section 2. Frame as ''Observation''\n    (standard OVB from Angrist & Pischke 2009), not ''Proposition''. MUST include\n    synthetic c_n point-estimate validation: generate data with known ground-truth\n    c_n, fit G-MFRM, report per-model c_n RMSE and 95% credible interval coverage\n    probability.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  notes: Can run in parallel with data collection. Extends MVP synthetic analysis.\n    Downgraded from 'Proposition' to 'Observation' per Dream review. Synthetic c_n\n    validation addresses Dream R1-N3.\n  status: planned\n- id: exp-012\n  name: error_propagation_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis for staged estimation: inject Gaussian noise\n    into e_i estimates at σ=0.1,0.2,0.5 before Stage 3 fitting. Measure θ̂ RMSE degradation\n    and c_n recovery accuracy. Shows three-stage pipeline is robust to e_i estimation\n    error. Use synthetic data with known ground truth.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  notes: Addresses Dream R2-W5 and R1-N1. Can run on MVP codebase with modifications.\n    Critical for defending staged estimation design choice.\n  status: planned\n- id: exp-010\n  name: wildbench_replication\n  claim: 3\n  description: Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark\n    generalization.\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-003\n  status: planned\n- id: exp-011\n  name: adversarial_robustness\n  claim: 2\n  description: Test G-MFRM robustness against adversarial contamination following\n    Wang et al. (ICLR 2026) fragility findings.\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    convergence: PASS\n    rho_0.0:\n      joint_gmfrm:\n        RMSE: 0.1540±0.0269\n        tau: 0.9042±0.0445\n      sequential:\n        RMSE: 0.1540±0.0242\n        tau: 0.9016±0.0467\n      p_value: 0.4782\n    rho_0.3:\n      joint_gmfrm:\n        RMSE: 0.1521±0.0283\n        tau: 0.9068±0.0419\n      sequential:\n        RMSE: 0.1527±0.0236\n        tau: 0.9011±0.0452\n      p_value: 0.3506\n    rho_0.6:\n      joint_gmfrm:\n        RMSE: 0.1529±0.0285\n        tau: 0.9047±0.0418\n      sequential:\n        RMSE: 0.1537±0.0237\n        tau: 0.9037±0.0419\n      p_value: 0.3921\n    rho_0.0_no_degradation_p: 0.9563\n    runtime_seconds: 1675.6\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL (convergence)\n    convergence:\n      max_rhat: 1.05\n      min_ess: 47\n      pass: false\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 32.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0449\n      tau: 0.8390±0.0351\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8596±0.0291\n    joint_gmfrm:\n      RMSE: 0.1486±0.0199\n      tau: 0.9028±0.0181\n    runtime_seconds: 1935.4\n    scatter_pearson_r: 0.6534\n    scatter_p: 0\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    convergence:\n      max_rhat: 1.03\n      min_ess: 224\n      pass: true\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 43.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0448\n      tau: 0.8388±0.0345\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8593±0.0293\n    joint_gmfrm:\n      RMSE: 0.1243±0.0164\n      tau: 0.9223±0.0098\n    runtime_seconds: 4385.5\n    kendall_tau_joint: 0.9223\n    kendall_tau_seq: 0.8593\n- exp_id: exp-009\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PARTIAL (σ≤0.2 robust, σ=0.5 exceeds threshold)\n    false_failure: true\n    false_failure_reason: EXIT_CODE=129 (SIGHUP) after all 80/80 fits completed and\n      results saved\n    sigma_0.0:\n      theta_rmse: 0.1277\n      theta_rmse_std: 0.0178\n      theta_tau: 0.9159\n      cn_rmse: 0.533\n      cn_corr: 0.8599\n      rhat_max: 1.02\n      ess_min: 276\n      n: 20\n    sigma_0.1:\n      theta_rmse: 0.1295\n      theta_rmse_std: 0.0178\n      theta_tau: 0.9153\n      cn_rmse: 0.5452\n      cn_corr: 0.8542\n      delta_theta_pct: 1.4\n      delta_cn_pct: 2.3\n    sigma_0.2:\n      theta_rmse: 0.1352\n      theta_rmse_std: 0.0175\n      theta_tau: 0.914\n      cn_rmse: 0.5751\n      cn_corr: 0.8385\n      delta_theta_pct: 5.9\n      delta_cn_pct: 7.9\n    sigma_0.5:\n      theta_rmse: 0.1748\n      theta_rmse_std: 0.0266\n      theta_tau: 0.885\n      cn_rmse: 0.8415\n      cn_corr: 0.745\n      delta_theta_pct: 36.9\n      delta_cn_pct: 57.9\n    convergence:\n      all_rhat_max: 1.02\n      pass: true\n    total_runtime_seconds: 14585\n    artifacts:\n    - error_propagation.png\n    - cn_degradation.png\n    - summary.csv\n- exp_id: exp-001\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T04:13:30.416Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T04:13:30.416Z",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae"
}
```

---

## Round 1

12 recorded events

### User

_source line 3 · 2026-05-22T04:13:30.440Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Real contamination moderate-to-strong, joint estimation clearly dominates sequential on real data, all three claims hold at full strength — Tier A narrative
核心假设：['Real c_n distribution has median ≥ 0.8 (closer to mvp_002/003 regime)', 'd_j and c_n·e_i empirically non-orthogonal on real data (confounding scatter r ≥ 0.4)', 'G-MFRM converges cleanly on real data (R̂ ≤ 1.05, ESS ≥ 150)', 'e_i estimation pipeline produces coherent signal (ConStat c_n validation corr ≥ 0.6)', '≥ 6 judges produce sufficient facet variance for identifiability', 'Chatbot Arena Elo is sufficiently stable as ground truth (test-retest τ ≥ 0.90)']
关键指标范围：{'real_cn_median': [0.8, 1.5], 'kendall_tau_gmfrm': [0.82, 0.92], 'kendall_tau_best_baseline': [0.75, 0.85], 'delta_tau_vs_best_baseline': [0.04, 0.1], 'delta_tau_p_value': [0.001, 0.03], 'theta_rmse_reduction_vs_sequential': [0.2, 0.45], 'confounding_scatter_r': [0.4, 0.7], 'convergence_rhat_max': [1.0, 1.05], 'convergence_ess_min': [150, 500], 'cn_constat_validation_corr': [0.6, 0.9], 'ei_pipeline_internal_consistency': [0.5, 0.8]}
叙事方向：Original framing holds: joint estimation is methodologically necessary AND empirically superior. Lead with ranking correction magnitude. All 3 claims at full strength. Headline: 'G-MFRM achieves X% higher τ with Arena while providing interpretable contamination diagnostics.' AAAI main conference positioning confident.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: gated_mfrm_judge_bias
venue: emnlp-2026

## paper_framing.md

# Paper Framing — gated_mfrm_judge_bias

## Target Venue
- Primary: AAAI 2027 (full paper, deadline July 28, 2026)
- Backup: ACL 2027 via ARR (submission August 3, 2026)
- Timeline: ~68 days from today (2026-05-21)

## Core Insight
Sequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.

## Core Claims (3 条，均可证伪)

1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding. (Note: OVB formalization supports this claim as mechanism explanation — "identify and quantify confounding in LLM evaluation" — not as independent theoretical contribution. Cite Angrist & Pischke 2009 as source.)

2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected "fair scores." (Note: "staged joint" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use "staged joint calibration" or "conditional joint estimation," never "fully joint.")

3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.

## Story Spine

- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.

- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. In LLM evaluation literature, no existing work jointly models both within a single calibration framework. (Note: educational measurement has MFRM+DIF joint modeling — Eckes 2011, Patz et al. 2002, Fox & Glas 2001, Wind & Peterson 2018 — but these address test fairness, not LLM contamination. G-MFRM is the first to apply continuous-exposure gating within MFRM for LLM evaluation. "First" claim must be precisely scoped to LLM evaluation with continuous exposure.)

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

9. **"No judge-model interaction term?"** — G-MFRM has d_j (judge-level) and c_n·e_i (model-item), but no f_{nj} (judge-model interaction). Preference Leakage shows same-model PLS≈23.6%, same-family≈8.9%. When GPT-5.5 judges GPT-5.5, this bias distributes uniformly across items and gets absorbed into θ̂_n. Mitigation: (a) exp-006 leave-one-judge-out residual diagnostic detects if specific judges inflate same-family models; (b) Limitations section acknowledges scope boundary; (c) rank-k extension with judge-model interaction is future work.

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

**Tier B+ — Diagnostics as sole primary (if Claim 1 ρ≈0 AND Claim 3 Δτ non-significant)**:
- Diagnostics become the **sole** primary contribution (not co-primary)
- Paper becomes "tool paper": G-MFRM as diagnostic framework for LLM evaluation auditing
- Contribution: per-model c_n (training data audit), per-item e_i (item retirement), per-judge d_j (judge calibration) — unified diagnostic outputs no existing tool provides
- Risk: "tool paper" positioning may be weaker for Main Conference; strong for Findings

exp-005 determines which tier. Decision point: after exp-005 results, before paper writing.

## Novelty Supplementation Strategy

Dream R2 exposed a novelty ceiling: "MFRM + 1 term" + "textbook OVB" = combinatorial novelty. Even with best-case data, Main Conference bar may not be met on novelty alone. Supplement with:

1. **Identifiability analysis** (Method section): Prove necessary and sufficient conditions for (θ, b, d, c) identifiability when e_i is fixed. This is a non-trivial technical contribution beyond "adding a term."
2. **Formal e_i uncertainty propagation**: Beyond sensitivity analysis (exp-012), provide theoretical treatment of how e_i estimation error propagates to c_n credible intervals. Compare to two-step estimator literature (Heckman 1979, Murphy & Topel 1985).
3. **Diagnostic framework formalization**: Frame the four-dimensional output (θ, d_j, c_n, e_i) as a principled measurement framework, not just parameter estimates. Connect to DIF (Differential Item Functioning) tradition.

## Bibliography Strategy (Paper Agent input)

Required references by positioning role:
- **Foundational IRT**: Rasch 1960, Lord & Novick 1968, Fox 2010 (Bayesian IRT)
- **MFRM ancestor**: Linacre 1989, Engelhard 2002/2013, Eckes 2011/2015
- **DG-IRT ancestor**: Shu et al. 2013 (Psychometrika), Robitzsch 2020
- **MFRM+DIF (educational)**: Wind & Peterson 2018, Patz et al. 2002, Fox & Glas 2001
- **LLM contamination**: Golchin & Surdeanu 2023, Shi et al. 2023 (Min-K%), ConStat, DCR
- **LLM judge bias**: Zheng et al. 2023 (MT-Bench), CyclicJudge, UDA, Preference Leakage
- **Benchmarks**: Arena-Hard original, WildBench original, LiveBench
- **Econometrics**: Angrist & Pischke 2009 (OVB), Heckman 1979 (two-step)
Target: 30-40 references total.

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
    budget). Position swap doubles evaluation count. MUST also collect judge response
    generations (--generate-judge-responses) for UDA baseline compatibility.
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
    debug time. Rank change analysis addresses Dream R2-W3. MUST include post-hoc
    power analysis: compute statistical power for Wilcoxon test to detect observed
    Δτ at α=0.05 with N models. If power < 0.80, discuss implications and consider
    increasing items/judges.'
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
    outperform sequential? Include leave-one-judge-out residual diagnostic: check
    if removing a judge that shares model family with targets systematically changes
    residuals (preference leakage detection).'
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
- exp_id: exp-009
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}
- exp_id: exp-012
  name: ''
  status: DONE
  conclusion: success
  metrics:
    verdict: PARTIAL (σ≤0.2 robust, σ=0.5 exceeds threshold)
    false_failure: true
    false_failure_reason: EXIT_CODE=129 (SIGHUP) after all 80/80 fits completed and
      results saved
    sigma_0.0:
      theta_rmse: 0.1277
      theta_rmse_std: 0.0178
      theta_tau: 0.9159
      cn_rmse: 0.533
      cn_corr: 0.8599
      rhat_max: 1.02
      ess_min: 276
      n: 20
    sigma_0.1:
      theta_rmse: 0.1295
      theta_rmse_std: 0.0178
      theta_tau: 0.9153
      cn_rmse: 0.5452
      cn_corr: 0.8542
      delta_theta_pct: 1.4
      delta_cn_pct: 2.3
    sigma_0.2:
      theta_rmse: 0.1352
      theta_rmse_std: 0.0175
      theta_tau: 0.914
      cn_rmse: 0.5751
      cn_corr: 0.8385
      delta_theta_pct: 5.9
      delta_cn_pct: 7.9
    sigma_0.5:
      theta_rmse: 0.1748
      theta_rmse_std: 0.0266
      theta_tau: 0.885
      cn_rmse: 0.8415
      cn_corr: 0.745
      delta_theta_pct: 36.9
      delta_cn_pct: 57.9
    convergence:
      all_rhat_max: 1.02
      pass: true
    total_runtime_seconds: 14585
    artifacts:
    - error_propagation.png
    - cn_degradation.png
    - summary.csv
- exp_id: exp-001
  name: ''
  status: RUNNING
  conclusion: ''
  metrics: {}

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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "04c946e6-72b5-43e8-9f3a-c1a344ebdd9e",
  "type": "user",
  "uuid": "003ee5bb-425a-4391-b378-24309514ca03",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T04:13:30.439Z_

```json
{
  "parentUuid": "003ee5bb-425a-4391-b378-24309514ca03",
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
  "uuid": "aa166580-9cd2-41b3-a5aa-f0daf8ccf459",
  "timestamp": "2026-05-22T04:13:30.439Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T04:13:30.439Z_

```json
{
  "parentUuid": "aa166580-9cd2-41b3-a5aa-f0daf8ccf459",
  "isSidechain": false,
  "attachment": {
    "type": "agent_listing_delta",
    "addedTypes": [
      "claude",
      "Explore",
      "general-purpose",
      "Plan",
      "statusline-setup"
    ],
    "addedLines": [
      "- claude: Catch-all for any task that doesn't fit a more specific agent. FleetView's default when no agent name is typed. (Tools: *)",
      "- Explore: Fast read-only search agent for locating code. Use it to find files by pattern (eg. \"src/components/**/*.tsx\"), grep for symbols or keywords (eg. \"API endpoints\"), or answer \"where is X defined / which files reference Y.\" Do NOT use it for code review, design-doc auditing, cross-file consistency checks, or open-ended analysis — it reads excerpts rather than whole files and will miss content past its read window. When calling, specify search breadth: \"quick\" for a single targeted lookup, \"medium\" for moderate exploration, or \"very thorough\" to search across multiple locations and naming conventions. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- general-purpose: General-purpose agent for researching complex questions, searching for code, and executing multi-step tasks. When you are searching for a keyword or file and are not confident that you will find the right match in the first few tries use this agent to perform the search for you. (Tools: *)",
      "- Plan: Software architect agent for designing implementation plans. Use this when you need to plan the implementation strategy for a task. Returns step-by-step plans, identifies critical files, and considers architectural trade-offs. (Tools: All tools except Agent, ExitPlanMode, Edit, Write, NotebookEdit)",
      "- statusline-setup: Use this agent to configure the user's Claude Code status line setting. (Tools: Read, Edit)"
    ],
    "removedTypes": [],
    "isInitial": true,
    "showConcurrencyNote": true
  },
  "type": "attachment",
  "uuid": "75fdcb24-30be-4335-9dda-19dfb7b1ef33",
  "timestamp": "2026-05-22T04:13:30.439Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 6 · 2026-05-22T04:13:30.439Z_

```json
{
  "parentUuid": "75fdcb24-30be-4335-9dda-19dfb7b1ef33",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "0386625d-bb6f-4ed1-b3bc-c09fc2ef695d",
  "timestamp": "2026-05-22T04:13:30.439Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real contamination moderate-to-strong, joint estimation clearly dominates sequential on real data, all three claims hold at full strength — Tier A narrativ…",
  "leafUuid": "0386625d-bb6f-4ed1-b3bc-c09fc2ef695d",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae"
}
```

---

### Runtime record

_source line 8_

```json
{
  "type": "ai-title",
  "aiTitle": "Real-data validation of G-MFRM joint contamination and bias correction",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae"
}
```

---

### Assistant

_source line 9 · 2026-05-22T04:13:57.416Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment plan, under the "best" tier assumptions. Let me review:

- best tier = Tier A narrative: real contamination moderate-to-strong, joint estimation clearly dominates, all three claims hold at full strength
- Key metric ranges are provided
- I need to provide result_rationale for each prediction

Let me go through each planned experiment:

1. exp-001: multi_judge_data_collection (planned)
2. exp-002: item_exposure_estimation (planned)
3. exp-003: gmfrm_real_data_fit (planned)


4. exp-004: baseline_comparison (planned)
5. exp-005: contamination_magnitude_calibration (planned)
6. exp-006: judge_count_sensitivity (planned)
7. exp-007: exposure_indicator_ablation (planned)
8. exp-008: facet_fit_diagnostics (planned)
9. exp-010: wildbench_replication (planned)
10. exp-011: adversarial_robustness (planned)

I'll skip exp-009 since it's currently running and exp-012 since it's already done.

Now I'm setting up detailed predictions for each of these planned experiments using the best tier assumptions. For the best tier, I'm estimating real_cn_median around 1.05, kendall_tau_gmfrm around 0.87, kendall_tau_best_baseline around 0.80, and delta_tau_vs_best_baseline starting around 0.07. Now I'm working through the detailed predictions for each experiment, thinking about what success looks like under best-tier conditions for the data collection phase, the item exposure pipeline, the core G-MFRM fitting, how it compares to baselines, and the contamination calibration work.

I'm also considering the sensitivity analyses—how the model holds up with fewer judges, whether all three exposure indicators pull their weight, if the facet diagnostics check out, and whether the results generalize to WildBench and withstand adversarial attacks.

Writing out the comprehensive predictions as YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "0386625d-bb6f-4ed1-b3bc-c09fc2ef695d",
  "isSidechain": false,
  "requestId": "req_011CbGxSVnWnEbtaHYmJ8Koe",
  "type": "assistant",
  "uuid": "c57e575f-689a-4d40-b624-440c985d2563",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172DQeSEDxbY6G88bHiMcAP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13959,
      "cache_read_input_tokens": 11447,
      "output_tokens": 21073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21073,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13959
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

_source line 10 · 2026-05-22T04:20:01.304Z_

```yaml
tier: best
narrative_guidance: >
  Original framing holds at full strength. Joint estimation is methodologically necessary AND empirically superior.
  Lead with ranking correction magnitude: "G-MFRM achieves 7pp higher Kendall-τ with Chatbot Arena while providing
  interpretable contamination diagnostics." Real contamination is moderate-to-strong (median c_n ≈ 1.05), validating
  the mvp_002/003 regime assumptions. Confounding scatter r ≥ 0.4 confirms the OVB mechanism operates on real data.
  All 3 claims hold at full strength — AAAI main conference positioning confident. No narrative pivot needed.
  Paper structure follows Tier A: Section 2 opens with OVB observation + toy example showing 33% θ-RMSE degradation,
  Section 4 presents G-MFRM dominance across both benchmarks, Section 5 ablation shows each component contributes.
  Headline: "On MT-Bench and Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve 8.7% higher Kendall-τ
  with Chatbot Arena human votes than the best sequential baseline."

imagined_experiments:
  - name: "multi_judge_data_collection"
    plan_id: "exp-001"
    description: >
      Collect multi-judge evaluation data on MT-Bench (80 items × 10 categories) and Arena-Hard (500 items)
      using 8 judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,
      Qwen3.6-27B, Llama 4 Maverick, Gemini 2.5 Pro. Evaluate 22 target models with position swap.
      Collect full judge response generations for UDA baseline compatibility.
    expected_results:
      num_judges: 8
      num_target_models: 22
      mt_bench_items: 80
      arena_hard_items: 500
      total_judgments_mt_bench: 28160  # 80 items × 22 models × 8 judges × 2 positions
      total_judgments_arena_hard: 176000  # 500 × 22 × 8 × 2
      api_cost_usd: 820
      vllm_gpu_hours: 95
      judge_agreement_fleiss_kappa: 0.42
      position_bias_rate_mean: 0.14
      position_bias_rate_std: 0.06
      missing_data_rate: 0.02
      judge_response_generation_success_rate: 0.97
    result_rationale: >
      Best 档假设 ≥ 6 judges produce sufficient facet variance for identifiability。8 judges 涵盖 4 家厂商
      (OpenAI, Anthropic, DeepSeek, Meta/Qwen) 确保 d_j 分布有足够异质性。22 target models 包括已知
      高污染 (GPT-4o, Claude 3.5 Sonnet 等训练数据覆盖广的模型) 和低污染 (新发布的 open-weight 模型)，
      保证 c_n 分布的方差。Fleiss κ ≈ 0.42 (moderate agreement) 是 LLM judge 的典型水平 (Zheng et al. 2023
      报告 MT-Bench 上 GPT-4 与人类 agreement ~0.65，但多 judge 间 agreement 会更低)。Position bias 14% ±6%
      基于已有文献 (MT-Bench position bias ~10-20%)。缺失率 2% 来自 API timeout 和 vLLM OOM，best 档下
      基础设施运行稳定。总评测数量 ~204K judgments 提供充足的统计功效。
    tables:
      - name: "Table: Judge Pool Summary"
        columns: ["Judge", "Provider", "Type", "Params", "Position Bias %", "Mean Score", "Score SD"]
        rows:
          - ["GPT-5.5", "OpenAI", "API", "~2T (est.)", "11.2", "7.83", "1.42"]
          - ["Claude Opus 4.7", "Anthropic", "API", "~1.5T (est.)", "8.7", "7.61", "1.58"]
          - ["Claude Sonnet 4.6", "Anthropic", "API", "~500B (est.)", "13.5", "7.45", "1.51"]
          - ["DeepSeek-V4-Pro", "DeepSeek", "API", "671B MoE", "16.1", "7.29", "1.63"]
          - ["Qwen3-235B-A22B", "Alibaba", "vLLM", "235B MoE", "18.3", "7.12", "1.71"]
          - ["Qwen3.6-27B", "Alibaba", "vLLM", "27B", "19.7", "6.88", "1.82"]
          - ["Llama 4 Maverick", "Meta", "vLLM", "400B MoE", "14.6", "7.35", "1.55"]
          - ["Gemini 2.5 Pro", "Google", "API", "~1T (est.)", "10.9", "7.72", "1.47"]
      - name: "Table: Target Model Coverage"
        columns: ["Model", "Family", "Release Date", "Expected Contamination Level", "Arena Elo (ref)"]
        rows:
          - ["GPT-5.5", "OpenAI", "2026-03", "High", "1382"]
          - ["GPT-4o", "OpenAI", "2024-05", "Very High", "1261"]
          - ["Claude Opus 4.7", "Anthropic", "2026-04", "High", "1375"]
          - ["Claude Sonnet 4.6", "Anthropic", "2026-02", "Moderate-High", "1338"]
          - ["Claude 3.5 Sonnet", "Anthropic", "2024-06", "Very High", "1268"]
          - ["Gemini 2.5 Pro", "Google", "2026-01", "High", "1355"]
          - ["DeepSeek-V4-Pro", "DeepSeek", "2026-02", "Moderate", "1342"]
          - ["DeepSeek-V3", "DeepSeek", "2024-12", "High", "1280"]
          - ["Qwen3-235B-A22B", "Alibaba", "2025-10", "Moderate", "1295"]
          - ["Qwen3.6-27B", "Alibaba", "2026-03", "Low-Moderate", "1245"]
          - ["Llama 4 Maverick", "Meta", "2025-11", "Moderate", "1302"]
          - ["Llama 4 Scout", "Meta", "2025-11", "Moderate", "1275"]
          - ["Mistral Large 3", "Mistral", "2025-09", "Moderate", "1265"]
          - ["Mixtral 8x22B v2", "Mistral", "2025-07", "Moderate-High", "1250"]
          - ["Phi-5", "Microsoft", "2026-01", "Low", "1230"]
          - ["Command R+ v2", "Cohere", "2025-12", "Low", "1225"]
          - ["Jamba 2", "AI21", "2025-10", "Low", "1210"]
          - ["Yi-2 Large", "01.AI", "2025-08", "Moderate", "1240"]
          - ["GPT-4-turbo", "OpenAI", "2024-04", "Very High", "1248"]
          - ["Gemini 1.5 Pro", "Google", "2024-05", "Very High", "1252"]
          - ["Llama 3.1 405B", "Meta", "2024-07", "High", "1243"]
          - ["Claude 3 Opus", "Anthropic", "2024-03", "Very High", "1232"]
    figures_description:
      - "Figure: Judge severity distribution (violin plot of raw scores by judge), showing d_j heterogeneity across 8 judges. Expected pattern: proprietary large models (GPT-5.5, Claude Opus) cluster as lenient scorers (high mean), smaller open-weight models (Qwen3.6-27B) as harsher scorers."
      - "Figure: Inter-judge agreement heatmap (pairwise Cohen's κ), showing moderate block structure by model family."
    analysis: >
      Data collection under best 档预期完整且高质量。8 judges 跨 5 家厂商确保 d_j facet 有足够异质性
      (judge severity SD ≈ 0.4-0.6 in Rasch logits)。22 target models 覆盖从 Very High 到 Low
      contamination 的完整光谱，为 c_n 估计提供必要的方差。Position swap 产生 ~204K 总判断，
      远超 MFRM identifiability 所需最小观测数 (8 judges × 22 models × 80 items = 14,080 cells，
      远大于参数数 22+80+8+22 = 132)。关键检查点：judge response generations 的 97% 成功率
      确保 UDA baseline 有足够训练数据。

  - name: "item_exposure_estimation"
    plan_id: "exp-002"
    description: >
      Estimate per-item exposure e_i via three-source weighted composite pipeline on MT-Bench and Arena-Hard items.
      Primary source: item-level performance gap (original vs GPT-5.5/Claude-rephrased reference variants).
      Secondary: temporal signal, LogProber memorization scores. ConStat per-model delta as c_n validation.
    expected_results:
      ei_pipeline_internal_consistency: 0.68
      source_weight_performance_gap: 0.55
      source_weight_temporal: 0.25
      source_weight_logprober: 0.20
      mt_bench_ei_mean: 0.62
      mt_bench_ei_std: 0.28
      arena_hard_ei_mean: 0.45
      arena_hard_ei_std: 0.31
      mt_bench_high_exposure_items_pct: 0.38
      arena_hard_high_exposure_items_pct: 0.22
      reference_variant_quality_validation_score: 0.91
      cn_constat_validation_corr: 0.72
      logprober_coverage_pct: 0.45
      temporal_signal_coverage_pct: 0.60
      spline_difficulty_correction_r2: 0.78
    result_rationale: >
      Best 档核心假设之一是 e_i estimation pipeline produces coherent signal (internal consistency ≥ 0.5)。
      MT-Bench 的 e_i 均值高于 Arena-Hard (0.62 vs 0.45)，因为 MT-Bench 发布更早 (2023-06)，
      已被大量训练数据覆盖，而 Arena-Hard (2024-04) 相对较新且项目更多样。38% 的 MT-Bench 项目
      属于 high-exposure (e_i > 0.8)，这些主要集中在 coding 和 math 类别 (训练数据中这些领域的
      benchmark overlap 最大)。三个信号源的权重反映其信息量：performance gap 最直接 (权重 0.55)，
      temporal signal 覆盖面广但噪声较大 (0.25)，LogProber 精确但覆盖有限 (0.20，仅 45% 模型有
      logprob API)。ConStat validation corr = 0.72 确认 fitted c_n 与外部 contamination 指标一致，
      处于 best 档要求的 [0.6, 0.9] 范围中部。Spline difficulty correction R² = 0.78 表明难度校正
      有效移除了 performance gap 中的 difficulty confound——否则难题上所有模型表现都差，会被错误
      标记为低暴露。
    tables:
      - name: "Table: Exposure Estimation by MT-Bench Category"
        columns: ["Category", "N Items", "Mean e_i", "SD e_i", "High Exposure %", "Primary Source Avail", "LogProber Avail"]
        rows:
          - ["Writing", "10", "0.71", "0.22", "50%", "100%", "45%"]
          - ["Roleplay", "10", "0.48", "0.30", "20%", "100%", "45%"]
          - ["Reasoning", "10", "0.55", "0.27", "30%", "100%", "45%"]
          - ["Math", "10", "0.82", "0.18", "60%", "100%", "45%"]
          - ["Coding", "10", "0.85", "0.15", "70%", "100%", "45%"]
          - ["Extraction", "10", "0.58", "0.25", "30%", "100%", "45%"]
          - ["STEM", "10", "0.63", "0.26", "30%", "100%", "45%"]
          - ["Humanities", "10", "0.35", "0.28", "10%", "100%", "45%"]
      - name: "Table: Three-Source Ablation (Validation Split)"
        columns: ["Source Combination", "Internal Consistency (α)", "ConStat c_n Corr", "Notes"]
        rows:
          - ["All three", "0.68", "0.72", "Full pipeline"]
          - ["Performance gap only", "0.58", "0.64", "Baseline"]
          - ["Perf gap + temporal", "0.63", "0.68", "+4pp consistency"]
          - ["Perf gap + LogProber", "0.65", "0.70", "+6pp consistency"]
          - ["Temporal only", "0.41", "0.48", "Insufficient alone"]
          - ["LogProber only", "0.52", "0.57", "Good but sparse"]
    figures_description:
      - "Figure: e_i distribution histograms for MT-Bench vs Arena-Hard, showing MT-Bench shifted right (higher exposure). Bimodal structure visible in MT-Bench: coding/math cluster at high e_i, humanities/roleplay cluster at low e_i."
      - "Figure: Scatter plot of e_i (performance gap method) vs LogProber Safe Score for the 45% of models with logprob access. Expected Pearson r ≈ 0.63, confirming convergent validity."
      - "Figure: Spline difficulty correction visualization — raw performance gap vs difficulty-corrected e_i, showing the correction flattens the difficulty confound."
    analysis: >
      e_i 估计在 best 档下表现良好。MT-Bench 的类别间 e_i 异质性 (coding/math 高, humanities/roleplay 低)
      与直觉一致，且与 ConStat 外部验证 corr=0.72 互相印证。关键发现是 MT-Bench 项目平均暴露度
      显著高于 Arena-Hard，这为后续 exp-003 中跨 benchmark 的 contamination magnitude 差异提供解释。
      三个信号源的互补性在 ablation 中清晰可见：LogProber 虽覆盖有限但对有覆盖的模型提供最精确信号，
      temporal signal 提供广覆盖但较粗的估计。Difficulty correction 的 R²=0.78 确认了未经校正的
      performance gap 会产生 ~22% 的系统性偏差（难题被低估暴露度）。

  - name: "gmfrm_real_data_fit"
    plan_id: "exp-003"
    description: >
      Fit G-MFRM three-stage pipeline on real data. Stage 1: MFRM (θ,b,d). Stage 2: e_i from exp-002.
      Stage 3: Joint gated model with e_i fixed, c_n as latent. Compare fair scores θ̂ with Chatbot Arena Elo.
    expected_results:
      kendall_tau_gmfrm_mt_bench: 0.87
      kendall_tau_gmfrm_arena_hard: 0.86
      kendall_tau_gmfrm_combined: 0.87
      kendall_tau_mfrm_only: 0.80
      kendall_tau_raw_average: 0.76
      spearman_rho_gmfrm: 0.93
      theta_rmse_vs_arena_elo_normalized: 0.089
      convergence_rhat_max: 1.03
      convergence_ess_min: 285
      convergence_divergent_transitions: 0
      cn_median: 1.05
      cn_iqr: [0.52, 1.61]
      cn_range: [0.08, 2.34]
      num_models_cn_gt_1: 12
      num_models_cn_lt_0_3: 4
      dj_range_logits: [-0.82, 0.95]
      dj_sd: 0.48
      stage1_runtime_seconds: 1200
      stage3_runtime_seconds: 3800
      total_runtime_seconds: 5200
      graceful_degradation_check: "Arena-Hard subset (low contamination): G-MFRM τ ≈ MFRM τ within 0.01"
    result_rationale: >
      Best 档假设 real c_n distribution has median ≥ 0.8。预测 median = 1.05，位于 [0.8, 1.5] 范围中部偏下，
      反映现实中的 contamination 是 moderate-to-strong 但非极端。这个水平接近 mvp_003 的 DGP 设定，
      因此合成数据中观察到的 joint vs sequential 优势 (τ +6.3pp, RMSE −43.8%) 可以部分迁移到真实数据。
      但真实数据的效应量会衰减约 30-40%，因为：(1) 真实 c_n 分布更离散、非均匀；(2) e_i 有估计误差
      (exp-012 显示 σ=0.2 时 θ-RMSE 仅增加 5.9%)；(3) 真实 d_j 和 c_n·e_i 的非正交性可能低于合成
      设定。Kendall-τ = 0.87 高于 MFRM-only 的 0.80 (+7pp)，对应真实数据上 contamination correction
      的实质性改善。R̂ max = 1.03、ESS min = 285 与 mvp_003 收敛质量相当 (mvp_003: R̂=1.03, ESS=224)，
      因为真实数据量 (~204K judgments) 远大于 MVP 合成数据，MCMC 有更多信息可利用。12/22 模型的
      c_n > 1 表明过半模型存在实质性 contamination，支撑 Tier A 叙事。Arena-Hard 子集的 graceful
      degradation (Δτ < 0.01) 确认当 contamination ≈ 0 时 G-MFRM 不损害估计质量。
    tables:
      - name: "Table: G-MFRM Stage 3 Convergence Diagnostics"
        columns: ["Parameter Group", "N Params", "R-hat Max", "R-hat Mean", "ESS Min", "ESS Median"]
        rows:
          - ["θ (model ability)", "22", "1.02", "1.005", "420", "680"]
          - ["b (item difficulty)", "580", "1.03", "1.008", "310", "550"]
          - ["d (judge severity)", "8", "1.01", "1.003", "850", "1120"]
          - ["c (contamination)", "22", "1.03", "1.012", "285", "480"]
          - ["σ_θ (ability SD)", "1", "1.01", "1.01", "780", "780"]
          - ["σ_c (contamination SD)", "1", "1.02", "1.02", "520", "520"]
      - name: "Table: Fitted c_n by Model (Top 10 Most Contaminated)"
        columns: ["Model", "c_n Posterior Mean", "95% CI", "Arena Elo", "θ_raw - θ_fair", "Rank Change"]
        rows:
          - ["GPT-4o", "2.34", "[1.82, 2.91]", "1261", "+0.41", "-3"]
          - ["Claude 3 Opus", "2.12", "[1.61, 2.68]", "1232", "+0.38", "-4"]
          - ["Gemini 1.5 Pro", "1.98", "[1.48, 2.53]", "1252", "+0.35", "-3"]
          - ["GPT-4-turbo", "1.85", "[1.37, 2.39]", "1248", "+0.33", "-2"]
          - ["Claude 3.5 Sonnet", "1.72", "[1.25, 2.24]", "1268", "+0.31", "-2"]
          - ["Llama 3.1 405B", "1.61", "[1.14, 2.13]", "1243", "+0.28", "-2"]
          - ["DeepSeek-V3", "1.45", "[1.01, 1.95]", "1280", "+0.24", "-1"]
          - ["Mixtral 8x22B v2", "1.32", "[0.88, 1.82]", "1250", "+0.22", "-1"]
          - ["GPT-5.5", "1.18", "[0.78, 1.64]", "1382", "+0.18", "0"]
          - ["Yi-2 Large", "1.08", "[0.67, 1.55]", "1240", "+0.17", "-1"]
      - name: "Table: Fitted d_j (Judge Severity)"
        columns: ["Judge", "d_j (logits)", "95% CI", "Interpretation"]
        rows:
          - ["Qwen3.6-27B", "0.95", "[0.78, 1.13]", "Most severe"]
          - ["Qwen3-235B-A22B", "0.62", "[0.47, 0.78]", "Severe"]
          - ["DeepSeek-V4-Pro", "0.31", "[0.18, 0.45]", "Moderate"]
          - ["Llama 4 Maverick", "0.15", "[0.02, 0.28]", "Slightly severe"]
          - ["Claude Sonnet 4.6", "-0.08", "[-0.21, 0.06]", "Near average"]
          - ["Gemini 2.5 Pro", "-0.25", "[-0.39, -0.11]", "Lenient"]
          - ["Claude Opus 4.7", "-0.48", "[-0.63, -0.34]", "Lenient"]
          - ["GPT-5.5", "-0.82", "[-0.98, -0.67]", "Most lenient"]
    figures_description:
      - "Figure: θ_raw vs θ_fair scatter (22 models), with arrows showing rank displacement. High-c_n models (GPT-4o, Claude 3 Opus) shift down; low-c_n models (Phi-5, Command R+) shift up. Arrow length proportional to c_n. Color by contamination tier."
      - "Figure: Posterior c_n violin plots for all 22 models, ordered by posterior mean. Clear separation between high/low contamination groups. Dashed line at c_n = 0.3 (negligible contamination threshold)."
      - "Figure: Trace plots for 4 representative parameters (θ_GPT-5.5, c_n_GPT-4o, d_GPT-5.5, b_item42). All show good mixing with no trends."
      - "Figure: Per-benchmark G-MFRM τ comparison bar chart — MT-Bench vs Arena-Hard. MT-Bench shows larger G-MFRM advantage (higher contamination), Arena-Hard shows modest advantage."
    analysis: >
      G-MFRM 在真实数据上的表现完全支撑 Tier A 叙事。核心发现：(1) c_n median = 1.05 确认现实
      contamination 处于 moderate-to-strong 范围，与 mvp_002/003 假设一致；(2) 12/22 模型 c_n > 1，
      old-generation 模型 (GPT-4o, Claude 3 Opus, Gemini 1.5 Pro) 污染最重，符合直觉——这些模型
      训练数据更可能包含 MT-Bench/Arena-Hard 原始题目；(3) 收敛质量优良 (R̂ ≤ 1.03, ESS ≥ 285)，
      与 mvp_003 可比；(4) Arena-Hard 上 G-MFRM 优势略小，因为该 benchmark 更新、暴露度更低，
      这恰好验证了 graceful degradation——当 contamination 低时，G-MFRM 不做有害调整。
      Judge severity 的分布符合预期：smaller open-weight models 更严格，大型 proprietary models 更宽松。

  - name: "baseline_comparison"
    plan_id: "exp-004"
    description: >
      Compare G-MFRM against 8 baselines on same data. Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena.
      Include rank change analysis and post-hoc power analysis.
    expected_results:
      kendall_tau_raw_average: 0.76
      kendall_tau_mfrm_only: 0.80
      kendall_tau_sequential_bias_first: 0.79
      kendall_tau_sequential_contam_first: 0.78
      kendall_tau_cyclicjudge: 0.81
      kendall_tau_cyclicjudge_discard: 0.80
      kendall_tau_dcr: 0.77
      kendall_tau_uda: 0.82
      kendall_tau_prefleak: 0.79
      kendall_tau_gmfrm: 0.87
      delta_tau_vs_best_baseline: 0.05
      best_baseline_name: "UDA"
      delta_tau_p_value_wilcoxon: 0.008
      spearman_rho_gmfrm: 0.93
      spearman_rho_best_baseline: 0.88
      rank_change_top5_stability_gmfrm: 0.90
      rank_change_top5_stability_raw: 0.70
      rank_change_max_displacement: 4
      rank_change_mean_displacement: 1.6
      post_hoc_power_at_observed_delta: 0.86
      n_models: 22
    result_rationale: >
      Best 档要求 delta_tau_vs_best_baseline ∈ [0.04, 0.10] 且 p ∈ [0.001, 0.03]。预测 Δτ = 0.05,
      p = 0.008。UDA 是最强 baseline (τ = 0.82)，因为它通过 neural K-factor 调整隐式捕捉了部分
      judge-item interaction，但它是 black-box 且 contamination-unaware，因此在高污染模型上仍会
      overestimate ability。CyclicJudge (τ = 0.81) 次之，round-robin 消除了 average judge bias
      但无法处理 item-specific judge effects 和 contamination。Sequential pipeline 表现差于
      MFRM-only 和 CyclicJudge，因为 OVB 导致第一阶段的偏差传递到第二阶段——这直接支持 Claim 1
      (confounding claim)。DCR (τ = 0.77) 仅调整 contamination 不调整 judge bias，因此效果有限。
      Post-hoc power = 0.86 > 0.80 阈值，22 models 提供足够的统计功效检测 Δτ = 0.05。
      Top-5 stability 从 raw 的 0.70 提升到 G-MFRM 的 0.90，表明 contamination correction
      主要影响 mid-tier 模型的排名，top models 的相对顺序更稳定但绝对位置有调整。
    tables:
      - name: "Table: Main Result — Method Comparison (Combined MT-Bench + Arena-Hard)"
        columns: ["Method", "Kendall-τ", "Spearman-ρ", "Mean Rank Δ", "Bias-Aware?", "Contam-Aware?"]
        rows:
          - ["Raw Multi-Judge Average", "0.760", "0.842", "ref", "No", "No"]
          - ["MFRM-only", "0.800", "0.871", "1.2", "Yes", "No"]
          - ["Sequential (bias→contam)", "0.790", "0.863", "1.8", "Partial", "Partial"]
          - ["Sequential (contam→bias)", "0.780", "0.855", "2.1", "Partial", "Partial"]
          - ["CyclicJudge", "0.810", "0.878", "1.0", "Yes", "No"]
          - ["CyclicJudge + Item Discard", "0.800", "0.870", "1.1", "Yes", "Partial"]
          - ["DCR Factor", "0.770", "0.848", "0.8", "No", "Yes"]
          - ["UDA", "0.820", "0.885", "1.3", "Yes (implicit)", "No"]
          - ["Preference Leakage Calib.", "0.790", "0.862", "0.9", "Partial", "No"]
          - ["G-MFRM (ours)", "**0.870**", "**0.930**", "**1.6**", "Yes", "Yes"]
      - name: "Table: Rank Change Analysis — Models with Largest Displacement"
        columns: ["Model", "Raw Rank", "G-MFRM Rank", "Displacement", "c_n", "Direction"]
        rows:
          - ["Claude 3 Opus", "8", "12", "-4", "2.12", "Overestimated → corrected down"]
          - ["GPT-4o", "10", "13", "-3", "2.34", "Overestimated → corrected down"]
          - ["Gemini 1.5 Pro", "9", "12", "-3", "1.98", "Overestimated → corrected down"]
          - ["Phi-5", "18", "15", "+3", "0.15", "Underestimated → corrected up"]
          - ["Command R+ v2", "20", "17", "+3", "0.12", "Underestimated → corrected up"]
          - ["GPT-4-turbo", "12", "14", "-2", "1.85", "Overestimated → corrected down"]
      - name: "Table: Post-hoc Power Analysis"
        columns: ["Comparison", "Observed Δτ", "N", "Power (α=0.05)", "Min N for Power=0.80"]
        rows:
          - ["G-MFRM vs UDA", "0.05", "22", "0.86", "18"]
          - ["G-MFRM vs CyclicJudge", "0.06", "22", "0.91", "15"]
          - ["G-MFRM vs Sequential", "0.08", "22", "0.97", "10"]
          - ["G-MFRM vs Raw", "0.11", "22", "0.99", "8"]
    figures_description:
      - "Figure: Bar chart of Kendall-τ for all 9 methods, with 95% bootstrap CI. G-MFRM bar clearly separated from cluster of baselines. Error bars non-overlapping with best baseline (UDA)."
      - "Figure: Rank displacement plot — each model is a horizontal arrow from raw rank to G-MFRM rank. Arrow color by c_n magnitude. High-c_n models shift right (rank worsens), low-c_n models shift left (rank improves)."
      - "Figure: Top-k stability curve (k = 3, 5, 10, 15, 20) for Raw, MFRM, UDA, and G-MFRM. G-MFRM dominates at all k, largest gap at k=10."
    analysis: >
      G-MFRM 在所有指标上显著超越全部 8 个 baseline，Δτ = +0.05 vs UDA (p = 0.008)。结果的
      核心模式完全符合 Claim 3 的预测：(1) 仅处理 bias 的方法 (CyclicJudge, MFRM-only) 优于
      raw average 但 inferior to G-MFRM，因为忽略 contamination；(2) 仅处理 contamination 的方法
      (DCR) 效果最差，因为 judge severity confound 未被处理；(3) sequential pipeline 表现甚至
      不如单独的 CyclicJudge，直接支持 Claim 1——sequential 的 OVB 产生了反效果。
      Rank change analysis 证实了 contamination correction 的实际意义：old-generation 高污染模型
      (GPT-4o, Claude 3 Opus) 被系统性高估了 2-4 个排名位置。Post-hoc power 0.86 确认
      22 models 足以检测观察到的效应量。

  - name: "contamination_magnitude_calibration"
    plan_id: "exp-005"
    description: >
      Compare fitted c_n from exp-003 with synthetic MVP assumptions. Determine if real contamination
      is closer to mvp_001 (weak) or mvp_002/003 (strong). Critical decision point for claim calibration.
    expected_results:
      real_cn_median: 1.05
      real_cn_mean: 1.14
      real_cn_std: 0.72
      real_cn_iqr: [0.52, 1.61]
      closest_mvp: "mvp_003"
      mvp_003_cn_median: 1.20
      mvp_001_cn_median: 0.50
      ratio_real_to_mvp003: 0.875
      high_contamination_model_count: 12
      low_contamination_model_count: 4
      negligible_contamination_model_count: 6
      tier_determination: "Tier A"
      confounding_scatter_r: 0.55
      confounding_scatter_p: 0.008
      theta_bias_direction: "positive (high c_n models overestimated)"
      mt_bench_cn_median: 1.25
      arena_hard_cn_median: 0.78
    result_rationale: >
      Best 档核心假设是 real c_n median ≥ 0.8。预测 median = 1.05，接近但略低于 mvp_003
      设定 (median ~1.2)。这是因为：(1) 现实中 contamination 的分布比合成 DGP 更离散——
      部分模型 (Phi-5, Command R+) 训练数据确实不包含 MT-Bench/Arena-Hard，c_n ≈ 0；
      (2) 但 old-generation models (GPT-4o, Claude 3 Opus, Gemini 1.5 Pro) 的 c_n > 1.8，
      说明这些模型的训练数据高度覆盖了这些 benchmarks；(3) 整体分布是右偏的 heavy-tailed
      分布，median < mean。MT-Bench 的 c_n median (1.25) 高于 Arena-Hard (0.78)，因为
      MT-Bench 更老、更广为人知。Confounding scatter r = 0.55 处于 best 档范围 [0.4, 0.7]
      中部，表明 sequential estimator 确实在高 c_n 模型上系统性高估 θ，OVB 机制在真实数据上
      得到验证。Tier A 判定成立：contamination 足够强，joint estimation 的优势有实际意义。
    tables:
      - name: "Table: Real vs Synthetic Contamination Magnitude"
        columns: ["Source", "c_n Median", "c_n Mean", "c_n SD", "IQR", "Best Tier Match"]
        rows:
          - ["mvp_001 (weak)", "0.50", "0.50", "0.25", "[0.33, 0.67]", "No"]
          - ["mvp_002 (strong, unconverged)", "1.30", "1.30", "0.60", "[0.85, 1.75]", "Partial"]
          - ["mvp_003 (strong, converged)", "1.20", "1.20", "0.55", "[0.78, 1.62]", "Closest"]
          - ["Real data (exp-003)", "1.05", "1.14", "0.72", "[0.52, 1.61]", "Tier A confirmed"]
      - name: "Table: Per-Benchmark Contamination Summary"
        columns: ["Benchmark", "N Items", "c_n Median", "Mean e_i", "High-c Models", "Tier"]
        rows:
          - ["MT-Bench", "80", "1.25", "0.62", "14/22", "A (strong)"]
          - ["Arena-Hard", "500", "0.78", "0.45", "9/22", "A (borderline)"]
          - ["Combined", "580", "1.05", "0.47", "12/22", "A"]
    figures_description:
      - "Figure: c_n distribution comparison — overlaid density plots for mvp_001, mvp_003, and real data. Real distribution sits between mvp_001 and mvp_003 but closer to mvp_003, with heavier right tail."
      - "Figure: Confounding scatter plot — x-axis: c_n (contamination susceptibility), y-axis: θ_sequential - θ_joint (bias). Pearson r = 0.55. Each dot is a model. Regression line with 95% CI shaded. Clear positive trend: high c_n → sequential overestimates."
      - "Figure: Per-benchmark c_n violin plots side by side, showing MT-Bench has systematically higher contamination than Arena-Hard."
    analysis: >
      实验明确确认 Tier A 叙事。real c_n median = 1.05 落在 best 档 [0.8, 1.5] 范围内，
      最接近 mvp_003 设定。关键的 confounding scatter r = 0.55 证明 OVB 机制在真实数据上
      不仅存在而且具有实际显著性 (p = 0.008)。跨 benchmark 分析显示一个有趣的模式：
      MT-Bench contamination 更强但 Arena-Hard contamination 也不可忽略——这意味着
      G-MFRM 在两个 benchmark 上都有修正价值，但 MT-Bench 上的修正更大。这个发现本身
      就有独立的方法论价值：不同 benchmark 的 contamination 程度不同，joint estimation
      的收益与 benchmark 年龄/知名度正相关。Tier A 判定使 paper framing 无需调整，
      三个 claims 都可以 full strength 呈现。

  - name: "judge_count_sensitivity"
    plan_id: "exp-006"
    description: >
      Sensitivity analysis: vary number of judges (2, 4, 6, 8) and measure G-MFRM performance degradation.
      Include leave-one-judge-out residual diagnostic for preference leakage detection.
    expected_results:
      tau_8_judges: 0.87
      tau_6_judges: 0.85
      tau_4_judges: 0.82
      tau_2_judges: 0.78
      min_judges_for_superiority_over_sequential: 4
      min_judges_for_superiority_over_best_baseline: 6
      graceful_degradation_at_2_judges: "G-MFRM ≈ MFRM (Δτ < 0.01)"
      leave_one_out_max_residual_change: 0.08
      leave_one_out_flagged_judge: "none (no preference leakage detected)"
      same_family_residual_inflation: 0.03
      rhat_max_at_4_judges: 1.04
      rhat_max_at_2_judges: 1.08
      ess_min_at_4_judges: 180
      ess_min_at_2_judges: 95
    result_rationale: >
      Best 档假设 ≥ 6 judges produce sufficient facet variance for identifiability。随着 judge 数量
      减少，d_j facet 的信息量下降，c_n 和 d_j 的区分变困难。8→6 judges 时性能仅轻微下降 (τ −0.02)
      因为 6 judges 仍然提供足够的 facet heterogeneity。6→4 时下降加速 (τ −0.03) 因为 judge 多样性
      显著降低。4→2 时 G-MFRM 退化到接近 MFRM 水平 (τ = 0.78 ≈ MFRM 0.80)，因为 2 judges 无法
      同时 identify d_j 和 c_n——这符合理论预期 (2 judges 只有 1 个 severity contrast)。关键阈值：
      4 judges 仍优于 sequential (0.82 > 0.79)，6 judges 优于 best baseline UDA (0.85 > 0.82)。
      Convergence 在 4 judges 时仍可接受 (R̂ ≤ 1.04, ESS ≥ 180) 但 2 judges 时 R̂ = 1.08 > 1.05 阈值，
      ESS = 95 < 150 阈值。Leave-one-out 分析未检测到明显的 preference leakage——在 best 档下，
      8 judges 的 round-robin 设计足以稀释 same-family bias (PLS ~23.6% 被 7 个其他 judges 稀释)。
    tables:
      - name: "Table: Judge Count Sensitivity"
        columns: ["N Judges", "Kendall-τ", "Δτ vs Best Baseline", "R-hat Max", "ESS Min", "Convergence OK?"]
        rows:
          - ["8 (full)", "0.870", "+0.050", "1.03", "285", "Yes"]
          - ["6", "0.850", "+0.030", "1.03", "230", "Yes"]
          - ["4", "0.820", "+0.000", "1.04", "180", "Yes"]
          - ["2", "0.780", "−0.040", "1.08", "95", "No"]
      - name: "Table: Leave-One-Judge-Out Residual Diagnostics"
        columns: ["Removed Judge", "Δτ", "Max Residual Change", "Same-Family Inflation", "Flagged?"]
        rows:
          - ["GPT-5.5", "-0.008", "0.06", "0.03", "No"]
          - ["Claude Opus 4.7", "-0.005", "0.04", "0.02", "No"]
          - ["Claude Sonnet 4.6", "-0.003", "0.03", "0.02", "No"]
          - ["DeepSeek-V4-Pro", "-0.004", "0.05", "0.01", "No"]
          - ["Qwen3-235B-A22B", "-0.006", "0.05", "0.02", "No"]
          - ["Qwen3.6-27B", "-0.009", "0.08", "0.03", "No"]
          - ["Llama 4 Maverick", "-0.005", "0.04", "0.02", "No"]
          - ["Gemini 2.5 Pro", "-0.004", "0.04", "0.01", "No"]
    figures_description:
      - "Figure: Judge count sensitivity curve — x-axis: N judges, y-axis: Kendall-τ. Lines for G-MFRM, MFRM, UDA, raw average. G-MFRM crosses MFRM at N=2, crosses UDA at N=6. Shaded region: convergence failure zone (N<3)."
      - "Figure: Leave-one-judge-out stability plot — 8 bars showing τ when each judge is removed. Error bars from bootstrap. No single judge removal causes >0.01 τ change."
    analysis: >
      结果为论文 Limitations 提供了具体指导：G-MFRM 在 4+ judges 时仍优于 sequential baseline，
      在 6+ judges 时优于 best baseline (UDA)，在 2 judges 时 gracefully degrades 到 MFRM 水平。
      这为 practitioners 提供了明确的 cost-benefit guidance：如果只能负担 4 judges，G-MFRM 仍有
      contamination correction 价值但不优于 UDA；6+ judges 是推荐最小配置。Leave-one-out 分析
      确认了 8-judge pool 的鲁棒性——没有单个 judge 是不可替代的，也没有 judge 表现出 preference
      leakage pattern。

  - name: "exposure_indicator_ablation"
    plan_id: "exp-007"
    description: >
      Ablation of each exposure indicator's contribution to e_i estimation quality.
      Leave-one-out analysis of performance gap, temporal signal, and LogProber.
    expected_results:
      full_pipeline_tau: 0.87
      ablate_logprober_tau: 0.855
      ablate_temporal_tau: 0.860
      ablate_performance_gap_tau: 0.830
      performance_gap_only_tau: 0.855
      temporal_only_tau: 0.810
      logprober_only_tau: 0.825
      ei_internal_consistency_full: 0.68
      ei_internal_consistency_no_logprober: 0.63
      ei_internal_consistency_no_temporal: 0.65
      ei_internal_consistency_no_perfgap: 0.48
      cn_recovery_corr_full: 0.72
      cn_recovery_corr_no_logprober: 0.67
      cn_recovery_corr_no_temporal: 0.69
      cn_recovery_corr_no_perfgap: 0.53
    result_rationale: >
      Performance gap 是 e_i 估计的主信号 (权重 0.55)，移除它导致最大性能下降 (τ: 0.87 → 0.83,
      Δ = −0.04)。这是因为 performance gap 是唯一直接度量 item-level contamination effect 的指标——
      通过比较模型在原始 vs 改写 items 上的表现差异，直接反映了 memorization 的程度。Temporal
      和 LogProber 各自只捕捉 contamination 的间接信号 (时间先后、token logprob)。移除 LogProber
      的影响较小 (Δτ = −0.015)，因为它只覆盖 45% 的模型，但对覆盖到的模型提供了高精度信号。
      移除 temporal signal 影响更小 (Δτ = −0.010)，因为它的噪声最大但提供了广覆盖的 baseline
      信号。关键发现：即使 performance gap only (τ = 0.855)，G-MFRM 仍然优于 all baselines
      except UDA (0.82)——这意味着 paper 的主结果不依赖于 LogProber 或 temporal signal 的
      可用性，降低了方法的 adoption barrier。
    tables:
      - name: "Table: Exposure Indicator Ablation"
        columns: ["Configuration", "e_i Consistency (α)", "c_n ConStat Corr", "G-MFRM τ", "Δτ vs Full"]
        rows:
          - ["Full pipeline (all 3)", "0.68", "0.72", "0.870", "ref"]
          - ["−LogProber", "0.63", "0.67", "0.855", "−0.015"]
          - ["−Temporal", "0.65", "0.69", "0.860", "−0.010"]
          - ["−Performance Gap", "0.48", "0.53", "0.830", "−0.040"]
          - ["Performance Gap only", "0.58", "0.64", "0.855", "−0.015"]
          - ["Temporal only", "0.41", "0.48", "0.810", "−0.060"]
          - ["LogProber only", "0.52", "0.57", "0.825", "−0.045"]
    figures_description:
      - "Figure: Ablation waterfall chart — starting from full pipeline τ=0.87, showing marginal contribution of each component. Performance gap contributes most (~60% of total improvement over no-exposure baseline)."
      - "Figure: e_i scatter — full pipeline e_i vs performance-gap-only e_i. High correlation (r=0.89) but temporal/LogProber provide refinement in mid-range exposure items."
    analysis: >
      Ablation 确认 performance gap 是核心信号，但三源组合比任何单一信号更好。对 paper 的意义：
      (1) 方法的最小可行版本只需要 reference variant construction (performance gap)，降低
      adoption barrier；(2) LogProber 和 temporal signal 提供增量改善，值得使用但不是 required；
      (3) 论文中可以将 performance gap 作为 primary method 呈现，其余两个作为 supplementary
      indicators。这也解释了为什么 exp-012 中 e_i noise σ=0.2 时 G-MFRM 仍然 robust——
      即使 secondary signals 有噪声，primary signal 足够稳定。

  - name: "facet_fit_diagnostics"
    plan_id: "exp-008"
    description: >
      Measurement quality validation: infit/outfit MNSQ for all facets, divergent transition count,
      posterior predictive check, trace plots.
    expected_results:
      theta_infit_mnsq_range: [0.82, 1.18]
      theta_outfit_mnsq_range: [0.78, 1.25]
      theta_misfit_count: 1
      b_infit_mnsq_range: [0.75, 1.30]
      b_outfit_mnsq_range: [0.70, 1.42]
      b_misfit_count: 18
      d_infit_mnsq_range: [0.85, 1.15]
      d_outfit_mnsq_range: [0.80, 1.20]
      d_misfit_count: 0
      c_infit_mnsq_range: [0.78, 1.22]
      c_outfit_mnsq_range: [0.72, 1.35]
      c_misfit_count: 2
      divergent_transitions: 0
      ppc_p_value: 0.38
      ppc_dof_corrected: true
      lz_vs_cn_correlation: 0.52
      emri_vs_cn_correlation: 0.48
      stage1_vs_stage3_theta_corr: 0.96
      flagged_items_outfit_gt_2: 3
    result_rationale: >
      Best 档假设 G-MFRM converges cleanly (R̂ ≤ 1.05, ESS ≥ 150)，facet fit diagnostics 是
      这个假设的延伸验证。θ facet 的 infit/outfit MNSQ 在 [0.82, 1.18] / [0.78, 1.25] 范围，
      完全在可接受范围 [0.5, 1.5] (Linacre 2002) 内，仅 1 个模型 misfit (可能是 Jamba 2——
      其能力 profile 与 Rasch 假设的单维度结构最不一致)。b facet 有 18 个 misfit items
      (580 items 中的 3.1%)，这是正常水平——MT-Bench coding items 倾向于 outfit > 1.3 因为
      它们更 "all-or-nothing" (不符合 Rasch 的渐进概率假设)。d facet 0 个 misfit 表明
      8 judges 的 severity 结构清晰。c facet 有 2 个 misfit models，可能是训练数据包含
      partial benchmark overlap 的模型 (rank-1 c_n·e_i 假设对它们近似较差)。零 divergent
      transitions 确认 NUTS sampler 在这个模型上工作良好。PPC p = 0.38 表明模型对数据
      的拟合在可接受范围 (p < 0.05 才报警)。lz vs c_n 的 corr = 0.52 表明 person-fit
      residual 和 contamination susceptibility 有中等相关——高 c_n 模型确实表现出更多
      model-data misfit，因为 contamination 造成的 performance inflation 产生了看似
      inconsistent 的 response pattern。
    tables:
      - name: "Table: Facet Fit Summary (Infit/Outfit MNSQ)"
        columns: ["Facet", "N", "Infit Range", "Outfit Range", "Misfit Count", "Misfit %"]
        rows:
          - ["θ (model ability)", "22", "[0.82, 1.18]", "[0.78, 1.25]", "1", "4.5%"]
          - ["b (item difficulty)", "580", "[0.75, 1.30]", "[0.70, 1.42]", "18", "3.1%"]
          - ["d (judge severity)", "8", "[0.85, 1.15]", "[0.80, 1.20]", "0", "0%"]
          - ["c (contamination)", "22", "[0.78, 1.22]", "[0.72, 1.35]", "2", "9.1%"]
      - name: "Table: MCMC Diagnostic Summary"
        columns: ["Diagnostic", "Value", "Threshold", "Status"]
        rows:
          - ["R-hat max (all params)", "1.03", "≤ 1.05", "PASS"]
          - ["ESS min (all params)", "285", "≥ 150", "PASS"]
          - ["Divergent transitions", "0", "0", "PASS"]
          - ["PPC p-value", "0.38", "> 0.05", "PASS"]
          - ["BFMI (E-BFMI)", "0.92", "> 0.3", "PASS"]
      - name: "Table: Person-Fit vs Contamination Correlation"
        columns: ["Person-Fit Index", "Corr with c_n", "p-value", "Interpretation"]
        rows:
          - ["lz (likelihood-based)", "0.52", "0.013", "Moderate: high c_n ↔ response aberrance"]
          - ["EMRi (residual-based)", "0.48", "0.024", "Moderate: contamination creates inconsistent patterns"]
          - ["Stage 1 θ - Stage 3 θ", "0.61", "0.003", "Strong: bias correction proportional to c_n"]
    figures_description:
      - "Figure: Infit-outfit bubble chart (Wright map) for all 22 models. Bubble size = c_n. Most models within acceptable zone; 2 high-c_n models near boundary."
      - "Figure: Posterior predictive check — observed vs predicted score distributions by judge and by model. Overlay shows good fit (close to diagonal)."
      - "Figure: Trace plots (4 panels) for representative parameters: θ_GPT-5.5, c_n_GPT-4o, d_Qwen3.6-27B, b_item42. All show stationary mixing."
    analysis: >
      Diagnostics 全面通过，为 G-MFRM 的 measurement quality 提供了坚实证据。关键发现：
      (1) 所有 MCMC diagnostics PASS，零 divergent transitions 说明 model parameterization 合适；
      (2) Item misfit 率 3.1% 在 Rasch 文献的正常范围 (typically 2-5%)，且 misfit items
      集中在 coding category (binary-like responses)——可在 Limitations 中讨论；
      (3) lz vs c_n 的 moderate correlation (0.52) 提供了 construct coherence 的 convergent evidence：
      contamination 确实产生了可被 person-fit 检测到的 response aberrance，且 G-MFRM 的 c_n
      parameter 正好捕捉了这个效应。这支持了 G-MFRM 不仅是 statistical fitting 而是在捕捉
      genuine contamination signal 的论点。

  - name: "confounding_formal_observation"
    plan_id: "exp-009"
    description: >
      Derive first-order bias approximation for sequential estimator under d_j/c_n·e_i non-orthogonality.
      Monte Carlo validation + synthetic c_n point-estimate validation.
    expected_results:
      bias_approximation_validated: true
      monte_carlo_replications: 1000
      bias_direction_correct_pct: 0.97
      first_order_bias_magnitude_mean: 0.18
      first_order_bias_magnitude_std: 0.06
      second_order_correction_improvement: 0.12
      cn_point_estimate_rmse: 0.48
      cn_95ci_coverage: 0.91
      cn_corr_with_truth: 0.88
      rho_range_tested: [0.0, 0.8]
      bias_at_rho_0: 0.003
      bias_at_rho_0_3: 0.052
      bias_at_rho_0_6: 0.141
      bias_at_rho_0_8: 0.248
      theta_rmse_sequential_vs_joint_rho_0_6: 0.33
    result_rationale: >
      Best 档假设 confounding scatter r ≥ 0.4，即 d_j 和 c_n·e_i 在真实数据上 empirically
      non-orthogonal。Monte Carlo 验证 first-order OVB approximation：在 1000 replications 中，
      97% 的情况下 sequential estimator 的 bias 方向与理论预测一致 (high c_n → overestimate θ)。
      Bias 随 ρ(d,c·e) 单调递增：ρ=0 时几乎无 bias (0.003，数值噪声)，ρ=0.3 时 bias = 0.052
      (对应 mvp_001 接近失败的区域)，ρ=0.6 时 bias = 0.141 (对应 best 档的真实数据区域)，
      ρ=0.8 时 bias = 0.248 (极端但可能的情景)。c_n 点估计 RMSE = 0.48，95% CI coverage = 0.91
      (接近 nominal 0.95)，c_n 与真值相关 0.88——确认 G-MFRM 的 Stage 3 不仅能 correct θ
      还能 recover underlying c_n signal with reasonable accuracy。CI 略 under-coverage (0.91 vs 0.95)
      可能因 Stage 2→3 的 error propagation 未完全被 posterior 捕捉，可引用 exp-012 的
      sensitivity analysis 作为补充讨论。
    tables:
      - name: "Table: Monte Carlo OVB Validation"
        columns: ["ρ(d, c·e)", "N Reps", "Mean Bias(θ_seq)", "SD Bias", "Bias Direction Correct %", "Joint RMSE", "Seq RMSE", "RMSE Reduction"]
        rows:
          - ["0.0", "1000", "0.003", "0.018", "52%", "0.128", "0.129", "0.8%"]
          - ["0.2", "1000", "0.031", "0.024", "83%", "0.130", "0.138", "5.8%"]
          - ["0.3", "1000", "0.052", "0.029", "91%", "0.131", "0.152", "13.8%"]
          - ["0.4", "1000", "0.082", "0.035", "95%", "0.132", "0.171", "22.8%"]
          - ["0.6", "1000", "0.141", "0.048", "97%", "0.134", "0.213", "37.1%"]
          - ["0.8", "1000", "0.248", "0.067", "99%", "0.137", "0.302", "54.6%"]
      - name: "Table: Synthetic c_n Recovery Accuracy"
        columns: ["Metric", "Value", "Threshold", "Status"]
        rows:
          - ["c_n RMSE (vs ground truth)", "0.48", "< 0.80", "PASS"]
          - ["c_n correlation with truth", "0.88", "> 0.70", "PASS"]
          - ["95% CI coverage probability", "0.91", "≈ 0.95", "Slight under-coverage"]
          - ["Mean c_n bias", "+0.05", "< |0.20|", "PASS"]
          - ["c_n rank-order Kendall-τ with truth", "0.85", "> 0.70", "PASS"]
    figures_description:
      - "Figure: Bias vs ρ curve — x-axis: non-orthogonality ρ(d,c·e), y-axis: mean |bias(θ_seq)|. Solid line = Monte Carlo mean, shaded = 95% envelope. Dashed line = first-order approximation. Close match up to ρ≈0.6, slight divergence at ρ>0.7 (higher-order terms)."
      - "Figure: c_n recovery scatter — fitted c_n vs true c_n (one dot per model, 20 models × 50 reps). Tight cluster around diagonal, slight upward bias for very high c_n."
      - "Figure: Sequential bias direction illustration — arrows showing how high c_n models get pushed right (θ overestimated) and low c_n models get pushed left (θ underestimated) under sequential estimation."
    analysis: >
      Formal observation 在 Monte Carlo 验证中得到完全确认。First-order OVB approximation 在
      ρ ≤ 0.6 范围内准确 (与 Monte Carlo 偏差 < 5%)，在更高 ρ 时 higher-order terms 变得
      重要但 bias direction 仍然正确 (99%)。这为 paper Section 2 提供了坚实的理论基础：
      sequential estimation 不是 "slightly suboptimal"，而是在 non-orthogonal 情况下
      systematically biased，bias 方向和大小可预测。c_n recovery 的成功 (RMSE=0.48, corr=0.88)
      直接回应 Dream R1-N3：G-MFRM 不仅能 correct rankings，还能产生有意义的 per-model
      contamination estimates。95% CI 的轻微 under-coverage 是 staged estimation 的已知代价，
      可与 exp-012 的 error propagation 结果交叉引用。

  - name: "wildbench_replication"
    plan_id: "exp-010"
    description: >
      Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark generalization test.
    expected_results:
      wildbench_items: 1024
      wildbench_judges: 8
      wildbench_models: 22
      kendall_tau_gmfrm_wildbench: 0.84
      kendall_tau_raw_average_wildbench: 0.74
      kendall_tau_best_baseline_wildbench: 0.79
      delta_tau_gmfrm_vs_best_baseline: 0.05
      delta_tau_p_value: 0.012
      cn_median_wildbench: 0.68
      cn_corr_with_mt_bench_cn: 0.82
      ei_mean_wildbench: 0.38
      rhat_max: 1.04
      ess_min: 195
      cross_benchmark_cn_consistency: 0.78
    result_rationale: >
      WildBench (2024-05 release, 1024 items from real user queries) 是比 MT-Bench 和 Arena-Hard
      更 diverse 的 benchmark，但 contamination level 预期较低 (median c_n = 0.68)，因为：
      (1) 更新，训练数据覆盖率更低；(2) items 来自 real user queries 而非人工设计，更难被
      memorized；(3) items 更多更多样，降低了每个 item 被特定训练的概率。τ = 0.84 低于
      MT-Bench + Arena-Hard combined (0.87)，反映了 WildBench 的 contamination 更低 (joint vs
      sequential 的优势随 contamination 降低而缩小)。但 Δτ = +0.05 vs best baseline 仍然
      显著 (p = 0.012)，确认 G-MFRM 的优势 generalizes across benchmarks。c_n 跨 benchmark
      相关 0.82 表明 per-model contamination susceptibility 是 model-level trait (不依赖于
      specific benchmark)——这是有意义的方法论发现。收敛略差 (R̂ = 1.04, ESS = 195) 因为
      WildBench items 更多样，Rasch 单维度假设拟合度稍差，但仍在可接受范围内。
    tables:
      - name: "Table: Cross-Benchmark Generalization"
        columns: ["Benchmark", "N Items", "G-MFRM τ", "Best Baseline τ", "Δτ", "p-value", "c_n Median"]
        rows:
          - ["MT-Bench", "80", "0.880", "0.830", "+0.050", "0.015", "1.25"]
          - ["Arena-Hard", "500", "0.860", "0.810", "+0.050", "0.010", "0.78"]
          - ["WildBench", "1024", "0.840", "0.790", "+0.050", "0.012", "0.68"]
          - ["Combined (all 3)", "1604", "0.870", "0.820", "+0.050", "0.003", "0.82"]
    figures_description:
      - "Figure: Cross-benchmark τ comparison grouped bar chart. Three benchmark clusters + combined. G-MFRM consistently above baselines, advantage inversely proportional to benchmark age/exposure."
      - "Figure: c_n cross-benchmark scatter — MT-Bench c_n vs WildBench c_n per model. High correlation (r=0.82) confirms contamination susceptibility is a stable model-level property."
    analysis: >
      WildBench replication 确认 G-MFRM 优势 generalizes across benchmarks。最重要的发现是
      跨 benchmark c_n 一致性 (r = 0.82)——同一个模型在不同 benchmarks 上的 contamination
      susceptibility 高度相关，这为 c_n 作为 "模型级 contamination trait" 的解释提供了
      empirical support。Δτ = +0.05 在三个 benchmarks 上高度一致，说明 G-MFRM 的改善
      不是 benchmark-specific artifact。WildBench 的较低 contamination (median 0.68) 导致
      较低的绝对 τ 但 Δτ 保持稳定——这支持了 best 档的叙事：即使在 moderate contamination
      场景下，joint estimation 仍有显著价值。

  - name: "adversarial_robustness"
    plan_id: "exp-011"
    description: >
      Test G-MFRM robustness against adversarial contamination following Wang et al. (ICLR 2026)
      fragility findings.
    expected_results:
      adversarial_attack_types_tested: 3
      attack_1_name: "answer_injection (direct benchmark answer insertion)"
      attack_1_cn_detection_rate: 0.85
      attack_1_tau_gmfrm: 0.83
      attack_1_tau_raw: 0.65
      attack_2_name: "style_mimicry (benchmark-style response training)"
      attack_2_cn_detection_rate: 0.72
      attack_2_tau_gmfrm: 0.82
      attack_2_tau_raw: 0.70
      attack_3_name: "selective_memorization (memorize only high-weight items)"
      attack_3_cn_detection_rate: 0.61
      attack_3_tau_gmfrm: 0.80
      attack_3_tau_raw: 0.68
      overall_robustness_score: 0.82
      rank_manipulation_success_rate_without_gmfrm: 0.73
      rank_manipulation_success_rate_with_gmfrm: 0.28
    result_rationale: >
      Best 档下 G-MFRM 对 adversarial contamination 展现出中等-强鲁棒性。Answer injection
      (最粗暴的攻击) 检测率最高 (0.85)，因为它产生最大的 performance gap (original vs reference)
      和最明显的 item-level anomaly pattern。Style mimicry (更隐蔽) 检测率降至 0.72，因为
      它不产生 item-specific memorization 而是 general style transfer，c_n·e_i 的 rank-1
      结构对此的拟合度较差。Selective memorization (最危险) 检测率最低 (0.61)，因为攻击者
      选择性地 memorize high-weight items，产生的 pattern 与 legitimate ability 更相似。
      但即使在最差情况下 (attack 3)，G-MFRM (τ = 0.80) 仍优于 raw average (τ = 0.68)。
      Rank manipulation success rate 从 without-G-MFRM 的 73% 降至 with-G-MFRM 的 28%——
      G-MFRM 使 adversarial ranking gaming 变得 substantially harder。这个实验主要为
      Discussion section 提供 material，不是 main contribution 但强化了 practical impact。
    tables:
      - name: "Table: Adversarial Robustness Summary"
        columns: ["Attack Type", "Detection Rate", "G-MFRM τ", "Raw τ", "τ Recovery %", "Rank Manip. Blocked"]
        rows:
          - ["No attack (baseline)", "N/A", "0.87", "0.76", "100%", "N/A"]
          - ["Answer injection", "0.85", "0.83", "0.65", "95%", "78%"]
          - ["Style mimicry", "0.72", "0.82", "0.70", "94%", "65%"]
          - ["Selective memorization", "0.61", "0.80", "0.68", "92%", "52%"]
    figures_description:
      - "Figure: Adversarial robustness radar chart — axes: detection rate, τ preservation, rank stability, c_n accuracy, convergence quality. G-MFRM polygon substantially larger than raw baseline across all attacks."
      - "Figure: Attack severity vs detection rate curve — as attack becomes more sophisticated, detection drops but G-MFRM still maintains significant advantage over unprotected evaluation."
    analysis: >
      G-MFRM 对 adversarial contamination 的鲁棒性为 paper 的 practical impact 增添重要维度。
      核心信息：G-MFRM 不是 foolproof 但 substantially raises the bar for adversarial gaming——
      rank manipulation 成功率从 73% 降至 28%。最隐蔽的攻击 (selective memorization) 仍有 39%
      逃逸率 (1 - 0.61 detection rate)，这应在 Limitations 中诚实报告。但即使攻击逃逸了 c_n
      检测，G-MFRM 的 judge severity correction (d_j) 仍提供 partial protection。这个结果
      支持了 paper 的 broader message：LLM evaluation 需要多维度的 protection，G-MFRM 是
      a significant step but not the final answer。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "c57e575f-689a-4d40-b624-440c985d2563",
  "isSidechain": false,
  "requestId": "req_011CbGxSVnWnEbtaHYmJ8Koe",
  "type": "assistant",
  "uuid": "f44427be-7c34-4b02-98d6-71e9992358db",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_0172DQeSEDxbY6G88bHiMcAP",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13959,
      "cache_read_input_tokens": 11447,
      "output_tokens": 21073,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13959,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 21073,
          "cache_read_input_tokens": 11447,
          "cache_creation_input_tokens": 13959,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13959
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

_source line 11_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real contamination moderate-to-strong, joint estimation clearly dominates sequential on real data, all three claims hold at full strength — Tier A narrativ…",
  "leafUuid": "f44427be-7c34-4b02-98d6-71e9992358db",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "ai-title",
  "aiTitle": "Real-data validation of G-MFRM joint contamination and bias correction",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Real contamination moderate-to-strong, joint estimation clearly dominates sequential on real data, all three claims hold at full strength — Tier A narrativ…",
  "leafUuid": "f44427be-7c34-4b02-98d6-71e9992358db",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "Real-data validation of G-MFRM joint contamination and bias correction",
  "sessionId": "f77fcd49-85a9-4148-bebd-f522d7131fae"
}
```

---
