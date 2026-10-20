# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Claims 1+3+4 hold; Claim 2 (meta-critique) seen as valid but insufficientl

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/4e44d1b7-fd1c-4ed7-af50-7fa78a30962b.jsonl`
- **Structured JSON:** [`192eb9a8aa9b3086e3ac.json`](../../sessions/19/192eb9a8aa9b3086e3ac.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T01:34:30.090Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T01:34:30.090Z",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Claims 1+3+4 hold; Claim 2 (meta-critique) seen as valid but insufficiently novel. GSM1K N=33 flagged as underpowered. Borderline accept — likely needs one revision cycle or lands in findings track.\n核心假设：[\"38% instability accepted but reviewers insist ρ=0.307 means 'probably just capability improvement' — demand explicit decomposition or hedge\", \"Meta-critique acknowledged but ≥1 reviewer says 'this is well-known in psychometrics, contribution to ML is incremental'\", 'GSM1K N=33 flagged: CI too wide (r ∈ [−0.7, −0.2]), reviewers want N≥50 or second contamination proxy', \"Downstream impact (z-scores) accepted but reviewers ask 'so what — rankings don't change (ρ=0.997)'\", 'plan_010 shows modest improvement: decoder-only C% at 26-30%, IRT fit marginal', 'No successful additional benchmark replication beyond GSM8K']\n关键指标范围：{'expected_reviewer_avg_score': [5.5, 6.5], 'architecture_stratified_c_pct': [26, 31], 'architecture_stratified_irt_rmsea': [0.05, 0.08], 'additional_benchmark_delta_tpr': [0.1, 0.4], 'gsm1k_correlation_if_bootstrapped_ci': [-0.75, -0.15], 'reviewer_novelty_score': [4, 6], 'reviewer_significance_score': [5, 7]}\n叙事方向：Soften Claim 2 from \"fundamental blind spot\" to \"underappreciated methodological gap\" — cite psychometric literature showing this distinction is known but not applied in ML. Add explicit caveat on 38%: \"instability reflects a mixture of capability improvement and differential item functioning; we measure the former as lower bound on the latter.\" Reframe ρ=0.997 paradox as feature: \"rankings are robust BECAUSE of massive redundancy, but the 31% unstable items carry disproportionate discriminative information — this is a measurement efficiency problem, not a validity crisis.\" GSM1K result downgraded from \"cross-benchmark validation\" to \"suggestive evidence; replication with larger N needed.\" Position for ICLR findings track if main rejected, with rebuttal emphasizing the semi-synthetic framework (Claim 3) as the most portable contribution.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: Post-pivot framing: characterization + methodology paper, NOT methods paper. Key new evidence since last Dream: (1) GSM8K cross-benchmark replication ΔTPR=+0.818, (2) GSM1K contamination gap anti-correlation r=−0.478 — DIF captures capability-discriminative items that contamination can't fake, (3) downstream impact z=-8 to -49σ confirming DIF items are discriminative carriers. Assess whether these strengthen ICLR main conference viability vs findings track.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — we cannot decompose 38% into contamination vs capability improvement\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\" — mutual value positioning\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T01:34:30.094Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T01:34:30.094Z",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T01:34:30.117Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Claims 1+3+4 hold; Claim 2 (meta-critique) seen as valid but insufficiently novel. GSM1K N=33 flagged as underpowered. Borderline accept — likely needs one revision cycle or lands in findings track.
核心假设：["38% instability accepted but reviewers insist ρ=0.307 means 'probably just capability improvement' — demand explicit decomposition or hedge", "Meta-critique acknowledged but ≥1 reviewer says 'this is well-known in psychometrics, contribution to ML is incremental'", 'GSM1K N=33 flagged: CI too wide (r ∈ [−0.7, −0.2]), reviewers want N≥50 or second contamination proxy', "Downstream impact (z-scores) accepted but reviewers ask 'so what — rankings don't change (ρ=0.997)'", 'plan_010 shows modest improvement: decoder-only C% at 26-30%, IRT fit marginal', 'No successful additional benchmark replication beyond GSM8K']
关键指标范围：{'expected_reviewer_avg_score': [5.5, 6.5], 'architecture_stratified_c_pct': [26, 31], 'architecture_stratified_irt_rmsea': [0.05, 0.08], 'additional_benchmark_delta_tpr': [0.1, 0.4], 'gsm1k_correlation_if_bootstrapped_ci': [-0.75, -0.15], 'reviewer_novelty_score': [4, 6], 'reviewer_significance_score': [5, 7]}
叙事方向：Soften Claim 2 from "fundamental blind spot" to "underappreciated methodological gap" — cite psychometric literature showing this distinction is known but not applied in ML. Add explicit caveat on 38%: "instability reflects a mixture of capability improvement and differential item functioning; we measure the former as lower bound on the latter." Reframe ρ=0.997 paradox as feature: "rankings are robust BECAUSE of massive redundancy, but the 31% unstable items carry disproportionate discriminative information — this is a measurement efficiency problem, not a validity crisis." GSM1K result downgraded from "cross-benchmark validation" to "suggestive evidence; replication with larger N needed." Position for ICLR findings track if main rejected, with rebuttal emphasizing the semi-synthetic framework (Claim 3) as the most portable contribution.


基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
focus: Post-pivot framing: characterization + methodology paper, NOT methods paper. Key new evidence since last Dream: (1) GSM8K cross-benchmark replication ΔTPR=+0.818, (2) GSM1K contamination gap anti-correlation r=−0.478 — DIF captures capability-discriminative items that contamination can't fake, (3) downstream impact z=-8 to -49σ confirming DIF items are discriminative carriers. Assess whether these strengthen ICLR main conference viability vs findings track.

## paper_framing.md

# Paper Framing — irt_equated_bench_regen

## Target Venue
- Primary: ICLR 2027 (expected deadline ~October 2026)

## Paper Type
Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."

## Core Claims (4 条, 可证伪)

**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.
- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)
- Honesty requirement: ρ=0.307 means "item instability" may mainly reflect "models got better at those domains" — we cannot decompose 38% into contamination vs capability improvement

**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"

**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability

**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.
3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.
4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).
- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)
- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading" — mutual value positioning
- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth

## Story Spine

**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.

**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.

**What we find**: Three discoveries, each a contribution:

1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.

2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.

3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.

4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.

**Headline result**: "Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000)."

## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks

Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.

## Venue Fit

- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.
- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as "bringing mature psychometric tools to characterize an urgent ML evaluation problem."

## Anticipated Reviewer Concerns (updated for pivot)

1. **"38% could just mean models got better"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.

2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.

3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.

4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.

5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.

6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.

## Dropped from Original Framing

- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.
- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.
- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.
- **Detection as primary contribution**: Pivoted from "we detect contamination" to "we characterize benchmark properties."


## experiment_plan (with registry status)

- id: plan_001
  name: real_data_dif_mmlu
  claim: 1
  description: "Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\
    \ × 12,508 items). Data characteristics: only 37% models classifiable by family\
    \ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\
    \ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\
    \ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\
    \ split (ability-based grouping, uses all models) (c) Item filtering: run with\
    \ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\
    \ detection on all items under both cohort definitions. Proxy validation against\
    \ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\
    \ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\
    \ (item exists on web), while DIF detects cohort-differential contamination (item\
    \ behaves differently across temporal cohorts). Low concordance is EXPECTED —\
    \ DIF only catches items where contamination is differential across cohorts, not\
    \ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\
    \ items) rather than TPR (which conflates uniform vs differential contamination).\
    \ Unlabeled items (26.2%) reported separately as \"unknown\". plan_011 (semi-synthetic\
    \ injection) provides controlled ground truth to complement this proxy. (d) Within-family\
    \ confound control: run DIF within model families where both versions\n    have\
    \ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\n\
    \    below threshold — use as supplementary only. Identify additional qualifying\
    \ pairs from\n    METABENCH metadata. If DIF flags\n    items that are NOT differentially\
    \ contaminated within-family, the flag reflects capability\n    gain, not contamination.\
    \ Report: DIF flag overlap between cross-cohort and within-family\n    analyses\
    \ to disentangle contamination from capability improvement.\n(e) Domain-specificity\
    \ analysis: correlate DIF flags with MMLU subject categories to check\n    whether\
    \ flags cluster in domains with known capability jumps vs known contamination.\n\
    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\
    \ + within-family confound control + domain-specificity analysis.\n"
  priority: P0
  gpu_budget_hours: 0
  deps: []
  registry_id: ''
  status: planned
- id: plan_002
  name: rl_robustness_validation
  claim: 1
  description: "Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\
    \ - \"Alignment RL\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\
    \ produce\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\
    \ 477 such models.\n- \"Reasoning RL\" (GRPO/PPO online training) = the mechanism\
    \ that conceals contamination\n  signals. This is what Claim 1 targets. METABENCH\
    \ has almost none of these.\nDesign (Reviewer-validated): (a) SFT-only cohort\
    \ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\
    \ as mechanism control —\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\
    \ if DIF works on both\n    (a) and (b), robustness covers the full RL spectrum\n\
    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\n\
    \    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\n\
    \    (not a standalone group): DIF is group-level, so we verify that adding RL\
    \ models\n    to a cohort doesn't degrade detection. Separately, run traditional\
    \ detectors\n    (Min-K%, ConStat) on these 10-15 models individually to show\
    \ per-model degradation.\nTwo-level validation: - Group level: DIF flags same\
    \ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\
    \ detectors degrade on (c) individuals → fragile This design works even with only\
    \ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\
    \ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\
    \ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\
    \ test or permutation test for pairwise AUROC differences - TOST equivalence testing\
    \ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\
    \ exploitation power analysis: formally characterize DIF detection power as\n\
    \    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\
    \ answers\n    memorized items correctly with probability p, shrinking DIF effect\
    \ size by ~p.\n    Show detection boundary and ensemble coverage handoff point.\n"
  priority: P0
  gpu_budget_hours: 100
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003a
  name: constat_perturbation_eval
  claim: 2
  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:
    (a) Generate semantically equivalent reformulations for 200+ MMLU items using
    LLM paraphrasing (b) Compare model performance on original vs reformulated items
    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection
    power by effect size — expected strength on non-RL models, weakness on RL Even
    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.

    '
  priority: P0
  gpu_budget_hours: 80
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003b
  name: dvd_generation_variance_eval
  claim: 2
  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select
    10-15 open-weight models with inference access (b) Generate 50 responses per item
    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect
    bimodal distributions (contamination signal) (d) Characterize detection power
    for variant contamination vs verbatim contamination Standalone results provide
    variant-contamination detection baseline independent of DIF.

    '
  priority: P0
  gpu_budget_hours: 70
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_003c
  name: ensemble_fusion
  claim: 2
  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate
    per-signal thresholds on subset of items with known contamination status (b) Evaluate
    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:
    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision
    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion
    weights (5-fold); report uniform-weight baseline alongside optimized Depends on
    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  - plan_003a
  - plan_003b
  registry_id: ''
  status: planned
- id: plan_004
  name: cross_benchmark_gsm8k
  claim: 1
  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.
    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard
    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with
    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability
    and provides an independent ground truth beyond Li et al. proxy labels.

    '
  priority: P1
  gpu_budget_hours: 100
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_005
  name: bifactor_irt_equating_pilot
  claim: 3
  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains
    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt
    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files
    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH
    MMLU data (general factor + subject-specific factors) (b) Select anchor items
    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter
    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model
    rankings on original vs replaced benchmark should correlate at Spearman rho ≥
    0.95 after equating.

    '
  priority: P1
  gpu_budget_hours: 50
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_006
  name: item_generation_calibration
  claim: 3
  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use
    LLM generation with construct constraints (same subject, same cognitive level)
    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty
    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45
    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate
    on holdout model panel

    '
  priority: P1
  gpu_budget_hours: 200
  deps:
  - plan_005
  registry_id: ''
  status: planned
- id: plan_007
  name: cumulative_bayesian_dif
  claim: 1
  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).
    Simulate 4 successive benchmark administrations. Show power improvement from accumulating
    evidence: individual administration power ~0.40 → cumulative power ~0.70 after
    3 administrations for medium effects (δ=1.0).

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_008
  name: graceful_degradation_analysis
  claim: 3
  description: 'Formal analysis of benchmark validity under item replacement: (a)
    Define validity metrics (ranking stability, score reliability, construct coverage)
    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish
    theoretical bounds on validity degradation as function of replacement rate (d)
    Empirical validation using METABENCH data

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_005
  - plan_006
  registry_id: ''
  status: planned
- id: plan_009
  name: item_focused_trees
  claim: 1
  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative
    to categorical cohort DIF. Treat model release date as continuous covariate. Compare
    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary
    cohort splits, uses full model sample.

    '
  priority: P2
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_010
  name: architecture_stratified_dif
  claim: 1
  description: "Run DIF within architecture-homogeneous subpopulations to test whether\
    \ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\
    \ is removed. Dream worst-case identified this as the critical missing experiment.\
    \ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\
    \ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\
    \ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\n\
    \    vs full-population DIF from plan_001\n(d) If fit improves substantially,\
    \ conclusion is \"DIF requires architecture-homogeneous\n    populations\" — a\
    \ fixable constraint, not a fundamental limitation\nZero GPU cost (uses existing\
    \ METABENCH data). Proactive defense against worst-case reviewer concern about\
    \ unidimensional IRT misfit.\n"
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_011
  name: semi_synthetic_contamination_validation
  claim: 1
  description: "Inject known contamination into the real METABENCH response matrix\
    \ and measure DIF detection power under controlled ground truth. Addresses ground\
    \ truth circularity concern (Li et al. proxy labels measure existence, not differential\
    \ contamination). Design: (a) Select 500 items with known-clean status (no DIF\
    \ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\
    \ synthetic contamination:\n    flip responses of focal-group models from incorrect→correct\
    \ with probability p\n    (simulating contamination at varying exploitation rates)\n\
    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\
    \ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\n\
    \    (0.4-1.0), focal group size (N=40-200)\nProvides controlled ground truth\
    \ that proxy labels (Li et al.) and GSM1K cannot.\n"
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned


## registry (completed experiments)

- exp_id: mvp_dif_power_sim
  name: ''
  status: DONE
  conclusion: success
  metrics:
    best_tpr_mh: 0.6817
    best_tpr_lr: 0.6869
    best_condition: N=100_delta=1.6
    best_auc_mh: 0.9393
    best_auc_lr: 0.9593
    pass_criterion_tpr_mh: 0.0416
    pass_criterion_tpr_lr: 0.0703
    pass_criterion_condition: N=50_delta=1.0
    verdict: FAIL
    all_fpr_below_015: true
- exp_id: mvp_dif_power_sim_phase2
  name: ''
  status: DONE
  conclusion: success
  metrics:
    ets_c_tpr_N80_d14: 0.6823
    ets_c_tpr_N80_d16: 0.7223
    ets_c_tpr_N100_d14: 0.7582
    ets_c_tpr_N100_d16: 0.7966
    ets_c_fpr_range: 0.036-0.042
    best_auc_mh: 0.9254
    best_auc_lr: 0.9405
    verdict: PASS
    pass_plus_met: true
    real_param_a_mean: 1.2
    real_param_b_mean: -0.84
- exp_id: plan_001_real_data_dif_mmlu
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    temporal_ets_c_pct: 31.3
    temporal_fpr_li_clean: 0.318
    temporal_enrichment: 0.96
    ability_ets_c_pct: 2.9
    ability_fpr_li_clean: 0.027
    ability_enrichment: 1.19
    within_family_llama2v3_c_pct: 61.3
    within_family_mistral_mixtral_c_pct: 38.7
    domain_spearman_rho: 0.307
    domain_spearman_p: 0.02
    sanity_random_split_c_pct: 0.18
    temporal_ability_jaccard: 0.014
- exp_id: plan_001b_matched_ability_dif
  name: ''
  status: DONE
  conclusion: negative
  metrics: {}
- exp_id: plan_011_semi_synthetic_validation
  name: ''
  status: DONE
  conclusion: success
  metrics:
    temporal_external_tpr_p0: 0.326
    temporal_external_tpr_p03: 0.548
    temporal_external_tpr_p05: 0.834
    temporal_external_tpr_p07: 0.99
    temporal_external_tpr_p10: 1
    temporal_external_fpr: 0.314
    temporal_external_delta_tpr_p10: 0.674
    ability_external_tpr_p0: 0.498
    ability_external_tpr_p10: 0.8
    ability_external_fpr: 0.493
    ability_external_delta_tpr_p10: 0.302
    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0
    matching_variable_contamination_confirmed: true
    bug_fix: inf-delta classified as extreme DIF not class A
- exp_id: plan_012_irt_theta_conditioning
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    temporal_theta_qt20_fpr: 0.312
    temporal_theta_qt20_tpr_p05: 0.876
    temporal_theta_qt20_tpr_p10: 1
    temporal_external5_fpr: 0.314
    temporal_external5_tpr_p05: 0.834
    ability_theta_qt10_fpr: 0.093
    ability_theta_qt10_tpr_p05: 0.206
    ability_theta_qt10_tpr_p10: 0.544
    ability_theta_qt20_fpr: 0.079
    ability_theta_qt20_tpr_p05: 0.21
    ability_theta_qt20_tpr_p10: 0.544
    ability_external5_fpr: 0.493
    ability_external5_tpr_p05: 0.756
    theta_total_score_corr: 0.9986
    enrichment_all_variants: 0.97-1.00
    success_criterion_met: false
- exp_id: plan_013_q3_local_independence
  name: ''
  status: DONE
  conclusion: success
  metrics:
    within_subject_mean_q3: 0.0086
    cross_subject_mean_q3: 0.0031
    within_subject_pct_above_020: 11.3
    cross_subject_pct_above_020: 2.2
    mann_whitney_p: 2.29e-09
    worst_subject: moral_scenarios
    worst_subject_pct_above_020: 34.2
    n_items_retained: 12251
    n_items_filtered: 257
    subject_size_q3_corr: 0.2064
    subject_size_q3_p: 0.123
- exp_id: plan_014_within_subject_dif
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    business_ethics_within_c_pct: 45.2
    human_aging_within_c_pct: 33
    formal_logic_within_c_pct: 39.5
    professional_medicine_within_c_pct: 31.1
    high_school_statistics_within_c_pct: 42
    avg_within_subject_c_pct: 38.1
    avg_cross_subject_c_pct: 40.5
    avg_delta_within_vs_cross: -2.4
    sibtest_available: false
    r_available: false
    decision_zone: '>25% HIGH'
- exp_id: plan_015_bifactor_irt
  name: ''
  status: PREPARING
  conclusion: killed
  metrics: {}
- exp_id: plan_016_within_subject_semi_synthetic
  name: ''
  status: DONE
  conclusion: success
  metrics:
    within_matching:
      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)
      business_ethics_baseline_fpr: 0.563
      business_ethics_delta_tpr_p05: -0.078
      human_aging_baseline_fpr: 0.334
      human_aging_delta_tpr_p05: 0.385
      professional_medicine_baseline_fpr: 0.312
      professional_medicine_delta_tpr_p05: 0.327
      formal_logic_baseline_fpr: 0.409
      formal_logic_delta_tpr_p05: 0.457
      high_school_statistics_baseline_fpr: 0.407
      high_school_statistics_delta_tpr_p05: 0.194
      fpr_inflates_with_injection: true
      avg_fpr_inflation_p10: 0.186
    cross_matching:
      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,
        high_school_statistics)
      business_ethics_baseline_fpr: 0.533
      business_ethics_delta_tpr_p05: 0.056
      human_aging_baseline_fpr: 0.431
      human_aging_delta_tpr_p05: 0.375
      professional_medicine_baseline_fpr: 0.38
      professional_medicine_delta_tpr_p05: 0.38
      formal_logic_baseline_fpr: 0.402
      formal_logic_delta_tpr_p05: 0.543
      high_school_statistics_baseline_fpr: 0.335
      high_school_statistics_delta_tpr_p05: 0.433
      fpr_stable_across_injection: true
      delta_fpr_all_subjects: 0
    success_criterion_met: true
- exp_id: plan_017_downstream_impact
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    n_dif_items: 3918
    n_stable_items: 8590
    dif_pct: 31.3
    rho_full_vs_stable_2023: 0.998851
    rho_full_vs_stable_2024: 0.997014
    rho_full_vs_stable_all: 0.996451
    shr_full: 0.9934
    shr_stable: 0.9919
    dif_vs_random_z_mean: -14.91
    dif_vs_random_all_21_conditions_significant: true
    dif_removal_MORE_disruptive_than_random: true
    cross_cohort_ratio_dif_vs_full: 1.0919
    cross_cohort_ratio_stable_vs_full: 0.9581
    top_beneficiaries: phi-3, llama-3 derivatives
    top_hurt: mistral merges, slerp models
    max_rank_change: 851
- exp_id: plan_004_gsm8k_cross_benchmark
  name: ''
  status: DONE
  conclusion: negative
  metrics:
    step1_gsm8k_temporal_dif:
      n_items: 1319
      n_ref: 1017
      n_foc: 804
      standard_c_pct: 18.9
      external_c_pct: 47.4
      sanity_c_pct: 0.3
      standard_external_spearman: 0.926
    step2_semi_synthetic:
      standard_delta_tpr_p10: 0.818
      external_delta_tpr_p10: 0.517
    step3_gsm1k_correlation:
      n_models: 33
      n_dif_c_items: 249
      pearson_r: -0.478
      pearson_p: 0.005
      spearman_rho: -0.403
      spearman_p: 0.02
      partial_r_controlling_accuracy: -0.385
      partial_p: 0.027
      permutation_p: 0.014
      dif_c_favor_2024: 78
      dif_c_favor_2023: 171
      direction: NEGATIVE (opposite to contamination hypothesis)
      cook_d_max_model: Deepseek-math-7b-rl
      leave_one_out_r_range: -0.537 to -0.374
      robust: true

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
  "promptId": "34a8ae63-1733-4e69-806b-bb537320387d",
  "type": "user",
  "uuid": "9c8e2172-ce4e-4176-84f6-71cdc6c3e061",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T01:34:30.116Z_

```json
{
  "parentUuid": "9c8e2172-ce4e-4176-84f6-71cdc6c3e061",
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
  "uuid": "d397b79e-a6de-4fce-9f47-95a801f9236e",
  "timestamp": "2026-05-21T01:34:30.116Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T01:34:30.116Z_

```json
{
  "parentUuid": "d397b79e-a6de-4fce-9f47-95a801f9236e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "e1bc2a42-b697-424b-824c-b6595f1c9d85",
  "timestamp": "2026-05-21T01:34:30.116Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1+3+4 hold; Claim 2 (meta-critique) seen as valid but insufficiently novel. GSM1K N=33 flagged as underpowered. Borderline accept — likely needs o…",
  "leafUuid": "e1bc2a42-b697-424b-824c-b6595f1c9d85",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize benchmark instability via differential item functioning",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b"
}
```

---

### Assistant

_source line 8 · 2026-05-21T01:35:10.788Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed imagined experimental data for each "planned" experiment in the experiment_plan, based on the "median" tier definition. Let me identify which experiments are still "planned" (not yet completed):

Looking at the experiment_plan and registry:
- plan_001: status "planned" in experiment_plan, but "DONE" in registry (plan_001_real_data_dif_mmlu) → already done
- plan_002: status "planned" — rl_robustness_validation → PLANNED
- plan_003a: status "planned" — constat_perturbation_eval → PLANNED


- plan_003b through plan_011: all marked as "planned" in the experiment_plan, so I need to generate synthetic data for each of these remaining experiments following the median tier specifications.

Now I'm checking which experiments are actually already completed in the registry — plan_001, plan_001b, plan_004, plan_011 through plan_017, and the MVP simulations are all marked as done, so I should focus on the ones that are genuinely still pending. dif_power_sim_phase2 → DONE

So the truly planned (not yet executed) experiments are:
- plan_002: rl_robustness_validation
- plan_003a: constat_perturbation_eval
- plan_003b: dvd_generation_variance_eval
- plan_003c: ensemble_fusion
- plan_005: bifactor_irt_equating_pilot
- plan_006: item_generation_calibration
- plan_007: cumulative_bayesian_dif
- plan_008: graceful_degradation_analysis
- plan_009: item_focused_trees
- plan_010: architecture_stratified_dif

Wait, but the median tier definition says plan_010 has been partially characterized with modest improvements but marginal IRT fit and no successful replication beyond GSM8K. Let me work through what the median tier assumptions mean for predicting outcomes across all these planned experiments.

The core tension is: reviewers accept the core DIF methodology but want either stronger empirical validation, larger sample sizes, or clearer novelty positioning. The metric ranges I'm seeing suggest most experiments will land in a "competent but not exceptional" zone—improvements exist but are modest, and the IRT fit diagnostics remain problematic. For the RL robustness work, I'd expect to show that DIF detection holds under RL perturbations, but the effect sizes will be small and the confidence intervals wide given the sample constraints. The ensemble approach shows modest gains but nothing dramatic. Moving through the remaining plans: bifactor IRT equating is computationally strained with marginal fit on the 57-subject dataset, item generation shows moderate but insufficient correlation for practical application, Bayesian cumulative methods demonstrate theoretical promise though reviewers may be skeptical of simulation-based results, degradation analysis confirms ranking stability holds up to around 20% replacement, and continuous DIF trees yield moderate improvements.

Now I'm organizing these findings into YAML format with detailed metrics and justifications for each approach.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "e1bc2a42-b697-424b-824c-b6595f1c9d85",
  "isSidechain": false,
  "requestId": "req_011CbErWKT4kN95h3Npja1bH",
  "type": "assistant",
  "uuid": "3b1ace32-ef35-4aee-8383-ce4623e31332",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYXUjAthauMJBEyrbkaQXx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16228,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10835,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16228
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

_source line 9 · 2026-05-21T01:38:25.399Z_

```yaml
tier: median
narrative_guidance: "Soften Claim 2 from 'fundamental blind spot' to 'underappreciated methodological gap.' Add explicit caveat on 38%: instability reflects mixture of capability improvement and DIF. Reframe ρ=0.997 as measurement efficiency problem. GSM1K downgraded to 'suggestive evidence.' Position for ICLR findings track with rebuttal emphasizing semi-synthetic framework (Claim 3) as most portable contribution."
imagined_experiments:
  - name: "rl_robustness_validation"
    plan_id: "plan_002"
    description: "Validate DIF robustness to reasoning-RL models by adding 13 GRPO/PPO models to focal cohort and comparing DIF flag stability + traditional detector degradation."
    expected_results:
      n_reasoning_rl_models: 13
      n_alignment_rl_models: 477
      dif_flag_retention_ratio_sft_vs_alignment_rl: 0.91
      dif_flag_retention_ratio_sft_vs_reasoning_rl_added: 0.86
      dif_jaccard_sft_vs_rl_augmented: 0.83
      constat_auroc_sft_only: 0.72
      constat_auroc_reasoning_rl: 0.54
      mink_auroc_sft_only: 0.68
      mink_auroc_reasoning_rl: 0.49
      delong_dif_vs_constat_p: 0.087
      delong_dif_vs_mink_p: 0.042
      tost_equivalence_dif_retention_p: 0.11
      bootstrap_ci_dif_retention: [0.79, 0.93]
      power_curve_detection_boundary_p: 0.55
    result_rationale: "With only N=13 reasoning-RL models, group-level DIF remains stable (retention 0.86) because DIF operates on full cohort N≥80 and RL models are a minority. Traditional detectors degrade individually (ConStat AUROC 0.72→0.54, Min-K% 0.68→0.49) as expected from NLL gap contraction. However, DeLong test for DIF vs ConStat is marginal (p=0.087) — underpowered at N=13. TOST equivalence fails (p=0.11 > 0.05), so reviewers can't rule out that DIF retention is coincidental. Median-tier outcome: suggestive robustness evidence insufficient for strong claim. Reviewers note 'N=13 is too few for definitive comparison; interesting pilot but not convincing.' Detection boundary at p=0.55 means DIF misses partial exploitation below 55%, which is a meaningful gap."
    tables:
      - title: "Table: DIF vs Traditional Detector Comparison Under RL"
        columns: ["Detector", "AUROC (SFT)", "AUROC (Alignment-RL)", "AUROC (Reasoning-RL)", "Δ", "95% CI"]
        rows:
          - ["DIF (MH)", "N/A (group)", "N/A (group)", "retention=0.86", "-0.14", "[−0.21, −0.07]"]
          - ["ConStat", "0.72", "0.69", "0.54", "-0.18", "[−0.31, −0.05]"]
          - ["Min-K%", "0.68", "0.64", "0.49", "-0.19", "[−0.33, −0.06]"]
    figures_description:
      - "Figure: Detection power as function of exploitation rate p ∈ [0.4, 1.0]. DIF power curve shows detection boundary at p≈0.55 (TPR>0.5). Below p=0.55, DIF effect size shrinks below δ=1.4 threshold. Shaded region shows ensemble coverage handoff zone (p=0.4-0.6) where ConStat on non-RL models still operates."
      - "Figure: Jaccard similarity of DIF flag sets across cohort compositions (SFT-only, +alignment-RL, +reasoning-RL). Box plots over 100 bootstrap resamples showing overlap stability."
    analysis: "Result is directionally supportive but statistically underpowered. DIF shows robustness (86% flag retention) while traditional detectors degrade, consistent with theoretical prediction. However, TOST equivalence failure and marginal DeLong test mean this cannot be claimed as definitive proof. In median tier, reviewers acknowledge the logic but request either (a) more reasoning-RL models when available, or (b) formal power analysis showing what N would be needed for conclusive evidence. The detection boundary at p=0.55 is an honest limitation — partial exploitation remains a blind spot. Best positioned as 'preliminary evidence consistent with theoretical robustness prediction' in limitations/future work, not as a standalone claim."

  - name: "constat_perturbation_eval"
    plan_id: "plan_003a"
    description: "Independent ConStat-style perturbation testing on 250 MMLU items with LLM-generated semantic reformulations across 15 models."
    expected_results:
      n_items_reformulated: 248
      n_models_tested: 15
      mean_performance_drop_original_vs_reformulated: 0.034
      constat_detection_rate_fdr_010: 0.127
      constat_detection_rate_fdr_005: 0.089
      constat_auroc_vs_li_labels: 0.61
      constat_auroc_non_rl_models: 0.67
      constat_auroc_rl_models: 0.52
      mean_reformulation_quality_score: 0.82
      semantic_equivalence_human_check: 0.91
      effect_size_detected_items_cohens_d: 0.73
    result_rationale: "ConStat operates at per-model level detecting performance drops on reformulations. On non-RL models (where memorization manifests as sensitivity to surface form), detection rate is moderate (12.7% at FDR=0.10). RL models show minimal surface-form sensitivity (AUROC 0.52, near chance) because PPO/GRPO training generalizes beyond verbatim patterns. The 3.4% mean performance drop across all items is small because most items aren't contaminated — only a subset shows the characteristic bimodal response pattern. AUROC vs Li et al. labels is weak (0.61) because, as established, web-overlap is a mismatched ground truth for item-level detection. In median tier, this provides a useful baseline comparison confirming ConStat's complementary detection space (non-RL, surface-form memorization) but doesn't change the paper's core narrative."
    tables:
      - title: "Table: ConStat Detection Rates by Model Category"
        columns: ["Model Category", "N Models", "Detection Rate (FDR=0.10)", "Mean Effect Size (d)"]
        rows:
          - ["SFT-only", "6", "0.153", "0.81"]
          - ["Alignment-RL (DPO)", "5", "0.134", "0.69"]
          - ["Reasoning-RL (GRPO)", "4", "0.071", "0.42"]
    figures_description:
      - "Figure: Distribution of per-item performance drops (original − reformulated) across 248 items. Bimodal distribution visible: bulk of items near zero, contaminated tail at Δ>0.15."
    analysis: "ConStat independently validates the complementary detection space claim — it works where DIF doesn't (per-model, small effects) but fails where DIF succeeds (RL-robust, group-differential). However, in median tier this experiment is not included in the main paper because plan_003c (ensemble) was never fully executed and the ensemble narrative (original Claim 2) was dropped during the pivot. ConStat results go to appendix as supplementary comparison, supporting the 'detection methods are complementary' theme without being a core contribution."

  - name: "dvd_generation_variance_eval"
    plan_id: "plan_003b"
    description: "DVD generation variance detection on 12 open-weight models with 50 generations per item at T=0.8 on 300 MMLU items."
    expected_results:
      n_models_tested: 12
      n_items_per_model: 300
      n_generations_per_item: 50
      temperature: 0.8
      bimodal_detection_rate: 0.094
      dvd_auroc_vs_dif_flags: 0.58
      dvd_auroc_verbatim_contamination: 0.71
      dvd_auroc_variant_contamination: 0.63
      mean_generation_variance_clean_items: 0.34
      mean_generation_variance_contaminated_items: 0.18
      gpu_hours_used: 62
      inference_failures: 3
    result_rationale: "DVD detects contamination via low generation variance (memorized items → consistently correct). Detection rate of 9.4% reflects that most contamination on MMLU is not verbatim memorization but pattern-level familiarity, which still produces moderate variance. AUROC for verbatim contamination (0.71) is better than variant (0.63) because verbatim produces clearer bimodal distributions. Correlation with DIF flags is weak (AUROC 0.58) because DIF and DVD measure fundamentally different signals: DIF measures cross-group differential, DVD measures within-model consistency. In median tier, DVD provides another complementary signal but is expensive (62 GPU-hours for 12 models × 300 items) and the low detection rate limits practical utility. The 3 inference failures (OOM on larger models) highlight scalability concerns."
    tables:
      - title: "Table: DVD Detection Characteristics"
        columns: ["Contamination Type", "AUROC", "Detection Rate (threshold=0.10)", "Mean Variance Reduction"]
        rows:
          - ["Verbatim", "0.71", "0.134", "0.21"]
          - ["Variant/Paraphrase", "0.63", "0.072", "0.12"]
          - ["None (clean)", "—", "0.031 (FPR)", "—"]
    figures_description:
      - "Figure: Generation variance distributions for DIF-flagged vs DIF-stable items across 12 models. Modest leftward shift for DIF-flagged items but heavy overlap, confirming weak correspondence between group-differential (DIF) and within-model (DVD) signals."
    analysis: "DVD results are informative but not compelling enough for inclusion in the pivoted paper. The weak correspondence with DIF flags (AUROC 0.58) actually supports the paper's narrative that different detection methods capture different contamination mechanisms. However, the high GPU cost and low detection rates make this a poor cost-benefit trade for the characterization paper. In median tier, this remains in supplementary material at best. The result is useful for future ensemble work but doesn't strengthen any of the four core claims."

  - name: "ensemble_fusion"
    plan_id: "plan_003c"
    description: "Attempt to fuse DIF + ConStat + DVD into multi-signal ensemble with majority voting and weighted fusion."
    expected_results:
      ensemble_2of3_precision: 0.41
      ensemble_2of3_recall: 0.23
      ensemble_weighted_auroc: 0.66
      ensemble_fpr: 0.087
      individual_dif_auroc: 0.62
      individual_constat_auroc: 0.61
      individual_dvd_auroc: 0.58
      cross_val_weight_variance: 0.15
      uniform_vs_optimized_auroc_gap: 0.03
      coverage_overlap_dif_constat: 0.31
      coverage_overlap_dif_dvd: 0.22
      coverage_overlap_constat_dvd: 0.38
    result_rationale: "Ensemble shows modest improvement over individuals (AUROC 0.66 vs best individual 0.62) but the improvement is not dramatic because the three signals have limited overlap — they detect different contamination mechanisms with low redundancy. 2-of-3 majority voting has good precision (0.41) but very low recall (0.23) because few items trigger multiple detectors simultaneously. FPR<0.10 criterion is met (0.087) but only because the ensemble is very conservative. Cross-validation weight variance is high (0.15) indicating instability — different folds produce different optimal weights, suggesting the calibration set is too small for reliable fusion. In median tier, this experiment is effectively abandoned during the pivot away from 'detection methods' framing. The ensemble was the core of original Claim 2 which is now dropped."
    tables:
      - title: "Table: Ensemble vs Individual Detector Performance"
        columns: ["Method", "AUROC", "Precision@FPR=0.10", "Coverage (items flagged)"]
        rows:
          - ["DIF (MH)", "0.62", "0.38", "31.3%"]
          - ["ConStat", "0.61", "0.34", "12.7%"]
          - ["DVD", "0.58", "0.29", "9.4%"]
          - ["Ensemble (2-of-3)", "0.66", "0.41", "6.8%"]
          - ["Ensemble (weighted)", "0.66", "0.43", "8.2%"]
    figures_description:
      - "Figure: Venn diagram showing overlap of flagged items across three detectors. DIF flags ~3,900 items, ConStat ~380, DVD ~280. Triple overlap: 47 items. Confirms complementary rather than redundant coverage."
    analysis: "Ensemble fusion fails to produce a compelling unified detector because the three methods target different contamination mechanisms with minimal overlap. This is actually the correct scientific conclusion — it supports the pivot away from 'unified contamination detector' toward 'characterization of differential item functioning.' In median tier, plan_003c is reported as a negative result in the appendix: 'ensemble approaches require contamination mechanisms to be partially redundant; when mechanisms are orthogonal, fusion provides minimal lift.' This negative result paradoxically supports the paper's reframing: DIF measures something fundamentally different from per-model detectors."

  - name: "bifactor_irt_equating_pilot"
    plan_id: "plan_005"
    description: "Fit bifactor IRT model (general + 57 subject-specific factors) to METABENCH MMLU response matrix and attempt test equating via anchor items."
    expected_results:
      bifactor_converged: true
      n_iterations_to_converge: 847
      general_factor_variance_explained: 0.62
      mean_subject_factor_variance: 0.14
      rmsea_bifactor: 0.041
      cfi_bifactor: 0.87
      n_anchor_items_selected: 1842
      anchor_stability_criterion: "DIF A-class across all cohort pairs"
      equated_rho_original_vs_replaced: 0.93
      equated_rho_anchor_only: 0.97
      replacement_item_calibration_rmse: 0.38
      kim_kolen_fixed_param_fit: "acceptable for 68% of replacement items"
    result_rationale: "Bifactor model converges but with marginal fit (CFI=0.87 < 0.90 threshold, RMSEA=0.041 acceptable). The 57-subject structure is too fine-grained for the model to fit cleanly — general factor explains 62% of variance, individual subjects contribute 14% on average, leaving ~24% residual. Anchor item selection yields 1,842 stable items (14.7% of total), sufficient for equating but a relatively small anchor set. Equated score correlation (ρ=0.93) falls below the target ρ≥0.95, primarily because replacement item calibration via fixed-parameter approach has high RMSE (0.38) — the item parameters estimated on one cohort don't transfer perfectly. In median tier, this is a 'proof of concept with caveats' — equating is feasible in principle but the bifactor model's marginal fit and the below-target equated correlation weaken the regeneration claim. Reviewers note 'interesting pilot but ρ=0.93 suggests non-trivial information loss during equating.'"
    tables:
      - title: "Table: Bifactor Model Fit Indices"
        columns: ["Index", "Value", "Acceptable", "Good"]
        rows:
          - ["RMSEA", "0.041", "< 0.08 ✓", "< 0.05 ✓"]
          - ["CFI", "0.87", "< 0.90 ✗", "≥ 0.95 ✗"]
          - ["TLI", "0.84", "< 0.90 ✗", "≥ 0.95 ✗"]
          - ["SRMR", "0.063", "< 0.08 ✓", "< 0.05 ✗"]
    figures_description:
      - "Figure: Scree plot showing general factor dominant (eigenvalue=3,847) followed by 57 subject-specific factors with eigenvalues 12-180. Clear elbow after general factor confirms unidimensional dominance with multidimensional residual structure."
      - "Figure: Scatter plot of equated vs original model scores (N=5,219). Correlation ρ=0.93, with visible heteroscedasticity — low-ability models show more equating error than high-ability models."
    analysis: "Bifactor equating is technically feasible but falls short of production quality. The marginal model fit (CFI=0.87) reflects the known challenge that 57 MMLU subjects create a high-dimensional latent space poorly captured by a single general factor. In median tier, this experiment is reported honestly as 'pilot demonstration with limitations' — it shows the path to benchmark regeneration exists but requires better IRT models (multidimensional, or domain-clustered bifactor). Reviewers would likely say 'interesting future direction but not mature enough for a contribution claim.' This supports the paper's positioning of equating as future work rather than a current claim. Plan_014 already showed within-subject C%=38.1%, so the bifactor pre-check approach for reducing DIF was killed — this equating pilot inherits that limitation."

  - name: "item_generation_calibration"
    plan_id: "plan_006"
    description: "Generate replacement items for 200 DIF-flagged MMLU questions using LLM generation with construct constraints, calibrate via student simulation."
    expected_results:
      n_items_generated: 200
      n_items_passing_quality_filter: 156
      difficulty_correlation_prompt_based: 0.31
      difficulty_correlation_student_sim: 0.64
      discrimination_correlation: 0.42
      construct_alignment_human_rating: 0.78
      holdout_panel_correlation: 0.58
      mean_difficulty_mae: 0.18
      pct_items_within_05_difficulty: 0.43
      gpu_hours_used: 187
    result_rationale: "Item generation produces grammatically correct, construct-aligned questions (78% human-rated alignment) but calibration accuracy is moderate. Student simulation improves difficulty prediction (ρ=0.64) over prompt-based targeting (ρ=0.31), consistent with literature (arXiv 2601.09953 reports r=0.75-0.82 — our lower value reflects MMLU's broader domain coverage vs focused benchmarks). Only 43% of generated items fall within ±0.5 difficulty of the target, meaning majority would need iterative recalibration. Discrimination correlation is lower (0.42) because item discrimination depends on subtle psychometric properties harder to control via generation. In median tier, this demonstrates that LLM item generation is a viable but immature pipeline — insufficient for automated benchmark regeneration without human-in-the-loop validation. Reviewers would flag the 58% holdout correlation as 'items don't transfer well to unseen models.'"
    tables:
      - title: "Table: Calibration Method Comparison"
        columns: ["Method", "Difficulty ρ", "Discrimination ρ", "% Within ±0.5 Target"]
        rows:
          - ["Prompt-based targeting", "0.31", "0.28", "0.24"]
          - ["Student simulation (5 students)", "0.64", "0.42", "0.43"]
          - ["Student simulation (20 students)", "0.68", "0.45", "0.47"]
    figures_description:
      - "Figure: Predicted vs actual item difficulty for 156 generated items. Student simulation shows tighter scatter (ρ=0.64) vs prompt-based (ρ=0.31), but both show ceiling/floor compression — hardest and easiest items are poorly calibrated."
    analysis: "Item generation calibration shows promise but not maturity. The gap between student simulation performance here (ρ=0.64) and published results (r=0.75-0.82) likely reflects MMLU's domain breadth — calibrating 'abstract algebra' items requires different student models than 'clinical knowledge.' In median tier, this supports the future work framing: 'automated benchmark regeneration is feasible with improved calibration pipelines' but is not ready as a standalone contribution. Combined with plan_005's marginal equating results, the regeneration storyline (original Claim 3) remains firmly in future work territory. The 187 GPU-hours for 200 items also highlights cost concerns for full-scale deployment."

  - name: "cumulative_bayesian_dif"
    plan_id: "plan_007"
    description: "Simulate cumulative Bayesian DIF with informative priors from prior administrations over 4 successive benchmark waves."
    expected_results:
      single_administration_power_delta10: 0.41
      cumulative_2_administrations_power: 0.54
      cumulative_3_administrations_power: 0.67
      cumulative_4_administrations_power: 0.74
      single_administration_fpr: 0.042
      cumulative_4_fpr: 0.051
      power_gain_per_administration: [0.13, 0.13, 0.07]
      convergence_plateau: "~4 administrations"
      bayes_factor_threshold: 3.0
      pct_items_bf_gt_3_after_4_admin: 0.68
    result_rationale: "Cumulative Bayesian approach shows expected power improvement (0.41→0.74 over 4 administrations for medium effects δ=1.0) as evidence accumulates. This is a well-established psychometric result (Sinharay 2006) applied to the LLM benchmark setting. FPR remains controlled (0.051) because Bayesian shrinkage prevents false alarms from accumulating. Power gains show diminishing returns (0.13, 0.13, 0.07) — the fourth administration adds less because most detectable items are already identified. In median tier, this is simulation-only (no real longitudinal MMLU data exists with 4 temporal waves), so reviewers note 'theoretically sound but purely simulated — would need actual longitudinal benchmark deployment to validate.' Positioned as future monitoring methodology, not a current empirical contribution."
    tables:
      - title: "Table: Cumulative Power by Effect Size"
        columns: ["Administrations", "δ=0.8", "δ=1.0", "δ=1.2", "δ=1.4"]
        rows:
          - ["1", "0.24", "0.41", "0.55", "0.68"]
          - ["2", "0.37", "0.54", "0.69", "0.81"]
          - ["3", "0.48", "0.67", "0.79", "0.89"]
          - ["4", "0.54", "0.74", "0.84", "0.92"]
    figures_description:
      - "Figure: Power accumulation curves across 4 administrations, stratified by effect size. Clear sigmoid shape with plateau around administration 3-4. Dashed line at TPR=0.50 shows that medium effects (δ=1.0) become reliably detectable only after 2+ administrations."
    analysis: "Bayesian cumulative DIF is theoretically elegant and directly addresses the power limitation identified in plan_001 (single-shot DIF only detects large effects δ≥1.4). However, it's purely simulation-based in the current paper because METABENCH provides only a single temporal snapshot (2023 vs 2024-H1), not 4 successive administrations. In median tier, reviewers appreciate the methodological contribution but note 'this requires longitudinal benchmark infrastructure that doesn't yet exist.' Best positioned as a concrete recommendation for benchmark maintainers: 'if you collect response matrices over time, here's how to accumulate evidence of item degradation.' Strengthens the 'measurement science for ML benchmarks' narrative without requiring new empirical data."

  - name: "graceful_degradation_analysis"
    plan_id: "plan_008"
    description: "Formal analysis of benchmark validity under progressive item replacement (5% to 50%) using METABENCH empirical data."
    expected_results:
      rho_5pct_replacement: 0.998
      rho_10pct_replacement: 0.996
      rho_20pct_replacement: 0.991
      rho_50pct_replacement: 0.972
      reliability_alpha_full: 0.943
      reliability_alpha_50pct_replaced: 0.921
      construct_coverage_5pct: 0.97
      construct_coverage_50pct: 0.84
      theoretical_bound_rho_vs_replacement_rate: "ρ ≥ 1 - 1.3r (r = replacement fraction)"
      critical_replacement_threshold: "~35% before ρ < 0.98"
      dif_targeted_vs_random_replacement_rho_gap: 0.008
    result_rationale: "Progressive replacement analysis reveals extreme ranking robustness — even 50% item replacement maintains ρ=0.972. This is consistent with plan_017's finding that ρ=0.997 after removing 31% DIF items. MMLU's 12,508 items provide massive redundancy; any subset of ~6,000+ items preserves relative model ordering. Reliability (Cronbach's α) degrades more noticeably (0.943→0.921 at 50%) because replacement items have higher calibration error. Construct coverage (proportion of original 57 subjects adequately sampled) drops to 0.84 at 50% because some small subjects (N<50 items) lose coverage entirely. The near-linear relationship ρ ≥ 1 - 1.3r holds empirically up to r=0.4. In median tier, this result cuts both ways: it shows equating is feasible (replacements don't destroy validity) but also undermines urgency (if rankings are so stable, why bother replacing items?). Reviewers invoke the 'so what' critique: ρ=0.997→0.972 is still excellent."
    tables:
      - title: "Table: Validity Metrics Under Progressive Replacement"
        columns: ["Replacement %", "Spearman ρ", "Cronbach α", "Construct Coverage", "Max Rank Δ"]
        rows:
          - ["0% (baseline)", "1.000", "0.943", "1.00", "0"]
          - ["5%", "0.998", "0.941", "0.97", "23"]
          - ["10%", "0.996", "0.938", "0.95", "47"]
          - ["20%", "0.991", "0.932", "0.91", "112"]
          - ["50%", "0.972", "0.921", "0.84", "341"]
    figures_description:
      - "Figure: Ranking stability (ρ) vs replacement fraction. Near-linear degradation with empirical bound overlaid. Shaded confidence band from 100 bootstrap resamples. Vertical dashed line at 31% (observed DIF percentage) showing ρ=0.993."
    analysis: "Graceful degradation analysis primarily serves as supplementary validation for plan_017's core finding. It formalizes what the ρ=0.997 result already implies: MMLU has enormous measurement redundancy. In median tier, this becomes a double-edged sword — reviewers use it to argue 'if the benchmark is so redundant, the 38% instability finding is merely academic, not practically concerning.' The paper's rebuttal must be: 'redundancy protects rankings but masks that 31% of items carry disproportionate discriminative information (z=-8 to -49σ from plan_017). Efficiency, not validity, is the real concern.' The 35% critical threshold aligns with the observed 38% DIF rate — we're near the edge where replacement starts to matter, even if we haven't crossed it yet."

  - name: "item_focused_trees"
    plan_id: "plan_009"
    description: "Implement Item-Focused Trees treating model release date as continuous covariate, comparing detection power and flexibility vs categorical temporal DIF."
    expected_results:
      n_items_analyzed: 12508
      ift_c_pct_equivalent: 28.4
      ift_vs_categorical_jaccard: 0.72
      ift_unique_flags: 0.08
      categorical_unique_flags: 0.12
      ift_split_point_median: "2023-09-15"
      ift_nonlinear_items_pct: 0.14
      ift_power_gain_vs_categorical: 0.03
      computation_time_hours: 4.2
    result_rationale: "Item-Focused Trees detect 28.4% of items as exhibiting DIF along the release-date continuum (vs 31.3% for categorical temporal split). Jaccard overlap of 0.72 with categorical DIF shows substantial agreement — most items flagged by IFT are also flagged by categorical MH, confirming the temporal split was reasonable. IFT identifies 8% unique items (gradual drift not captured by binary split) and misses 12% that categorical catches (items with sharp discontinuity better detected by group contrast). 14% of items show nonlinear DIF trajectories (early models and late models both struggle, middle cohort performs differently). Power gain is minimal (+0.03) because the binary temporal split already captures the primary contrast. In median tier, IFT provides methodological sophistication but minimal empirical gain — reviewers appreciate the robustness check ('arbitrary temporal split didn't distort results') but note 'the continuous approach doesn't change your main finding.'"
    tables:
      - title: "Table: IFT vs Categorical DIF Comparison"
        columns: ["Method", "Items Flagged", "Unique Flags", "Overlap (Jaccard)", "Computation Time"]
        rows:
          - ["Categorical MH (2023 vs 2024-H1)", "31.3%", "12%", "—", "0.3 hours"]
          - ["Item-Focused Trees (continuous date)", "28.4%", "8%", "0.72", "4.2 hours"]
    figures_description:
      - "Figure: Example IFT splits for 4 items showing different DIF trajectories. (a) Sharp discontinuity at 2023-11 (well-detected by categorical), (b) Gradual linear drift (better detected by IFT), (c) U-shaped nonlinear pattern (only detected by IFT), (d) No DIF (flat)."
    analysis: "IFT serves primarily as a robustness check confirming that the categorical temporal split was not misleading. The 72% overlap validates the simpler approach while the 14% nonlinear items are methodologically interesting but don't change conclusions. In median tier, this goes to supplementary material as 'sensitivity analysis: continuous treatment of release date produces concordant results (Jaccard=0.72), with 14% of items showing nonlinear trajectories warranting future investigation.' Reviewers may note that IFT is more principled but the limited power gain doesn't justify the complexity for the main paper. Most useful as a reviewer rebuttal resource: 'our arbitrary temporal split is validated by the continuous approach.'"

  - name: "architecture_stratified_dif"
    plan_id: "plan_010"
    description: "Run DIF within decoder-only architecture subpopulation to test whether IRT fit improves and spurious DIF reduces when architecture heterogeneity is removed."
    expected_results:
      n_decoder_only_models: 3412
      n_ref_decoder_only_2023: 891
      n_foc_decoder_only_2024h1: 523
      decoder_only_c_pct: 28.2
      full_population_c_pct: 31.3
      delta_c_pct: -3.1
      rmsea_full_population: 0.089
      rmsea_decoder_only: 0.067
      cfi_full_population: 0.78
      cfi_decoder_only: 0.83
      tli_decoder_only: 0.81
      srmr_decoder_only: 0.058
      jaccard_decoder_vs_full: 0.81
      fpr_decoder_only: 0.282
      tpr_decoder_only_semi_synthetic_p05: 0.79
      delta_tpr_decoder_only: 0.508
    result_rationale: "Architecture stratification reduces C% from 31.3% to 28.2% — a modest 3.1pp improvement, not the dramatic reduction that would indicate architecture heterogeneity was the primary driver of spurious DIF. IRT fit improves marginally (RMSEA 0.089→0.067, from 'poor' to 'marginal'; CFI 0.78→0.83, still below 0.90 'acceptable'). This confirms that architecture mixing contributes some model misfit but is not the dominant source — the remaining 28.2% DIF reflects genuine temporal item instability within decoder-only models. Jaccard overlap of 0.81 with full-population flags confirms most DIF items are flagged regardless of population composition. In median tier, this is the 'modest improvement' outcome specified: reviewers acknowledge architecture stratification helps but note 'RMSEA=0.067 and CFI=0.83 are still below standard fit thresholds, suggesting deeper structural issues with unidimensional IRT on MMLU.'"
    tables:
      - title: "Table: IRT Fit Comparison: Full Population vs Decoder-Only"
        columns: ["Metric", "Full Population", "Decoder-Only", "Improvement", "Acceptable Threshold"]
        rows:
          - ["RMSEA", "0.089", "0.067", "−0.022", "< 0.05"]
          - ["CFI", "0.78", "0.83", "+0.05", "≥ 0.90"]
          - ["TLI", "0.75", "0.81", "+0.06", "≥ 0.90"]
          - ["SRMR", "0.074", "0.058", "−0.016", "< 0.05"]
          - ["C% (ETS)", "31.3%", "28.2%", "−3.1pp", "—"]
    figures_description:
      - "Figure: Item-level DIF effect sizes (|Δ_MH|) for decoder-only vs full population. Scatter plot showing high correlation (r=0.91) with slight downward shift for decoder-only, confirming most DIF persists within homogeneous architecture."
      - "Figure: RMSEA distribution across 57 MMLU subjects for decoder-only population. Most subjects in 0.05-0.08 range (marginal fit), with moral_scenarios and professional_law as outliers (>0.10)."
    analysis: "Plan_010 is the proactive defense experiment against the 'IRT model misfit' reviewer concern. In median tier, the result is honest but not fully reassuring: architecture stratification helps (3.1pp C% reduction, RMSEA improvement) but doesn't solve the fundamental issue that unidimensional IRT is a simplification for 57-subject MMLU. The paper frames this as: 'architecture stratification provides modest improvement, confirming that population homogeneity is beneficial but not sufficient — multidimensional IRT or domain-specific modeling remain future directions.' Reviewers likely say 'you've shown the problem is partially addressable but haven't solved it — reframe 38% as upper bound, 28% as lower bound under controlled conditions.' This is consistent with median-tier narrative guidance: 'instability reflects a mixture' with explicit bounds."
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3b1ace32-ef35-4aee-8383-ce4623e31332",
  "isSidechain": false,
  "requestId": "req_011CbErWKT4kN95h3Npja1bH",
  "type": "assistant",
  "uuid": "2a457d51-5c75-4442-9406-8fbf2eb5d4d2",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01SYXUjAthauMJBEyrbkaQXx",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16228,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10835,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16228,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10835,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16228,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16228
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1+3+4 hold; Claim 2 (meta-critique) seen as valid but insufficiently novel. GSM1K N=33 flagged as underpowered. Borderline accept — likely needs o…",
  "leafUuid": "2a457d51-5c75-4442-9406-8fbf2eb5d4d2",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize benchmark instability via differential item functioning",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Claims 1+3+4 hold; Claim 2 (meta-critique) seen as valid but insufficiently novel. GSM1K N=33 flagged as underpowered. Borderline accept — likely needs o…",
  "leafUuid": "2a457d51-5c75-4442-9406-8fbf2eb5d4d2",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Characterize benchmark instability via differential item functioning",
  "sessionId": "4e44d1b7-fd1c-4ed7-af50-7fa78a30962b"
}
```

---
