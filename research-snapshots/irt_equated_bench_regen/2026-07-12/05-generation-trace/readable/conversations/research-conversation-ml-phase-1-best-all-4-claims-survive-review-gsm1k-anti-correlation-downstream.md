# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：All 4 claims survive review; GSM1K anti-correlation + downstream z-scores co

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/f449a4a6-65be-4cd0-9aef-f871609ad8db.jsonl`
- **Structured JSON:** [`44ad755f972db2c0b90e.json`](../../sessions/44/44ad755f972db2c0b90e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T01:30:34.710Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T01:30:34.710Z",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：All 4 claims survive review; GSM1K anti-correlation + downstream z-scores convince reviewers DIF reveals genuine structural insight. ICLR main conference oral/spotlight territory.\n核心假设：['Reviewers accept 38% instability as substantive empirical finding even without causal decomposition (contamination vs capability)', \"Ground truth meta-critique lands as 'important blind spot the field overlooked', not 'obvious in hindsight'\", 'GSM1K anti-correlation r=−0.478 (N=33) accepted as cross-benchmark validation despite small N', 'Downstream z=−8 to −49σ convinces reviewers DIF items are informationally special, not just noisy', 'plan_010 (architecture-stratified) shows decoder-only C% drops to 20-25%, proving architecture confounding is controllable', 'At least one additional benchmark replication (ARC or HellaSwag via METABENCH) confirms generalizability']\n关键指标范围：{'expected_reviewer_avg_score': [6.5, 7.5], 'architecture_stratified_c_pct': [18, 25], 'architecture_stratified_irt_rmsea': [0.02, 0.05], 'additional_benchmark_delta_tpr': [0.4, 0.9], 'gsm1k_correlation_if_bootstrapped_ci': [-0.7, -0.3], 'reviewer_novelty_score': [6, 8], 'reviewer_significance_score': [6, 8]}\n叙事方向：Original framing holds: \"Psychometric DIF reveals that 38% of MMLU items are functionally unstable, the field's ground truth validation is fundamentally mismatched, and DIF items concentrate discriminative signal that contamination cannot fake.\" Four claims presented at full strength. Architecture stratification shows the method is refinable (not broken), and cross-benchmark replication on GSM8K+additional benchmarks demonstrates generalizability. Growing Pains complementarity positioning accepted. Paper reads as a definitive characterization study that changes how the community thinks about benchmark temporal validity.\n\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: Post-pivot framing: characterization + methodology paper, NOT methods paper. Key new evidence since last Dream: (1) GSM8K cross-benchmark replication ΔTPR=+0.818, (2) GSM1K contamination gap anti-correlation r=−0.478 — DIF captures capability-discriminative items that contamination can't fake, (3) downstream impact z=-8 to -49σ confirming DIF items are discriminative carriers. Assess whether these strengthen ICLR main conference viability vs findings track.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — we cannot decompose 38% into contamination vs capability improvement\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\" — mutual value positioning\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T01:30:34.715Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T01:30:34.715Z",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T01:30:34.741Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：All 4 claims survive review; GSM1K anti-correlation + downstream z-scores convince reviewers DIF reveals genuine structural insight. ICLR main conference oral/spotlight territory.
核心假设：['Reviewers accept 38% instability as substantive empirical finding even without causal decomposition (contamination vs capability)', "Ground truth meta-critique lands as 'important blind spot the field overlooked', not 'obvious in hindsight'", 'GSM1K anti-correlation r=−0.478 (N=33) accepted as cross-benchmark validation despite small N', 'Downstream z=−8 to −49σ convinces reviewers DIF items are informationally special, not just noisy', 'plan_010 (architecture-stratified) shows decoder-only C% drops to 20-25%, proving architecture confounding is controllable', 'At least one additional benchmark replication (ARC or HellaSwag via METABENCH) confirms generalizability']
关键指标范围：{'expected_reviewer_avg_score': [6.5, 7.5], 'architecture_stratified_c_pct': [18, 25], 'architecture_stratified_irt_rmsea': [0.02, 0.05], 'additional_benchmark_delta_tpr': [0.4, 0.9], 'gsm1k_correlation_if_bootstrapped_ci': [-0.7, -0.3], 'reviewer_novelty_score': [6, 8], 'reviewer_significance_score': [6, 8]}
叙事方向：Original framing holds: "Psychometric DIF reveals that 38% of MMLU items are functionally unstable, the field's ground truth validation is fundamentally mismatched, and DIF items concentrate discriminative signal that contamination cannot fake." Four claims presented at full strength. Architecture stratification shows the method is refinable (not broken), and cross-benchmark replication on GSM8K+additional benchmarks demonstrates generalizability. Growing Pains complementarity positioning accepted. Paper reads as a definitive characterization study that changes how the community thinks about benchmark temporal validity.


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
  "promptId": "eb19a1ec-d8b0-479d-bd96-de172ae37ddb",
  "type": "user",
  "uuid": "5b81540c-65d6-4cc9-8787-c0d8ce290be1",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T01:30:34.738Z_

```json
{
  "parentUuid": "5b81540c-65d6-4cc9-8787-c0d8ce290be1",
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
  "uuid": "103ed266-485a-41a0-949f-499af17c5107",
  "timestamp": "2026-05-21T01:30:34.738Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T01:30:34.739Z_

```json
{
  "parentUuid": "103ed266-485a-41a0-949f-499af17c5107",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "d13c122a-d11d-4ca7-a82f-30cdd03d0a80",
  "timestamp": "2026-05-21T01:30:34.739Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims survive review; GSM1K anti-correlation + downstream z-scores convince reviewers DIF reveals genuine structural insight. ICLR main conference o…",
  "leafUuid": "d13c122a-d11d-4ca7-a82f-30cdd03d0a80",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF benchmark characterization for ICLR 2027",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db"
}
```

---

### Assistant

_source line 8 · 2026-05-21T01:31:52.990Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "best" tier scenario. Let me identify which experiments are still "planned" (not yet completed):

Looking at the experiment_plan and registry:

1. plan_001 - status: planned in experiment_plan, but DONE in registry (plan_001_real_data_dif_mmlu)
2. plan_002 - status: planned, not in registry → PLANNED
3. plan_003a - status: planned, not in registry → PLANNED


4. plan_003b through plan_003c - both planned and not yet in registry
5. plan_004 - already completed in the registry
6. plan_005 through plan_009 - all marked as planned with no registry entries yet
7. plan_010 - appears to be planned but the status line is cut off
8. plan_011 - planned in the experiment_plan but already marked done in the registry

So I need to identify which experiments are still in planned status and haven't been completed. Looking back at the user's request, they want detailed data for each planned experiment in the experiment_plan. Since all experiments start with status: planned, I should focus on the ones that haven't been marked as done in the registry yet. That gives me plan_002, plan_003a, plan_003b, plan_003c, plan_005 through plan_010 as the ones needing predictions.

Now I'm reviewing which experiments have already been completed in the registry - there's quite a list of them including plan_001, plan_001b, plan_011 through plan_017, plan_004, and the MVP simulation phases. So the remaining planned experiments that still need work are...

Looking at the ones that haven't been done yet - plan_002 through plan_010 - and the user wants me to generate imagined results for each assuming they hit the "best" tier, meaning ICLR oral or spotlight quality across all four evaluation metrics.

I need to keep in mind the specific target ranges for the best tier: architecture_stratified_c_pct should drop to 20-25%, IRT RMSEA between 0.02-0.05, additional benchmark TPR delta hitting 0.4-0.9, GSM1K correlation bootstrapped CI in the -0.7 to -0.3 range, and reviewer novelty and significance scores both 6-8. Some of these experiments like the ensemble variants got consolidated, so I should focus on the ones that are actually still in scope.

For plan_002 on RL robustness, the original framing noted insufficient sample size and limitations, but in a best-case scenario we'd have enough reasoning-RL models to show DIF remains stable while traditional detectors degrade. That could become supplementary evidence even if it wasn't the main claim.

Plans 003a/b/c were never executed and are marked as future work. Plans 005 and 006 got dropped entirely—the bifactor approach was killed by an earlier pre-check, and plan 015 depended on it. Plan 007 is secondary priority but still viable. Plan 009 offers a continuous covariate alternative, also secondary. Now I need to assess plan_010 on architecture-stratified DIF.

For the YAML output, I'm laying out best-tier predictions: plan_002 should show DIF retention around 92-95% when adding reasoning-RL models, while traditional detectors like Min-K% and ConStat degrade sharply on those models. I'm also predicting tight bootstrap confidence intervals and TOST equivalence confirmation. For plan_003a, I'm expecting ConStat to achieve ~0.72 AUROC on non-RL models but drop to near-chance performance on RL models, with FDR-controlled detection at q=0.10.

For plan_003b, DVD variance detection should reach ~0.68 AUROC for verbatim contamination and ~0.55 for variants, with bimodal distributions appearing in roughly 15% of items. Plan_003c's ensemble approach using 2-of-3 voting should maintain false positive rate below 0.08 while hitting true positive rate around 0.85, and the weighted fusion method should achieve ~0.88 AUROC with stable cross-validation. For plan_005, the bifactor model would still reveal that within-subject contamination percentage stays high around 35%, confirming the limitation isn't a model specification issue rather than a data problem.

Even though plan_005 was initially dropped, if it ran in the best-tier scenario it would show the bifactor fits reasonably well with RMSEA ~0.04, but anchor item selection still can't push the contamination percentage below 30-35% after equating, which actually strengthens the narrative by confirming structural constraints. The equated score correlation would land around 0.96-0.97. For plan_006, item generation shows moderate difficulty correlation of ~0.55 when using student simulation versus only ~0.25 with prompt-only approaches.

Student simulation-based calibration outperforms prompt-only targeting, though the practical gains are limited by what plan_005 reveals. Plan_007 demonstrates meaningful power gains from 0.40 to 0.72 across three administrations at δ=1.0. Plan_008 shows progressive item replacement degrades equating quality monotonically—at 20% replacement the correlation stays above 0.98, but at 50% it drops to 0.92. Plan_009's continuous treatment of release date as a DIF variable captures the smooth trajectory better than categorical splits, especially for medium effects where categorical approaches lose power. Plan_010 appears to be the critical experiment for the best-tier narrative, examining decoder-only architecture effects.

The architecture stratification results show the confounding was substantial—false positive rates drop from 31.3% to 20-25%, IRT RMSEA improves from ~0.08 to 0.03-0.04, and semi-synthetic TPR gains are visible. This confirms that DIF detection requires architecture-homogeneous populations, which is a constraint we can address. Now I'm preparing the full YAML output with predictions for the truly unexecuted experiments—plan_002, plan_003a through 003c, plan_005, plan_006, plan_007, plan_008, plan_009, and plan_010.

For plan_010 in the best tier, the architecture-stratified metrics show C% should land around 20-25% with RMSEA between 0.02-0.05, representing roughly a 30% reduction from the full population baseline and confirming architecture heterogeneity was responsible for about 9 percentage points of the original signal. Plan_002 with its small sample of 10-15 reasoning-RL models still achieves best-tier clarity, and the DIF flag stability measured by Jaccard similarity should be robust.

Now I'm thinking through which experiments actually support the paper's core claims versus which ones belong in supplementary material or should be dropped entirely—plan_002 and plan_007 and plan_009 are supplementary additions, while the ensemble and bifactor approaches don't fit the current narrative, and plan_010 is essential for demonstrating that the original framing holds at full strength across the planned experiments.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "d13c122a-d11d-4ca7-a82f-30cdd03d0a80",
  "isSidechain": false,
  "requestId": "req_011CbErCyCS9CHFcJazSBpXd",
  "type": "assistant",
  "uuid": "3cef9f01-cab0-4cca-a073-6eeac6aaa804",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6TAnWeLXYHrhtxdcnaqrt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16129,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10428,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16129
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

_source line 9 · 2026-05-21T01:34:27.613Z_

```yaml
tier: best
narrative_guidance: >
  Original framing holds at full strength. 38% instability is empirically robust, architecture stratification
  (plan_010) shows C% drops to 20-25% confirming confounding is controllable rather than fatal, and all four
  claims survive review. Dropped experiments (003a/b/c, 005, 006, 008) are reported as future work or appendix
  confirmations — their absence does not weaken the core narrative. plan_002 (RL robustness) serves as
  supplementary defense despite small N. plan_010 is the single most impactful remaining experiment: it
  transforms the "31% baseline FPR" objection into "architecture-stratified DIF reduces spurious flags by
  ~30%, demonstrating the method is refinable." Paper reads as definitive characterization study.

imagined_experiments:
  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      Validate DIF robustness to reasoning-RL models by adding 10-15 open-weight GRPO/PPO models
      to METABENCH temporal cohorts and comparing DIF flag stability + traditional detector degradation.
    expected_results:
      n_reasoning_rl_models: 13
      n_alignment_rl_models: 477
      dif_flag_jaccard_with_vs_without_rl: 0.88
      dif_retention_ratio_rl_added: 0.93
      tost_equivalence_p: 0.008
      mink_auroc_sft_only: 0.81
      mink_auroc_alignment_rl: 0.74
      mink_auroc_reasoning_rl: 0.52
      constat_auroc_sft_only: 0.77
      constat_auroc_reasoning_rl: 0.48
      delong_dif_vs_constat_p: 0.003
      bootstrap_ci_dif_auroc: [0.87, 0.94]
      bootstrap_ci_mink_auroc_rl: [0.41, 0.63]
      partial_exploitation_detection_boundary: 0.45
    result_rationale: >
      In best tier, DIF's group-level design absorbs RL models without degradation because DIF operates
      on item-level response patterns across cohorts (N≥80 total), not on per-model NLL signals. Adding
      13 reasoning-RL models to a cohort of ~800 shifts aggregate response distributions negligibly
      (Jaccard 0.88). Traditional detectors rely on model-level NLL gaps or generation variance — both
      are directly contracted by PPO clipping (Wang et al.), so AUROC drops to near-chance (0.48-0.52)
      on reasoning-RL individuals. TOST confirms equivalence at α=0.05. The detection boundary at p=0.45
      means DIF maintains power above exploitation rate 45%, covering the operationally relevant regime
      where contamination actually inflates scores. N=13 is still acknowledged as a limitation in the
      paper, but the directional signal is unambiguous.
    tables:
      - "Table S1: DIF flag stability under cohort composition perturbation (SFT-only vs +alignment-RL vs +reasoning-RL)"
      - "Table S2: Traditional detector AUROC by model training regime with bootstrap 95% CIs and DeLong pairwise tests"
    figures_description:
      - "Figure S1: AUROC comparison bar chart — DIF vs Min-K% vs ConStat across three training regimes, with 95% bootstrap CIs"
      - "Figure S2: Detection power curve as function of exploitation rate p ∈ [0.4, 1.0] showing DIF detection boundary"
    analysis: >
      Supplementary result supporting Claim 1. DIF's group-level architecture is fundamentally orthogonal
      to the NLL-gap-contraction mechanism that defeats per-model detectors. The result does not make
      a strong standalone contribution (N=13 is small), but it pre-empts the reviewer concern "does RL
      break DIF?" with empirical evidence rather than theoretical argument. In best tier, this is
      Appendix material referenced in §4.1 with a one-paragraph summary in the main text.

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      Independent evaluation of ConStat-style perturbation testing on MMLU: generate 200+ semantically
      equivalent reformulations, compare original vs reformulated performance, apply FDR-controlled detection.
    expected_results:
      n_items_reformulated: 240
      n_models_evaluated: 15
      paraphrase_semantic_similarity: 0.94
      constat_detection_rate_fdr010: 0.32
      constat_auroc_non_rl: 0.73
      constat_auroc_rl: 0.44
      correlation_constat_vs_dif_flags: 0.21
      effect_size_verbatim_contaminated: 0.85
      effect_size_paraphrase_contaminated: 0.31
    result_rationale: >
      In best tier, ConStat works well on non-RL models where verbatim memorization produces large
      original-vs-reformulated accuracy gaps (effect size 0.85). AUROC 0.73 is respectable but not
      exceptional because MMLU items vary in reformulation difficulty — some semantically equivalent
      versions change difficulty unintentionally. On RL models, PPO's generalization smooths out
      original-vs-reformulated gaps (effect size 0.31, AUROC 0.44). Low correlation with DIF flags
      (r=0.21) confirms orthogonal detection axes — ConStat catches per-model verbatim memorization,
      DIF catches cohort-level differential functioning. This orthogonality is exactly what motivates
      the ensemble concept (plan_003c), though the ensemble itself is deferred to future work.
    tables:
      - "Table (future work): ConStat detection rates by MMLU subject category"
    figures_description:
      - "Figure (future work): Scatter plot of ConStat detection score vs DIF Δ_MH showing orthogonal axes"
    analysis: >
      Dropped from paper per pivot decision. In best tier, these results would appear in a follow-up
      ensemble paper. For ICLR submission, ConStat is referenced in Related Work as a complementary
      per-model approach, with the orthogonality observation (r=0.21) cited as motivation for future
      multi-signal work. Not running this experiment does NOT weaken the current paper — the paper's
      contribution is the characterization finding, not detection methodology.

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      Independent evaluation of DVD generation variance on MMLU: temperature sampling on 10-15 models,
      compute variance scores, detect bimodal contamination signal.
    expected_results:
      n_models: 12
      n_items_scored: 2400
      responses_per_item: 50
      sampling_temperature: 0.8
      dvd_auroc_verbatim: 0.66
      dvd_auroc_variant: 0.58
      bimodal_detection_rate: 0.14
      dvd_vs_dif_correlation: 0.15
      gpu_hours_consumed: 65
    result_rationale: >
      In best tier, DVD captures verbatim contamination via bimodal response distributions (memorized
      items show near-deterministic correct answers at any temperature). AUROC 0.66 for verbatim is
      moderate — real contamination produces noisier bimodality than theory predicts because many
      "contaminated" items are also genuinely easy. Variant contamination detection (AUROC 0.58) is
      weak because paraphrased memorization produces smooth variance, not bimodality. Very low
      correlation with DIF (r=0.15) again confirms orthogonality: DVD is per-model generation-level,
      DIF is group-level response-pattern-level. The 65 GPU-hours cost is justified only if building
      toward the ensemble (plan_003c).
    tables:
      - "Table (future work): DVD bimodal detection rates by contamination type"
    figures_description:
      - "Figure (future work): Histogram of generation variance scores showing bimodal vs unimodal items"
    analysis: >
      Dropped from paper. DVD's moderate performance and high GPU cost make it the weakest signal
      in the proposed ensemble. In best tier, this result confirms that single-signal per-model
      detectors have inherent limitations — further supporting the paper's pivot away from detection
      toward characterization. Not running this saves 65 GPU-hours for higher-priority experiments.

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      Fuse DIF + ConStat + DVD into multi-signal ensemble with majority voting and weighted fusion.
    expected_results:
      ensemble_2of3_tpr: 0.84
      ensemble_2of3_fpr: 0.07
      weighted_fusion_auroc: 0.89
      uniform_weight_auroc: 0.86
      cross_validated_weight_stability: 0.03
      dif_coverage_delta_ge14: true
      constat_coverage_non_rl_delta_ge06: true
      dvd_coverage_variant: false
      effective_coverage_union: 0.78
    result_rationale: >
      In best tier, ensemble achieves what no single detector can: broad coverage across contamination
      types with controlled FPR. 2-of-3 voting drives FPR to 0.07 because false positives are
      uncorrelated across orthogonal detection axes (Jaccard <0.21 pairwise). TPR 0.84 reflects
      the union of coverage regions — DIF catches large differential effects, ConStat catches
      per-model verbatim on non-RL, DVD adds marginal bimodal signal. Weighted fusion (AUROC 0.89)
      outperforms uniform (0.86) modestly, and cross-validated weights are stable (σ=0.03),
      indicating the ensemble is not overfitting. DVD contributes least — 2-signal DIF+ConStat
      would achieve AUROC 0.87, suggesting DVD is dispensable.
    tables:
      - "Table (future work): Ensemble coverage matrix — which contamination types each signal catches"
      - "Table (future work): Cross-validated fusion weights with stability analysis"
    figures_description:
      - "Figure (future work): Venn diagram of DIF/ConStat/DVD detection overlap"
      - "Figure (future work): ROC curves for individual signals vs ensemble"
    analysis: >
      Dropped from paper — explicitly listed as future work. In best tier, ensemble results would
      be strong enough for a standalone methods paper (AUROC 0.89 with FPR 0.07). For the current
      characterization paper, the ensemble is referenced as a natural extension: "Our DIF analysis
      reveals the characterization; combining DIF with per-model detectors (ConStat, DVD) into an
      ensemble is a natural next step for practical detection." This positions a follow-up paper
      without weakening the current submission.

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      Pilot bifactor IRT equating on MMLU: fit bifactor model (general + subject-specific factors),
      select anchor items, calibrate replacements via fixed-parameter calibration.
    expected_results:
      bifactor_rmsea: 0.038
      bifactor_cfi: 0.91
      bifactor_tli: 0.89
      general_factor_variance_explained: 0.42
      subject_factor_avg_variance: 0.18
      n_anchor_items_selected: 4200
      anchor_stability_criterion: "no DIF across 3 temporal cohorts"
      c_pct_after_equating: 33.5
      equated_rho_original_vs_replaced: 0.965
      calibration_method: "fixed-parameter (Kim & Kolen 2019)"
    result_rationale: >
      In best tier, bifactor model fits reasonably (RMSEA 0.038 within acceptable range, CFI 0.91
      borderline) confirming that MMLU has genuine multidimensional structure — a general ability
      factor explains 42% of variance, with subject-specific factors adding 18% average. However,
      equating does NOT solve the DIF problem: C% only drops from 38.1% (within-subject, plan_014)
      to 33.5% after anchoring — consistent with plan_014's finding that subject-specific factors
      account for only ~2.4 pp of the instability. Equated score correlation ρ=0.965 meets the
      ≥0.95 criterion, but this just confirms MMLU's massive redundancy (already shown by plan_017's
      ρ=0.997). The bifactor structure is real but doesn't rescue item stability. This is actually
      a GOOD result for the paper: it confirms the "empirical observation" about structural constraints
      — even proper psychometric modeling cannot eliminate the 31%+ baseline.
    tables:
      - "Table (appendix): Bifactor model fit indices across model subsamples"
    figures_description:
      - "Figure (appendix): Scree plot showing general vs subject-specific eigenvalue structure"
    analysis: >
      Killed in practice (plan_015 status: killed) after plan_014 showed within-subject C%=38.1%.
      In best tier, running this would confirm rather than contradict the pivot: the multidimensional
      structure is real but insufficient to explain item instability. This strengthens the
      "empirical observation" narrative — we tried three structural corrections (matched-ability,
      IRT θ-conditioning, bifactor), all failed to reduce baseline below 31%. The result is
      cited in §4.4 as evidence that higher-dimensional IRT is needed (future work), not that
      DIF is broken.

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      Generate replacement items for DIF-flagged MMLU questions using LLM generation with construct
      constraints, calibrate via student simulation.
    expected_results:
      n_items_generated: 500
      n_subjects_covered: 30
      prompt_difficulty_rho: 0.28
      student_sim_difficulty_rho: 0.71
      student_sim_discrimination_rho: 0.58
      holdout_panel_n_models: 50
      holdout_difficulty_rho: 0.64
      holdout_discrimination_rho: 0.49
      construct_coverage_jaccard: 0.82
      gpu_hours_consumed: 180
    result_rationale: >
      In best tier, student simulation (arXiv 2601.09953) substantially outperforms prompt-based
      difficulty targeting (ρ=0.71 vs 0.28), consistent with the literature's range (r=0.75-0.82
      reported, we get 0.71 on MMLU's diverse domains). Discrimination calibration is harder
      (ρ=0.58) because discrimination depends on item-ability interaction, not just surface
      difficulty. Holdout validation shows modest shrinkage (difficulty ρ drops from 0.71 to 0.64)
      due to distribution shift between student simulation and real model population. Construct
      coverage Jaccard 0.82 indicates generated items cover most of the original construct space
      but miss some domain-specific nuances (e.g., professional medicine clinical reasoning chains).
      This is a solid pilot but insufficient for operational replacement — the "graceful degradation"
      question (plan_008) remains.
    tables:
      - "Table (future work): Difficulty and discrimination calibration accuracy by MMLU subject"
    figures_description:
      - "Figure (future work): Scatter of predicted vs observed difficulty — student sim vs prompt-only"
    analysis: >
      Dropped from paper (regeneration claim killed). In best tier, these results would anchor
      a follow-up paper on automated benchmark maintenance. For the current submission, item
      generation is mentioned in Future Work (§7) as a practical application of DIF diagnostics:
      "DIF identifies which items need replacement; student simulation calibration provides a
      feasible generation pipeline (ρ=0.71 difficulty calibration in pilot)." One sentence, no
      more — the characterization paper does not need to solve the replacement problem.

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      Simulate cumulative Bayesian DIF priors over 4 successive benchmark administrations,
      showing power improvement from evidence accumulation.
    expected_results:
      admin_1_tpr_delta10: 0.42
      admin_2_tpr_delta10: 0.58
      admin_3_tpr_delta10: 0.71
      admin_4_tpr_delta10: 0.78
      admin_1_fpr: 0.041
      admin_4_fpr: 0.039
      prior_posterior_shrinkage: 0.35
      bayes_factor_threshold: 3.2
      n_simulated_models_per_admin: 200
      delta_values_tested: [0.8, 1.0, 1.2, 1.4]
      power_at_delta08_admin4: 0.53
      power_at_delta14_admin4: 0.89
    result_rationale: >
      In best tier, cumulative Bayesian priors provide the expected statistical benefit: each
      administration adds ~15 pp TPR for medium effects (δ=1.0), reaching 0.71 after 3
      administrations (vs 0.42 single-shot). FPR remains stable at ~0.04 because Bayesian
      updating with proper priors is conservative on non-DIF items. The key insight is that
      DIF detection becomes operationally viable for medium effects (δ=0.8-1.2) through temporal
      accumulation — exactly the regime where single-shot MH testing lacks power (TPR<0.50).
      At δ=1.4 (the current operational threshold), power reaches 0.89 by administration 4,
      approaching ceiling. The Bayes factor threshold of 3.2 ("substantial evidence") provides
      a principled decision criterion superior to the arbitrary |Δ_MH|≥1.5 cutoff.
    tables:
      - "Table (appendix): Cumulative power by administration × effect size matrix"
    figures_description:
      - "Figure (appendix): Power accumulation curves over 4 administrations for δ ∈ {0.8, 1.0, 1.2, 1.4}"
    analysis: >
      Supplementary contribution supporting Claim 1's practical utility. In best tier, this
      provides a forward-looking operational recommendation: "Benchmark maintainers should
      accumulate DIF evidence across evaluation rounds rather than relying on single-shot
      detection." This transitions the paper from retrospective characterization to prospective
      methodology. Appears as §5.3 or Appendix B, ~1 page. Does not change the core claims
      but adds practical value that reviewers appreciate for a characterization paper.

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      Formal analysis of benchmark validity under progressive item replacement (5%-50%),
      establishing theoretical bounds on validity degradation.
    expected_results:
      rho_at_5pct_replacement: 0.9991
      rho_at_10pct_replacement: 0.9978
      rho_at_20pct_replacement: 0.9943
      rho_at_50pct_replacement: 0.9821
      shr_at_20pct_replacement: 0.988
      construct_coverage_at_20pct: 0.96
      construct_coverage_at_50pct: 0.88
      theoretical_lower_bound_rho: "1 - 2r(1-r) where r=replacement fraction"
      empirical_vs_theoretical_gap: 0.008
    result_rationale: >
      In best tier, MMLU's massive redundancy (plan_017 showed ρ=0.997 after 31% removal) means
      progressive replacement barely degrades rankings. Even at 50% replacement, ρ=0.982 because
      the remaining 50% of items carry sufficient discriminative information — MMLU has ~3× more
      items than needed for stable rankings. Construct coverage degrades faster (0.88 at 50%)
      because some subjects have few items, and replacing them risks changing the construct space.
      The theoretical bound 1-2r(1-r) provides a model-free prediction that tracks empirical
      results within 0.008, giving benchmark maintainers a planning tool. The key finding:
      MMLU can tolerate aggressive item replacement (up to 20%) with negligible validity loss,
      confirming that DIF-flagged items CAN be replaced without breaking the benchmark.
    tables:
      - "Table (future work): Validity metrics × replacement rate matrix with theoretical bounds"
    figures_description:
      - "Figure (future work): Degradation curve — Spearman ρ and construct coverage vs replacement rate"
    analysis: >
      Dropped (depends on plan_005/006 which were killed). In best tier, this result would be
      a strong practical contribution — proving MMLU is replaceable at scale. For the current
      paper, plan_017's ρ=0.997 result already makes the key point about redundancy. Graceful
      degradation is cited in Future Work: "The massive redundancy we observe (ρ=0.997 after
      31% item removal) suggests benchmark maintenance via item replacement is feasible;
      formal degradation analysis is underway."

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Implement Item-Focused Trees (Tutz & Berger 2016) treating model release date as
      continuous covariate, comparing detection power and flexibility vs categorical DIF.
    expected_results:
      n_items_analyzed: 12508
      continuous_covariate: "release_date (days since 2023-01-01)"
      ift_c_pct_equivalent: 28.4
      ift_vs_categorical_flag_jaccard: 0.76
      ift_unique_flags: 412
      categorical_unique_flags: 891
      ift_auc_semi_synthetic: 0.91
      categorical_auc_semi_synthetic: 0.88
      ift_smooth_transition_detected: 0.34
      tree_depth_median: 3
      split_points_cluster_around: "2023-Q4 and 2024-Q2"
    result_rationale: >
      In best tier, Item-Focused Trees capture gradual DIF transitions that categorical splits
      miss. IFT identifies 28.4% of items as functionally unstable (vs 31.3% categorical) —
      slightly fewer because continuous modeling avoids the artificial inflation from forcing a
      binary cohort split. Jaccard 0.76 with categorical flags shows substantial overlap but
      412 unique IFT detections capture items with smooth temporal drift (34% show gradual
      transition patterns). AUC 0.91 on semi-synthetic slightly outperforms categorical (0.88)
      because IFT's flexible splits adapt to the actual contamination timing. Tree split points
      cluster around 2023-Q4 and 2024-Q2, aligning with major model release waves (Llama-2→3
      transition, Qwen-1.5→2). This provides temporal resolution that categorical DIF cannot.
    tables:
      - "Table (appendix): Item-Focused Tree vs categorical DIF detection concordance"
    figures_description:
      - "Figure (appendix): Example IFT tree for a single MMLU item showing DIF trajectory over release date"
      - "Figure (appendix): Split-point histogram showing clustering around model release waves"
    analysis: >
      P2 supplementary analysis. In best tier, IFT adds methodological sophistication without
      changing the core finding — 28-31% of items are unstable regardless of detection method.
      The temporal resolution (split points at model release waves) provides interpretive value:
      instability is concentrated at model generation transitions, consistent with the capability-
      improvement interpretation (ρ=0.307 from plan_001). Appears as Appendix C, ~0.5 pages.
      Strengthens Claim 1 by showing the 38% finding is robust to methodological variation.

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      Run DIF within decoder-only models only to test whether architecture homogeneity
      reduces spurious DIF and improves IRT model fit.
    expected_results:
      n_decoder_only_total: 3847
      n_decoder_only_ref: 892
      n_decoder_only_foc: 541
      decoder_only_c_pct: 22.1
      full_population_c_pct: 31.3
      c_pct_reduction: 29.4%
      irt_rmsea_full: 0.082
      irt_rmsea_decoder_only: 0.037
      irt_cfi_decoder_only: 0.93
      irt_tli_decoder_only: 0.91
      irt_srmr_decoder_only: 0.028
      semi_synthetic_delta_tpr_decoder_only: 0.72
      semi_synthetic_delta_tpr_full: 0.674
      semi_synthetic_fpr_decoder_only: 0.221
      semi_synthetic_fpr_full: 0.314
      decoder_only_sanity_random_split_c_pct: 0.12
      dif_flag_overlap_full_vs_decoder_only: 0.68
      enrichment_vs_li_decoder_only: 0.98
    result_rationale: >
      In best tier, restricting to decoder-only models removes architecture as a confounding
      factor — the unidimensional IRT assumption is more tenable when all models share the same
      basic architecture (autoregressive transformer). RMSEA drops from 0.082 (poor fit) to 0.037
      (acceptable fit), confirming that architecture heterogeneity was driving model misfit, not
      the items themselves. C% drops from 31.3% to 22.1% — a 29% reduction — meaning ~9 pp of
      the original flags were architecture-confounded (encoder-decoder and mixture-of-experts
      models process items differently, creating artificial DIF). The remaining 22.1% represents
      genuine temporal instability within a homogeneous architecture population. Semi-synthetic
      validation improves: FPR drops from 0.314 to 0.221 (fewer false alarms), ΔTPR increases
      from 0.674 to 0.72 (better signal-to-noise). Sanity check confirms the reduction is not
      from power loss (random split C% stays at 0.12%). Flag overlap of 0.68 with full-population
      analysis shows the core DIF items persist — architecture stratification refines rather than
      contradicts the original finding.
    tables:
      - "Table 4: IRT fit diagnostics — full population vs decoder-only subgroup"
      - "Table 5: DIF detection rates and semi-synthetic validation — architecture-stratified vs full"
    figures_description:
      - "Figure 5: C% comparison bar chart — full population (31.3%) vs decoder-only (22.1%) vs random sanity (0.12%)"
      - "Figure 6: IRT fit improvement — RMSEA/CFI/TLI comparison showing acceptable fit in homogeneous subgroup"
    analysis: >
      CRITICAL experiment for best tier — transforms the strongest reviewer objection into a
      methodological contribution. The finding is dual: (1) architecture heterogeneity inflates
      DIF by ~9 pp, confirming the concern is real; (2) 22.1% genuine instability persists even
      in a homogeneous population, confirming the core finding is NOT an artifact. The practical
      recommendation — "run DIF within architecture-homogeneous subpopulations" — is simple,
      zero-cost, and immediately actionable. This appears as §4.3 in the main text (~1.5 pages)
      and is referenced in the abstract. In best tier, reviewers read this as: "the authors
      anticipated our concern, ran the experiment, showed the method is refinable, and the core
      finding survives." This is the difference between a borderline accept and a clear accept.
      IRT RMSEA 0.037 falls within the best-tier target range [0.02, 0.05], and C% 22.1% is
      within [18, 25]. The architecture stratification narrative complements Growing Pains: their
      anchor-item approach also benefits from architecture-homogeneous calibration.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3cef9f01-cab0-4cca-a073-6eeac6aaa804",
  "isSidechain": false,
  "requestId": "req_011CbErCyCS9CHFcJazSBpXd",
  "type": "assistant",
  "uuid": "cb2036aa-a434-48be-b870-57921ddd272d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01R6TAnWeLXYHrhtxdcnaqrt",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16129,
      "cache_read_input_tokens": 11841,
      "output_tokens": 10428,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16129,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 10428,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16129,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16129
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims survive review; GSM1K anti-correlation + downstream z-scores convince reviewers DIF reveals genuine structural insight. ICLR main conference o…",
  "leafUuid": "cb2036aa-a434-48be-b870-57921ddd272d",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF benchmark characterization for ICLR 2027",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：All 4 claims survive review; GSM1K anti-correlation + downstream z-scores convince reviewers DIF reveals genuine structural insight. ICLR main conference o…",
  "leafUuid": "cb2036aa-a434-48be-b870-57921ddd272d",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF benchmark characterization for ICLR 2027",
  "sessionId": "f449a4a6-65be-4cd0-9aef-f871609ad8db"
}
```

---
