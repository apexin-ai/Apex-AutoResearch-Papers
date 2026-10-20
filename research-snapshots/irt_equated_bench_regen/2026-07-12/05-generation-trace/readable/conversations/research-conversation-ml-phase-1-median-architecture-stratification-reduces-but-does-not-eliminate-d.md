# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义： 含义：Architecture stratification reduces but does not eliminate DIF; instabilit

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 16
- **Recorded user turns:** 1
- **Tool calls:** 1
- **Original source:** `logs/chats/exported-trajectories/account-3/3dc50d3f-5ce4-43a1-86c4-2728856df457.jsonl`
- **Structured JSON:** [`c6dc530c207c6858021c.json`](../../sessions/c6/c6dc530c207c6858021c.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:35:05.833Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:35:05.833Z",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：\n\n含义：Architecture stratification reduces but does not eliminate DIF; instability mostly explained by capability improvement; semi-synthetic framework becomes the primary methodological contribution\n核心假设：['Decoder-only IRT fit improves modestly (RMSEA 0.03-0.05) — better than full population but not clean', 'Decoder-only temporal DIF C% drops to 15-24% — meaningful reduction from 31%, but still substantively large', \"Instability decomposition: partial ρ (controlling domain accuracy) drops below significance (p>0.10) — most DIF is explained by 'models got better at those domains'\", 'Non-uniform DIF check shows 40-69% overlap — some MH flags are uniform-only artifacts', 'All existing completed experiment results hold (no reanalysis surprises)']\n关键指标范围：{'decoder_only_c_pct': [15, 24], 'decoder_only_irt_rmsea': [0.03, 0.05], 'decoder_only_irt_cfi': [0.9, 0.95], 'partial_rho_controlling_domain_accuracy': [0.02, 0.14], 'partial_rho_p_value': [0.1, 0.6], 'non_uniform_mh_overlap_pct': [40, 69], 'claims_at_full_strength': [2, 3]}\n叙事方向：Claim 1 softens: '15-24% of items show large DIF even in architecture-homogeneous populations' — still substantial but honest that full-population 31% was inflated by architecture heterogeneity. Drop '38% instability' headline; lead with '~20% items function differently across model generations, largely driven by domain-specific capability improvement.' Claim 2 (ground truth meta-critique) and Claim 3 (semi-synthetic framework) are unaffected — pivot these to primary contributions. Claim 4 downstream impact recalculates with lower DIF count; ranking redundancy finding (ρ≈0.997) actually strengthens since fewer items removed. Reframe paper emphasis: semi-synthetic validation framework (ΔFPR=0.000 cross-subject matching) as main methodological contribution, with DIF characterization as motivating empirical finding rather than headline result. GSM1K cross-benchmark validation (r=−0.478) provides independent support. Paper remains competitive for ICLR but with 'validation methodology + empirical characterization' framing rather than 'massive instability discovery' framing.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: 31.3% (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). Architecture-stratified estimate (decoder-only subset) TBD — plan_010 executing. Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). The >15% finding holds at standard thresholds [1.0, 2.0]; at the conservative 2.5 threshold, 10.2% (1,278 items) still exhibit large DIF. BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 ETS C items at 1.5 threshold).\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified TBD), plan_018 (threshold sensitivity: 48.9%/31.3%/18.3%/10.2% at 1.0/1.5/2.0/2.5; BH correction negligible)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — instability decomposition (partial out domain accuracy improvement) TBD\n- IRT fit: Full-population fit indices TBD from plan_010; if decoder-only fit substantially improves, lead with that subset as primary\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling METABENCH accuracy, p=0.023; permutation p=0.014). Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33 CI upper bound |r|=0.16 (small effect possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]). DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling accuracy). We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 28–38% instability at unprecedented scale (5,227×12,508), (2) the ground truth meta-critique affecting the field's validation methodology, (3) the semi-synthetic validation framework with cross-subject matching innovation (ΔFPR=0.000), (4) DIF as diagnostic lens revealing benchmark measurement structure. Explicitly acknowledge MH-DIF is applied without modification; novelty is empirical characterization + framework design, not algorithmic. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem — the scale creates novel statistical challenges (architecture heterogeneity, multidimensional construct, 5000+ examinees).\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.\n\n10. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: median\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:35:05.837Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:35:05.837Z",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457"
}
```

---

## Round 1

14 recorded events

### User

_source line 3 · 2026-05-21T03:35:05.859Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：

含义：Architecture stratification reduces but does not eliminate DIF; instability mostly explained by capability improvement; semi-synthetic framework becomes the primary methodological contribution
核心假设：['Decoder-only IRT fit improves modestly (RMSEA 0.03-0.05) — better than full population but not clean', 'Decoder-only temporal DIF C% drops to 15-24% — meaningful reduction from 31%, but still substantively large', "Instability decomposition: partial ρ (controlling domain accuracy) drops below significance (p>0.10) — most DIF is explained by 'models got better at those domains'", 'Non-uniform DIF check shows 40-69% overlap — some MH flags are uniform-only artifacts', 'All existing completed experiment results hold (no reanalysis surprises)']
关键指标范围：{'decoder_only_c_pct': [15, 24], 'decoder_only_irt_rmsea': [0.03, 0.05], 'decoder_only_irt_cfi': [0.9, 0.95], 'partial_rho_controlling_domain_accuracy': [0.02, 0.14], 'partial_rho_p_value': [0.1, 0.6], 'non_uniform_mh_overlap_pct': [40, 69], 'claims_at_full_strength': [2, 3]}
叙事方向：Claim 1 softens: '15-24% of items show large DIF even in architecture-homogeneous populations' — still substantial but honest that full-population 31% was inflated by architecture heterogeneity. Drop '38% instability' headline; lead with '~20% items function differently across model generations, largely driven by domain-specific capability improvement.' Claim 2 (ground truth meta-critique) and Claim 3 (semi-synthetic framework) are unaffected — pivot these to primary contributions. Claim 4 downstream impact recalculates with lower DIF count; ranking redundancy finding (ρ≈0.997) actually strengthens since fewer items removed. Reframe paper emphasis: semi-synthetic validation framework (ΔFPR=0.000 cross-subject matching) as main methodological contribution, with DIF characterization as motivating empirical finding rather than headline result. GSM1K cross-benchmark validation (r=−0.478) provides independent support. Paper remains competitive for ICLR but with 'validation methodology + empirical characterization' framing rather than 'massive instability discovery' framing.

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen

## paper_framing.md

# Paper Framing — irt_equated_bench_regen

## Target Venue
- Primary: ICLR 2027 (expected deadline ~October 2026)

## Paper Type
Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."

## Core Claims (4 条, 可证伪)

**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: 31.3% (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). Architecture-stratified estimate (decoder-only subset) TBD — plan_010 executing. Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). The >15% finding holds at standard thresholds [1.0, 2.0]; at the conservative 2.5 threshold, 10.2% (1,278 items) still exhibit large DIF. BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 ETS C items at 1.5 threshold).
- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified TBD), plan_018 (threshold sensitivity: 48.9%/31.3%/18.3%/10.2% at 1.0/1.5/2.0/2.5; BH correction negligible)
- Honesty requirement: ρ=0.307 means "item instability" may mainly reflect "models got better at those domains" — instability decomposition (partial out domain accuracy improvement) TBD
- IRT fit: Full-population fit indices TBD from plan_010; if decoder-only fit substantially improves, lead with that subset as primary

**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)
- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection"

**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability

**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.
4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling METABENCH accuracy, p=0.023; permutation p=0.014). Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.
- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)
- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.
- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
- Caveats (→ limitations): N=33 CI upper bound |r|=0.16 (small effect possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed

## Story Spine

**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.

**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.

**What we find**: Three discoveries, each a contribution:

1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.

2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.

3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.

4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]). DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.

**Headline result**: "Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling accuracy). We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000)."

## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks

Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.

## Venue Fit

- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.
- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 28–38% instability at unprecedented scale (5,227×12,508), (2) the ground truth meta-critique affecting the field's validation methodology, (3) the semi-synthetic validation framework with cross-subject matching innovation (ΔFPR=0.000), (4) DIF as diagnostic lens revealing benchmark measurement structure. Explicitly acknowledge MH-DIF is applied without modification; novelty is empirical characterization + framework design, not algorithmic. Frame as "bringing mature psychometric tools to characterize an urgent ML evaluation problem — the scale creates novel statistical challenges (architecture heterogeneity, multidimensional construct, 5000+ examinees)."

## Anticipated Reviewer Concerns (updated for pivot)

1. **"38% could just mean models got better"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.

2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.

3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.

4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.

5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.

6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.

7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.

8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.

9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.

10. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.

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
  "promptId": "8c0b757f-ee8c-4965-866b-e2315f8e0d60",
  "type": "user",
  "uuid": "854db3a2-8e51-4266-b872-3ab67c1d7e1d",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:35:05.858Z_

```json
{
  "parentUuid": "854db3a2-8e51-4266-b872-3ab67c1d7e1d",
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
  "uuid": "762f1f47-1269-40ff-971a-53b3a8086319",
  "timestamp": "2026-05-21T03:35:05.858Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:35:05.858Z_

```json
{
  "parentUuid": "762f1f47-1269-40ff-971a-53b3a8086319",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "5c8209de-0471-4c18-b478-3109bd6e56f6",
  "timestamp": "2026-05-21T03:35:05.858Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Architecture stratification reduces but does not eliminate DIF; instability mostly explained by capability improvement; semi-synthetic framework becomes…",
  "leafUuid": "5c8209de-0471-4c18-b478-3109bd6e56f6",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis characterization with semi-synthetic validation",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:35:08.808Z_

I'll analyze the experiment plan to identify all `planned` experiments and generate detailed median-tier predictions for each.

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "5c8209de-0471-4c18-b478-3109bd6e56f6",
  "isSidechain": false,
  "requestId": "req_011CbF1hhS1EzxYNUCx9PgrN",
  "type": "assistant",
  "uuid": "f3ee1681-5c53-43e5-8812-2281240f5147",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wr7ebJk29Jz4vKHypixWmq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17171,
      "cache_read_input_tokens": 11841,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 137,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17171
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

### Tool call

_source line 9 · 2026-05-21T03:35:10.879Z_

<details open><summary>🔧 Tool call — Read · `toolu_01DXr9HFxM3qZuKJCkNTC59d`</summary>

```json
{
  "file_path": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/.claude/CLAUDE.md",
  "offset": 0,
  "limit": 50
}
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f3ee1681-5c53-43e5-8812-2281240f5147",
  "isSidechain": false,
  "requestId": "req_011CbF1hhS1EzxYNUCx9PgrN",
  "type": "assistant",
  "uuid": "c1dcee57-544e-4fe7-a7f2-32383dddbf9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01Wr7ebJk29Jz4vKHypixWmq",
    "type": "message",
    "stop_reason": "tool_use",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17171,
      "cache_read_input_tokens": 11841,
      "output_tokens": 137,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17171,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 137,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17171,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17171
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

### Tool result

_source line 10 · 2026-05-21T03:35:10.895Z_

<details><summary>↩ Tool result · `toolu_01DXr9HFxM3qZuKJCkNTC59d`</summary>

```text
0	
1	## 输出风格
2	
3	- 回复简洁直接，不说废话
4	- 禁止客套开场（"好的！"、"没问题！"、"这是个好问题！"）和结束语（"希望对你有帮助！"、"如果还有问题请随时问！"）
5	- 不要复述用户的问题
6	- 不要给未被要求的建议或补充说明
7	- 推理要彻底，但输出只保留结论和必要信息
8	
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "user",
  "parentUuid": "c1dcee57-544e-4fe7-a7f2-32383dddbf9c",
  "isSidechain": false,
  "promptId": "8c0b757f-ee8c-4965-866b-e2315f8e0d60",
  "type": "user",
  "uuid": "f605270f-11e7-4147-8df3-46da3607ed48",
  "toolUseResult": {
    "type": "text",
    "file": {
      "filePath": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2/.claude/CLAUDE.md",
      "content": "\n## 输出风格\n\n- 回复简洁直接，不说废话\n- 禁止客套开场（\"好的！\"、\"没问题！\"、\"这是个好问题！\"）和结束语（\"希望对你有帮助！\"、\"如果还有问题请随时问！\"）\n- 不要复述用户的问题\n- 不要给未被要求的建议或补充说明\n- 推理要彻底，但输出只保留结论和必要信息\n",
      "numLines": 9,
      "startLine": 0,
      "totalLines": 9
    }
  },
  "sourceToolAssistantUUID": "c1dcee57-544e-4fe7-a7f2-32383dddbf9c",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Assistant

_source line 11 · 2026-05-21T03:36:44.474Z_

<details><summary>Logged reasoning block</summary>

```text
Let me identify all planned experiments from the experiment_plan. Looking at the status field:

1. plan_001 - status: planned (but registry shows plan_001_real_data_dif_mmlu as DONE)
2. plan_002 - status: planned
3. plan_003a - status: planned
4. plan_003b - status: planned
5. plan_003c - status: planned
6. plan_004 - status: planned (but registry shows plan_004_gsm8k_cross_benchmark as DONE)
7. plan_005 - status: planned


8. plan_006 - status: planned
9. plan_007 - status: planned
10. plan_008 - status: planned
11. plan_009 - status: planned
12. plan_010 - status: planned
13. plan_011 - status: planned (but registry shows plan_011_semi_synthetic_validation as DONE)

There's a discrepancy here—the experiment_plan marks everything as "planned" but the registry shows several as DONE. Since the user wants detailed data for each planned experiment in the experiment_plan, I should focus on those marked as planned in that file, though I'm noticing this mismatch might be important to clarify.

Looking more carefully, the truly planned experiments that haven't appeared in the registry as completed are plan_002 through plan_009, with some gaps where others have already been executed. I need to generate predictions for these remaining planned experiments. Looking at the registry, I can see plan_017 and plan_004 are also marked as done. So the remaining unexecuted experiments are plan_002 through plan_010 — that's ten planned studies covering robustness validation, perturbation evaluation, ensemble methods, bifactor IRT, item generation, Bayesian approaches, degradation analysis, and stratified DIF analysis. plan_006 through plan_010 are the remaining experiments I need to generate predictions for. Looking at the median tier narrative, the key insight is that architecture stratification reduces DIF but doesn't eliminate it, with instability primarily driven by capability improvements rather than other factors. The semi-synthetic framework emerges as the main methodological contribution. I'll use the specified metric ranges—decoder_only_c_pct between 15-24%, RMSEA between 0.03-0.05, CFI between 0.9-0.95, and partial correlations between 0.02-0.14—to ground my predictions for each remaining experiment.

For plan_010, the architecture stratification experiment is critical because it directly tests whether decoder-only models show the predicted DIF reduction, with C% dropping meaningfully from 31.3% to the 15-24% range and IRT fit improving modestly. Plan_002 on RL robustness faces a practical constraint: only about 13 reasoning-RL models exist in METABENCH, making the sample too small for strong conclusions, though DIF flags should remain largely consistent when adding these models.

Plan_003a tests ConStat perturbation effectiveness on non-RL models where it should show moderate detection power, though paraphrasing quality varies across MMLU subjects and RL models remain harder to detect. Plan_003b examines generation variance through DVD, expecting bimodal distributions on some items but limited by the computational cost of open-weight model inference.

Plan_003c (ensemble fusion) depends on both prior plans and becomes future work if the ensemble claim is dropped. Plan_005 (bifactor IRT equating) faces the same within-subject contamination issues that killed the earlier bifactor approach, making it deprioritized in the median tier. Plan_006 (item generation calibration) depends on bifactor success, so it loses relevance if that direction is abandoned.

Plan_007 (Bayesian DIF) is a simulation study with no GPU requirements that should deliver the expected mathematical results—showing power improvement from around 0.40 to 0.70 after three administrations—though it's supplementary in the median tier. Plan_008 (graceful degradation analysis) depends on the bifactor and regeneration work, so it shifts to future work given those are dropped. Plan_009 (item-focused trees) offers an alternative DIF method using continuous release dates for additional insight, though it remains supplementary analysis in the median tier.

Now I'm clarifying what's actually planned versus what the paper framing indicates was dropped or deferred. The ensemble methods were never executed, regeneration got killed by the bifactor pre-check, and RL robustness has limitations due to insufficient sample size. So the truly relevant planned experiments in the median tier are the architecture-stratified DIF (the critical one), RL robustness at the limitations level, Bayesian DIF as supplementary, and item-focused trees as supplementary. The others are acknowledged as dropped or future work, but since the user asked for predictions across all planned experiments, I should generate them anyway.

Now I'm constructing the full YAML output with the median tier parameters for plan_010, including the decoder-only model counts, temporal reference and focus sample sizes, control percentage, IRT fit indices, and population-level comparisons.

Continuing with plan_002's median tier, I'm documenting the reasoning RL model count, DIF retention ratios showing stability when adding RL models, AUROC values for both constraint and mink conditions across RL and non-RL settings, equivalence test results, and the partial exploitation detection boundary around p≈0.5.

Moving into plan_003a's median tier parameters...

For plan_003b, I'm tracking 12 models tested with bimodal detection rates between 15-30%, and TPR/FPR metrics for both verbatim and variant DVD conditions.

Plan_003c shows ensemble coverage ranging from 0.55-0.70 with FPR between 0.08-0.12.

Moving to plan_005, the bifactor model only partially converges with some subjects, general factor loadings around 0.30-0.50, but there aren't enough clean anchor items per subject and the equated rho model fails to converge entirely—plan_014's pre-checks already flagged this as unviable.

Plan_006 depends on plan_005's convergence, which won't happen, so the difficulty correlations (0.25-0.40 with prompts, 0.55-0.70 with student similarity) and the 100-200 generated items with a 3.2/5 human quality rating are compromised from the start.

For plan_008, I'm looking at how replacement validity holds up across different percentages—staying above 0.99 for 5% replacement down to 0.88 for 50% replacement—though this also depends on the earlier plans that are already problematic. Plan_009 shows the IFT detection power matches categorical DIF detection with a monotonic trend in DIF over time, sidestepping arbitrary cutoffs.

Some subjects display non-linear patterns that complicate the picture, but these are supplementary findings. Now I'm thinking about how to structure this as YAML with proper rationales for each result. The instability decomposition is really the crux—when I control for domain accuracy, the partial correlation drops to 0.02-0.14 and loses significance, suggesting most of the DIF effect is actually just domains where models improved. This finding could fit into plan_010 or as a reanalysis of plan_001, which already showed domain_spearman_rho=0.307 at p=0.02, so the median tier's result would be a natural extension showing that relationship doesn't hold once you account for the underlying accuracy gains.

For the non-uniform DIF check with that 40-69% overlap range, I should include it as part of plan_010's robustness checks since it addresses reviewer concern #9 about SIBTEST and logistic regression approaches. Now I need to reconcile what's actually planned versus what's already in the registry—the experiment_plan lists everything as "planned" but many appear completed. The user's request is specifically for detailed data on each planned experiment, so I think they want me to either fill in results for completed ones or expand the planned ones with actual findings.

Looking at what's truly not yet in the registry as DONE, I have ten experiments that need detailed predictions: the RL robustness validation, the perturbation and variance evaluations, ensemble fusion, the bifactor IRT equating pilot, item generation calibration, cumulative Bayesian DIF, graceful degradation analysis, item-focused trees, and the architecture-stratified DIF analysis. Let me work through generating the detailed predictions for each of these.

Now I'm thinking through the median tier narrative more carefully to keep everything consistent. The core story is that architecture stratification reduces but doesn't fully eliminate DIF, making plan_010 essential to the argument. Most of the instability traces back to capability improvement rather than fundamental measurement issues. The semi-synthetic framework becomes the methodological centerpiece, which means plans 011 and 016 already provide that contribution. The first claim softens to account for residual DIF even in homogeneous populations, while the other claims hold. The fourth claim actually strengthens because recalculating with fewer DIF instances gives a higher correlation. The paper's framing shifts away from "massive instability discovery" toward methodology and characterization.

For the experiments I'm dropping—the perturbation and variance evaluations, ensemble fusion, bifactor IRT equating, item generation calibration, graceful degradation, and item-focused trees—the median tier predicts they either get deprioritized or, if they do run, yield mixed or inconclusive results.
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "f605270f-11e7-4147-8df3-46da3607ed48",
  "isSidechain": false,
  "requestId": "req_011CbF1i4ne9xhQb7awoRBjs",
  "type": "assistant",
  "uuid": "3e44c9df-06e4-4743-b471-de592a7ce9c4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6XxA9VFrbL45T6oWYcWsK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 29012,
      "output_tokens": 16639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16639,
          "cache_read_input_tokens": 29012,
          "cache_creation_input_tokens": 309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 309
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

_source line 12 · 2026-05-21T03:41:08.049Z_

```yaml
tier: median
narrative_guidance: >
  Architecture stratification (plan_010) is the pivot point: decoder-only C% drops to ~19%,
  confirming architecture heterogeneity inflated the full-population 31% estimate by ~12pp.
  Instability decomposition shows partial ρ (controlling domain accuracy) falls below significance,
  meaning most remaining DIF reflects "models improved at those domains" rather than item malfunction.
  Semi-synthetic framework (already validated in plan_011/016) becomes the primary methodological
  contribution. Paper reframes from "massive instability discovery" to "validation methodology +
  empirical characterization." Claims 2/3 untouched; Claim 1 softened but honest; Claim 4
  strengthened (fewer items removed → ρ≈0.997 even more robust). Ensemble (003a/b/c) and
  regeneration (005/006/008) deprioritized — acknowledged as future work. RL robustness (002)
  is limitations-level due to N=13. Remaining experiments (007, 009) are supplementary
  methodological extensions.

imagined_experiments:
  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      DIF within decoder-only models only. THE critical median-tier experiment.
      Tests whether removing architecture heterogeneity (encoder-decoder, mixture-of-experts,
      hybrid models) improves IRT fit and reduces spurious DIF.
    expected_results:
      decoder_only_n_total: 3482
      decoder_only_n_ref_2023: 876
      decoder_only_n_foc_2024h1: 498
      decoder_only_irt_rmsea: 0.042
      decoder_only_irt_cfi: 0.923
      decoder_only_irt_tli: 0.908
      decoder_only_irt_srmr: 0.038
      full_population_irt_rmsea: 0.073
      full_population_irt_cfi: 0.841
      decoder_only_temporal_c_pct: 19.2
      decoder_only_temporal_c_count: 2402
      full_population_c_pct_comparison: 31.3
      reduction_pct_points: 12.1
      decoder_only_sanity_random_split_c_pct: 0.14
      decoder_only_enrichment_vs_li: 0.94
      partial_rho_controlling_domain_accuracy: 0.08
      partial_rho_p_value: 0.31
      zero_order_rho_domain_accuracy: 0.29
      zero_order_rho_p_value: 0.03
      non_uniform_dif_logistic_regression_flagged_pct: 14.3
      non_uniform_mh_overlap_pct: 58
      instability_decomposition_explained_by_capability: 0.74
    result_rationale: >
      Full-population 31.3% includes DIF driven by fundamental architectural differences
      (encoder-decoder vs decoder-only have systematically different item response profiles
      — e.g., encoder-decoder models handle long-context items differently). Removing
      ~1,700 non-decoder-only models eliminates this architecture confound. RMSEA improves
      from ~0.07 to ~0.04 because unidimensional IRT fits better when the population
      shares a common cognitive architecture — architecture heterogeneity introduced
      multidimensionality that violated the unidimensional assumption. However, RMSEA
      doesn't reach <0.03 ("good fit") because MMLU's 57-subject structure still creates
      multidimensionality within decoder-only models. C% drops to ~19% because roughly
      12pp of the original DIF was architecture-driven (items where encoder-decoder
      models systematically differed from decoder-only regardless of temporal cohort).
      The remaining 19% represents genuine temporal DIF within a homogeneous architecture.
      Partial ρ controlling domain accuracy drops below significance (p=0.31) because
      decoder-only models' temporal improvement is more uniformly distributed across
      domains than the full population — the full-population ρ=0.307 was partly driven
      by architecture-specific domain strengths. This means the remaining 19% DIF is
      largely explained by "decoder-only models improved more in certain domains across
      generations." Non-uniform DIF check via logistic regression shows ~58% overlap
      with MH flags, meaning ~42% of MH flags capture uniform-only artifacts that
      wouldn't appear under a method sensitive to non-uniform DIF — a non-trivial
      artifact rate that honest reporting must acknowledge.
    tables:
      - name: "Table: IRT Fit Comparison"
        columns: [population, N, RMSEA, CFI, TLI, SRMR]
        rows:
          - [full_population, 5219, 0.073, 0.841, 0.822, 0.061]
          - [decoder_only, 3482, 0.042, 0.923, 0.908, 0.038]
      - name: "Table: DIF Rate Comparison"
        columns: [population, C_pct, C_count, sanity_pct, enrichment]
        rows:
          - [full_population, 31.3, 3918, 0.18, 0.96]
          - [decoder_only, 19.2, 2402, 0.14, 0.94]
      - name: "Table: Instability Decomposition"
        columns: [analysis, rho, p_value, interpretation]
        rows:
          - [zero_order_domain_accuracy, 0.29, 0.03, "DIF correlates with domain improvement"]
          - [partial_controlling_domain_accuracy, 0.08, 0.31, "DIF not significant after controlling for capability gain"]
          - [explained_variance_ratio, 0.74, "—", "74% of DIF variance attributable to domain-specific capability improvement"]
    figures_description:
      - "Scatter plot: decoder-only C% vs full-population C% per MMLU subject, showing systematic reduction. Diagonal line (y=x) for reference; points cluster below, especially subjects with high architecture-dependent performance."
      - "Bar chart: IRT fit metrics (RMSEA, CFI) side-by-side for full-population vs decoder-only, with conventional threshold lines (RMSEA=0.05 'acceptable', 0.08 'mediocre')."
      - "Instability decomposition: path diagram showing zero-order ρ=0.29 decomposed into direct effect (partial ρ=0.08, n.s.) and indirect effect via domain accuracy (0.21)."
    analysis: >
      Median-tier result: architecture stratification reduces C% by ~12pp (31→19%), confirming
      that architecture heterogeneity was a substantial but not sole driver of DIF. IRT fit
      improves to "acceptable" range (RMSEA<0.05) but not "good" (<0.03), reflecting
      residual multidimensionality from MMLU's 57 subjects. The instability decomposition
      is the key analytical finding: partial ρ dropping below significance means we cannot
      claim item instability is independent of capability improvement. Lead with "~19% of items
      show large DIF even within architecture-homogeneous decoder-only models, largely driven
      by domain-specific capability gains across model generations." This is honest, substantive,
      and still novel — no prior work has characterized this at scale. Non-uniform DIF overlap
      of 58% means roughly 4 in 10 MH flags are uniform-only artifacts, supporting the
      recommendation to use logistic regression DIF as a robustness check. For the paper:
      report decoder-only as primary analysis, full-population as sensitivity analysis showing
      architecture inflation. Claim 1 headline shifts from "31-38% instability" to "~19%
      items function differently across decoder-only model generations."

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      Validate DIF robustness to RL training. Core challenge: only ~13 reasoning-RL
      models available. Group-level DIF stability tested by adding RL models to focal
      cohort. Model-level comparison of DIF vs traditional detectors on RL models.
    expected_results:
      n_reasoning_rl_models_available: 13
      n_alignment_rl_models: 477
      dif_flag_retention_ratio_with_rl: 0.91
      dif_flag_jaccard_with_vs_without_rl: 0.87
      dif_c_pct_with_rl_added: 30.1
      dif_c_pct_without_rl: 31.3
      constat_auroc_non_rl: 0.72
      constat_auroc_rl: 0.54
      mink_auroc_non_rl: 0.68
      mink_auroc_rl: 0.51
      dif_group_level_robust: true
      tost_equivalence_p: 0.18
      tost_equivalence_conclusion: inconclusive
      bootstrap_ci_auroc_diff_dif_vs_constat: [-0.08, 0.22]
      partial_exploitation_detection_boundary_p: 0.50
      partial_exploitation_tpr_at_p04: 0.12
      partial_exploitation_tpr_at_p06: 0.45
      partial_exploitation_tpr_at_p10: 0.83
    result_rationale: >
      DIF is a group-level statistic computed across the entire focal cohort (N≈650).
      Adding 13 RL models to a 650-model cohort shifts group proportions by <2%,
      so DIF flags are inherently stable (retention ratio ~0.91). The ~9% flag change
      reflects slight shifts in MH stratification from RL models' unusual ability
      profiles (reasoning-RL models have high math/logic but variable MMLU performance).
      Traditional detectors (ConStat, Min-K%) degrade on RL models because they rely
      on per-model distributional assumptions that PPO clipping disrupts: Min-K%'s
      token-level likelihood distribution becomes less discriminative when PPO
      flattens the likelihood landscape; ConStat's perturbation sensitivity is
      confounded by RL-trained robustness to paraphrase. DIF avoids this because
      it operates on binary correct/incorrect at the item level, not token-level
      distributions. TOST equivalence testing is inconclusive (p=0.18) because N=13
      provides insufficient power for equivalence bounds of ±0.10 — the CI is too
      wide to reject the null of non-equivalence. Partial exploitation analysis
      shows a detection cliff at p≈0.50: below 50% exploitation rate, DIF effect
      size (Δ_MH) drops below the ETS C threshold of 1.5, making detection
      unreliable. This is an honest power limitation consistent with simulation
      results (mvp_dif_power_sim: operational region requires δ≥1.4).
    tables:
      - name: "Table: Detection Power by Method × Model Type"
        columns: [method, non_rl_auroc, alignment_rl_auroc, reasoning_rl_auroc]
        rows:
          - [DIF_group_level, 0.83, 0.83, 0.83]
          - [ConStat, 0.72, 0.66, 0.54]
          - [Min-K%, 0.68, 0.62, 0.51]
      - name: "Table: DIF Flag Stability Under Cohort Composition Change"
        columns: [cohort_composition, c_pct, jaccard_vs_baseline, delta_c_pct]
        rows:
          - [temporal_no_rl, 31.3, 1.00, 0.0]
          - [temporal_with_alignment_rl, 30.8, 0.94, -0.5]
          - [temporal_with_reasoning_rl, 30.1, 0.87, -1.2]
          - [temporal_with_all_rl, 29.7, 0.85, -1.6]
    figures_description:
      - "Detection power curve: AUROC vs exploitation rate p for DIF, ConStat, Min-K%. Shows DIF detection cliff at p≈0.50, ConStat degradation starting earlier for RL models."
      - "Violin plot: per-model scores for 13 reasoning-RL models under each detector, showing Min-K% and ConStat distributions collapsing toward random while DIF flags remain stable."
    analysis: >
      In median tier, this experiment produces suggestive but not definitive results.
      DIF group-level robustness is nearly tautological with N=13 (adding 2% of the cohort
      can't meaningfully shift group statistics). The more interesting finding — traditional
      detector degradation on RL models — is underpowered (N=13 yields wide CIs on AUROC
      differences). TOST inconclusive means we cannot formally claim equivalence. For the
      paper: report as "preliminary evidence consistent with theoretical RL-robustness
      prediction" in limitations section, not as a validated claim. The partial exploitation
      analysis (detection boundary at p≈0.50) is the most useful output — it honestly
      characterizes DIF's operational envelope and provides the power analysis reviewers
      will ask for. Recommend framing: "DIF's binary response design is theoretically
      robust to RL training; empirical validation requires larger reasoning-RL samples
      as these models proliferate."

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      Independent evaluation of ConStat perturbation testing on MMLU. Paraphrase 200+
      items, measure detection power on non-RL vs RL models. Provides baseline for
      ensemble comparison (plan_003c). Dropped from main claims; supplementary analysis.
    expected_results:
      n_items_paraphrased: 216
      n_paraphrases_per_item: 5
      paraphrase_quality_human_judged_equivalence: 0.84
      n_models_tested: 15
      constat_tpr_non_rl_fdr005: 0.38
      constat_tpr_rl_fdr005: 0.14
      constat_fpr_fdr005: 0.07
      constat_auroc_non_rl: 0.71
      constat_auroc_rl: 0.53
      subject_variance_in_paraphrase_quality: 0.12
      worst_paraphrase_subjects: [formal_logic, abstract_algebra]
      best_paraphrase_subjects: [high_school_geography, business_ethics]
    result_rationale: >
      ConStat detection power on non-RL models (TPR≈0.38 at FDR 0.05) is moderate because
      memorized items show statistically significant performance drops under paraphrase
      (the contamination signal is real). FDR control at 0.05 is conservative, limiting
      sensitivity. RL models show TPR≈0.14 because PPO/DPO training builds robustness
      to surface-level perturbations — the model generalizes the memorized answer pattern
      to paraphrases, eliminating the performance gap ConStat relies on. Paraphrase
      quality at 84% reflects the difficulty of preserving semantic equivalence in
      formal logic and abstract algebra (where precise notation matters), while
      factual-knowledge subjects paraphrase cleanly. The 16% non-equivalent paraphrases
      inflate FPR slightly (a model answering differently because the question changed
      meaning, not because of contamination). AUROC of 0.71 (non-RL) is respectable
      but below DIF's group-level power because ConStat operates per-model, requiring
      multiple paraphrases per item to achieve significance — a sample efficiency
      disadvantage vs DIF's use of the full model population.
    tables:
      - name: "Table: ConStat Detection by Model Type"
        columns: [model_type, N, TPR_fdr005, FPR_fdr005, AUROC]
        rows:
          - [non_rl, 10, 0.38, 0.07, 0.71]
          - [alignment_rl, 3, 0.22, 0.06, 0.62]
          - [reasoning_rl, 2, 0.14, 0.09, 0.53]
    figures_description:
      - "Heatmap: paraphrase quality (semantic equivalence score) by MMLU subject category, highlighting subjects where paraphrasing preserves/degrades meaning."
      - "ROC curves: ConStat detection power stratified by model type (non-RL, alignment-RL, reasoning-RL)."
    analysis: >
      In median tier, ConStat produces a credible but modest baseline. The key finding —
      RL-induced robustness degrades perturbation-based detection — is directionally correct
      but underpowered (only 2-3 reasoning-RL models). Paraphrase quality variance across
      subjects is a genuine methodological concern that the ensemble paper would need to
      address. Since ensemble claim (003c) is dropped from the paper, this experiment's
      value is as a comparison method in the related work / baselines section. Report
      ConStat AUROC alongside DIF to show complementary detection profiles rather than
      superiority claims. Not worth allocating 80 GPU-hours for a supplementary result.

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      Independent evaluation of DVD generation variance on MMLU. Measure bimodal
      response distributions indicative of contamination. Requires inference on 10-15
      open-weight models. Dropped from main claims; supplementary analysis.
    expected_results:
      n_models_tested: 12
      n_responses_per_item: 50
      temperature: 0.8
      bimodal_detection_rate_all_items: 0.18
      bimodal_detection_rate_dif_flagged: 0.27
      bimodal_detection_rate_clean: 0.12
      dvd_tpr_verbatim_contamination: 0.48
      dvd_tpr_variant_contamination: 0.23
      dvd_fpr: 0.09
      dvd_auroc_overall: 0.67
      dvd_dif_agreement_jaccard: 0.15
      generation_cost_gpu_hours: 65
    result_rationale: >
      DVD detects contamination through response consistency: a contaminated model
      produces nearly identical correct answers across temperature samples (low
      variance), while an uncontaminated model shows natural variation. Bimodal
      detection rate of 18% overall (27% on DIF-flagged items) reflects that not
      all contamination produces zero-variance responses — partial memorization
      and stochastic decoding create intermediate variance profiles. TPR for verbatim
      contamination (0.48) exceeds variant contamination (0.23) because verbatim
      memorization produces the sharpest variance collapse; variant contamination
      (paraphrased training data) still allows response diversity. The low
      DIF-DVD Jaccard agreement (0.15) confirms these methods detect different
      contamination signals: DIF detects items that function differently across
      model cohorts (group-level), while DVD detects per-model memorization artifacts
      (individual-level). FPR of 0.09 is acceptable but non-trivial — some
      genuinely easy items produce low response variance without contamination
      (ceiling effect confound). GPU cost is substantial (65 hours for 12 models ×
      50 responses × 12,508 items) relative to the supplementary nature of this result.
    tables:
      - name: "Table: DVD Detection by Contamination Type"
        columns: [contamination_type, TPR, FPR, AUROC, N_items]
        rows:
          - [verbatim, 0.48, 0.09, 0.72, 216]
          - [variant, 0.23, 0.09, 0.58, 216]
          - [none_baseline, "—", 0.09, "—", 12508]
    figures_description:
      - "Bimodal distribution examples: response variance histograms for representative contaminated vs clean items across 12 models."
      - "Scatter: DVD score vs DIF Δ_MH for each item, colored by Li et al. label, showing low correlation (different detection signals)."
    analysis: >
      DVD provides complementary signal to DIF but at high GPU cost for a supplementary
      result. The low Jaccard with DIF (0.15) is actually the most interesting finding —
      it empirically demonstrates that item-level contamination is multifaceted: some
      items are differentially contaminated across cohorts (DIF catches), others are
      memorized by individual models without cohort-level effects (DVD catches). In
      median tier, this experiment is deprioritized (70 GPU-hours for a dropped claim).
      If executed, results support the "complementary detection" narrative but don't
      change the paper's core claims. Recommend deferring to future work unless GPU
      budget is unconstrained.

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      Fuse DIF + ConStat + DVD into multi-signal ensemble. Depends on 003a and 003b.
      Dropped from paper claims — ensemble (original Claim 2) never executed.
    expected_results:
      ensemble_2of3_tpr: 0.55
      ensemble_2of3_fpr: 0.06
      ensemble_weighted_tpr: 0.61
      ensemble_weighted_fpr: 0.09
      ensemble_auroc_overall: 0.76
      best_single_signal_auroc: 0.71
      ensemble_improvement_over_best_single: 0.05
      cross_validation_weight_stability: moderate
      dif_optimal_weight: 0.45
      constat_optimal_weight: 0.35
      dvd_optimal_weight: 0.20
      fpr_below_010_all_configs: true
      coverage_dif_only: [delta_gte_1.4]
      coverage_constat_adds: [non_rl_delta_0.6_to_1.4]
      coverage_dvd_adds: [variant_contamination]
    result_rationale: >
      Ensemble improvement is modest (+0.05 AUROC over best single) because the three
      signals are partially correlated — items with strong DIF effects also tend to show
      ConStat sensitivity (the underlying contamination drives both). The remaining
      improvement comes from coverage complementarity: ConStat catches medium-effect
      non-RL contamination that DIF misses (δ=0.6-1.4 range below DIF's operational
      threshold), and DVD catches individual-model memorization without cohort-level
      patterns. 2-of-3 voting is conservative (TPR=0.55, FPR=0.06) because requiring
      agreement across fundamentally different detection mechanisms filters out
      method-specific artifacts. Weighted fusion performs better (TPR=0.61) because
      DIF's weight (0.45) reflects its superior group-level power. Cross-validation
      weight stability is moderate — optimal weights shift ±0.10 across folds, suggesting
      the training signal is noisy with only 216 items with semi-synthetic ground truth.
      FPR<0.10 across all configurations is achievable because each individual signal
      has low FPR and voting/fusion only increases specificity. However, the ensemble's
      value proposition is undermined by the deployment cost: requiring paraphrase
      generation (ConStat) and 50-sample inference (DVD) per new benchmark evaluation
      makes the ensemble impractical for routine use.
    tables:
      - name: "Table: Ensemble vs Individual Detectors"
        columns: [method, TPR, FPR, AUROC, practical_cost]
        rows:
          - [DIF_alone, 0.51, 0.08, 0.71, low_existing_data]
          - [ConStat_alone, 0.38, 0.07, 0.68, high_paraphrase_generation]
          - [DVD_alone, 0.35, 0.09, 0.67, high_50x_inference]
          - [ensemble_2of3, 0.55, 0.06, 0.74, very_high_all_three]
          - [ensemble_weighted, 0.61, 0.09, 0.76, very_high_all_three]
    figures_description:
      - "Venn diagram: items detected by each method, showing overlap regions and unique detections per signal."
      - "Coverage map: detection power as function of contamination effect size and type, showing ensemble coverage advantage in 0.6-1.4 region."
    analysis: >
      In median tier, ensemble fusion is strictly future work. Even if executed, the
      +0.05 AUROC gain doesn't justify the deployment complexity increase. The more
      valuable contribution is the coverage analysis showing which contamination types
      each method catches — this informs future detector design without requiring a
      deployed ensemble. Paper framing acknowledges ensemble as "natural extension"
      in future work section, citing the coverage complementarity finding. Not allocating
      GPU budget here.

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      Pilot bifactor IRT equating on MMLU. Fit general + subject-specific factors,
      select anchor items, calibrate replacements. Killed by plan_014 pre-check
      (within-subject C%=38.1% shows DIF persists within subjects, undermining
      the bifactor premise).
    expected_results:
      bifactor_convergence: partial
      n_subjects_converged: 38
      n_subjects_failed: 19
      general_factor_loading_mean: 0.38
      subject_factor_loading_mean: 0.52
      general_factor_variance_explained: 0.22
      total_anchor_items_identified: 412
      anchor_items_per_subject_mean: 10.8
      anchor_sufficiency_for_equating: false
      equated_rho_achievable: false
      estimation_time_hours: 14
      convergence_issues: [heywood_cases, negative_variance_estimates]
    result_rationale: >
      Bifactor model partially converges because MMLU subjects have genuine
      multidimensional structure — items within a subject share subject-specific
      variance beyond the general "LLM ability" factor. However, 19/57 subjects fail
      to converge due to: (a) small subject sizes (some MMLU subjects have <100 items,
      insufficient for stable subject-factor estimation with N=5,219 models), (b)
      Heywood cases where subject-factor loadings exceed 1.0 (indicating model
      misspecification for heterogeneous LLM populations), (c) negative variance
      estimates in subjects with near-uniform item difficulty (ceiling/floor effects).
      The general factor explains only 22% of variance — much lower than human
      testing (typically 40-60%) — because LLM ability profiles are more jagged
      across domains than human ability profiles (a model can excel at math but fail
      at moral reasoning in ways humans rarely do). This low general-factor loading
      means anchor items selected on general-factor stability are poor anchors for
      subject-specific equating. With only ~10 anchors per subject (many subjects need
      ≥20 for stable equating), the fixed-parameter calibration in step (c) would
      produce unstable parameter estimates. Plan_014's finding (within-subject
      C%=38.1%) confirms the fundamental problem: DIF is not a cross-subject artifact
      that bifactor modeling can absorb — it exists within subjects, reflecting
      genuine temporal item functioning changes that no factor model eliminates.
    tables:
      - name: "Table: Bifactor Model Fit Summary"
        columns: [metric, value, interpretation]
        rows:
          - [subjects_converged, "38/57", partial]
          - [general_factor_loading_mean, 0.38, weak]
          - [subject_factor_loading_mean, 0.52, moderate]
          - [general_variance_explained, "22%", "low — LLM ability is domain-fragmented"]
          - [anchor_items_total, 412, insufficient_for_equating]
          - [heywood_cases, 7, model_misspecification]
    figures_description:
      - "Loading plot: general factor loading vs subject factor loading for all converged subjects, showing LLM-specific dominance of subject factors over general factor."
      - "Convergence diagnostic: iteration count and log-likelihood trajectory for converged vs failed subjects."
    analysis: >
      Bifactor equating is not viable for MMLU in its current form. The fundamental
      issue is that LLM ability structure is too jagged for a general+specific bifactor
      model — unlike human test-takers who have a strong g-factor, LLMs have domain-specific
      capabilities that dominate the general factor. Combined with plan_014's evidence
      that DIF persists within subjects (38.1%), there is no factor-analytic escape from
      temporal DIF. In median tier, this experiment confirms the "dropped from paper"
      status of regeneration/equating. Report as: "bifactor IRT equating is theoretically
      appealing but empirically infeasible for current LLM benchmarks due to weak general
      factor structure (22% variance explained) and insufficient anchor items." Future
      work direction: multidimensional IRT with domain-specific equating (per-subject
      rather than bifactor).

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      Generate replacement items for DIF-flagged MMLU questions using LLM generation
      with construct constraints. Calibrate via student simulation. Depends on plan_005
      (bifactor equating) which doesn't converge.
    expected_results:
      n_items_generated: 150
      n_subjects_covered: 12
      difficulty_correlation_prompt_based: 0.32
      difficulty_correlation_student_sim: 0.62
      difficulty_correlation_empirical_panel: 0.71
      construct_alignment_human_judged: 0.78
      n_holdout_models: 20
      holdout_ranking_rho_original_vs_replaced: 0.94
      item_quality_rating_human_mean: 3.4
      item_quality_rating_human_std: 0.9
      generation_cost_gpu_hours: 180
      calibration_iterations_needed: 3
    result_rationale: >
      Prompt-based difficulty targeting achieves only ρ=0.32 (consistent with arXiv
      2602.06631 range of 0.10-0.45) because LLMs lack reliable introspective access
      to item difficulty — they can judge "this is a hard question" but cannot predict
      the precise proportion of models that will answer correctly. Student simulation
      (arXiv 2601.09953) improves to ρ=0.62 because it actually simulates the answering
      process rather than judging difficulty abstractly, but falls short of the claimed
      r=0.75-0.82 range because MMLU items span 57 diverse subjects and the simulation
      model has uneven fidelity across domains (strong in STEM, weak in humanities/law).
      Empirical calibration on a 20-model holdout panel achieves ρ=0.71 — the best
      result but requiring actual inference, defeating the purpose of automated
      calibration. Construct alignment at 78% means ~22% of generated items subtly
      shift the cognitive demand (e.g., from factual recall to reasoning, or from
      domain A to domain B) — acceptable for rough replacement but not for
      psychometric equating. Holdout ranking ρ=0.94 falls short of the ≥0.95
      target because difficulty miscalibration compounds across 150 items: even small
      per-item difficulty errors accumulate into ranking perturbation. Without viable
      bifactor equating (plan_005), the calibration step cannot be anchored to a
      psychometric framework, making the replacements empirically calibrated but
      theoretically ungrounded.
    tables:
      - name: "Table: Difficulty Calibration Methods Comparison"
        columns: [method, rho_with_empirical, cost, scalability]
        rows:
          - [prompt_based, 0.32, zero, high]
          - [student_simulation, 0.62, "20 GPU-hrs", medium]
          - [empirical_panel_20_models, 0.71, "180 GPU-hrs", low]
    figures_description:
      - "Scatter: predicted vs empirical difficulty (p-value) for each calibration method, showing regression lines and confidence bands."
      - "Box plot: construct alignment scores by subject category, showing STEM vs humanities gap in generation quality."
    analysis: >
      In median tier, item generation produces moderate-quality replacements that fall
      short of psychometric standards. The ρ=0.94 ranking correlation (below 0.95 target)
      combined with bifactor equating failure means the regeneration pipeline is not
      paper-ready. Student simulation calibration is the most interesting methodological
      finding (ρ=0.62 without any model inference), but it's a contribution for a
      separate paper, not this one. Recommend deferring entirely — the paper's framing
      has already pivoted away from regeneration toward characterization and validation
      methodology. Mention as future work: "automated item generation with simulation-based
      calibration is a promising direction for benchmark maintenance."

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      Implement cumulative Bayesian DIF priors (Sinharay et al., 2006). Simulate
      4 successive benchmark administrations to show power accumulation over time.
      Zero GPU cost (pure simulation).
    expected_results:
      single_admin_power_delta10: 0.41
      cumulative_2admin_power_delta10: 0.58
      cumulative_3admin_power_delta10: 0.69
      cumulative_4admin_power_delta10: 0.76
      single_admin_power_delta14: 0.68
      cumulative_2admin_power_delta14: 0.82
      cumulative_3admin_power_delta14: 0.89
      cumulative_4admin_power_delta14: 0.93
      fpr_all_administrations: 0.04
      prior_sensitivity_halfnormal_vs_uniform: 0.03
      prior_sensitivity_informative_vs_weakly: 0.07
      bayes_factor_threshold_bf10: 3.0
      convergence_mcmc_rhat_max: 1.02
      simulation_n_per_admin: 100
      simulation_n_items: 500
      computation_time_minutes: 45
    result_rationale: >
      Bayesian DIF accumulation works because informative priors from administration t
      narrow the posterior for administration t+1 — items previously flagged as DIF
      receive higher prior probability of DIF, concentrating detection power. Single
      administration power of 0.41 at δ=1.0 is consistent with simulation results
      (mvp_dif_power_sim: TPR≈0.04 at N=50/δ=1.0, improving at larger N). The
      cumulative improvement follows a diminishing-returns curve: biggest jump from
      admin 1→2 (+0.17), smaller 2→3 (+0.11), smallest 3→4 (+0.07). This is because
      early administrations identify the "easy" DIF items (large effects), and later
      administrations mainly add marginal items near the detection boundary. FPR
      remains controlled at 0.04 across administrations because the Bayesian framework
      naturally penalizes false alarms through the prior update mechanism — an item
      consistently not flagged receives decreasing DIF prior probability. Prior
      sensitivity analysis shows weak sensitivity to the choice of half-normal vs
      uniform prior (Δpower=0.03) because with 100+ models per administration, the
      likelihood dominates the prior. Informative vs weakly-informative priors show
      slightly more sensitivity (Δpower=0.07) because informative priors carry forward
      more information from previous administrations, which helps at small effect sizes
      but risks propagating false positives if the initial administration was noisy.
    tables:
      - name: "Table: Cumulative Power by Administration and Effect Size"
        columns: [n_administrations, power_delta_10, power_delta_14, power_delta_16, fpr]
        rows:
          - [1, 0.41, 0.68, 0.72, 0.04]
          - [2, 0.58, 0.82, 0.87, 0.04]
          - [3, 0.69, 0.89, 0.93, 0.04]
          - [4, 0.76, 0.93, 0.96, 0.04]
      - name: "Table: Prior Sensitivity Analysis"
        columns: [prior_type, power_3admin_delta10, fpr, bayes_factor_calibration]
        rows:
          - [half_normal_01, 0.69, 0.04, well_calibrated]
          - [uniform_0_5, 0.66, 0.05, slight_fpr_inflation]
          - [informative_prev_posterior, 0.73, 0.04, best_power]
          - [weakly_informative, 0.66, 0.03, conservative]
    figures_description:
      - "Power accumulation curve: TPR as function of number of administrations for δ ∈ {0.8, 1.0, 1.2, 1.4, 1.6}, showing diminishing returns pattern."
      - "Prior-posterior update visualization: posterior DIF probability distribution for a representative item across 4 administrations, showing progressive narrowing."
    analysis: >
      This is a clean simulation result that works as expected from the statistical
      theory. The key value is practical: it provides a roadmap for benchmark
      maintainers — "even if single-time-point DIF detection has limited power for
      medium effects (δ≈1.0), accumulating evidence across 3 evaluation cycles brings
      power from 0.41 to 0.69." This directly addresses reviewer concern about DIF's
      limited power at moderate effect sizes. In median tier, this is a nice
      supplementary result that strengthens the "practical methodology" contribution.
      Include as a short section or appendix: "Bayesian evidence accumulation for
      longitudinal benchmark monitoring." Zero GPU cost makes it an easy win.

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      Formal analysis of benchmark validity under progressive item replacement.
      Depends on plan_005 (bifactor equating) and plan_006 (item generation).
      Both upstream dependencies produce insufficient results in median tier.
    expected_results:
      validity_5pct_replacement_rho: 0.993
      validity_10pct_replacement_rho: 0.984
      validity_20pct_replacement_rho: 0.961
      validity_50pct_replacement_rho: 0.892
      reliability_5pct_shr: 0.991
      reliability_10pct_shr: 0.988
      reliability_20pct_shr: 0.979
      reliability_50pct_shr: 0.941
      construct_coverage_loss_20pct: 0.03
      construct_coverage_loss_50pct: 0.11
      theoretical_bound_rho_vs_replacement_rate: "ρ ≥ 1 - 1.8r (r = replacement fraction)"
      empirical_vs_theoretical_gap: 0.02
      n_replacement_scenarios: 20
    result_rationale: >
      Ranking stability degrades gracefully because MMLU has massive redundancy
      (plan_017 showed ρ≈0.997 after removing 31% DIF items entirely, without
      replacement). Replacement with calibrated items preserves even more stability
      than removal because replacement maintains the total item count and construct
      coverage. At 5% replacement (626 items), the ranking perturbation is within
      noise — individual item contributions to total score are ~0.008% each, so
      replacing 626 items with ρ=0.71 difficulty-calibrated alternatives produces
      minimal ranking change. At 20% (2,502 items), the accumulated difficulty
      miscalibration starts to matter: if mean difficulty shifts by 0.05 (plausible
      with ρ=0.71 calibration), 2,502 items create a systematic ~125-item equivalent
      shift, producing ρ=0.961. At 50% replacement, the benchmark is substantially
      different — ρ=0.892 means ~11% of pairwise rankings change, which approaches
      the boundary of "different benchmark" rather than "refreshed benchmark."
      The theoretical bound (ρ ≥ 1 - 1.8r) is a linearization of the empirical
      curve, valid for r<0.3; beyond that, non-linear effects from construct
      coverage loss and difficulty distribution shift create faster degradation.
      However, this analysis is moot in median tier because the upstream item
      generation pipeline (plan_006) doesn't achieve psychometric-grade calibration,
      making the degradation curves optimistic (they assume ρ=0.71 calibration,
      but operational quality would be lower without bifactor anchoring).
    tables:
      - name: "Table: Validity Degradation Under Replacement"
        columns: [replacement_pct, n_items_replaced, ranking_rho, shr, construct_coverage_loss]
        rows:
          - [5, 626, 0.993, 0.991, 0.01]
          - [10, 1251, 0.984, 0.988, 0.02]
          - [20, 2502, 0.961, 0.979, 0.03]
          - [30, 3753, 0.938, 0.964, 0.06]
          - [50, 6254, 0.892, 0.941, 0.11]
    figures_description:
      - "Degradation curve: ρ vs replacement fraction, with theoretical bound overlay and 95% CI bands from bootstrap."
      - "Construct coverage map: heatmap of subject representation before/after 20% and 50% replacement, showing which subjects lose coverage."
    analysis: >
      In median tier, this is an informative simulation but lacks practical grounding
      because the item generation pipeline (plan_006) isn't paper-ready. The degradation
      curves are useful for framing the "benchmark maintenance" narrative: "MMLU can
      tolerate 20% item refresh with <4% ranking disruption, but 50% replacement
      approaches the boundary of a different benchmark." This finding actually supports
      the Claim 4 message (benchmark redundancy) from a different angle. However,
      without a viable replacement pipeline, this remains theoretical. Recommend:
      run the simulation using plan_017's random-replacement baseline (no calibration,
      just random new items) to establish the worst-case degradation curve, and frame
      as "even random replacement degrades gracefully up to 20%, implying MMLU
      rankings are dominated by construct-level signal, not individual item properties."
      This doesn't require plan_005/006 and can be derived from existing plan_017 data.

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Item-Focused Trees (Tutz & Berger, 2016) as alternative to categorical cohort
      DIF. Treats model release date as continuous covariate. Avoids arbitrary
      temporal cohort splits.
    expected_results:
      ift_n_items_tested: 12508
      ift_dif_items_detected: 2856
      ift_dif_pct: 22.8
      ift_mh_agreement_jaccard: 0.61
      ift_mh_overlap_pct: 74
      ift_unique_detections: 418
      mh_unique_detections: 1062
      ift_continuous_trend_monotonic_pct: 68
      ift_continuous_trend_nonlinear_pct: 32
      ift_primary_split_date: 2023-09-15
      ift_computation_time_hours: 8
      ift_tree_depth_median: 3
      ift_tree_depth_max: 5
      subjects_with_nonlinear_dif_trend: [moral_scenarios, computer_security, machine_learning, virology]
    result_rationale: >
      IFT detects 22.8% DIF items — between the full-population MH estimate (31.3%)
      and the decoder-only estimate (~19%). This intermediate rate occurs because IFT
      uses release date as a continuous covariate, which partially absorbs the
      architecture confound (architecture correlates with release date: encoder-decoder
      models are predominantly pre-2023) without explicitly stratifying by architecture.
      The 74% overlap with MH confirms both methods detect the same core DIF signal,
      but IFT misses 1,062 MH items because its tree-splitting approach requires
      sufficient evidence at each split point (analogous to a multiple-comparisons
      correction inherent in the recursive partitioning). IFT uniquely detects 418
      items where the continuous trend reveals DIF that the binary temporal split
      masks — items with gradual DIF onset that hasn't reached the ETS C threshold
      at the arbitrary 2023/2024 boundary but accumulates significance over the full
      date range. The primary split at 2023-09-15 aligns with the major model
      generation boundary (Llama-2 → Llama-3 era). Non-linear DIF trends in 32% of
      flagged items are concentrated in subjects undergoing rapid capability change
      (moral_scenarios, machine_learning) where model performance improves
      discontinuously rather than gradually. Tree depth of 3-5 indicates DIF is
      not a simple before/after effect but has internal structure (e.g., items
      that are stable 2022-2023, then DIF in early 2024, then stable again as
      the capability plateau).
    tables:
      - name: "Table: IFT vs MH Detection Comparison"
        columns: [method, n_dif_items, dif_pct, overlap_with_other, unique_detections]
        rows:
          - [MH_temporal, 3918, 31.3, "74% of IFT", 1062]
          - [IFT_continuous, 2856, 22.8, "96% overlap with MH subset", 418]
      - name: "Table: IFT DIF Trend Types"
        columns: [trend_type, pct_of_dif_items, example_subjects, interpretation]
        rows:
          - [monotonic_increasing, 52, "most STEM subjects", "steady capability gain → steady DIF"]
          - [monotonic_decreasing, 16, "formal_logic, abstract_algebra", "capability plateau → DIF attenuation"]
          - [step_function, 19, "professional_medicine, law", "abrupt generation boundary effect"]
          - [non_monotonic, 13, "moral_scenarios, virology", "capability oscillation across generations"]
    figures_description:
      - "Representative IFT trees for 4 items: one monotonic, one step-function, one non-monotonic, one with deep splits. Each tree shows split dates and DIF effect size at leaves."
      - "Heatmap: DIF effect size as continuous function of release date × MMLU subject, showing temporal-domain interaction structure. Rows sorted by primary IFT split date."
    analysis: >
      IFT provides a methodologically cleaner alternative to arbitrary temporal cohort
      splits. The 22.8% detection rate sits between full-population MH (31.3%) and
      decoder-only MH (~19%), suggesting IFT partially accounts for architecture
      confounding through its continuous date variable. The most valuable finding is
      the 32% non-linear DIF trends — these reveal that item functioning changes are
      not uniform across time, with some items showing step-function changes at
      generation boundaries and others showing gradual drift. This granularity is
      impossible with binary MH. In median tier, IFT serves as a robustness check
      confirming the core DIF finding while providing richer temporal characterization.
      Include as a supplementary analysis: "IFT confirms 23% DIF rate using continuous
      temporal modeling, with 74% overlap with MH flags, and reveals non-linear
      temporal DIF trends in 32% of flagged items." Strengthens the paper's
      methodological rigor without changing the headline. Zero GPU cost.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "3e44c9df-06e4-4743-b471-de592a7ce9c4",
  "isSidechain": false,
  "requestId": "req_011CbF1i4ne9xhQb7awoRBjs",
  "type": "assistant",
  "uuid": "e872593c-fa60-4b80-adbd-a8103deb28f4",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01L6XxA9VFrbL45T6oWYcWsK",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 1,
      "cache_creation_input_tokens": 309,
      "cache_read_input_tokens": 29012,
      "output_tokens": 16639,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 309,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 1,
          "output_tokens": 16639,
          "cache_read_input_tokens": 29012,
          "cache_creation_input_tokens": 309,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 309
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

_source line 13_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Architecture stratification reduces but does not eliminate DIF; instability mostly explained by capability improvement; semi-synthetic framework becomes…",
  "leafUuid": "e872593c-fa60-4b80-adbd-a8103deb28f4",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457"
}
```

---

### Runtime record

_source line 14_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis characterization with semi-synthetic validation",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457"
}
```

---

### Runtime record

_source line 15_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 median 档的含义：  含义：Architecture stratification reduces but does not eliminate DIF; instability mostly explained by capability improvement; semi-synthetic framework becomes…",
  "leafUuid": "e872593c-fa60-4b80-adbd-a8103deb28f4",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457"
}
```

---

### Runtime record

_source line 16_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF analysis characterization with semi-synthetic validation",
  "sessionId": "3dc50d3f-5ce4-43a1-86c4-2728856df457"
}
```

---
