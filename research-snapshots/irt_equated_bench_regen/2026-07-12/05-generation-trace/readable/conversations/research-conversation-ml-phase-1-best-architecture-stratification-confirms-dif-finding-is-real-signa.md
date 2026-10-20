# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义： 含义：Architecture stratification confirms DIF finding is real signal, not populat

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-3/2cfaa65f-72b1-47fa-82d8-3ab65e16d19f.jsonl`
- **Structured JSON:** [`2c0d73b17266737256eb.json`](../../sessions/2c/2c0d73b17266737256eb.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T03:30:06.762Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T03:30:06.762Z",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：\n\n含义：Architecture stratification confirms DIF finding is real signal, not population heterogeneity artifact; instability partially independent of capability improvement\n核心假设：['Decoder-only subpopulation IRT fit substantially improves (RMSEA<0.03), validating unidimensional model for homogeneous architectures', 'Decoder-only temporal DIF C% remains ≥25%, confirming instability is not driven by architecture mixing', \"Instability decomposition: partial ρ (controlling domain accuracy improvement) remains significant — DIF captures item function change beyond 'models just got better'\", 'Non-uniform DIF check (SIBTEST/logistic regression) shows ≥70% overlap with MH flags — MH is not missing major non-uniform effects', \"GSM1K anti-correlation (r=−0.478) survives all robustness checks (already confirmed: leave-one-out, Cook's D, partial r)\"]\n关键指标范围：{'decoder_only_c_pct': [25, 35], 'decoder_only_irt_rmsea': [0.015, 0.03], 'decoder_only_irt_cfi': [0.95, 0.99], 'partial_rho_controlling_domain_accuracy': [0.15, 0.3], 'partial_rho_p_value': [0.001, 0.05], 'non_uniform_mh_overlap_pct': [70, 90], 'claims_at_full_strength': [4, 4]}\n叙事方向：All four claims hold as written. Lead with '38% instability persists in architecture-homogeneous populations with good IRT fit (RMSEA<0.03)' — eliminates the strongest reviewer objection preemptively. Instability decomposition strengthens Claim 1 by showing DIF captures genuine item function change beyond domain-level capability gains. Paper runs the original framing: 'psychometric analysis reveals structural benchmark problems that existing contamination validation methodology cannot detect.' Circularity ablation (plan_020) and cross-benchmark GSM1K validation are load-bearing complementary evidence. Strongest possible ICLR submission.\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: ICLR 2027 (expected deadline ~October 2026)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: 31–38% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: 31.3% (temporal cohort, plan_001); within-subject range 31-45%, avg 38.1% (plan_014). This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates with domain-specific accuracy improvement (ρ=0.307, p=0.02). Architecture-stratified estimate (decoder-only subset) TBD — plan_010 executing. Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). The >15% finding holds at standard thresholds [1.0, 2.0]; at the conservative 2.5 threshold, 10.2% (1,278 items) still exhibit large DIF. BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 ETS C items at 1.5 threshold).\n- Evidence: plan_001 (C%=31.3%, enrichment=0.96, sanity=0.18%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified TBD), plan_018 (threshold sensitivity: 48.9%/31.3%/18.3%/10.2% at 1.0/1.5/2.0/2.5; BH correction negligible)\n- Honesty requirement: ρ=0.307 means \"item instability\" may mainly reflect \"models got better at those domains\" — instability decomposition (partial out domain accuracy improvement) TBD\n- IRT fit: Full-population fit indices TBD from plan_010; if decoder-only fit substantially improves, lead with that subset as primary\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\"\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587.\n4. **Cross-benchmark validation — DIF items resist contamination-based gains**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling METABENCH accuracy, p=0.023; permutation p=0.014). Models with larger contamination gaps show disproportionately lower performance on DIF-C items. This is consistent with contamination producing surface-level gains concentrated on non-DIF items, while DIF items capture genuine capability differences.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_004 Step 3 (r=−0.478, p=0.005, N=33)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227), Step 3 adds contamination dimension but is suggestive (N=33, CI wide). If Step 3 attacked, plan_017 stands independently.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33 CI upper bound |r|=0.16 (small effect possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine\n\n**Problem**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Item-level behavioral drift across model generations could silently erode this assumption.\n\n**Approach**: We apply Differential Item Functioning (DIF) analysis — a classical psychometric tool for detecting item-level behavioral anomalies — to the METABENCH response matrix (5,227 models × 12,508 MMLU items), the largest-scale DIF analysis on LLM benchmarks to date.\n\n**What we find**: Three discoveries, each a contribution:\n\n1. **38% of MMLU items are functionally unstable** across model generations (ETS C DIF, temporal cohorts). This persists within every subject domain (31-45% per subject), is not statistical noise (random split: 0.18%), and cannot be eliminated by three structural corrections (matched-ability, IRT θ-conditioning, bifactor pre-check). The instability correlates with capability improvement (ρ=0.307) — models got better at those domains, changing how items function.\n\n2. **The field's standard validation approach has a blind spot**: Web-overlap contamination labels (Li et al.) measure whether an item is publicly accessible — a global, model-agnostic property. DIF detects whether an item functions differently across model cohorts — a dynamic, group-specific signal. Enrichment≈1.0 between DIF flags and web-overlap labels is expected when most items have equal global exposure (MMLU on Common Crawl since 2020). Semi-synthetic injection proves DIF works (ΔTPR=+0.508) — the problem is the ground truth, not the detector. Any contamination detection paper validating against web-overlap labels at the item level has the same issue.\n\n3. **A semi-synthetic validation framework** that injects controlled differential contamination into real response matrices, measuring ΔTPR as the detection power metric. Cross-subject matching eliminates the matching variable contamination problem (ΔFPR=0.000). This infrastructure is reusable for validating any item-level contamination detector.\n\n4. **DIF is a diagnostic lens, not a quality filter**. MMLU rankings are massively redundant (ρ≈0.997 after 31% removal), but DIF items concentrate the discriminative signal that differentiates model generations (removal disrupts rankings MORE than random, z=-8 to -49σ). Cross-benchmark validation on GSM8K shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]). DIF identifies which capability dimensions are changing — complementing Growing Pains' anchor-item approach by detecting which anchors are degrading.\n\n**Headline result**: \"Psychometric analysis of METABENCH reveals that 38% of MMLU items are functionally unstable across model generations. Web-overlap contamination labels do not capture this differential signal (enrichment≈1.0), while semi-synthetic injection confirms detection capability (ΔTPR=+0.508 on MMLU, +0.818 on GSM8K). Cross-benchmark validation using GSM1K contamination gaps shows DIF items resist contamination-based performance gains (r=−0.478, 95% CI [−0.71, −0.16]; partial r=−0.394 controlling accuracy). We provide a reusable validation framework with cross-subject matching (ΔFPR=0.000).\"\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **ICLR 2027**: Good fit — empirical analysis of evaluation methodology, psychometric rigor, large-scale characterization. Risk: ML reviewers may not be familiar with DIF/IRT. Mitigation: §3 provides self-contained DIF primer with ML translations.\n- **Novelty concern**: DIF itself is not new (1988). Our contributions are: (1) the empirical finding of 28–38% instability at unprecedented scale (5,227×12,508), (2) the ground truth meta-critique affecting the field's validation methodology, (3) the semi-synthetic validation framework with cross-subject matching innovation (ΔFPR=0.000), (4) DIF as diagnostic lens revealing benchmark measurement structure. Explicitly acknowledge MH-DIF is applied without modification; novelty is empirical characterization + framework design, not algorithmic. Frame as \"bringing mature psychometric tools to characterize an urgent ML evaluation problem — the scale creates novel statistical challenges (architecture heterogeneity, multidimensional construct, 5000+ examinees).\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"38% could just mean models got better\"** — Yes, partially. ρ=0.307 confirms correlation. We discuss this honestly. The contribution is the finding itself: benchmarks have massive item-level behavioral drift, regardless of cause.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). GSM1K contamination gap validation (N=33) provides cross-benchmark evidence. Full generalization to diverse benchmarks remains future work.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — Apply SIBTEST or logistic regression DIF to 5-10 representative subjects as robustness check. Show MH results are not missing substantial non-uniform DIF.\n\n10. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: best\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T03:30:06.767Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T03:30:06.767Z",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T03:30:06.793Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：

含义：Architecture stratification confirms DIF finding is real signal, not population heterogeneity artifact; instability partially independent of capability improvement
核心假设：['Decoder-only subpopulation IRT fit substantially improves (RMSEA<0.03), validating unidimensional model for homogeneous architectures', 'Decoder-only temporal DIF C% remains ≥25%, confirming instability is not driven by architecture mixing', "Instability decomposition: partial ρ (controlling domain accuracy improvement) remains significant — DIF captures item function change beyond 'models just got better'", 'Non-uniform DIF check (SIBTEST/logistic regression) shows ≥70% overlap with MH flags — MH is not missing major non-uniform effects', "GSM1K anti-correlation (r=−0.478) survives all robustness checks (already confirmed: leave-one-out, Cook's D, partial r)"]
关键指标范围：{'decoder_only_c_pct': [25, 35], 'decoder_only_irt_rmsea': [0.015, 0.03], 'decoder_only_irt_cfi': [0.95, 0.99], 'partial_rho_controlling_domain_accuracy': [0.15, 0.3], 'partial_rho_p_value': [0.001, 0.05], 'non_uniform_mh_overlap_pct': [70, 90], 'claims_at_full_strength': [4, 4]}
叙事方向：All four claims hold as written. Lead with '38% instability persists in architecture-homogeneous populations with good IRT fit (RMSEA<0.03)' — eliminates the strongest reviewer objection preemptively. Instability decomposition strengthens Claim 1 by showing DIF captures genuine item function change beyond domain-level capability gains. Paper runs the original framing: 'psychometric analysis reveals structural benchmark problems that existing contamination validation methodology cannot detect.' Circularity ablation (plan_020) and cross-benchmark GSM1K validation are load-bearing complementary evidence. Strongest possible ICLR submission.

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
  "promptId": "11fbb077-1287-484c-8d9d-e483bd72734e",
  "type": "user",
  "uuid": "1f7dda54-d605-4819-9756-aef7db213f34",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T03:30:06.791Z_

```json
{
  "parentUuid": "1f7dda54-d605-4819-9756-aef7db213f34",
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
  "uuid": "97716608-3dff-4b3a-a054-7b494fd2fd1e",
  "timestamp": "2026-05-21T03:30:06.791Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T03:30:06.791Z_

```json
{
  "parentUuid": "97716608-3dff-4b3a-a054-7b494fd2fd1e",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "91defcc7-eaf6-467b-8985-be4eec3af307",
  "timestamp": "2026-05-21T03:30:06.791Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Architecture stratification confirms DIF finding is real signal, not population heterogeneity artifact; instability partially independent of capability imp…",
  "leafUuid": "91defcc7-eaf6-467b-8985-be4eec3af307",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF validation framework for benchmark structural analysis",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f"
}
```

---

### Assistant

_source line 8 · 2026-05-21T03:31:32.645Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted results for each "planned" experiment in the experiment_plan, under the "best" tier assumptions defined in Phase 1. Let me identify which experiments are still "planned" (not yet completed):

Looking at the experiment_plan and registry:

Completed experiments (in registry):
- plan_001 (DONE)
- plan_001b (DONE)
- plan_011 (DONE)


- plan_012 (DONE)
- plan_013 (DONE)
- plan_014 (DONE)
- plan_016 (DONE)
- plan_017 (DONE)
- plan_004 (DONE)
- plan_015 (killed)

Planned experiments still to generate results for:
- plan_002 - rl_robustness_validation
- plan_003a - constat_perturbation_eval
- plan_003b - dvd_generation_variance_eval
- plan_003c - ensemble_fusion
- plan_005 - bifactor_irt_equating_pilot
- plan_006 - item_generation_calibration
- plan_007 - cumulative_bayesian_dif
- plan_008 - graceful_degradation_analysis
- plan_009 - item_focused_trees
- plan_010 - architecture_stratified_dif
- plan_011 (DONE)

I need to cross-reference what's marked as planned in the experiment plan against what's already completed in the registry, then generate detailed predictions for the ones that haven't been executed yet. I'm noticing some discrepancies between what's documented in paper_framing.md and what's actually in the experiment registry—plan_018 and plan_020 are referenced in the framing but don't appear in the official plan list, suggesting they were added later. I should also flag that "Ensemble" was dropped from the original framing, which might explain why plan_003c on ensemble fusion is still in the planned-but-not-executed category. I'm checking which experiments were actually completed versus planned—plan_018 and plan_020 show up in the paper framing with cited results, so they're additional studies that got added during the research. For the five planned experiments under the best tier, I need to predict whether they'll meet those performance thresholds across the decoder metrics, partial correlations, DIF overlap, and claims validation.

Now working through the remaining experiments: plan_006 through plan_010, with special attention to plan_010 since it's the linchpin for the best tier—it needs to show that architecture stratification isolates the DIF signal from population heterogeneity effects. For the decoder-only models, I'm expecting the conformity percentage around 30%, RMSEA near 0.024, and CFI around 0.97 based on the tier definition.

Looking at the partial correlation metrics when controlling for domain accuracy, I'd predict the correlation coefficient around 0.22 with a p-value near 0.012, and the non-uniform Mantel-Haenszel overlap staying in the 78% range. This pattern would confirm that item instability persists even after removing architectural variation, and that the temporal DIF isn't simply riding on capability improvements—it's a partially independent phenomenon. For plan_002 on RL robustness, the best tier assumptions hold across all validation checks.

Now I'm seeing that the paper framing treats plan_002 as a limitations disclosure rather than a core claim due to the small sample size of 13 models. The experiment is still planned, so I should expect DIF flags to remain stable when RL models are added, though traditional detectors will likely degrade on reasoning-RL variants. Plans 003a/b/c are marked as future work and dropped from the current framing, so they're not needed for this paper. Plan_005 on bifactor IRT equating might still be relevant since it's about equating rather than the regeneration claim that was cut. Looking at which experiments are still planned versus already completed in the registry, I need to generate predictions for plan_002 through plan_003c since those haven't been executed yet. Let me draft the YAML structure with detailed data for each of these remaining planned experiments. - plan_004 → DONE in registry
- plan_005 → NOT in registry → PREDICT
- plan_006 → NOT in registry → PREDICT
- plan_007 → NOT in registry → PREDICT
- plan_008 → NOT in registry → PREDICT
- plan_009 → NOT in registry → PREDICT
- plan_010 → NOT in registry → PREDICT
- plan_011 → DONE in registry

So 10 experiments to predict.

I also notice plan_018 (threshold sensitivity) and plan_020 (circularity ablation) are referenced in the paper_framing with results but not in the experiment_plan list—those are already done so I'll skip predicting them.

For plan_010, this is the critical architecture stratification experiment that defines the best tier. The full population has about 5,219 models with 31.3% temporal C%, but when I focus on decoder-only models (roughly 3,500), I'd expect the temporal C% to drop to around 28-30%, and the IRT fit metrics should improve dramatically—RMSEA dropping from 0.06-0.08 down to 0.022-0.028, and CFI jumping from 0.85-0.90 to 0.96-0.97—which would confirm that unidimensional IRT works well for homogeneous architectures and that the DIF finding is genuine signal rather than an artifact of mixing different model types. Now I'm working through the instability decomposition with partial correlations... (flag retention ~88-92%)
- Traditional detectors on reasoning-RL models: AUROC drops from ~0.75 to ~0.52
- DeLong test p < 0.05 for DIF vs ConStat degradation
- Power analysis: detection boundary at p ≈ 0.45 for δ=1.4

But remember: N=13 reasoning-RL models is low. Bootstrap CIs will be wide.

### plan_003a - constat_perturbation_eval

Under best tier (but noted as "future work" in framing):
- 200 MMLU items reformulated
- ConStat detection on non-RL models: moderate power, AUROC ~0.70-0.75
- ConStat on RL models: degraded, AUROC ~0.55-0.60
- FDR-controlled detection: ~

Looking at the reasoning-RL models, I'm seeing that traditional detectors lose discriminative power significantly—AUROC drops to 0.52—while DIF flags remain stable at 88-92% retention, which is statistically significant. The sample size of 13 models is small though, so I need to be cautious about the confidence intervals. For the perturbation evaluation, I'm reformulating 200 MMLU items to test whether ConStat can catch these changes, but the performance degrades on RL models compared to standard models, dropping to around 0.55-0.60 AUROC.

### plan_003b - dvd_generation_variance_eval

Under best tier:
- Generation variance on 10-15 open-weight models
- DVD detection: moderate for verbatim contamination (AUROC ~0.65-0.70)
- Bimodal distribution detection: works for some items (~10-15% show bimodality)
- Weaker for variant contamination
- Correlation with DIF flags: low-moderate (Jaccard ~0.10-0.20)

### plan_003c - ensemble_fusion

Under best tier:
- Ensemble coverage: DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant
- 2

For the generation variance evaluation, I'm testing DVD detection across 10-15 open-weight models, and it shows moderate performance for catching verbatim contamination but struggles with variants. The bimodal distribution signal appears in only a subset of items. When I look at how these methods overlap with DIF flags, the correlation is fairly weak—Jaccard indices around 0.10-0.20—suggesting they're capturing different aspects of contamination. The ensemble approach divides the detection space: DIF handles large effect sizes, ConStat works better on non-RL models at smaller deltas, and DVD targets variant contamination specifically.

For the fusion strategy, I'm testing majority voting and weighted approaches. The weighted fusion performs better with a true positive rate around 0.62 while keeping false positives under 0.07, and the ensemble stays stable across cross-validation folds. Moving into the bifactor IRT work, I'm fitting a model with a general factor plus 57 subject-specific factors to MMLU data, where the general factor accounts for about 60% of variance and subject factors split the remaining 15-25%. The anchor item selection yields roughly 70% of stable items as candidates, and when I equate scores using fixed-parameter calibration for replacements, the correlation between original and equated scores reaches 0.97-0.98, well above the 0.95 threshold.

For item generation, I'm using LLM-generated replacements for items flagged with differential item functioning. Student simulation gives me a correlation of about 0.78 for difficulty estimation, and while prompt-based targeting alone only reaches 0.30, combining it with empirical calibration through student simulation pushes that to 0.72. The holdout validation confirms replacement items match the target difficulty within 0.15 logits. In the cumulative Bayesian DIF analysis, I'm simulating four successive test administrations to see how detection power accumulates—starting at 0.40 after one administration, climbing to 0.58 after two, 0.70 after three, and 0.76 after four. Bayesian shrinkage also helps reduce false positives from 0.05 down to 0.02.

For graceful degradation, I'm testing how the system holds up as I replace more items—at 5% replacement the correlation stays at 0.999, at 10% it's 0.998, and even at 50% replacement it degrades to 0.985, which is acceptable. The item-focused trees approach uses release date as a continuous covariate to detect drift, finding that about 35% of items show significant date effects, with 80% overlap to categorical DIF detection, plus another 5-8% of items with gradual drift that categorical methods miss.

Now I'm organizing all these results into YAML format...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "91defcc7-eaf6-467b-8985-be4eec3af307",
  "isSidechain": false,
  "requestId": "req_011CbF1KeqcxpGQvWWF4jkmv",
  "type": "assistant",
  "uuid": "4a7cd534-b463-4314-bd81-9c9205d88744",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJUpDBWhh2jhvZSkgEaJ43",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17084,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15054,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17084
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

_source line 9 · 2026-05-21T03:35:03.406Z_

```yaml
tier: best
narrative_guidance: >
  All four claims hold as written. Lead with '28-30% instability persists in architecture-homogeneous
  decoder-only populations with good IRT fit (RMSEA=0.024)' — eliminates the strongest reviewer
  objection preemptively. Instability decomposition strengthens Claim 1 by showing partial ρ=0.22
  (p=0.012) after controlling domain accuracy improvement — DIF captures genuine item function
  change beyond domain-level capability gains. Non-uniform DIF check confirms MH adequacy (78%
  overlap with SIBTEST). Paper runs the original framing: 'psychometric analysis reveals structural
  benchmark problems that existing contamination validation methodology cannot detect.' Architecture
  stratification (plan_010) and cross-benchmark GSM1K validation (plan_004, already done) are
  load-bearing complementary evidence. Strongest possible ICLR submission.

imagined_experiments:
  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      Run DIF within decoder-only subpopulation to test whether IRT model fit improves
      and temporal DIF persists when architecture heterogeneity is removed. Includes
      instability decomposition (partial ρ controlling domain accuracy) and non-uniform
      DIF robustness check (SIBTEST/logistic regression).
    expected_results:
      decoder_only_n_models: 3487
      decoder_only_n_ref_2023: 892
      decoder_only_n_foc_2024h1: 513
      decoder_only_temporal_c_pct: 29.1
      decoder_only_sanity_random_c_pct: 0.14
      full_population_irt_rmsea: 0.067
      full_population_irt_cfi: 0.874
      decoder_only_irt_rmsea: 0.024
      decoder_only_irt_cfi: 0.966
      decoder_only_irt_tli: 0.958
      decoder_only_irt_srmr: 0.031
      rmsea_improvement_pct: 64.2
      cfi_improvement: 0.092
      full_vs_decoder_only_flag_jaccard: 0.71
      partial_rho_controlling_domain_accuracy: 0.22
      partial_rho_p_value: 0.012
      zero_order_rho_domain_accuracy: 0.307
      variance_explained_by_accuracy_alone: 9.4
      residual_instability_pct: 20.5
      non_uniform_sibtest_n_subjects_tested: 8
      non_uniform_sibtest_c_flags: 2814
      non_uniform_mh_c_flags: 3627
      non_uniform_mh_overlap_pct: 78
      non_uniform_only_sibtest_pct: 4.2
      non_uniform_only_mh_pct: 26.2
      logistic_regression_r2_interaction_median: 0.008
    result_rationale: >
      Decoder-only models share transformer architecture, tokenizer family, and training
      paradigm — removing encoder-decoder (T5, BART, UL2) and hybrid (Mamba, RWKV, Griffin)
      models eliminates the multidimensional ability structure that confounds unidimensional
      IRT. RMSEA drops from 0.067 to 0.024 because the latent trait is now genuinely closer
      to unidimensional within the decoder-only population — these models vary primarily along
      a single capability axis (scale × data × training quality). CFI jumps above 0.95,
      validating the measurement model. Despite this improved fit, temporal C% drops only
      modestly from 31.3% to 29.1% — architecture mixing contributed ~2pp of spurious DIF,
      but the remaining 29% is real signal. The partial ρ=0.22 (controlling domain accuracy
      improvement) stays significant because item function change is partially but not fully
      explained by "models got better": some items genuinely changed HOW they function (e.g.,
      distractor attractiveness shifted, required reasoning chain changed in difficulty) beyond
      the aggregate accuracy gain. The 78% SIBTEST-MH overlap confirms MH captures the
      dominant uniform DIF pattern — the 22% SIBTEST-only flags represent non-uniform effects
      (items where DIF magnitude varies by ability level), which are real but secondary. The
      low logistic regression R² for the interaction term (0.008 median) confirms non-uniform
      DIF is present but small in magnitude relative to uniform DIF.
    tables:
      - title: "Table: IRT Fit Comparison — Full Population vs Decoder-Only"
        columns: [population, n_models, RMSEA, CFI, TLI, SRMR, temporal_C_pct]
        rows:
          - [full, 5219, 0.067, 0.874, 0.851, 0.058, 31.3]
          - [decoder_only, 3487, 0.024, 0.966, 0.958, 0.031, 29.1]
          - [encoder_decoder, 412, 0.041, 0.921, 0.903, 0.044, 34.8]
      - title: "Table: Instability Decomposition"
        columns: [predictor, rho, p_value, variance_explained_pct]
        rows:
          - [domain_accuracy_improvement, 0.307, 0.020, 9.4]
          - [partial_rho_residual, 0.220, 0.012, 4.8]
          - [total_temporal_c_variance, null, null, 100.0]
      - title: "Table: Non-Uniform DIF Overlap (8 subjects)"
        columns: [method, n_c_flags, overlap_with_mh_pct, unique_flags_pct]
        rows:
          - [MH_standard, 3627, 100.0, 26.2]
          - [SIBTEST, 2814, 78.0, 4.2]
          - [logistic_regression, 2951, 81.3, 3.8]
    figures_description:
      - "Scatter plot: full-population RMSEA by subject vs decoder-only RMSEA by subject, showing systematic improvement across all 57 subjects with regression line"
      - "Venn diagram: MH C-flags vs SIBTEST C-flags for 8 tested subjects, showing 78% overlap region"
      - "Partial regression plot: temporal C% residuals vs domain accuracy improvement residuals, slope = partial ρ = 0.22"
    analysis: >
      This is the single most important experiment for the paper. The RMSEA improvement from
      0.067 to 0.024 validates the measurement model for the decoder-only population —
      reviewers cannot dismiss the DIF findings as IRT misfit artifacts. The persistence of
      29% temporal DIF eliminates the strongest objection ("it's just architecture mixing").
      The instability decomposition is the key new contribution: ρ=0.307 honest disclosure
      becomes a strength when we show partial ρ=0.22 remains significant — "yes, capability
      improvement explains ~9% of variance in item instability, but ~5% is genuine item
      function change independent of aggregate accuracy gains." The non-uniform DIF check
      is a clean robustness confirmation — 78% overlap means MH captures the dominant signal,
      and the paper can state "MH is adequate for this population; non-uniform effects are
      present but secondary."

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      Empirically validate DIF stability across SFT-only, alignment-RL, and reasoning-RL
      cohort compositions. Compare DIF group-level robustness against traditional detector
      model-level degradation. Power analysis for detection boundary.
    expected_results:
      sft_only_n_models: 1843
      sft_only_temporal_c_pct: 30.8
      alignment_rl_n_models: 477
      alignment_rl_temporal_c_pct: 32.1
      reasoning_rl_n_models: 13
      reasoning_rl_models_added_to_focal: true
      cohort_with_rl_temporal_c_pct: 31.0
      flag_retention_sft_vs_alignment: 0.91
      flag_retention_sft_vs_with_rl: 0.89
      flag_retention_bootstrap_ci_95: [0.84, 0.94]
      constat_auroc_non_rl: 0.73
      constat_auroc_reasoning_rl: 0.54
      constat_auroc_drop: 0.19
      mink_auroc_non_rl: 0.68
      mink_auroc_reasoning_rl: 0.51
      dif_flag_stability_auroc: 0.88
      delong_dif_vs_constat_p: 0.003
      delong_dif_vs_mink_p: 0.008
      tost_equivalence_dif_retention_p: 0.021
      power_boundary_p_at_delta14: 0.45
      power_boundary_p_at_delta10: 0.62
      detection_tpr_at_p04: 0.38
      detection_tpr_at_p06: 0.61
      detection_tpr_at_p08: 0.79
      detection_tpr_at_p10: 0.92
    result_rationale: >
      DIF is a group-level statistic computed over entire cohorts — adding 13 reasoning-RL
      models to a focal group of ~500 changes cohort composition by <3%, producing negligible
      perturbation to the MH statistic. Flag retention at 89-91% reflects minor sampling
      variability, not RL-induced degradation. Traditional detectors (ConStat, Min-K%) operate
      at the individual model level — reasoning-RL training with PPO/GRPO contracts the NLL
      gap between memorized and non-memorized items (Wang et al.), directly degrading these
      detectors' signal. AUROC drops from 0.73/0.68 to 0.54/0.51 because the per-model
      distributional signature that these methods rely on is explicitly optimized away by RL.
      DIF's immunity stems from its design: it conditions on total score and compares GROUP
      response patterns, making it agnostic to individual model training procedures. The power
      analysis shows detection boundary at p≈0.45 for δ=1.4 — below this exploitation rate,
      the contamination-induced DIF effect size drops below the MH detection threshold. This
      is an honest limitation: DIF catches strong differential contamination, not subtle
      partial exploitation.
    tables:
      - title: "Table: DIF Flag Stability Across Cohort Compositions"
        columns: [cohort, n_models, temporal_c_pct, flag_retention_vs_sft, bootstrap_95ci]
        rows:
          - [sft_only, 1843, 30.8, 1.000, "—"]
          - [alignment_rl, 477, 32.1, 0.91, "[0.87, 0.95]"]
          - [sft_plus_reasoning_rl, 1856, 31.0, 0.89, "[0.84, 0.94]"]
          - [all_combined, 2333, 31.4, 0.90, "[0.85, 0.94]"]
      - title: "Table: Traditional Detector Degradation on Reasoning-RL Models"
        columns: [detector, auroc_non_rl, auroc_reasoning_rl, delta_auroc, delong_p]
        rows:
          - [ConStat, 0.73, 0.54, -0.19, 0.003]
          - [Min-K%, 0.68, 0.51, -0.17, 0.008]
          - [DIF_group_flag, 0.88, 0.86, -0.02, 0.71]
    figures_description:
      - "Detection power curve: TPR vs exploitation rate p ∈ [0.3, 1.0] at δ=1.0, 1.4, 1.6 showing detection boundary"
      - "Paired AUROC comparison: DIF vs ConStat vs Min-K% on non-RL and reasoning-RL models with bootstrap CIs"
    analysis: >
      Results confirm DIF's architectural advantage: group-level statistics are inherently
      robust to individual model training variations. The N=13 reasoning-RL limitation is
      honestly acknowledged — bootstrap CIs on flag retention are wide [0.84, 0.94]. However,
      the DeLong tests are significant (p<0.01) for DIF vs traditional detectors, and TOST
      equivalence confirms DIF retention is statistically equivalent across compositions
      (p=0.021). This goes into the paper as supporting evidence for Claim 1's robustness,
      with explicit caveats about N=13 in limitations. The power analysis provides a useful
      operational characterization: DIF works for strong differential contamination (p≥0.45),
      complementary methods needed for subtle effects.

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      Independent ConStat-style perturbation testing on 200+ MMLU items to characterize
      detection power by effect size and RL training type.
    expected_results:
      n_items_reformulated: 237
      n_models_non_rl: 42
      n_models_reasoning_rl: 11
      constat_fdr_q005_flagged_pct: 17.3
      constat_auroc_non_rl_verbatim: 0.74
      constat_auroc_non_rl_variant: 0.61
      constat_auroc_reasoning_rl_verbatim: 0.55
      constat_auroc_reasoning_rl_variant: 0.48
      constat_tpr_at_fpr010_non_rl: 0.42
      constat_tpr_at_fpr010_rl: 0.18
      reformulation_semantic_similarity_mean: 0.91
      reformulation_difficulty_correlation: 0.83
      constat_dif_flag_jaccard: 0.18
    result_rationale: >
      ConStat detects contamination by measuring performance DROP on semantically equivalent
      reformulations — if a model memorized the exact wording, it performs worse on
      paraphrases. This works well on non-RL models (AUROC=0.74) because memorization creates
      a sharp original-vs-reformulation gap. On reasoning-RL models, PPO/GRPO training
      generalizes the memorized knowledge to nearby phrasings, collapsing the perturbation
      signal (AUROC drops to 0.55). The 17.3% flagging rate at FDR q=0.05 is reasonable —
      ConStat is conservative by design. Low Jaccard overlap with DIF (0.18) is expected:
      ConStat detects per-model memorization signals while DIF detects group-level differential
      functioning — they capture fundamentally different aspects of contamination. Variant
      contamination (model trained on paraphrased items) is harder for ConStat (AUROC=0.61)
      because both original and reformulation are equally "seen."
    tables:
      - title: "Table: ConStat Detection Power by Model Type and Contamination Type"
        columns: [model_type, contam_type, auroc, tpr_at_fpr010, n_models]
        rows:
          - [non_rl, verbatim, 0.74, 0.42, 42]
          - [non_rl, variant, 0.61, 0.24, 42]
          - [reasoning_rl, verbatim, 0.55, 0.18, 11]
          - [reasoning_rl, variant, 0.48, 0.09, 11]
    figures_description:
      - "ROC curves: ConStat detection for non-RL vs reasoning-RL models, verbatim vs variant contamination"
      - "Heatmap: ConStat flag vs DIF flag overlap by MMLU subject"
    analysis: >
      ConStat provides a complementary signal to DIF: per-model perturbation sensitivity
      vs group-level differential functioning. Under best tier, ConStat works well enough
      on non-RL models to serve as an ensemble component, but degrades on reasoning-RL as
      expected. This experiment is marked as future work in the current paper framing — results
      would strengthen a methods-comparison table but are not load-bearing for any current
      claim.

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      DVD generation variance analysis on 10-15 open-weight models with 50 responses
      per item via temperature sampling.
    expected_results:
      n_models: 12
      n_items_tested: 500
      responses_per_item: 50
      temperature: 0.8
      dvd_bimodal_detection_pct: 12.4
      dvd_auroc_verbatim: 0.67
      dvd_auroc_variant: 0.53
      dvd_tpr_at_fpr010: 0.28
      generation_variance_clean_mean: 0.34
      generation_variance_contaminated_mean: 0.18
      variance_ratio_clean_vs_contam: 1.89
      dvd_dif_flag_jaccard: 0.13
      dvd_constat_flag_jaccard: 0.22
      gpu_hours_actual: 58
    result_rationale: >
      DVD detects contamination via generation variance: memorized items produce consistently
      correct answers across temperature samples (low variance), while genuinely understood
      items show natural stochasticity. The 1.89 variance ratio is moderate — contaminated
      items have roughly half the generation variance of clean items. 12.4% bimodal detection
      reflects items where some models show memorization signature (near-zero variance) while
      others show normal variance. AUROC=0.67 for verbatim contamination is decent but below
      ConStat (0.74) because generation variance is a noisier signal — temperature sampling
      introduces variance even on memorized items, and some genuinely easy items also have
      low variance. Variant contamination AUROC drops to 0.53 (near chance) because
      paraphrase-based contamination doesn't produce the sharp variance reduction that
      verbatim memorization does. Low Jaccard with DIF (0.13) is expected — DVD is a
      per-model metric while DIF is group-level.
    tables:
      - title: "Table: DVD Generation Variance Statistics"
        columns: [item_category, mean_variance, std_variance, bimodal_pct]
        rows:
          - [clean_items, 0.34, 0.12, 3.1]
          - [dif_flagged_items, 0.29, 0.15, 8.7]
          - [injected_verbatim, 0.18, 0.09, 12.4]
          - [injected_variant, 0.31, 0.13, 5.2]
    figures_description:
      - "Violin plot: generation variance distribution by item category (clean, DIF-flagged, injected)"
      - "Bimodality detection example: variance histogram for a representative contaminated item showing bimodal peak structure"
    analysis: >
      DVD provides the weakest individual signal of the three methods but captures a unique
      dimension — generation-time behavioral signatures that neither DIF nor ConStat access.
      As with plan_003a, this is future work under current framing. The 58 GPU-hours cost
      is substantial for a supporting result. Strongest contribution would be in the ensemble
      (plan_003c) where DVD covers variant contamination cases that ConStat misses.

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      Fuse DIF + ConStat + DVD into multi-signal ensemble with calibrated thresholds,
      majority voting, and weighted fusion.
    expected_results:
      majority_2of3_fpr: 0.07
      majority_2of3_tpr_verbatim: 0.58
      majority_2of3_tpr_variant: 0.34
      weighted_fusion_fpr: 0.06
      weighted_fusion_tpr_verbatim: 0.64
      weighted_fusion_tpr_variant: 0.39
      weighted_fusion_auroc: 0.82
      uniform_weight_auroc: 0.79
      cv_5fold_auroc_std: 0.03
      dif_coverage_delta_ge_14: true
      constat_coverage_non_rl_delta_ge_06: true
      dvd_coverage_variant: partial
      ensemble_fpr_all_configs_below_010: true
      optimal_weights: {dif: 0.45, constat: 0.35, dvd: 0.20}
    result_rationale: >
      The ensemble works because the three detectors exploit orthogonal signals: DIF uses
      group-level response pattern differences (robust to RL, needs large groups), ConStat
      uses per-model perturbation sensitivity (strong on non-RL, degrades on RL), DVD uses
      generation variance (unique signal, noisiest). Majority voting at 2-of-3 achieves
      FPR=0.07 because false positives from one method are unlikely to be corroborated by
      another operating on a different signal. The weighted fusion gives DIF the highest
      weight (0.45) because it has the best calibrated FPR and strongest theoretical grounding.
      Cross-validation shows stable performance (std=0.03 on AUROC) because the three signals
      are largely uncorrelated in their error patterns. The ensemble FPR < 0.10 across all
      configurations confirms operational reliability. Variant contamination remains the
      hardest case (TPR=0.39) because no individual method handles it well — this is an
      honest limitation.
    tables:
      - title: "Table: Ensemble Performance Comparison"
        columns: [strategy, fpr, tpr_verbatim, tpr_variant, auroc]
        rows:
          - [dif_only, 0.04, 0.48, 0.12, 0.76]
          - [constat_only, 0.06, 0.42, 0.24, 0.71]
          - [dvd_only, 0.08, 0.28, 0.19, 0.64]
          - [majority_2of3, 0.07, 0.58, 0.34, 0.79]
          - [weighted_fusion, 0.06, 0.64, 0.39, 0.82]
          - [uniform_weight, 0.07, 0.61, 0.36, 0.79]
    figures_description:
      - "Coverage Venn diagram: items detected by DIF-only, ConStat-only, DVD-only, and overlaps"
      - "ROC curves: individual detectors vs majority voting vs weighted fusion"
    analysis: >
      The ensemble demonstrates clear additive value over any single detector. Under best
      tier, the +0.06 AUROC gain from DIF-only (0.76) to weighted fusion (0.82) justifies
      the multi-method approach. However, this entire experiment tree (003a/b/c) is currently
      designated as future work — the paper's four claims stand without it. Strongest case
      for inclusion would be as a §6 "Extensions" section showing the framework's
      composability. The 270 total GPU-hours across 003a/b/c is a significant investment
      for a non-load-bearing result.

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      Pilot bifactor IRT equating on MMLU: fit bifactor model, select anchor items,
      calibrate replacements via fixed-parameter calibration, demonstrate equated score
      equivalence.
    expected_results:
      bifactor_general_factor_variance_pct: 61.3
      bifactor_subject_factor_variance_pct_range: [8.2, 27.4]
      bifactor_rmsea: 0.019
      bifactor_cfi: 0.978
      n_anchor_items_selected: 6107
      anchor_selection_criteria: "no_DIF_flag AND discrimination>0.5 AND fit_residual<2.0"
      anchor_pct_of_total: 48.8
      n_replacement_items_calibrated: 500
      fixed_param_calibration_convergence_pct: 94.2
      equated_score_spearman_rho: 0.976
      equated_score_rmse: 1.83
      equated_vs_unequated_rank_change_max: 127
      equated_vs_unequated_rank_change_mean: 8.4
    result_rationale: >
      The bifactor model fits well (RMSEA=0.019, CFI=0.978) because MMLU genuinely has a
      general factor (broad LLM capability) plus subject-specific factors — this is the
      correct psychometric model for a multidimensional benchmark. The general factor
      explains 61% of variance, confirming that a dominant unidimensional signal exists
      (supporting the adequacy of simpler IRT for ranking purposes). Anchor item selection
      retains ~49% of items — the non-DIF items with adequate discrimination and model fit.
      This is enough for stable equating. Fixed-parameter calibration converges at 94%
      because most replacement items are well-behaved (the 6% non-convergence reflects items
      with extreme parameters or poor fit). The equated score ρ=0.976 exceeds the 0.95
      threshold because equating preserves the dominant general factor — subject-specific
      variance introduces minor rank perturbations (mean change 8.4 ranks out of ~5000) but
      the overall ordering is highly stable. This confirms MMLU's measurement redundancy
      finding from plan_017 via a different lens.
    tables:
      - title: "Table: Bifactor Model Fit and Factor Structure"
        columns: [factor, variance_explained_pct, n_items_loading_above_03]
        rows:
          - [general, 61.3, 12508]
          - [subject_specific_mean, 15.8, 219]
          - [subject_specific_min, 8.2, 87]
          - [subject_specific_max, 27.4, 412]
      - title: "Table: Equating Quality by Replacement Rate"
        columns: [replacement_pct, n_replaced, spearman_rho, rmse, max_rank_change]
        rows:
          - [5, 625, 0.998, 0.41, 23]
          - [10, 1251, 0.994, 0.89, 54]
          - [20, 2502, 0.987, 1.34, 89]
          - [31, 3918, 0.976, 1.83, 127]
    figures_description:
      - "Scree plot: eigenvalues for general factor + top 10 subject factors, showing dominant first eigenvalue"
      - "Bland-Altman plot: equated vs original scores, showing mean bias and limits of agreement"
    analysis: >
      This experiment extends plan_017's ranking redundancy finding by providing a principled
      psychometric framework for item replacement. Under best tier, the ρ=0.976 result at
      31% replacement (replacing ALL DIF items) confirms that equated benchmarks can maintain
      validity. However, this experiment relates to the dropped "regeneration" claim (old
      Claim 3) — under the current paper pivot, this is future work. Could appear as a
      brief §7 "Toward Benchmark Maintenance" sketch if space permits.

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      Generate replacement items for DIF-flagged MMLU questions using LLM generation
      with construct constraints, calibrated via student simulation.
    expected_results:
      n_dif_items_targeted: 500
      n_replacements_generated: 1500
      n_replacements_passing_quality: 1127
      quality_pass_rate: 0.751
      student_sim_difficulty_correlation: 0.78
      prompt_based_difficulty_correlation: 0.32
      student_sim_discrimination_correlation: 0.64
      empirical_difficulty_match_within_015_logits: 0.68
      empirical_difficulty_match_within_030_logits: 0.89
      holdout_panel_n_models: 30
      holdout_spearman_original_vs_replacement: 0.971
      subject_coverage_all_57: true
      cognitive_level_match_pct: 82.4
      gpu_hours_actual: 173
    result_rationale: >
      LLM-generated items achieve r=0.78 difficulty correlation via student simulation
      because the simulation approach (arXiv 2601.09953) directly estimates how a population
      of models will respond — much more informative than prompt-based difficulty targeting
      (r=0.32), which only captures surface-level difficulty cues. The 75% quality pass rate
      reflects that ~25% of generated items have flaws: ambiguous wording, incorrect answer
      keys, or construct misalignment detected by automated checks. The 0.68 rate of
      difficulty matching within 0.15 logits means most replacements are "close enough" for
      equating — the remaining 32% need iterative regeneration or manual adjustment. 82%
      cognitive level match indicates LLMs can reproduce factual recall and comprehension
      items well, but struggle more with application and analysis items (the 18% mismatch
      concentrates in these higher Bloom levels). The holdout ρ=0.971 confirms replacement
      items preserve measurement function at the benchmark level.
    tables:
      - title: "Table: Difficulty Calibration Method Comparison"
        columns: [method, difficulty_r, discrimination_r, within_015_logits_pct]
        rows:
          - [prompt_based_targeting, 0.32, 0.18, 0.24]
          - [student_simulation, 0.78, 0.64, 0.68]
          - [student_sim_plus_iterative, 0.84, 0.71, 0.82]
    figures_description:
      - "Scatter plot: predicted difficulty (student sim) vs empirical difficulty, with r=0.78 annotation"
      - "Bar chart: cognitive level match rates by Bloom's taxonomy level (remember, understand, apply, analyze)"
    analysis: >
      Item generation calibration demonstrates a practical pipeline for benchmark
      maintenance. Under best tier, the student simulation approach substantially outperforms
      naive prompt-based generation. However, 173 GPU-hours and the dependency on plan_005
      make this the most resource-intensive experiment chain. Like plan_005, this supports
      the dropped regeneration claim — future work under current framing.

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      Simulate 4 successive benchmark administrations with cumulative Bayesian DIF priors
      (Sinharay et al., 2006) to show power improvement from evidence accumulation.
    expected_results:
      n_simulated_administrations: 4
      n_items_per_administration: 12508
      n_models_per_administration: [1253, 656, 800, 900]
      individual_power_delta_10: 0.41
      cumulative_power_2_admin_delta_10: 0.57
      cumulative_power_3_admin_delta_10: 0.71
      cumulative_power_4_admin_delta_10: 0.77
      individual_fpr: 0.048
      cumulative_fpr_4_admin: 0.022
      bayesian_shrinkage_factor_mean: 0.73
      posterior_credible_interval_width_reduction_pct: 38
      individual_power_delta_14: 0.68
      cumulative_power_3_admin_delta_14: 0.89
    result_rationale: >
      Bayesian DIF accumulates evidence across administrations via informative priors —
      each administration's posterior becomes the next administration's prior. At δ=1.0
      (medium effect), individual administration power is only 0.41 because the MH statistic
      has limited sensitivity at this effect size with typical LLM benchmark sample sizes.
      After 3 administrations, the accumulated evidence pushes power to 0.71 — the prior
      effectively increases the sample size by pooling information. FPR decreases from 0.048
      to 0.022 because Bayesian shrinkage pulls spurious flags toward zero across
      administrations (transient false positives don't persist). The 38% credible interval
      width reduction reflects genuine information gain. At δ=1.4 (the MH operational
      threshold from power simulations), cumulative power reaches 0.89 after 3
      administrations — near the 0.90 monitoring standard. This provides a practical
      framework for longitudinal benchmark monitoring: any single time point may miss medium
      DIF, but persistent effects are reliably detected.
    tables:
      - title: "Table: Cumulative Bayesian DIF Power by Administration Count"
        columns: [n_administrations, power_delta_08, power_delta_10, power_delta_14, fpr]
        rows:
          - [1, 0.22, 0.41, 0.68, 0.048]
          - [2, 0.35, 0.57, 0.81, 0.033]
          - [3, 0.47, 0.71, 0.89, 0.025]
          - [4, 0.54, 0.77, 0.93, 0.022]
    figures_description:
      - "Power curves: detection power vs effect size (δ) for 1-4 cumulative administrations, showing progressive improvement"
      - "FPR trajectory: false positive rate decreasing across administrations due to Bayesian shrinkage"
    analysis: >
      Cumulative Bayesian DIF is a natural extension for benchmark monitoring. Under best
      tier, the power improvement from 0.41 to 0.71 at δ=1.0 after 3 administrations is
      compelling for longitudinal deployment. Zero GPU cost makes this attractive. However,
      it's P2 priority — a nice-to-have for a future-work section or a follow-up paper on
      operational benchmark monitoring. The simulation is clean and fast to execute; if space
      permits, a single figure could convey the key message.

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      Formal analysis of benchmark validity under progressive item replacement: define
      validity metrics, simulate replacement rates 5-50%, establish theoretical bounds.
    expected_results:
      replacement_5pct_rho: 0.9991
      replacement_5pct_shr: 0.9928
      replacement_5pct_construct_coverage: 0.997
      replacement_10pct_rho: 0.9984
      replacement_10pct_shr: 0.9921
      replacement_10pct_construct_coverage: 0.993
      replacement_20pct_rho: 0.9962
      replacement_20pct_shr: 0.9904
      replacement_20pct_construct_coverage: 0.984
      replacement_50pct_rho: 0.9871
      replacement_50pct_shr: 0.9842
      replacement_50pct_construct_coverage: 0.951
      theoretical_bound_rho: "1 - O(r × (1 - ρ_anchor²))"
      theoretical_bound_shr: "1 - O(r × σ²_replacement / σ²_original)"
      critical_replacement_rate_rho_below_099: 0.27
      critical_replacement_rate_shr_below_098: 0.41
    result_rationale: >
      MMLU's massive measurement redundancy (ρ=0.997 at 31% removal from plan_017) means
      replacement degrades validity very slowly. At 5% replacement, ρ=0.9991 because only
      625 items change, and equating ensures replacement items measure similar constructs.
      The degradation is approximately linear in replacement rate when equating is well-
      calibrated, because each replaced item introduces independent small perturbation. The
      theoretical bound involves the replacement rate r multiplied by the (1 - ρ²_anchor)
      term — when anchor items are strong (ρ_anchor ≈ 0.99), the multiplicative penalty is
      tiny. SHR degrades slightly faster than Spearman ρ because split-half reliability is
      more sensitive to local item perturbations than rank ordering. Construct coverage
      (proportion of subject domains with ≥10 items remaining) stays above 0.95 even at 50%
      replacement because MMLU's 57 subjects average 219 items each — even halving doesn't
      eliminate coverage. The critical rate of 27% for ρ<0.99 aligns with the empirical
      finding that 31% DIF removal gives ρ=0.996 — replacement with equated items is LESS
      disruptive than removal.
    tables:
      - title: "Table: Validity Degradation Under Progressive Replacement"
        columns: [replacement_pct, spearman_rho, shr, construct_coverage, max_rank_change]
        rows:
          - [0, 1.000, 0.9934, 1.000, 0]
          - [5, 0.9991, 0.9928, 0.997, 18]
          - [10, 0.9984, 0.9921, 0.993, 42]
          - [20, 0.9962, 0.9904, 0.984, 78]
          - [31, 0.9938, 0.9886, 0.972, 127]
          - [50, 0.9871, 0.9842, 0.951, 203]
    figures_description:
      - "Line plot: Spearman ρ and SHR vs replacement rate (0-50%), with theoretical bound overlay"
      - "Heatmap: per-subject construct coverage at each replacement rate, highlighting subjects dropping below 10 items"
    analysis: >
      This experiment provides the theoretical backbone for equating-based benchmark
      maintenance. Under best tier, the key message is that MMLU can tolerate ~27% item
      replacement while maintaining ρ>0.99 — and since DIF flags 31% of items, a single
      replacement cycle could refresh the most unstable items with minimal validity loss.
      Depends on plan_005/006; shares their "future work" status under current framing.

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Implement Item-Focused Trees (Tutz & Berger, 2016) using model release date as
      continuous covariate. Compare detection power and flexibility vs categorical DIF.
    expected_results:
      n_items_analyzed: 12508
      n_models_with_release_date: 3842
      ift_significant_date_effect_pct: 34.7
      ift_gradual_drift_items_pct: 8.3
      ift_abrupt_change_items_pct: 26.4
      ift_categorical_dif_overlap_pct: 81.2
      ift_unique_detections_pct: 5.8
      categorical_dif_unique_pct: 2.4
      ift_split_date_mode: "2023-09"
      ift_split_date_range: ["2023-06", "2024-01"]
      ift_detection_power_delta_14: 0.72
      ift_fpr: 0.041
      ift_vs_mh_concordance_kappa: 0.74
    result_rationale: >
      IFT treats release date as a continuous covariate and recursively partitions the
      model sample to find the split that maximizes DIF detection — avoiding the arbitrary
      2023/2024-H1 boundary. The 81% overlap with categorical DIF confirms the temporal
      boundary is approximately correct: IFT's modal split date (2023-09) is close to the
      categorical cutoff. The 5.8% unique IFT detections are items with gradual drift —
      their DIF effect accumulates slowly over time, crossing the threshold only when IFT
      optimally places the split point. These tend to be items where capability improvement
      is continuous rather than punctuated (e.g., math reasoning items that gradually become
      easier). The 8.3% gradual drift items (where IFT fits a smooth function rather than a
      step change) capture a distinct drift pattern: these items don't suddenly change but
      their functioning shifts continuously as model capability increases. IFT detection
      power (0.72 at δ=1.4) is comparable to MH (0.68) because optimal split placement
      partially compensates for the loss of predetermined grouping. Cohen's κ=0.74
      indicates substantial agreement — the two methods capture largely overlapping phenomena
      via different mechanisms.
    tables:
      - title: "Table: IFT vs Categorical DIF Detection Comparison"
        columns: [method, significant_pct, unique_pct, fpr, power_delta_14, kappa]
        rows:
          - [categorical_mh, 31.3, 2.4, 0.042, 0.68, "—"]
          - [ift_continuous, 34.7, 5.8, 0.041, 0.72, 0.74]
          - [intersection, 28.9, "—", "—", "—", "—"]
      - title: "Table: IFT Drift Pattern Classification"
        columns: [pattern, pct_of_significant, example_domain, interpretation]
        rows:
          - [abrupt_change, 76.1, abstract_algebra, "sudden capability jump at specific model generation"]
          - [gradual_drift, 23.9, high_school_mathematics, "continuous capability improvement over time"]
    figures_description:
      - "IFT tree visualization for a representative item: split at 2023-09, showing DIF effect size in each partition"
      - "Temporal DIF effect trajectory: 5 example items showing abrupt vs gradual drift patterns"
    analysis: >
      IFT validates the categorical DIF approach while revealing additional nuance. Under
      best tier, the 81% overlap confirms the 2023/2024-H1 split is appropriate, and the
      unique gradual-drift detections provide a richer characterization of temporal instability.
      P2 priority — an elegant methodological refinement that strengthens Claim 1 but isn't
      required for it. The key insight (gradual vs abrupt drift patterns) could motivate a
      follow-up paper on continuous benchmark monitoring. Zero GPU cost; the main investment
      is implementation of the IFT algorithm.
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "4a7cd534-b463-4314-bd81-9c9205d88744",
  "isSidechain": false,
  "requestId": "req_011CbF1KeqcxpGQvWWF4jkmv",
  "type": "assistant",
  "uuid": "645d3f1e-89ad-42c9-8d4d-c5c80eefdb48",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01CJUpDBWhh2jhvZSkgEaJ43",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 17084,
      "cache_read_input_tokens": 11841,
      "output_tokens": 15054,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 17084,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 15054,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 17084,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 17084
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Architecture stratification confirms DIF finding is real signal, not population heterogeneity artifact; instability partially independent of capability imp…",
  "leafUuid": "645d3f1e-89ad-42c9-8d4d-c5c80eefdb48",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF validation framework for benchmark structural analysis",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 best 档的含义：  含义：Architecture stratification confirms DIF finding is real signal, not population heterogeneity artifact; instability partially independent of capability imp…",
  "leafUuid": "645d3f1e-89ad-42c9-8d4d-c5c80eefdb48",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "DIF validation framework for benchmark structural analysis",
  "sessionId": "2cfaa65f-72b1-47fa-82d8-3ab65e16d19f"
}
```

---
