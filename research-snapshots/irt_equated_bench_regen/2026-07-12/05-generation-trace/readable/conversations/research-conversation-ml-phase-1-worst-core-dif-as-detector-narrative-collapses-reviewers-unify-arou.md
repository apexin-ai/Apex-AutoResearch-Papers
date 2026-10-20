# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Core DIF-as-detector narrative collapses — reviewers unify around 'this is 

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/79e7c2fe-a977-4e1b-aceb-6f83f3baf848.jsonl`
- **Structured JSON:** [`dbbecf3ccc9cad11356a.json`](../../sessions/db/dbbecf3ccc9cad11356a.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T01:38:27.829Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T01:38:27.829Z",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Core DIF-as-detector narrative collapses — reviewers unify around 'this is just measuring capability improvement, not finding anything wrong with benchmarks.' Reject from main, findings track unlikely without reframe. Must find new angle.\n核心假设：[\"Multiple reviewers argue 38% instability + ρ=0.307 = 'DIF is a capability improvement detector, not a benchmark problem detector' — and this is uninteresting\", \"Meta-critique dismissed: 'You haven't shown DIF detects contamination either — ΔTPR only works with synthetic injection, real contamination unknown'\", \"GSM1K anti-correlation r=−0.478 turned against us: 'DIF flags anti-correlate with contamination, confirming DIF measures capability, not contamination'\", \"Downstream ρ=0.997 used as evidence against significance: 'If removing 31% of items doesn't matter, why should we care about DIF flags?'\", 'plan_010 shows no improvement: decoder-only C% stays at 30-33%, IRT fit poor (RMSEA>0.08)', 'Reviewer familiar with psychometrics argues unidimensional MH on 57-subject MMLU is methodologically invalid']\n关键指标范围：{'expected_reviewer_avg_score': [3.5, 5.5], 'architecture_stratified_c_pct': [30, 38], 'architecture_stratified_irt_rmsea': [0.08, 0.15], 'additional_benchmark_delta_tpr': [0.0, 0.2], 'gsm1k_correlation_if_bootstrapped_ci': [-0.75, -0.05], 'reviewer_novelty_score': [3, 5], 'reviewer_significance_score': [3, 5]}\n叙事方向：Abandon \"DIF reveals benchmark problems\" framing entirely. Reframe as: \"DIF as a model capability archaeology tool.\" The r=−0.478 anti-correlation becomes the HEADLINE: \"DIF items are the ones where genuine capability improvement concentrates — contaminated models can't fake performance on these items.\" New angle: DIF identifies capability-authentic items, enabling contamination-robust evaluation subsets. The 38% instability becomes \"38% of items are capability-sensitive\" (positive framing). Semi-synthetic framework repositioned as \"calibration infrastructure for item sensitivity analysis.\" ρ=0.997 reframed as \"current benchmarks are 3× larger than needed for stable rankings; DIF identifies the informative core.\" Target same venue (ICLR 2027) but as a measurement efficiency / robust evaluation paper rather than a benchmark integrity paper. Title shift from \"Psychometric Analysis Reveals Benchmark Instability\" toward \"Identifying Capability-Authentic Benchmark Items via Differential Item Functioning.\" This reframe leverages the same data and experiments but inverts the valence — instability becomes signal, not noise.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nfocus: Post-pivot framing: characterization + methodology paper, NOT methods paper. Key new evidence since last Dream: (1) GSM8K cross-benchmark replication ΔTPR=+0.818, (2) GSM1K contamination gap anti-correlation r=−0.478 — DIF captures capability-discriminative items that contamination can't fake, (3) downstream impact z=-8 to -49σ confirming DIF items are discriminative carriers. Assess whether these strengthen ICLR main conference viability vs findings track.\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. This instability persists within every subject domain (within-subject C%=31-45%, avg 38.1%), is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). This means cross-temporal MMLU score comparisons carry uncontrolled item-level variance.\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — we cannot decompose 38% into contamination vs capability improvement\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items = discriminative signal carriers**: DIF removal causes significantly MORE ranking disruption than random removal (z=-8 to -49σ, 21/21 conditions). DIF items carry 1.09× cross-cohort accuracy swing vs 0.96× for stable items — they concentrate the information that differentiates model generations.\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF captures capability, not contamination**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005; partial r=−0.385 controlling accuracy; permutation p=0.014). Contaminated models (high GSM8K-GSM1K gap: Phi, Gemma families) perform WORSE on DIF items. DIF captures genuine capability-discriminative items that contamination cannot fake — contamination produces shallow performance gains concentrated on non-DIF items. N=33 matched models, leave-one-out robust (min |r|=0.374).\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_004 Step 3 (r=−0.478, p=0.005, 33 models)\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\" — mutual value positioning\n- Caveats (→ limitations): super-family analysis limited to N≥20 families; GSM1K validation N=33 (CI wide); contamination gap is proxy, not ground truth\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K confirms: DIF flags anti-correlate with contamination (r=−0.478, p=0.005) — contaminated models can't fake performance on DIF items, which capture genuine capability differences. DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF flags anti-correlate with contamination (r=−0.478, p=0.005): DIF captures genuine capability-discriminative items that contamination cannot replicate. We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 38% instability, (2) the ground truth meta-critique affecting the field, (3) the semi-synthetic framework. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T01:38:27.832Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T01:38:27.832Z",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T01:38:27.854Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Core DIF-as-detector narrative collapses — reviewers unify around 'this is just measuring capability improvement, not finding anything wrong with benchmarks.' Reject from main, findings track unlikely without reframe. Must find new angle.
核心假设：["Multiple reviewers argue 38% instability + ρ=0.307 = 'DIF is a capability improvement detector, not a benchmark problem detector' — and this is uninteresting", "Meta-critique dismissed: 'You haven't shown DIF detects contamination either — ΔTPR only works with synthetic injection, real contamination unknown'", "GSM1K anti-correlation r=−0.478 turned against us: 'DIF flags anti-correlate with contamination, confirming DIF measures capability, not contamination'", "Downstream ρ=0.997 used as evidence against significance: 'If removing 31% of items doesn't matter, why should we care about DIF flags?'", 'plan_010 shows no improvement: decoder-only C% stays at 30-33%, IRT fit poor (RMSEA>0.08)', 'Reviewer familiar with psychometrics argues unidimensional MH on 57-subject MMLU is methodologically invalid']
关键指标范围：{'expected_reviewer_avg_score': [3.5, 5.5], 'architecture_stratified_c_pct': [30, 38], 'architecture_stratified_irt_rmsea': [0.08, 0.15], 'additional_benchmark_delta_tpr': [0.0, 0.2], 'gsm1k_correlation_if_bootstrapped_ci': [-0.75, -0.05], 'reviewer_novelty_score': [3, 5], 'reviewer_significance_score': [3, 5]}
叙事方向：Abandon "DIF reveals benchmark problems" framing entirely. Reframe as: "DIF as a model capability archaeology tool." The r=−0.478 anti-correlation becomes the HEADLINE: "DIF items are the ones where genuine capability improvement concentrates — contaminated models can't fake performance on these items." New angle: DIF identifies capability-authentic items, enabling contamination-robust evaluation subsets. The 38% instability becomes "38% of items are capability-sensitive" (positive framing). Semi-synthetic framework repositioned as "calibration infrastructure for item sensitivity analysis." ρ=0.997 reframed as "current benchmarks are 3× larger than needed for stable rankings; DIF identifies the informative core." Target same venue (ICLR 2027) but as a measurement efficiency / robust evaluation paper rather than a benchmark integrity paper. Title shift from "Psychometric Analysis Reveals Benchmark Instability" toward "Identifying Capability-Authentic Benchmark Items via Differential Item Functioning." This reframe leverages the same data and experiments but inverts the valence — instability becomes signal, not noise.

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
  "promptId": "cc4b2450-9e4c-40c9-8b60-8b9d9d91138d",
  "type": "user",
  "uuid": "899934cd-2f3a-4bd1-b70e-9701bcddbdd9",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T01:38:27.852Z_

```json
{
  "parentUuid": "899934cd-2f3a-4bd1-b70e-9701bcddbdd9",
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
  "uuid": "0bee0aff-5fca-4813-ae9d-b511ee96184c",
  "timestamp": "2026-05-21T01:38:27.852Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T01:38:27.853Z_

```json
{
  "parentUuid": "0bee0aff-5fca-4813-ae9d-b511ee96184c",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "01c086cb-31a2-40f6-9e68-658439679080",
  "timestamp": "2026-05-21T01:38:27.853Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core DIF-as-detector narrative collapses — reviewers unify around 'this is just measuring capability improvement, not finding anything wrong with benchmar…",
  "leafUuid": "01c086cb-31a2-40f6-9e68-658439679080",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF benchmark characterization worst-case scenario analysis",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848"
}
```

---

### Assistant

_source line 8 · 2026-05-21T01:39:15.580Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "worst" tier scenario. Let me identify which experiments are still "planned" (not completed):

Looking at the experiment_plan statuses:
- plan_001: planned (but registry shows plan_001_real_data_dif_mmlu as DONE)
- plan_002: planned (rl_robustness_validation)
- plan_003a: planned (constat_perturbation_eval)
- plan_003b: planned (dvd_generation_variance_eval)


- plan_003c: planned (ensemble_fusion)
- plan_004: planned (but registry shows plan_004_gsm8k_cross_benchmark as DONE)
- plan_005: planned (bifactor_irt_equating_pilot)
- plan_006: planned (item_generation_calibration)
- plan_007: planned (cumulative_bayesian_dif)
- plan_008: planned (graceful_degradation_analysis)
- plan_009: planned (item_focused_trees)
- plan_010: planned (architecture_stratified_dif)
- plan_011: planned (but registry shows DONE)

I notice there's a discrepancy between the plan statuses and what's actually in the registry, so let me cross-reference to get the accurate list of what still needs predictions.

Looking at the user's request more carefully — they want worst-tier predictions for each planned experiment in the experiment_plan. Some of these have already been executed with real results, but the user is asking for worst-tier scenario predictions across all of them, which would show what happens when reviewers interpret findings in the most negative light possible.

The worst-tier framing hinges on reviewers dismissing the meta-critique and reinterpreting the instability metrics and correlations as evidence that DIF is just measuring capability differences rather than detecting benchmark problems. Key vulnerabilities include the 38% instability being framed as noise, the negative GSM1K correlation being weaponized against the findings, and the high correlation in plan_010 being used to argue against significance.

Looking at the expected metric ranges for worst-case scenarios, I'm seeing reviewer scores clustering in the 3.5-5.5 range, architecture performance staying flat at 30-38% accuracy, IRT fit degrading to 0.08-0.15 RMSEA, and the bootstrapped GSM1K correlation remaining deeply negative. The novelty and significance scores would hover around 3-5, suggesting moderate but contested contributions.

Now I'm working through each experiment to generate worst-tier predictions, keeping the reframe narrative in mind—positioning DIF as a capability archaeology tool that reveals how models encode different competencies, which could flip the negative framing if executed well.

For the real DIF-MMLU experiment that's already complete, the 31.3% C% and 0.307 correlation would be reinterpreted under worst tier as evidence that DIF detects genuine capability shifts rather than contamination, with the 0.96 enrichment score confirming no relationship to data leakage. The RL robustness validation faces constraints with only 13 reasoning-RL models available, which limits the statistical power of the analysis.

For the remaining experiments, ConStat might actually outperform DIF on non-RL models, making the motivation for DIF questionable, while DVD could show reasonable detection on open-weight models that would undermine the necessity of the approach. The ensemble fusion would likely yield only marginal gains over individual methods, and the cross-benchmark GSM8K results with the negative correlation could be turned into an argument against the method's effectiveness.

The bifactor IRT model might fail to converge on the MMLU subset or show poor fit, and the generated items could have weak difficulty correlations that undermine the student simulation approach. The cumulative Bayesian DIF strategy risks amplifying false positives if the baseline FPR is already high, though the graceful degradation analysis would at least confirm the robustness finding.

Plans 009 through 011 explore whether temporal DIF, architectural stratification, and semi-synthetic contamination actually drive improvements, but under worst-case conditions they either show no meaningful gains or get dismissed as artifacts of synthetic data rather than evidence of real-world utility. Now I'm working through the detailed YAML structure with worst-tier metrics and reframe narratives for each experiment.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "01c086cb-31a2-40f6-9e68-658439679080",
  "isSidechain": false,
  "requestId": "req_011CbEroqzKYosL7jznTy8jZ",
  "type": "assistant",
  "uuid": "300e8deb-1a27-410e-9f74-56c702f62f7f",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfHisQ2E9fnvSr13CK47dh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16316,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16316
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

_source line 9 · 2026-05-21T01:43:38.134Z_

```yaml
tier: worst
narrative_guidance: >
  Core "DIF reveals benchmark problems" narrative collapses. Reviewers converge on:
  DIF is a capability improvement detector, not a benchmark integrity tool. 38% instability
  = 38% of items are capability-sensitive (models improved on them). ρ=0.307 is the
  smoking gun for reviewers. GSM1K r=−0.478 is weaponized: "DIF anti-correlates with
  contamination, confirming DIF captures capability, not contamination." ρ=0.997
  trivializes downstream significance. Semi-synthetic injection dismissed as non-transferable
  to real contamination. Unidimensional MH on 57-subject MMLU called methodologically
  invalid by psychometrics-literate reviewer. Reframe required: pivot to "DIF as
  capability archaeology / measurement efficiency" paper. Title: "Identifying
  Capability-Authentic Benchmark Items via Differential Item Functioning." The same
  data supports a different story — instability becomes signal, ρ=0.997 becomes
  "benchmarks are 3× too large," r=−0.478 becomes the headline positive finding.
  Target ICLR 2027 as robust evaluation / measurement efficiency contribution.

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      Apply MH DIF to METABENCH MMLU 5,219×12,508 matrix. Temporal cohort (2023 vs 2024-H1),
      ability-quintile cohort, within-family confound control, domain-specificity analysis.
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.318
      temporal_enrichment: 0.96
      ability_ets_c_pct: 2.9
      within_family_llama2v3_c_pct: 61.3
      domain_spearman_rho: 0.307
      domain_spearman_p: 0.02
      sanity_random_split_c_pct: 0.18
      reviewer_interpretation: "capability_gain_detector"
    result_rationale: >
      Under worst tier, the actual results hold (these are already observed) but their
      interpretation collapses. ρ=0.307 (p=0.02) correlating DIF flags with domain-level
      accuracy improvement is seized by reviewers as causal evidence: items flagged by DIF
      are simply items where models improved. Enrichment=0.96 against Li et al. labels
      confirms zero relationship to contamination — reviewers read this as "DIF doesn't
      detect contamination at all." The 61.3% within-family Llama-2-vs-3 C% is devastating:
      within the same family (same training pipeline, likely same data), DIF flags 61% of
      items, which reviewers attribute entirely to capability gain between generations.
      The sanity check (0.18%) proves DIF detects *something* real, but reviewers argue
      that "something" is capability improvement, not benchmark pathology. The meta-critique
      about Li et al. labels is dismissed: "You haven't provided ANY ground truth showing
      DIF detects contamination — enrichment=0.96 is your only validation, and it failed."
    tables:
      - name: "Table 1: DIF Detection Summary Under Worst Interpretation"
        columns: [cohort_definition, c_pct, enrichment_vs_li, reviewer_counterargument]
        rows:
          - [temporal_2023_vs_2024, 31.3, 0.96, "Capability gain across generations"]
          - [ability_quintile, 2.9, 1.19, "Minimal DIF = items function consistently across ability levels (expected)"]
          - [within_family_llama2v3, 61.3, "N/A", "Same family, same data pipeline → pure capability gain"]
          - [random_split_sanity, 0.18, "N/A", "Confirms real signal, but signal = capability"]
      - name: "Table 2: Domain Correlation Detail"
        columns: [metric, value, reviewer_spin]
        rows:
          - [spearman_rho_dif_vs_accuracy_gain, 0.307, "DIF tracks capability improvement"]
          - [p_value, 0.02, "Significant correlation confirms confound"]
          - [variance_explained, "9.4%", "Remainder is noise, not contamination signal"]
    figures_description:
      - "Fig 1a: Scatter plot of per-subject C% vs accuracy improvement (2023→2024). Positive trend (ρ=0.307) with regression line. Reviewer annotation: 'DIF flags cluster in high-improvement domains (coding, math, reasoning) — exactly where models improved most.'"
      - "Fig 1b: Enrichment ratio histogram across Li et al. label categories. Flat distribution centered at 1.0, showing no preferential DIF flagging of contaminated items."
    analysis: >
      The plan_001 results are empirically sound but narratively fatal under worst tier.
      The reframe salvages them: 31.3% "instability" becomes "31% of items are capability-
      sensitive — they differentiate model generations." ρ=0.307 becomes evidence that DIF
      identifies items where genuine capability improvement concentrates. Enrichment=0.96
      is reframed as "DIF and contamination labels measure orthogonal constructs — DIF
      captures differential item functioning, not data leakage." The within-family result
      becomes the strongest evidence FOR the reframe: even within Llama family, DIF
      identifies where architectural/training improvements manifest at the item level.

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      Validate DIF robustness to RL training. Alignment-RL (DPO/ORPO, N=477) and
      reasoning-RL (GRPO/PPO, N≈13) cohorts. Compare DIF vs Min-K%/ConStat per-model
      degradation. Power analysis for partial exploitation.
    expected_results:
      n_reasoning_rl_models: 13
      dif_flag_overlap_sft_vs_alignment_rl: 0.82
      dif_flag_overlap_sft_vs_reasoning_rl: 0.71
      mink_auroc_sft: 0.63
      mink_auroc_alignment_rl: 0.58
      mink_auroc_reasoning_rl: 0.44
      constat_auroc_sft: 0.67
      constat_auroc_reasoning_rl: 0.51
      dif_tpr_with_rl_in_cohort: 0.65
      dif_tpr_without_rl_in_cohort: 0.68
      bootstrap_ci_overlap: true
      delong_p_dif_vs_constat: 0.23
      tost_equivalence_p: 0.34
      partial_exploitation_detection_boundary: 0.55
      reviewer_score: 4.0
    result_rationale: >
      With only N=13 reasoning-RL models, no comparison reaches statistical significance.
      DIF flag overlap between SFT and RL-containing cohorts is 71%, which reviewers
      dismiss as "you can't distinguish robustness from noise with N=13." The DeLong test
      p=0.23 means we cannot claim DIF outperforms ConStat. TOST equivalence test fails
      (p=0.34 > 0.05) — we can't even claim equivalence. Min-K% drops to 0.44 AUROC on
      reasoning-RL models, but reviewers note "you're comparing DIF (group-level, N=477
      cohort) against per-model detectors on 13 models — apples to oranges." The partial
      exploitation analysis shows detection boundary at p=0.55, meaning DIF misses
      contamination below 55% exploitation rate — reviewers call this "DIF only detects
      extreme contamination, which is also detectable by simpler methods." The entire
      experiment is underpowered and reviewers recommend "defer until more GRPO/PPO models
      exist on public leaderboards."
    tables:
      - name: "Table 3: RL Robustness Comparison (Underpowered)"
        columns: [method, sft_auroc, alignment_rl_auroc, reasoning_rl_auroc, "95% CI width"]
        rows:
          - [DIF_MH, 0.69, 0.66, 0.65, "±0.14"]
          - [Min-K%, 0.63, 0.58, 0.44, "±0.18"]
          - [ConStat, 0.67, 0.61, 0.51, "±0.16"]
      - name: "Table 4: Statistical Tests (All Non-Significant)"
        columns: [comparison, test, statistic, p_value, conclusion]
        rows:
          - [DIF_vs_ConStat_RL, DeLong, "z=1.19", 0.23, "Cannot reject H0"]
          - [DIF_retention_equivalence, TOST, "t=0.96", 0.34, "Cannot claim equivalence"]
          - [flag_overlap_SFT_vs_RL, "Bootstrap Jaccard", 0.71, "CI [0.54, 0.88]", "Wide CI, inconclusive"]
    figures_description:
      - "Fig 2: ROC curves for DIF vs Min-K% vs ConStat on reasoning-RL subset. All curves are noisy with wide confidence bands due to N=13. Overlapping CIs prevent any method from claiming superiority."
      - "Fig 3: Detection power vs exploitation rate p. Curve shows TPR<0.5 for p<0.55. Shaded region marks 'practical contamination range' (p=0.3-0.7) where DIF is weakest."
    analysis: >
      Experiment is fatally underpowered. N=13 reasoning-RL models cannot support any
      statistical claim. Under worst tier, this becomes ammunition: "authors claim RL
      robustness but provide no evidence." Reframe option: drop RL robustness as a claim
      entirely, acknowledge in limitations, reposition the alignment-RL (N=477) result as
      "DIF is stable across training objective variations" without claiming reasoning-RL
      coverage. Under the capability-archaeology reframe, RL robustness is less central
      anyway — the question becomes "do capability-authentic items remain stable across
      training paradigms?" which is interesting but not load-bearing.

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      Independent ConStat-style perturbation evaluation on 200+ MMLU items. Generate
      semantic reformulations, compare original vs reformulated performance, apply
      FDR-controlled detection.
    expected_results:
      n_items_reformulated: 220
      n_models_tested: 15
      constat_detection_rate_non_rl: 0.41
      constat_detection_rate_rl: 0.12
      constat_fdr_controlled_rate: 0.28
      constat_vs_dif_overlap: 0.18
      paraphrase_quality_score: 0.73
      reformulation_difficulty_shift_mean: 0.08
      reviewer_critique: "paraphrase quality uncontrolled"
    result_rationale: >
      Under worst tier, ConStat shows moderate detection on non-RL models (41%) — notably
      higher than DIF's enrichment=0.96 against contamination labels. Reviewers argue
      "ConStat at least detects something correlated with memorization; DIF detects
      capability improvement." The 18% overlap between ConStat and DIF flags confirms
      they measure different constructs, but reviewers spin this negatively: "DIF is
      orthogonal to contamination detection." The RL degradation (41%→12%) is expected
      but reviewers note "at least ConStat provides per-model detection; DIF requires
      cohort structure." Paraphrase quality (0.73) is attacked: "reformulations may
      introduce difficulty shifts (mean Δ=0.08), confounding detection." The entire
      comparison undermines DIF rather than supporting it — ConStat looks like the
      more direct contamination tool, and DIF looks like a capability change detector
      with no contamination detection ability.
    tables:
      - name: "Table 5: ConStat vs DIF Detection Comparison"
        columns: [method, detection_target, rate_non_rl, rate_rl, per_model, requires_cohort]
        rows:
          - [ConStat, memorization, 0.41, 0.12, "Yes", "No"]
          - [DIF_MH, "differential_functioning", 0.313, "N/A (group-level)", "No", "Yes"]
          - [overlap, "both_flag", 0.18, "N/A", "-", "-"]
    figures_description:
      - "Fig 4: Venn diagram of ConStat vs DIF flags. Small overlap (18%) with large DIF-only region. Reviewer annotation: 'DIF-only items are capability-gain items, not contamination.'"
    analysis: >
      ConStat comparison backfires under worst tier. It provides a foil that makes DIF
      look less like a contamination detector. Under reframe, this becomes irrelevant —
      DIF is repositioned as capability-item identifier, not competing with ConStat on
      contamination detection. Drop from reframed paper or move to appendix as
      "related method comparison showing orthogonal signals."

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      DVD generation variance evaluation on 10-15 open-weight models. 50 responses per
      item via temperature sampling, bimodal distribution detection for contamination.
    expected_results:
      n_models: 12
      n_items_tested: 500
      dvd_bimodal_detection_rate: 0.23
      dvd_variance_auc: 0.58
      dvd_vs_dif_overlap: 0.14
      temperature_sensitivity: "high (results vary 15-30% across T=0.7 vs T=1.0)"
      gpu_hours_used: 65
      generation_cost_barrier: "high"
      reviewer_critique: "expensive and noisy"
    result_rationale: >
      DVD shows weak detection (AUC=0.58, barely above chance) on only 12 models. The
      bimodal detection rate of 23% is unstable across temperature settings (15-30%
      variation), making the signal unreliable. Overlap with DIF is minimal (14%),
      confirming both methods detect different phenomena. Under worst tier, reviewers
      dismiss DVD as "noisy, expensive, and only applicable to open-weight models."
      The 65 GPU-hour cost for testing 12 models × 500 items is criticized as
      impractical. More importantly, DVD's failure doesn't help DIF's case — reviewers
      note "neither DVD nor DIF convincingly detects contamination; DIF detects
      capability change, DVD detects generation instability, neither detects what
      we actually care about." The experiment consumes resources without strengthening
      any claim.
    tables:
      - name: "Table 6: DVD Results Summary"
        columns: [metric, value, stability]
        rows:
          - [bimodal_detection_rate, 0.23, "±0.09 across temperatures"]
          - [variance_auc, 0.58, "±0.07"]
          - [dif_overlap, 0.14, "stable"]
          - [cost_per_model, "5.4 GPU-hrs", "fixed"]
    figures_description:
      - "Fig 5: DVD variance distributions for flagged vs unflagged items. Heavy overlap between distributions, AUC=0.58. Contrast with theoretical bimodal expectation shows real data is messier than assumed."
    analysis: >
      DVD is the weakest experiment under worst tier. Low AUC, high cost, temperature
      sensitivity, minimal DIF overlap. Under reframe, DVD is irrelevant — drop entirely.
      The capability-archaeology framing doesn't need generation variance.

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      Fuse DIF + ConStat + DVD into multi-signal ensemble. Majority voting and weighted
      fusion. Cross-validate fusion weights.
    expected_results:
      ensemble_2of3_precision: 0.31
      ensemble_2of3_recall: 0.15
      ensemble_weighted_auc: 0.62
      ensemble_fpr: 0.14
      uniform_weight_auc: 0.59
      optimized_weight_auc: 0.64
      cv_overfit_gap: 0.08
      dif_weight_in_optimized: 0.22
      constat_weight_in_optimized: 0.51
      dvd_weight_in_optimized: 0.27
      reviewer_critique: "ensemble of weak signals is still weak"
    result_rationale: >
      Under worst tier, ensemble fusion fails to produce meaningful improvement. The
      2-of-3 majority voting achieves only 15% recall because DIF, ConStat, and DVD
      flag largely non-overlapping items (Jaccard 0.14-0.18). Weighted fusion (AUC=0.64)
      barely beats uniform (0.59), and cross-validation reveals 0.08 overfit gap,
      suggesting the optimized weights don't generalize. Critically, DIF receives the
      lowest weight (0.22) in the optimized ensemble — reviewers read this as "even the
      ensemble agrees DIF contributes least to contamination detection." The ensemble
      FPR of 0.14 technically meets the <0.10 target... no, it doesn't (0.14 > 0.10).
      Reviewers conclude: "three individually weak contamination signals don't combine
      into a strong one. The fundamental problem — lack of ground truth — isn't solved
      by fusion." The entire plan_003 sequence (a+b+c) consumed 150 GPU-hours for
      a negative meta-result.
    tables:
      - name: "Table 7: Ensemble Performance (Worst Tier)"
        columns: [strategy, precision, recall, auc, fpr]
        rows:
          - [DIF_only, 0.29, 0.31, 0.54, 0.31]
          - [ConStat_only, 0.38, 0.41, 0.61, 0.22]
          - [DVD_only, 0.24, 0.23, 0.58, 0.28]
          - [majority_2of3, 0.31, 0.15, 0.55, 0.14]
          - [weighted_fusion_cv, 0.35, 0.32, 0.64, 0.19]
    figures_description:
      - "Fig 6: Stacked bar chart of ensemble weights. ConStat dominates (51%), DIF minimal (22%). Reviewer reads: 'DIF is the least informative signal for contamination.'"
    analysis: >
      Ensemble experiment is counterproductive under worst tier. It demonstrates DIF's
      weakness relative to ConStat for contamination detection. Under reframe, the entire
      plan_003 sequence should be dropped — the capability-archaeology paper doesn't need
      contamination detection ensemble. Save 150 GPU-hours.

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      Replicate DIF on GSM8K (1,319 items × 6,702 models). Semi-synthetic validation.
      GSM1K contamination gap correlation as external validation.
    expected_results:
      gsm8k_temporal_c_pct: 18.9
      gsm8k_semi_synthetic_delta_tpr_p10: 0.818
      gsm1k_pearson_r: -0.478
      gsm1k_pearson_p: 0.005
      gsm1k_partial_r: -0.385
      gsm1k_n_models: 33
      gsm1k_bootstrap_ci_r: [-0.71, -0.12]
      gsm1k_permutation_p: 0.014
      cook_d_max: "Deepseek-math-7b-rl"
      leave_one_out_min_r: -0.374
      reviewer_reinterpretation: "anti-correlation confirms DIF=capability, not contamination"
    result_rationale: >
      Under worst tier, the r=−0.478 result — the strongest cross-benchmark finding — is
      turned against the original narrative. Reviewers argue: "DIF items anti-correlate
      with contamination gap. Models that are MORE contaminated (high GSM8K-GSM1K gap:
      Phi, Gemma) perform WORSE on DIF items. This proves DIF identifies items where
      genuine capability matters — contaminated models can't fake their way through these
      items. DIF is a capability detector, not a contamination detector." The bootstrap
      CI [-0.71, -0.12] is wide (N=33), and reviewers note "this could be as weak as
      r=-0.12, barely meaningful." The ΔTPR=0.818 on semi-synthetic injection is
      dismissed: "synthetic contamination (flipping incorrect→correct deterministically)
      doesn't resemble real contamination (partial memorization, shallow pattern matching).
      High ΔTPR on synthetic data doesn't validate real-world detection." The 18.9%
      temporal C% on GSM8K (vs 31.3% on MMLU) is spun as "DIF flags vary wildly across
      benchmarks — no stable characterization." Deepseek-math-7b-rl as Cook's D outlier
      raises concerns about robustness of the correlation despite leave-one-out showing
      min |r|=0.374.
    tables:
      - name: "Table 8: GSM1K Correlation Under Worst-Case Scrutiny"
        columns: [metric, point_estimate, "95% CI", reviewer_counterargument]
        rows:
          - [pearson_r, -0.478, "[-0.71, -0.12]", "CI includes near-zero; N=33 too small"]
          - [partial_r, -0.385, "[-0.64, -0.04]", "Controlling accuracy weakens signal"]
          - [permutation_p, 0.014, "N/A", "Multiple testing not corrected"]
          - [leave_one_out_min, -0.374, "N/A", "One model removal cuts 22% of effect"]
      - name: "Table 9: Cross-Benchmark C% Instability"
        columns: [benchmark, temporal_c_pct, interpretation]
        rows:
          - [MMLU, 31.3, "High instability or high capability sensitivity"]
          - [GSM8K, 18.9, "Lower instability — benchmark-dependent"]
          - [delta, 12.4, "No universal 'instability rate' — DIF is benchmark-specific"]
    figures_description:
      - "Fig 7: Scatter of per-model DIF-C-proportion vs GSM1K contamination gap. Negative trend with r=−0.478. Phi-3/Gemma family models (high contamination gap) cluster at low DIF-C-proportion. Reviewer overlay: 'Contaminated models fail DIF items = DIF measures genuine capability.'"
      - "Fig 8: Bootstrap distribution of r with 95% CI. Distribution centered at −0.48 but CI extends to −0.12, shown with dashed lines."
    analysis: >
      The GSM1K correlation is the pivotal result. Under original framing, r=−0.478 is
      devastating (DIF anti-correlates with contamination). Under reframe, it becomes the
      HEADLINE: "DIF identifies capability-authentic items that contamination cannot
      replicate." The wide CI (N=33) remains a vulnerability. The reframed paper should
      lead with this finding and frame it as: "Contaminated models show inflated scores
      on non-DIF items (shallow memorization) but cannot maintain performance on DIF
      items (genuine capability discriminators)." ΔTPR=0.818 is repositioned as
      "calibration infrastructure" rather than "detection proof."

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      Pilot bifactor IRT on MMLU (general factor + 57 subject factors). Anchor item
      selection, fixed-parameter calibration for replacement items.
    expected_results:
      bifactor_convergence: false
      bifactor_rmsea: 0.11
      bifactor_cfi: 0.72
      bifactor_tli: 0.68
      n_subjects_57: 57
      n_items_12508: 12508
      n_models_5219: 5219
      anchor_items_selected: 0
      equating_rho: "N/A (model failed to converge)"
      computation_time_hours: 48
      memory_peak_gb: 180
      reviewer_critique: "57-factor bifactor on 12K items is computationally intractable"
    result_rationale: >
      Under worst tier, bifactor IRT fails catastrophically. The 57-subject structure of
      MMLU means a bifactor model requires estimating 1 general + 57 specific factors —
      a 58-dimensional latent space with ~25,000 item parameters. This exceeds practical
      computational limits (180GB RAM, 48 hours without convergence). Even if forced to
      converge with simplifications (e.g., constraining factor loadings), fit indices
      are poor: RMSEA=0.11 (>0.08 threshold), CFI=0.72 (<0.90 threshold), TLI=0.68
      (<0.90). The unidimensionality assumption underlying MH-DIF is confirmed as
      violated, but the alternative (bifactor) is intractable. Reviewers argue: "You've
      demonstrated that the psychometric foundation of your method is inappropriate for
      MMLU, but provided no working alternative. Multidimensional DIF methods exist
      (MIMIC, MIRT-DIF) but you haven't implemented them." Anchor item selection fails
      because the bifactor model didn't converge — no equating is possible. The entire
      regeneration pipeline (plan_005 → plan_006 → plan_008) collapses at step one.
    tables:
      - name: "Table 10: Bifactor IRT Fit Diagnostics"
        columns: [metric, value, threshold, verdict]
        rows:
          - [RMSEA, 0.11, "<0.08", FAIL]
          - [CFI, 0.72, ">0.90", FAIL]
          - [TLI, 0.68, ">0.90", FAIL]
          - [SRMR, 0.09, "<0.08", FAIL]
          - [convergence, "No (48h timeout)", "Yes", FAIL]
          - [n_parameters, "~25,000", "<5,000 practical", FAIL]
    figures_description:
      - "Fig 9: Bifactor model log-likelihood trace over 48 hours. Curve plateaus without convergence. Annotated with parameter count and memory consumption at each iteration."
    analysis: >
      Bifactor failure is expected and, under worst tier, becomes evidence that MMLU is
      fundamentally unsuitable for IRT-based psychometric analysis. Reviewers cite this
      as proof that "applying unidimensional psychometric methods to a 57-subject
      multidimensional benchmark is methodologically invalid." Under reframe, this is
      acknowledged honestly in limitations: "MMLU's multidimensional structure exceeds
      current IRT modeling capacity; our within-subject analysis (plan_014) partially
      addresses this but doesn't eliminate the concern." Drop the equating pipeline
      entirely.

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      Generate replacement items for DIF-flagged questions. LLM generation with construct
      constraints, student simulation calibration, difficulty correlation validation.
    expected_results:
      n_items_generated: 300
      n_subjects_covered: 15
      difficulty_correlation_prompt: 0.18
      difficulty_correlation_student_sim: 0.34
      cognitive_level_match_rate: 0.45
      item_quality_human_eval: 0.61
      construct_alignment_score: 0.53
      holdout_panel_rho: 0.42
      gpu_hours_used: 180
      reviewer_critique: "difficulty calibration too weak for operational use"
    result_rationale: >
      Under worst tier, item generation produces mediocre results. Prompt-based difficulty
      targeting yields ρ=0.18 (consistent with literature range 0.10-0.45 from arXiv
      2602.06631 — on the low end). Student simulation calibration improves to ρ=0.34
      but still far below the r=0.75-0.82 claimed in arXiv 2601.09953 — the discrepancy
      arises because student simulation was validated on simple math items, not MMLU's
      diverse knowledge domains. Cognitive level matching (45%) means over half of
      replacement items test different cognitive processes than originals. Construct
      alignment (53%) is poor — reviewers argue "replacing items with construct-misaligned
      substitutes invalidates the benchmark more than the DIF items did." The holdout
      panel validation (ρ=0.42) shows replacement items don't preserve model rankings.
      Reviewers conclude: "The cure is worse than the disease — DIF-flagged items at
      least produce stable rankings (ρ=0.997); replacements introduce genuine measurement
      error." 180 GPU-hours consumed for a negative result. Under reframe, this
      experiment is dropped entirely — the capability-archaeology paper doesn't need
      item replacement.
    tables:
      - name: "Table 11: Item Generation Calibration Failure"
        columns: [calibration_method, difficulty_rho, claimed_in_literature, achieved]
        rows:
          - [prompt_targeting, 0.18, "0.10-0.45", "Low end"]
          - [student_simulation, 0.34, "0.75-0.82", "Far below"]
          - [holdout_validation, 0.42, ">0.90 needed", "Insufficient"]
    figures_description:
      - "Fig 10: Scatter of generated item difficulty vs target difficulty. Wide dispersion, ρ=0.34. Diagonal reference line shows ideal calibration. Most points far from diagonal."
    analysis: >
      Item generation is the most expensive failure (180 GPU-hrs). Under worst tier, it
      actively undermines the paper — reviewers use it to argue "you can't replace DIF
      items, and you've shown DIF items don't affect rankings (ρ=0.997), so what's the
      practical value?" Under reframe, this experiment should not be run at all. The
      capability-archaeology paper frames DIF items as valuable signal carriers, not
      problems to be replaced. Save the 200 GPU-hour budget.

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      Implement cumulative Bayesian DIF priors (Sinharay et al., 2006). Simulate 4
      successive administrations. Show power improvement from evidence accumulation.
    expected_results:
      single_admin_power_d10: 0.38
      cumulative_2_admin_power_d10: 0.49
      cumulative_3_admin_power_d10: 0.58
      cumulative_4_admin_power_d10: 0.64
      single_admin_fpr: 0.05
      cumulative_4_admin_fpr: 0.11
      fpr_inflation_per_admin: 0.02
      convergence_rate: 0.92
      reviewer_critique: "cumulative FPR inflation makes this impractical"
    result_rationale: >
      Under worst tier, cumulative Bayesian DIF shows power improvement (0.38→0.64 over
      4 administrations for medium effects δ=1.0) but fails to reach the 0.70 target
      from the plan description. More critically, FPR inflates from 0.05 to 0.11 across
      4 administrations — each administration's prior carries forward false positive
      evidence. Reviewers argue: "With baseline FPR already at 31% in real data
      (plan_001), cumulative approaches will amplify false positives. You're
      accumulating evidence that items changed function — but we've established this
      is capability improvement, not contamination. You're building a more powerful
      detector of the wrong thing." The simulation uses idealized conditions (known
      item parameters, controlled drift) that don't match real MMLU conditions. Under
      reframe, this becomes interesting — "cumulative tracking of capability-sensitive
      items across model generations" — but the FPR inflation concern remains.
    tables:
      - name: "Table 12: Cumulative Bayesian DIF Power Trajectory"
        columns: [n_administrations, tpr_d10, tpr_d14, fpr, net_power_gain]
        rows:
          - [1, 0.38, 0.68, 0.05, baseline]
          - [2, 0.49, 0.78, 0.07, "+0.11/+0.10"]
          - [3, 0.58, 0.84, 0.09, "+0.09/+0.06"]
          - [4, 0.64, 0.87, 0.11, "+0.06/+0.03"]
    figures_description:
      - "Fig 11: Power curves across cumulative administrations. Diminishing returns visible. FPR creep shown as shaded region growing with each administration."
    analysis: >
      Cumulative Bayesian is theoretically elegant but practically undermined by FPR
      inflation. Under worst tier, it's a distraction — reviewers see diminishing
      returns and growing false positives. Under reframe, it has modest value as
      "longitudinal capability tracking infrastructure" but is not central. Recommend
      moving to appendix or future work.

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      Formal analysis of benchmark validity under progressive item replacement
      (5%-50%). Validity metrics, theoretical bounds, empirical validation.
    expected_results:
      rho_at_5pct_replacement: 0.998
      rho_at_10pct_replacement: 0.996
      rho_at_20pct_replacement: 0.991
      rho_at_50pct_replacement: 0.972
      reliability_alpha_original: 0.94
      reliability_alpha_50pct_replaced: 0.88
      construct_coverage_original: 57
      construct_coverage_50pct_replaced: 52
      theoretical_bound_rho_min: 0.95
      replacement_rate_at_bound: 0.38
      reviewer_critique: "confirms DIF removal doesn't matter"
    result_rationale: >
      Under worst tier, graceful degradation analysis confirms the ρ=0.997 finding from
      plan_017 — removing/replacing up to 50% of items barely affects rankings (ρ=0.972).
      Reviewers weaponize this: "Even replacing HALF the benchmark changes rankings by
      less than 3%. This proves MMLU is massively redundant, and DIF-flagged items are
      redundant too. Why should anyone care about 31% item instability if it doesn't
      affect rankings?" Reliability drops from 0.94 to 0.88 at 50% replacement, but
      remains above acceptable thresholds (0.70). Construct coverage loses 5 of 57
      subjects at 50% replacement — reviewers note "acceptable." The theoretical bound
      (ρ≥0.95 up to 38% replacement) perfectly matches the DIF flagging rate (31.3%),
      which reviewers read as "you can safely ignore everything DIF flags." This
      experiment depends on plan_005/006 (which fail), so the "replacement" is simulated
      via random item substitution rather than actual generated items — further reducing
      credibility.
    tables:
      - name: "Table 13: Graceful Degradation Curves"
        columns: [replacement_pct, rank_rho, reliability_alpha, subjects_covered, verdict]
        rows:
          - [0, 1.000, 0.94, 57, baseline]
          - [5, 0.998, 0.93, 57, negligible]
          - [10, 0.996, 0.93, 57, negligible]
          - [20, 0.991, 0.91, 56, minor]
          - [31, 0.987, 0.90, 55, "DIF removal point"]
          - [50, 0.972, 0.88, 52, "still acceptable"]
    figures_description:
      - "Fig 12: Degradation curve showing ρ vs replacement rate. Nearly flat until 40%, gentle decline thereafter. DIF removal rate (31%) marked — well within 'safe' zone. Reviewer: 'This graph argues against your own paper.'"
    analysis: >
      Graceful degradation is self-defeating under worst tier AND original framing. It
      proves removing DIF items doesn't matter, undermining significance. Under reframe,
      this becomes: "MMLU is 3× larger than needed for stable rankings — DIF identifies
      the informative core (the items that DO contribute discriminative signal)." The
      ρ=0.972 at 50% replacement becomes "you could cut MMLU in half and preserve
      rankings — DIF tells you which half to keep." This is actually a strong reframe,
      turning the worst finding into a measurement efficiency contribution.

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Item-Focused Trees (Tutz & Berger, 2016) as alternative to categorical cohort DIF.
      Continuous covariate (release date). Compare detection power vs categorical MH.
    expected_results:
      ift_detection_rate: 0.34
      ift_vs_mh_overlap: 0.78
      ift_unique_flags: 0.06
      mh_unique_flags: 0.04
      ift_uses_full_sample: true
      ift_avoids_cohort_splits: true
      ift_computational_cost_ratio: 12.0
      ift_release_date_coefficient_mean: 0.08
      ift_release_date_coefficient_std: 0.15
      reviewer_critique: "confirms temporal trend = capability gain"
    result_rationale: >
      Under worst tier, Item-Focused Trees detect 34% of items as having significant
      temporal DIF — nearly identical to MH's 31.3%. The 78% overlap confirms both
      methods detect the same phenomenon. The IFT release-date coefficient (mean=0.08,
      SD=0.15) is positive: items become easier over time, consistent with capability
      improvement. Reviewers read the continuous coefficient as: "DIF is a smooth
      function of time, not a discrete shift — this is exactly what capability
      improvement looks like. If contamination caused DIF, we'd expect discrete jumps
      when specific training data became available." The 12× computational cost over
      MH makes IFT impractical at scale. Reviewers conclude: "IFT confirms MH findings
      but adds computational cost and the interpretation that item changes are gradual
      (capability) not abrupt (contamination)."
    tables:
      - name: "Table 14: IFT vs MH Comparison"
        columns: [method, flagging_rate, unique_flags, cost_ratio, temporal_pattern]
        rows:
          - [MH_categorical, 0.313, 0.04, 1.0, "Discrete cohort split"]
          - [IFT_continuous, 0.34, 0.06, 12.0, "Smooth positive trend"]
          - [overlap, 0.78, "-", "-", "Same underlying signal"]
    figures_description:
      - "Fig 13: IFT temporal coefficient distribution. Positive skew (mean=0.08), indicating items become easier over time. Reviewer: 'Gradual easing = capability improvement.'"
    analysis: >
      IFT provides marginal methodological value but under worst tier confirms the
      capability-improvement interpretation via smooth temporal trends. Under reframe,
      the smooth trend is actually interesting: "capability-authentic items show
      predictable sensitivity to model generation — enabling prospective identification
      of items that will become less discriminative." Recommend as supplementary/appendix
      rather than main paper contribution.

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      DIF within decoder-only homogeneous subpopulation. IRT fit diagnostics.
      Compare FPR/TPR vs full-population DIF from plan_001.
    expected_results:
      n_decoder_only: 3400
      decoder_only_c_pct: 33.1
      decoder_only_irt_rmsea: 0.092
      decoder_only_irt_cfi: 0.81
      decoder_only_irt_tli: 0.78
      decoder_only_irt_srmr: 0.073
      full_population_c_pct: 31.3
      delta_c_pct: 1.8
      fpr_decoder_only: 0.33
      fpr_full_population: 0.318
      tpr_delta_p05: -0.02
      reviewer_critique: "architecture homogeneity doesn't fix the problem"
    result_rationale: >
      Under worst tier (explicitly specified in tier definition), architecture
      stratification fails to improve results. Decoder-only C% = 33.1% (vs 31.3%
      full population) — no meaningful reduction, slightly HIGHER. IRT fit remains
      poor: RMSEA=0.092 (>0.08), CFI=0.81 (<0.90), TLI=0.78 (<0.90). Removing
      encoder-decoder and hybrid architectures doesn't address the fundamental
      unidimensionality problem — MMLU's 57-subject structure violates unidimensional
      IRT regardless of architecture homogeneity. The C% increase from 31.3%→33.1%
      is within noise but reviewers spin it: "architecture stratification made things
      WORSE — DIF flags more items in a homogeneous population, confirming that flags
      reflect capability variation, not architecture confounding." FPR and TPR are
      essentially unchanged (ΔFPR=+0.01, ΔTPR=−0.02). Reviewers familiar with
      psychometrics argue: "RMSEA=0.092 on decoder-only models proves the IRT model
      is misspecified for MMLU. Your entire DIF analysis rests on an inappropriate
      measurement model. This is not fixable by subsetting — it requires multidimensional
      IRT, which you haven't implemented."
    tables:
      - name: "Table 15: Architecture Stratification Results"
        columns: [population, n_models, c_pct, rmsea, cfi, tli]
        rows:
          - [full_population, 5219, 31.3, "N/A (not computed)", "N/A", "N/A"]
          - [decoder_only, 3400, 33.1, 0.092, 0.81, 0.78]
          - [delta, "-1819", "+1.8", "FAIL (>0.08)", "FAIL (<0.90)", "FAIL (<0.90)"]
      - name: "Table 16: Detection Power Comparison"
        columns: [population, fpr_baseline, tpr_p05, tpr_p10, enrichment]
        rows:
          - [full_population, 0.318, 0.834, 1.0, 0.96]
          - [decoder_only, 0.33, 0.82, 0.99, 0.95]
          - [delta, "+0.012", "-0.014", "-0.01", "-0.01"]
    figures_description:
      - "Fig 14: IRT fit indices for decoder-only vs full population. All indices remain below acceptable thresholds. RMSEA shown with 90% CI entirely above 0.08 cutoff."
      - "Fig 15: DIF flagging rate comparison. Near-identical distributions between full and decoder-only populations, disproving the architecture confound hypothesis."
    analysis: >
      Architecture stratification is the critical missing experiment identified by
      worst-case Dream, and it produces the predicted negative result. Under worst tier,
      this closes the last escape route: DIF flagging rates cannot be reduced by
      controlling for architecture. The IRT misfit is structural (MMLU dimensionality)
      not population-driven. Under reframe, this becomes neutral: "DIF item sensitivity
      is robust to population composition — capability-authentic items are identified
      regardless of architecture mix." The IRT fit concern is acknowledged honestly but
      framed as "conservative: poor IRT fit means DIF may UNDERESTIMATE the true
      proportion of capability-sensitive items."

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      Inject known contamination into METABENCH response matrix. Measure DIF TPR/FPR
      against controlled ground truth. Vary injection parameters.
    expected_results:
      delta_tpr_p03: 0.222
      delta_tpr_p05: 0.508
      delta_tpr_p07: 0.664
      delta_tpr_p10: 0.674
      external_matching_fpr: 0.314
      within_matching_fpr_inflation: 0.186
      cross_subject_delta_fpr: 0.000
      cross_subject_delta_tpr_p05_avg: 0.36
      dose_response_present: true
      reviewer_critique: "synthetic injection mechanism unrealistic"
    result_rationale: >
      Under worst tier, semi-synthetic results (already observed) are technically sound
      but dismissed on ecological validity grounds. ΔTPR=0.508 at p=0.5 shows DIF
      detects injected contamination — but reviewers argue the injection mechanism
      (flip incorrect→correct with probability p) doesn't model real contamination.
      Real contamination involves: (1) partial memorization (model recalls fragments,
      not full answers), (2) shallow pattern matching (model exploits surface features),
      (3) chain-of-thought reasoning from memorized premises. None of these produce
      the clean incorrect→correct flipping that synthetic injection assumes. The
      dose-response curve (ΔTPR increases with p) is called "trivially expected — of
      course flipping more answers makes items behave more differently." The cross-
      subject matching innovation (ΔFPR=0.000) is acknowledged as methodologically
      sound, but reviewers argue "you've built a valid framework for detecting something
      that doesn't exist in the real world in this form." The gap between synthetic
      ΔTPR=0.508 and real enrichment=0.96 is the fatal disconnect: "Your method works
      perfectly on synthetic contamination and not at all on real data — this means
      your synthetic model is wrong, not that your ground truth is wrong."
    tables:
      - name: "Table 17: Semi-Synthetic Results Under Worst Interpretation"
        columns: [injection_rate_p, delta_tpr_standard, delta_tpr_cross_subject, reviewer_spin]
        rows:
          - [0.3, 0.222, 0.18, "Below useful detection"]
          - [0.5, 0.508, 0.36, "Only works at 50%+ exploitation"]
          - [0.7, 0.664, 0.52, "High exploitation = easy detection"]
          - [1.0, 0.674, 0.62, "Saturates — ceiling effect"]
      - name: "Table 18: Matching Strategy Comparison"
        columns: [matching, fpr_baseline, fpr_at_p10, delta_fpr, verdict]
        rows:
          - [standard_MH, 0.298, 0.616, "+0.318", "FPR inflates (contaminated matching var)"]
          - [external_5subj, 0.314, 0.314, 0.000, "FPR stable (clean matching var)"]
          - [cross_subject, 0.33, 0.33, 0.000, "FPR stable (recommended)"]
    figures_description:
      - "Fig 16: Dose-response curve. ΔTPR vs injection rate p. Monotonic increase but with diminishing returns. Reviewer annotation: 'Detection requires >50% exploitation — real contamination is partial.'"
      - "Fig 17: FPR comparison across matching strategies. Standard MH shows inflation; cross-subject matching maintains stable FPR. The methodological contribution is acknowledged even under worst tier."
    analysis: >
      Semi-synthetic validation is the strongest methodological contribution even under
      worst tier. The cross-subject matching innovation (ΔFPR=0.000) is genuinely novel
      and useful. Under reframe, the semi-synthetic framework is repositioned as
      "calibration infrastructure for item sensitivity analysis" — it characterizes
      how much differential signal is needed before DIF detects it, without claiming
      this maps to real contamination. The dose-response curve becomes "sensitivity
      calibration" rather than "contamination detection power." This experiment survives
      the reframe relatively intact.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "300e8deb-1a27-410e-9f74-56c702f62f7f",
  "isSidechain": false,
  "requestId": "req_011CbEroqzKYosL7jznTy8jZ",
  "type": "assistant",
  "uuid": "1c9be3c5-dfae-4f79-ad75-7860d9b7c9ae",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CfHisQ2E9fnvSr13CK47dh",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 16316,
      "cache_read_input_tokens": 11841,
      "output_tokens": 14210,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 16316,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 14210,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 16316,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 16316
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core DIF-as-detector narrative collapses — reviewers unify around 'this is just measuring capability improvement, not finding anything wrong with benchmar…",
  "leafUuid": "1c9be3c5-dfae-4f79-ad75-7860d9b7c9ae",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF benchmark characterization worst-case scenario analysis",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Core DIF-as-detector narrative collapses — reviewers unify around 'this is just measuring capability improvement, not finding anything wrong with benchmar…",
  "leafUuid": "1c9be3c5-dfae-4f79-ad75-7860d9b7c9ae",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF benchmark characterization worst-case scenario analysis",
  "sessionId": "79e7c2fe-a977-4e1b-aceb-6f83f3baf848"
}
```

---
