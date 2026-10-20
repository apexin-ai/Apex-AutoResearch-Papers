# Research conversation: 你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义： 含义：Permutation null 暴露 temporal structure 显著 inflate DIF，ability confound 比预期严

**Temporal Score Incomparability in LLM Benchmarks: A Large-Scale Psychometric Audit of 5,227 Models (July export snapshot)** · Conversation logs

This page is a human-readable rendering of one source record. It preserves the recorded order and wording; the linked JSON keeps the complete machine-readable structure.

## Record overview

- **Events:** 13
- **Recorded user turns:** 1
- **Tool calls:** 0
- **Original source:** `logs/chats/exported-trajectories/account-2/ecedaf1a-ae54-46fe-97ae-3de8dd377c47.jsonl`
- **Structured JSON:** [`0f4e07f8d7782ee7187e.json`](../../sessions/0f/0f4e07f8d7782ee7187e.json)

## How to read this transcript

`User` marks a recorded user-role instruction, `Assistant` marks an agent response, and the collapsible `Tool call` / `Tool result` blocks show the actions and observations between them. A user-role record may come from another agent or the runtime system; it is not an authorship label.

## Before a recorded user message

2 recorded events

### Runtime record

_source line 1 · 2026-05-21T12:44:43.767Z_

````json
{
  "type": "queue-operation",
  "operation": "enqueue",
  "timestamp": "2026-05-21T12:44:43.767Z",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47",
  "content": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：\n\n含义：Permutation null 暴露 temporal structure 显著 inflate DIF，ability confound 比预期严重，reviewer 一致认为贡献不足以达到 EMNLP long paper 门槛 — 需要 reframe 但不降级 venue\n核心假设：['plan_029 permutation null C% 在 8–18%：temporal cohort 的 ability gap（虽然 d=-0.17）在 12,508 items × 1,887 models 的规模下产生系统性 DIF inflation，31% 中有相当部分是 ability confound 的 residual artifact', 'NN matching C%=28.9% 被 reviewer 质疑：匹配后 d≈-0.01 但 remaining DIF 可能反映 matching 未覆盖的 latent dimensions（57-subject multidimensionality），不足以排除 confound', \"至少两位 reviewer 给 borderline reject，核心理由：(1) no methodological contribution, (2) 31% 可能 inflated, (3) 'diagnostic lens' 是 post-hoc reframing\", '6 benchmark 中 HellaSwag（17.9%）和 GSM8K（18.9%）明显低于 MMLU（31.3%），reviewer 质疑 benchmark 间差异是否反映方法 artifact 而非真实 instability 差异', \"Simpson's paradox + negative GSM1K correlation 被 reviewer 解读为 DIF 实际上在 capture ability improvement 而非 item-level instability\"]\n关键指标范围：{'permutation_null_c_pct': [8.0, 18.0], 'residual_c_pct_after_all_controls': [15.0, 23.0], 'ability_confound_explained_pp': [6.0, 12.0], 'cross_benchmark_c_range_pct': [12.0, 32.0], 'semi_synthetic_delta_tpr_p05': [0.25, 0.4], 'cross_subject_delta_fpr': [0.005, 0.02], 'ranking_stability_rho': [0.99, 0.996], 'simulated_avg_reviewer_score': [1.5, 2.5], 'page_count_main_body': [8.5, 9.5]}\n叙事方向：核心 reframe：从 'DIF reveals 31% instability' 转向 'Permutation-calibrated DIF reveals 15–23% genuine item-level instability after accounting for temporal ability structure — still 2–3× above null, and the methodology for separating genuine DIF from ability artifact is itself a contribution.' Paper 重心从 Claim 1 的 headline number 转移到三个方向：(1) Semi-synthetic validation framework（Claim 3）升格为 primary contribution — ΔFPR=0 的 cross-subject matching 是 genuine methodological insight，独立于 instability magnitude；(2) Multi-benchmark temporal DIF atlas（6 benchmarks × permutation-calibrated）作为 empirical resource contribution；(3) Permutation null 本身成为 finding — 'temporal cohort structure inflates naive DIF by X pp, establishing calibration requirements for future LLM DIF studies.' Meta-critique（Claim 2）保留但从 aggressive 改为 measured。Diagnostic lens 保留但弱化 claim 强度。Abstract 不再领 31%，改领 'permutation-calibrated genuine instability rate' + 'semi-synthetic validation framework with provable FPR control.' 仍冲 EMNLP long paper，但需要 camera-ready 前补充 propensity-score matching 或 MIMIC model 作为 additional robustness。\n\n基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。\n每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。\n\n# Project context\nproject: irt_equated_bench_regen\nvenue: emnlp-2026\n\n## paper_framing.md\n\n# Paper Framing — irt_equated_bench_regen\n\n## Target Venue\n- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)\n- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)\n\n## Paper Type\nEmpirical analysis / psychometric characterization. Discovery paper, not methods paper. \"DIF reveals benchmark structural problems,\" not \"DIF detects contamination.\"\n\n## Core Claims (4 条, 可证伪)\n\n**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).\n- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)\n- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.\n- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.\n\n**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).\n- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)\n- Framing: aggressive — \"the field's standard validation approach is fundamentally mismatched for item-level detection\" — now with direct empirical evidence, not just conceptual argument\n\n**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).\n- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)\n- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks\n- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability\n\n**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:\n1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.\n2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies \"items that changed across generations,\" not \"good items.\"\n3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not \"find bad items and remove\" but \"understand what changed and why.\" Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.\n4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.\n- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)\n- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.\n- Growing Pains互补: \"Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading\"\n- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed\n\n## Story Spine (v2 — no-pivot narrative)\n\n**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say \"Model B outperforms Model A on MMLU,\" we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.\n\n**Key narrative principle**: \"Instability ≠ invalidity.\" DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**\n\n**What we find** (4 contributions, focused):\n\n1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for \"models got better.\"\n\n2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.\n\n3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.\n\n4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).\n\n**Headline result**: \"Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance.\"\n\n## Scope Control (main body vs appendix)\n\n**MAIN BODY (4 claims + robustness)**:\n- §1 Introduction (problem + \"instability ≠ invalidity\" framing upfront)\n- §2 Related Work (45 papers, 5 clusters)\n- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)\n- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)\n- §5 Discussion + Limitations\n- §6 Conclusion\n\n**APPENDIX (pruned from main body)**:\n- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped\n- RL robustness (plan_002) — N=13, underpowered\n- Ensemble fusion (plan_003a/b/c) — negative, not executed\n- Bifactor equating pilot — below target fit\n- Item generation pilot — below benchmarks\n- Graceful degradation — clean but supplementary\n- Item-Focused Trees — robustness check, supplementary\n- ConStat/DVD comparisons — complementary baselines\n\n## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks\n\nSystematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.\n\n## Venue Fit\n\n- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. \"Empirical, not algorithmic\" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.\n\n## Novelty Articulation (三层，显式化)\n\nMH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:\n\n1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.\n\n2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).\n\n3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).\n\n**Framing**: \"We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm.\"\n\n## Anticipated Reviewer Concerns (updated for pivot)\n\n1. **\"31% could just mean models got better / ability confound inflates C%\"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.\n\n2. **\"Ground truth critique is obvious — of course web labels don't capture differential effects\"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.\n\n3. **\"Semi-synthetic injection is artificial\"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.\n\n4. **\"DIF power is only sufficient for large effects\"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.\n\n5. **\"Only validated on MMLU\"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.\n\n6. **\"Higher methods (MIMIC, propensity-score) could solve the confounding\"** — Acknowledged as future work. We frame our three-attempt negative results as \"empirical observation\" that motivates these directions, not as impossibility.\n\n7. **\"ETS threshold is uncalibrated for LLM populations\"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: \"finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF.\" Do NOT claim \">15% at all thresholds\" — be honest that 2.5 drops below.\n\n8. **\"Multiple testing: 12,508 simultaneous tests without correction\"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.\n\n9. **\"Only uniform DIF — non-uniform DIF plausible for LLMs\"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: \"our 31% uniform-only estimate is conservative.\"\n\n10. **\"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance\"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.\n\n11. **\"Ranking disruption result is tautological\"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.\n\n## Dropped from Original Framing\n\n- **Ensemble (Claim 2 old)**: plan_003a/b/c never executed. Future work.\n- **Regeneration (Claim 3 old)**: Bifactor killed by plan_014 pre-check. Dropped entirely.\n- **RL robustness**: Theoretically motivated but N=13 insufficient. Limitations disclosure, not claim.\n- **Detection as primary contribution**: Pivoted from \"we detect contamination\" to \"we characterize benchmark properties.\"\n\n\n## experiment_plan (with registry status)\n\n- id: plan_001\n  name: real_data_dif_mmlu\n  claim: 1\n  description: \"Apply DIF analysis to METABENCH MMLU response matrix (5,219 models\\\n    \\ × 12,508 items). Data characteristics: only 37% models classifiable by family\\\n    \\ (1,929); effective temporal span ~1.5 years (2023: N=1,253, 2024-H1: N=656);\\\n    \\ 15.4% items have negative discrimination. Design: (a) Primary cohort: temporal\\\n    \\ split (2023 vs 2024-H1, both N≥80 ✓) (b) Alternative cohort: accuracy-quintile\\\n    \\ split (ability-based grouping, uses all models) (c) Item filtering: run with\\\n    \\ and without negative-discrimination items (sensitivity analysis) Run ETS C DIF\\\n    \\ detection on all items under both cohort definitions. Proxy validation against\\\n    \\ Li et al. (EMNLP 2024) web-overlap contamination labels (9,229 items, 73.8%\\\n    \\ coverage). IMPORTANT conceptual distinction: Li et al. labels are model-agnostic\\\n    \\ (item exists on web), while DIF detects cohort-differential contamination (item\\\n    \\ behaves differently across temporal cohorts). Low concordance is EXPECTED —\\\n    \\ DIF only catches items where contamination is differential across cohorts, not\\\n    \\ uniform. Primary validation metric: FPR analysis (DIF flags on Li-et-al-clean\\\n    \\ items) rather than TPR (which conflates uniform vs differential contamination).\\\n    \\ Unlabeled items (26.2%) reported separately as \\\"unknown\\\". plan_011 (semi-synthetic\\\n    \\ injection) provides controlled ground truth to complement this proxy. (d) Within-family\\\n    \\ confound control: run DIF within model families where both versions\\n    have\\\n    \\ N≥80. Confirmed feasible: Llama-2 (N=161) vs Llama-3 (N=308) ✓. Qwen-1.5 (N=67)\\n\\\n    \\    below threshold — use as supplementary only. Identify additional qualifying\\\n    \\ pairs from\\n    METABENCH metadata. If DIF flags\\n    items that are NOT differentially\\\n    \\ contaminated within-family, the flag reflects capability\\n    gain, not contamination.\\\n    \\ Report: DIF flag overlap between cross-cohort and within-family\\n    analyses\\\n    \\ to disentangle contamination from capability improvement.\\n(e) Domain-specificity\\\n    \\ analysis: correlate DIF flags with MMLU subject categories to check\\n    whether\\\n    \\ flags cluster in domains with known capability jumps vs known contamination.\\n\\\n    Report: DIF flags × cohort definition × item filtering — 4-way sensitivity matrix\\\n    \\ + within-family confound control + domain-specificity analysis.\\n\"\n  priority: P0\n  gpu_budget_hours: 0\n  deps: []\n  registry_id: ''\n  status: planned\n- id: plan_002\n  name: rl_robustness_validation\n  claim: 1\n  description: \"Empirically validate DIF's RL-robustness claim. CRITICAL DISTINCTION:\\\n    \\ - \\\"Alignment RL\\\" (DPO/ORPO/KTO) = offline preference optimization, does NOT\\\n    \\ produce\\n  the NLL gap contraction that Wang et al. demonstrate. METABENCH has\\\n    \\ 477 such models.\\n- \\\"Reasoning RL\\\" (GRPO/PPO online training) = the mechanism\\\n    \\ that conceals contamination\\n  signals. This is what Claim 1 targets. METABENCH\\\n    \\ has almost none of these.\\nDesign (Reviewer-validated): (a) SFT-only cohort\\\n    \\ from METABENCH as baseline (b) Alignment-RL cohort (DPO/ORPO, N=477) from METABENCH\\\n    \\ as mechanism control —\\n    DPO doesn't use PPO clipping, so no NLL gap contraction;\\\n    \\ if DIF works on both\\n    (a) and (b), robustness covers the full RL spectrum\\n\\\n    (c) Reasoning-RL models (DeepSeek-R1-7B/32B, Qwen2.5-RL, etc.) — run MMLU inference\\n\\\n    \\    on 10-15 open-weight GRPO/PPO models. These are ADDED to the focal cohort\\n\\\n    \\    (not a standalone group): DIF is group-level, so we verify that adding RL\\\n    \\ models\\n    to a cohort doesn't degrade detection. Separately, run traditional\\\n    \\ detectors\\n    (Min-K%, ConStat) on these 10-15 models individually to show\\\n    \\ per-model degradation.\\nTwo-level validation: - Group level: DIF flags same\\\n    \\ items regardless of cohort composition (a/b/c) → robust - Model level: traditional\\\n    \\ detectors degrade on (c) individuals → fragile This design works even with only\\\n    \\ 10-15 reasoning-RL models because DIF doesn't need N≥80 RL models — it needs\\\n    \\ N≥80 in the cohort total, and RL models are mixed in. Statistical rigor requirements:\\\n    \\ - Bootstrap 95% CIs on all AUROC comparisons (DIF vs ConStat vs Min-K%) - DeLong\\\n    \\ test or permutation test for pairwise AUROC differences - TOST equivalence testing\\\n    \\ for DIF retention ratio vs ConStat (not just null-result reasoning) (d) Partial\\\n    \\ exploitation power analysis: formally characterize DIF detection power as\\n\\\n    \\    function of exploitation rate p ∈ [0.4, 1.0]. At p<1, contaminated model\\\n    \\ answers\\n    memorized items correctly with probability p, shrinking DIF effect\\\n    \\ size by ~p.\\n    Show detection boundary and ensemble coverage handoff point.\\n\"\n  priority: P0\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003a\n  name: constat_perturbation_eval\n  claim: 2\n  description: 'Independent evaluation of ConStat-style perturbation testing on MMLU:\n    (a) Generate semantically equivalent reformulations for 200+ MMLU items using\n    LLM paraphrasing (b) Compare model performance on original vs reformulated items\n    (c) Apply FDR-controlled detection (ConStat protocol) (d) Characterize detection\n    power by effect size — expected strength on non-RL models, weakness on RL Even\n    if DIF or DVD fails, ConStat standalone results have paper value as baseline comparison.\n\n    '\n  priority: P0\n  gpu_budget_hours: 80\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003b\n  name: dvd_generation_variance_eval\n  claim: 2\n  description: 'Independent evaluation of DVD generation variance on MMLU: (a) Select\n    10-15 open-weight models with inference access (b) Generate 50 responses per item\n    via temperature sampling (T=0.7-1.0) (c) Compute generation variance scores; detect\n    bimodal distributions (contamination signal) (d) Characterize detection power\n    for variant contamination vs verbatim contamination Standalone results provide\n    variant-contamination detection baseline independent of DIF.\n\n    '\n  priority: P0\n  gpu_budget_hours: 70\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_003c\n  name: ensemble_fusion\n  claim: 2\n  description: 'Fuse DIF + ConStat + DVD into multi-signal ensemble: (a) Calibrate\n    per-signal thresholds on subset of items with known contamination status (b) Evaluate\n    2-of-3 majority voting and weighted fusion strategies (c) Show ensemble coverage:\n    DIF covers δ≥1.4, ConStat covers non-RL δ≥0.6, DVD covers variant (d) Precision\n    analysis: ensemble FPR<0.10 across all configurations (e) Cross-validate fusion\n    weights (5-fold); report uniform-weight baseline alongside optimized Depends on\n    003a and 003b completing; if one signal fails, degrade to 2-signal ensemble.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  - plan_003a\n  - plan_003b\n  registry_id: ''\n  status: planned\n- id: plan_004\n  name: cross_benchmark_gsm8k\n  claim: 1\n  description: 'Replicate DIF analysis on GSM8K using GSM1K as ground truth for contamination.\n    Collect per-item binary responses from 50+ models on GSM8K (via existing leaderboard\n    data or inference). Run DIF across temporal cohorts. Correlate DIF flags with\n    per-model GSM8K-GSM1K accuracy gap. Validates cross-benchmark generalizability\n    and provides an independent ground truth beyond Li et al. proxy labels.\n\n    '\n  priority: P1\n  gpu_budget_hours: 100\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_005\n  name: bifactor_irt_equating_pilot\n  claim: 3\n  description: 'Pilot bifactor IRT equating on MMLU: NOTE: METABENCH preproc.rds contains\n    CTT statistics (p-value, rpbis), NOT IRT parameters. True IRT params are in mirt\n    model objects (crossvalidate.R). Must either extract from METABENCH mirt RDS files\n    or refit from the 5219×12508 response matrix. (a) Fit bifactor model to METABENCH\n    MMLU data (general factor + subject-specific factors) (b) Select anchor items\n    (high-stability, no DIF across cohorts) (c) Calibrate replacement items via fixed-parameter\n    calibration (Kim & Kolen 2019) (d) Demonstrate equated score equivalence: model\n    rankings on original vs replaced benchmark should correlate at Spearman rho ≥\n    0.95 after equating.\n\n    '\n  priority: P1\n  gpu_budget_hours: 50\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_006\n  name: item_generation_calibration\n  claim: 3\n  description: 'Generate replacement items for DIF-flagged MMLU questions: (a) Use\n    LLM generation with construct constraints (same subject, same cognitive level)\n    (b) Calibrate via student simulation (arXiv 2601.09953, r=0.75-0.82 for difficulty\n    estimation) (c) Compare difficulty correlation: prompt-based targeting (rho=0.10-0.45\n    per arXiv 2602.06631) vs empirical calibration via student simulation (d) Validate\n    on holdout model panel\n\n    '\n  priority: P1\n  gpu_budget_hours: 200\n  deps:\n  - plan_005\n  registry_id: ''\n  status: planned\n- id: plan_007\n  name: cumulative_bayesian_dif\n  claim: 1\n  description: 'Implement cumulative Bayesian DIF priors (Sinharay et al., 2006).\n    Simulate 4 successive benchmark administrations. Show power improvement from accumulating\n    evidence: individual administration power ~0.40 → cumulative power ~0.70 after\n    3 administrations for medium effects (δ=1.0).\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_008\n  name: graceful_degradation_analysis\n  claim: 3\n  description: 'Formal analysis of benchmark validity under item replacement: (a)\n    Define validity metrics (ranking stability, score reliability, construct coverage)\n    (b) Simulate progressive replacement (5%, 10%, 20%, 50% items replaced) (c) Establish\n    theoretical bounds on validity degradation as function of replacement rate (d)\n    Empirical validation using METABENCH data\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_005\n  - plan_006\n  registry_id: ''\n  status: planned\n- id: plan_009\n  name: item_focused_trees\n  claim: 1\n  description: 'Implement Item-Focused Trees (Tutz & Berger, 2016) as alternative\n    to categorical cohort DIF. Treat model release date as continuous covariate. Compare\n    detection power and flexibility vs categorical DIF. Advantages: avoids arbitrary\n    cohort splits, uses full model sample.\n\n    '\n  priority: P2\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_010\n  name: architecture_stratified_dif\n  claim: 1\n  description: \"Run DIF within architecture-homogeneous subpopulations to test whether\\\n    \\ IRT model fit improves and spurious DIF reduces when architecture heterogeneity\\\n    \\ is removed. Dream worst-case identified this as the critical missing experiment.\\\n    \\ Design: (a) Subset METABENCH to decoder-only models only (N≈3,000-4,000) (b)\\\n    \\ Report IRT fit diagnostics (RMSEA, CFI, TLI, SRMR) for this homogeneous subgroup\\\n    \\ (c) Run DIF detection on decoder-only temporal cohorts; compare FPR and TPR\\n\\\n    \\    vs full-population DIF from plan_001\\n(d) If fit improves substantially,\\\n    \\ conclusion is \\\"DIF requires architecture-homogeneous\\n    populations\\\" — a\\\n    \\ fixable constraint, not a fundamental limitation\\nZero GPU cost (uses existing\\\n    \\ METABENCH data). Proactive defense against worst-case reviewer concern about\\\n    \\ unidimensional IRT misfit.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_011\n  name: semi_synthetic_contamination_validation\n  claim: 1\n  description: \"Inject known contamination into the real METABENCH response matrix\\\n    \\ and measure DIF detection power under controlled ground truth. Addresses ground\\\n    \\ truth circularity concern (Li et al. proxy labels measure existence, not differential\\\n    \\ contamination). Design: (a) Select 500 items with known-clean status (no DIF\\\n    \\ flags, stable across cohorts) (b) For a random subset of 100-200 items, inject\\\n    \\ synthetic contamination:\\n    flip responses of focal-group models from incorrect→correct\\\n    \\ with probability p\\n    (simulating contamination at varying exploitation rates)\\n\\\n    (c) Run DIF detection; measure TPR/FPR against known-injected ground truth (d)\\\n    \\ Vary injection parameters: contamination prevalence (5%-30%), exploitation rate\\n\\\n    \\    (0.4-1.0), focal group size (N=40-200)\\nProvides controlled ground truth\\\n    \\ that proxy labels (Li et al.) and GSM1K cannot.\\n\"\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_028\n  name: multi_benchmark_temporal_dif\n  claim: 1,5\n  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,\n    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023\n    vs 2024) on each. Addresses Dream #6 three-tier consensus: \"only MMLU + GSM8K,\n    generalizability insufficient.\" Report C% + sample sizes + random-split control\n    for each benchmark.\n\n    '\n  priority: P0\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_029\n  name: permutation_null_c_rate\n  claim: 1\n  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels\n    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes\n    null distribution for C%. Dream #6 three-tier consensus: reviewers ask \"is 31%\n    above chance?\" Current random-split control (0.18%) is within-cohort, not temporal\n    permutation null.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n- id: plan_030\n  name: odds_ratio_regression_transparency\n  claim: 1\n  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke\n    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level\n    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.\n    Dream #6 two-tier concern.\n\n    '\n  priority: P1\n  gpu_budget_hours: 0\n  deps:\n  - plan_001\n  registry_id: ''\n  status: planned\n\n\n## registry (completed experiments)\n\n- exp_id: mvp_dif_power_sim\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    best_tpr_mh: 0.6817\n    best_tpr_lr: 0.6869\n    best_condition: N=100_delta=1.6\n    best_auc_mh: 0.9393\n    best_auc_lr: 0.9593\n    pass_criterion_tpr_mh: 0.0416\n    pass_criterion_tpr_lr: 0.0703\n    pass_criterion_condition: N=50_delta=1.0\n    verdict: FAIL\n    all_fpr_below_015: true\n- exp_id: mvp_dif_power_sim_phase2\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    ets_c_tpr_N80_d14: 0.6823\n    ets_c_tpr_N80_d16: 0.7223\n    ets_c_tpr_N100_d14: 0.7582\n    ets_c_tpr_N100_d16: 0.7966\n    ets_c_fpr_range: 0.036-0.042\n    best_auc_mh: 0.9254\n    best_auc_lr: 0.9405\n    verdict: PASS\n    pass_plus_met: true\n    real_param_a_mean: 1.2\n    real_param_b_mean: -0.84\n- exp_id: plan_001_real_data_dif_mmlu\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_ets_c_pct: 31.3\n    temporal_fpr_li_clean: 0.318\n    temporal_enrichment: 0.96\n    ability_ets_c_pct: 2.9\n    ability_fpr_li_clean: 0.027\n    ability_enrichment: 1.19\n    within_family_llama2v3_c_pct: 61.3\n    within_family_mistral_mixtral_c_pct: 38.7\n    domain_spearman_rho: 0.307\n    domain_spearman_p: 0.02\n    sanity_random_split_c_pct: 0.18\n    temporal_ability_jaccard: 0.014\n- exp_id: plan_001b_matched_ability_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics: {}\n- exp_id: plan_011_semi_synthetic_validation\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    temporal_external_tpr_p0: 0.326\n    temporal_external_tpr_p03: 0.548\n    temporal_external_tpr_p05: 0.834\n    temporal_external_tpr_p07: 0.99\n    temporal_external_tpr_p10: 1\n    temporal_external_fpr: 0.314\n    temporal_external_delta_tpr_p10: 0.674\n    ability_external_tpr_p0: 0.498\n    ability_external_tpr_p10: 0.8\n    ability_external_fpr: 0.493\n    ability_external_delta_tpr_p10: 0.302\n    standard_mh_fpr_inflation: temporal 0.298→0.616 at p=1.0\n    matching_variable_contamination_confirmed: true\n    bug_fix: inf-delta classified as extreme DIF not class A\n- exp_id: plan_012_irt_theta_conditioning\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    temporal_theta_qt20_fpr: 0.312\n    temporal_theta_qt20_tpr_p05: 0.876\n    temporal_theta_qt20_tpr_p10: 1\n    temporal_external5_fpr: 0.314\n    temporal_external5_tpr_p05: 0.834\n    ability_theta_qt10_fpr: 0.093\n    ability_theta_qt10_tpr_p05: 0.206\n    ability_theta_qt10_tpr_p10: 0.544\n    ability_theta_qt20_fpr: 0.079\n    ability_theta_qt20_tpr_p05: 0.21\n    ability_theta_qt20_tpr_p10: 0.544\n    ability_external5_fpr: 0.493\n    ability_external5_tpr_p05: 0.756\n    theta_total_score_corr: 0.9986\n    enrichment_all_variants: 0.97-1.00\n    success_criterion_met: false\n- exp_id: plan_013_q3_local_independence\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_subject_mean_q3: 0.0086\n    cross_subject_mean_q3: 0.0031\n    within_subject_pct_above_020: 11.3\n    cross_subject_pct_above_020: 2.2\n    mann_whitney_p: 2.29e-09\n    worst_subject: moral_scenarios\n    worst_subject_pct_above_020: 34.2\n    n_items_retained: 12251\n    n_items_filtered: 257\n    subject_size_q3_corr: 0.2064\n    subject_size_q3_p: 0.123\n- exp_id: plan_014_within_subject_dif\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    business_ethics_within_c_pct: 45.2\n    human_aging_within_c_pct: 33\n    formal_logic_within_c_pct: 39.5\n    professional_medicine_within_c_pct: 31.1\n    high_school_statistics_within_c_pct: 42\n    avg_within_subject_c_pct: 38.1\n    avg_cross_subject_c_pct: 40.5\n    avg_delta_within_vs_cross: -2.4\n    sibtest_available: false\n    r_available: false\n    decision_zone: '>25% HIGH'\n- exp_id: plan_015_bifactor_irt\n  name: ''\n  status: PREPARING\n  conclusion: killed\n  metrics: {}\n- exp_id: plan_016_within_subject_semi_synthetic\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    within_matching:\n      subjects_passing_p05: 3/5 (human_aging, professional_medicine, formal_logic)\n      business_ethics_baseline_fpr: 0.563\n      business_ethics_delta_tpr_p05: -0.078\n      human_aging_baseline_fpr: 0.334\n      human_aging_delta_tpr_p05: 0.385\n      professional_medicine_baseline_fpr: 0.312\n      professional_medicine_delta_tpr_p05: 0.327\n      formal_logic_baseline_fpr: 0.409\n      formal_logic_delta_tpr_p05: 0.457\n      high_school_statistics_baseline_fpr: 0.407\n      high_school_statistics_delta_tpr_p05: 0.194\n      fpr_inflates_with_injection: true\n      avg_fpr_inflation_p10: 0.186\n    cross_matching:\n      subjects_passing_p05: 4/5 (human_aging, professional_medicine, formal_logic,\n        high_school_statistics)\n      business_ethics_baseline_fpr: 0.533\n      business_ethics_delta_tpr_p05: 0.056\n      human_aging_baseline_fpr: 0.431\n      human_aging_delta_tpr_p05: 0.375\n      professional_medicine_baseline_fpr: 0.38\n      professional_medicine_delta_tpr_p05: 0.38\n      formal_logic_baseline_fpr: 0.402\n      formal_logic_delta_tpr_p05: 0.543\n      high_school_statistics_baseline_fpr: 0.335\n      high_school_statistics_delta_tpr_p05: 0.433\n      fpr_stable_across_injection: true\n      delta_fpr_all_subjects: 0\n    success_criterion_met: true\n- exp_id: plan_017_downstream_impact\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    n_dif_items: 3918\n    n_stable_items: 8590\n    dif_pct: 31.3\n    rho_full_vs_stable_2023: 0.998851\n    rho_full_vs_stable_2024: 0.997014\n    rho_full_vs_stable_all: 0.996451\n    shr_full: 0.9934\n    shr_stable: 0.9919\n    dif_vs_random_z_mean: -14.91\n    dif_vs_random_all_21_conditions_significant: true\n    dif_removal_MORE_disruptive_than_random: true\n    cross_cohort_ratio_dif_vs_full: 1.0919\n    cross_cohort_ratio_stable_vs_full: 0.9581\n    top_beneficiaries: phi-3, llama-3 derivatives\n    top_hurt: mistral merges, slerp models\n    max_rank_change: 851\n- exp_id: plan_004_gsm8k_cross_benchmark\n  name: ''\n  status: DONE\n  conclusion: negative\n  metrics:\n    step1_gsm8k_temporal_dif:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      standard_c_pct: 18.9\n      external_c_pct: 47.4\n      sanity_c_pct: 0.3\n      standard_external_spearman: 0.926\n    step2_semi_synthetic:\n      standard_delta_tpr_p10: 0.818\n      external_delta_tpr_p10: 0.517\n    step3_gsm1k_correlation:\n      n_models: 33\n      n_dif_c_items: 249\n      pearson_r: -0.478\n      pearson_p: 0.005\n      spearman_rho: -0.403\n      spearman_p: 0.02\n      partial_r_controlling_accuracy: -0.385\n      partial_p: 0.027\n      permutation_p: 0.014\n      dif_c_favor_2024: 78\n      dif_c_favor_2023: 171\n      direction: NEGATIVE (opposite to contamination hypothesis)\n      cook_d_max_model: Deepseek-math-7b-rl\n      leave_one_out_r_range: -0.537 to -0.374\n      robust: true\n- exp_id: plan_027_temporal_overlap\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    cohort_2023_n: 1080\n    cohort_2023_mean: 0.5814\n    cohort_2023_sd: 0.1405\n    cohort_2024_n: 807\n    cohort_2024_mean: 0.6068\n    cohort_2024_sd: 0.1556\n    cohens_d: -0.173\n    overlap_coefficient: 0.764\n    bhattacharyya: 0.961\n    full_c_pct: 31.3\n    score_range_overlap_c_pct: 30.9\n    nn_matched_c_pct_mean: 28.9\n    nn_matched_c_pct_sd: 0.1\n    nn_matched_n_per_group: 638\n    nn_matched_d: -0.01\n    ability_confound_pp: 2.4\n    ability_confound_pct_of_total: 7.7\n    llama_comparison_d: -0.99\n    llama_comparison_overlap: 0.18\n    llama_matched_c_pct: 28.3\n- exp_id: plan_030_odds_ratio\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    model1_domain_delta:\n      mcfadden_r2: 0.0007\n      nagelkerke_r2: 0.0012\n      aic: 15545.2\n      subject_acc_delta_or: 80.86\n      subject_acc_delta_or_per_010: 1.55\n      subject_acc_delta_or_ci_per_010:\n      - 1.19\n      - 2.03\n    model2_domain_delta_plus_items:\n      mcfadden_r2: 0.0423\n      nagelkerke_r2: 0.072\n      aic: 14902.3\n      subject_acc_delta_or_per_010: 0.73\n      ctt_difficulty_or_per_010: 0.78\n      ctt_discrimination_or_per_010: 1.51\n    model3_item_delta:\n      mcfadden_r2: 0.0012\n      nagelkerke_r2: 0.0021\n      aic: 15536.9\n      item_acc_change_or: 2.11\n      item_acc_change_or_per_010: 1.08\n      item_acc_change_ci:\n      - 1.51\n      - 2.96\n    model4_item_delta_plus_items:\n      mcfadden_r2: 0.0434\n      nagelkerke_r2: 0.0737\n      aic: 14885.4\n      item_acc_change_or_per_010: 0.92\n      ctt_difficulty_or_per_010: 0.77\n      ctt_discrimination_or_per_010: 1.54\n    simpsons_paradox: true\n    lr_test_m1_vs_m2_chi2: 646.98\n    lr_test_m3_vs_m4_chi2: 655.53\n    best_model: Model 4 (item Δ + item props)\n- exp_id: plan_028_multi_bench_dif\n  name: ''\n  status: DONE\n  conclusion: success\n  metrics:\n    mmlu:\n      n_items: 12508\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 31.3\n      random_pct_c: 0.18\n    winogrande:\n      n_items: 1267\n      n_ref: 1017\n      n_foc: 803\n      pct_c: 30.3\n      random_pct_c: 0.32\n    truthfulqa:\n      n_items: 817\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 29.7\n      random_pct_c: 0.37\n    arc:\n      n_items: 1172\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 26.9\n      random_pct_c: 0.6\n    gsm8k:\n      n_items: 1319\n      n_ref: 1017\n      n_foc: 804\n      pct_c: 18.9\n      random_pct_c: 0.3\n    hellaswag:\n      n_items: 10042\n      n_ref: 1080\n      n_foc: 807\n      pct_c: 17.9\n      random_pct_c: 0.28\n    cross_benchmark_range: 17.9-31.3%\n    all_random_controls_below_1pct: true\n    min_enrichment_ratio: 45\n    n_benchmarks: 6\n\n# 输出格式（YAML，仅输出一个 ```yaml 块）\n\n```yaml\ntier: worst\nnarrative_guidance: \"...\"\nimagined_experiments:\n  - name: \"...\"\n    plan_id: \"...\"\n    description: \"...\"\n    expected_results: {metric: value, ...}\n    result_rationale: \"...\"\n    tables: []\n    figures_description: []\n    analysis: \"...\"\n```\n"
}
````

---

### Runtime record

_source line 2 · 2026-05-21T12:44:43.770Z_

```json
{
  "type": "queue-operation",
  "operation": "dequeue",
  "timestamp": "2026-05-21T12:44:43.770Z",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47"
}
```

---

## Round 1

11 recorded events

### User

_source line 3 · 2026-05-21T12:44:43.792Z_

你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：

含义：Permutation null 暴露 temporal structure 显著 inflate DIF，ability confound 比预期严重，reviewer 一致认为贡献不足以达到 EMNLP long paper 门槛 — 需要 reframe 但不降级 venue
核心假设：['plan_029 permutation null C% 在 8–18%：temporal cohort 的 ability gap（虽然 d=-0.17）在 12,508 items × 1,887 models 的规模下产生系统性 DIF inflation，31% 中有相当部分是 ability confound 的 residual artifact', 'NN matching C%=28.9% 被 reviewer 质疑：匹配后 d≈-0.01 但 remaining DIF 可能反映 matching 未覆盖的 latent dimensions（57-subject multidimensionality），不足以排除 confound', "至少两位 reviewer 给 borderline reject，核心理由：(1) no methodological contribution, (2) 31% 可能 inflated, (3) 'diagnostic lens' 是 post-hoc reframing", '6 benchmark 中 HellaSwag（17.9%）和 GSM8K（18.9%）明显低于 MMLU（31.3%），reviewer 质疑 benchmark 间差异是否反映方法 artifact 而非真实 instability 差异', "Simpson's paradox + negative GSM1K correlation 被 reviewer 解读为 DIF 实际上在 capture ability improvement 而非 item-level instability"]
关键指标范围：{'permutation_null_c_pct': [8.0, 18.0], 'residual_c_pct_after_all_controls': [15.0, 23.0], 'ability_confound_explained_pp': [6.0, 12.0], 'cross_benchmark_c_range_pct': [12.0, 32.0], 'semi_synthetic_delta_tpr_p05': [0.25, 0.4], 'cross_subject_delta_fpr': [0.005, 0.02], 'ranking_stability_rho': [0.99, 0.996], 'simulated_avg_reviewer_score': [1.5, 2.5], 'page_count_main_body': [8.5, 9.5]}
叙事方向：核心 reframe：从 'DIF reveals 31% instability' 转向 'Permutation-calibrated DIF reveals 15–23% genuine item-level instability after accounting for temporal ability structure — still 2–3× above null, and the methodology for separating genuine DIF from ability artifact is itself a contribution.' Paper 重心从 Claim 1 的 headline number 转移到三个方向：(1) Semi-synthetic validation framework（Claim 3）升格为 primary contribution — ΔFPR=0 的 cross-subject matching 是 genuine methodological insight，独立于 instability magnitude；(2) Multi-benchmark temporal DIF atlas（6 benchmarks × permutation-calibrated）作为 empirical resource contribution；(3) Permutation null 本身成为 finding — 'temporal cohort structure inflates naive DIF by X pp, establishing calibration requirements for future LLM DIF studies.' Meta-critique（Claim 2）保留但从 aggressive 改为 measured。Diagnostic lens 保留但弱化 claim 强度。Abstract 不再领 31%，改领 'permutation-calibrated genuine instability rate' + 'semi-synthetic validation framework with provable FPR control.' 仍冲 EMNLP long paper，但需要 camera-ready 前补充 propensity-score matching 或 MIMIC model 作为 additional robustness。

基于以上定义，对 experiment_plan 中每个 planned 实验展开详细数据。
每条预测都必须给出 result_rationale —— 解释为什么在这个档位下会得到这样的结果。

# Project context
project: irt_equated_bench_regen
venue: emnlp-2026

## paper_framing.md

# Paper Framing — irt_equated_bench_regen

## Target Venue
- Primary: EMNLP 2026 (via ARR; long paper 8-page limit + unlimited refs)
- Page limit: 8 pages main text (当前 10 页，需压缩 2 页)

## Paper Type
Empirical analysis / psychometric characterization. Discovery paper, not methods paper. "DIF reveals benchmark structural problems," not "DIF detects contamination."

## Core Claims (4 条, 可证伪)

**Claim 1 (Temporal Comparability Concern)**: ~31% of MMLU items are functionally unstable across model generations — they exhibit large DIF (ETS C, |Δ_MH|≥1.5) between 2023 and 2024-H1 model cohorts. Primary estimate: **31.3%** (temporal cohort, plan_001). All 57 subjects show instability (C% range 20.7–48.4%, unweighted mean ≈30%, plan_001 domain_specificity.csv). Within-subject matching on 5 high-C% subjects yields higher rates (31-45%, avg 38.1%, plan_014) — report as robustness check, not primary. This instability is not a statistical artifact (random split sanity check: 0.18%), and correlates weakly with domain-specific accuracy improvement (ρ=0.307, p=0.02), but item-level decomposition shows domain improvement explains only 2.4pp (7.6%). Architecture heterogeneity is a non-issue: METABENCH MMLU is 99.98% decoder-only (5226/5227), excluding the 1 non-decoder model changes nothing (Jaccard=1.0). Threshold sensitivity robustness confirmed: C% ranges from 48.9% (|Δ_MH|≥1.0) to 18.3% (|Δ_MH|≥2.0) to 10.2% (|Δ_MH|≥2.5). BH FDR correction at q=0.05 has negligible impact (removes 3/3,918 items).
- Evidence: plan_001 (C%=31.3%), plan_014 (within-subject C%=38.1%), plan_010 (arch-stratified: 99.98% decoder-only, C% unchanged, Jaccard=1.0), plan_018 (threshold: 49/31/18/10% at 1.0/1.5/2.0/2.5; BH negligible), plan_019 (decomposition: ≤2.4pp/7.6% explained by domain improvement), plan_022 (model independence: graduated de-duplication to 1 model per family → C% ≤ random subsample control at every cap K; K=20: 29.1% vs random 30.9%, K=5: 11.7% vs random 16.9%; family structure does NOT inflate C%), plan_027 (temporal ability overlap: d=-0.17, OVL=76.4%; 1:1 NN matching C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp; contrast with Llama-2v3 d=-0.99→matched C%=28.3%, where ability confound explains 33pp)
- Honesty requirement: ρ=0.307 (p=0.02) at subject level reflects a modest ecological correlation. Item-level decomposition (plan_019) shows domain improvement accounts for at most 2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific. Caveat: item difficulty may be a mediator rather than confounder — use Model 1 as primary; Model 2 (Simpson's paradox) as supplementary.
- IRT fit: 98% of models show |Lz|>2, reflecting MMLU's inherent multidimensionality (57 subjects), not architecture heterogeneity. 1D IRT is fundamentally misspecified for MMLU — discuss in limitations as motivation for future multidimensional IRT work.

**Claim 2 (Ground Truth Meta-critique)**: Existing contamination detection literature validates against web-overlap/n-gram labels that measure global exposure (whether an item is publicly accessible), not differential contamination (whether an item functions differently across model cohorts). DIF enrichment≈1.0 against Li et al. labels is expected, not failure — these labels cannot evaluate item-level differential detectors. This is a fundamental validation methodology gap: all work using web-overlap labels as ground truth for item-level detectors (including Min-K%, n-gram methods) has the same blind spot. **Empirically validated** (plan_026): direct comparison of DIF-C flags vs Li et al. web-overlap labels on 9,229 MMLU items shows enrichment=0.964, Jaccard=0.206, Phi=0.012, χ²=1.28 (p=0.258), OR=1.05 [0.96, 1.15]. Consistent across subtypes (input_only: 0.986, input_and_label: 0.960). Semi-synthetic injection confirms DIF can detect differential contamination (ΔTPR=+0.508 at p=0.5, dose-response from p=0.3 to p=1.0).
- Evidence: plan_001 (enrichment=0.96), plan_026 (direct comparison: enrichment=0.964, Jaccard=0.206, p=0.258), plan_011 (ΔTPR=+0.508, dose-response)
- Framing: aggressive — "the field's standard validation approach is fundamentally mismatched for item-level detection" — now with direct empirical evidence, not just conceptual argument

**Claim 3 (Semi-synthetic Validation Framework)**: The ΔTPR methodology — injecting known differential contamination into real response matrices and measuring detection power increase — provides a controlled validation infrastructure for any item-level contamination detector. Cross-subject matching (using total score on OTHER subjects as MH matching variable) eliminates FPR inflation (ΔFPR=0.000 across all 5 tested subjects), while within-subject matching suffers from matching variable contamination (FPR inflation +0.186).
- Evidence: plan_011, plan_016 (ΔFPR=0.000 cross-subject, 4/5 subjects ΔTPR>0.3), plan_004 Step 2 (GSM8K ΔTPR=+0.818 standard, +0.517 external)
- Cross-benchmark: GSM8K replication confirms framework portability to single-domain math benchmarks
- Positioning: cross-subject matching is a practical methodological recommendation; cross-benchmark replication strengthens generalizability

**Claim 4 (Downstream Impact — Four-Layer Finding)**: DIF as diagnostic lens, not quality filter. Four sub-findings:
1. **Benchmark redundancy**: ρ≈0.997 between full and stable-only rankings — MMLU rankings are extremely robust to 31% item removal, revealing massive measurement redundancy in the benchmark.
2. **DIF items carry cross-cohort signal but are NOT the most ranking-defining items**: DIF removal causes MORE disruption than random removal (z=-8 to -49σ, 21/21 conditions), confirming DIF items are non-trivial. But circularity ablation (plan_020) shows DIF is the LEAST disruptive non-random strategy: accuracy-gap removal disrupts 10-16× more (z=-157 vs -9.5), high-variance 11× more (z=-108), high-discrimination 1.7× more (z=-16). MH's ability conditioning filters out raw accuracy differences, isolating genuine differential functioning rather than generally informative items. DIF-discrimination overlap is only 22.1% (Jaccard=0.12) — DIF identifies "items that changed across generations," not "good items."
3. **DIF as diagnostic lens**: DIF identifies which items' functioning changes most across model generations → reveals which capability dimensions drive ranking shifts. Not "find bad items and remove" but "understand what changed and why." Model-specific patterns: phi-3/llama-3 gain +700-850 ranks from DIF items, mistral merges lose -400 to -587. **Item characterization** (plan_023): DIF-C items are moderately harder (Cohen's d=-0.247) and higher-discrimination (d=0.230) than non-DIF items, but uniformly distributed across MMLU domains (χ² p=0.32). Key finding: difficulty × DIF direction interaction (ρ=-0.597) — hardest-decile DIF-C items are 88.7% focal-favoring (2024 models do better), easiest-decile are 96.2% reference-favoring (2023 models do better). This reveals a systematic pattern: capability improvement concentrates on hard items, while easy items' difficulty structure erodes across generations.
4. **Cross-benchmark validation (exploratory)**: On GSM8K (1,319 items × 6,702 models), DIF flags anti-correlate with GSM1K contamination gap (r=−0.478, p=0.005, N=33). **DEMOTED to exploratory** per Dream #6 three-tier consensus: N=33, CI wide [−0.71, −0.16], not strong enough for numbered contribution. This evidence is suggestive but should NOT appear in abstract/conclusion as core support.
- Evidence: plan_017 (z=-8 to -49σ, ρ=0.996-0.999), plan_020 (circularity ablation: DIF z=-9.5 vs acc-gap z=-157, disc z=-16, var z=-108), plan_023 (item characterization: difficulty ρ=-0.597, domain uniformity χ² p=0.32)
- Architecture: plan_017 is load-bearing (strong, full N=5,227). plan_020 circularity ablation is the second pillar. GSM1K correlation (plan_004 Step 3) is supplementary/exploratory only.
- Growing Pains互补: "Growing Pains uses anchor items for efficient evaluation; our DIF diagnostic tells them which anchor items are degrading"
- Caveats (→ limitations): N=33, Pearson CI upper bound |r|=0.155 (small effect possible), Spearman CI upper bound |ρ|=0.031 (near zero possible); item difficulty confound not fully excluded (DIF-C items harder for all models); contamination gap is proxy, not ground truth; replication with larger matched sample needed

## Story Spine (v2 — no-pivot narrative)

**Opening frame**: LLM benchmarks implicitly assume temporal score comparability — when we say "Model B outperforms Model A on MMLU," we presume both scores reflect the same latent construct. But do they? Psychometrics has a mature tool for testing exactly this: Differential Item Functioning (DIF) analysis detects items whose difficulty changes across examinee groups after controlling for overall ability. We apply MH-DIF to the METABENCH response matrix (5,227 models × 12,508 MMLU items) — the largest-scale DIF analysis on LLM benchmarks to date.

**Key narrative principle**: "Instability ≠ invalidity." DIF flags items whose functioning changed across generations — this is a diagnostic signal, not a quality verdict. MMLU rankings are massively redundant (ρ≈0.997 after removing 31% of items), so instability doesn't threaten validity. But it reveals WHICH capability dimensions are shifting. **This framing must appear in the Introduction, not be deferred to Discussion.**

**What we find** (4 contributions, focused):

1. **31% of MMLU items are functionally unstable** across model generations (ETS C, |Δ_MH|≥1.5). Robust to threshold choice (49%/31%/18%/10% at 1.0/1.5/2.0/2.5), multiple testing (BH removes 3/3918 items), and architecture composition (99.98% decoder-only). Domain accuracy improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). The instability is predominantly item-specific, not a proxy for "models got better."

2. **Ground truth meta-critique**: Web-overlap contamination labels measure global exposure, not differential contamination. Enrichment≈1.0 is expected. Semi-synthetic injection confirms DIF detects differential contamination (ΔTPR=+0.508). Any item-level detector validated against web-overlap labels has this blind spot.

3. **Semi-synthetic validation framework**: ΔTPR methodology with cross-subject matching (ΔFPR=0.000). Portable across benchmarks (GSM8K ΔTPR=+0.818). Reusable for validating any item-level contamination detector.

4. **DIF as diagnostic lens + actionable protocol**: DIF items carry cross-cohort signal (z=-8 to -49σ vs random) but are the LEAST disruptive non-random strategy (z=-9.5 vs accuracy-gap z=-157). DIF isolates genuine differential functioning, not just informative items. **Actionable contribution**: DIF audit protocol for benchmark maintainers (monitoring frequency, decision rules, response options).

**Headline result**: "Psychometric DIF analysis of 5,227 models × 12,508 MMLU items reveals 31% temporal instability — robust across thresholds, not driven by capability improvement (≤7.6%), and not a validity threat (ρ≈0.997 ranking stability). The field's web-overlap ground truth cannot capture this differential signal; we provide a semi-synthetic validation framework with cross-subject matching (ΔFPR=0.000). DIF serves as a diagnostic lens for understanding what changed across model generations, with a concrete audit protocol for benchmark maintenance."

## Scope Control (main body vs appendix)

**MAIN BODY (4 claims + robustness)**:
- §1 Introduction (problem + "instability ≠ invalidity" framing upfront)
- §2 Related Work (45 papers, 5 clusters)
- §3 Method (MH-DIF primer, semi-synthetic framework, cross-subject matching)
- §4 Experiments: Claim 1 (temporal DIF + threshold + BH + decomposition + architecture), Claim 2 (enrichment + meta-critique), Claim 3 (semi-synthetic + cross-benchmark), Claim 4 (redundancy + circularity ablation + diagnostic lens + GSM1K validation)
- §5 Discussion + Limitations
- §6 Conclusion

**APPENDIX (pruned from main body)**:
- Bayesian cumulative DIF (plan_007) — simulation-only, underdeveloped
- RL robustness (plan_002) — N=13, underpowered
- Ensemble fusion (plan_003a/b/c) — negative, not executed
- Bifactor equating pilot — below target fit
- Item generation pilot — below benchmarks
- Graceful degradation — clean but supplementary
- Item-Focused Trees — robustness check, supplementary
- ConStat/DVD comparisons — complementary baselines

## Empirical Observation: Structural Constraints on DIF in LLM Benchmarks

Systematic experimentation reveals that three structural improvements — matched-ability cohort design (plan_001b), IRT θ-conditioning (plan_012, r=0.9986), and bifactor pre-check (plan_014, within-subject C%=38.1%) — all fail to reduce temporal DIF baseline FPR below 31% while maintaining detection power. This is an empirical observation, not a formal impossibility result. The constraints arise from: (a) unidimensional IRT limitations in modeling 57-subject multidimensional ability, (b) statistical power requirements (N≥80, δ≥1.4), and (c) inability to separate ability confounding from genuine item-level changes. Higher-level methods (MIMIC, propensity-score matching, multidimensional IRT) may address individual constraints — future work.

## Venue Fit

- **EMNLP 2026**: Strong fit — NLP evaluation methodology is a dedicated area, reviewers expect empirical studies of benchmarks. "Empirical, not algorithmic" contribution type well-received. Risk: 8-page limit requires significant compression (current 10 pages). Mitigation: move structural analysis details to appendix.

## Novelty Articulation (三层，显式化)

MH-DIF (1959/1988) is applied without modification. **Explicitly acknowledge this.** Novelty is NOT algorithmic. Three layers of genuine contribution:

1. **Empirical discovery at unprecedented scale**: First DIF analysis on 5,227×12,508 LLM response matrix. Finding: 31% temporal instability is robust across thresholds (10-49%), not explained by capability improvement (≤7.6%), and architecturally homogeneous (99.98% decoder-only). No prior work has characterized item-level stability of LLM benchmarks at this scale. The instability finding itself is new data about MMLU's measurement properties.

2. **Ground truth meta-critique with field-wide implications**: The observation that web-overlap labels cannot validate item-level differential detectors is NOT obvious — the field routinely uses them. This affects the validity claims of Min-K%, ConStat, n-gram methods, and all papers using web-overlap as ground truth. First empirical demonstration (enrichment≈1.0 + semi-synthetic proof).

3. **Semi-synthetic validation framework + cross-subject matching**: The ΔTPR methodology is a reusable infrastructure contribution. Cross-subject matching (ΔFPR=0.000) is a novel practical innovation — the insight that within-subject matching contaminates the conditioning variable is subtle and general. Portable to any multi-domain benchmark (demonstrated on GSM8K).

**Framing**: "We bring mature psychometric tools to characterize an urgent ML evaluation problem. The contribution is the empirical findings, the validation methodology critique, and the reusable framework — not a new algorithm."

## Anticipated Reviewer Concerns (updated for pivot)

1. **"31% could just mean models got better / ability confound inflates C%"** — ✅ RESOLVED (plan_019 + plan_027). Item-level decomposition shows domain improvement explains ≤2.4pp of 31.3% C% (7.6%; pseudo R²=0.0007). Temporal cohort ability gap is negligible (d=-0.17, OVL=76.4%); 1:1 NN matching (d≈-0.01) yields C%=28.9%±0.1% vs full 31.3% — ability confound explains only 2.4pp. Contrast: Llama-2v3 (d=-0.99) drops from 61.3% to 28.3% under matching. Both converge to ~28-29% genuine item-level DIF.

2. **"Ground truth critique is obvious — of course web labels don't capture differential effects"** — Not obvious: the field routinely uses these labels for item-level validation. We provide the first empirical demonstration with both the enrichment≈1.0 result and the semi-synthetic proof of concept.

3. **"Semi-synthetic injection is artificial"** — We inject into real response matrices (not simulated), preserving real ability distributions and item characteristics. The mechanism (incorrect→correct flipping) is a simplification acknowledged in limitations.

4. **"DIF power is only sufficient for large effects"** — Large effects are precisely what threaten benchmark validity most. Operational region: N≥80, δ≥1.4, TPR=0.68-0.80.

5. **"Only validated on MMLU"** — Partially addressed: GSM8K replication (METABENCH 1,319 items × 6,702 models) confirms semi-synthetic framework portability (ΔTPR=+0.818) and temporal DIF pattern (C%=18.9%). **plan_028 in progress**: checking METABENCH for ARC/HellaSwag/WinoGrande/TruthfulQA response matrices to run multi-benchmark temporal DIF. Full generalization to diverse benchmarks remains future work if METABENCH lacks other benchmarks.

6. **"Higher methods (MIMIC, propensity-score) could solve the confounding"** — Acknowledged as future work. We frame our three-attempt negative results as "empirical observation" that motivates these directions, not as impossibility.

7. **"ETS threshold is uncalibrated for LLM populations"** — ✅ RESOLVED (plan_018). C% at {1.0, 1.5, 2.0, 2.5} = {48.9%, 31.3%, 18.3%, 10.2%}. Finding >15% holds at standard thresholds [1.0, 2.0]. At conservative 2.5, still 10.2% (1,278 items). Present as: "finding is robust across standard thresholds; even at the most conservative cutoff, >10% of items show large DIF." Do NOT claim ">15% at all thresholds" — be honest that 2.5 drops below.

8. **"Multiple testing: 12,508 simultaneous tests without correction"** — ✅ RESOLVED (plan_018). BH FDR correction at q=0.05 removes only 3/3,918 ETS C items (31.32%→31.30%). At higher thresholds, BH impact is zero. ETS dual requirement (effect size + significance) provides near-complete implicit protection. Random-split sanity check (C%=0.18%) confirms empirically.

9. **"Only uniform DIF — non-uniform DIF plausible for LLMs"** — ✅ RESOLVED (plan_021). LR-DIF on 9 subjects (1787 items): MH C-class 92.1% concordance with LR uniform DIF → MH detection robust. Non-uniform DIF: 38.7% at significance threshold, **24.8% at |β_interaction|≥0.5** (conservative, effect-size controlled). MH structurally underestimates instability. Caveat: LR used within-subject matching (vs MH's cross-benchmark), so 38.7% may be inflated; use 24.8% in paper. Framing: "our 31% uniform-only estimate is conservative."

10. **"5,227 models are not independent — fine-tunes/merges inflate N and DIF significance"** — ✅ RESOLVED (plan_022). Graduated de-duplication (capping models per family at K=1,2,5,10,20) shows C% ≤ random subsample control at every cap: K=20 (447 models) C%=29.1% vs random 30.9%; K=5 (146 models) C%=11.7% vs random 16.9%; K=1 (33 families) C%=0.17% (underpowered, N<80). Family structure does NOT inflate C% — if anything, de-duplication reduces it slightly less than random subsampling. The 31.3% figure is robust to model non-independence.

11. **"Ranking disruption result is tautological"** — ✅ RESOLVED (plan_020). Circularity ablation shows DIF removal is the LEAST disruptive non-random strategy: z=-9.5 vs accuracy-gap z=-157, discrimination z=-16, variance z=-108. Despite 62.6% item overlap with accuracy-gap selection, MH ability conditioning makes DIF 10-16× less disruptive. DIF isolates genuine differential functioning, not just items with large raw group differences. Tautology refuted.

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
- id: plan_028
  name: multi_benchmark_temporal_dif
  claim: 1,5
  description: 'Check METABENCH for additional benchmark response matrices (ARC-Challenge,
    HellaSwag, WinoGrande, TruthfulQA, MMLU-Pro) and run temporal DIF analysis (2023
    vs 2024) on each. Addresses Dream #6 three-tier consensus: "only MMLU + GSM8K,
    generalizability insufficient." Report C% + sample sizes + random-split control
    for each benchmark.

    '
  priority: P0
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_029
  name: permutation_null_c_rate
  claim: 1
  description: '1000× permutation test: randomly reassign 2023/2024 temporal labels
    (preserving group sizes N_ref=1080, N_foc=807) and run MH-DIF each time. Establishes
    null distribution for C%. Dream #6 three-tier consensus: reviewers ask "is 31%
    above chance?" Current random-split control (0.18%) is within-cohort, not temporal
    permutation null.

    '
  priority: P1
  gpu_budget_hours: 0
  deps:
  - plan_001
  registry_id: ''
  status: planned
- id: plan_030
  name: odds_ratio_regression_transparency
  claim: 1
  description: 'Supplement pseudo R²=0.0007 with odds ratio + 95% CI + McFadden/Nagelkerke
    R² + deviance ratio. Add finer-grained model: item-level DIF flag ~ item-level
    accuracy change (per-item 2024-2023 accuracy delta) vs current domain-level predictor.
    Dream #6 two-tier concern.

    '
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
- exp_id: plan_027_temporal_overlap
  name: ''
  status: DONE
  conclusion: success
  metrics:
    cohort_2023_n: 1080
    cohort_2023_mean: 0.5814
    cohort_2023_sd: 0.1405
    cohort_2024_n: 807
    cohort_2024_mean: 0.6068
    cohort_2024_sd: 0.1556
    cohens_d: -0.173
    overlap_coefficient: 0.764
    bhattacharyya: 0.961
    full_c_pct: 31.3
    score_range_overlap_c_pct: 30.9
    nn_matched_c_pct_mean: 28.9
    nn_matched_c_pct_sd: 0.1
    nn_matched_n_per_group: 638
    nn_matched_d: -0.01
    ability_confound_pp: 2.4
    ability_confound_pct_of_total: 7.7
    llama_comparison_d: -0.99
    llama_comparison_overlap: 0.18
    llama_matched_c_pct: 28.3
- exp_id: plan_030_odds_ratio
  name: ''
  status: DONE
  conclusion: success
  metrics:
    model1_domain_delta:
      mcfadden_r2: 0.0007
      nagelkerke_r2: 0.0012
      aic: 15545.2
      subject_acc_delta_or: 80.86
      subject_acc_delta_or_per_010: 1.55
      subject_acc_delta_or_ci_per_010:
      - 1.19
      - 2.03
    model2_domain_delta_plus_items:
      mcfadden_r2: 0.0423
      nagelkerke_r2: 0.072
      aic: 14902.3
      subject_acc_delta_or_per_010: 0.73
      ctt_difficulty_or_per_010: 0.78
      ctt_discrimination_or_per_010: 1.51
    model3_item_delta:
      mcfadden_r2: 0.0012
      nagelkerke_r2: 0.0021
      aic: 15536.9
      item_acc_change_or: 2.11
      item_acc_change_or_per_010: 1.08
      item_acc_change_ci:
      - 1.51
      - 2.96
    model4_item_delta_plus_items:
      mcfadden_r2: 0.0434
      nagelkerke_r2: 0.0737
      aic: 14885.4
      item_acc_change_or_per_010: 0.92
      ctt_difficulty_or_per_010: 0.77
      ctt_discrimination_or_per_010: 1.54
    simpsons_paradox: true
    lr_test_m1_vs_m2_chi2: 646.98
    lr_test_m3_vs_m4_chi2: 655.53
    best_model: Model 4 (item Δ + item props)
- exp_id: plan_028_multi_bench_dif
  name: ''
  status: DONE
  conclusion: success
  metrics:
    mmlu:
      n_items: 12508
      n_ref: 1080
      n_foc: 807
      pct_c: 31.3
      random_pct_c: 0.18
    winogrande:
      n_items: 1267
      n_ref: 1017
      n_foc: 803
      pct_c: 30.3
      random_pct_c: 0.32
    truthfulqa:
      n_items: 817
      n_ref: 1080
      n_foc: 807
      pct_c: 29.7
      random_pct_c: 0.37
    arc:
      n_items: 1172
      n_ref: 1080
      n_foc: 807
      pct_c: 26.9
      random_pct_c: 0.6
    gsm8k:
      n_items: 1319
      n_ref: 1017
      n_foc: 804
      pct_c: 18.9
      random_pct_c: 0.3
    hellaswag:
      n_items: 10042
      n_ref: 1080
      n_foc: 807
      pct_c: 17.9
      random_pct_c: 0.28
    cross_benchmark_range: 17.9-31.3%
    all_random_controls_below_1pct: true
    min_enrichment_ratio: 45
    n_benchmarks: 6

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
  "promptId": "3e1d1047-4509-4576-9306-e616e5268cc6",
  "type": "user",
  "uuid": "839c7c12-63ca-4e6e-b4fc-56b7ede15dc6",
  "permissionMode": "bypassPermissions",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

</details>

---

### Runtime record

_source line 4 · 2026-05-21T12:44:43.790Z_

```json
{
  "parentUuid": "839c7c12-63ca-4e6e-b4fc-56b7ede15dc6",
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
  "uuid": "dd885415-04a8-473d-8652-94daef7b465a",
  "timestamp": "2026-05-21T12:44:43.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47",
  "version": "2.1.126",
  "gitBranch": "HEAD"
}
```

---

### Runtime record

_source line 5 · 2026-05-21T12:44:43.790Z_

```json
{
  "parentUuid": "dd885415-04a8-473d-8652-94daef7b465a",
  "isSidechain": false,
  "attachment": {
    "type": "skill_listing",
    "content": "- update-config: Use this skill to configure the Claude Code harness via settings.json. Automated behaviors (\"from now on when X\", \"each time X\", \"whenever X\", \"before/after X\") require hooks configured in settings.json - the harness executes these, not Claude, so memory/preferences cannot fulfill them. Also use for: permissions (\"allow X\", \"add permission\", \"move permission to\"), env vars (\"set X=Y\"), hook troubleshooting, or any changes to settings.json/settings.local.json files. Examples: \"allow npm commands\", \"add bq permission to global settings\", \"move permission to user settings\", \"set DEBUG=true\", \"when claude stops show X\". For simple settings like theme/model, suggest the /config command.\n- keybindings-help: Use when the user wants to customize keyboard shortcuts, rebind keys, add chord bindings, or modify ~/.claude/keybindings.json. Examples: \"rebind ctrl+s\", \"add a chord shortcut\", \"change the submit key\", \"customize keybindings\".\n- simplify: Review changed code for reuse, quality, and efficiency, then fix any issues found.\n- fewer-permission-prompts: Scan your transcripts for common read-only Bash and MCP tool calls, then add a prioritized allowlist to project .claude/settings.json to reduce permission prompts.\n- loop: Run a prompt or slash command on a recurring interval (e.g. /loop 5m /foo). Omit the interval to let the model self-pace. - When the user wants to set up a recurring task, poll for status, or run something repeatedly on an interval (e.g. \"check the deploy every 5 minutes\", \"keep running /babysit-prs\"). Do NOT invoke for one-off tasks.\n- schedule: Create, update, list, or run scheduled remote agents (routines) that execute on a cron schedule. - When the user wants to schedule a recurring remote agent, set up automated tasks, create a cron job for Claude Code, or manage their scheduled agents/routines. Also use when the user wants a one-time scheduled run (\"run this once at 3pm\", \"remind me to check X tomorrow\").\n- claude-api: Build, debug, and optimize Claude API / Anthropic SDK apps. Apps built with this skill should include prompt caching. Also handles migrating existing Claude API code between Claude model versions (4.5 → 4.6, 4.6 → 4.7, retired-model replacements).\nTRIGGER when: code imports `anthropic`/`@anthropic-ai/sdk`; user asks for the Claude API, Anthropic SDK, or Managed Agents; user adds/modifies/tunes a Claude feature (caching, thinking, compaction, tool use, batch, files, citations, memory) or model (Opus/Sonnet/Haiku) in a file; questions about prompt caching / cache hit rate in an Anthropic SDK project.\nSKIP: file imports `openai`/other-provider SDK, filename like `*-openai.py`/`*-generic.py`, provider-neutral code, general programming/ML.\n- init: Initialize a new CLAUDE.md file with codebase documentation\n- review: Review a pull request\n- security-review: Complete a security review of the pending changes on the current branch",
    "skillCount": 10,
    "isInitial": true
  },
  "type": "attachment",
  "uuid": "951de100-d2df-4520-86f5-26d8f26ca3b8",
  "timestamp": "2026-05-21T12:44:43.790Z",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47",
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Permutation null 暴露 temporal structure 显著 inflate DIF，ability confound 比预期严重，reviewer 一致认为贡献不足以达到 EMNLP long paper 门槛 — 需要 reframe 但不降级 venue 核心假设：['plan_…",
  "leafUuid": "951de100-d2df-4520-86f5-26d8f26ca3b8",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47"
}
```

---

### Runtime record

_source line 7_

```json
{
  "type": "ai-title",
  "aiTitle": "Permutation-calibrated DIF reveals genuine LLM benchmark instability",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47"
}
```

---

### Assistant

_source line 8 · 2026-05-21T12:45:38.143Z_

<details><summary>Logged reasoning block</summary>

```text
The user wants me to generate detailed predicted experimental results for the "worst" tier scenario for each planned experiment in their experiment_plan. Let me carefully analyze each planned experiment and predict what would happen under the worst-case scenario they've defined.

The worst tier is defined as:
- Permutation null exposes temporal structure that significantly inflates DIF
- Ability confound is worse than expected
- Reviewers consistently find contributions insufficient for EMNLP long paper
- Need to reframe but not downgrade venue

Key metric ranges for worst tier:
- permutation_null_c_pct: [8.0, 18.0]


- residual_c_pct_after_all_controls: [15.0, 23.0]
- ability_confound_explained_pp: [6.0, 12.0]
- cross_benchmark_c_range_pct: [12.0, 32.0]
- semi_synthetic_delta_tpr_p05: [0.25, 0.4]
- cross_subject_delta_fpr: [0.005, 0.02]
- ranking_stability_rho: [0.99, 0.996]
- simulated_avg_reviewer_score: [1.5, 2.5]
- page_count

Now I'm looking at the expected metric ranges for the worst-case scenario across all experiments, which show how much the results could degrade if the confounds and methodological issues manifest as expected.

Looking through the planned experiments, I need to distinguish between what's actually still pending versus what's already been completed in the registry. Several of these have already been executed—plan_001 and plan_004 are done—while others like the robustness validation, perturbation evaluation, and ensemble fusion work are still in progress. Plan_005 was originally planned but got cancelled, so I should skip that one. in the experiment_plan under the "worst" scenario. Even though some are already done with actual results, the "worst" tier imagining would predict what happens when things go badly.

So I need to go through each of the thirteen experiments listed and imagine worst-case outcomes for all of them, treating even the completed ones as hypothetical failures to understand the lower bounds of performance.

For the worst tier, the pattern is clear: permutation null C% sits at 8-18%, suggesting temporal artifacts account for a substantial chunk of the observed 31%; residual C% after controlling for everything drops to just 15-23%; ability confounds are much larger than currently estimated at 6-12 percentage points rather than 2.4; semi-synthetic ΔTPR collapses from 0.834 down to 0.25-0.4 at p=0.5; and cross-subject ΔFPR stays minimal around 0.005.

02 but not the clean zero I've been assuming. Ranking stability degrades slightly to 0.99-0.996, and simulated reviewer scores land in the 1.5-2.5 range—borderline reject territory.

Now I'm working through the specific predictions for each experiment. For plan_001 with real data MMLU, the 31% temporal C% persists as a headline number, but the permutation null will later reveal much of this is inflated by temporal structure. The enrichment with Li et al. labels stays around 1.0, though domain correlation might be stronger than expected due to ability confounds. Within-family Llama2v3 comparisons show very high C%, pointing to ability confound effects, so the 31% figure holds but becomes less meaningful once permutation testing is applied.

For plan_002 on RL robustness, I'm working with only 10-15 reasoning-RL models—N=13 is underpowered. DIF retention degrades when RL models enter the cohort, traditional detectors show expected degradation on RL models, but with such a small sample the comparison lacks conviction. The TOST equivalence test comes back inconclusive and bootstrap confidence intervals are too wide to be informative.

For plan_003a on ConStat perturbation evaluation, the GPU requirement for paraphrasing is a constraint. ConStat shows decent detection power on non-RL models under worst case, but comparing it to DIF is unfavorable—they detect different items with low overlap, weakening the ensemble argument.

For plan_003b on DVD generation variance, the GPU intensity continues to be a limiting factor, and under worst case DVD shows low detection power for verbatim contamination since it's designed for variants, while the generation variance signal itself is noisy with high false positive rates.

Plan_003c on ensemble fusion depends on both upstream signals succeeding, so if either 003a or 003b fails, the ensemble either collapses to DIF-only or doesn't materialize at all.

For plan_004 on cross-benchmark GSM8K evaluation, the negative correlation of r=-0.478 risks being misinterpreted by reviewers as DIF capturing ability improvement rather than instability, and the contamination percentage of 18.9% is lower than MMLU, suggesting benchmark-specific effects. Semi-synthetic approaches work but with reduced ΔTPR gains.

For plan_005 on bifactor IRT equating, the bifactor model either fails to converge with 57 subjects or produces poor fit, and this plan was already effectively killed per the registry.

Plan_006 on item generation calibration is downstream of plan_005, so if bifactor fails, calibration becomes impossible or unreliable.

Plan_007 on cumulative Bayesian DIF is simulation-only, and reviewers might dismiss the power improvements as incremental rather than novel.

Plan_008 on graceful degradation analysis risks showing faster degradation than expected, which would undermine the redundancy narrative.

Plan_009 on item-focused trees could reveal that DIF emerges gradually rather than sharply at cohort boundaries, challenging the discrete cohort framing.

Plan_010 on architecture-stratified DIF faces the problem that decoder-only models comprise 99.98% of the architecture, making this essentially a non-experiment where removing one model changes nothing.

Plan_011 on semi-synthetic contamination validation shows worst-case ΔTPR dropping to 0.25-0.4 with significant FPR inflation, confirming within-subject contamination but revealing non-zero cross-subject ΔFPR.

Plan_028 on multi-benchmark temporal DIF could show wide cross-benchmark variation (12-32%), with HellaSwag and GSM8K performing poorly, raising questions about whether differences reflect method artifacts or benchmark-specific effects.

The permutation null experiment is crucial—if C% sits at 8-18% under worst case, temporal structure alone accounts for substantial DIF, deflating the 31% headline by that margin. Plan_030's odds ratio regression adds nuance through Simpson's paradox and negative GSM8K correlation, though reviewers may interpret it unfavorably.

Now I'm writing the full YAML configuration...
```

</details>

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "951de100-d2df-4520-86f5-26d8f26ca3b8",
  "isSidechain": false,
  "requestId": "req_011CbFjceZ8DsAtNE5QYm6N9",
  "type": "assistant",
  "uuid": "aa05c34c-7d45-4221-b324-12ecbc220965",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XM7RhgcgnTaxVKmeD29VfL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21090,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16706,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16706,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21090
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

_source line 9 · 2026-05-21T12:50:18.057Z_

```yaml
tier: worst
narrative_guidance: >
  Permutation null 暴露 temporal cohort structure 对 MH-DIF 的系统性 inflation：1000× permutation 产生 C%=8–18%
  的 null baseline，将 31.3% headline 拉低至 15–23% genuine item-level instability。Ability confound
  比 plan_027 的 2.4pp 估计严重——NN matching 未覆盖的 latent dimensions（57-subject multidimensionality）
  留下 6–12pp residual。Reviewer 共识：(1) no methodological contribution（MH 1988 直接套用），
  (2) 31% inflated 且 permutation-calibrated number 不够 dramatic，(3) diagnostic lens 是 post-hoc
  reframing 缺乏 prospective validation。GSM8K negative correlation 被解读为 DIF=ability proxy。
  HellaSwag/GSM8K 的低 C% 与 MMLU 的高 C% 差异被质疑为 method artifact（item count / domain structure 驱动）。
  Reframe 方向：permutation calibration methodology 本身升格为 contribution，semi-synthetic framework
  作为 primary，empirical atlas 作为 resource，headline 从 '31% instability' 改为 'permutation-calibrated
  15–23% genuine instability + calibration methodology for future DIF studies'。仍冲 EMNLP long paper
  但需 camera-ready 前补 propensity-score matching 或 MIMIC model。

imagined_experiments:
  - name: real_data_dif_mmlu
    plan_id: plan_001
    description: >
      METABENCH MMLU 5,219×12,508 response matrix 上的 MH-DIF，temporal/ability/within-family
      cohort 对比 + Li et al. proxy validation + domain-specificity。
    expected_results:
      temporal_ets_c_pct: 31.3
      temporal_fpr_li_clean: 0.321
      temporal_enrichment: 0.96
      ability_ets_c_pct: 2.9
      ability_enrichment: 1.19
      within_family_llama2v3_c_pct: 61.3
      within_family_mistral_mixtral_c_pct: 38.7
      domain_spearman_rho: 0.36
      domain_spearman_p: 0.006
      sanity_random_split_c_pct: 0.18
      temporal_ability_jaccard: 0.014
      n_subjects_with_nonzero_c: 57
      subject_c_range: "20.7–48.4%"
    result_rationale: >
      Raw numbers 与 registry 一致（plan_001 已完成），但在 worst 档下这些数字被后续实验重新解读：
      31.3% 中有 8–18pp 来自 temporal structure（plan_029 permutation null），domain ρ=0.36（略高于
      registry 的 0.307）意味着 domain-level ability improvement 的解释力比预期更强。
      Llama-2v3 C%=61.3% 被 reviewer 用作 'DIF captures ability gap' 的直接证据——d=-0.99 的
      cohort 产生 61.3% C%，d=-0.17 产生 31.3%，线性外推 d=0 时 C%≈25%，与 permutation null
      上界吻合。enrichment≈1.0 仍然成立但对 reviewer 来说是 'DIF 与 contamination 无关' 的证据
      而非 'web labels 不适用' 的证据——framing battle 在 worst 档下输给 reviewer。
    tables:
      - name: "Table 1: Temporal DIF Summary by Cohort Definition"
        rows:
          - cohort: temporal_2023v2024
            n_ref: 1080
            n_foc: 807
            c_pct: 31.3
            enrichment: 0.96
            permutation_null_c_pct: "12.4 (worst-tier midpoint)"
            genuine_c_pct: "~18.9"
          - cohort: ability_quintile
            n_ref: 1044
            n_foc: 1044
            c_pct: 2.9
            enrichment: 1.19
            permutation_null_c_pct: 0.21
            genuine_c_pct: "~2.7"
          - cohort: within_family_llama2v3
            n_ref: 161
            n_foc: 308
            c_pct: 61.3
            enrichment: null
            permutation_null_c_pct: "38.2"
            genuine_c_pct: "~23.1"
      - name: "Table 2: Domain-Specificity Top/Bottom 5 Subjects"
        note: "C% range 20.7–48.4%, ρ=0.36 with domain accuracy Δ"
    figures_description:
      - "Fig 1: C% histogram across 57 MMLU subjects, colored by domain accuracy Δ quartile — worst 档下 top-quartile accuracy-Δ subjects 明显偏高 C%，ρ=0.36 可视化为斜向聚集"
    analysis: >
      plan_001 的 raw output 在 worst 档下不变，但 interpretive frame 被 plan_029 的 permutation
      null 彻底重写。31.3% 不再是 headline——permutation-calibrated 的 ~19% 才是。domain ρ=0.36
      虽然 item-level R²仍低（0.0007），但 reviewer 会 argue ecological correlation 足以
      cast doubt。within-family Llama-2v3 的 61.3% 成为 ability confound 的 poster child。

  - name: rl_robustness_validation
    plan_id: plan_002
    description: >
      验证 DIF 对 reasoning-RL 模型的鲁棒性：SFT baseline + alignment-RL (N=477) +
      10-15 reasoning-RL models mixed into focal cohort。
    expected_results:
      sft_baseline_c_pct: 30.8
      alignment_rl_cohort_c_pct: 31.1
      reasoning_rl_mixed_c_pct: 30.5
      dif_retention_jaccard_sft_vs_rl_mixed: 0.82
      constat_auroc_on_rl_models: 0.58
      mink_auroc_on_rl_models: 0.54
      delong_p_dif_vs_constat: 0.34
      tost_equivalence_p: 0.18
      bootstrap_ci_dif_retention: [0.74, 0.89]
      n_reasoning_rl_models: 13
      n_total_focal_with_rl: 820
    result_rationale: >
      N=13 reasoning-RL 模型混入 N=807 focal cohort 后 total N=820，DIF 作为 group-level
      方法对 13 个模型的加入不敏感（C% 从 31.3 微降至 30.5）。但这恰恰是问题：reviewer 指出
      13/820=1.6% 的混入比例根本无法测试 robustness——即使 RL 模型完全破坏 DIF 信号，
      1.6% 的权重也会被 group statistic 淹没。TOST equivalence test p=0.18 不显著，
      无法声称等价。DeLong test p=0.34 也不显著，但这是因为 power 不足而非真正等价。
      ConStat/MinK 在 RL 模型上的 AUROC 降至 0.54-0.58（接近随机），但 N=13 的 CI 极宽，
      任何比较都 underpowered。整个实验在 worst 档下被 reviewer 一致判定为 underpowered
      且设计上无法回答其声称要回答的问题。移入 appendix 作为 preliminary evidence。
    tables:
      - name: "Table: DIF Retention Under Cohort Composition Variation"
        rows:
          - condition: SFT-only focal
            n_focal: 412
            c_pct: 30.8
            jaccard_vs_baseline: 0.87
          - condition: Alignment-RL focal
            n_focal: 477
            c_pct: 31.1
            jaccard_vs_baseline: 0.89
          - condition: Reasoning-RL mixed
            n_focal: 820
            c_pct: 30.5
            jaccard_vs_baseline: 0.82
    figures_description:
      - "Fig: AUROC comparison (DIF group-level vs ConStat/MinK per-model) on 13 RL models — wide bootstrap CIs overlapping random baseline"
    analysis: >
      Worst 档下这个实验是 paper 的 liability 而非 asset。N=13 的 reasoning-RL sample
      使任何统计声明都不可信。Reviewer 会指出：(a) 1.6% 混入比例是 trivial perturbation，
      (b) 缺乏 GRPO/PPO 模型的 MMLU response data 是 data limitation 而非 DIF limitation，
      (c) 'DIF is group-level so it doesn't need N≥80 RL' 的 argument 回避了真正的问题。
      建议：从 main body 移除，appendix 中报告为 'preliminary with acknowledged power limitation'。

  - name: constat_perturbation_eval
    plan_id: plan_003a
    description: >
      ConStat-style perturbation测试：200+ MMLU items 的 LLM paraphrase + FDR-controlled detection。
    expected_results:
      n_items_paraphrased: 240
      constat_detection_rate_non_rl: 0.23
      constat_detection_rate_rl: 0.07
      constat_fdr_controlled_fpr: 0.08
      constat_dif_overlap_jaccard: 0.11
      paraphrase_semantic_similarity: 0.91
      gpu_hours_used: 72
      n_models_tested: 50
    result_rationale: >
      ConStat 在 non-RL 模型上检测率 23%（中等），但在 RL 模型上暴跌至 7%——符合理论预期
      但 N=240 items × 50 models 的规模使 CI 宽。与 DIF flags 的 Jaccard=0.11 极低，
      意味着两种方法检测不同维度的 instability。在 worst 档下，reviewer 将此解读为
      '两种方法都不可靠' 而非 '互补覆盖'。paraphrase quality（similarity=0.91）被质疑
      为不够 semantically equivalent——任何 detection 可能是 paraphrase artifact。
      80 GPU hours 的投入产出比在 worst 档下被认为不值得放入 main body。
    tables: []
    figures_description:
      - "Fig: ConStat detection rate vs DIF C-flag rate per subject, showing near-zero correlation"
    analysis: >
      ConStat 独立结果在 worst 档下价值有限：detection rate 低且与 DIF 正交。
      如果 reviewer 已经质疑 DIF 的 31% 是 inflated，ConStat 的 23% 也面临同样的
      calibration 问题（没有 permutation null）。实验本身 clean 但不 strengthen paper。
      建议：appendix baseline comparison，不作为 contribution。

  - name: dvd_generation_variance_eval
    plan_id: plan_003b
    description: >
      DVD generation variance：10-15 open-weight 模型 × 50 responses/item × temperature sampling。
    expected_results:
      n_models: 12
      n_items: 500
      responses_per_item: 50
      dvd_bimodal_detection_rate: 0.14
      dvd_verbatim_detection_power: 0.09
      dvd_variant_detection_power: 0.31
      dvd_fpr: 0.12
      gpu_hours_used: 65
      dvd_dif_overlap_jaccard: 0.06
    result_rationale: >
      DVD 设计用于 variant contamination（模型见过 paraphrase 而非原题），对 verbatim
      contamination 的检测力极低（0.09）。Bimodal distribution 在 temperature=0.7-1.0
      下确实出现但 only 14% 的 items——大部分 contaminated items 不产生 bimodal variance
      因为 LLM 在 high temperature 下的 stochasticity 掩盖了 memorization signal。
      与 DIF 的 Jaccard=0.06 接近零：两种方法在 item-level 上几乎完全不重叠。
      在 worst 档下，70 GPU hours 产出一个 near-null result，reviewer 认为 DVD
      evaluation 与 paper 的 temporal DIF 主线无关。
    tables: []
    figures_description:
      - "Fig: Bimodal score distribution example for 3 items — showing weak signal"
    analysis: >
      DVD 在 worst 档下是 sunk cost。Detection power 不足以作为 standalone baseline，
      与 DIF 的互补性接近零。Reviewer 质疑为什么在 temporal DIF paper 中评估 generation
      variance method。建议：完全 drop，不进 appendix。

  - name: ensemble_fusion
    plan_id: plan_003c
    description: >
      DIF + ConStat + DVD 三信号融合：majority voting + weighted fusion + cross-validation。
    expected_results:
      ensemble_not_executed: true
      reason: "upstream signal quality insufficient for meaningful fusion"
      constat_weak: true
      dvd_near_null: true
      projected_2of3_tpr: 0.15
      projected_2of3_fpr: 0.06
      decision: "killed — degrade to appendix note"
    result_rationale: >
      ConStat detection rate=23% 和 DVD detection rate=14% 均低于 DIF 的 31.3%，
      且三者 pairwise Jaccard 均<0.12。2-of-3 majority voting 的 TPR 暴跌至 ~15%
      因为 agreement 极低——三种方法检测的是不同 item populations。Weighted fusion
      可能略好但 cross-validation 在 N=240 items 上 overfit 风险高。在 worst 档下
      ensemble 从未执行（per paper_framing: 'plan_003a/b/c never executed'），
      这一决策被 worst 档的 upstream results 证明正确。
    tables: []
    figures_description: []
    analysis: >
      Ensemble 在 worst 档下正确地被 kill。upstream 信号质量不足、方法间 overlap 极低、
      fusion 没有理论基础（不是 'same signal different noise' 而是 'different signals'）。
      Paper framing 中已标记为 'Future work'。

  - name: cross_benchmark_gsm8k
    plan_id: plan_004
    description: >
      GSM8K temporal DIF + GSM1K ground truth correlation + semi-synthetic validation。
    expected_results:
      step1_gsm8k_temporal_c_pct: 18.9
      step1_external_c_pct: 47.4
      step1_sanity_c_pct: 0.3
      step2_standard_delta_tpr_p10: 0.818
      step2_external_delta_tpr_p10: 0.517
      step2_standard_delta_tpr_p05: 0.32
      step3_pearson_r: -0.478
      step3_pearson_p: 0.005
      step3_spearman_rho: -0.403
      step3_n_models: 33
      step3_ci_r: [-0.71, -0.16]
      step3_ci_rho: [-0.66, -0.03]
      permutation_null_gsm8k_c_pct: 9.2
      genuine_c_pct_after_calibration: 9.7
    result_rationale: >
      GSM8K C%=18.9% 在 permutation calibration 后降至 ~9.7%（null=9.2%），远低于 MMLU
      calibrated ~19%。Reviewer 质疑：如果 permutation null 已经解释了一半的 GSM8K C%，
      genuine instability 可能微不足道。Step 3 的 negative correlation (r=-0.478) 是
      worst 档的核心问题——reviewer 解读为 'DIF flags items where 2024 models improved
      most, and GSM1K gap shrinks for these models because improvement is genuine
      (not contamination)'。即 DIF 不是在检测 instability 而是在检测 ability improvement。
      ΔTPR at p=0.5 降至 0.32（worst 档范围内），semi-synthetic 仍然 work 但 power
      reduction 明显。N=33 使所有 correlation 的 CI 宽到包含 near-zero effect。
    tables:
      - name: "Table: GSM8K DIF Summary with Permutation Calibration"
        rows:
          - metric: raw_c_pct
            value: 18.9
          - metric: permutation_null_c_pct
            value: 9.2
          - metric: calibrated_genuine_c_pct
            value: 9.7
          - metric: gsm1k_correlation_r
            value: -0.478
          - metric: gsm1k_correlation_ci
            value: "[-0.71, -0.16]"
    figures_description:
      - "Fig: Scatter plot of DIF-C item proportion vs GSM1K gap (N=33 models) — negative trend with wide CI band, annotated Deepseek-math-7b-rl as potential outlier"
    analysis: >
      GSM8K 在 worst 档下是 double-edged：semi-synthetic ΔTPR=0.818（p=1.0）证明
      framework portability，但 GSM1K negative correlation 被 reviewer 武器化为
      'DIF = ability proxy' 的证据。Permutation calibration 将 genuine C% 压至 ~10%，
      further weakening the instability narrative。Paper 必须将 GSM1K correlation
      从 'contamination validation' 完全 pivot 到 'exploratory/anomalous finding
      requiring further investigation'。N=33 的 limitation 必须 prominent display。

  - name: bifactor_irt_equating_pilot
    plan_id: plan_005
    description: >
      MMLU 57-subject bifactor IRT model + anchor item selection + fixed-parameter calibration。
    expected_results:
      bifactor_convergence: false
      attempted_subjects: 57
      converged_subjects: 23
      rmsea_converged: 0.089
      cfi_converged: 0.74
      tli_converged: 0.71
      anchor_items_selected: 0
      equating_completed: false
      killed: true
      kill_reason: "bifactor non-convergence on 34/57 subjects; converged subjects show poor fit"
    result_rationale: >
      57-subject MMLU 的 bifactor model 在 worst 档下无法收敛——items per subject 从
      18（formal_logic）到 1534（miscellaneous），subject-specific factors 的 sample
      size 极不均衡。即使 converged subjects（23/57）的 fit 也差（RMSEA=0.089, CFI=0.74），
      因为 MMLU items 不满足 unidimensional within-subject assumption（moral_scenarios
      Q3=34.2% above 0.20）。没有 reliable bifactor model 就没有 anchor items，
      equating pipeline 无法启动。这与 registry 中 plan_015 被 killed 一致。
      在 worst 档下，这不仅是 technical failure 而是 structural impossibility——
      MMLU 的 multidimensionality 从根本上不适合 bifactor parameterization。
    tables: []
    figures_description: []
    analysis: >
      Bifactor failure 在 worst 档下被 reviewer 用作两面攻击：(1) 'if bifactor fails,
      your MH-DIF conditioning on total score is even more misspecified'，(2) 'you
      acknowledge multidimensionality but use a unidimensional method'。Defense：
      MH conditions on observed total score（nonparametric），不依赖 IRT model fit。
      但 reviewer 不一定接受这个区分。建议：limitations 中 prominently acknowledge，
      frame as motivation for future multidimensional DIF work。

  - name: item_generation_calibration
    plan_id: plan_006
    description: >
      LLM-generated replacement items for DIF-flagged questions + student simulation calibration。
    expected_results:
      n_items_generated: 300
      difficulty_correlation_prompt: 0.18
      difficulty_correlation_simulation: 0.62
      difficulty_correlation_empirical: 0.48
      subject_match_rate: 0.83
      cognitive_level_match_rate: 0.61
      holdout_model_panel_rho: 0.72
      gpu_hours_used: 180
      item_quality_pass_rate: 0.41
    result_rationale: >
      Item generation 在 worst 档下的核心问题是 calibration accuracy：prompt-based
      difficulty targeting 仍然差（ρ=0.18），student simulation 改善至 0.62 但不及
      arXiv 报告的 0.75-0.82 因为 MMLU 的 57-subject diversity 使 simulation 泛化差。
      Empirical calibration（在 holdout models 上测试）降至 0.48，因为 LLM-generated
      items 的 discrimination 系统性偏低（生成的 items 倾向于 either too easy or 随机
      difficulty）。41% 的 quality pass rate 意味着 300 items 中只有 ~123 可用。
      Cognitive level matching 只有 61% 因为 MMLU 本身没有 explicit cognitive level
      labels。在 worst 档下，reviewer 认为 item generation 是 tangential to paper's
      contribution 且 execution quality 不足以支撑任何 claim。
    tables: []
    figures_description:
      - "Fig: Difficulty calibration scatter — generated vs empirical, showing systematic underestimation of hard items"
    analysis: >
      Item generation 在 worst 档下应完全 drop from paper。ρ=0.48 的 empirical
      calibration + 41% pass rate 不构成 contribution。且 paper 已 pivot away from
      'regeneration' toward 'diagnostic lens'，generation 不 serve the narrative。
      180 GPU hours sunk cost。

  - name: cumulative_bayesian_dif
    plan_id: plan_007
    description: >
      Sinharay et al. (2006) cumulative Bayesian DIF priors across 4 simulated administrations。
    expected_results:
      single_admin_power_d10: 0.38
      cumulative_2_admin_power_d10: 0.52
      cumulative_3_admin_power_d10: 0.61
      cumulative_4_admin_power_d10: 0.67
      target_power_0_70_reached: false
      single_admin_power_d14: 0.59
      cumulative_3_admin_power_d14: 0.74
      fpr_cumulative: 0.055
      prior_specification_sensitivity: "moderate — informative vs diffuse prior changes power by ±0.08"
    result_rationale: >
      Cumulative power 在 worst 档下不达标（0.67 < 0.70 at δ=1.0 after 4 admins），
      因为 simulation 使用 realistic parameters（not optimistic）：inter-administration
      correlation of DIF effects < 1.0（items 的 DIF 在不同时间点不完全一致），
      prior-posterior updating efficiency 受 small N per administration 限制。
      Prior specification sensitivity ±0.08 意味着结果对分析选择敏感。
      Reviewer 认为：(a) simulation-only 没有 empirical grounding，(b) 4 administrations
      是假设性的（METABENCH 只有 1 snapshot），(c) power improvement 从 0.38 到 0.67
      modest且 costly（需要 4× data）。
    tables:
      - name: "Table: Cumulative Power by Administration Count"
        rows:
          - admins: 1
            power_d10: 0.38
            power_d14: 0.59
          - admins: 2
            power_d10: 0.52
            power_d14: 0.68
          - admins: 3
            power_d10: 0.61
            power_d14: 0.74
          - admins: 4
            power_d10: 0.67
            power_d14: 0.78
    figures_description:
      - "Fig: Power accumulation curves at δ=1.0 and δ=1.4, with 70% threshold line — δ=1.0 never crosses"
    analysis: >
      Simulation-only experiment 在 worst 档下是 appendix material。不达 0.70 target
      at δ=1.0 是 honest result 但 weakens the 'DIF is practical' narrative。
      Reviewer：'if you need 4 benchmark snapshots to detect medium effects, the method
      is impractical for real-time monitoring.' 建议：brief mention in future work，
      不进 main body。

  - name: graceful_degradation_analysis
    plan_id: plan_008
    description: >
      Progressive item replacement (5%-50%) 下 validity degradation 的理论 + 实证分析。
    expected_results:
      rho_5pct_replacement: 0.998
      rho_10pct_replacement: 0.995
      rho_20pct_replacement: 0.987
      rho_50pct_replacement: 0.962
      reliability_alpha_full: 0.94
      reliability_alpha_50pct_replaced: 0.88
      construct_coverage_50pct: 0.79
      degradation_rate: "non-linear — accelerates after 30%"
      theoretical_bound_violation_at: "42% replacement"
    result_rationale: >
      Graceful degradation 在 worst 档下呈现 non-linear cliff：前 20% replacement
      几乎无影响（ρ=0.987），但 30%+ 后加速恶化，50% 时 reliability 降至 0.88（acceptable
      但 approaching concern），construct coverage 降至 0.79。问题是：31% 的 DIF items
      恰好落在 cliff 的起始区域——如果要 replace 所有 flagged items，degradation 开始
      加速。Reviewer 会 point out：'your own analysis shows that replacing 31% of items
      causes non-trivial degradation, undermining the regeneration rationale.'
      但 paper 已 pivot away from regeneration，所以这个 concern 被 defused。
      不过 worst 档下 reviewer 仍然 raise it as internal inconsistency。
    tables:
      - name: "Table: Validity Metrics Under Progressive Replacement"
        rows:
          - pct_replaced: 5
            rho: 0.998
            alpha: 0.935
            coverage: 0.97
          - pct_replaced: 10
            rho: 0.995
            alpha: 0.928
            coverage: 0.95
          - pct_replaced: 20
            rho: 0.987
            alpha: 0.912
            coverage: 0.91
          - pct_replaced: 50
            rho: 0.962
            alpha: 0.880
            coverage: 0.79
    figures_description:
      - "Fig: Degradation curves for ρ, α, coverage — showing non-linear cliff around 30%"
    analysis: >
      Graceful degradation 在 worst 档下是 supplementary material。Non-linear cliff
      at ~30% 是 interesting finding 但与 reframed narrative（diagnostic lens, not
      replacement protocol）的关系 tangential。建议：appendix 中报告，main body 中
      一句话引用 'replacement beyond 30% shows accelerating degradation'。

  - name: item_focused_trees
    plan_id: plan_009
    description: >
      Tutz & Berger (2016) IFT：release date 作为 continuous covariate 的 DIF 检测。
    expected_results:
      ift_c_pct_continuous: 27.4
      ift_mh_concordance: 0.78
      ift_detects_gradual_drift: true
      n_items_gradual_not_abrupt: 1840
      pct_gradual: 47.0
      ift_vs_mh_power_ratio: 0.92
      computation_time_hours: 8.2
    result_rationale: >
      IFT 在 worst 档下揭示一个 uncomfortable truth：47% 的 DIF items 展示的是
      gradual temporal drift 而非 abrupt cohort shift。这意味着 MH 的 binary temporal
      split (2023 vs 2024) 人为地将 continuous process discretize——reviewer 质疑
      为什么不直接用 IFT。IFT concordance with MH = 0.78（不够高），IFT C%=27.4%
      vs MH 31.3%——差异来自 IFT 对 gradual drift 的不同 classification。
      IFT 的 power ratio=0.92（vs MH）表明 continuous approach 没有 power advantage，
      反而 computational cost 高 8×。但 reviewer 的 concern 不是 power 而是 validity：
      'if drift is gradual, your cohort-based framework is misspecified.'
    tables:
      - name: "Table: IFT vs MH Detection Comparison"
        rows:
          - method: MH categorical
            c_pct: 31.3
            computation_hours: 1.0
            gradual_detection: "no"
          - method: IFT continuous
            c_pct: 27.4
            computation_hours: 8.2
            gradual_detection: "yes (47% gradual)"
    figures_description:
      - "Fig: Example items showing gradual vs abrupt DIF trajectories — IFT captures both, MH only captures abrupt"
    analysis: >
      IFT 在 worst 档下是 challenging but informative robustness check。47% gradual
      drift 的 finding 如果放在 main body 会 undermine categorical DIF framework。
      但如果放在 appendix 作为 'MH is conservative approximation of continuous drift'
      的 evidence，可以 strengthen 而非 weaken the paper。关键 framing：'MH detects
      the 53% of items with abrupt changes + partially detects the 47% with gradual
      drift — our 31% is a lower bound on items with ANY temporal instability.'
      这需要 careful writing 但在 worst 档下是 feasible defense。

  - name: architecture_stratified_dif
    plan_id: plan_010
    description: >
      Decoder-only subpopulation DIF + IRT fit diagnostics。
    expected_results:
      n_decoder_only: 5226
      n_non_decoder: 1
      pct_decoder_only: 99.98
      decoder_only_c_pct: 31.3
      full_population_c_pct: 31.3
      jaccard_decoder_vs_full: 1.0
      rmsea_decoder_only: 0.048
      cfi_decoder_only: 0.71
      tli_decoder_only: 0.68
      srmr_decoder_only: 0.052
      irt_fit_improved: false
    result_rationale: >
      METABENCH MMLU 是 99.98% decoder-only（5226/5227），移除 1 个 non-decoder 模型
      改变 nothing（Jaccard=1.0, C% identical）。IRT fit diagnostics 在 worst 档下
      仍然差（CFI=0.71, TLI=0.68, 远低于 0.90 threshold），因为 fit 问题不是
      architecture heterogeneity 而是 57-subject multidimensionality。
      这个实验在 worst 档下的结论是：architecture 不是 confounder（positive），
      但 IRT misfit 是 fundamental（negative）。Reviewer：'you've shown architecture
      isn't the problem, but the IRT fit is still terrible — what IS the problem?'
      Answer：multidimensionality。但 MH 不依赖 IRT fit——这个 distinction 需要
      in paper 但 reviewer 可能不接受。
    tables:
      - name: "Table: IRT Fit Diagnostics"
        rows:
          - population: full (N=5227)
            rmsea: 0.049
            cfi: 0.71
            tli: 0.68
          - population: decoder-only (N=5226)
            rmsea: 0.048
            cfi: 0.71
            tli: 0.68
    figures_description: []
    analysis: >
      Architecture stratification 在 worst 档下是 trivial experiment（99.98% homogeneous）。
      Positive finding（architecture not confounding）但不增加 persuasive value
      因为 reviewer 已经知道 METABENCH is decoder-only dominant。IRT fit diagnostics
      反而打开 'misspecification' attack surface。建议：report in one sentence +
      footnote，不做 major experiment。IRT fit numbers 放 appendix 如果 reviewer 问起。

  - name: semi_synthetic_contamination_validation
    plan_id: plan_011
    description: >
      Known contamination injection into real METABENCH response matrix + DIF detection power。
    expected_results:
      temporal_external_tpr_p0: 0.326
      temporal_external_tpr_p03: 0.42
      temporal_external_tpr_p05: 0.58
      temporal_external_tpr_p07: 0.81
      temporal_external_tpr_p10: 0.95
      temporal_external_fpr: 0.318
      temporal_external_delta_tpr_p05: 0.254
      temporal_external_delta_tpr_p10: 0.624
      cross_subject_delta_fpr_p05: 0.012
      cross_subject_delta_fpr_p10: 0.018
      within_subject_fpr_inflation_p10: 0.196
      matching_variable_contamination: true
      n_clean_items: 500
      n_injected_items: 150
    result_rationale: >
      Worst 档下 semi-synthetic 的核心退化在两处：(1) ΔTPR at p=0.5 从 registry 的 0.508
      降至 0.254——因为 permutation null 的存在意味着 baseline FPR 已经 high（0.318），
      injection 需要在 already-noisy background 上增加 signal。实际上 0.254 仍然 >0
      证明 DIF 能检测 injected contamination，但 reviewer 认为 power 不足以 claim
      'practical detection capability'。(2) Cross-subject matching 的 ΔFPR 不再是
      0.000 而是 0.012-0.018——permutation 分析揭示 cross-subject total score 与
      temporal cohort membership 有 residual correlation through latent dimensions
      that cross-subject matching 未完全消除。0.012 仍然很低但不再是 'provable FPR
      control' 的 zero。这对 Claim 3 的 framing 有 material impact：从 'ΔFPR=0.000'
      改为 'ΔFPR<0.02, near-zero FPR inflation'。Within-subject matching 的 FPR
      inflation 确认（0.196），strengthening the cross-subject recommendation。
    tables:
      - name: "Table: Semi-Synthetic Detection Power (Worst Tier)"
        rows:
          - injection_p: 0.0
            tpr: 0.326
            fpr: 0.318
            delta_tpr: 0.0
          - injection_p: 0.3
            tpr: 0.42
            fpr: 0.319
            delta_tpr: 0.094
          - injection_p: 0.5
            tpr: 0.58
            fpr: 0.330
            delta_tpr: 0.254
          - injection_p: 0.7
            tpr: 0.81
            fpr: 0.331
            delta_tpr: 0.484
          - injection_p: 1.0
            tpr: 0.95
            fpr: 0.336
            delta_tpr: 0.624
      - name: "Table: Cross-Subject vs Within-Subject Matching FPR"
        rows:
          - matching: cross-subject
            delta_fpr_p05: 0.012
            delta_fpr_p10: 0.018
          - matching: within-subject
            delta_fpr_p05: 0.098
            delta_fpr_p10: 0.196
    figures_description:
      - "Fig: ΔTPR dose-response curve at p=0.3 to 1.0 — monotone increasing but shifted down from registry values"
      - "Fig: ΔFPR comparison: cross-subject (near-zero but nonzero) vs within-subject (substantial inflation)"
    analysis: >
      Semi-synthetic 在 worst 档下仍然是 paper 最强的 methodological contribution，但需要
      recalibrate claims。ΔFPR=0.012 而非 0.000 意味着 'provable FPR control' 改为
      'near-zero FPR inflation (<2%)'——仍然是 strong practical recommendation 但
      theoretical cleanness 下降。ΔTPR=0.254 at p=0.5 仍然 statistically significant
      但 reviewer 会 argue 'detection power 太低 for practical use below p=0.7'。
      Key defense：semi-synthetic framework 的 value 在于 methodology（reusable for
      any detector），不在于 specific power numbers。Cross-subject matching insight
      独立于 DIF magnitude，是 genuine contribution。

  - name: multi_benchmark_temporal_dif
    plan_id: plan_028
    description: >
      6 benchmarks（MMLU, WinoGrande, TruthfulQA, ARC, GSM8K, HellaSwag）temporal DIF atlas。
    expected_results:
      mmlu_c_pct: 31.3
      mmlu_permutation_null: 14.2
      mmlu_calibrated: 17.1
      winogrande_c_pct: 30.3
      winogrande_permutation_null: 16.8
      winogrande_calibrated: 13.5
      truthfulqa_c_pct: 29.7
      truthfulqa_permutation_null: 15.1
      truthfulqa_calibrated: 14.6
      arc_c_pct: 26.9
      arc_permutation_null: 12.3
      arc_calibrated: 14.6
      gsm8k_c_pct: 18.9
      gsm8k_permutation_null: 9.2
      gsm8k_calibrated: 9.7
      hellaswag_c_pct: 17.9
      hellaswag_permutation_null: 10.6
      hellaswag_calibrated: 7.3
      cross_benchmark_raw_range: "17.9–31.3%"
      cross_benchmark_calibrated_range: "7.3–17.1%"
      all_random_controls_below_1pct: true
      spearman_raw_vs_calibrated: 0.886
      n_items_correlation_with_c_pct: 0.72
    result_rationale: >
      Permutation calibration 后的 cross-benchmark range 从 17.9–31.3% 缩至 7.3–17.1%。
      关键问题：HellaSwag calibrated=7.3% 和 GSM8K calibrated=9.7% 接近 'trivial' 水平，
      reviewer 会质疑这些 benchmark 上的 instability 是否 meaningful。MMLU 仍最高
      （17.1%）但不再 dramatic。Reviewer concern：n_items 与 C% 的 correlation=0.72 暗示
      larger benchmarks 产生 more DIF 可能是 statistical artifact（more items = more
      chances for stochastic DIF flags）。虽然 permutation null 应该 calibrate 这个
      away，但 HellaSwag（10042 items）的 null=10.6% 远高于 ARC（1172 items, null=12.3%）
      ——relationship 不是 monotone，但 reviewer 仍然质疑。WinoGrande 和 TruthfulQA
      的 calibrated C% 居中（13.5-14.6%），ARC 也类似（14.6%）。All random controls
      <1% 证明 temporal structure 是真实的——但 'temporal structure ≠ item instability'
      在 worst 档下是 reviewer 的核心攻击。
    tables:
      - name: "Table: Multi-Benchmark Temporal DIF Atlas (Raw vs Calibrated)"
        rows:
          - benchmark: MMLU
            n_items: 12508
            raw_c_pct: 31.3
            permutation_null: 14.2
            calibrated_c_pct: 17.1
            random_control: 0.18
          - benchmark: WinoGrande
            n_items: 1267
            raw_c_pct: 30.3
            permutation_null: 16.8
            calibrated_c_pct: 13.5
            random_control: 0.32
          - benchmark: TruthfulQA
            n_items: 817
            raw_c_pct: 29.7
            permutation_null: 15.1
            calibrated_c_pct: 14.6
            random_control: 0.37
          - benchmark: ARC
            n_items: 1172
            raw_c_pct: 26.9
            permutation_null: 12.3
            calibrated_c_pct: 14.6
            random_control: 0.60
          - benchmark: GSM8K
            n_items: 1319
            raw_c_pct: 18.9
            permutation_null: 9.2
            calibrated_c_pct: 9.7
            random_control: 0.30
          - benchmark: HellaSwag
            n_items: 10042
            raw_c_pct: 17.9
            permutation_null: 10.6
            calibrated_c_pct: 7.3
            random_control: 0.28
    figures_description:
      - "Fig: Bar chart of raw C% vs calibrated C% across 6 benchmarks, with permutation null as shaded band — visual impact of calibration is dramatic"
      - "Fig: Calibrated C% vs benchmark n_items scatter — testing the 'more items = more DIF' artifact hypothesis"
    analysis: >
      Multi-benchmark atlas 在 worst 档下的 reframe value 很高：permutation calibration
      across 6 benchmarks 是 genuine methodological contribution（'establishing calibration
      requirements for future LLM DIF studies'）。Calibrated range 7.3–17.1% 仍然
      2–3× above random controls，supporting 'genuine instability exists'。但 headline
      impact 大幅下降——'7% of HellaSwag items show genuine temporal instability' 不够
      exciting for EMNLP long paper opening。Defense：atlas 作为 empirical resource
      而非 single-number claim。Cross-benchmark variation itself 是 finding：
      'benchmarks differ 2.3× in genuine instability rate, suggesting domain-specific
      temporal dynamics' 是 legitimate contribution。

  - name: permutation_null_c_rate
    plan_id: plan_029
    description: >
      1000× permutation test：随机重分配 temporal labels，建立 C% null distribution。
    expected_results:
      n_permutations: 1000
      null_c_pct_mean: 12.4
      null_c_pct_sd: 1.8
      null_c_pct_95ci: [9.1, 16.2]
      null_c_pct_p025: 9.3
      null_c_pct_p975: 16.1
      observed_c_pct: 31.3
      z_score_vs_null: 10.5
      empirical_p_value: 0.0
      genuine_excess_c_pct: 18.9
      pct_inflation_explained: 39.6
      ability_gap_in_permuted: "mean d=0.001, sd=0.052"
      temporal_structure_components:
        release_date_clustering: "contributes ~7pp to null"
        training_data_overlap: "contributes ~3pp to null"
        residual_cohort_structure: "contributes ~2.4pp to null"
    result_rationale: >
      Permutation null C%=12.4%（CI 9.1–16.2%）揭示 temporal cohort 赋值本身带入
      substantial structure：即使在 random relabeling 下，2023 和 2024 cohort 的
      model composition 差异（不同 family 分布、不同 training data vintage）仍然
      产生 ~12% DIF。这不是 ability confound（permuted d≈0.001）而是 temporal structure
      confound：模型的 release date、training data composition、architecture generations
      在 temporal cohort 间不均匀分布。31.3% - 12.4% = 18.9% genuine excess，但
      reviewer 会 argue (a) 18.9% 远不如 31.3% dramatic，(b) 12.4% null 本身说明
      MH-DIF 对 temporal structure 过度敏感，(c) 'genuine excess' 的定义依赖于
      'permutation null is the correct null'——如果 temporal structure IS the confound
      of interest（not something to subtract），那么应该 subtract 更少。
      z=10.5 证明 31.3% 显著高于 null（p<0.001），但 reviewer 的 concern 不是
      significance 而是 magnitude：'significant ≠ important.'
    tables:
      - name: "Table: Permutation Null Distribution"
        rows:
          - statistic: observed_c_pct
            value: 31.3
          - statistic: null_mean
            value: 12.4
          - statistic: null_sd
            value: 1.8
          - statistic: null_95ci
            value: "[9.1, 16.2]"
          - statistic: z_score
            value: 10.5
          - statistic: genuine_excess
            value: 18.9
          - statistic: pct_explained_by_structure
            value: "39.6%"
    figures_description:
      - "Fig: Permutation null histogram (1000×) with observed C%=31.3% as vertical line — clearly right of distribution but distribution itself centered at ~12%"
      - "Fig: Null distribution decomposition — stacked contributions from release clustering, training overlap, residual"
    analysis: >
      Permutation null 是 worst 档的 pivotal experiment。C%=12.4% null 意味着
      naive DIF inflation 约 40%。这 simultaneously (a) weakens the 31% headline
      和 (b) creates a new contribution：'permutation calibration reveals substantial
      temporal structure inflation in LLM DIF studies — future work must calibrate.'
      Paper 的 reframe 核心在这里：permutation null 从 threat 变成 finding。
      'Temporal cohort structure inflates naive DIF by ~12pp' 是 a warning to the
      field，独立于 specific instability number。但要 execute 这个 reframe，paper
      需要 convincingly argue 为什么 12.4% null 本身 interesting 而非 damning。
      Defense：'all prior benchmark evaluation studies using temporal splits face
      this inflation — we are the first to quantify and correct for it.'

  - name: odds_ratio_regression_transparency
    plan_id: plan_030
    description: >
      Odds ratio + multi-R² + deviance + item-level vs domain-level accuracy change models。
    expected_results:
      model1_domain_mcfadden_r2: 0.0007
      model1_domain_nagelkerke_r2: 0.0012
      model1_domain_or_per_010: 1.55
      model1_ci: [1.19, 2.03]
      model2_item_props_mcfadden_r2: 0.0523
      model2_item_props_nagelkerke_r2: 0.0890
      model3_item_delta_mcfadden_r2: 0.0018
      model3_item_delta_or_per_010: 1.12
      model3_ci: [1.02, 1.23]
      model4_full_mcfadden_r2: 0.0545
      model4_nagelkerke_r2: 0.0924
      simpsons_paradox: true
      lr_test_m1_vs_m2_chi2: 690.2
      lr_test_m3_vs_m4_chi2: 702.1
      item_acc_change_marginal_significant: true
      item_acc_change_conditional_ns: true
      discrimination_or: 1.58
      difficulty_or: 0.74
    result_rationale: >
      Worst 档下 Model 3（item-level accuracy Δ）的 OR=1.12 per 0.10 change
      是 marginally significant（CI=[1.02, 1.23]），给 reviewer 'DIF=ability proxy'
      的 ammunition。虽然 conditional on item properties（Model 4）后 item Δ 变
      nonsignificant（Simpson's paradox confirmed），reviewer 会 argue Simpson's
      paradox 本身说明 'item difficulty 和 discrimination 是 mediators not confounders，
      so conditioning on them removes genuine ability signal, not spurious confound.'
      Nagelkerke R²=0.092 in full model 意味着 item properties 解释 ~9% variance——
      虽然低但 reviewer 认为 remaining 91% unexplained doesn't mean 'genuine instability'，
      可能是 measurement noise / unmeasured confounders。discrimination OR=1.58 意味着
      high-discrimination items 更可能被 flagged——reviewer 质疑 'DIF preferentially
      flags the best items, which is problematic for diagnostic interpretation.'
    tables:
      - name: "Table: Logistic Regression Model Comparison (Worst Tier)"
        rows:
          - model: "M1: domain Δ"
            mcfadden_r2: 0.0007
            key_or: "1.55 [1.19, 2.03]"
            interpretation: "domain improvement weakly predicts DIF"
          - model: "M2: domain Δ + item props"
            mcfadden_r2: 0.0523
            key_or: "disc=1.58, diff=0.74"
            interpretation: "item properties dominate over domain Δ"
          - model: "M3: item Δ"
            mcfadden_r2: 0.0018
            key_or: "1.12 [1.02, 1.23]"
            interpretation: "item-level change marginally significant"
          - model: "M4: item Δ + item props"
            mcfadden_r2: 0.0545
            key_or: "item Δ ns; disc=1.58"
            interpretation: "Simpson's paradox — item Δ absorbed by properties"
    figures_description:
      - "Fig: Simpson's paradox visualization — marginal vs conditional relationship between item accuracy change and DIF flag"
    analysis: >
      OR regression 在 worst 档下是 transparency contribution 但也是 attack surface。
      Reviewer 可以同时 argue (a) R²<0.10 意味着 model doesn't explain DIF，所以 DIF
      is noise 和 (b) Simpson's paradox 意味着 you're conditioning away the real signal。
      这两个 attacks 互相矛盾但 reviewer 可以 deploy both。Defense：focus on
      discrimination OR=1.58 作为 positive finding——'DIF preferentially flags items
      whose discrimination changed across cohorts, exactly what a temporal instability
      detector should do.' Simpson's paradox 解读为：'domain improvement is fully
      mediated through item-level properties, confirming that DIF operates at
      item level not domain level.'
```

<details><summary>Recorded metadata</summary>

```json
{
  "recorded_role": "assistant",
  "parentUuid": "aa05c34c-7d45-4221-b324-12ecbc220965",
  "isSidechain": false,
  "requestId": "req_011CbFjceZ8DsAtNE5QYm6N9",
  "type": "assistant",
  "uuid": "c3e419a7-298d-43bc-94ce-7f7de6f8101d",
  "userType": "external",
  "entrypoint": "sdk-cli",
  "cwd": "/home/ubuntu/.agent-ml-research-idea_gen_0520_2",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47",
  "version": "2.1.126",
  "gitBranch": "HEAD",
  "message": {
    "model": "claude-opus-4-6",
    "id": "msg_01XM7RhgcgnTaxVKmeD29VfL",
    "type": "message",
    "stop_reason": "end_turn",
    "stop_sequence": null,
    "stop_details": null,
    "usage": {
      "input_tokens": 2,
      "cache_creation_input_tokens": 21090,
      "cache_read_input_tokens": 11841,
      "output_tokens": 16706,
      "server_tool_use": {
        "web_search_requests": 0,
        "web_fetch_requests": 0
      },
      "service_tier": "standard",
      "cache_creation": {
        "ephemeral_1h_input_tokens": 21090,
        "ephemeral_5m_input_tokens": 0
      },
      "inference_geo": "",
      "iterations": [
        {
          "input_tokens": 2,
          "output_tokens": 16706,
          "cache_read_input_tokens": 11841,
          "cache_creation_input_tokens": 21090,
          "cache_creation": {
            "ephemeral_5m_input_tokens": 0,
            "ephemeral_1h_input_tokens": 21090
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
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Permutation null 暴露 temporal structure 显著 inflate DIF，ability confound 比预期严重，reviewer 一致认为贡献不足以达到 EMNLP long paper 门槛 — 需要 reframe 但不降级 venue 核心假设：['plan_…",
  "leafUuid": "c3e419a7-298d-43bc-94ce-7f7de6f8101d",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47"
}
```

---

### Runtime record

_source line 11_

```json
{
  "type": "ai-title",
  "aiTitle": "Permutation-calibrated DIF reveals genuine LLM benchmark instability",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47"
}
```

---

### Runtime record

_source line 12_

```json
{
  "type": "last-prompt",
  "lastPrompt": "你是一位经验丰富的 ML 研究者。Phase 1 已定义了 worst 档的含义：  含义：Permutation null 暴露 temporal structure 显著 inflate DIF，ability confound 比预期严重，reviewer 一致认为贡献不足以达到 EMNLP long paper 门槛 — 需要 reframe 但不降级 venue 核心假设：['plan_…",
  "leafUuid": "c3e419a7-298d-43bc-94ce-7f7de6f8101d",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47"
}
```

---

### Runtime record

_source line 13_

```json
{
  "type": "ai-title",
  "aiTitle": "Permutation-calibrated DIF reveals genuine LLM benchmark instability",
  "sessionId": "ecedaf1a-ae54-46fe-97ae-3de8dd377c47"
}
```

---
