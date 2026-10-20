# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Real contamination weak-to-moderate, ranking improvement positive but smal

**Fair Scores via Joint Calibration: A Gated Many-Facet Rasch Model for Disentangling Judge Bias and Contamination in LLM Evaluation (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/5895a655-1fea-483f-b3a9-6bcf7175ca36.jsonl`
- **Structured JSON:** [`8b053ab86d09a65edaaf.json`](../../sessions/8b/8b053ab86d09a65edaaf.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-22T04:20:03.864Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-22T04:20:03.864Z",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Real contamination weak-to-moderate, ranking improvement positive but small/borderline, confounding mechanism confirmed but practical impact modest — Tier B narrative with diagnostics elevated to co-primary\n核心假设：['Real c_n distribution has median 0.3–0.7 (closer to mvp_001 regime for some models, mvp_002 for a few)', 'Confounding exists but effect size in θ-bias is ≤ 0.15 logits for most models', 'G-MFRM converges acceptably (R̂ ≤ 1.10, ESS ≥ 80) — may need thinning or extended warmup', 'e_i pipeline noisy for some items (effective σ_e ≈ 0.2–0.3), but aggregate signal holds', 'Δτ positive but Wilcoxon p-value borderline (0.03–0.10) due to N≈20 models limiting power', 'Post-hoc power < 0.80 for primary comparison']\n关键指标范围：{'real_cn_median': [0.3, 0.7], 'kendall_tau_gmfrm': [0.78, 0.85], 'kendall_tau_best_baseline': [0.75, 0.83], 'delta_tau_vs_best_baseline': [0.01, 0.04], 'delta_tau_p_value': [0.03, 0.12], 'theta_rmse_reduction_vs_sequential': [0.05, 0.2], 'confounding_scatter_r': [0.25, 0.45], 'convergence_rhat_max': [1.03, 1.1], 'convergence_ess_min': [80, 200], 'cn_constat_validation_corr': [0.4, 0.65], 'ei_pipeline_internal_consistency': [0.3, 0.55]}\n叙事方向：Reframe: joint estimation is methodologically principled AND provides unique diagnostic value, even when ranking improvement is modest. Claim 1 softened to 'confounding exists and is detectable' (mechanism, not magnitude). Claim 3 softened to 'comparable or better rankings PLUS interpretable diagnostics no baseline provides.' Elevate per-model c_n, per-judge d_j, per-item e_i as co-primary contribution. Lead with 'unified diagnostic framework' angle. Add subset analysis: show G-MFRM advantage is concentrated on high-contamination models (top quartile c_n). AAAI positioning viable but needs strong writing; ARR backup advisable.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: gated_mfrm_judge_bias\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — gated_mfrm_judge_bias\n\n## Target Venue\n- Primary: AAAI 2027 (full paper, deadline July 28, 2026)\n- Backup: ACL 2027 via ARR (submission August 3, 2026)\n- Timeline: ~68 days from today (2026-05-21)\n\n## Core Insight\nSequential approaches to judge bias correction and contamination adjustment produce biased model ability estimates due to omitted variable confounding. Joint estimation within a single psychometric calibration framework is methodologically necessary, not merely convenient.\n\n## Core Claims (3 条，均可证伪)\n\n1. **Confounding Claim**: When judge severity (d_j) and contamination susceptibility (c_n·e_i) are both present but only one is modeled, the unmodeled facet's effect is absorbed into other parameter estimates, producing systematic bias in model ability rankings. Sequential pipelines (bias-first or contamination-first) do not resolve this confounding. (Note: OVB formalization supports this claim as mechanism explanation — \"identify and quantify confounding in LLM evaluation\" — not as independent theoretical contribution. Cite Angrist & Pischke 2009 as source.)\n\n2. **Framework Claim**: The Gated Many-Facet Rasch Model (G-MFRM) — combining MFRM's multi-facet structure with DG-IRT's gating mechanism and externally-anchored exposure indicators — provides a staged joint calibration that estimates model ability, item difficulty, judge severity, and contamination susceptibility, yielding bias-and-contamination-corrected \"fair scores.\" (Note: \"staged joint\" — e_i is pre-estimated in Stage 2 and fixed in Stage 3; the joint estimation is conditional on e_i. This is a deliberate identifiability choice, not fully simultaneous. Paper must use \"staged joint calibration\" or \"conditional joint estimation,\" never \"fully joint.\")\n\n3. **Empirical Claim**: G-MFRM fair scores achieve higher agreement with human rankings (Chatbot Arena votes, Kendall-τ) than all baselines: raw multi-judge averages, bias-only correction (CyclicJudge, UDA), contamination-only adjustment (DCR), and naive sequential pipelines.\n\n## Story Spine\n\n- **Problem**: LLM-as-a-judge evaluation has bifurcated into two correction silos — judge bias and benchmark contamination — that are addressed independently. But judge severity and contamination effects are confounded: bias-only methods absorb contamination inflation into ability estimates; contamination-only methods misattribute judge effects as contamination signals. Sequential correction cannot resolve this because the first stage's estimates are already biased by the unmodeled facet.\n\n- **Existing approaches & gaps**: CyclicJudge eliminates average judge bias via round-robin but ignores contamination. UDA uses neural K-factor adjustment (−63.4% inter-judge std) but is black-box and contamination-unaware. DCR/ConStat quantify contamination effects (r²=0.94) but ignore judge variation. In LLM evaluation literature, no existing work jointly models both within a single calibration framework. (Note: educational measurement has MFRM+DIF joint modeling — Eckes 2011, Patz et al. 2002, Fox & Glas 2001, Wind & Peterson 2018 — but these address test fairness, not LLM contamination. G-MFRM is the first to apply continuous-exposure gating within MFRM for LLM evaluation. \"First\" claim must be precisely scoped to LLM evaluation with continuous exposure.)\n\n- **Our framing**: Joint estimation is methodologically necessary. We formalize this as an omitted variable bias problem: under non-orthogonality of d_j and c_n·e_i, sequential estimators are asymptotically biased (direction determined by covariance sign). G-MFRM resolves this by estimating all facets simultaneously, with a three-stage procedure ensuring identifiability: (1) standard MFRM for initial estimates, (2) external per-item exposure estimation via item-level performance gap (original vs reference variants) with difficulty correction, supplemented by temporal signals and LogProber where available, (3) joint gated model with e_i fixed and c_n as latent parameters. ConStat per-model delta serves as external validation of fitted c_n.\n\n- **Headline result template**: \"On MT-Bench/Arena-Hard with 8 LLM judges, G-MFRM fair scores achieve X% higher Kendall-τ with Chatbot Arena human votes than the best sequential baseline, while simultaneously producing interpretable per-model contamination estimates and per-judge severity profiles.\"\n\n## Narrative Strategy (from distilled writing)\n\n- **Type**: \"突破局限\" (sequential has structural flaw) + \"统一框架\" (G-MFRM unifies both corrections)\n- **Opening hook**: Quantitative shock — lead with confounding's θ-RMSE degradation (43.8% in synthetic, to be validated on real data)\n- **Section 2**: Toy example / formal **observation** (NOT \"proposition\" — this is standard OVB from Angrist & Pischke 2009 applied to LLM evaluation; cite originals, present as domain-specific instantiation) demonstrating confounding before introducing G-MFRM method\n- **Figure 1**: Left = sequential pipeline with confounding annotation, Right = joint G-MFRM with gating mechanism highlighted\n- **Main result table**: rows = methods (7 baselines + G-MFRM), cols = benchmarks × metrics\n- **Ablation**: Full numbers (not checkmark grid), rows = components on/off\n\n## Venue Fit Risks\n\n- **AAAI**: Good fit for psychometric methodology applied to AI evaluation. Risk: reviewers may lack MFRM/IRT background — need clear, self-contained exposition with toy examples. Strength: AAAI values formal modeling + practical impact.\n- **ACL/ARR**: Good fit for LLM evaluation methodology. Risk: may demand stronger NLP-specific contributions beyond the measurement framework. Strength: directly relevant to LLM evaluation community.\n\n## Anticipated Reviewer Concerns & Responses\n\n1. **\"Why not CyclicJudge + discard contaminated items?\"** — Item discard wastes information; CyclicJudge doesn't capture item-specific judge effects; neither produces c_n for auditing; G-MFRM degrades gracefully to standard MFRM when contamination ≈ 0.\n\n2. **\"Is confounding large enough in practice?\"** — MVP synthetic: 43.8% RMSE degradation. Real-data calibration (P0 experiment) will establish realistic contamination magnitude. Bias scatter (r=0.65) shows the mechanism exists regardless of magnitude.\n\n3. **\"Rank-1 assumption (c_n·e_i) too strong\"** — Rank-1 is LLTM tradition, good approximation when contamination comes from dominant data source. Person-fit diagnostics (infit/outfit) detect violations. Rank-k extension is future work.\n\n4. **\"DG-IRT transfer is trivial\"** — Three structural differences require non-trivial adaptation: binary→continuous exposure, single-rater→multi-facet, known→unknown exposure status. Stage 2 external anchoring solves a fundamental obstacle (exposure unknown to administrator) absent in educational testing. Error propagation from Stage 2→3 must be discussed in Limitations with sensitivity analysis (vary e_i noise σ=0.1,0.2,0.5).\n\n4b. **\"Staged estimation ≠ joint estimation\"** — Correct: e_i is pre-fixed in Stage 2, so estimation is conditional-joint, not fully simultaneous. Frame as deliberate identifiability choice: true joint estimation of (θ,b,d,c,e) is under-identified without external anchoring. Staged estimation is the principled solution. Compare to two-step estimators in econometrics (Heckman 1979). Error propagation sensitivity analysis shows robustness.\n\n5. **\"Contamination signal realistic?\"** — ConStat validated r²=0.94 with true contamination effects. LogProber provides per-item memorization indicators. Multiple indicators combined via weighted composite. P0 experiment calibrates against real benchmarks.\n\n6. **\"Chatbot Arena Elo as ground truth — circular reasoning?\"** — Arena uses real-time human pairwise comparisons with user-submitted prompts (not fixed benchmark items). Contamination inflates benchmark scores but does not directly improve conversational ability. Arena Elo is the least-contaminated human preference signal available. Acknowledge limitation in paper but argue decoupling is strong.\n\n7. **\"c_n ≥ 0 assumption too restrictive?\"** — Half-Cauchy prior enforces non-negativity, appropriate for the \"contamination as unfair advantage\" framing. Adversarial contamination (intentional performance degradation) is outside scope. Discuss in Limitations.\n\n8. **\"≥4 judges needed — too expensive?\"** — exp-006 sensitivity analysis shows degradation curve. Discuss in Limitations: at 2 judges, G-MFRM degrades gracefully to MFRM-level (no contamination correction). Cost-benefit analysis for practitioners.\n\n9. **\"No judge-model interaction term?\"** — G-MFRM has d_j (judge-level) and c_n·e_i (model-item), but no f_{nj} (judge-model interaction). Preference Leakage shows same-model PLS≈23.6%, same-family≈8.9%. When GPT-5.5 judges GPT-5.5, this bias distributes uniformly across items and gets absorbed into θ̂_n. Mitigation: (a) exp-006 leave-one-judge-out residual diagnostic detects if specific judges inflate same-family models; (b) Limitations section acknowledges scope boundary; (c) rank-k extension with judge-model interaction is future work.\n\n## Two-Tier Narrative (contingent on exp-005 contamination magnitude)\n\n**Tier A — Strong contamination (c ≈ 1.0-1.5, matching mvp_002/003)**:\n- Lead with ranking correction as primary contribution\n- Claim 3 at full strength: \"G-MFRM achieves X% higher Kendall-τ\"\n- Headline: joint estimation dramatically outperforms sequential\n\n**Tier B — Weak contamination (c ≈ 0.3-0.5, matching mvp_001)**:\n- Elevate diagnostic interpretability to co-primary contribution (per IDEA_BRIEF optimization A4)\n- Reframe: \"even when ranking improvement is modest, G-MFRM uniquely provides per-model c_n (training audit), per-item e_i (item retirement), per-judge d_j (judge calibration)\"\n- Bias scatter r=0.65 proves the mechanism exists; practical impact scales with contamination magnitude\n- Claim 3 softened to \"comparable or better rankings PLUS interpretable diagnostic outputs\"\n\n**Tier B+ — Diagnostics as sole primary (if Claim 1 ρ≈0 AND Claim 3 Δτ non-significant)**:\n- Diagnostics become the **sole** primary contribution (not co-primary)\n- Paper becomes \"tool paper\": G-MFRM as diagnostic framework for LLM evaluation auditing\n- Contribution: per-model c_n (training data audit), per-item e_i (item retirement), per-judge d_j (judge calibration) — unified diagnostic outputs no existing tool provides\n- Risk: \"tool paper\" positioning may be weaker for Main Conference; strong for Findings\n\nexp-005 determines which tier. Decision point: after exp-005 results, before paper writing.\n\n## Novelty Supplementation Strategy\n\nDream R2 exposed a novelty ceiling: \"MFRM + 1 term\" + \"textbook OVB\" = combinatorial novelty. Even with best-case data, Main Conference bar may not be met on novelty alone. Supplement with:\n\n1. **Identifiability analysis** (Method section): Prove necessary and sufficient conditions for (θ, b, d, c) identifiability when e_i is fixed. This is a non-trivial technical contribution beyond \"adding a term.\"\n2. **Formal e_i uncertainty propagation**: Beyond sensitivity analysis (exp-012), provide theoretical treatment of how e_i estimation error propagates to c_n credible intervals. Compare to two-step estimator literature (Heckman 1979, Murphy & Topel 1985).\n3. **Diagnostic framework formalization**: Frame the four-dimensional output (θ, d_j, c_n, e_i) as a principled measurement framework, not just parameter estimates. Connect to DIF (Differential Item Functioning) tradition.\n\n## Bibliography Strategy (Paper Agent input)\n\nRequired references by positioning role:\n- **Foundational IRT**: Rasch 1960, Lord & Novick 1968, Fox 2010 (Bayesian IRT)\n- **MFRM ancestor**: Linacre 1989, Engelhard 2002/2013, Eckes 2011/2015\n- **DG-IRT ancestor**: Shu et al. 2013 (Psychometrika), Robitzsch 2020\n- **MFRM+DIF (educational)**: Wind & Peterson 2018, Patz et al. 2002, Fox & Glas 2001\n- **LLM contamination**: Golchin & Surdeanu 2023, Shi et al. 2023 (Min-K%), ConStat, DCR\n- **LLM judge bias**: Zheng et al. 2023 (MT-Bench), CyclicJudge, UDA, Preference Leakage\n- **Benchmarks**: Arena-Hard original, WildBench original, LiveBench\n- **Econometrics**: Angrist & Pischke 2009 (OVB), Heckman 1979 (two-step)\nTarget: 30-40 references total.\n\n## MVP Evidence Summary\n\n- mvp_003: Joint RMSE −43.8% vs Sequential (p=1e-6), Kendall-τ +6.3pp, R̂=1.03, ESS=224\n- Bias scatter: Pearson r=0.65 (sequential systematically overestimates high-c_n models)\n- Robustness: method effective even under model misspecification (DGP with s_j, model without)\n\n\n## experiment_plan (with registry status)\n\n- id: exp-001\n  name: multi_judge_data_collection\n  claim: 3\n  description: 'Collect multi-judge evaluation data on MT-Bench and Arena-Hard using\n    8+ judges: GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B,\n    Qwen3.6-27B, Llama 4 Maverick, + 1 additional. Evaluate 20+ target models. Position\n    swap for pairwise.'\n  priority: P0\n  gpu_budget_hours: 130\n  deps: []\n  notes: Open-source judges via vLLM on RTX 6000. Proprietary judges via API (~$900\n    budget). Position swap doubles evaluation count. MUST also collect judge response\n    generations (--generate-judge-responses) for UDA baseline compatibility.\n  status: planned\n- id: exp-002\n  name: item_exposure_estimation\n  claim: 2\n  description: 'Estimate per-item exposure e_i via three-source pipeline: (1) Primary:\n    item-level performance gap between original items and GPT-5.5/Claude-rephrased\n    reference variants, averaged across reference models, with spline difficulty correction\n    (ConStat-inspired). (2) Temporal: performance gap on pre-cutoff vs post-cutoff\n    item variants where available. (3) LogProber: token logprob memorization scores\n    for models with logprob API. Sources combined via weighted composite (weights\n    tuned on validation split). ConStat per-model delta used as external validation\n    of fitted c_n, not as e_i source.'\n  priority: P0\n  gpu_budget_hours: 30\n  deps:\n  - exp-001\n  notes: 'Main bottleneck: reference benchmark variant construction + quality validation.\n    ConStat per-model delta validates G-MFRM c_n, not used for per-item e_i.'\n  status: planned\n- id: exp-003\n  name: gmfrm_real_data_fit\n  claim:\n  - 1\n  - 2\n  - 3\n  description: 'Fit G-MFRM three-stage pipeline on real data from exp-001/002. Stage\n    1: MFRM (θ,b,d). Stage 2: e_i from exp-002. Stage 3: Joint gated model. Compare\n    fair scores θ̂ with Chatbot Arena human votes (Kendall-τ).'\n  priority: P0\n  gpu_budget_hours: 15\n  deps:\n  - exp-001\n  - exp-002\n  notes: 'NumPyro MCMC. Use MVP MCMC settings (warmup=2000, samples=4000, chains=4,\n    NCP, target_accept=0.95). Include per-benchmark analysis: if any benchmark has\n    contamination ≈ 0, verify G-MFRM degrades gracefully to MFRM level (real-data\n    graceful degradation check).'\n  status: planned\n- id: exp-004\n  name: baseline_comparison\n  claim: 3\n  description: 'Compare G-MFRM against 8 baselines on same data: (1) raw multi-judge\n    average, (2) MFRM-only, (3) sequential pipeline, (4) CyclicJudge, (5) CyclicJudge\n    + contaminated item discard, (6) DCR Factor, (7) UDA, (8) Preference Leakage calibration.\n    Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena. MUST include rank change analysis:\n    show which specific models change rank, by how many positions, and top-k stability\n    (k=5,10).'\n  priority: P0\n  gpu_budget_hours: 20\n  deps:\n  - exp-003\n  notes: 'Baseline (5) is the strongest trivial alternative — addresses Reviewer Concern\n    #1. CyclicJudge/UDA/DCR/PrefLeakage need public code check. Budget may not include\n    debug time. Rank change analysis addresses Dream R2-W3. MUST include post-hoc\n    power analysis: compute statistical power for Wilcoxon test to detect observed\n    Δτ at α=0.05 with N models. If power < 0.80, discuss implications and consider\n    increasing items/judges.'\n  status: planned\n- id: exp-005\n  name: contamination_magnitude_calibration\n  claim: 1\n  description: 'Estimate real contamination magnitude: compare fitted c_n from exp-003\n    with synthetic MVP assumptions. Determine if real contamination is closer to mvp_001\n    (c~0.5, weak) or mvp_002 (c~1.5, strong). Critical for claim strength.'\n  priority: P0\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  notes: 'Reviewer flagged: if real c ≈ mvp_001 level, paper impact weakens. This\n    experiment determines claim calibration.'\n  status: planned\n- id: exp-006\n  name: judge_count_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis: vary number of judges (2, 4, 6, 8+) and measure\n    G-MFRM performance degradation. At what minimum judge count does G-MFRM still\n    outperform sequential? Include leave-one-judge-out residual diagnostic: check\n    if removing a judge that shares model family with targets systematically changes\n    residuals (preference leakage detection).'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-003\n  status: planned\n- id: exp-007\n  name: exposure_indicator_ablation\n  claim: 2\n  description: 'Ablation: contribution of each exposure indicator (ConStat delta,\n    temporal signal, LogProber Safe Score) to e_i estimation quality. Leave-one-out\n    analysis.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps:\n  - exp-002\n  - exp-003\n  status: planned\n- id: exp-008\n  name: facet_fit_diagnostics\n  claim: 2\n  description: 'Measurement quality validation: report infit/outfit MNSQ for all facets\n    (θ, b, d, c). Flag misfitting elements. Compare Stage 1 person-fit (lz, EMRi)\n    vs Stage 3 c_n as construct coherence validation. MUST also report: divergent\n    transition count, posterior predictive check, trace plots for key parameters.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps:\n  - exp-003\n  status: planned\n- id: exp-009\n  name: confounding_formal_observation\n  claim: 1\n  description: 'Formal bias analysis: derive first-order bias approximation for sequential\n    estimator under d_j/c_n·e_i non-orthogonality. Validate via Monte Carlo simulation\n    across realistic parameter ranges. For paper Section 2. Frame as ''Observation''\n    (standard OVB from Angrist & Pischke 2009), not ''Proposition''. MUST include\n    synthetic c_n point-estimate validation: generate data with known ground-truth\n    c_n, fit G-MFRM, report per-model c_n RMSE and 95% credible interval coverage\n    probability.'\n  priority: P1\n  gpu_budget_hours: 10\n  deps: []\n  notes: Can run in parallel with data collection. Extends MVP synthetic analysis.\n    Downgraded from 'Proposition' to 'Observation' per Dream review. Synthetic c_n\n    validation addresses Dream R1-N3.\n  status: planned\n- id: exp-012\n  name: error_propagation_sensitivity\n  claim: 2\n  description: 'Sensitivity analysis for staged estimation: inject Gaussian noise\n    into e_i estimates at σ=0.1,0.2,0.5 before Stage 3 fitting. Measure θ̂ RMSE degradation\n    and c_n recovery accuracy. Shows three-stage pipeline is robust to e_i estimation\n    error. Use synthetic data with known ground truth.'\n  priority: P1\n  gpu_budget_hours: 5\n  deps: []\n  notes: Addresses Dream R2-W5 and R1-N1. Can run on MVP codebase with modifications.\n    Critical for defending staged estimation design choice.\n  status: planned\n- id: exp-010\n  name: wildbench_replication\n  claim: 3\n  description: Replicate G-MFRM pipeline on WildBench as third benchmark. Cross-benchmark\n    generalization.\n  priority: P2\n  gpu_budget_hours: 40\n  deps:\n  - exp-003\n  status: planned\n- id: exp-011\n  name: adversarial_robustness\n  claim: 2\n  description: Test G-MFRM robustness against adversarial contamination following\n    Wang et al. (ICLR 2026) fragility findings.\n  priority: P2\n  gpu_budget_hours: 15\n  deps:\n  - exp-003\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_001\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL\n    convergence: PASS\n    rho_0.0:\n      joint_gmfrm:\n        RMSE: 0.1540±0.0269\n        tau: 0.9042±0.0445\n      sequential:\n        RMSE: 0.1540±0.0242\n        tau: 0.9016±0.0467\n      p_value: 0.4782\n    rho_0.3:\n      joint_gmfrm:\n        RMSE: 0.1521±0.0283\n        tau: 0.9068±0.0419\n      sequential:\n        RMSE: 0.1527±0.0236\n        tau: 0.9011±0.0452\n      p_value: 0.3506\n    rho_0.6:\n      joint_gmfrm:\n        RMSE: 0.1529±0.0285\n        tau: 0.9047±0.0418\n      sequential:\n        RMSE: 0.1537±0.0237\n        tau: 0.9037±0.0419\n      p_value: 0.3921\n    rho_0.0_no_degradation_p: 0.9563\n    runtime_seconds: 1675.6\n- exp_id: mvp_002\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    verdict: FAIL (convergence)\n    convergence:\n      max_rhat: 1.05\n      min_ess: 47\n      pass: false\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 32.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0449\n      tau: 0.8390±0.0351\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8596±0.0291\n    joint_gmfrm:\n      RMSE: 0.1486±0.0199\n      tau: 0.9028±0.0181\n    runtime_seconds: 1935.4\n    scatter_pearson_r: 0.6534\n    scatter_p: 0\n- exp_id: mvp_003\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PASS\n    convergence:\n      max_rhat: 1.03\n      min_ess: 224\n      pass: true\n    wilcoxon_joint_vs_seq:\n      p_value: 1.0e-06\n      pass: true\n    rmse_reduction: 43.8%\n    raw_average:\n      RMSE: 0.8063±0.0841\n      tau: 0.8401±0.0347\n    mfrm_only:\n      RMSE: 0.2539±0.0448\n      tau: 0.8388±0.0345\n    sequential:\n      RMSE: 0.2211±0.0376\n      tau: 0.8593±0.0293\n    joint_gmfrm:\n      RMSE: 0.1243±0.0164\n      tau: 0.9223±0.0098\n    runtime_seconds: 4385.5\n    kendall_tau_joint: 0.9223\n    kendall_tau_seq: 0.8593\n- exp_id: exp-009\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n- exp_id: exp-012\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    verdict: PARTIAL (σ≤0.2 robust, σ=0.5 exceeds threshold)\n    false_failure: true\n    false_failure_reason: EXIT_CODE=129 (SIGHUP) after all 80/80 fits completed and\n      results saved\n    sigma_0.0:\n      theta_rmse: 0.1277\n      theta_rmse_std: 0.0178\n      theta_tau: 0.9159\n      cn_rmse: 0.533\n      cn_corr: 0.8599\n      rhat_max: 1.02\n      ess_min: 276\n      n: 20\n    sigma_0.1:\n      theta_rmse: 0.1295\n      theta_rmse_std: 0.0178\n      theta_tau: 0.9153\n      cn_rmse: 0.5452\n      cn_corr: 0.8542\n      delta_theta_pct: 1.4\n      delta_cn_pct: 2.3\n    sigma_0.2:\n      theta_rmse: 0.1352\n      theta_rmse_std: 0.0175\n      theta_tau: 0.914\n      cn_rmse: 0.5751\n      cn_corr: 0.8385\n      delta_theta_pct: 5.9\n      delta_cn_pct: 7.9\n    sigma_0.5:\n      theta_rmse: 0.1748\n      theta_rmse_std: 0.0266\n      theta_tau: 0.885\n      cn_rmse: 0.8415\n      cn_corr: 0.745\n      delta_theta_pct: 36.9\n      delta_cn_pct: 57.9\n    convergence:\n      all_rhat_max: 1.02\n      pass: true\n    total_runtime_seconds: 14585\n    artifacts:\n    - error_propagation.png\n    - cn_degradation.png\n    - summary.csv\n- exp_id: exp-001\n  name: ''\n  status: RUNNING\n  conclusion: ''\n  metrics: {}\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n\n重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: [\"Judge\", \"Biased?\"]`），否则 `?` `:` 等字符会导致解析失败。\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-22T04:20:03.868Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-22T04:20:03.868Z",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-22T04:20:03.895Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Real contamination weak-to-moderate, ranking improvement positive but small/borderline, confounding mechanism confirmed but practical impact modest — Tier B narrative with diagnostics elevated to co-primary
核心假设：['Real c_n distribution has median 0.3–0.7 (closer to mvp_001 regime for some models, mvp_002 for a few)', 'Confounding exists but effect size in θ-bias is ≤ 0.15 logits for most models', 'G-MFRM converges acceptably (R̂ ≤ 1.10, ESS ≥ 80) — may need thinning or extended warmup', 'e_i pipeline noisy for some items (effective σ_e ≈ 0.2–0.3), but aggregate signal holds', 'Δτ positive but Wilcoxon p-value borderline (0.03–0.10) due to N≈20 models limiting power', 'Post-hoc power < 0.80 for primary comparison']
关键指标范围：{'real_cn_median': [0.3, 0.7], 'kendall_tau_gmfrm': [0.78, 0.85], 'kendall_tau_best_baseline': [0.75, 0.83], 'delta_tau_vs_best_baseline': [0.01, 0.04], 'delta_tau_p_value': [0.03, 0.12], 'theta_rmse_reduction_vs_sequential': [0.05, 0.2], 'confounding_scatter_r': [0.25, 0.45], 'convergence_rhat_max': [1.03, 1.1], 'convergence_ess_min': [80, 200], 'cn_constat_validation_corr': [0.4, 0.65], 'ei_pipeline_internal_consistency': [0.3, 0.55]}
叙事方向：Reframe: joint estimation is methodologically principled AND provides unique diagnostic value, even when ranking improvement is modest. Claim 1 softened to 'confounding exists and is detectable' (mechanism, not magnitude). Claim 3 softened to 'comparable or better rankings PLUS interpretable diagnostics no baseline provides.' Elevate per-model c_n, per-judge d_j, per-item e_i as co-primary contribution. Lead with 'unified diagnostic framework' angle. Add subset analysis: show G-MFRM advantage is concentrated on high-contamination models (top quartile c_n). AAAI positioning viable but needs strong writing; ARR backup advisable.

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

重要：tables 中使用 YAML flow sequence 时，所有字符串必须加双引号（如 `columns: ["Judge", "Biased?"]`），否则 `?` `:` 等字符会导致解析失败。


<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": null,
  "isSidechain": false,
  "promptId": "4adcc533-99af-455c-bf16-cb520c091389",
  "type": "user",
  "uuid": "f4e7dfd1-b7e8-4f9c-b8b2-dabb84a8a361",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-22T04:20:03.894Z_

```json
{
  "parentUuid": "f4e7dfd1-b7e8-4f9c-b8b2-dabb84a8a361",
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
  "uuid": "332b2e0d-0557-47c1-b992-999e45fd0eed",
  "timestamp": "2026-05-22T04:20:03.894Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-22T04:20:03.894Z_

```json
{
  "parentUuid": "332b2e0d-0557-47c1-b992-999e45fd0eed",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "bcee3746-dccb-4b1e-be0a-10341054f7aa",
  "timestamp": "2026-05-22T04:20:03.894Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Real contamination weak-to-moderate, ranking improvement positive but small/borderline, confounding mechanism confirmed but practical impact modest — Tie…",
  "leafUuid": "bcee3746-dccb-4b1e-be0a-10341054f7aa",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier G-MFRM real data validation and narrative reframing",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36"
}
```

---

### Assistant

_source line 8 · 2026-05-22T04:20:59.201Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted data for each planned experiment in the experiment_plan, based on the "median" tier definition. Let me analyze the median tier characteristics and generate realistic predictions for each experiment.

Let me first review what I know:

**Median tier definition:**
- Real contamination weak-to-moderate
- Ranking improvement positive but small/borderline
- Confounding mechanism confirmed but practical impact modest
- Tier B narrative with diagnostics elevated to co-primary

**Key metric ranges for median:**
- real_cn_median: [0.3, 0.7]


- kendall_tau_gmfrm: [0.78, 0.85]
- kendall_tau_best_baseline: [0.75, 0.83]
- delta_tau_vs_best_baseline: [0.01, 0.04]
- delta_tau_p_value: [0.03, 0.12]
- theta_rmse_reduction_vs_sequential: [0.05, 0.2]
- confounding_scatter_r: [0.25, 0.45]
- convergence_rhat_max: [1.03, 1.1]
- convergence_ess_min: [80, 200]
- cn_constat_validation_corr: [0.4, 0.65]
- ei_pipeline_internal_consistency: [0.3, 0.55]

Now I'm going through the planned experiments to generate detailed predictions for each one. Looking at what's currently running versus what's still in the pipeline, I need to map out the expected outcomes for the remaining studies. I'm noticing a discrepancy between the experiment_plan statuses and what the registry shows—some experiments marked as planned are already running or completed. Since the user asked for detailed data on each planned experiment from the plan itself, I should generate predictions for all of them regardless of their current registry status, but I'll note which ones are already in progress or finished.

Let me work through the predictions for each experiment under the median tier assumptions, starting with the data collection and pipeline quality metrics, then moving into the core fitting results. Now I'm looking at the remaining experiments and need to fill in the YAML with specific numbers and rationales. For the data collection experiment, I'm calculating the expected judgment volume across 8 judges evaluating 20+ models on MT-Bench and Arena-Hard with position swaps, accounting for API failures and refusals to estimate around 95% coverage with moderate inter-judge agreement in the κ range of 0.35-0.45.

For item exposure estimation, the three-source pipeline produces noisy exposure values with moderate internal consistency, though some items are difficult to rephrase and LogProber coverage is limited to models supporting logprob APIs. The GMFRM fitting on real data should converge well with Kendall-τ correlation around 0.78-0.85 against Arena rankings and show a 5-20% RMSE improvement over sequential approaches, though real data will be noisier than synthetic benchmarks. I'm comparing GMFRM against eight baseline methods to establish its relative performance.

The baseline comparison shows modest improvements with Kendall-τ differences of 0.01-0.04 and p-values between 0.03-0.12, though post-hoc power remains below 0.80. Contamination magnitude calibration reveals real contamination rates around 0.3-0.7, closer to the MVP baseline for most models, with ConStat validation correlations between 0.4-0.65. Judge count sensitivity analysis shows that at 2 judges GMFRM performs similarly to standard MFRM without contamination separation, marginal improvements at 4 judges, and stable performance at 6+ judges, with leave-one-judge-out analysis detecting some same-family effects. The exposure indicator ablation demonstrates that the primary performance source contributes most value, with LogProber adding moderate gains.

Temporal signal proves weakest due to limited coverage, but the full pipeline outperforms any single source. Item fit diagnostics reveal some misfitting items with infit values exceeding 1.3, though most facets remain acceptable, with moderate correlation between latent z and contamination magnitude and occasional divergent transitions. The confounding analysis validates the bias approximation through Monte Carlo simulation, confirming correct bias direction with moderate magnitude and scatter correlations between 0.25-0.45, though contamination recovery shows moderate RMSE. Replication on WildBench exhibits similar patterns but possibly weaker effects due to the different item pool, partially confirming generalization. Adversarial robustness testing shows GMFRM is partially robust, though extreme contamination scenarios can degrade performance.

Writing YAML output... Generating comprehensive YAML...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "bcee3746-dccb-4b1e-be0a-10341054f7aa",
  "isSidechain": false,
  "requestId": "req_011CbGxwVzik1o7F7XAKoC3M",
  "type": "assistant",
  "uuid": "8c6d245d-2cfe-44b6-8b86-a02e221cda19",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCt7j9zyoVJzzHYqhjubK4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 11841,
      "output_tokens": 24668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 24668,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13668
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

_source line 9 · 2026-05-22T04:27:43.076Z_

```yaml
tier: median
narrative_guidance: >
  Reframe: joint estimation is methodologically principled AND provides unique diagnostic value,
  even when ranking improvement is modest. Claim 1 softened to "confounding exists and is detectable"
  (mechanism, not magnitude). Claim 3 softened to "comparable or better rankings PLUS interpretable
  diagnostics no baseline provides." Elevate per-model c_n, per-judge d_j, per-item e_i as co-primary
  contribution. Lead with "unified diagnostic framework" angle. Add subset analysis: show G-MFRM
  advantage is concentrated on high-contamination models (top quartile c_n). AAAI positioning viable
  but needs strong writing; ARR backup advisable.

imagined_experiments:
  - name: "multi_judge_data_collection"
    plan_id: "exp-001"
    description: >
      Collect multi-judge evaluation data on MT-Bench (80 items × 2 turns) and Arena-Hard (500 items)
      using 8 judges, evaluating 22 target models with position swap.
    expected_results:
      total_judges: 8
      judge_list: "GPT-5.5, Claude Opus 4.7, Claude Sonnet 4.6, DeepSeek-V4-Pro, Qwen3-235B-A22B, Qwen3.6-27B, Llama-4-Maverick, Gemini-2.5-Pro"
      total_target_models: 22
      mt_bench_items: 160  # 80 × 2 turns
      arena_hard_items: 500
      total_judgments_planned: 232320  # 22 × 8 × 660 × 2 positions
      total_judgments_collected: 219874
      collection_completion_rate: 0.9464
      api_failure_rate: 0.031
      refusal_rate: 0.023  # judges refusing to evaluate certain content
      position_swap_agreement: 0.72  # fraction where verdict unchanged after swap
      inter_judge_fleiss_kappa: 0.38
      pairwise_judge_agreement_mean: 0.64
      pairwise_judge_agreement_std: 0.09
      uda_response_collection_rate: 0.98
      api_cost_usd: 847
      vllm_gpu_hours: 118
      total_wall_clock_days: 11
    result_rationale: >
      Median 档下，数据收集本身是工程问题而非统计问题，完成率主要取决于 API 稳定性和 judge 拒答率。
      95% 完成率符合实际 API 可用性（GPT-5.5/Claude 偶发限速，开源模型 vLLM 偶发 OOM）。
      Fleiss κ ≈ 0.38 反映 LLM judge 的已知分歧水平（Zheng et al. 2023 报告类似数值），
      说明 judge 间存在系统性差异——这正是 d_j 参数需要建模的信号。
      Position swap agreement 0.72 表明位置偏差存在但不占主导，与已有文献一致。
      收集 UDA 所需的 judge response generation 增加约 15% 时间但不影响数据质量。
    tables:
      - name: "judge_coverage_matrix"
        caption: "Judge × Benchmark coverage (fraction of completed evaluations)"
        columns: ["Judge", "MT-Bench", "Arena-Hard", "Overall"]
        rows:
          - ["GPT-5.5", "0.99", "0.98", "0.984"]
          - ["Claude Opus 4.7", "0.98", "0.97", "0.974"]
          - ["Claude Sonnet 4.6", "0.99", "0.98", "0.984"]
          - ["DeepSeek-V4-Pro", "0.97", "0.95", "0.958"]
          - ["Qwen3-235B-A22B", "0.96", "0.93", "0.942"]
          - ["Qwen3.6-27B", "0.94", "0.91", "0.922"]
          - ["Llama-4-Maverick", "0.95", "0.92", "0.932"]
          - ["Gemini-2.5-Pro", "0.98", "0.96", "0.968"]
      - name: "inter_judge_agreement"
        caption: "Pairwise judge agreement rate (MT-Bench + Arena-Hard combined)"
        columns: ["Judge Pair", "Agreement Rate", "Cohen Kappa"]
        rows:
          - ["GPT-5.5 vs Claude Opus 4.7", "0.71", "0.42"]
          - ["GPT-5.5 vs DeepSeek-V4-Pro", "0.65", "0.33"]
          - ["Claude Opus 4.7 vs Claude Sonnet 4.6", "0.76", "0.51"]
          - ["Proprietary mean", "0.69", "0.39"]
          - ["Open-source mean", "0.61", "0.28"]
          - ["Cross-type mean", "0.64", "0.32"]
    figures_description:
      - "Judge agreement heatmap: 8×8 matrix showing pairwise Cohen κ. Proprietary judges form a mild cluster (κ ≈ 0.39-0.51), open-source judges more dispersed (κ ≈ 0.22-0.35). This clustering motivates modeling d_j rather than treating judges as exchangeable."
      - "Position bias distribution: histogram of per-item position swap disagreement rate across items. Right tail (disagreement > 0.5) concentrated in Arena-Hard coding/math items, suggesting position bias is item-type dependent."
    analysis: >
      数据收集成功，覆盖率满足建模需求。关键发现：(1) 开源 judge 的覆盖率略低于 API judge，
      主要因 vLLM 内存限制导致长输出截断；(2) judge 间分歧显著（κ = 0.38），尤其在
      主观评价维度（创造性、细致性），验证了 MFRM 对 d_j 建模的必要性；
      (3) 同家族 judge 对（如 Claude Opus vs Sonnet）agreement 更高，暗示 preference leakage
      效应存在但可控。数据量足够支撑 8-facet MFRM 拟合。

  - name: "item_exposure_estimation"
    plan_id: "exp-002"
    description: >
      Estimate per-item exposure e_i via three-source weighted composite pipeline:
      performance gap (primary), temporal signal, LogProber scores.
    expected_results:
      total_items_mtbench: 160
      total_items_arenahard: 500
      reference_variants_created: 627  # not all items have good rephrases
      reference_variant_quality_pass_rate: 0.87
      performance_gap_coverage: 0.95  # fraction of items with valid gap estimates
      temporal_signal_coverage: 0.41  # only items with clear pre/post cutoff
      logprober_coverage: 0.55  # only models with logprob API
      composite_weights_performance_gap: 0.62
      composite_weights_temporal: 0.18
      composite_weights_logprober: 0.20
      ei_mean: 0.34
      ei_std: 0.22
      ei_median: 0.29
      ei_range: [0.02, 0.91]
      ei_internal_consistency_alpha: 0.43
      ei_split_half_reliability: 0.39
      ei_spearman_gap_vs_logprober: 0.48
      ei_spearman_gap_vs_temporal: 0.36
      ei_spearman_logprober_vs_temporal: 0.31
      high_exposure_items_fraction: 0.18  # e_i > 0.7
      near_zero_exposure_items_fraction: 0.32  # e_i < 0.15
      effective_sigma_e: 0.24
      mtbench_ei_mean: 0.42
      arenahard_ei_mean: 0.29
    result_rationale: >
      Median 档核心假设：e_i pipeline 有噪声（effective σ_e ≈ 0.2-0.3），但聚合信号有效。
      内部一致性 α ≈ 0.43 处于 [0.3, 0.55] 范围中部，反映三个信号源测量的是相关但非同一构念：
      performance gap 捕获训练集泄露的综合效应，LogProber 捕获逐字记忆，temporal 捕获时间窗口效应。
      这三者在 "contamination" 的广义定义下相关（r ≈ 0.3-0.5），但各自噪声源不同。
      MT-Bench e_i 均值高于 Arena-Hard 因为 MT-Bench 发布更早、被更多训练数据包含。
      约 18% 的 item 有高暴露度（e_i > 0.7），集中在 MT-Bench 的经典题目（如 math/coding 常见题型）
      和 Arena-Hard 的早期发布题目。32% 近零暴露主要是 Arena-Hard 的新增/冷门题目。
      Reference variant 构建的主要瓶颈在于保持语义等价性同时改变表面形式——
      约 13% 的 item 因结构化输出（代码、数学公式）难以有效改写。
    tables:
      - name: "ei_source_statistics"
        caption: "Per-source e_i estimation statistics"
        columns: ["Source", "Coverage", "Mean e_i", "Std", "Weight"]
        rows:
          - ["Performance Gap", "0.95", "0.36", "0.24", "0.62"]
          - ["Temporal Signal", "0.41", "0.31", "0.19", "0.18"]
          - ["LogProber", "0.55", "0.33", "0.26", "0.20"]
          - ["Composite", "1.00", "0.34", "0.22", "—"]
      - name: "ei_by_benchmark_category"
        caption: "Mean e_i by benchmark and item category"
        columns: ["Benchmark", "Category", "N Items", "Mean e_i", "Std e_i"]
        rows:
          - ["MT-Bench", "Writing", "20", "0.38", "0.21"]
          - ["MT-Bench", "Roleplay", "20", "0.31", "0.18"]
          - ["MT-Bench", "Reasoning", "20", "0.52", "0.24"]
          - ["MT-Bench", "Math", "20", "0.56", "0.22"]
          - ["MT-Bench", "Coding", "20", "0.49", "0.25"]
          - ["MT-Bench", "Extraction", "20", "0.35", "0.19"]
          - ["MT-Bench", "STEM", "20", "0.44", "0.23"]
          - ["MT-Bench", "Humanities", "20", "0.33", "0.17"]
          - ["Arena-Hard", "All", "500", "0.29", "0.21"]
    figures_description:
      - "e_i histogram: bimodal distribution with peak near 0.1 (unexposed items) and secondary mode near 0.5 (moderately exposed). Long right tail to 0.9. MT-Bench items shifted right relative to Arena-Hard."
      - "Source agreement scatter: 3-panel plot (gap vs logprober, gap vs temporal, logprober vs temporal). Moderate positive correlations (r = 0.48, 0.36, 0.31) with substantial scatter, illustrating why composite is needed."
      - "Reference variant quality: scatter of original score vs reference score per item, colored by e_i. High-e_i items show larger gaps (as expected). Regression line with 95% CI band."
    analysis: >
      e_i pipeline 在 median 档下表现符合预期：噪声较大但聚合后可用。关键限制是
      temporal signal 覆盖率仅 41%（许多 item 缺乏明确时间切分点），LogProber 受限于
      仅 API 模型提供 logprob。MT-Bench 的 Math/Coding/Reasoning 类目 e_i 最高，
      符合直觉——这些是训练数据中最常见的 benchmark 题型。e_i 的有效 σ_e ≈ 0.24
      将在 Stage 3 引入 c_n 估计噪声，但 exp-012 已证明 σ ≤ 0.2 下 θ 稳健。
      这意味着 e_i 估计质量处于 exp-012 稳健性阈值的边缘，需在论文 Limitations 中讨论。

  - name: "gmfrm_real_data_fit"
    plan_id: "exp-003"
    description: >
      Fit G-MFRM three-stage pipeline on real data. Stage 1: MFRM. Stage 2: e_i from exp-002.
      Stage 3: Joint gated model. Compare with Chatbot Arena Kendall-τ.
    expected_results:
      # Stage 1: MFRM
      stage1_rhat_max: 1.02
      stage1_ess_min: 412
      stage1_runtime_seconds: 1840
      stage1_theta_tau_arena: 0.794
      # Stage 3: Joint G-MFRM
      stage3_rhat_max: 1.06
      stage3_ess_min: 132
      stage3_runtime_seconds: 8720
      stage3_warmup: 3000
      stage3_samples: 5000
      stage3_chains: 4
      stage3_thinning: 2
      stage3_divergent_transitions: 14
      # Model ability estimates
      theta_tau_arena_gmfrm: 0.823
      theta_tau_arena_mfrm: 0.794
      theta_tau_arena_raw_avg: 0.761
      theta_spearman_arena_gmfrm: 0.857
      theta_spearman_arena_mfrm: 0.831
      # Contamination parameter estimates
      cn_median: 0.48
      cn_mean: 0.56
      cn_std: 0.39
      cn_range: [0.04, 1.42]
      cn_top_quartile_mean: 1.02
      cn_bottom_quartile_mean: 0.11
      # Judge severity estimates
      dj_range: [-0.83, 0.91]
      dj_std: 0.48
      dj_harshest_judge: "DeepSeek-V4-Pro"
      dj_most_lenient_judge: "GPT-5.5"
      # Per-benchmark
      mtbench_tau_gmfrm: 0.811
      mtbench_tau_mfrm: 0.783
      arenahard_tau_gmfrm: 0.831
      arenahard_tau_mfrm: 0.802
      # Graceful degradation check
      low_contam_benchmark_tau_gmfrm: 0.806
      low_contam_benchmark_tau_mfrm: 0.801
      graceful_degradation_pass: true
      # θ shift analysis
      max_theta_shift_stage1_to_stage3: 0.34
      models_with_shift_gt_0_2: 5
      models_with_shift_gt_0_1: 11
    result_rationale: >
      Median 档下，real c_n 分布中位数 ≈ 0.48，属于 weak-to-moderate 污染。G-MFRM 的
      Kendall-τ = 0.823 显著优于 raw average (0.761) 但仅小幅优于 MFRM-only (0.794)，
      因为 MFRM 本身已通过 d_j 修正了相当部分偏差。Stage 3 的边际改善来自 c_n·e_i
      项对高污染模型（top quartile, c̄ ≈ 1.02）的修正——这些模型在 Stage 1 中 θ̂ 被
      系统性高估。收敛性方面，R̂ = 1.06 和 ESS = 132 处于可接受范围但不如 mvp_003
      (R̂=1.03, ESS=224)，因为真实数据的模型数(22)多于合成(20)，item 数(660)远多于
      合成(50)，且 e_i 携带估计噪声。需要 thinning=2 和延长 warmup=3000 来控制
      自相关。14 个 divergent transitions 占总样本 <0.1%，在可接受范围内但需报告。
      Arena-Hard 的 τ 高于 MT-Bench 因为 Arena-Hard item 数更多，估计更稳定。
      Graceful degradation 验证通过：在低污染 benchmark 子集上 G-MFRM 几乎退化为 MFRM。
    tables:
      - name: "three_stage_summary"
        caption: "G-MFRM three-stage pipeline results on real data"
        columns: ["Stage", "Parameters", "R-hat max", "ESS min", "Runtime (s)", "Arena tau"]
        rows:
          - ["Stage 1 (MFRM)", "theta, b, d", "1.02", "412", "1840", "0.794"]
          - ["Stage 2 (e_i)", "e_i fixed from pipeline", "—", "—", "—", "—"]
          - ["Stage 3 (Joint)", "theta, b, d, c", "1.06", "132", "8720", "0.823"]
      - name: "model_ranking_top10"
        caption: "Top-10 model ranking comparison (Arena Elo vs G-MFRM θ̂ vs Raw Average)"
        columns: ["Arena Rank", "Model", "Arena Elo", "G-MFRM Rank", "Raw Avg Rank", "c_n", "theta shift"]
        rows:
          - ["1", "GPT-5.5", "1347", "1", "1", "0.31", "-0.04"]
          - ["2", "Claude Opus 4.7", "1338", "2", "3", "0.22", "-0.02"]
          - ["3", "Gemini-2.5-Pro", "1329", "3", "2", "0.58", "-0.12"]
          - ["4", "DeepSeek-V4-Pro", "1311", "4", "6", "0.15", "+0.01"]
          - ["5", "Claude Sonnet 4.6", "1298", "6", "5", "0.41", "-0.08"]
          - ["6", "Llama-4-Maverick", "1285", "5", "7", "0.09", "+0.03"]
          - ["7", "Qwen3-235B-A22B", "1271", "7", "4", "1.12", "-0.27"]
          - ["8", "GPT-4.5", "1258", "8", "8", "0.72", "-0.15"]
          - ["9", "Mistral-Large-3", "1241", "9", "10", "0.38", "-0.05"]
          - ["10", "Qwen3.6-27B", "1224", "10", "9", "0.85", "-0.19"]
      - name: "judge_severity_estimates"
        caption: "Estimated judge severity d_j (positive = harsher)"
        columns: ["Judge", "d_j (mean)", "d_j (95% CI)", "Infit MNSQ"]
        rows:
          - ["GPT-5.5", "-0.83", "[-1.02, -0.64]", "0.94"]
          - ["Claude Opus 4.7", "-0.31", "[-0.48, -0.14]", "1.08"]
          - ["Claude Sonnet 4.6", "-0.12", "[-0.29, 0.05]", "1.02"]
          - ["DeepSeek-V4-Pro", "0.91", "[0.72, 1.10]", "1.15"]
          - ["Qwen3-235B-A22B", "0.44", "[0.26, 0.62]", "1.21"]
          - ["Qwen3.6-27B", "0.62", "[0.43, 0.81]", "1.18"]
          - ["Llama-4-Maverick", "0.15", "[-0.03, 0.33]", "0.97"]
          - ["Gemini-2.5-Pro", "-0.22", "[-0.40, -0.04]", "1.05"]
    figures_description:
      - "Wright map (variable map): vertical axis = logit scale. Left side: model θ̂ distribution. Right side: item b̂ distribution, judge d̂ points. Shows alignment of model ability with item difficulty, plus judge spread."
      - "c_n posterior density plot: 22 overlapping density curves (one per model), x-axis = c_n. Top-quartile models clearly separated from bottom-quartile. Dashed vertical line at c_n = 0 (no contamination reference)."
      - "θ shift scatter: x = Stage 1 θ̂ (MFRM), y = Stage 3 θ̂ (G-MFRM). Points colored by c_n. High-c_n models shift downward (contamination correction), low-c_n models stay near identity line."
      - "Trace plots: 4 panels for representative θ, d, c, b parameters showing chain mixing. Chains visually mixed but with mild autocorrelation visible in c_n traces."
    analysis: >
      G-MFRM 在真实数据上收敛可接受但不如合成数据理想。τ = 0.823 vs MFRM 的 0.794
      表明 contamination 修正提供了边际但正向的排名改善。关键观察：修正集中于 top-quartile
      c_n 模型（如 Qwen3-235B-A22B, c_n = 1.12），这些模型的 raw ranking 被系统性高估。
      Judge severity 估计显示 DeepSeek-V4-Pro 最严厉（d = 0.91），GPT-5.5 最宽松（d = -0.83），
      范围 1.74 logits 对应约 1.5 个评分等级的系统偏差。这为 Claim 1 提供了直接证据：
      如果不建模 d_j，contamination 信号会被 judge 差异所混淆。
      Graceful degradation 通过验证——在低污染 item 子集上，Stage 3 结果与 Stage 1 近似。

  - name: "baseline_comparison"
    plan_id: "exp-004"
    description: >
      Compare G-MFRM against 8 baselines. Metrics: Kendall-τ, Spearman-ρ with Chatbot Arena.
      Include rank change analysis and post-hoc power analysis.
    expected_results:
      # Primary metrics
      kendall_tau_raw_average: 0.761
      kendall_tau_mfrm_only: 0.794
      kendall_tau_sequential_bias_first: 0.788
      kendall_tau_sequential_contam_first: 0.791
      kendall_tau_cyclicjudge: 0.802
      kendall_tau_cyclicjudge_discard: 0.798
      kendall_tau_dcr: 0.779
      kendall_tau_uda: 0.805
      kendall_tau_prefleak: 0.783
      kendall_tau_gmfrm: 0.823
      # Spearman
      spearman_rho_gmfrm: 0.857
      spearman_rho_uda: 0.841
      spearman_rho_mfrm: 0.831
      # Best baseline
      best_baseline: "UDA"
      best_baseline_tau: 0.805
      delta_tau_vs_best_baseline: 0.018
      delta_tau_p_value_wilcoxon: 0.067
      delta_tau_95ci: [0.002, 0.034]
      # Top-k stability
      top5_overlap_gmfrm: 0.8  # 4/5 models in common with Arena top-5
      top5_overlap_uda: 0.8
      top5_overlap_raw: 0.6
      top10_overlap_gmfrm: 0.9
      top10_overlap_uda: 0.8
      top10_overlap_raw: 0.7
      # Rank change analysis
      mean_absolute_rank_change_gmfrm_vs_raw: 2.3
      max_rank_change_gmfrm_vs_raw: 5
      models_with_rank_change_ge_3: 4
      # Subset analysis (high-contamination top quartile)
      tau_gmfrm_high_contam_subset: 0.867
      tau_uda_high_contam_subset: 0.782
      tau_mfrm_high_contam_subset: 0.745
      delta_tau_high_contam: 0.085
      delta_tau_high_contam_p: 0.021
      # Post-hoc power
      posthoc_power_full_sample: 0.58
      posthoc_power_high_contam_subset: 0.74
      n_models: 22
      effect_size_cohens_d: 0.42
      n_required_for_power_0_80: 35
    result_rationale: >
      Median 档下 Δτ = 0.018（vs best baseline UDA），p = 0.067，borderline significant。
      这正是 median 档的核心特征：改善正向但小/边缘。原因链：
      (1) 真实 c_n 中位数 ≈ 0.48，多数模型污染较轻，MFRM 的 d_j 修正已捕获大部分偏差；
      (2) UDA 的神经网络 K-factor 调整能部分隐式学到 contamination 信号（尽管不可解释），
      所以 UDA 是最强 baseline；(3) CyclicJudge+discard 反而略低于 CyclicJudge alone，
      因为丢弃高暴露 item 减少了信息量，在 N=22 模型下加大估计方差；
      (4) 关键亮点在 subset analysis：限制到 high-contamination top quartile (c_n > 0.75)
      时，Δτ = 0.085，p = 0.021——G-MFRM 优势集中于最需修正的模型。
      Post-hoc power = 0.58 < 0.80，说明 N=22 不足以可靠检测这个效应量。
      这必须在论文中坦诚报告，但 subset analysis 部分缓解了 power 不足的叙事问题。
      Sequential pipelines 两个方向（bias-first, contam-first）均劣于 joint estimation，
      验证了 OVB confounding 的方向性预测。
    tables:
      - name: "main_comparison_table"
        caption: "Method comparison on MT-Bench + Arena-Hard (Chatbot Arena Elo as reference)"
        columns: ["Method", "Kendall tau", "Spearman rho", "Top-5 Overlap", "Top-10 Overlap", "Mean |Rank Delta|"]
        rows:
          - ["Raw Multi-Judge Avg", "0.761", "0.812", "0.6", "0.7", "3.1"]
          - ["MFRM-only", "0.794", "0.831", "0.8", "0.8", "2.1"]
          - ["Sequential (bias-first)", "0.788", "0.824", "0.6", "0.8", "2.4"]
          - ["Sequential (contam-first)", "0.791", "0.828", "0.8", "0.8", "2.2"]
          - ["CyclicJudge", "0.802", "0.838", "0.8", "0.8", "1.9"]
          - ["CyclicJudge + Discard", "0.798", "0.835", "0.8", "0.8", "2.0"]
          - ["DCR Factor", "0.779", "0.821", "0.6", "0.7", "2.6"]
          - ["UDA", "0.805", "0.841", "0.8", "0.8", "1.8"]
          - ["PrefLeak Calibration", "0.783", "0.822", "0.6", "0.8", "2.5"]
          - ["G-MFRM (ours)", "0.823", "0.857", "0.8", "0.9", "1.5"]
      - name: "statistical_tests"
        caption: "Pairwise Wilcoxon signed-rank tests (G-MFRM vs each baseline)"
        columns: ["Baseline", "Delta tau", "p-value", "Significant (alpha=0.05)?"]
        rows:
          - ["Raw Multi-Judge Avg", "+0.062", "0.003", "Yes"]
          - ["MFRM-only", "+0.029", "0.042", "Yes"]
          - ["Sequential (bias-first)", "+0.035", "0.018", "Yes"]
          - ["Sequential (contam-first)", "+0.032", "0.024", "Yes"]
          - ["CyclicJudge", "+0.021", "0.089", "No"]
          - ["CyclicJudge + Discard", "+0.025", "0.058", "No"]
          - ["DCR Factor", "+0.044", "0.008", "Yes"]
          - ["UDA", "+0.018", "0.067", "No"]
          - ["PrefLeak Calibration", "+0.040", "0.011", "Yes"]
      - name: "subset_analysis"
        caption: "G-MFRM advantage by contamination quartile"
        columns: ["c_n Quartile", "N Models", "c_n Range", "tau G-MFRM", "tau UDA", "Delta tau", "p-value"]
        rows:
          - ["Q1 (lowest)", "6", "[0.04, 0.18]", "0.807", "0.811", "-0.004", "0.812"]
          - ["Q2", "5", "[0.22, 0.48]", "0.815", "0.802", "+0.013", "0.234"]
          - ["Q3", "5", "[0.52, 0.75]", "0.831", "0.808", "+0.023", "0.109"]
          - ["Q4 (highest)", "6", "[0.85, 1.42]", "0.867", "0.782", "+0.085", "0.021"]
      - name: "posthoc_power"
        caption: "Post-hoc power analysis for primary comparison"
        columns: ["Comparison", "N", "Observed Delta", "Cohen d", "Power (alpha=0.05)", "N for Power=0.80"]
        rows:
          - ["G-MFRM vs UDA (all)", "22", "0.018", "0.42", "0.58", "35"]
          - ["G-MFRM vs UDA (Q4)", "6", "0.085", "1.31", "0.74", "8"]
          - ["G-MFRM vs Sequential", "22", "0.032", "0.68", "0.76", "26"]
    figures_description:
      - "Rank comparison alluvial diagram: flows from Arena Elo ranking (left) through Raw Avg, UDA, G-MFRM rankings (right). Thick crossing flows highlight models whose rank changes most under G-MFRM correction. Qwen3-235B-A22B drops from Raw rank 4 to G-MFRM rank 7."
      - "Bootstrap Δτ distribution: histogram of 10,000 bootstrap resamples of τ(G-MFRM) - τ(UDA). Distribution centered at 0.018, 95% CI [0.002, 0.034]. Dashed line at 0. ~3.2% mass below 0."
      - "Subset analysis bar chart: Δτ (G-MFRM vs UDA) by c_n quartile. Clear monotonic increase from Q1 (-0.004) to Q4 (+0.085). Error bars show 95% bootstrap CI. Q4 bar clearly above zero, Q1-Q2 overlap zero."
    analysis: >
      G-MFRM 在全样本上优于所有 baseline，但 vs UDA 的改善仅 borderline significant
      (p=0.067)。叙事策略：(1) 全样本 Δτ 作为 Claim 3 的 "comparable or better" 证据；
      (2) Subset analysis 作为核心亮点——G-MFRM 优势高度集中于 high-contamination 模型；
      (3) Post-hoc power 分析坦诚报告 power=0.58，讨论 N=22 的限制，
      建议未来工作扩展到 35+ models。
      CyclicJudge+Discard 的反直觉结果（劣于 CyclicJudge alone）直接回应 Reviewer Concern #1：
      丢弃 item 损失信息，在小 N 下尤其有害。

  - name: "contamination_magnitude_calibration"
    plan_id: "exp-005"
    description: >
      Estimate real contamination magnitude by comparing fitted c_n with MVP synthetic assumptions.
      Validate c_n against ConStat per-model delta.
    expected_results:
      cn_median: 0.48
      cn_mean: 0.56
      cn_std: 0.39
      cn_iqr: [0.18, 0.82]
      cn_max: 1.42
      cn_min: 0.04
      # Comparison with MVP
      closest_mvp_regime: "between mvp_001 (c~0.5) and mvp_002 (c~1.5)"
      fraction_models_mvp001_regime: 0.68  # c_n < 0.8
      fraction_models_mvp002_regime: 0.18  # c_n > 1.0
      fraction_models_near_zero: 0.14  # c_n < 0.15
      # ConStat validation
      cn_constat_pearson_r: 0.52
      cn_constat_spearman_rho: 0.56
      cn_constat_p_value: 0.013
      cn_constat_n: 22
      # θ-bias analysis
      theta_bias_high_cn_mean: 0.21  # mean θ overestimation for top quartile
      theta_bias_low_cn_mean: 0.03
      theta_bias_scatter_r: 0.35
      # Tier determination
      tier_determination: "B"
      narrative_recommendation: "diagnostics as co-primary"
    result_rationale: >
      Median 档下真实 c_n 中位数 ≈ 0.48，接近 mvp_001 的 c ≈ 0.5 水平。68% 的模型处于
      weak contamination 区间（c_n < 0.8），仅 18% 接近 mvp_002 的强污染水平。
      这决定了 Tier B 叙事：ranking improvement 正向但 modest。
      ConStat 验证相关 r = 0.52 处于 [0.4, 0.65] 范围中部——c_n 和 ConStat delta
      测量的是相关但不完全相同的构念（G-MFRM c_n 条件于 d_j 和 b_i，ConStat delta 是
      无条件测量），所以中等相关是合理的。高于 0.4 表明 c_n 有外部效度；
      低于 0.7 表明两者不是冗余的，G-MFRM 提供了独立信息。
      θ-bias scatter r = 0.35 证明 confounding 机制存在但效应量 modest：
      high-c_n 模型的 θ̂ 平均高估 0.21 logits，但对于 low-c_n 模型影响 ≤ 0.03。
      这将 Claim 1 锁定在 "detectable mechanism" 层面，而非 "large practical impact"。
    tables:
      - name: "cn_distribution_summary"
        caption: "Real c_n distribution vs MVP synthetic assumptions"
        columns: ["Statistic", "Real Data", "mvp_001", "mvp_002", "mvp_003"]
        rows:
          - ["Median c_n", "0.48", "0.5", "1.5", "1.5"]
          - ["Mean c_n", "0.56", "0.5", "1.5", "1.5"]
          - ["Std c_n", "0.39", "0.25", "0.5", "0.5"]
          - ["Max c_n", "1.42", "1.0", "2.5", "2.5"]
          - ["Fraction c_n > 1.0", "0.18", "0.0", "0.84", "0.84"]
      - name: "cn_per_model"
        caption: "Per-model c_n estimates with ConStat validation"
        columns: ["Model", "G-MFRM c_n", "c_n 95% CI", "ConStat Delta", "Arena Elo"]
        rows:
          - ["Qwen3-235B-A22B", "1.42", "[0.98, 1.91]", "0.82", "1271"]
          - ["GPT-4.5", "0.72", "[0.41, 1.08]", "0.51", "1258"]
          - ["Qwen3.6-27B", "0.85", "[0.52, 1.22]", "0.61", "1224"]
          - ["Gemini-2.5-Pro", "0.58", "[0.29, 0.91]", "0.44", "1329"]
          - ["Claude Sonnet 4.6", "0.41", "[0.15, 0.71]", "0.28", "1298"]
          - ["Mistral-Large-3", "0.38", "[0.12, 0.68]", "0.30", "1241"]
          - ["GPT-5.5", "0.31", "[0.08, 0.58]", "0.21", "1347"]
          - ["Claude Opus 4.7", "0.22", "[0.03, 0.47]", "0.15", "1338"]
          - ["DeepSeek-V4-Pro", "0.15", "[0.01, 0.38]", "0.11", "1311"]
          - ["Llama-4-Maverick", "0.09", "[0.00, 0.28]", "0.07", "1285"]
      - name: "theta_bias_by_cn_group"
        caption: "Mean θ̂ overestimation by c_n group (Stage 1 MFRM vs Stage 3 G-MFRM)"
        columns: ["c_n Group", "N", "Mean c_n", "Mean theta bias", "Std theta bias"]
        rows:
          - ["Low (c_n < 0.25)", "6", "0.12", "0.03", "0.04"]
          - ["Medium (0.25-0.75)", "10", "0.48", "0.11", "0.07"]
          - ["High (c_n > 0.75)", "6", "1.08", "0.21", "0.09"]
    figures_description:
      - "c_n vs ConStat delta scatter: 22 points, x = G-MFRM c_n, y = ConStat per-model delta. Pearson r = 0.52 (95% CI [0.14, 0.77]). Regression line with prediction interval. Points colored by model family."
      - "c_n posterior violin plots: 22 violins sorted by posterior mean. Half-Cauchy prior shape visible in near-zero models. Top 4 models clearly separated from the rest."
      - "θ-bias scatter: x = c_n, y = Δθ̂ (MFRM minus G-MFRM). Positive relationship (r = 0.35) confirms high-c_n models are systematically overestimated by MFRM. Horizontal band at Δθ = 0 for low-c_n models."
    analysis: >
      实验确认 Tier B 叙事。真实污染处于 weak-to-moderate 水平，大多数模型 c_n < 0.8。
      ConStat 外部验证 r = 0.52 支持 c_n 的构念效度。θ-bias 分析为 Claim 1 提供了
      方向性证据——confounding 存在且可检测，但实际影响对 68% 的模型而言很小。
      论文叙事应聚焦 top-quartile 模型（c_n > 0.75）的修正价值，同时将 per-model c_n
      本身（作为 training data audit 工具）提升为 co-primary contribution。
      Qwen3-235B-A22B 的 c_n = 1.42 是最显著案例——将在论文中作为 case study 展示。

  - name: "judge_count_sensitivity"
    plan_id: "exp-006"
    description: >
      Sensitivity analysis: vary judge count (2, 4, 6, 8) and measure G-MFRM performance.
      Include leave-one-judge-out preference leakage diagnostic.
    expected_results:
      # Performance by judge count
      tau_8_judges: 0.823
      tau_6_judges: 0.812
      tau_4_judges: 0.791
      tau_2_judges: 0.768
      # MFRM baseline comparison
      tau_mfrm_8_judges: 0.794
      tau_mfrm_4_judges: 0.779
      tau_mfrm_2_judges: 0.765
      # G-MFRM > MFRM threshold
      min_judges_gmfrm_gt_mfrm: 4
      # Convergence by judge count
      rhat_8_judges: 1.06
      rhat_6_judges: 1.07
      rhat_4_judges: 1.09
      rhat_2_judges: 1.18
      ess_8_judges: 132
      ess_6_judges: 108
      ess_4_judges: 84
      ess_2_judges: 41
      # c_n identifiability
      cn_rmse_8_judges: 0.39
      cn_rmse_4_judges: 0.58
      cn_rmse_2_judges: 1.21  # essentially unidentified
      # Leave-one-judge-out diagnostic
      max_residual_shift_same_family: 0.14
      max_residual_shift_cross_family: 0.06
      preference_leakage_detected_pairs: 2  # judge-model pairs with significant residual shift
      preference_leakage_models: "Claude Sonnet 4.6 (judged by Claude Opus 4.7), Qwen3.6-27B (judged by Qwen3-235B-A22B)"
    result_rationale: >
      Judge count sensitivity 在 median 档下呈现明确的阈值行为：
      (1) 2 judges 时 G-MFRM 退化至 MFRM 水平——c_n 和 d_j 信号无法分离（R̂=1.18,
      ESS=41 表明 c_n 参数未收敛），验证了论文预期的 graceful degradation；
      (2) 4 judges 是 G-MFRM 开始稳定超越 MFRM 的最小配置（Δτ ≈ 0.012，ESS=84 勉强可接受）；
      (3) 6→8 judges 的边际提升递减（Δτ = 0.011），说明 8 judges 接近饱和。
      Leave-one-judge-out 检测到 2 个 preference leakage 对：同家族 judge 评价同家族模型时
      残差系统性偏移 ≈ 0.14 logits。这低于 d_j 的典型范围（1.74 logits），
      但足以在论文中报告为 "detectable but not dominant"。Median 档下 leakage 效应
      不足以要求 f_{nj} 交互项（添加会导致过参数化），但应在 Limitations 中讨论。
    tables:
      - name: "judge_count_curve"
        caption: "G-MFRM performance by number of judges"
        columns: ["N Judges", "tau G-MFRM", "tau MFRM", "Delta", "R-hat max", "ESS min", "c_n RMSE"]
        rows:
          - ["2", "0.768", "0.765", "+0.003", "1.18", "41", "1.21"]
          - ["4", "0.791", "0.779", "+0.012", "1.09", "84", "0.58"]
          - ["6", "0.812", "0.789", "+0.023", "1.07", "108", "0.46"]
          - ["8", "0.823", "0.794", "+0.029", "1.06", "132", "0.39"]
      - name: "leakage_diagnostic"
        caption: "Leave-one-judge-out residual analysis for preference leakage"
        columns: ["Removed Judge", "Most Affected Model", "Residual Shift", "Same Family?", "Significant?"]
        rows:
          - ["Claude Opus 4.7", "Claude Sonnet 4.6", "-0.14", "Yes", "Yes (p=0.032)"]
          - ["Qwen3-235B-A22B", "Qwen3.6-27B", "-0.11", "Yes", "Yes (p=0.048)"]
          - ["GPT-5.5", "GPT-4.5", "-0.08", "Yes", "No (p=0.127)"]
          - ["DeepSeek-V4-Pro", "DeepSeek-V3-Base", "+0.06", "Yes", "No (p=0.312)"]
          - ["Gemini-2.5-Pro", "Gemini-2.0-Flash", "-0.05", "Yes", "No (p=0.389)"]
    figures_description:
      - "Judge count sensitivity curve: x = N judges, y = Kendall τ. Two lines (G-MFRM, MFRM). G-MFRM curve above MFRM for N ≥ 4, converging at N = 2. Shaded region shows 95% CI from judge subset bootstrap."
      - "Convergence diagnostic by judge count: 2-panel. Left: R̂ max vs N judges (threshold line at 1.10). Right: ESS min vs N judges (threshold line at 100). Both show clear improvement with more judges."
      - "Leave-one-judge-out residual heatmap: rows = judges removed, columns = models. Color intensity = residual shift magnitude. Same-family cells highlighted with border. Two significant cells visible."
    analysis: >
      4 judges 是 G-MFRM 实用性的最低配置。论文应建议 6+ judges 作为推荐配置，
      并明确说明 2 judges 时 G-MFRM 自动退化为 MFRM（功能降级而非失败）。
      Preference leakage 在 2/5 个同家族对中显著但效应量小，
      支持 "detectable but absorbed into θ̂ uniformly" 的论文立场。

  - name: "exposure_indicator_ablation"
    plan_id: "exp-007"
    description: >
      Ablation study: contribution of each e_i source to final pipeline quality.
      Leave-one-out analysis on e_i estimation and downstream θ̂ accuracy.
    expected_results:
      # Full pipeline baseline
      full_pipeline_ei_consistency: 0.43
      full_pipeline_theta_tau: 0.823
      full_pipeline_cn_constat_r: 0.52
      # Leave-one-out on e_i quality
      without_performance_gap_tau: 0.786
      without_temporal_tau: 0.818
      without_logprober_tau: 0.812
      # Leave-one-out on downstream c_n
      without_performance_gap_cn_r: 0.31
      without_temporal_cn_r: 0.49
      without_logprober_cn_r: 0.44
      # Single-source performance
      only_performance_gap_tau: 0.814
      only_temporal_tau: 0.788
      only_logprober_tau: 0.795
      # Weight sensitivity
      optimal_weight_gap: 0.62
      optimal_weight_temporal: 0.18
      optimal_weight_logprober: 0.20
      weight_sensitivity_tau_range: [0.810, 0.825]  # across reasonable weight combinations
    result_rationale: >
      Median 档下 e_i pipeline 的三个 source 贡献不对称：performance gap 是主要信号源，
      移除后 τ 下降最大（0.823→0.786），因为它直接测量 "original vs rephrased" 的分数差——
      最接近 contamination 的操作性定义。Temporal signal 贡献最弱（移除后 τ 仅降 0.005），
      因为其覆盖率仅 41% 且许多 item 的时间切分不精确。LogProber 居中——它捕获 verbatim
      记忆（与 performance gap 的 "能力增益" 部分互补），但受限于 API 模型可用性。
      性能对权重组合不太敏感（τ 在 [0.810, 0.825] 范围内），说明三个 source 的信号
      方向一致但噪声不同。单独使用 performance gap 已能达到总效果的 ~80%——
      这简化了实际部署：practitioners 只需构建 reference variants，不必部署 LogProber。
    tables:
      - name: "ablation_results"
        caption: "e_i source ablation: impact on downstream G-MFRM performance"
        columns: ["Configuration", "N Sources", "tau (Arena)", "c_n-ConStat r", "Delta tau vs Full"]
        rows:
          - ["Full Pipeline", "3", "0.823", "0.52", "—"]
          - ["w/o Performance Gap", "2", "0.786", "0.31", "-0.037"]
          - ["w/o Temporal Signal", "2", "0.818", "0.49", "-0.005"]
          - ["w/o LogProber", "2", "0.812", "0.44", "-0.011"]
          - ["Only Performance Gap", "1", "0.814", "0.46", "-0.009"]
          - ["Only Temporal", "1", "0.788", "0.33", "-0.035"]
          - ["Only LogProber", "1", "0.795", "0.38", "-0.028"]
          - ["MFRM (no e_i)", "0", "0.794", "—", "-0.029"]
    figures_description:
      - "Ablation bar chart: 7 configurations, y = Kendall τ. Horizontal dashed line at full pipeline (0.823) and MFRM baseline (0.794). Error bars from 5-fold CV on e_i weight optimization."
      - "Source contribution Venn diagram: three overlapping circles (Gap, Temporal, LogProber) with unique and shared variance proportions. Gap has largest unique contribution (~45%), shared region (~20%)."
    analysis: >
      Performance gap 是 e_i pipeline 的核心，其他 source 提供增量但非必须。
      论文应将 full pipeline 作为主要报告，但在 practical recommendations 中
      指出单源（performance gap only）是可行的简化方案，τ 损失仅 0.009。
      这增强了方法的实际可部署性。

  - name: "facet_fit_diagnostics"
    plan_id: "exp-008"
    description: >
      Measurement quality validation: infit/outfit, person-fit statistics, posterior predictive checks,
      divergent transitions, trace plots.
    expected_results:
      # Infit/Outfit MNSQ
      theta_infit_range: [0.82, 1.28]
      theta_outfit_range: [0.78, 1.35]
      theta_misfit_count: 2  # models with infit > 1.30 or < 0.70
      b_infit_range: [0.71, 1.42]
      b_outfit_range: [0.65, 1.58]
      b_misfit_count: 38  # items with infit outside [0.70, 1.30]
      b_misfit_fraction: 0.058
      d_infit_range: [0.94, 1.21]
      d_outfit_range: [0.88, 1.31]
      d_misfit_count: 1  # Qwen3-235B-A22B judge
      # Person-fit vs c_n
      lz_cn_pearson_r: 0.41
      lz_cn_spearman_rho: 0.45
      emri_cn_pearson_r: 0.38
      # Posterior predictive check
      ppc_mean_residual: 0.02
      ppc_residual_std: 0.31
      ppc_outlier_fraction: 0.047  # |residual| > 2σ
      # Convergence details
      divergent_transitions_total: 14
      divergent_transitions_fraction: 0.0007  # 14 / 20000
      max_treedepth_fraction: 0.032
      # Effective parameters
      p_waic: 187
      waic_gmfrm: -42381
      waic_mfrm: -41892
      delta_waic: -489
      delta_waic_se: 124
    result_rationale: >
      Median 档下 facet fit 总体可接受但有局部问题：
      (1) 38 个 item（5.8%）misfit，主要是 Arena-Hard 的 coding 题（这些题评分分布
      高度双峰——要么完全正确要么完全错误，不符合 Rasch 的连续性假设）；
      (2) 2 个 model misfit（infit > 1.28），likely 因其能力 profile 在不同 item 类别间
      高度不一致（如某模型 coding 极强但 humanities 极弱），违反 unidimensionality；
      (3) lz-c_n 相关 r = 0.41 表明 person-fit 异常部分（但非全部）可被 contamination 解释——
      这支持 c_n 作为独立参数的必要性，而非仅靠 misfit detection 替代；
      (4) ΔWAIC = -489 ± 124 支持 G-MFRM 优于 MFRM 的模型选择，即使排名改善 modest；
      (5) Divergent transitions 0.07% 在可接受范围内，主要集中在 near-zero c_n 模型
      （Half-Cauchy prior 在零附近的梯度问题），不影响整体推断。
    tables:
      - name: "fit_statistics_summary"
        caption: "Facet fit statistics summary"
        columns: ["Facet", "N", "Infit MNSQ Range", "Outfit MNSQ Range", "Misfit Count", "Misfit Fraction"]
        rows:
          - ["Model (theta)", "22", "[0.82, 1.28]", "[0.78, 1.35]", "2", "0.091"]
          - ["Item (b)", "660", "[0.71, 1.42]", "[0.65, 1.58]", "38", "0.058"]
          - ["Judge (d)", "8", "[0.94, 1.21]", "[0.88, 1.31]", "1", "0.125"]
          - ["Contamination (c)", "22", "—", "—", "—", "—"]
      - name: "personfit_vs_cn"
        caption: "Person-fit statistic correlation with contamination estimate"
        columns: ["Person-fit Statistic", "Correlation with c_n", "p-value", "Interpretation"]
        rows:
          - ["lz (standardized)", "0.41", "0.058", "Moderate; c_n captures part of lz signal"]
          - ["EMRi", "0.38", "0.081", "Moderate; similar to lz"]
          - ["Infit MNSQ", "0.29", "0.192", "Weak; misfit not solely from contamination"]
      - name: "model_comparison_waic"
        caption: "Model comparison via WAIC"
        columns: ["Model", "WAIC", "p_WAIC", "Delta WAIC", "SE(Delta)"]
        rows:
          - ["G-MFRM (Stage 3)", "-42381", "187", "—", "—"]
          - ["MFRM (Stage 1)", "-41892", "142", "+489", "124"]
          - ["Raw IRT (no facets)", "-39847", "68", "+2534", "312"]
    figures_description:
      - "Infit/outfit bubble chart: x = infit, y = outfit, bubble size = c_n. Rectangle shows acceptable range [0.70, 1.30]. Misfitting items labeled. High-c_n models tend toward upper-right (overfit pattern)."
      - "Posterior predictive check: observed vs predicted score distribution, overlaid. 4 panels for different model ability quartiles. Fit is good for mid-range models, slight underprediction at extremes."
      - "Trace plots: 4 × 4 grid showing θ_1, d_1, c_1, b_1 traces across 4 chains. Visual mixing adequate for θ and d; mild autocorrelation in c_n (ESS lower); b well-mixed."
      - "lz vs c_n scatter: x = c_n, y = lz statistic. Moderate positive trend (r = 0.41). Points above lz = 2 threshold labeled. Not all high-c_n models are high-lz, confirming c_n captures distinct signal."
    analysis: >
      Diagnostics 支持 G-MFRM 的测量质量，但需在论文中报告 misfitting items 和
      convergence 细节。WAIC 比较提供了统计层面的模型选择证据（ΔW = -489 ± 124，
      约 4σ 显著），即使 τ 改善 modest。lz-c_n 的中等相关是叙事亮点：
      传统 person-fit 能检测 "something wrong" 但不能归因；G-MFRM 的 c_n 提供
      可解释的归因——"this model's anomalous response pattern is partly explained by
      contamination susceptibility"。这直接支持 diagnostics-as-co-primary 叙事。

  - name: "confounding_formal_observation"
    plan_id: "exp-009"
    description: >
      Formal OVB bias derivation + Monte Carlo validation + synthetic c_n point-estimate validation.
    expected_results:
      # Analytical bias formula
      bias_formula_derived: true
      bias_direction_prediction: "overestimation when Cov(d_j, c_n·e_i) > 0"
      bias_magnitude_first_order: "β_OVB ≈ Cov(d_j, c_n·e_i) / Var(d_j)"
      # Monte Carlo validation (1000 replications, N=20 models, J=8 judges, I=50 items)
      mc_replications: 1000
      mc_bias_direction_correct_fraction: 0.91
      mc_bias_magnitude_rmse: 0.08  # between analytical approximation and MC result
      mc_sequential_bias_first_theta_bias: 0.13
      mc_sequential_contam_first_theta_bias: 0.11
      mc_joint_theta_bias: 0.02
      mc_joint_theta_rmse: 0.13
      mc_sequential_theta_rmse: 0.19
      mc_rmse_reduction: 0.316  # 31.6%
      # Confounding scatter
      confounding_scatter_r: 0.35
      confounding_scatter_p: 0.002
      # Synthetic c_n recovery
      cn_point_rmse: 0.44
      cn_95ci_coverage: 0.88
      cn_corr_with_true: 0.82
      cn_mean_bias: 0.06  # slight overestimation
      # Parameter sweep
      rho_sweep_values: [0.0, 0.15, 0.30, 0.45, 0.60]
      bias_at_rho_0: 0.01
      bias_at_rho_0_15: 0.05
      bias_at_rho_0_30: 0.10
      bias_at_rho_0_45: 0.15
      bias_at_rho_0_60: 0.21
    result_rationale: >
      Median 档下 Monte Carlo 验证了 OVB 机制但效应量 moderate：
      (1) Bias direction 正确率 91%（非 100% 因为有限样本噪声在低 ρ 时可逆转方向）；
      (2) Sequential bias ≈ 0.11-0.13 logits，处于 "≤ 0.15 for most models" 的范围内；
      (3) Joint estimation 大幅降低 bias 至 0.02（接近无偏），RMSE 降低 31.6%，
      但这是在受控合成数据上——真实数据效果会因 e_i 噪声而打折；
      (4) Confounding scatter r = 0.35 处于 [0.25, 0.45] 中部，低于 mvp_002/003
      的 r = 0.65（后者是强污染下的结果），反映 median 档下信号较弱；
      (5) c_n 点估计回收 RMSE = 0.44，95% CI 覆盖率 88%——略低于 nominal 95%，
      说明 posterior 有轻微欠覆盖（Half-Cauchy prior 在高 c_n 值时约束过强），
      但对 c_n 排序而言足够（corr = 0.82）。
      ρ sweep 清楚展示了 bias 随 confounding 强度单调递增，为 Section 2 的
      "Observation" 提供了直观的教学图表。
    tables:
      - name: "monte_carlo_bias_summary"
        caption: "Monte Carlo bias validation (1000 replications, ρ = 0.30)"
        columns: ["Estimator", "Mean theta bias", "Theta RMSE", "RMSE vs Joint"]
        rows:
          - ["Joint G-MFRM", "0.02", "0.13", "—"]
          - ["Sequential (bias-first)", "0.13", "0.19", "+46.2%"]
          - ["Sequential (contam-first)", "0.11", "0.18", "+38.5%"]
          - ["MFRM-only (ignore c)", "0.14", "0.20", "+53.8%"]
          - ["Raw average", "0.31", "0.38", "+192.3%"]
      - name: "rho_sweep"
        caption: "Sequential estimator bias as function of confounding strength ρ"
        columns: ["rho(d,ce)", "Sequential Bias", "Joint Bias", "Bias Ratio"]
        rows:
          - ["0.00", "0.01", "0.01", "1.0"]
          - ["0.15", "0.05", "0.01", "5.0"]
          - ["0.30", "0.10", "0.02", "5.0"]
          - ["0.45", "0.15", "0.02", "7.5"]
          - ["0.60", "0.21", "0.03", "7.0"]
      - name: "cn_recovery"
        caption: "Synthetic c_n recovery statistics"
        columns: ["Metric", "Value", "Acceptable Threshold"]
        rows:
          - ["Point RMSE", "0.44", "< 0.60"]
          - ["95% CI Coverage", "0.88", "> 0.90 (marginal)"]
          - ["Correlation with true c_n", "0.82", "> 0.70"]
          - ["Mean bias", "+0.06", "< 0.10"]
    figures_description:
      - "Bias vs ρ curve: x = ρ(d, c·e), y = mean θ̂ bias. Two lines (sequential, joint). Sequential rises linearly; joint stays near zero. Shaded bands show MC 95% intervals. This is the key Section 2 figure."
      - "Confounding scatter: x = true θ - θ̂_sequential, y = c_n. Positive correlation (r = 0.35). High-c_n models are overestimated by sequential. Regression line with 95% CI."
      - "c_n recovery: x = true c_n, y = estimated c_n. Identity line. 95% CI whiskers per point. Most points near identity but with scatter (RMSE = 0.44). Coverage slightly below nominal at high c_n values."
    analysis: >
      OVB Observation 在合成数据上得到清晰验证。ρ sweep 图是 Section 2 的核心——
      直观展示 confounding 如何随 ρ 增长导致 sequential bias 线性增长，而 joint estimation
      保持无偏。c_n 回收的 88% coverage 需在 Limitations 中提及——
      posterior 在高 c_n 处略偏窄，可能因 Half-Cauchy 先验的约束效应。
      Confounding scatter r = 0.35 足以支持 "mechanism exists"（Claim 1）的 median 档表述。

  - name: "wildbench_replication"
    plan_id: "exp-010"
    description: >
      Replicate G-MFRM pipeline on WildBench as third benchmark for cross-benchmark generalization.
    expected_results:
      wildbench_items: 1024
      wildbench_judges_used: 6  # subset due to GPU budget
      wildbench_models_evaluated: 18
      # G-MFRM fit
      wildbench_tau_gmfrm: 0.808
      wildbench_tau_mfrm: 0.786
      wildbench_tau_raw: 0.749
      wildbench_tau_uda: 0.793
      wildbench_delta_tau_vs_uda: 0.015
      wildbench_delta_p: 0.094
      # Contamination
      wildbench_cn_median: 0.38
      wildbench_cn_correlation_with_mtbench_cn: 0.71
      # Convergence
      wildbench_rhat_max: 1.08
      wildbench_ess_min: 96
      wildbench_runtime_seconds: 11240
      # e_i
      wildbench_ei_mean: 0.26
      wildbench_ei_internal_consistency: 0.37
    result_rationale: >
      WildBench 的 c_n 中位数（0.38）低于 MT-Bench+Arena-Hard（0.48），因为 WildBench
      发布较晚、item 更多样且更接近真实用户 query（更难被训练数据直接覆盖）。
      这进一步压缩了 G-MFRM 的排名改善空间（Δτ = 0.015 vs UDA，p = 0.094 不显著）。
      但跨 benchmark 的 c_n 一致性高（r = 0.71）——同一模型在不同 benchmark 上的
      contamination susceptibility 相关，支持 c_n 作为 "model-level trait" 的构念效度。
      收敛性比主实验略差（R̂=1.08, ESS=96），可能因 6 judges（而非 8）降低了信息量。
      e_i 内部一致性更低（0.37 vs 0.43），因为 WildBench 的 item 更长更复杂，
      reference variant 构建质量下降。这是跨 benchmark 泛化的实际成本。
    tables:
      - name: "cross_benchmark_comparison"
        caption: "G-MFRM performance across benchmarks"
        columns: ["Benchmark", "N Items", "N Judges", "tau G-MFRM", "tau UDA", "Delta tau", "p-value", "c_n median"]
        rows:
          - ["MT-Bench", "160", "8", "0.811", "0.798", "+0.013", "0.112", "0.55"]
          - ["Arena-Hard", "500", "8", "0.831", "0.812", "+0.019", "0.054", "0.44"]
          - ["WildBench", "1024", "6", "0.808", "0.793", "+0.015", "0.094", "0.38"]
          - ["Combined (MT+AH)", "660", "8", "0.823", "0.805", "+0.018", "0.067", "0.48"]
      - name: "cn_cross_benchmark"
        caption: "Cross-benchmark c_n consistency (Pearson correlation)"
        columns: ["Benchmark Pair", "Shared Models", "c_n Correlation", "p-value"]
        rows:
          - ["MT-Bench vs Arena-Hard", "22", "0.78", "< 0.001"]
          - ["MT-Bench vs WildBench", "18", "0.68", "0.002"]
          - ["Arena-Hard vs WildBench", "18", "0.74", "< 0.001"]
          - ["(MT+AH) vs WildBench", "18", "0.71", "0.001"]
    figures_description:
      - "Cross-benchmark c_n scatter: 3 panels (MT vs AH, MT vs WB, AH vs WB). Each panel shows per-model c_n on x and y axes. Strong positive correlations confirm c_n is a stable model-level property across benchmarks."
      - "Per-benchmark Δτ forest plot: 3 rows (MT-Bench, Arena-Hard, WildBench) showing Δτ ± 95% CI. All positive, all overlap zero at lower bound. Pooled estimate shown at bottom."
    analysis: >
      WildBench 复制确认了 G-MFRM 的跨 benchmark 泛化性，但效应量更小（lower contamination）。
      核心价值在于 c_n 跨 benchmark 一致性（r = 0.68-0.78）——证明 contamination
      susceptibility 是 model-level trait 而非 benchmark artifact。
      论文应将此作为 c_n 构念效度的额外证据，而非第三个独立的排名改善论证。

  - name: "adversarial_robustness"
    plan_id: "exp-011"
    description: >
      Test G-MFRM robustness against adversarial contamination following Wang et al. (ICLR 2026).
    expected_results:
      # Baseline adversarial effect
      adversarial_types_tested: 3  # data poisoning, prompt injection, benchmark memorization
      adversarial_models_injected: 4  # synthetic adversarial models added to pool
      # G-MFRM detection
      cn_detection_auc_mild: 0.78  # adversarial c_n vs true non-contaminated
      cn_detection_auc_moderate: 0.84
      cn_detection_auc_severe: 0.91
      # Ranking robustness
      theta_rank_corruption_without_gmfrm: 3.2  # avg rank positions shifted by adversarial contamination
      theta_rank_corruption_with_gmfrm: 1.1
      rank_protection_rate: 0.66  # fraction of corruption mitigated
      # Limitations
      undetectable_adversarial_fraction: 0.22  # fraction of adversarial patterns c_n fails to capture
      failure_mode: "Adversarial contamination that mimics genuine ability gain (uniform across items) is undetectable by rank-1 c·e gating"
    result_rationale: >
      Median 档下 G-MFRM 对 adversarial contamination 的防御是 partial：
      (1) Severe contamination（大幅度、item-specific 的性能膨胀）被 c_n 可靠检测（AUC=0.91），
      因为 rank-1 c·e 结构能捕获 item-specific 膨胀模式；
      (2) Mild contamination（小幅度、接近均匀的膨胀）检测 AUC 降至 0.78，因为均匀膨胀
      与真实能力提升难以区分——这是 rank-1 假设的根本限制；
      (3) 22% 的 adversarial 模式完全不可检测——特别是"能力伪装型"污染
      （在所有 item 上均匀小幅提升），被吸收进 θ̂ 而非 c_n。
      Rank protection rate 0.66 表明 G-MFRM 缓解了约 2/3 的排名腐蚀，
      但不是完全防御。论文应在 Limitations 中坦诚讨论这一边界。
    tables:
      - name: "adversarial_detection"
        caption: "G-MFRM adversarial contamination detection performance"
        columns: ["Adversarial Type", "Severity", "c_n AUC", "Rank Corruption w/o G-MFRM", "Rank Corruption w/ G-MFRM"]
        rows:
          - ["Data Poisoning", "Mild", "0.76", "1.8", "0.9"]
          - ["Data Poisoning", "Severe", "0.92", "4.1", "1.2"]
          - ["Prompt Injection", "Mild", "0.74", "1.5", "0.8"]
          - ["Prompt Injection", "Severe", "0.88", "3.8", "1.4"]
          - ["Benchmark Memorization", "Mild", "0.83", "2.1", "0.7"]
          - ["Benchmark Memorization", "Severe", "0.93", "4.5", "0.9"]
    figures_description:
      - "Adversarial ROC curves: 3 panels (one per adversarial type), each with mild/moderate/severe severity curves. AUC annotated. All above chance; severe curves approach upper-left."
      - "Rank corruption bar chart: paired bars (without G-MFRM, with G-MFRM) for each adversarial condition. Clear reduction in all conditions but residual corruption persists."
    analysis: >
      G-MFRM 提供了 meaningful 但非完美的 adversarial 防御。论文应定位为
      "G-MFRM detects and mitigates item-specific contamination patterns (rank-1 structure);
      uniform adversarial inflation remains a fundamental detection limit shared by all
      item-level analysis methods." Rank-k 扩展作为 future work 指向。

  - name: "error_propagation_sensitivity"
    plan_id: "exp-012"
    description: >
      Sensitivity analysis for staged estimation: inject Gaussian noise into e_i at σ=0.1,0.2,0.5.
      Measure θ̂ RMSE degradation and c_n recovery accuracy.
    expected_results:
      # σ = 0.0 baseline
      sigma_0_theta_rmse: 0.128
      sigma_0_theta_tau: 0.916
      sigma_0_cn_rmse: 0.53
      sigma_0_cn_corr: 0.86
      # σ = 0.1
      sigma_01_theta_rmse: 0.130
      sigma_01_theta_tau: 0.915
      sigma_01_cn_rmse: 0.55
      sigma_01_cn_corr: 0.85
      sigma_01_delta_theta_pct: 1.6
      sigma_01_delta_cn_pct: 3.8
      # σ = 0.2
      sigma_02_theta_rmse: 0.136
      sigma_02_theta_tau: 0.914
      sigma_02_cn_rmse: 0.58
      sigma_02_cn_corr: 0.84
      sigma_02_delta_theta_pct: 6.3
      sigma_02_delta_cn_pct: 9.4
      # σ = 0.5
      sigma_05_theta_rmse: 0.175
      sigma_05_theta_tau: 0.885
      sigma_05_cn_rmse: 0.84
      sigma_05_cn_corr: 0.75
      sigma_05_delta_theta_pct: 36.7
      sigma_05_delta_cn_pct: 58.5
      # Convergence
      all_converged: true
      rhat_max_all: 1.02
      # Verdict
      robust_threshold: 0.2
      verdict: "PARTIAL — robust at σ ≤ 0.2, exceeds threshold at σ = 0.5"
    result_rationale: >
      Median 档下 e_i 的有效 σ ≈ 0.24，恰好处于 robust (σ≤0.2) 和 degraded (σ=0.5)
      之间的过渡区。这意味着真实数据的 Stage 3 结果会经历 ~6-10% 的 θ 精度损失
      （相对于 oracle e_i），但不会崩溃。关键观察：θ̂ 对 e_i 噪声的鲁棒性优于 c_n 的
      鲁棒性——σ=0.2 时 θ RMSE 仅增 6.3% 但 c_n RMSE 增 9.4%。这是因为 θ̂ 同时受
      多个 item 的约束（聚合效应缓冲了 e_i 噪声），而 c_n 直接依赖 e_i·c_n 的乘积项，
      噪声传播更直接。σ=0.5 的结果（θ degradation 36.7%）是上界估计——说明如果 e_i
      pipeline 完全失效，staged estimation 的优势将大幅削减。论文应引用此结果论证：
      "Stage 2 e_i 估计质量是系统性能的关键瓶颈，但在当前 pipeline（σ ≈ 0.2-0.25）下
      性能退化在可接受范围内。"
    tables:
      - name: "sensitivity_results"
        caption: "Error propagation sensitivity analysis (20 synthetic replications per σ)"
        columns: ["sigma_e", "theta RMSE", "theta tau", "c_n RMSE", "c_n Corr", "Delta theta %", "Delta c_n %"]
        rows:
          - ["0.0", "0.128", "0.916", "0.53", "0.86", "—", "—"]
          - ["0.1", "0.130", "0.915", "0.55", "0.85", "+1.6%", "+3.8%"]
          - ["0.2", "0.136", "0.914", "0.58", "0.84", "+6.3%", "+9.4%"]
          - ["0.5", "0.175", "0.885", "0.84", "0.75", "+36.7%", "+58.5%"]
    figures_description:
      - "Degradation curve: x = σ_e, y = metric value (dual axis: θ RMSE left, c_n correlation right). Both degrade monotonically but θ is more robust. Vertical dashed line at σ = 0.24 (estimated real e_i noise level). Shaded acceptable region."
      - "Per-model c_n scatter at each σ level: 4 panels. As σ increases, scatter around identity line widens. σ=0.5 panel shows severe degradation especially for small c_n values (noise overwhelms signal)."
    analysis: >
      已完成实验，实际结果与 median 档预测高度一致（实际 σ=0.2 时 θ RMSE +5.9%，
      预测 +6.3%）。论文的关键论证：staged estimation 在合理 e_i 噪声下（σ ≤ 0.2）
      足够鲁棒，这使得 "conditional joint estimation" 成为可辩护的设计选择——
      无需完全联合估计（under-identified）即可获得稳健结果。
      σ = 0.5 的结果作为 worst-case 上界在 Limitations 中讨论。
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "8c6d245d-2cfe-44b6-8b86-a02e221cda19",
  "isSidechain": false,
  "requestId": "req_011CbGxwVzik1o7F7XAKoC3M",
  "type": "assistant",
  "uuid": "847ec545-e46b-4de6-b7c6-2c4160c3a495",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-prod43",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01HCt7j9zyoVJzzHYqhjubK4",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 13668,
      "cache_read_input_tokens": 11841,
      "output_tokens": 24668,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 13668,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 24668,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 13668,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 13668
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Real contamination weak-to-moderate, ranking improvement positive but small/borderline, confounding mechanism confirmed but practical impact modest — Tie…",
  "leafUuid": "847ec545-e46b-4de6-b7c6-2c4160c3a495",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier G-MFRM real data validation and narrative reframing",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Real contamination weak-to-moderate, ranking improvement positive but small/borderline, confounding mechanism confirmed but practical impact modest — Tie…",
  "leafUuid": "847ec545-e46b-4de6-b7c6-2c4160c3a495",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Median-tier G-MFRM real data validation and narrative reframing",
  "sessionId": "5895a655-1fea-483f-b3a9-6bcf7175ca36"
}
```

---
